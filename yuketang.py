import datetime
import requests
import json
import math
import random

numstart=19339944
numend=19340044
classroomid = 14857712  # 每一个大课的课堂编号是固定的
starttime = datetime.datetime(2023, 9, 28, 9, 34, 47)  # 设置刷课起始时间
random_number = random.randint(30, 40)  #设置刷课视频时间间隔，例：刷的每个视频时间间隔为三四十分钟随机
schoolurl='changjiang.yuketang.cn'
x_csrftoken = 'hFMN1EU2Xn4u5R28QtvNx4VWZ5o9H'
cookie = 'ogin_type=WX; django_language=zh-cn; classroomId=14857712; classroom_id=14857712; user_role=-1; JG_fcdf8e635093adde6; csrftoken=hFMN1EU2Xn4u5R28QtvNx4VWZ5o9H; sessionid=psqo4to6tb085laefnagyxp'

headers = {'authority': schoolurl,
           'method': 'GET',
           'path': '/mooc-api/v1/lms/learn/leaf_info/' + str(classroomid) + '/15745084/', 
           'scheme': 'https',
           'accept': 'application/json, text/plain, */*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'classroom-id': str(classroomid),  
           'cookie': cookie,
           'referer': 'https://'+schoolurl+'/v2/web/xcloud/video-student/' + str(classroomid) + '/15745084', 
           'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'university-id': '3288',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
           'uv-id': '3288',
           'x-Csrftoken': x_csrftoken,
           'xt-Agent': 'web',
           'xtbz': 'ykt'
           }
header1s = {'authority': schoolurl,
            'method': 'POST',
            'path': '/video-log/heartbeat/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'classroom-id': str(classroomid),
            'content-length': '1037',
            'content-type': 'application/json',
            'cookie': cookie,
            'origin': 'https://'+schoolurl,
            'referer': 'https://'+schoolurl+'/v2/web/xcloud/video-student/' + str(classroomid) + '/15745084',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'university-id': '3288',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-client': 'web',
            'x-csrftoken': x_csrftoken,
            'xt-agent': 'web',
            'xtbz': 'ykt'
            }

numlist = list(range(numstart, numend, 1))
for i in range(len(numlist)):
    data = { 'heart_data': [] }
    videoid = str(numlist[i])
    headers["path"] = '/mooc-api/v1/lms/learn/leaf_info/' + str(classroomid) + '/' + videoid + '/'
    headers["referer"] = 'https://'+schoolurl+'/v2/web/xcloud/video-student/' + str(
        classroomid) + '/' + videoid
    header1s['referer'] = 'https://'+schoolurl+'/v2/web/xcloud/video-student/' + str(
        classroomid) + '/' + videoid
    offset = 5  # 正常每5秒发送一次数据包
    details = requests.get(
        url="https://"+schoolurl+"/mooc-api/v1/lms/learn/leaf_info/" + str(classroomid) + "/" + videoid + "/",
        headers=headers)
    c=json.loads(details.text)['data']
    if(json.loads(details.text)['msg']=='Objects does not exist.'):
        print(numlist[i], "不存在")
        continue
    if ('ccid' not in c['content_info']['media'] or 'duration' not in c['content_info']['media']):
        print(numlist[i], "非法id")
        continue
    if (c["leaf_type"] != 0):
        print(numlist[i], "不是视频")
        continue

    duration= 1000 if  c['content_info']['media']['duration']==0 else c['content_info']['media']['duration']
    times=math.ceil(duration/5)
    starttime += datetime.timedelta(minutes=random_number)
    timestamp = int(starttime.timestamp() * 1000)

    for j in range(times+1):
        cp=j*5
        if cp > duration:
            cp = duration
        item = {"i": 5, "et": "heartbeat", "p": "web", "n": "ali-cdn.xuetangx.com", "lob": "ykt", "cp": cp, "fp": 0,
                "tp": 0, "sp": 1, "ts": timestamp, "u": c["user_id"], "uip": "", "c": c["course_id"], "v": c["id"],
                "skuid": c['sku_id'], "classroomid": str(classroomid), "cc": c["content_info"]["media"]["ccid"], "d": duration,
                "pg": str(c["id"]) + '_14i0z', "sq": j + 1, "t": "video", "cards_id": "", "slide": 0, "v_url": ""}
        data['heart_data'].append(item)
    rev=requests.post(url='https://'+schoolurl+'/video-log/heartbeat/',headers=header1s,data=json.dumps(data))
    print(numlist[i], '已完成观看')
