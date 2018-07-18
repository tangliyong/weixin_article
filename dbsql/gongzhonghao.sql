/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50711
Source Host           : 127.0.0.1:3306
Source Database       : gongzhonghao

Target Server Type    : MYSQL
Target Server Version : 50711
File Encoding         : 65001

Date: 2017-02-16 17:16:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `add_mp_list`
-- ----------------------------
DROP TABLE IF EXISTS `mp_list`;
CREATE TABLE `mp_list` (
  `_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `wechat_name` varchar(50) DEFAULT '' COMMENT '要添加的公众号名称',
  `wechat_id` varchar(50) DEFAULT '' COMMENT '公众号的微信号',
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of add_mp_list
-- ----------------------------
INSERT INTO `mp_list` VALUES (1,'今日头条', 'headline_today');
INSERT INTO `mp_list` VALUES (2,'新榜', 'newrankcn');
INSERT INTO `mp_list` VALUES (3,'娱乐新榜', 'yulexinbang');

-- ----------------------------
-- Table structure for `mp_info`
-- ----------------------------
DROP TABLE IF EXISTS `mp_info`;
CREATE TABLE `mp_info` (
  `_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `open_id` varchar(50) DEFAULT '' COMMENT '微信号唯一ID',
  `profile_url` varchar(500) DEFAULT '' COMMENT '最近10条群发页链接',
  `headimage` varchar(500) DEFAULT '' COMMENT '头像',
  `wechat_name` varchar(200) DEFAULT '' COMMENT '名称',
  `wechat_id` varchar(200) DEFAULT '' COMMENT '微信id',
  `post_perm` varchar(200) DEFAULT '' COMMENT '最近一月群发数',
  `qrcode` varchar(500) DEFAULT '' COMMENT '二维码',
  `introduction` varchar(200) DEFAULT '' COMMENT '介绍',
  `authentication` varchar(200) DEFAULT '' COMMENT '认证',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=286 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for `wenzhang_info`
-- ----------------------------
DROP TABLE IF EXISTS `wenzhang_info`;
CREATE TABLE `wenzhang_info` (
  `_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `wechat_id` varchar(100) DEFAULT '' COMMENT 'wechat_id',
  `send_id` varchar(100) DEFAULT '' COMMENT '群发id',
  `date_time` datetime DEFAULT NULL COMMENT '文章推送时间',
  `type` int(11) DEFAULT '0' COMMENT '消息类型',
  `main` varchar(100) DEFAULT '' COMMENT '是否是一次群发的第一次消息',
  `title` varchar(200) DEFAULT '' COMMENT '文章标题',
  `abstract` varchar(500) DEFAULT '' COMMENT '文章摘要',
  `fileid` varchar(50) DEFAULT '' COMMENT 'fileid',
  `content_url` varchar(500) DEFAULT '' COMMENT '文章链接',
  `source_url` varchar(500) DEFAULT '' COMMENT '阅读原文的链接',
  `cover` varchar(200) DEFAULT '' COMMENT '封面图',
  `author` varchar(50) DEFAULT '' COMMENT '作者',
  `copyright_stat` int(1) DEFAULT '0' COMMENT '11表示原创 其它表示非原创',
  `content` MEDIUMBLOB COMMENT '文章内容',
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6559 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of wenzhang_info
-- ----------------------------


