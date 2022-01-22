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
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Customer',7,'add_customer'),(26,'Can change Customer',7,'change_customer'),(27,'Can delete Customer',7,'delete_customer'),(28,'Can view Customer',7,'view_customer'),(29,'Can add Purchase',8,'add_purchase'),(30,'Can change Purchase',8,'change_purchase'),(31,'Can delete Purchase',8,'delete_purchase'),(32,'Can view Purchase',8,'view_purchase'),(33,'Can add Sale',9,'add_sale'),(34,'Can change Sale',9,'change_sale'),(35,'Can delete Sale',9,'delete_sale'),(36,'Can view Sale',9,'view_sale'),(37,'Can add Scheme',10,'add_scheme'),(38,'Can change Scheme',10,'change_scheme'),(39,'Can delete Scheme',10,'delete_scheme'),(40,'Can view Scheme',10,'view_scheme'),(41,'Can add Vehicle',11,'add_vehicle'),(42,'Can change Vehicle',11,'change_vehicle'),(43,'Can delete Vehicle',11,'delete_vehicle'),(44,'Can view Vehicle',11,'view_vehicle'),(45,'Can add customer_ dim',12,'add_customer_dim'),(46,'Can change customer_ dim',12,'change_customer_dim'),(47,'Can delete customer_ dim',12,'delete_customer_dim'),(48,'Can view customer_ dim',12,'view_customer_dim'),(49,'Can add purchase_ record_ dim',13,'add_purchase_record_dim'),(50,'Can change purchase_ record_ dim',13,'change_purchase_record_dim'),(51,'Can delete purchase_ record_ dim',13,'delete_purchase_record_dim'),(52,'Can view purchase_ record_ dim',13,'view_purchase_record_dim'),(53,'Can add sale_ fact',14,'add_sale_fact'),(54,'Can change sale_ fact',14,'change_sale_fact'),(55,'Can delete sale_ fact',14,'delete_sale_fact'),(56,'Can view sale_ fact',14,'view_sale_fact'),(57,'Can add sale_ record_ dim',15,'add_sale_record_dim'),(58,'Can change sale_ record_ dim',15,'change_sale_record_dim'),(59,'Can delete sale_ record_ dim',15,'delete_sale_record_dim'),(60,'Can view sale_ record_ dim',15,'view_sale_record_dim'),(61,'Can add scheme_ dim',16,'add_scheme_dim'),(62,'Can change scheme_ dim',16,'change_scheme_dim'),(63,'Can delete scheme_ dim',16,'delete_scheme_dim'),(64,'Can view scheme_ dim',16,'view_scheme_dim'),(65,'Can add time_ dim',17,'add_time_dim'),(66,'Can change time_ dim',17,'change_time_dim'),(67,'Can delete time_ dim',17,'delete_time_dim'),(68,'Can view time_ dim',17,'view_time_dim'),(69,'Can add vehicle_ dim',18,'add_vehicle_dim'),(70,'Can change vehicle_ dim',18,'change_vehicle_dim'),(71,'Can delete vehicle_ dim',18,'delete_vehicle_dim'),(72,'Can view vehicle_ dim',18,'view_vehicle_dim');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-21 17:47:37
