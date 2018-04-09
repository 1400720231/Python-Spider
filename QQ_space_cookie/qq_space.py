# coding:utf-8
import requests

"""
方法1：每次请求带上headers,其中cookie包含在headers中

# """
# s =requests.session()


# url = 'https://user.qzone.qq.com/937886362'
# cookie = 'pgv_pvi=270815232; ptui_loginuin=937886362; pt2gguin=o0937886362; RK=rf7xbFDkVu; ptcz=014ce957fb0ff44bcee8bc4101d17bf49abb57ffa854cd0b1caf770a8314f854; luin=o0937886362; tvfe_boss_uuid=3a70612a82d1d77b; pgv_pvid=7697825562; o_cookie=937886362; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; mobileUV=1_16286309a46_7ca70; __Q_w_s_hat_seed=1; lskey=0001000001b6085bfa9d198e4ccd7311643f2db6b37c66a1ce06d3bb657c0e10265aa2fd146c9d19797dd663; uid=263517280; __layoutStat=9; pgv_si=s3919702016; ptisp=cm; pgv_info=ssid=s2599169595; uin=o0937886362; skey=@fsQmYSjGH; p_uin=o0937886362; pt4_token=tOVlSqaMPCSUu9Ugwpe6ceD6xYEVaUqZjyqzyC7JG9k_; p_skey=8anozI6XdDWG899lACBORrIjrr4f*FQnFkgrVybg3uY_; fnc=2; Loading=Yes; x-stgw-ssl-info=7c5dada4d52e9c591363171b2262b736|0.145|1523237098.147|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|42500|h2|0; qzmusicplayer=qzone_player_937886362_1523237099240; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; 937886362_todaycount=0; 937886362_totalcount=20751; cpu_performance_v8=7'

# # 这是返回我的说说内容信息的js路径，需要慢慢找到这个路径
# get_url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=937886362&ftype=0&sort=0&pos=0&num=20&replynum=100&g_tk=1278728291&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken=30dae7408817cca121ec834c6d091b546b6dc0b75a74ba7dbedaf143219da25cf72e09624c2240d2&g_tk=1278728291'
# headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#     'cookie':cookie}
# # 每次都要加带有cookie的headers
# b = s.get(get_url,headers=headers)   

# print(b.text)



"""
方法2：给session中的cookies赋值，这样就不用每次都带上headers了
"""

s =requests.session()
cookie = 'pgv_pvi=270815232; ptui_loginuin=937886362; pt2gguin=o0937886362; RK=rf7xbFDkVu; ptcz=014ce957fb0ff44bcee8bc4101d17bf49abb57ffa854cd0b1caf770a8314f854; luin=o0937886362; tvfe_boss_uuid=3a70612a82d1d77b; pgv_pvid=7697825562; o_cookie=937886362; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; mobileUV=1_16286309a46_7ca70; __Q_w_s_hat_seed=1; lskey=0001000001b6085bfa9d198e4ccd7311643f2db6b37c66a1ce06d3bb657c0e10265aa2fd146c9d19797dd663; uid=263517280; __layoutStat=9; pgv_si=s3919702016; ptisp=cm; pgv_info=ssid=s2599169595; uin=o0937886362; skey=@fsQmYSjGH; p_uin=o0937886362; pt4_token=tOVlSqaMPCSUu9Ugwpe6ceD6xYEVaUqZjyqzyC7JG9k_; p_skey=8anozI6XdDWG899lACBORrIjrr4f*FQnFkgrVybg3uY_; fnc=2; Loading=Yes; x-stgw-ssl-info=7c5dada4d52e9c591363171b2262b736|0.145|1523237098.147|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|42500|h2|0; qzmusicplayer=qzone_player_937886362_1523237099240; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; 937886362_todaycount=0; 937886362_totalcount=20751; cpu_performance_v8=7'

s.cookies['cookie'] = cookie
url = 'https://user.qzone.qq.com/937886362'

# 这是返回我的说说内容信息的js路径，需要慢慢找到这个路径
get_url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=937886362&ftype=0&sort=0&pos=0&num=20&replynum=100&g_tk=1278728291&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken=30dae7408817cca121ec834c6d091b546b6dc0b75a74ba7dbedaf143219da25cf72e09624c2240d2&g_tk=1278728291'
# headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#     }

b = s.get(get_url)   
print(b.text)

