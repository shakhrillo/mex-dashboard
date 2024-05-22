-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: schichtprotokoll
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `preparation_shift` tinyint(1) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `shift` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_comments_token` (`token`),
  KEY `ix_comments_shift` (`shift`),
  KEY `ix_comments_comment` (`comment`),
  KEY `ix_comments_date` (`date`),
  KEY `ix_comments_preparation_shift` (`preparation_shift`),
  KEY `ix_comments_id` (`id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`token`) REFERENCES `users` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `machineQrCode` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `shift` varchar(255) DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `toolMounted` tinyint(1) DEFAULT NULL,
  `machineStopped` tinyint(1) DEFAULT NULL,
  `barcodeProductionNo` int DEFAULT NULL,
  `cavity` int DEFAULT NULL,
  `cycleTime` varchar(255) DEFAULT NULL,
  `partStatus` tinyint(1) DEFAULT NULL,
  `pieceNumber` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `toolCleaning` tinyint(1) DEFAULT NULL,
  `remainingProductionTime` int DEFAULT NULL,
  `remainingProductionDays` int DEFAULT NULL,
  `operatingHours` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `machineQrCode` (`machineQrCode`),
  KEY `token` (`token`),
  KEY `ix_data_partStatus` (`partStatus`),
  KEY `ix_data_createdAt` (`createdAt`),
  KEY `ix_data_remainingProductionTime` (`remainingProductionTime`),
  KEY `ix_data_barcodeProductionNo` (`barcodeProductionNo`),
  KEY `ix_data_operatingHours` (`operatingHours`),
  KEY `ix_data_pieceNumber` (`pieceNumber`),
  KEY `ix_data_toolMounted` (`toolMounted`),
  KEY `ix_data_remainingProductionDays` (`remainingProductionDays`),
  KEY `ix_data_cavity` (`cavity`),
  KEY `ix_data_shift` (`shift`),
  KEY `ix_data_note` (`note`),
  KEY `ix_data_machineStopped` (`machineStopped`),
  KEY `ix_data_cycleTime` (`cycleTime`),
  KEY `ix_data_toolCleaning` (`toolCleaning`),
  KEY `ix_data_id` (`id`),
  CONSTRAINT `data_ibfk_1` FOREIGN KEY (`machineQrCode`) REFERENCES `machines` (`machineQrCode`),
  CONSTRAINT `data_ibfk_2` FOREIGN KEY (`token`) REFERENCES `users` (`token`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (1,'Emac50-1','0004650166692','S2','2024-05-17 19:30:53',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(2,'Emac50-1','0004650166692','S2','2024-05-17 19:33:24',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(3,'Emac50-1','0004650166692','S2','2024-05-17 19:33:29',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(4,'Emac50-1','0004650166692','S2','2024-05-17 19:35:05',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(5,'Emac50-1','0004650166692','S2','2024-05-17 19:35:06',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(6,'Emac50-1','0004650166692','S2','2024-05-17 19:35:07',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(7,'Emac50-1','0004650166692','S2','2024-05-17 19:35:52',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(8,'Emac50-1','0004650166692','S2','2024-05-17 19:37:12',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00'),(9,'Emac50-1','0004650166692','S2','2024-05-17 19:37:13',0,0,811202001,4,'13.1',1,27656,'.',1,840,2,'00:00');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines`
--

DROP TABLE IF EXISTS `machines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machines` (
  `machineQrCode` varchar(255) NOT NULL,
  PRIMARY KEY (`machineQrCode`),
  KEY `ix_machines_machineQrCode` (`machineQrCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- insert into machines
-- E 35-1
-- E 45-1
-- E 45-2
-- F450iA-1
-- E 50-2
-- E 50-3
-- F150iA-1
-- Emac50-1
-- Emac50-2
-- Emac50-3
-- KM 50-1
-- KM 80-1
-- KM 150-1
-- E 55-1
-- KM 420-1
-- E 120-1
-- E 80-1
-- F250iA-1

INSERT INTO `machines` VALUES ('E 45-1'),('E 45-2'),('F450iA-1'),('E 50-2'),('E 50-3'),('F150iA-1'),('Emac50-1'),('Emac50-2'),('Emac50-3'),('KM 50-1'),('KM 80-1'),('KM 150-1'),('E 55-1'),('KM 420-1'),('E 120-1'),('E 80-1'),('F250iA-1');

--
-- Dumping data for table `machines`
--

LOCK TABLES `machines` WRITE;
/*!40000 ALTER TABLE `machines` DISABLE KEYS */;
INSERT INTO `machines` VALUES ('Emac50-1');
/*!40000 ALTER TABLE `machines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_users_name` (`name`),
  KEY `ix_users_surname` (`surname`),
  KEY `ix_users_token` (`token`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','0004650166692'),(2,'admin','admin','0004650166692'),(3,'user','user','0004650166693'),(4,'user2','user2','0004653466693'),(5,'user3','user3','0004650166694'),(6,'user4','user4','0004650166695'),(7,'admin','admin','0004650166692'),(8,'user','user','0004650166693'),(9,'user2','user2','0004653466693'),(10,'user3','user3','0004650166694'),(11,'user4','user4','0004650166695'),(12,'admin','admin','0004650166692'),(13,'user','user','0004650166693'),(14,'user2','user2','0004653466693'),(15,'user3','user3','0004650166694'),(16,'user4','user4','0004650166695');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workflow`
--

DROP TABLE IF EXISTS `workflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workflow` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(255) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_workflow_start_time` (`start_time`),
  KEY `ix_workflow_id` (`id`),
  KEY `ix_workflow_end_time` (`end_time`),
  KEY `ix_workflow_token` (`token`),
  CONSTRAINT `workflow_ibfk_1` FOREIGN KEY (`token`) REFERENCES `users` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workflow`
--

LOCK TABLES `workflow` WRITE;
/*!40000 ALTER TABLE `workflow` DISABLE KEYS */;
/*!40000 ALTER TABLE `workflow` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-18 17:26:36
