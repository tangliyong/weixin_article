# weixin_article
基于搜狗微信搜索的微信公众号爬虫

# 项目简介：

基于搜狗微信搜索的微信公众号爬虫 可以抓取指定公众号的文章信息到mysql数据库。对sogo和微信验证码，调用ruokuai接口进行识别。

# 项目使用：

一、使用说明
1、在mysql数据库中创建数据库，sql语句见gongzhonghao.sql

2、修改config.py文件中对应的设置，打码平台配置ruokuai这个一定要设置，否则出现验证码就不能正常工作了

3、python对应的库的安装好，参见各python文件引用的包。

二、文件说明

1、add_wechat.py 该文件遍历待抓取列表（数据库表：mp_list），将公众号基本信息写入数据库表mp_info

2、add_article.py 将mp_list中对应的公众号文章写入wenzhang_info表中

3、 config.py mysql数据库配置和ruokuai配置

# 依赖项目
基于搜狗微信搜索的微信公众号爬虫接口
https://github.com/Chyroc/WechatSogou

1、安装
pip install wechatsogou --upgrade

2、安装WechatSogou要求的包
https://github.com/Chyroc/WechatSogou/blob/master/requirements.txt

# 参考项目

项目大量参考了wechat_sogou_crawl项目，https://github.com/jaryee/wechat_sogou_crawl
