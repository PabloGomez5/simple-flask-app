-- MySQL dump 10.13  Distrib 8.0.26, for macos11.4 (arm64)
--
-- Host: 127.0.0.1    Database: footballteammanageappdb
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `Calendario`
--

DROP TABLE IF EXISTS `Calendario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Calendario` (
  `rival` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `campo` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Calendario`
--

LOCK TABLES `Calendario` WRITE;
/*!40000 ALTER TABLE `Calendario` DISABLE KEYS */;
INSERT INTO `Calendario` VALUES ('vimenor','fuera','2021-09-26'),('gimnastica b','casa','2021-10-03'),('santillana a','casa','2021-10-10'),('amistad b','fuera','2021-10-17'),('trope b','casa','2021-10-24'),('p amigos gim','fuera','2021-11-07'),('mineros a','casa','2021-11-14'),('bezana a','fuera','2021-11-21'),('pandas a','casa','2021-11-28'),('vimenor b','casa','2021-12-12'),('gimnastica b','fuera','2021-12-19'),('santillana a','fuera','2022-01-09'),('amistad b','casa','2022-01-16'),('trope b','fuera','2022-01-23'),('p amigos gim','casa','2022-01-30'),('mineros a','fuera','2022-02-06'),('bezana a','casa','2022-02-13'),('pandas a','fuera','2022-02-20');
/*!40000 ALTER TABLE `Calendario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Convocatoria`
--

DROP TABLE IF EXISTS `Convocatoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Convocatoria` (
  `dorsal` int NOT NULL,
  `jugador` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `convocado` int NOT NULL DEFAULT '0',
  `desconvocado` int NOT NULL DEFAULT '0',
  `titular` int NOT NULL DEFAULT '0',
  `minutos` int NOT NULL DEFAULT '0',
  `rendimiento` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Convocatoria`
--

LOCK TABLES `Convocatoria` WRITE;
/*!40000 ALTER TABLE `Convocatoria` DISABLE KEYS */;
INSERT INTO `Convocatoria` VALUES (1,'Adrian',0,0,0,0,0),(2,'Raul',0,0,0,0,0),(3,'Ruben',0,0,0,0,0),(4,'Aitor',0,0,0,0,0),(5,'Fernando',0,0,0,0,0),(6,'Ramon',0,0,0,0,0),(7,'Dani San',0,0,0,0,0),(8,'Diego',0,0,0,0,0),(9,'Eneko',0,0,0,0,0),(10,'Jorge P',0,0,0,0,0),(11,'Rojo A',0,0,0,0,0),(12,'Adrian G',0,0,0,0,0),(13,'Jorge A',0,0,0,0,0),(14,'Alex P',0,0,0,0,0),(15,'Sergio',0,0,0,0,0),(16,'Noriega',0,0,0,0,0),(17,'Pablo C',0,0,0,0,0),(18,'Dani Go',0,0,0,0,0),(19,'Alex',0,0,0,0,0),(20,'Chicho',0,0,0,0,0),(21,'Dani Gu',0,0,0,0,0),(22,'Nico',0,0,0,0,0),(23,'Cantero',0,0,0,0,0);
/*!40000 ALTER TABLE `Convocatoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Entrenadores`
--

DROP TABLE IF EXISTS `Entrenadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Entrenadores` (
  `entrenador` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `amarillas` int DEFAULT '0',
  `rojas` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entrenadores`
--

LOCK TABLES `Entrenadores` WRITE;
/*!40000 ALTER TABLE `Entrenadores` DISABLE KEYS */;
INSERT INTO `Entrenadores` VALUES ('tato',0,0),('adri',10,50),('pablo',0,0);
/*!40000 ALTER TABLE `Entrenadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Entrenamientos`
--

DROP TABLE IF EXISTS `Entrenamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Entrenamientos` (
  `numEntrenamiento` int NOT NULL,
  `fecha` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `dia` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `dorsal` int NOT NULL,
  `jugador` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `asistencia` int NOT NULL DEFAULT '0',
  `rendimiento` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entrenamientos`
--

LOCK TABLES `Entrenamientos` WRITE;
/*!40000 ALTER TABLE `Entrenamientos` DISABLE KEYS */;
INSERT INTO `Entrenamientos` VALUES (1,'2020-08-23','Lunes',1,'Adrian',1,2),(1,'2020-08-23','Lunes',13,'Jorge A',1,2),(1,'2020-08-23','Lunes',2,'Raul',1,3),(1,'2020-08-23','Lunes',3,'Ruben',1,2),(1,'2020-08-23','Lunes',5,'Fernando',1,2),(1,'2020-08-23','Lunes',4,'Aitor',1,4),(1,'2020-08-23','Lunes',6,'Ramon',1,4),(1,'2020-08-23','Lunes',7,'Dani San',1,3),(1,'2020-08-23','Lunes',8,'Diego',0,0),(1,'2020-08-23','Lunes',9,'Eneko',1,3),(1,'2020-08-23','Lunes',10,'Jorge P',1,2),(1,'2020-08-23','Lunes',11,'Rojo A',1,2),(1,'2020-08-23','Lunes',12,'Adrian G',0,0),(1,'2020-08-23','Lunes',14,'Alex P',0,0),(1,'2020-08-23','Lunes',15,'Sergio',1,2),(1,'2020-08-23','Lunes',16,'Noriega',1,2),(1,'2020-08-23','Lunes',17,'Pablo C',1,3),(1,'2020-08-23','Lunes',18,'Dani Go',1,3),(1,'2020-08-23','Lunes',19,'Alex',1,1),(1,'2020-08-23','Lunes',20,'Chicho',1,1),(1,'2020-08-23','Lunes',21,'Dani Gu',1,2),(1,'2020-08-23','Lunes',22,'Nico',1,3),(1,'2020-08-23','Lunes',23,'Cantero',1,2),(2,'2020-08-25','Miercoles',1,'Adrian',1,2),(2,'2020-08-25','Miercoles',13,'Jorge A',1,2),(2,'2020-08-25','Miercoles',2,'Raul',1,3),(2,'2020-08-25','Miercoles',3,'Ruben',1,2),(2,'2020-08-25','Miercoles',5,'Fernando',0,0),(2,'2020-08-25','Miercoles',4,'Aitor',1,4),(2,'2020-08-25','Miercoles',6,'Ramon',1,4),(2,'2020-08-25','Miercoles',7,'Dani San',1,4),(2,'2020-08-25','Miercoles',8,'Diego',0,0),(2,'2020-08-25','Miercoles',9,'Eneko',1,3),(2,'2020-08-25','Miercoles',10,'Jorge P',1,3),(2,'2020-08-25','Miercoles',11,'Rojo A',1,3),(2,'2020-08-25','Miercoles',12,'Adrian G',1,2),(2,'2020-08-25','Miercoles',14,'Alex P',0,0),(2,'2020-08-25','Miercoles',15,'Sergio',1,2),(2,'2020-08-25','Miercoles',16,'Noriega',0,0),(2,'2020-08-25','Miercoles',17,'Pablo C',1,3),(2,'2020-08-25','Miercoles',18,'Dani Go',1,3),(2,'2020-08-25','Miercoles',19,'Alex',1,2),(2,'2020-08-25','Miercoles',20,'Chicho',1,2),(2,'2020-08-25','Miercoles',21,'Dani Gu',1,2),(2,'2020-08-25','Miercoles',22,'Nico',0,0),(2,'2020-08-25','Miercoles',23,'Cantero',1,2),(0,NULL,'Miercoles',1,'Adrian',0,0),(0,NULL,'Miercoles',13,'Jorge A',0,0),(0,NULL,'Miercoles',2,'Raul',0,0),(0,NULL,'Miercoles',3,'Ruben',0,0),(0,NULL,'Miercoles',5,'Fernando',0,0),(0,NULL,'Miercoles',4,'Aitor',0,0),(0,NULL,'Miercoles',6,'Ramon',0,0),(0,NULL,'Miercoles',7,'Dani San',0,0),(0,NULL,'Miercoles',8,'Diego',0,0),(0,NULL,'Miercoles',9,'Eneko',0,0),(0,NULL,'Miercoles',10,'Jorge P',0,0),(0,NULL,'Miercoles',11,'Rojo A',0,0),(0,NULL,'Miercoles',12,'Adrian G',0,0),(0,NULL,'Miercoles',14,'Alex P',0,0),(0,NULL,'Miercoles',15,'Sergio',0,0),(0,NULL,'Miercoles',16,'Noriega',0,0),(0,NULL,'Miercoles',17,'Pablo C',0,0),(0,NULL,'Miercoles',18,'Dani Go',0,0),(0,NULL,'Miercoles',19,'Alex',0,0),(0,NULL,'Miercoles',20,'Chicho',0,0),(0,NULL,'Miercoles',21,'Dani Gu',0,0),(0,NULL,'Miercoles',22,'Nico',0,0),(0,NULL,'Miercoles',22,'Cantero',0,0);
/*!40000 ALTER TABLE `Entrenamientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jugadores`
--

DROP TABLE IF EXISTS `Jugadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Jugadores` (
  `dorsal` int unsigned NOT NULL AUTO_INCREMENT,
  `jugador` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `posicion` varchar(10) DEFAULT NULL,
  `numEntrenamientos` int NOT NULL DEFAULT '0',
  `rendEntrenamientos` double DEFAULT NULL,
  `numPartidos` int DEFAULT NULL,
  `rendPartidos` double DEFAULT NULL,
  PRIMARY KEY (`dorsal`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jugadores`
--

LOCK TABLES `Jugadores` WRITE;
/*!40000 ALTER TABLE `Jugadores` DISABLE KEYS */;
INSERT INTO `Jugadores` VALUES (1,'Adrian','POR',2,2,0,5),(2,'Raul','LD',2,2,0,5),(3,'Ruben','LI',2,2,0,5),(4,'Aitor','DFC',2,2,0,5),(5,'Fernando','DFC',1,2,0,5),(6,'Ramon','LD',2,2,0,5),(7,'Dani San','MC',2,2,0,5),(8,'Diego','MC',0,2,0,5),(9,'Eneko','DC',2,2,0,5),(10,'Jorge P','MC',2,2,0,5),(11,'Rojo A','ED',2,2,0,5),(12,'Adrian G','?',1,2,0,5),(13,'Jorge A','POR',2,2,0,5),(14,'Alex P','DFC',0,2,0,5),(15,'Sergio','MC',2,2,0,5),(16,'Noriega','EI',1,2,0,5),(17,'Pablo C','ED',2,2,0,5),(18,'Dani Go','MC',2,2,0,5),(19,'Alex','DC',2,2,0,5),(20,'Chicho','DFC',2,2,0,5),(21,'Dani Gu','?',2,2,0,5),(22,'Nico','ED',1,2,0,5),(23,'Cantero','LI',2,2,0,5);
/*!40000 ALTER TABLE `Jugadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Partidos`
--

DROP TABLE IF EXISTS `Partidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Partidos` (
  `numPartido` int NOT NULL,
  `fecha` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `rival` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `campo` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `resultado` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `dorsal` int DEFAULT NULL,
  `jugador` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `convocado` int NOT NULL DEFAULT '0',
  `titular` int NOT NULL DEFAULT '0',
  `minutos` bigint NOT NULL DEFAULT '0',
  `posicion` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `asistencias` int NOT NULL DEFAULT '0',
  `goles` int NOT NULL DEFAULT '0',
  `amarillas` int NOT NULL DEFAULT '0',
  `roja` int NOT NULL DEFAULT '0',
  `rendimiento` int NOT NULL DEFAULT '0',
  `mvp` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Partidos`
--

LOCK TABLES `Partidos` WRITE;
/*!40000 ALTER TABLE `Partidos` DISABLE KEYS */;
INSERT INTO `Partidos` VALUES (0,'2021-09-26','vimenor','fuera','7-0',9,'Eneko',1,1,80,'DC',3,5,1,0,10,1),(1,'2021-10-10','santillana a','casa','7-0',9,'Eneko',1,1,80,'DC',3,17,1,1,8,1),(2,'2022-01-09','santillana a','fuera','7-0',9,'Eneko',1,1,20,'DC',0,0,1,1,5,0),(2,'2022-01-09','santillana a','fuera','7-0',9,'Ramon',1,1,20,'DC',0,0,1,1,5,0);
/*!40000 ALTER TABLE `Partidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-31 21:13:53
