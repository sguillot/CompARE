-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.31 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour compare3
CREATE DATABASE IF NOT EXISTS `compare3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `compare3`;

-- Listage de la structure de table compare3. assumptions_ns
CREATE TABLE IF NOT EXISTS `assumptions_ns` (
  `id_Assumptions` int NOT NULL AUTO_INCREMENT,
  `AssumptionsPrimary` varchar(60) DEFAULT NULL,
  `AssumptionsSecondary` varchar(60) DEFAULT NULL,
  `AssumptionsDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`id_Assumptions`)
) ENGINE=InnoDB AUTO_INCREMENT=696 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.assumptions_ns : ~9 rows (environ)
INSERT INTO `assumptions_ns` (`id_Assumptions`, `AssumptionsPrimary`, `AssumptionsSecondary`, `AssumptionsDescription`) VALUES
	(687, 'Atmosphere Composition', 'helium', 'description of composition assumption'),
	(688, 'Magnetic field', 'non-magneticdsdsdsdsq', 'description of B-field assumption'),
	(689, 'Rotation', 'non-rotating', 'description of slow rotation assumption'),
	(690, 'Prior', 'distance prior', 'description of distance prior assumption'),
	(691, 'Emitting fraction', 'full surface', 'description of full surface emission'),
	(692, 'Interstellar medium', 'solar abundances and Vern cross-sections', 'description of ISM absorption parameters'),
	(693, 'Atmosphere Composition', 'hydrogen', 'description of composition assumption'),
	(694, 'Magnetic field', 'non-magneticdsdsds', 'description of B-field assumptiondqsdsqdqsdsqd'),
	(695, 'Magnetic field', 'non-magnetic', 'description of B-field assumption');

-- Listage de la structure de table compare3. auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.auth_group : ~9 rows (environ)
INSERT INTO `auth_group` (`id`, `name`) VALUES
	(8, 'coldMSP'),
	(4, 'NS Mass'),
	(2, 'NS Spin'),
	(5, 'NS-NS_mergers'),
	(6, 'PPM'),
	(7, 'qLMXB'),
	(9, 'Thermal INSs'),
	(3, 'Transiently Accreting NS'),
	(10, 'Type-I X-ray bursts');

-- Listage de la structure de table compare3. auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.auth_group_permissions : ~0 rows (environ)

-- Listage de la structure de table compare3. auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.auth_permission : ~60 rows (environ)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add constrain ns', 7, 'add_constrainns'),
	(26, 'Can change constrain ns', 7, 'change_constrainns'),
	(27, 'Can delete constrain ns', 7, 'delete_constrainns'),
	(28, 'Can view constrain ns', 7, 'view_constrainns'),
	(29, 'Can add method ns', 8, 'add_methodns'),
	(30, 'Can change method ns', 8, 'change_methodns'),
	(31, 'Can delete method ns', 8, 'delete_methodns'),
	(32, 'Can view method ns', 8, 'view_methodns'),
	(33, 'Can add name ns', 9, 'add_namens'),
	(34, 'Can change name ns', 9, 'change_namens'),
	(35, 'Can delete name ns', 9, 'delete_namens'),
	(36, 'Can view name ns', 9, 'view_namens'),
	(37, 'Can add ns', 10, 'add_ns'),
	(38, 'Can change ns', 10, 'change_ns'),
	(39, 'Can delete ns', 10, 'delete_ns'),
	(40, 'Can view ns', 10, 'view_ns'),
	(41, 'Can add ref ns', 11, 'add_refns'),
	(42, 'Can change ref ns', 11, 'change_refns'),
	(43, 'Can delete ref ns', 11, 'delete_refns'),
	(44, 'Can view ref ns', 11, 'view_refns'),
	(45, 'Can add assumptions ns', 12, 'add_assumptionsns'),
	(46, 'Can change assumptions ns', 12, 'change_assumptionsns'),
	(47, 'Can delete assumptions ns', 12, 'delete_assumptionsns'),
	(48, 'Can view assumptions ns', 12, 'view_assumptionsns'),
	(49, 'Can add ns to assumptions', 13, 'add_nstoassumptions'),
	(50, 'Can change ns to assumptions', 13, 'change_nstoassumptions'),
	(51, 'Can delete ns to assumptions', 13, 'delete_nstoassumptions'),
	(52, 'Can view ns to assumptions', 13, 'view_nstoassumptions'),
	(53, 'Can add model ns', 14, 'add_modelns'),
	(54, 'Can change model ns', 14, 'change_modelns'),
	(55, 'Can delete model ns', 14, 'delete_modelns'),
	(56, 'Can view model ns', 14, 'view_modelns'),
	(57, 'Can add ns to model', 15, 'add_nstomodel'),
	(58, 'Can change ns to model', 15, 'change_nstomodel'),
	(59, 'Can delete ns to model', 15, 'delete_nstomodel'),
	(60, 'Can view ns to model', 15, 'view_nstomodel');

-- Listage de la structure de table compare3. auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
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

-- Listage des données de la table compare3.auth_user : ~6 rows (environ)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$600000$jIhPfL8hS5HpsIPk704mnS$0tHtY0TSJt3JQKMWYbyOYkitJhE/hTwJ3G88SWFmpkc=', '2023-06-19 12:53:53.522848', 1, 'root', '', '', '', 1, 1, '2023-04-24 14:57:09.161937'),
	(2, 'pbkdf2_sha256$600000$zrvy554j2FYIO1SwrxLuc1$oE09WJ9lIMo6S3LruGjkL3ydrCxM5Izgsu9bP/c9jGU=', '2023-04-26 08:35:18.741259', 0, 'vincent', '', '', '', 0, 1, '2023-04-26 07:31:16.000000'),
	(3, 'pbkdf2_sha256$600000$HKNXHsshde3Ww35HEqk3Lp$HQougSfuRKwN48usmwnlXXiaQgwWqSLmX7jEFQ425A4=', '2023-06-09 07:22:24.599195', 0, 'v', '', '', '', 0, 1, '2023-05-04 12:38:15.000000'),
	(4, 'pbkdf2_sha256$600000$moFzAIdW9KH0dviUIjl2xe$YOsyEAzDFkRUYHggv/lGuGBoNWJKoiH8JVV7iQkusdU=', '2023-05-15 07:28:08.805407', 0, 't', '', '', '', 0, 1, '2023-05-09 08:10:03.000000'),
	(5, 'pbkdf2_sha256$600000$Syr00a8j2MWUKwm9s0c4ty$u+9lkyZW5MLVVyREfZgyTmLqgbbxJ4YBZtbFQdy3GE4=', '2023-05-15 14:54:45.123993', 0, 'usertest', '', '', '', 0, 1, '2023-05-15 14:53:58.000000'),
	(6, 'pbkdf2_sha256$600000$trlTMsBRkLlVDYxoSzcao4$OwD5NSyA7Pu+mij4umFL+CtLvRXtW6QO1ELqiyT0++I=', '2023-06-13 09:49:09.996797', 0, 'sg', '', '', '', 0, 1, '2023-05-17 07:45:34.000000');

-- Listage de la structure de table compare3. auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.auth_user_groups : ~17 rows (environ)
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
	(3, 2, 3),
	(1, 2, 8),
	(2, 2, 9),
	(10, 3, 8),
	(13, 4, 7),
	(14, 4, 8),
	(16, 5, 7),
	(15, 5, 8),
	(17, 6, 2),
	(18, 6, 3),
	(19, 6, 4),
	(20, 6, 5),
	(21, 6, 6),
	(22, 6, 7),
	(23, 6, 8),
	(24, 6, 9),
	(25, 6, 10);

-- Listage de la structure de table compare3. auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.auth_user_user_permissions : ~0 rows (environ)

-- Listage de la structure de table compare3. constrain_ns
CREATE TABLE IF NOT EXISTS `constrain_ns` (
  `id_Constrain` int NOT NULL AUTO_INCREMENT,
  `ConstrainType` enum('Likelihood','MCMC samples','Confidence Interval','value+errors','R value+errors','M-R values+errors') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `constrainvariable` enum('R','M-R','R value+errors') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ConstrainVersion` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_Constrain`)
) ENGINE=InnoDB AUTO_INCREMENT=235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.constrain_ns : ~14 rows (environ)
INSERT INTO `constrain_ns` (`id_Constrain`, `ConstrainType`, `constrainvariable`, `ConstrainVersion`) VALUES
	(221, 'MCMC samples', 'M-R', 1),
	(222, 'value+errors', 'R', 123),
	(223, 'MCMC samples', 'R', 1),
	(224, 'Likelihood', 'R', 1),
	(225, 'value+errors', 'R', 1),
	(226, 'R value+errors', 'R', 1),
	(227, 'M-R values+errors', 'R', 1),
	(228, 'Confidence Interval', 'M-R', 2),
	(229, 'M-R values+errors', 'M-R', 56),
	(230, 'R value+errors', 'R value+errors', 786),
	(231, 'value+errors', 'R value+errors', 87),
	(232, 'Confidence Interval', 'R value+errors', 3),
	(233, 'value+errors', 'R value+errors', 3),
	(234, 'Likelihood', 'R', 876);

-- Listage de la structure de table compare3. django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
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

-- Listage des données de la table compare3.django_admin_log : ~25 rows (environ)
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2023-04-26 07:30:08.723043', '1', 'Add and View', 1, '[{"added": {}}]', 3, 1),
	(2, '2023-04-26 07:30:13.888209', '1', 'Add and View', 2, '[]', 3, 1),
	(3, '2023-04-26 07:31:16.937829', '2', 'vincent', 1, '[{"added": {}}]', 4, 1),
	(4, '2023-04-26 08:13:03.335594', '2', 'NS Spin', 1, '[{"added": {}}]', 3, 1),
	(5, '2023-04-26 08:13:15.540345', '1', 'Add and View', 3, '', 3, 1),
	(6, '2023-04-26 08:13:44.859017', '3', 'Transiently Accreting NS', 1, '[{"added": {}}]', 3, 1),
	(7, '2023-04-26 08:13:56.008137', '4', 'NS Mass', 1, '[{"added": {}}]', 3, 1),
	(8, '2023-04-26 08:14:03.301892', '5', 'NS-NS_mergers', 1, '[{"added": {}}]', 3, 1),
	(9, '2023-04-26 08:14:08.493832', '6', 'PPM', 1, '[{"added": {}}]', 3, 1),
	(10, '2023-04-26 08:14:12.988344', '7', 'qLMXB', 1, '[{"added": {}}]', 3, 1),
	(11, '2023-04-26 08:14:18.138490', '8', 'Cold MSPs', 1, '[{"added": {}}]', 3, 1),
	(12, '2023-04-26 08:14:25.185006', '9', 'Thermal INSs', 1, '[{"added": {}}]', 3, 1),
	(13, '2023-04-26 08:14:30.626567', '10', 'Type-I X-ray bursts', 1, '[{"added": {}}]', 3, 1),
	(14, '2023-04-26 08:14:51.232629', '2', 'vincent', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(15, '2023-05-04 12:38:15.910624', '3', 'v', 1, '[{"added": {}}]', 4, 1),
	(16, '2023-05-05 09:34:40.301397', '3', 'v', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(17, '2023-05-05 09:51:54.608576', '3', 'v', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(18, '2023-05-05 10:13:08.003241', '8', 'coldMSP', 2, '[{"changed": {"fields": ["Name"]}}]', 3, 1),
	(19, '2023-05-09 08:10:03.760294', '4', 't', 1, '[{"added": {}}]', 4, 1),
	(20, '2023-05-09 08:10:13.579728', '4', 't', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(21, '2023-05-10 09:17:43.340026', '4', 't', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(22, '2023-05-15 14:53:58.972537', '5', 'usertest', 1, '[{"added": {}}]', 4, 1),
	(23, '2023-05-15 14:54:22.019333', '5', 'usertest', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1),
	(24, '2023-05-17 07:45:35.478560', '6', 'sg', 1, '[{"added": {}}]', 4, 1),
	(25, '2023-05-17 07:45:45.398746', '6', 'sg', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);

-- Listage de la structure de table compare3. django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.django_content_type : ~15 rows (environ)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(12, 'compare', 'assumptionsns'),
	(7, 'compare', 'constrainns'),
	(8, 'compare', 'methodns'),
	(14, 'compare', 'modelns'),
	(9, 'compare', 'namens'),
	(10, 'compare', 'ns'),
	(13, 'compare', 'nstoassumptions'),
	(15, 'compare', 'nstomodel'),
	(11, 'compare', 'refns'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session');

-- Listage de la structure de table compare3. django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.django_migrations : ~23 rows (environ)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-04-12 07:27:46.250375'),
	(2, 'auth', '0001_initial', '2023-04-12 07:27:46.753844'),
	(3, 'admin', '0001_initial', '2023-04-12 07:27:46.946037'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-12 07:27:46.961657'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-12 07:27:46.978238'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-12 07:27:47.120014'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-12 07:27:47.191127'),
	(8, 'auth', '0003_alter_user_email_max_length', '2023-04-12 07:27:47.240594'),
	(9, 'auth', '0004_alter_user_username_opts', '2023-04-12 07:27:47.256464'),
	(10, 'auth', '0005_alter_user_last_login_null', '2023-04-12 07:27:47.328274'),
	(11, 'auth', '0006_require_contenttypes_0002', '2023-04-12 07:27:47.334324'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-12 07:27:47.352398'),
	(13, 'auth', '0008_alter_user_username_max_length', '2023-04-12 07:27:47.431628'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-12 07:27:47.507476'),
	(15, 'auth', '0010_alter_group_name_max_length', '2023-04-12 07:27:47.545013'),
	(16, 'auth', '0011_update_proxy_permissions', '2023-04-12 07:27:47.560473'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-12 07:27:47.632717'),
	(18, 'sessions', '0001_initial', '2023-04-12 07:27:47.671109'),
	(19, 'compare', '0001_initial', '2023-04-12 10:25:10.550121'),
	(20, 'compare', '0002_alter_assumptionsns_options_and_more', '2023-05-12 08:43:38.146061'),
	(21, 'compare', '0003_constrainns_constrainvariable_ns_id_constrain_and_more', '2023-05-24 08:30:36.247454'),
	(22, 'compare', '0004_alter_assumptionsns_assumptionsdescription_and_more', '2023-05-24 08:30:36.257978'),
	(23, 'compare', '0005_alter_constrainns_constrainvariable', '2023-05-24 08:32:03.354445');

-- Listage de la structure de table compare3. django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.django_session : ~1 rows (environ)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('y33pqcs67pamc8qjntp7z1v9avs4d503', '.eJxVjDsOwjAQBe_iGllr5M-Gkp4zWGvvggPIluKkirg7iZQC2jczb1WRlrnEpcsUR1YXZdTpd0uUX1J3wE-qj6Zzq_M0Jr0r-qBd3xrL-3q4fweFetlqQmGXPVIOAJ4pWXByRhqIMWVEIHvHAB5AQh7IihFjHaBDTpvi1ecL-NI4MQ:1qBEOH:2-d4IvR_kZj-RWp6NODkQlx9adY1s6ftBgeKjhieQ2g', '2023-07-03 12:53:53.536921');

-- Listage de la structure de table compare3. method_ns
CREATE TABLE IF NOT EXISTS `method_ns` (
  `id_Method` int NOT NULL AUTO_INCREMENT,
  `Method` enum('Pulsar timing','Thermal emission','Gravitational wave merger') NOT NULL,
  `Method_Specific` text NOT NULL,
  `ProcessinfInfo` text NOT NULL,
  `DataDate` varchar(70) NOT NULL,
  PRIMARY KEY (`id_Method`)
) ENGINE=InnoDB AUTO_INCREMENT=427 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.method_ns : ~15 rows (environ)
INSERT INTO `method_ns` (`id_Method`, `Method`, `Method_Specific`, `ProcessinfInfo`, `DataDate`) VALUES
	(412, 'Thermal emission', 'X-ray Spectral fitting', 'CIAO v4.10 and CALDB v.4.8.2', 'Multiple Chandra obs (2017 Sept)'),
	(413, 'Thermal emission', 'X-ray Spectral fitting', 'Find CIAO and CALDB versions used', 'Find chandra ObsID'),
	(414, 'Thermal emission', 'X-ray Spectral fitting', 'CIAO v4.9 & CALDB v4.7.3; SAS v15.0.0', 'Multiple XMM and Chandra obs'),
	(415, 'Gravitational wave merger', 'dd', 'CIAO v4.13 ', 'Multiple Chandra obs'),
	(416, 'Thermal emission', 'X-ray Spectral fitting', 'CIAO v4.5, SAS 13.0', 'Multiple Chandra and XMM-Newton obs'),
	(417, 'Thermal emission', 'X-ray Spectral fitting', 'CIAO v4.5, SAS 13.1', 'Multiple Chandra and XMM-Newton obs'),
	(418, 'Thermal emission', 'X-ray Spectral fitting', 'Find CIAO and CALDB versions used', 'Multiple Chandra obs'),
	(419, 'Thermal emission', 'X-ray Spectral fitting', 'CIAO v4.13 ', 'Multiple Chandra obs'),
	(420, 'Gravitational wave merger', 'dsqdsqds', 'dqsdqsd', 'dsqdsq'),
	(421, 'Thermal emission', 'gros test', 'gros test', 'gros test'),
	(422, 'Gravitational wave merger', 'boup', 'boup', 'boup'),
	(423, 'Gravitational wave merger', 'fdsfsd', 'dfdsfsd', 'fsdfsdf'),
	(424, 'Thermal emission', 'bon', 'bon', 'bon'),
	(425, 'Gravitational wave merger', 'fdsf', 'dsfds', 'fdsf'),
	(426, 'Pulsar timing', 'hfghgh', 'hgfhfghfghgfh', 'gfhfg');

-- Listage de la structure de table compare3. model_ns
CREATE TABLE IF NOT EXISTS `model_ns` (
  `id_Model` int NOT NULL AUTO_INCREMENT,
  `DependenciesPrimary` varchar(60) DEFAULT NULL,
  `DependenciesSecondary` varchar(60) DEFAULT NULL,
  `DependeciesDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `CaveatsReferences` text,
  PRIMARY KEY (`id_Model`)
) ENGINE=InnoDB AUTO_INCREMENT=352 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.model_ns : ~31 rows (environ)
INSERT INTO `model_ns` (`id_Model`, `DependenciesPrimary`, `DependenciesSecondary`, `DependeciesDescription`, `CaveatsReferences`) VALUES
	(321, 'atmosphere', 'nsx', 'description of atmosphere model', 'fsd'),
	(322, 'absorption', 'tbabs', 'description of absorption model', 'fdsfs'),
	(323, 'atmosphere', 'nsatmosdddddsdsqdqsdqs', 'description of atmosphere model', 'tttt'),
	(324, ' absorption', ' tbabs', 'description of absorption model', 'hhh'),
	(325, 'atmosphere', 'dsqdqsd', 'description of atmosphere model', 'gdf'),
	(326, 'atmosphere', 'nsatmos', 'description of atmosphere model', 'bf'),
	(327, 'test', 'test', 'test', NULL),
	(328, 'test2', 'test2', 'test2', NULL),
	(329, 'grostest', 'grostest', 'grostest', NULL),
	(330, 'grosteststs', 'grosteststs', 'grosteststs', NULL),
	(331, 'boup', 'boup', 'boup', NULL),
	(332, 'boup2', 'boup2', 'boup2', NULL),
	(333, 'boup3', 'boup3', '', NULL),
	(334, 'boup4', 'boup4', '', NULL),
	(335, 'boup5', 'boup5', '', NULL),
	(336, NULL, NULL, 'boup', NULL),
	(337, 'vincent', 'vincent', 'vincent', NULL),
	(338, 'vincent2', 'vincent2', 'vincent2', NULL),
	(339, 'vincent3', 'vincent3', '', NULL),
	(340, 'bon', 'bon', 'bon', NULL),
	(341, 'bon2', 'bon2', 'bon2', NULL),
	(342, 'bon3', 'bon3', 'bon3', NULL),
	(343, 'bon4', 'bon4', '', NULL),
	(344, 'fdsfsd', 'fdsfds', 'fdsfds', NULL),
	(345, 'fdsfsdfds', 'fdsfdsf', 'dsfsd', NULL),
	(346, 'fgdgfd', 'sze', 'rezrr', NULL),
	(347, 'jhgj', 'ghjkjhg', 'jhj', 'miam'),
	(348, 'jhgjh', 'jhj', 'j', 'jjhj'),
	(349, 'hfgg', 'hfghfg', NULL, 'jfjhf'),
	(350, 'jfgjgfjg', 'jgfjfgj', 'tjrjf', NULL),
	(351, 'jhgj', 'ghjkjhg', 'jhj', 'aaaaaaaaaaaabangbang');

-- Listage de la structure de table compare3. name_ns
CREATE TABLE IF NOT EXISTS `name_ns` (
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
) ENGINE=InnoDB AUTO_INCREMENT=408 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.name_ns : ~13 rows (environ)
INSERT INTO `name_ns` (`id_Name`, `NameDB`, `ClassDB`, `NameSimbad`, `ClassSimbad`, `RA`, `Declination`, `LocalisationFile`, `EventDate`) VALUES
	(395, 'M30_qlmxb', 'qLMXB', 'CXOGlb J214022.1-231045', 'LXB', 325.0923380000, -23.1794580000, NULL, NULL),
	(396, 'M3_CX2', 'qLMXB', '...', '...', 205.5625000000, 28.3781830000, NULL, NULL),
	(397, 'M13_qlmxb', 'qLMXB', '...', '...', 250.4323380000, 27.6160670000, NULL, NULL),
	(398, 'M28_qlmxbbbb', 'qLMXB', NULL, NULL, NULL, -24.8689610000, 'None', NULL),
	(399, 'omega_cen_qlmxb', 'qLMXB', '...', '...', 201.5823210000, -47.4861990000, NULL, NULL),
	(400, 'NGC_6397_qlmxbgfdxfghjk', 'qLMXB', NULL, NULL, NULL, 6.0041670000, 'None', NULL),
	(401, '47 Tuc_X5', 'qLMXB', 'CXOGlb J002400.9-720453 ', NULL, 6.0041670000, -72.0814440000, NULL, NULL),
	(402, '47 Tuc_X7', 'qLMXB', 'CXOGlb J002403.4-720451 ', NULL, 6.0166670000, -72.0810830000, NULL, NULL),
	(403, 'M28_qlmxbbbbfdqsd', 'qLMXB', NULL, NULL, NULL, -24.8689610000, 'None', NULL),
	(404, 'NGC$^poiu', 'qLMXB', NULL, NULL, NULL, 6.0041670000, 'None', NULL),
	(405, 'M28_qlmxb', 'qLMXB', 'CXOGlb J182432.8-245208', 'LXB', 276.1367540000, -24.8689610000, NULL, NULL),
	(406, 'M30_qlmxb', 'qLMXB', 'CXOGlb J214022.1-231045', 'LXB', 325.0923380000, 23.1794580000, NULL, NULL),
	(407, 'M30_qlmxb', 'NS Spin', 'CXOGlb J214022.1-231045	', 'LXB', 325.0923380000, 23.1794580000, NULL, NULL);

-- Listage de la structure de table compare3. ns
CREATE TABLE IF NOT EXISTS `ns` (
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

-- Listage des données de la table compare3.ns : ~19 rows (environ)
INSERT INTO `ns` (`FileName`, `FilePath`, `id_ref`, `id_Name`, `id_Method`, `id_Constrain`) VALUES
	('bon', 'bon', 334, 398, 424, 232),
	('boup', 'boup', 332, 405, 422, 230),
	('fds', 'fdsfds', 333, 398, 425, 233),
	('fdsfsdf', 'fsdf', 331, 396, 426, 234),
	('file1.txt', 'qdsdsqdsqdsq.txt', 332, 396, 413, 225),
	('file10.txt', 'qdsdsqdsqdsq.txt', 337, 402, 418, 226),
	('file2.txt', 'qdsdsqdsqdsq.txt', 333, 397, 414, 225),
	('file4.txt', 'qdsdsqdsqdsq.txt', 338, 405, 419, 226),
	('file5.txt', 'qdsdsqdsqdsq.txt', 338, 405, 419, 226),
	('file6.txt', 'qdsdsqdsqdsq.txt', 335, 399, 416, 227),
	('file7.txt', 'qdsdsqdsqdsq.txt', 336, 404, 417, 222),
	('file8.txt', 'qdsdsqdsqdsq.txt', 337, 401, 418, 223),
	('file9.txt', 'qdsdsqdsqdsq.txt', 337, 402, 418, 223),
	('fileNone.txt', 'qdsdsqdsqdsq.txt', 333, 397, 414, 222),
	('fsdf', 'dsfdsf', 332, 400, 423, 231),
	('gros test', 'gros test', 331, 397, 421, 229),
	('M30_nsatmos_MCMCsamples.txt', 'qdsdsqdsqdsq.txt', 331, 395, 412, 221),
	('M30_nsx_MCMCsamples.txt', 'qdsdsqdsqdsq.txt', 331, 395, 412, 221),
	('test', 'testststs', 334, 396, 420, 228);

-- Listage de la structure de table compare3. ns_to_assumptions
CREATE TABLE IF NOT EXISTS `ns_to_assumptions` (
  `id_ns_to_assumptions` int NOT NULL AUTO_INCREMENT,
  `id_Assumptions` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_assumptions`),
  UNIQUE KEY `Uni_cons` (`id_Assumptions`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_assumptions_ibfk_1` FOREIGN KEY (`id_Assumptions`) REFERENCES `assumptions_ns` (`id_Assumptions`),
  CONSTRAINT `ns_to_assumptions_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=2643 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.ns_to_assumptions : ~72 rows (environ)
INSERT INTO `ns_to_assumptions` (`id_ns_to_assumptions`, `id_Assumptions`, `FileName`) VALUES
	(2613, 687, 'file2.txt'),
	(2619, 687, 'file4.txt'),
	(2595, 687, 'file9.txt'),
	(2535, 687, 'M30_nsatmos_MCMCsamples.txt'),
	(2584, 688, 'file7.txt'),
	(2590, 688, 'file8.txt'),
	(2596, 688, 'file9.txt'),
	(2560, 688, 'fileNone.txt'),
	(2536, 688, 'M30_nsatmos_MCMCsamples.txt'),
	(2542, 688, 'M30_nsx_MCMCsamples.txt'),
	(2609, 689, 'file1.txt'),
	(2639, 689, 'file10.txt'),
	(2615, 689, 'file2.txt'),
	(2621, 689, 'file4.txt'),
	(2627, 689, 'file5.txt'),
	(2633, 689, 'file6.txt'),
	(2585, 689, 'file7.txt'),
	(2591, 689, 'file8.txt'),
	(2597, 689, 'file9.txt'),
	(2561, 689, 'fileNone.txt'),
	(2537, 689, 'M30_nsatmos_MCMCsamples.txt'),
	(2543, 689, 'M30_nsx_MCMCsamples.txt'),
	(2610, 690, 'file1.txt'),
	(2640, 690, 'file10.txt'),
	(2616, 690, 'file2.txt'),
	(2622, 690, 'file4.txt'),
	(2628, 690, 'file5.txt'),
	(2634, 690, 'file6.txt'),
	(2586, 690, 'file7.txt'),
	(2592, 690, 'file8.txt'),
	(2598, 690, 'file9.txt'),
	(2562, 690, 'fileNone.txt'),
	(2538, 690, 'M30_nsatmos_MCMCsamples.txt'),
	(2544, 690, 'M30_nsx_MCMCsamples.txt'),
	(2611, 691, 'file1.txt'),
	(2641, 691, 'file10.txt'),
	(2617, 691, 'file2.txt'),
	(2623, 691, 'file4.txt'),
	(2629, 691, 'file5.txt'),
	(2635, 691, 'file6.txt'),
	(2587, 691, 'file7.txt'),
	(2593, 691, 'file8.txt'),
	(2599, 691, 'file9.txt'),
	(2563, 691, 'fileNone.txt'),
	(2539, 691, 'M30_nsatmos_MCMCsamples.txt'),
	(2545, 691, 'M30_nsx_MCMCsamples.txt'),
	(2612, 692, 'file1.txt'),
	(2642, 692, 'file10.txt'),
	(2618, 692, 'file2.txt'),
	(2624, 692, 'file4.txt'),
	(2630, 692, 'file5.txt'),
	(2636, 692, 'file6.txt'),
	(2588, 692, 'file7.txt'),
	(2594, 692, 'file8.txt'),
	(2600, 692, 'file9.txt'),
	(2564, 692, 'fileNone.txt'),
	(2540, 692, 'M30_nsatmos_MCMCsamples.txt'),
	(2546, 692, 'M30_nsx_MCMCsamples.txt'),
	(2607, 693, 'file1.txt'),
	(2637, 693, 'file10.txt'),
	(2625, 693, 'file5.txt'),
	(2631, 693, 'file6.txt'),
	(2583, 693, 'file7.txt'),
	(2589, 693, 'file8.txt'),
	(2559, 693, 'fileNone.txt'),
	(2541, 693, 'M30_nsx_MCMCsamples.txt'),
	(2608, 695, 'file1.txt'),
	(2638, 695, 'file10.txt'),
	(2614, 695, 'file2.txt'),
	(2620, 695, 'file4.txt'),
	(2626, 695, 'file5.txt'),
	(2632, 695, 'file6.txt');

-- Listage de la structure de table compare3. ns_to_model
CREATE TABLE IF NOT EXISTS `ns_to_model` (
  `id_ns_to_model` int NOT NULL AUTO_INCREMENT,
  `id_Model` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_model`),
  UNIQUE KEY `Uni_con_mod` (`id_Model`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_model_ibfk_1` FOREIGN KEY (`id_Model`) REFERENCES `model_ns` (`id_Model`),
  CONSTRAINT `ns_to_model_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=1031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.ns_to_model : ~48 rows (environ)
INSERT INTO `ns_to_model` (`id_ns_to_model`, `id_Model`, `FileName`) VALUES
	(997, 321, 'file2.txt'),
	(999, 321, 'file4.txt'),
	(991, 321, 'file9.txt'),
	(971, 321, 'M30_nsatmos_MCMCsamples.txt'),
	(996, 322, 'file1.txt'),
	(998, 322, 'file2.txt'),
	(972, 322, 'M30_nsatmos_MCMCsamples.txt'),
	(974, 322, 'M30_nsx_MCMCsamples.txt'),
	(987, 323, 'file7.txt'),
	(989, 323, 'file8.txt'),
	(979, 323, 'fileNone.txt'),
	(973, 323, 'M30_nsx_MCMCsamples.txt'),
	(1006, 324, 'file10.txt'),
	(1000, 324, 'file4.txt'),
	(1002, 324, 'file5.txt'),
	(1004, 324, 'file6.txt'),
	(988, 324, 'file7.txt'),
	(990, 324, 'file8.txt'),
	(992, 324, 'file9.txt'),
	(980, 324, 'fileNone.txt'),
	(995, 326, 'file1.txt'),
	(1005, 326, 'file10.txt'),
	(1001, 326, 'file5.txt'),
	(1003, 326, 'file6.txt'),
	(1007, 327, 'test'),
	(1008, 328, 'test'),
	(1009, 329, 'gros test'),
	(1010, 330, 'gros test'),
	(1011, 331, 'boup'),
	(1012, 332, 'boup'),
	(1013, 333, 'boup'),
	(1014, 334, 'boup'),
	(1015, 335, 'boup'),
	(1016, 336, 'boup'),
	(1017, 337, 'fsdf'),
	(1018, 338, 'fsdf'),
	(1019, 339, 'fsdf'),
	(1020, 340, 'bon'),
	(1021, 341, 'bon'),
	(1022, 342, 'bon'),
	(1023, 343, 'bon'),
	(1024, 344, 'fds'),
	(1025, 345, 'fds'),
	(1026, 346, 'fds'),
	(1027, 347, 'fdsfsdf'),
	(1028, 348, 'fdsfsdf'),
	(1029, 349, 'fdsfsdf'),
	(1030, 350, 'fdsfsdf');

-- Listage de la structure de table compare3. ref_ns
CREATE TABLE IF NOT EXISTS `ref_ns` (
  `id_Ref` int NOT NULL AUTO_INCREMENT,
  `Author` varchar(30) NOT NULL,
  `RefYear` int NOT NULL,
  `Short` varchar(50) NOT NULL,
  `Bibtex` text NOT NULL,
  `DOI` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `RepositoryDOI` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DataLink` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_Ref`)
) ENGINE=InnoDB AUTO_INCREMENT=339 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table compare3.ref_ns : ~8 rows (environ)
INSERT INTO `ref_ns` (`id_Ref`, `Author`, `RefYear`, `Short`, `Bibtex`, `DOI`, `RepositoryDOI`, `DataLink`) VALUES
	(331, 'Echiburu', 2020, '2020MNRAS.495.4508E', '@ARTICLE{2020MNRAS.495.4508E,       author = {{Echibur{\\\'u}}, C.~S. and {Guillot}, S. and {Zhao}, Y. and {Heinke}, C.~O. and {{\\"O}zel}, F. and {Webb}, N.~A.},        title = "{Spectral analysis of the quiescent low-mass X-ray binary in the globular cluster M30}",      journal = {\\mnras},     keywords = {stars: neutron, globular clusters: individual: M30, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},         year = 2020,        month = jul,       volume = {495},       number = {4},        pages = {4508-4517},          doi = {10.1093/mnras/staa1456},archivePrefix = {arXiv},       eprint = {2005.11345}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2020MNRAS.495.4508E},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.1093/mnras/staa1456', NULL, NULL),
	(332, 'Zhao', 2019, '2019MNRAS.483.4560Z', '@ARTICLE{2019MNRAS.483.4560Z,       author = {{Zhao}, Yue and {Heinke}, Craig O. and {Cohn}, Haldan N. and {Lugger}, Phyillis M. and {Cool}, Adrienne M.},        title = "{Identifications of faint Chandra sources in the globular cluster M3}",      journal = {\\mnras},     keywords = {stars: neutron, novae, cataclysmic variables, globular clusters: individual (M3), X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},         year = 2019,        month = mar,       volume = {483},       number = {4},        pages = {4560-4577},          doi = {10.1093/mnras/sty3384},archivePrefix = {arXiv},       eprint = {1812.05130}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.4560Z},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}       author = {{Zhao}, Yue and {Heinke}, Craig O. and {Cohn}, Haldan N. and {Lugger}, Phyillis M. and {Cool}, Adrienne M.},        title = "{Identifications of faint Chandra sources in the globular cluster M3}",      journal = {\\mnras},     keywords = {stars: neutron, novae, cataclysmic variables, globular clusters: individual (M3), X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},         year = 2019,        month = mar,       volume = {483},       number = {4},        pages = {4560-4577},          doi = {10.1093/mnras/sty3384},archivePrefix = {arXiv},       eprint = {1812.05130}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.4560Z},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.1093/mnras/sty3384', NULL, NULL),
	(333, 'Shaw', 2018, '2018MNRAS.476.4713S', '@ARTICLE{2018MNRAS.476.4713S,       author = {{Shaw}, A.~W. and {Heinke}, C.~O. and {Steiner}, A.~W. and {Campana}, S. and {Cohn}, H.~N. and {Ho}, W.~C.~G. and {Lugger}, P.~M. and {Servillat}, M.},        title = "{The radius of the quiescent neutron star in the globular cluster M13}",      journal = {\\mnras},     keywords = {stars: neutron, globular clusters: general, globular clusters: individual: M13, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},         year = 2018,        month = jun,       volume = {476},       number = {4},        pages = {4713-4718},          doi = {10.1093/mnras/sty582},archivePrefix = {arXiv},       eprint = {1803.00029}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2018MNRAS.476.4713S},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}       author = {{Servillat}, M. and {Webb}, N.~A. and {Lewis}, F. and {Knigge}, C. and {van den Berg}, M. and {Dieball}, A. and {Grindlay}, J.},        title = "{A Dwarf Nova in the Globular Cluster M13}",      journal = {\\apj},     keywords = {globular clusters: individual: M13 NGC 6205, novae, cataclysmic variables, stars: dwarf novae, X-rays: general, Astrophysics - Solar and Stellar Astrophysics, Astrophysics - Astrophysics of Galaxies, Astrophysics - High Energy Astrophysical Phenomena},         year = 2011,        month = jun,       volume = {733},       number = {2},          eid = {106},        pages = {106},          doi = {10.1088/0004-637X/733/2/106},archivePrefix = {arXiv},       eprint = {1103.4638}, primaryClass = {astro-ph.SR},       adsurl = {https://ui.adsabs.harvard.edu/abs/2011ApJ...733..106S},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.1093/mnras/sty582', NULL, NULL),
	(334, 'Vurgundddd', 2022, '2022ApJ...941...76V', '@ARTICLE{2022ApJ...941...76V,       author = {{Vurgun}, Eda and {Linares}, Manuel and {Ransom}, Scott and {Papitto}, Alessandro and {Bogdanov}, Slavko and {Bozzo}, Enrico and {Rea}, Nanda and {Garc{\\\'\\i}a-Senz}, Domingo and {Freire}, Paulo and {Stairs}, Ingrid},        title = "{The Neutron Star Population in M28: A Joint Chandra/GBT Look at Pulsar Paradise}",      journal = {\\apj},     keywords = {Neutron stars, Millisecond pulsars, Low-mass x-ray binary stars, 1108, 1062, 939, Astrophysics - High Energy Astrophysical Phenomena},         year = 2022,        month = dec,       volume = {941},       number = {1},          eid = {76},        pages = {76},          doi = {10.3847/1538-4357/ac9ea0},archivePrefix = {arXiv},       eprint = {2211.01067}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2022ApJ...941...76V},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.3847/1538-4357/ac9ea0', 'None', NULL),
	(335, 'Heinke', 2014, '2014MNRAS.444..443H', '@ARTICLE{2014MNRAS.444..443H,       author = {{Heinke}, C.~O. and {Cohn}, H.~N. and {Lugger}, P.~M. and {Webb}, N.~A. and {Ho}, W.~C.~G. and {Anderson}, J. and {Campana}, S. and {Bogdanov}, S. and {Haggard}, D. and {Cool}, A.~M. and {Grindlay}, J.~E.},        title = "{Improved mass and radius constraints for quiescent neutron stars in {\\ensuremath{\\omega}} Cen and NGC 6397}",      journal = {\\mnras},     keywords = {dense matter, stars: neutron, globular clusters: individual: NGC 6397, globular clusters: individual: NGC 5139, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},         year = 2014,        month = oct,       volume = {444},       number = {1},        pages = {443-456},          doi = {10.1093/mnras/stu1449},archivePrefix = {arXiv},       eprint = {1406.1497}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..443H},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.1093/mnras/stu1449', NULL, NULL),
	(336, 'Heinke', 2014, '2014MNRAS.444..443H', '@ARTICLE{2014MNRAS.444..443H,       author = {{Heinke}, C.~O. and {Cohn}, H.~N. and {Lugger}, P.~M. and {Webb}, N.~A. and {Ho}, W.~C.~G. and {Anderson}, J. and {Campana}, S. and {Bogdanov}, S. and {Haggard}, D. and {Cool}, A.~M. and {Grindlay}, J.~E.},        title = "{Improved mass and radius constraints for quiescent neutron stars in {\\ensuremath{\\omega}} Cen and NGC 6397}",      journal = {\\mnras},     keywords = {dense matter, stars: neutron, globular clusters: individual: NGC 6397, globular clusters: individual: NGC 5139, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},         year = 2014,        month = oct,       volume = {444},       number = {1},        pages = {443-456},          doi = {10.1093/mnras/stu1449},archivePrefix = {arXiv},       eprint = {1406.1497}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..443H},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.1093/mnras/stu1450', NULL, NULL),
	(337, 'Bogdanov', 2016, '2016ApJ...831..184B', '@ARTICLE{2016ApJ...831..184B,       author = {{Bogdanov}, Slavko and {Heinke}, Craig O. and {{\\"O}zel}, Feryal and {G{\\"u}ver}, Tolga},        title = "{Neutron Star Mass-Radius Constraints of the Quiescent Low-mass X-Ray Binaries X7 and X5 in the Globular Cluster 47 Tuc}",      journal = {\\apj},     keywords = {dense matter, equation of state, globular clusters: individual: 47 Tucanae, stars: neutron, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},         year = 2016,        month = nov,       volume = {831},       number = {2},          eid = {184},        pages = {184},          doi = {10.3847/0004-637X/831/2/184},archivePrefix = {arXiv},       eprint = {1603.01630}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2016ApJ...831..184B},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', ' 10.3847/0004-637X/831/2/184', NULL, NULL),
	(338, 'Vurgun', 2022, '2022ApJ...941...76V', '@ARTICLE{2022ApJ...941...76V,       author = {{Vurgun}, Eda and {Linares}, Manuel and {Ransom}, Scott and {Papitto}, Alessandro and {Bogdanov}, Slavko and {Bozzo}, Enrico and {Rea}, Nanda and {Garc{\\\'\\i}a-Senz}, Domingo and {Freire}, Paulo and {Stairs}, Ingrid},        title = "{The Neutron Star Population in M28: A Joint Chandra/GBT Look at Pulsar Paradise}",      journal = {\\apj},     keywords = {Neutron stars, Millisecond pulsars, Low-mass x-ray binary stars, 1108, 1062, 939, Astrophysics - High Energy Astrophysical Phenomena},         year = 2022,        month = dec,       volume = {941},       number = {1},          eid = {76},        pages = {76},          doi = {10.3847/1538-4357/ac9ea0},archivePrefix = {arXiv},       eprint = {2211.01067}, primaryClass = {astro-ph.HE},       adsurl = {https://ui.adsabs.harvard.edu/abs/2022ApJ...941...76V},      adsnote = {Provided by the SAO/NASA Astrophysics Data System}}', '10.3847/1538-4357/ac9ea0', NULL, NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
