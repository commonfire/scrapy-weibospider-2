# -*- coding: utf-8 -*-      
import re
from urllib import urlencode,quote 
from analyzer import Analyzer
from pyquery import PyQuery as pq
import urllib2

class FriendCircle:
    '''挖掘朋友圈信息 '''
    def atuser_parser(self,atuser_info_list):
        '''解析某微博@用户，返回解析列表'''
        result_list = []
        p=re.compile('@(.*?) ',re.S)
        for atuser_info in atuser_info_list:
            result_list.append({}.fromkeys(p.findall(str(atuser_info)+" "),""))
        return result_list


    def atuser_uid_parser(self,atuser_list):
        '''获取@用户对应用户昵称的用户uid'''
        analyzer = Analyzer()
        tmp_dict = {}
        for atuser_dict in atuser_list:
            if atuser_dict != []:
                for key in atuser_dict.keys():
                    if not tmp_dict.has_key(key):
                        response = urllib2.urlopen("http://s.weibo.com/user/"+quote(quote(str(key)))+"&Refer=SUer_box")  
                        total_pq = analyzer.get_html(response.read(),'script:contains("W_texta")') 
                        uid = self.get_user_uid(total_pq)
                        atuser_dict[key] = uid
                        tmp_dict[key] = uid
                    else:
                        atuser_dict[key] = tmp_dict[key]
            else:
                continue
        return atuser_list 

    def repostuser_uid_parser(self,repostuser_list):
        '''获取转发用户对应用户昵称的用户uid'''
        analyzer = Analyzer()
        repostuser_uid_list = []
        for repostuser_nickname in repostuser_list:
            if repostuser_nickname != "":
                print "!!!!!http://s.weibo.com/user/"+quote(quote(str(repostuser_nickname)))+"&Refer=SUer_box"
                response =  urllib2.urlopen("http://s.weibo.com/user/"+quote(quote(str(repostuser_nickname)))+"&Refer=SUer_box") 
                total_pq = analyzer.get_html(response.read(),'script:contains("W_texta")') 
                uid = self.get_user_uid(total_pq)
                repostuser_uid_list.append(uid)
            else:
                repostuser_uid_list.append('')
        return repostuser_uid_list


    def get_user_uid(self,total_pq):
        '''获得@用户uid'''
        tmp = total_pq("p.person_name")
        uid = pq(pq(tmp)[0]).find('a').eq(0).attr('uid')
        return uid


         
