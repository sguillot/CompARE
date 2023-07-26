-- MySQL dump 10.13  Distrib 5.7.24, for osx10.9 (x86_64)
--
-- Host: localhost    Database: compare3
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `assumptions_ns`
--

DROP TABLE IF EXISTS `assumptions_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assumptions_ns` (
  `id_Assumptions` int NOT NULL AUTO_INCREMENT,
  `AssumptionsPrimary` varchar(60) DEFAULT NULL,
  `AssumptionsSecondary` varchar(60) DEFAULT NULL,
  `AssumptionsDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`id_Assumptions`)
) ENGINE=InnoDB AUTO_INCREMENT=770 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assumptions_ns`
--

LOCK TABLES `assumptions_ns` WRITE;
/*!40000 ALTER TABLE `assumptions_ns` DISABLE KEYS */;
INSERT INTO `assumptions_ns` VALUES (757,'Atmosphere Composition','hydrogen','At the surface of a neutron star, elements stratify on time scales of minutes/hours leaving the lightest on top (Romani 1987). Also, the thickness of the last scattering layer of a NS is on the order of a few cm. Therefore, it is common to assume a single composition, being that of the lightest element. Hydrogen is therefore a reasonable assumption for the composition, especially for a NS that has accreted matter from a companion star. Other effects are in competition and may put some uncertainties on the surface composition, namely, accretion from the interstellar medium, diffuse nuclear burning of light of H into He (Chang & Bildsten 2003, 2004), and spallation of heavier elements into lighter ones (Bildsten et al. 1992).'),(758,'\nMagnetic field','\nnon-magnetic','This analyses also assume emission from a low-magnetic field neutron stars (as typically measured for MSPs, specifically B_dip ~ 2.8e8 G for PSR J0437-4715). The atmosphere model is that of a non-magnetised atmosphere, which is a good approximation as B-field effect (modified opacities) become important above 1e10 G. However, this neglects potential high-magnetic loop near the NS surface.'),(759,'\nRotation','\nnon-rotating','The relativistic effects of rotation on the emergent spectrum are neglected in this analysis. However, the effects on the radius are < 1 km at the rotational frequency of PSR J0437-4715 (173.6 Hz), see Baubock et al. 2015). '),(760,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature (modulo the contribution of the hot spots)'),(761,'\nInterstellar medium','\nsolar abundances','The modelling of the x-ray absorption (with the tbabs model) assumes solar abundances for the interstellar medium, a reasonable assumption for a pulsar located at 156 pc.'),(762,'\nPrior','\ndistance prior','The radio timing of the pulsar provided priors on the pulsar mass (1.44Msun), see Reardon et al. 2016. No uncertainties on this measurement was included in the analysis. '),(763,' Prior',' mass prior','The radio timing of the pulsar provided priors on the pulsar distance (156.79 pc), see Reardon et al. 2016. No uncertainties on this measurement was included in the analysis.'),(764,' Prior',' redenning prior','The reddening was also provided as a prior, using estimation for Galactic dust maps:  E(B-V) = 0.002+/-0.014 (Lallement et al. 2018).'),(765,'Atmosphere Composition','helium','At the surface of a neutron star, elements stratify on time scales of minutes/hours leaving the lightest on top (Romani 1987). Also, the thickness of the last scattering layer of a NS is on the order of a few cm. Therefore, it is common to assume a single composition, being that of the lightest element. If no Hydrogen is present in the system, the next expected element is Helium, which is a possibility if the NS has accreted only Helium from a companion star. Other effects are in competition and may put some uncertainties on the surface composition, namely, accretion from the interstellar medium, diffuse nuclear burning of light of H into He (Chang & Bildsten 2003, 2004), and spallation of heavier elements into lighter ones (Bildsten et al. 1992).'),(766,'\nRotation','\nnon-rotating','The relativistic effects of rotation on the emergent spectrum are neglected in this analysis. However, the effects on the radius are < 1 % at the rotational frequency of PSR J0437-4715 (173.6 Hz), see Baubock et al. 2015. '),(767,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature (modulo the contribution of the hot spots).'),(768,'Gravitation theory','General relativity','The estimation of the post-Keplerian parameters and Shapiro delay were done assuming general relativity as the theory of gravitation'),(769,NULL,NULL,NULL);
/*!40000 ALTER TABLE `assumptions_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (8,'coldMSP'),(4,'NS Mass'),(2,'NS Spin'),(5,'NS-NS_mergers'),(6,'PPM'),(7,'qLMXB'),(9,'Thermal INSs'),(3,'Transiently Accreting NS'),(10,'Type-I X-ray bursts');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add constrain ns',7,'add_constrainns'),(26,'Can change constrain ns',7,'change_constrainns'),(27,'Can delete constrain ns',7,'delete_constrainns'),(28,'Can view constrain ns',7,'view_constrainns'),(29,'Can add method ns',8,'add_methodns'),(30,'Can change method ns',8,'change_methodns'),(31,'Can delete method ns',8,'delete_methodns'),(32,'Can view method ns',8,'view_methodns'),(33,'Can add name ns',9,'add_namens'),(34,'Can change name ns',9,'change_namens'),(35,'Can delete name ns',9,'delete_namens'),(36,'Can view name ns',9,'view_namens'),(37,'Can add ns',10,'add_ns'),(38,'Can change ns',10,'change_ns'),(39,'Can delete ns',10,'delete_ns'),(40,'Can view ns',10,'view_ns'),(41,'Can add ref ns',11,'add_refns'),(42,'Can change ref ns',11,'change_refns'),(43,'Can delete ref ns',11,'delete_refns'),(44,'Can view ref ns',11,'view_refns'),(45,'Can add assumptions ns',12,'add_assumptionsns'),(46,'Can change assumptions ns',12,'change_assumptionsns'),(47,'Can delete assumptions ns',12,'delete_assumptionsns'),(48,'Can view assumptions ns',12,'view_assumptionsns'),(49,'Can add ns to assumptions',13,'add_nstoassumptions'),(50,'Can change ns to assumptions',13,'change_nstoassumptions'),(51,'Can delete ns to assumptions',13,'delete_nstoassumptions'),(52,'Can view ns to assumptions',13,'view_nstoassumptions'),(53,'Can add model ns',14,'add_modelns'),(54,'Can change model ns',14,'change_modelns'),(55,'Can delete model ns',14,'delete_modelns'),(56,'Can view model ns',14,'view_modelns'),(57,'Can add ns to model',15,'add_nstomodel'),(58,'Can change ns to model',15,'change_nstomodel'),(59,'Can delete ns to model',15,'delete_nstomodel'),(60,'Can view ns to model',15,'view_nstomodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$jIhPfL8hS5HpsIPk704mnS$0tHtY0TSJt3JQKMWYbyOYkitJhE/hTwJ3G88SWFmpkc=','2023-06-21 09:20:59.807159',1,'root','','','',1,1,'2023-04-24 14:57:09.161937'),(2,'pbkdf2_sha256$600000$zrvy554j2FYIO1SwrxLuc1$oE09WJ9lIMo6S3LruGjkL3ydrCxM5Izgsu9bP/c9jGU=','2023-04-26 08:35:18.741259',0,'vincent','','','',0,1,'2023-04-26 07:31:16.000000'),(3,'pbkdf2_sha256$600000$HKNXHsshde3Ww35HEqk3Lp$HQougSfuRKwN48usmwnlXXiaQgwWqSLmX7jEFQ425A4=','2023-06-09 07:22:24.599195',0,'v','','','',0,1,'2023-05-04 12:38:15.000000'),(4,'pbkdf2_sha256$600000$moFzAIdW9KH0dviUIjl2xe$YOsyEAzDFkRUYHggv/lGuGBoNWJKoiH8JVV7iQkusdU=','2023-05-15 07:28:08.805407',0,'t','','','',0,1,'2023-05-09 08:10:03.000000'),(5,'pbkdf2_sha256$600000$Syr00a8j2MWUKwm9s0c4ty$u+9lkyZW5MLVVyREfZgyTmLqgbbxJ4YBZtbFQdy3GE4=','2023-05-15 14:54:45.123993',0,'usertest','','','',0,1,'2023-05-15 14:53:58.000000'),(6,'pbkdf2_sha256$600000$trlTMsBRkLlVDYxoSzcao4$OwD5NSyA7Pu+mij4umFL+CtLvRXtW6QO1ELqiyT0++I=','2023-07-26 09:18:27.338439',0,'sg','','','',0,1,'2023-05-17 07:45:34.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (3,2,3),(1,2,8),(2,2,9),(10,3,8),(13,4,7),(14,4,8),(16,5,7),(15,5,8),(17,6,2),(18,6,3),(19,6,4),(20,6,5),(21,6,6),(22,6,7),(23,6,8),(24,6,9),(25,6,10);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constrain_ns`
--

DROP TABLE IF EXISTS `constrain_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `constrain_ns` (
  `id_Constrain` int NOT NULL AUTO_INCREMENT,
  `ConstrainType` enum('MCMC samples','Posterior samples','Quantiles','mean +/- 1 sigma') NOT NULL,
  `constrainvariable` enum('M','R','M-R','F','L','M-L') NOT NULL,
  `ConstrainVersion` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_Constrain`)
) ENGINE=InnoDB AUTO_INCREMENT=269 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constrain_ns`
--

LOCK TABLES `constrain_ns` WRITE;
/*!40000 ALTER TABLE `constrain_ns` DISABLE KEYS */;
INSERT INTO `constrain_ns` VALUES (265,'MCMC samples','M-R',1),(266,'mean +/- 1 sigma','M',1),(267,'mean +/- 1 sigma','M',2),(268,'mean +/- 1 sigma','F',1);
/*!40000 ALTER TABLE `constrain_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-04-26 07:30:08.723043','1','Add and View',1,'[{\"added\": {}}]',3,1),(2,'2023-04-26 07:30:13.888209','1','Add and View',2,'[]',3,1),(3,'2023-04-26 07:31:16.937829','2','vincent',1,'[{\"added\": {}}]',4,1),(4,'2023-04-26 08:13:03.335594','2','NS Spin',1,'[{\"added\": {}}]',3,1),(5,'2023-04-26 08:13:15.540345','1','Add and View',3,'',3,1),(6,'2023-04-26 08:13:44.859017','3','Transiently Accreting NS',1,'[{\"added\": {}}]',3,1),(7,'2023-04-26 08:13:56.008137','4','NS Mass',1,'[{\"added\": {}}]',3,1),(8,'2023-04-26 08:14:03.301892','5','NS-NS_mergers',1,'[{\"added\": {}}]',3,1),(9,'2023-04-26 08:14:08.493832','6','PPM',1,'[{\"added\": {}}]',3,1),(10,'2023-04-26 08:14:12.988344','7','qLMXB',1,'[{\"added\": {}}]',3,1),(11,'2023-04-26 08:14:18.138490','8','Cold MSPs',1,'[{\"added\": {}}]',3,1),(12,'2023-04-26 08:14:25.185006','9','Thermal INSs',1,'[{\"added\": {}}]',3,1),(13,'2023-04-26 08:14:30.626567','10','Type-I X-ray bursts',1,'[{\"added\": {}}]',3,1),(14,'2023-04-26 08:14:51.232629','2','vincent',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(15,'2023-05-04 12:38:15.910624','3','v',1,'[{\"added\": {}}]',4,1),(16,'2023-05-05 09:34:40.301397','3','v',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(17,'2023-05-05 09:51:54.608576','3','v',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(18,'2023-05-05 10:13:08.003241','8','coldMSP',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',3,1),(19,'2023-05-09 08:10:03.760294','4','t',1,'[{\"added\": {}}]',4,1),(20,'2023-05-09 08:10:13.579728','4','t',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(21,'2023-05-10 09:17:43.340026','4','t',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(22,'2023-05-15 14:53:58.972537','5','usertest',1,'[{\"added\": {}}]',4,1),(23,'2023-05-15 14:54:22.019333','5','usertest',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(24,'2023-05-17 07:45:35.478560','6','sg',1,'[{\"added\": {}}]',4,1),(25,'2023-05-17 07:45:45.398746','6','sg',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(12,'compare','assumptionsns'),(7,'compare','constrainns'),(8,'compare','methodns'),(14,'compare','modelns'),(9,'compare','namens'),(10,'compare','ns'),(13,'compare','nstoassumptions'),(15,'compare','nstomodel'),(11,'compare','refns'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-12 07:27:46.250375'),(2,'auth','0001_initial','2023-04-12 07:27:46.753844'),(3,'admin','0001_initial','2023-04-12 07:27:46.946037'),(4,'admin','0002_logentry_remove_auto_add','2023-04-12 07:27:46.961657'),(5,'admin','0003_logentry_add_action_flag_choices','2023-04-12 07:27:46.978238'),(6,'contenttypes','0002_remove_content_type_name','2023-04-12 07:27:47.120014'),(7,'auth','0002_alter_permission_name_max_length','2023-04-12 07:27:47.191127'),(8,'auth','0003_alter_user_email_max_length','2023-04-12 07:27:47.240594'),(9,'auth','0004_alter_user_username_opts','2023-04-12 07:27:47.256464'),(10,'auth','0005_alter_user_last_login_null','2023-04-12 07:27:47.328274'),(11,'auth','0006_require_contenttypes_0002','2023-04-12 07:27:47.334324'),(12,'auth','0007_alter_validators_add_error_messages','2023-04-12 07:27:47.352398'),(13,'auth','0008_alter_user_username_max_length','2023-04-12 07:27:47.431628'),(14,'auth','0009_alter_user_last_name_max_length','2023-04-12 07:27:47.507476'),(15,'auth','0010_alter_group_name_max_length','2023-04-12 07:27:47.545013'),(16,'auth','0011_update_proxy_permissions','2023-04-12 07:27:47.560473'),(17,'auth','0012_alter_user_first_name_max_length','2023-04-12 07:27:47.632717'),(18,'sessions','0001_initial','2023-04-12 07:27:47.671109'),(19,'compare','0001_initial','2023-04-12 10:25:10.550121'),(20,'compare','0002_alter_assumptionsns_options_and_more','2023-05-12 08:43:38.146061'),(21,'compare','0003_constrainns_constrainvariable_ns_id_constrain_and_more','2023-05-24 08:30:36.247454'),(22,'compare','0004_alter_assumptionsns_assumptionsdescription_and_more','2023-05-24 08:30:36.257978'),(23,'compare','0005_alter_constrainns_constrainvariable','2023-05-24 08:32:03.354445');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4xa2dkp01kzrq02f5jxftzjrigmlyzi0','.eJxVjEEOwiAQRe_C2hAGHAou3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIirDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqt9dmycUYnhd64jOQyOMdRgzXMRSEm8AYKFK8Lki3shwhaxQEzcAHx_gDHZzd2:1qOaf5:pk2OJ76DiU1B5GfGBEVm7gmFu_Uk_ewpUQPFAgOK8WI','2023-08-09 09:18:27.340606'),('af27azqe98h45c353p5lyxjur8dwoe4k','.eJxVjEEOwiAQRe_C2hAGHAou3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIirDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqt9dmycUYnhd64jOQyOMdRgzXMRSEm8AYKFK8Lki3shwhaxQEzcAHx_gDHZzd2:1qBu5K:hxT7PptW9h3rECEFLdZUbgYXvHNK-H0bi3SUqeLClQA','2023-07-05 09:25:06.914202'),('y33pqcs67pamc8qjntp7z1v9avs4d503','.eJxVjDsOwjAQBe_iGllr5M-Gkp4zWGvvggPIluKkirg7iZQC2jczb1WRlrnEpcsUR1YXZdTpd0uUX1J3wE-qj6Zzq_M0Jr0r-qBd3xrL-3q4fweFetlqQmGXPVIOAJ4pWXByRhqIMWVEIHvHAB5AQh7IihFjHaBDTpvi1ecL-NI4MQ:1qBEOH:2-d4IvR_kZj-RWp6NODkQlx9adY1s6ftBgeKjhieQ2g','2023-07-03 12:53:53.536921');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `method_ns`
--

DROP TABLE IF EXISTS `method_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `method_ns` (
  `id_Method` int NOT NULL AUTO_INCREMENT,
  `Method` enum('Pulsar timing','Thermal emission') NOT NULL,
  `Method_Specific` text NOT NULL,
  `ProcessinfInfo` text NOT NULL,
  `DataDate` text NOT NULL,
  PRIMARY KEY (`id_Method`)
) ENGINE=InnoDB AUTO_INCREMENT=474 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `method_ns`
--

LOCK TABLES `method_ns` WRITE;
/*!40000 ALTER TABLE `method_ns` DISABLE KEYS */;
INSERT INTO `method_ns` VALUES (468,'Thermal emission','Spectral fitting (FUV and Xray data)','See Kargalstev2004, Durant2012, Guillot2016','FUV (Kargalstev2004 + Durant2012), X-ray (Rosat, up to 0.3 keV)'),(469,'Thermal emission','Spectral fitting (FUV and Xray data)','See Kargalstev2004, Durant2012, Guillot2016','FUV (Kargalstev2004 + Durant2012), X-ray (Guillot2016, Rosat, up to 0.3 keV)'),(470,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo2 packages','NANOGrav 15-year (2008-2022)'),(471,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo2 packages','NANOGrav 11-year (2008-2016)'),(472,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo packages','GBT 20131214-20200406 and CHIME 20190203-20200506'),(473,'Pulsar timing','Frequency measurement','psrchive and Tempo packages','June 2004 to May 2005');
/*!40000 ALTER TABLE `method_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_ns`
--

DROP TABLE IF EXISTS `model_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_ns` (
  `id_Model` int NOT NULL AUTO_INCREMENT,
  `DependenciesPrimary` varchar(60) DEFAULT NULL,
  `DependenciesSecondary` varchar(60) DEFAULT NULL,
  `DependeciesDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `CaveatsReferences` text,
  PRIMARY KEY (`id_Model`)
) ENGINE=InnoDB AUTO_INCREMENT=419 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_ns`
--

LOCK TABLES `model_ns` WRITE;
/*!40000 ALTER TABLE `model_ns` DISABLE KEYS */;
INSERT INTO `model_ns` VALUES (407,'atmosphere','Gonzalez2019','The atmosphere model used in this analysis was calculated for low-temperature atmosphere (<10^5.5 K) and includes the effect of plasma.','2019MNRAS.490.5848G 1987ApJ...313..718R 2003ApJ...585..464C 2004ApJ...616L.147C'),(408,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using absorption tables based on the tbabs model of Wilms et al. 2020.',' 1992ApJ...384..143B'),(409,'\nredenning','\nClayton2003','The frequency-dependent reddenning has been implemented based on results of Clayton et al. 2003 (Fig.1).',' 2015ApJ...799...22B'),(410,'\nhot spots model','\n2 blackbodies','The contribution of the two hot spots to the X-ray spectrum analysed (<0.3 keV) was included using 2 blackbody components.',' 2018A&A...616A.132L'),(411,'atmosphere','Gonzalez2019','The atmosphere model used in this analysis was calculated for low-temperature atmosphere (<10^5.5 K) and includes the effect of plasma.','2019MNRAS.490.5848G 1987ApJ...313..718R 2003ApJ...585..464C'),(412,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using absorption tables based on the tbabs model of Wilms et al. 2020.',' 2004ApJ...616L.147C'),(413,'\nredenning','\nClayton2003','The frequency-dependent reddenning has been implemented based on results of Clayton et al. 2003 (Fig.1).',' 1992ApJ...384..143B'),(414,'\nhot spots model','\nignored','The contribution of the hot spots to the X-ray spectrum analysed (<0.3 keV) was ignored.',' 2015ApJ...799...22B'),(415,'Shapiro delay','m_c sini parametrization','The Shapiro delay is estimated using the traditional Mcomp and sini parametrization','2023ApJL..951...L9'),(416,'Shapiro delay','m_c sini parametrization','The Shapiro delay is estimated using the traditional Mcomp and sini parametrization','2018ApJS..235...37A'),(417,'Dispersion measure','DMX','Three different piece-wise DMX models were employed in the analysis of Fonseca et al. 2021 and the averaged mass from these 3 analyses was reported.','2021ApJ...915L..12F'),(418,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `model_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `name_ns`
--

DROP TABLE IF EXISTS `name_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `name_ns` (
  `id_Name` int NOT NULL AUTO_INCREMENT,
  `NameDB` varchar(50) NOT NULL,
  `ClassDB` varchar(50) NOT NULL,
  `NameSimbad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ClassSimbad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `RA` decimal(20,10) DEFAULT NULL,
  `Declination` decimal(20,10) DEFAULT NULL,
  `LocalisationFile` text,
  `EventDate` date DEFAULT NULL,
  PRIMARY KEY (`id_Name`)
) ENGINE=InnoDB AUTO_INCREMENT=439 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `name_ns`
--

LOCK TABLES `name_ns` WRITE;
/*!40000 ALTER TABLE `name_ns` DISABLE KEYS */;
INSERT INTO `name_ns` VALUES (435,'PSR J0437-4715','Cold MSP','PSR J0437-47','Psr',69.3158310000,-47.2523730000,NULL,NULL),(436,'PSR J1614-2230','NS mass','PSR J1614-2230','Psr',243.6521120000,-22.5086690000,NULL,NULL),(437,'PSR J0740+6620','NS mass','PSR J0740+6620','Psr',115.1908290000,66.3426670000,NULL,NULL),(438,'PSR J1748-2446ad','NS spin','PSR J1748-2446ad','Psr',267.0204170000,-24.7677780000,NULL,NULL);
/*!40000 ALTER TABLE `name_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns`
--

DROP TABLE IF EXISTS `ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ns` (
  `FileName` varchar(100) NOT NULL,
  `FilePath` text NOT NULL,
  `id_ref` int DEFAULT NULL,
  `id_Name` int DEFAULT NULL,
  `id_Method` int DEFAULT NULL,
  `id_Constrain` int DEFAULT NULL,
  PRIMARY KEY (`FileName`),
  KEY `id_ref` (`id_ref`),
  KEY `id_Name` (`id_Name`),
  KEY `id_Method` (`id_Method`),
  KEY `id_Constrain` (`id_Constrain`),
  CONSTRAINT `ns_ibfk_1` FOREIGN KEY (`id_ref`) REFERENCES `ref_ns` (`id_Ref`),
  CONSTRAINT `ns_ibfk_2` FOREIGN KEY (`id_Name`) REFERENCES `name_ns` (`id_Name`),
  CONSTRAINT `ns_ibfk_3` FOREIGN KEY (`id_Method`) REFERENCES `method_ns` (`id_Method`),
  CONSTRAINT `ns_ibfk_4` FOREIGN KEY (`id_Constrain`) REFERENCES `constrain_ns` (`id_Constrain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ns`
--

LOCK TABLES `ns` WRITE;
/*!40000 ALTER TABLE `ns` DISABLE KEYS */;
INSERT INTO `ns` VALUES ('Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt','qdsdsqdsqdsq.txt',376,435,469,265),('Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt','qdsdsqdsqdsq.txt',376,435,468,265),('NS_Mass-PSRJ0740+6620-2020-mass-shapiro-1.txt','qdsdsqdsqdsq.txt',379,437,472,266),('NS_Mass-PSRJ1614-2230-NANOgrav11yr-mass-shapiro-1.txt','qdsdsqdsqdsq.txt',378,436,471,267),('NS_Mass-PSRJ1614-2230-NANOgrav15yr-mass-shapiro-2.txt','qdsdsqdsqdsq.txt',377,436,470,266),('NS_Spin-PSRJ1748-2446ad-2005-spin-1.txt','qdsdsqdsqdsq.txt',380,438,473,268);
/*!40000 ALTER TABLE `ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns_to_assumptions`
--

DROP TABLE IF EXISTS `ns_to_assumptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ns_to_assumptions` (
  `id_ns_to_assumptions` int NOT NULL AUTO_INCREMENT,
  `id_Assumptions` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_assumptions`),
  UNIQUE KEY `Uni_cons` (`id_Assumptions`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_assumptions_ibfk_1` FOREIGN KEY (`id_Assumptions`) REFERENCES `assumptions_ns` (`id_Assumptions`),
  CONSTRAINT `ns_to_assumptions_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=2779 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ns_to_assumptions`
--

LOCK TABLES `ns_to_assumptions` WRITE;
/*!40000 ALTER TABLE `ns_to_assumptions` DISABLE KEYS */;
INSERT INTO `ns_to_assumptions` VALUES (2760,757,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2769,758,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2761,758,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2762,759,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2763,760,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2772,761,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2764,761,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2773,762,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2765,762,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2774,763,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2766,763,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2767,764,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(2768,765,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2770,766,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2771,767,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(2777,768,'NS_Mass-PSRJ0740+6620-2020-mass-shapiro-1.txt'),(2776,768,'NS_Mass-PSRJ1614-2230-NANOgrav11yr-mass-shapiro-1.txt'),(2775,768,'NS_Mass-PSRJ1614-2230-NANOgrav15yr-mass-shapiro-2.txt'),(2778,769,'NS_Spin-PSRJ1748-2446ad-2005-spin-1.txt');
/*!40000 ALTER TABLE `ns_to_assumptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns_to_model`
--

DROP TABLE IF EXISTS `ns_to_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ns_to_model` (
  `id_ns_to_model` int NOT NULL AUTO_INCREMENT,
  `id_Model` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_model`),
  UNIQUE KEY `Uni_con_mod` (`id_Model`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_model_ibfk_1` FOREIGN KEY (`id_Model`) REFERENCES `model_ns` (`id_Model`),
  CONSTRAINT `ns_to_model_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=1127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ns_to_model`
--

LOCK TABLES `ns_to_model` WRITE;
/*!40000 ALTER TABLE `ns_to_model` DISABLE KEYS */;
INSERT INTO `ns_to_model` VALUES (1115,407,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(1116,408,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(1117,409,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(1118,410,'Cold_MSP-PSRJ0437-4715-2019-massradius-hydrogen-1.txt'),(1119,411,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(1120,412,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(1121,413,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(1122,414,'Cold_MSP-PSRJ0437-4715-2019-massradius-helium-1.txt'),(1123,415,'NS_Mass-PSRJ1614-2230-NANOgrav15yr-mass-shapiro-2.txt'),(1124,416,'NS_Mass-PSRJ1614-2230-NANOgrav11yr-mass-shapiro-1.txt'),(1125,417,'NS_Mass-PSRJ0740+6620-2020-mass-shapiro-1.txt'),(1126,418,'NS_Spin-PSRJ1748-2446ad-2005-spin-1.txt');
/*!40000 ALTER TABLE `ns_to_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref_ns`
--

DROP TABLE IF EXISTS `ref_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ref_ns` (
  `id_Ref` int NOT NULL AUTO_INCREMENT,
  `Author` varchar(30) NOT NULL,
  `RefYear` int NOT NULL,
  `Short` varchar(50) NOT NULL,
  `Bibtex` text NOT NULL,
  `DOI` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `RepositoryDOI` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DataLink` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_Ref`)
) ENGINE=InnoDB AUTO_INCREMENT=381 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref_ns`
--

LOCK TABLES `ref_ns` WRITE;
/*!40000 ALTER TABLE `ref_ns` DISABLE KEYS */;
INSERT INTO `ref_ns` VALUES (376,'Gonzalez-Canuilef',2019,'2019MNRAS.490.5848G','@ARTICLE{2019MNRAS.490.5848G,\n       author = {{Gonz{\\\'a}lez-Caniulef}, Denis and {Guillot}, Sebastien and {Reisenegger}, Andreas},\n        title = \"{Neutron star radius measurement from the ultraviolet and soft X-ray thermal emission of PSR J0437-4715}\",\n      journal = {\\mnras},\n     keywords = {dense matter, equation of state, plasmas, stars: atmospheres, stars: neutron, pulsars: individual (PSR J0437-4715), Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2019,\n        month = dec,\n       volume = {490},\n       number = {4},\n        pages = {5848-5859},\n          doi = {10.1093/mnras/stz2941},\narchivePrefix = {arXiv},\n       eprint = {1904.12114},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.5848G},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}\n\n','10.1093/mnras/stz2941',NULL,NULL),(377,'Agazie',2023,'2023ApJL..951...L9','@ARTICLE{2018ApJS..235...37A,\n       author = {{Arzoumanian}, Zaven and {Brazier}, Adam and {Burke-Spolaor}, Sarah and {Chamberlin}, Sydney and {Chatterjee}, Shami and {Christy}, Brian and {Cordes}, James M. and {Cornish}, Neil J. and {Crawford}, Fronefield and {Thankful Cromartie}, H. and {Crowter}, Kathryn and {DeCesar}, Megan E. and {Demorest}, Paul B. and {Dolch}, Timothy and {Ellis}, Justin A. and {Ferdman}, Robert D. and {Ferrara}, Elizabeth C. and {Fonseca}, Emmanuel and {Garver-Daniels}, Nathan and {Gentile}, Peter A. and {Halmrast}, Daniel and {Huerta}, E.~A. and {Jenet}, Fredrick A. and {Jessup}, Cody and {Jones}, Glenn and {Jones}, Megan L. and {Kaplan}, David L. and {Lam}, Michael T. and {Lazio}, T. Joseph W. and {Levin}, Lina and {Lommen}, Andrea and {Lorimer}, Duncan R. and {Luo}, Jing and {Lynch}, Ryan S. and {Madison}, Dustin and {Matthews}, Allison M. and {McLaughlin}, Maura A. and {McWilliams}, Sean T. and {Mingarelli}, Chiara and {Ng}, Cherry and {Nice}, David J. and {Pennucci}, Timothy T. and {Ransom}, Scott M. and {Ray}, Paul S. and {Siemens}, Xavier and {Simon}, Joseph and {Spiewak}, Ren{\\\'e}e and {Stairs}, Ingrid H. and {Stinebring}, Daniel R. and {Stovall}, Kevin and {Swiggum}, Joseph K. and {Taylor}, Stephen R. and {Vallisneri}, Michele and {van Haasteren}, Rutger and {Vigeland}, Sarah J. and {Zhu}, Weiwei and {NANOGrav Collaboration}},\n        title = \"{The NANOGrav 11-year Data Set: High-precision Timing of 45 Millisecond Pulsars}\",\n      journal = {\\apjs},\n     keywords = {binaries: general, gravitational waves, parallaxes, proper motions, pulsars: general, stars: neutron},\n         year = 2018,\n        month = apr,\n       volume = {235},\n       number = {2},\n          eid = {37},\n        pages = {37},\n          doi = {10.3847/1538-4365/aab5b0},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2018ApJS..235...37A},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/acda9a',NULL,NULL),(378,'Arzoumanian',2018,'2018ApJS..235...37A','@ARTICLE{2018ApJS..235...37A,\n       author = {{Arzoumanian}, Zaven and {Brazier}, Adam and {Burke-Spolaor}, Sarah and {Chamberlin}, Sydney and {Chatterjee}, Shami and {Christy}, Brian and {Cordes}, James M. and {Cornish}, Neil J. and {Crawford}, Fronefield and {Thankful Cromartie}, H. and {Crowter}, Kathryn and {DeCesar}, Megan E. and {Demorest}, Paul B. and {Dolch}, Timothy and {Ellis}, Justin A. and {Ferdman}, Robert D. and {Ferrara}, Elizabeth C. and {Fonseca}, Emmanuel and {Garver-Daniels}, Nathan and {Gentile}, Peter A. and {Halmrast}, Daniel and {Huerta}, E.~A. and {Jenet}, Fredrick A. and {Jessup}, Cody and {Jones}, Glenn and {Jones}, Megan L. and {Kaplan}, David L. and {Lam}, Michael T. and {Lazio}, T. Joseph W. and {Levin}, Lina and {Lommen}, Andrea and {Lorimer}, Duncan R. and {Luo}, Jing and {Lynch}, Ryan S. and {Madison}, Dustin and {Matthews}, Allison M. and {McLaughlin}, Maura A. and {McWilliams}, Sean T. and {Mingarelli}, Chiara and {Ng}, Cherry and {Nice}, David J. and {Pennucci}, Timothy T. and {Ransom}, Scott M. and {Ray}, Paul S. and {Siemens}, Xavier and {Simon}, Joseph and {Spiewak}, Ren{\\\'e}e and {Stairs}, Ingrid H. and {Stinebring}, Daniel R. and {Stovall}, Kevin and {Swiggum}, Joseph K. and {Taylor}, Stephen R. and {Vallisneri}, Michele and {van Haasteren}, Rutger and {Vigeland}, Sarah J. and {Zhu}, Weiwei and {NANOGrav Collaboration}},\n        title = \"{The NANOGrav 11-year Data Set: High-precision Timing of 45 Millisecond Pulsars}\",\n      journal = {\\apjs},\n     keywords = {binaries: general, gravitational waves, parallaxes, proper motions, pulsars: general, stars: neutron},\n         year = 2018,\n        month = apr,\n       volume = {235},\n       number = {2},\n          eid = {37},\n        pages = {37},\n          doi = {10.3847/1538-4365/aab5b0},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2018ApJS..235...37A},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/1538-4365/aab5b0',NULL,NULL),(379,'Fonseca',2021,'2021ApJ...915L..12F','@ARTICLE{2021ApJ...915L..12F,\n       author = {{Fonseca}, E. and {Cromartie}, H.~T. and {Pennucci}, T.~T. and {Ray}, P.~S. and {Kirichenko}, A. Yu. and {Ransom}, S.~M. and {Demorest}, P.~B. and {Stairs}, I.~H. and {Arzoumanian}, Z. and {Guillemot}, L. and {Parthasarathy}, A. and {Kerr}, M. and {Cognard}, I. and {Baker}, P.~T. and {Blumer}, H. and {Brook}, P.~R. and {DeCesar}, M. and {Dolch}, T. and {Dong}, F.~A. and {Ferrara}, E.~C. and {Fiore}, W. and {Garver-Daniels}, N. and {Good}, D.~C. and {Jennings}, R. and {Jones}, M.~L. and {Kaspi}, V.~M. and {Lam}, M.~T. and {Lorimer}, D.~R. and {Luo}, J. and {McEwen}, A. and {McKee}, J.~W. and {McLaughlin}, M.~A. and {McMann}, N. and {Meyers}, B.~W. and {Naidu}, A. and {Ng}, C. and {Nice}, D.~J. and {Pol}, N. and {Radovan}, H.~A. and {Shapiro-Albert}, B. and {Tan}, C.~M. and {Tendulkar}, S.~P. and {Swiggum}, J.~K. and {Wahl}, H.~M. and {Zhu}, W.~W.},\n        title = \"{Refined Mass and Geometric Measurements of the High-mass PSR J0740+6620}\",\n      journal = {\\apjl},\n     keywords = {Neutron stars, Pulsars, General relativity, Compact objects, Binary pulsars, 1108, 1306, 641, 288, 153},\n         year = 2021,\n        month = jul,\n       volume = {915},\n       number = {1},\n          eid = {L12},\n        pages = {L12},\n          doi = {10.3847/2041-8213/ac03b8},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJ...915L..12F},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/ac03b8',NULL,NULL),(380,'Hessels',2006,'2006Sci...311.1901H','@ARTICLE{2006Sci...311.1901H,\n       author = {{Hessels}, Jason W.~T. and {Ransom}, Scott M. and {Stairs}, Ingrid H. and {Freire}, Paulo C.~C. and {Kaspi}, Victoria M. and {Camilo}, Fernando},\n        title = \"{A Radio Pulsar Spinning at 716 Hz}\",\n      journal = {Science},\n     keywords = {ASTRONOMY},\n         year = 2006,\n        month = mar,\n       volume = {311},\n       number = {5769},\n        pages = {1901-1904},\n          doi = {10.1126/science.1123430},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2006Sci...311.1901H},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}\n','10.1126/science.1123430',NULL,NULL);
/*!40000 ALTER TABLE `ref_ns` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-26 17:33:11
