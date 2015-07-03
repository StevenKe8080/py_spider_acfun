#-*- coding:utf-8 -*-
'''
author='stevenke'
'''

import urllib2
import re
import os
import time
from BeautifulSoup import BeautifulSoup


def create_file():
    if os.path.exists(r'a_info.txt'):
        f = open('a_info.txt','wb+')
        f.write('')
        f.close()

def operate_file(write_info):
	f = open('a_info.txt','a')
	f.write(write_info)
	f.write('\n')
	f.close()

create_file()
operate_file("用户编号-用户名-真实姓名-性别-性取向-所在地-注册时间-个人主页-QQ号码")

'''记录用户编号'''
i=12000
'''记录未找到页面数'''
j=0
time.clock()
while j<10000:
    time.sleep(1)
    try:
        url_request = urllib2.Request("http://www.acfun.tv/u/"+str(i)+".aspx#area=post-history")
        url_request.add_header('User-Agent','Mozilla/5.0')
        get_code = urllib2.urlopen(url_request).getcode()
        if get_code==200:
            con_b = urllib2.urlopen(url_request).read()
            soup = BeautifulSoup(con_b,fromEncoding="gb18030")
            #soup.originalEncoding
            tag_name = soup.findAll('a', attrs={'class':'name'})
            re_tag_name = re.compile(r'class="name">(.*?)</a>')
            re_tag = re.findall(re_tag_name,str(tag_name[1]))
            soup_ul = soup.findAll(id="list-info-user")
            re_name_con = re.compile(r'<li>真实姓名：(.*?)</li>')
            re_name = re.findall(re_name_con,str(soup_ul[0]))
            re_sex_con = re.compile(r'<li>性别：(.*?)</li>')
            re_sex =  re.findall(re_sex_con,str(soup_ul[0]))
            re_tosex_con = re.compile(r'<li>性取向：(.*?)</li>')
            re_tosex = re.findall(re_tosex_con,str(soup_ul[0]))
            re_add_con = re.compile(r'<li>所在地：(.*?)</li>')
            re_add = re.findall(re_add_con,str(soup_ul[0]))
            re_createtime_con = re.compile(r'<li>注册时间：(.*?)</li>')
            re_createtime = re.findall(re_createtime_con,str(soup_ul[0]))
            re_page_con = re.compile(r'<li>个人主页：(.*?)</li>')
            re_page = re.findall(re_page_con,str(soup_ul[0]))
            re_qq_con = re.compile(r'<li>QQ号码：(.*?)</li>')
            re_qq = re.findall(re_qq_con,str(soup_ul[0]))
            str_info = str(i)+'-'+str(re_tag[0])+'-'+str(re_name[0])+'-'+str(re_sex[0])+'-'+str(re_tosex[0])+'-'+str(re_add[0])+'-'\
                       +str(re_createtime[0])+'-'+str(re_page[0])+'-'+str(re_qq[0])
            print "正在记录用户："+str(i)
            operate_file(str_info)
            i=i+1
            j=0
        else:
            i=i+1
            j=j+1
            print '未找到用户：'+str(i)+'  返回代码：'+str(get_code)+' 1秒后继续查找下一个'
    except:
        i=i+1
        j=j+1
        print '（/TДT)/  未找到用户,1秒后继续查找下一个'
time = time.clock()
print '(=・ω・=) 执行完毕！共用时：'+str(time)
raw_input('按回车键结束')