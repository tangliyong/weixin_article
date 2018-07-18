# -*- coding: utf-8 -*-
#查找公众号最新文章

import datetime
import time
import logging.config
import random
import wechatsogou
import weixinsogo.db
from weixinsogo.rk import (
    __identify_image_callback,
    identify_image_callback_ruokuai_sogou,
    identify_image_callback_ruokuai_weixin)
# 日志
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

# WechatSogouAPI 如 设置超时 # 验证码输入错误的重试次数，默认为1
ws_api = wechatsogou.WechatSogouAPI(timeout=1, captcha_break_time=3)

#数据库实例
mysql = weixinsogo.db.mysql('mp_list')

#循环获取数据库中所有公众号
mysql.order_sql = " order by _id desc"
mp_list = mysql.find(0)

now_time = datetime.datetime.today()
now_time = datetime.datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0)

for item in mp_list:
    try:
        time.sleep(random.randrange(1,3))

        wechat_id = item['wechat_id'] #获得公众号wechat id

        #获取最近文章信息
        wechat_info = ws_api.get_gzh_info (wechat_id)
        if not wechat_info['profile_url']:
            continue

        wz_url = wechat_info['profile_url'];
        wz_list = ws_api.get_gzh_article_by_history (url=wz_url,
                                                     identify_image_callback_sogou=identify_image_callback_ruokuai_sogou,
                                                     identify_image_callback_weixin=identify_image_callback_ruokuai_weixin)

        #获取公众号最新的100篇文章
        mysql.order_sql = " order by _id desc"
        wenzhang_list =mysql.table ('wenzhang_info').where ({'wechat_id': wechat_id}).find (100)

        #type==49表示是图文消息
        for wz_item in wz_list['article'] :
            if wz_item['type'] == '49':
                #根据标题判断是否包含已经将文章存入数据库
                hasTitle = False
                for wenzhang_item in wenzhang_list:
                    if wenzhang_item['title'] == wz_item['title']:
                        hasTitle = True
                        break

                if hasTitle:
                    continue

                #把文章写入数据库
                content = ''
                print(wz_item['content_url'])
                if not wz_item['content_url'] :
                    continue
                else:
                    content = ws_api.get_article_content(wz_item['content_url'],
                                                         identify_image_callback=__identify_image_callback)['content_html']

                sourceurl = wz_item['source_url']
                if len(sourceurl) >= 300 :
                    sourceurl = ''

                mysql.table('wenzhang_info').add({'send_id':wz_item['send_id'],
                                                'wechat_id':wechat_id,
                                                'date_time': time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(wz_item['datetime'])),
                                                'type':wz_item['type'],
                                                'main':wz_item['main'],
                                                'title':wz_item['title'],
                                                'abstract':wz_item['abstract'],
                                                'fileid':wz_item['fileid'],
                                                'source_url':sourceurl,
                                                'content_url':wz_item['content_url'],
                                                'cover':wz_item['cover'],
                                                'author':wz_item['author'],
                                                'copyright_stat':wz_item['copyright_stat'],
                                                'content':content})

    except Exception as e:
        print(u"error "+ e)
        logger.error (u"error " + e)
            
print('success')