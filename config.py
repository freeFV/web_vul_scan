#coding:utf8
import time
import traceback
from colorprinter import *

IGNORE_EXT = ['css','js','jpg','png','gif','rar','pdf','doc']
#不期待的文件后缀
EXPECT_EXT = ['php','jsp','asp','aspx']


HEADER = {
	'Cookie':"PHPSESSID=gqhvekgincgiunfpnm1819drji"
	#'Cookie':"__huid=111FB5QLrfmXmazjXSCgpKJCE9wpSTUotq8TP5vrSL+uQ=; __guid=193518196.2625901926484400128.1537945307001.5347; __DC_gid=59612149.49732202.1537962193195.1537962193195.1; opennews=1246a5df9011bc33; __sid=65234612.3981878673782017000.1538051400322.209; quCryptCode=D6TqMQxFspm09vZHFMpam08D4L7ToEFGsjbNr5aQyPmDhPSOad5o32EYaDH12NU6XTZTdbY1vQU%253D; quCapStyle=2; Q=u%3D360H3061940700%26n%3Doyvatoyvatovat%26le%3D%26m%3DZGH2WGWOWGWOWGWOWGWOWGWOZwHk%26qid%3D3061940700%26im%3D1_t014896567d42ffc231%26src%3Dpcw_so%26t%3D1; T=s%3Df30e9916edb788605cba1e88193e711b%26t%3D1538051791%26lm%3D%26lf%3D2%26sk%3Df258b40ac3e2046dade6ef531c5e7ae3%26mt%3D1538051791%26rc%3D%26v%3D2.0%26a%3D1; test_cookie_enable=null; monitor_count=8; __gid=133660893.123339936.1538021435934.1538052074654.60"
	#'Cookie':'JSESSIONID=1B73D55564BC005AF5EB87745860AB8F'
	#'Cookie':'PHPSESSID=kbnbiqqr1fdec1mm4eg9251k55; __guid=174447738.3574693008836675600.1537962173028.0884; count=2'
	#'Cookie':'tracker_u=direct; vid=U25861538223176935; uid=U8A8B1538223176935; provinceId=1; Hm_lvt_d69a759ccf3a7184844852dabec00bfe=1538223238; Hm_lvt_21936694257e7e343d2dbbaee538e9ee=1538223238; NTKF_T2D_CLIENTID=guestEBF5BBF8-2B04-5EA2-CB98-253FF8A340E3; UM_distinctid=166253ff8af1079-0e89c2a3086083-8383268-144000-166253ff8b08ea; CNZZDATA1256399051=510150115-1538219841-http%253A%252F%252Fwww.360haoyao.com%252F%7C1538219841; _citem_count=0; tcpos=g--0--0--0--0--0--0--0--0; JUM=15801001202; JUD=914027; JUN=15801001202; UserInfo="UserId=914027&UserName=20180929201620_15801001202&NickName=15801001202&Token=b2d259f3375e4bfa8b949006dc16e65d&Security=2SnGIZFxOrp+9Kt6Dc1kvg==&userLeverId=1"; SIGN=7181602631124226; SECURITY="2SnGIZFxOrp+9Kt6Dc1kvg=="; pre_citem_count=0; islogin_merge=1; nTalk_CACHE_DATA={uid:gy_1000_ISME9754_914027,tid:1538223377845154}; Hm_lpvt_21936694257e7e343d2dbbaee538e9ee=1538223459; Hm_lpvt_d69a759ccf3a7184844852dabec00bfe=1538223459'
	#'Cookie':'connect.sid=s%3A_oL_Wj8tAIyAQB47Yg6p2kG_DY-4sJ_o.Ku1UVKZKCtuBEmA8OY2RN8uYj8t7O40HedboxRIzdpk'
}


QUEUE = []
TOTAL_URL = set()
SIMILAR_SET = set()
debug = 1
output = ColorPrinter()

IS_CRAWL_SUBDOMAIN = False  #默认也会爬取其他子域名，如果需要只爬去某一个子域名，则设置为False

def get_ctime():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

