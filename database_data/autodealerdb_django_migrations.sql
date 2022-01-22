CREATE DATABASE  IF NOT EXISTS `autodealerdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `autodealerdb`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: autodealerdb
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-01-17 11:16:44.720910'),(2,'auth','0001_initial','2022-01-17 11:16:45.700869'),(3,'admin','0001_initial','2022-01-17 11:16:45.951961'),(4,'admin','0002_logentry_remove_auto_add','2022-01-17 11:16:45.967568'),(5,'admin','0003_logentry_add_action_flag_choices','2022-01-17 11:16:45.983183'),(6,'contenttypes','0002_remove_content_type_name','2022-01-17 11:16:46.203403'),(7,'auth','0002_alter_permission_name_max_length','2022-01-17 11:16:46.312795'),(8,'auth','0003_alter_user_email_max_length','2022-01-17 11:16:46.375455'),(9,'auth','0004_alter_user_username_opts','2022-01-17 11:16:46.407013'),(10,'auth','0005_alter_user_last_login_null','2022-01-17 11:16:46.548158'),(11,'auth','0006_require_contenttypes_0002','2022-01-17 11:16:46.563795'),(12,'auth','0007_alter_validators_add_error_messages','2022-01-17 11:16:46.611120'),(13,'auth','0008_alter_user_username_max_length','2022-01-17 11:16:46.744926'),(14,'auth','0009_alter_user_last_name_max_length','2022-01-17 11:16:46.854826'),(15,'auth','0010_alter_group_name_max_length','2022-01-17 11:16:46.902530'),(16,'auth','0011_update_proxy_permissions','2022-01-17 11:16:46.918197'),(17,'auth','0012_alter_user_first_name_max_length','2022-01-17 11:16:47.043705'),(18,'customer','0001_initial','2022-01-17 11:16:47.090583'),(19,'vehicle','0001_initial','2022-01-17 11:16:47.184841'),(20,'purchase','0001_initial','2022-01-17 11:16:47.358161'),(21,'scheme','0001_initial','2022-01-17 11:16:47.421181'),(22,'sale','0001_initial','2022-01-17 11:16:47.955064'),(23,'sessions','0001_initial','2022-01-17 11:16:48.032930'),(24,'warehouse','0001_initial','2022-01-17 11:16:49.247078'),(25,'purchase','0002_rename_vehicle_id_purchase_vehicle','2022-01-17 11:24:58.325672'),(26,'sale','0002_rename_customer_id_sale_customer_and_more','2022-01-17 11:24:58.900404'),(27,'customer','0002_alter_customer_phone','2022-01-19 03:12:51.354423');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-21 17:47:36
