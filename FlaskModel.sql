-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: FlaskModel
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('42c9ea53caa4');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_category`
--

DROP TABLE IF EXISTS `bbs_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classname` varchar(60) NOT NULL,
  `parentid` int(11) NOT NULL,
  `replycount` int(11) NOT NULL,
  `compere` varchar(10) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `orderby` smallint(6) NOT NULL,
  `lastpost` varchar(600) DEFAULT NULL,
  `namestyle` varchar(10) DEFAULT NULL,
  `ispass` smallint(6) NOT NULL,
  `classpic` varchar(200) DEFAULT NULL,
  `themecount` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_category`
--

LOCK TABLES `bbs_category` WRITE;
/*!40000 ALTER TABLE `bbs_category` DISABLE KEYS */;
INSERT INTO `bbs_category` VALUES (1,'python技术交流',0,4,'开源小猿',NULL,0,NULL,NULL,1,NULL,2),(2,'内核源码',1,7,'开源小猿马',NULL,2,'风男',NULL,0,NULL,11),(3,'程序人生',0,3,'python框架',NULL,0,NULL,NULL,1,NULL,1),(5,'PHP框架',1,4,'进阶讨论',NULL,0,'阿娇',NULL,1,NULL,6),(6,'开源产品',1,11,'进阶讨论',NULL,0,'杰哥',NULL,1,NULL,1),(7,'进阶讨论',1,2,'进阶讨论',NULL,0,'雷哥',NULL,1,NULL,4),(9,'名人故事',3,3,'技术交流',NULL,0,'凯哥',NULL,1,NULL,1),(10,'经验分享',3,9,'求职者',NULL,0,'人生',NULL,1,NULL,11),(11,'名人名言',3,3,'技术',NULL,0,'ming',NULL,1,NULL,1),(12,'情感咨询',0,3,'情感大师',NULL,0,NULL,NULL,1,NULL,3),(13,'撩妹全书',12,3,'国服渣男',NULL,0,'darren',NULL,1,NULL,3);
/*!40000 ALTER TABLE `bbs_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_closeip`
--

DROP TABLE IF EXISTS `bbs_closeip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_closeip` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ip` int(10) NOT NULL,
  `addtime` int(10) DEFAULT NULL,
  `over` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_closeip`
--

LOCK TABLES `bbs_closeip` WRITE;
/*!40000 ALTER TABLE `bbs_closeip` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbs_closeip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_details`
--

DROP TABLE IF EXISTS `bbs_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_details` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first` tinyint(1) NOT NULL DEFAULT '0',
  `tid` int(10) NOT NULL,
  `authorid` int(10) NOT NULL,
  `title` varchar(600) NOT NULL,
  `content` mediumtext NOT NULL,
  `addtime` int(12) NOT NULL,
  `addip` int(12) NOT NULL,
  `classid` int(10) NOT NULL,
  `replycount` int(12) NOT NULL DEFAULT '0',
  `hits` int(12) NOT NULL DEFAULT '0',
  `istop` tinyint(2) NOT NULL DEFAULT '0',
  `elite` tinyint(2) NOT NULL DEFAULT '0',
  `ishot` tinyint(2) NOT NULL DEFAULT '0',
  `rate` smallint(3) NOT NULL DEFAULT '0',
  `attachment` smallint(3) DEFAULT NULL,
  `isdel` int(2) NOT NULL,
  `style` char(10) DEFAULT NULL,
  `isdisplay` int(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_details`
--

LOCK TABLES `bbs_details` WRITE;
/*!40000 ALTER TABLE `bbs_details` DISABLE KEYS */;
INSERT INTO `bbs_details` VALUES (1,1,1,1,'一个小碟子','今晚的夜色真美',2012,1,0,1,2,1,1,1,20,NULL,1,NULL,1),(2,1,2,2,'风男','风也温柔',2011,2,0,3,5,1,0,0,50,NULL,0,NULL,1),(3,0,2,3,'阿布','大英雄者,腹有大志,胸有良谋',2008,3,0,5,5,0,1,0,50,NULL,0,NULL,1),(4,0,2,4,'阿水','有包藏宇宙之机,有吞吐天地之志',2006,4,0,7,5,1,0,1,50,NULL,0,NULL,1),(5,1,5,5,'阿娇','红豆生南国,春来发几枝',2019,5,0,5,4,1,0,1,40,NULL,1,NULL,1),(6,1,5,6,'杰哥','花有重开日人无再少年',2001,6,0,5,10,1,0,1,50,NULL,0,NULL,1),(7,1,7,6,'雷哥','进入布达拉宫,我是雪域最大的王',2000,7,0,5,11,1,0,1,57,NULL,0,NULL,1),(8,1,8,7,'伟哥','走在拉萨街头,我是世间最美的情郎',2000,8,0,5,12,1,0,1,57,NULL,0,NULL,1),(9,1,9,9,'凯哥','将军未挂封侯印,腰下常悬带血刀',1999,9,0,7,13,1,0,1,58,NULL,0,NULL,1),(10,0,10,10,'人生','人生苦短,我学python',2002,10,0,5,5,1,0,1,2,NULL,5,NULL,0),(11,1,5,2,'阿成','你若盛开,蝴蝶自来',2006,11,2,6,6,1,0,1,5,NULL,5,NULL,1);
/*!40000 ALTER TABLE `bbs_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_link`
--

DROP TABLE IF EXISTS `bbs_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_link` (
  `lid` smallint(6) NOT NULL AUTO_INCREMENT,
  `displayorder` tinyint(2) NOT NULL DEFAULT '0',
  `name` varchar(30) NOT NULL,
  `url` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `addtime` int(12) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_link`
--

LOCK TABLES `bbs_link` WRITE;
/*!40000 ALTER TABLE `bbs_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbs_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_order`
--

DROP TABLE IF EXISTS `bbs_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_order` (
  `oid` int(10) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `addtime` int(11) NOT NULL,
  `ispay` tinyint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_order`
--

LOCK TABLES `bbs_order` WRITE;
/*!40000 ALTER TABLE `bbs_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbs_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbs_user`
--

DROP TABLE IF EXISTS `bbs_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bbs_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` char(16) NOT NULL,
  `password` char(32) NOT NULL,
  `email` char(30) NOT NULL,
  `udertype` tinyint(2) NOT NULL,
  `regtime` int(12) NOT NULL,
  `lasttime` int(12) NOT NULL,
  `regip` int(12) NOT NULL,
  `picture` varchar(255) NOT NULL DEFAULT 'public/images/avatar_blank.gif',
  `grade` int(10) DEFAULT '0',
  `problem` varchar(200) DEFAULT NULL,
  `result` varchar(200) DEFAULT NULL,
  `realname` char(50) DEFAULT NULL,
  `sex` tinyint(4) DEFAULT '2',
  `birthday` varchar(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `qq` char(13) DEFAULT NULL,
  `autograph` varchar(500) DEFAULT NULL,
  `allowlogin` tinyint(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbs_user`
--

LOCK TABLES `bbs_user` WRITE;
/*!40000 ALTER TABLE `bbs_user` DISABLE KEYS */;
INSERT INTO `bbs_user` VALUES (1,'999','999','999',1,1997,2007,1,'upload/1.jpg',0,NULL,NULL,NULL,2,NULL,NULL,NULL,NULL,1),(2,'999','999','999',1,1997,2007,1,'public/images/avatar_blank.gif',0,NULL,NULL,NULL,2,NULL,NULL,NULL,NULL,1),(3,'darren','1234','1234@qq.com',1,1997,2007,1,'public/images/avatar_blank.gif',0,NULL,NULL,'张三',2,NULL,'2','132','蛋刀赴会',1),(4,'一只鱼','123456@','123456@qq.com',1,1997,2007,1,'public/images/avatar_blank.gif',0,NULL,NULL,NULL,2,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `bbs_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-22  9:32:30
