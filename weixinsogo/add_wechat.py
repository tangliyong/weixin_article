# -*- coding: utf-8 -*-

import time
import logging.config
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
mp_list = mysql.find(0)

for mp_item in mp_list :
    try:
        print(mp_item)
        if mp_item['wechat_id']:
            mysql.where_sql = "wechat_id ='" + mp_item['wechat_id'] + "'"
            mp_data = mysql.table('mp_info').find(1)
            if not mp_data :
                wechat_info = ws_api.get_gzh_info(mp_item['wechat_name'], identify_image_callback=__identify_image_callback)
                time.sleep(1)
                #print(wechat_info)
                if(wechat_info != ""):
                    mysql.table('mp_info').add({'open_id':wechat_info['open_id'],
                                                'profile_url':wechat_info['profile_url'],
                                                'headimage':wechat_info['headimage'],
                                                'wechat_name':wechat_info['wechat_name'],
                                                'wechat_id':wechat_info['wechat_id'],
                                                'post_perm': wechat_info['post_perm'],
                                                'qrcode': wechat_info['qrcode'],
                                                'introduction': wechat_info['introduction'],
                                                'authentication': wechat_info['authentication'],
                                                'create_time':time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))})
            else:
                print(u"已经存在的公众号")

        #删除已添加项
        #mysql.table('add_mp_list').where({'_id':add_item['_id']}).delete()
    except Exception as e:
        logger.error(u"error "+ e)
        pass

print("success")
