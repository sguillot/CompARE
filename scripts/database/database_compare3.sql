-- MySQL dump 10.13  Distrib 8.0.33, for macos12.6 (x86_64)
--
-- Host: localhost    Database: compare3
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `assumptions_ns`
--

DROP TABLE IF EXISTS `assumptions_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assumptions_ns` (
  `id_Assumptions` int NOT NULL AUTO_INCREMENT,
  `AssumptionsPrimary` varchar(60) DEFAULT NULL,
  `AssumptionsSecondary` varchar(60) DEFAULT NULL,
  `AssumptionsDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `AssumptionsReferences` text,
  PRIMARY KEY (`id_Assumptions`)
) ENGINE=InnoDB AUTO_INCREMENT=989 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assumptions_ns`
--

LOCK TABLES `assumptions_ns` WRITE;
/*!40000 ALTER TABLE `assumptions_ns` DISABLE KEYS */;
INSERT INTO `assumptions_ns` VALUES (929,'Atmosphere Composition','hydrogen','At the surface of a neutron star, elements stratify on time scales of minutes/hours leaving the lightest on top (Romani 1987). Also, the thickness of the last scattering layer of a NS is on the order of a few cm. Therefore, it is common to assume a single composition, being that of the lightest element. Hydrogen is therefore a reasonable assumption for the composition, especially for a NS that has accreted matter from a companion star. Other effects are in competition and may put some uncertainties on the surface composition, namely, accretion from the interstellar medium, diffuse nuclear burning of light of H into He (Chang & Bildsten 2003, 2004), and spallation of heavier elements into lighter ones (Bildsten et al. 1992).','1987ApJ...313..718R, 1992ApJ...384..143B, 2003ApJ...585..464C, 2004ApJ...616L.147C'),(930,'\nMagnetic field','\nnon-magnetic','This analyses also assume emission from a low-magnetic field neutron stars (as typically measured for MSPs, specifically B_dip ~ 2.8e8 G for PSR J0437-4715). The atmosphere model is that of a non-magnetised atmosphere, which is a good approximation as B-field effect (modified opacities) become important above 1e10 G (Kaminker et al., 1983; Zavlin et al., 1996). However, this neglects potential high-magnetic loop near the NS surface.','1983Ap&SS..91..167K, 1996A&A...315..141Z, 2019MNRAS.490.5848G '),(931,'\nRotation','\nnon-rotating','The relativistic effects of rotation on the emergent spectrum are neglected in this analysis. However, the effects on the radius are < 1 km at the rotational frequency of PSR J0437-4715 (173.6 Hz), see Baubock et al. 2015). ','2015ApJ...799...22B'),(932,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature (modulo the contribution of the hot spots).','2019MNRAS.490.5848G '),(933,'\nInterstellar medium','\nsolar abundances','The modelling of the x-ray absorption (with the tbabs model) assumes solar abundances for the interstellar medium, a reasonable assumption for a pulsar located at 156 pc.','2000ApJ...542..914W'),(934,'\nPrior','\ndistance prior','The radio timing of the pulsar provided priors on the pulsar mass (1.44Msun), see Reardon et al. 2016. No uncertainties on this measurement was included in the analysis. ','2016MNRAS.455.1751R'),(935,' Prior',' mass prior','The radio timing of the pulsar provided priors on the pulsar distance (156.79 pc), see Reardon et al. 2016. No uncertainties on this measurement was included in the analysis.','2016MNRAS.455.1751R'),(936,' Prior',' reddening prior','The reddening was also provided as a prior, using estimation for Galactic dust maps: E(B-V) = 0.002+/-0.014 (Lallement et al. 2018).','2018A&A...616A.132L'),(937,'Atmosphere Composition','helium','At the surface of a neutron star, elements stratify on time scales of minutes/hours leaving the lightest on top (Romani 1987). Also, the thickness of the last scattering layer of a NS is on the order of a few cm. Therefore, it is common to assume a single composition, being that of the lightest element. If no Hydrogen is present in the system, the next expected element is Helium, which is a possibility if the NS has accreted only Helium from a companion star. Other effects are in competition and may put some uncertainties on the surface composition, namely, accretion from the interstellar medium, diffuse nuclear burning of light of H into He (Chang & Bildsten 2003, 2004), and spallation of heavier elements into lighter ones (Bildsten et al. 1992).','1987ApJ...313..718R, 1992ApJ...384..143B, 2003ApJ...585..464C, 2004ApJ...616L.147C'),(938,'\nRotation','\nnon-rotating','The relativistic effects of rotation on the emergent spectrum are neglected in this analysis. However, the effects on the radius are < 1 % at the rotational frequency of PSR J0437-4715 (173.6 Hz), see Baubock et al. 2015. ','2015ApJ...799...22B'),(939,'Gravitation theory','General relativity','The estimation of the post-Keplerian parameters and Shapiro delay were done assuming general relativity as the theory of gravitation.','Agazie et al. 2023, 2023ApJL..951...L9'),(940,'Gravitation theory','General relativity','The estimation of the post-Keplerian parameters and Shapiro delay were done assuming general relativity as the theory of gravitation.','Arzoumanian et al. 2018, 2018ApJS..235...37A'),(941,'Gravitation theory','General relativity','The estimation of the post-Keplerian parameters and Shapiro delay were done assuming general relativity as the theory of gravitation.','Fonseca et al. 2021, 2021ApJ...915L..12F'),(942,'Gravitation theory','General relativity','The ray-tracing model of this analysis (described in Bogdanov et al. 2019, Paper II) assumes general relativity as the theory of gravitation.','2019ApJ...887L..26B'),(943,'\nAtmosphere composition',' \nhydrogen','At the surface of a neutron star, elements stratify on time scales of minutes/hours leaving the lightest on top (Romani 1987). Also, the thickness of the last scattering layer of a NS is on the order of a few cm. Therefore, it is common to assume a single composition, being that of the lightest element. Hydrogen is therefore a reasonable assumption for the composition, especially for a NS that has accreted matter from a companion star, as is the case for a millisecond pulsar. Other effects are in competition and may put some uncertainties on the surface composition, namely, accretion from the interstellar medium, diffuse nuclear burning of light of H into He (Chang & Bildsten 2003, 2004), and spallation of heavier elements into lighter ones (Bildsten et al. 1992).','1987ApJ...313..718R, 1992ApJ...384..143B, 2003ApJ...585..464C, 2004ApJ...616L.147C'),(944,'\nIonization degree',' \nfully ionized','The radiative transfer calculations of the atmosphere model were performed assuming full ionisation of the material (i.e., using opacity tables of fully ionised elements).  At the temperatures of the hot spots of millisecond pulsars (0.5-2 x 10^6 K), the neutral fraction may be negligible. See discussion in Bogdanov et al. 2019, Paper II) ','2019ApJ...887L..26B'),(945,'\nMagnetic field',' \nnon-magnetic','This analyses assumed emission from a low-magnetic field neutron stars as measured  for the dipolar fields of millisecond pulsars (Manchester et al. 2005). The atmosphere model is that of a non-magnetised atmosphere, which is a good approximation as B-field effect (modified opacities) become important above 1e10 G (Kaminker et al., 1983; Zavlin et al., 1996). However, this neglects potential high-magnetic loop near the NS surface.','2005AJ....129.1993M, 1983Ap&SS..91..167K, 1996A&A...315..141Z'),(946,'\nInsterstellar medium',' \nsolar abundances','The modelling of the x-ray absorption (with the tbabs model) assumes solar abundances for the interstellar medium.','2000ApJ...542..914W'),(947,'\nSpot pattern',' \nST-PDT','The assumed spot geometrical pattern of this analysis was ST-PDT: Single-temperature + Protruding Single-Temperature, i.e., a circular spot (ST) with a crescent-shape spot (PST, i.e., with the \'inner\' temperature consistent with zero); See Riley et al. 2019 for a description of the geometrical spot patterns.  Note that simpler spot patterns (e.g., two circular spots) were not statistically preferred (Riley et al. 2019).','2019ApJ...887L..21R'),(948,'\nNon-thermal emission',' \nignored','This analysis ignored the possible presence of non-thermal emission from the millisecond pulsar. However, in the energy range used for the analysis (0.25-3.0 keV), non-thermal emission is unlikely to have a significant contribution (see for e.g., Guillot et al. 2016). Moreover, no such thermal emission has been detected in the X-ray spectrum of this pulsar (Bogdanov et al. 2008)','2016MNRAS.463.2612G, 2008ApJ...689..407B'),(949,'\nPrior','\ndistance prior','The radio timing of the pulsar provided a prior on the pulsar distance (325 +/- 9 pc), see Arzoumanian et al 2018.','2018ApJS..235...37A'),(950,'\nPrior','\nabsorption prior','A prior on the interstellar absorption was used in this analysis, with a neutron hydrogen column density Nh in the range 0 to 5x10^20 cm^-2, i.e, a flat prior (Riley et al. 2019).','2019ApJ...887L..21R'),(951,'\nSpot pattern',' \ntwo oval spots','The assumed spot geometrical pattern of this analysis was that of two oval spots (allowed to overlap partially or fully), see Miller et al. 2019.','2019ApJ...887L..24M'),(952,'\nPrior','\nabsorption prior','A prior on the interstellar absorption was used in this analysis, with a neutron hydrogen column density Nh in the range 0 to 2.5x10^20 cm^-2, i.e, a flat prior (Miller et al. 2019).','2019ApJ...887L..24M'),(953,'\nSpot pattern',' \nSTU','The assumed spot geometrical pattern of this analysis was STU: Single-temperature unshared, i.e., two circular spots (not overlapping); See Riley et al. 2019 ans Riley et al. 2021 for a description of the geometrical spot patterns.','2019ApJ...887L..21R, 2021ApJ...918L..27R'),(954,'\nNon-thermal emission',' \nignored','This analysis ignored the possible presence of non-thermal emission from the millisecond pulsar. However, in the energy range used for the analysis (0.25-1.5 keV), non-thermal emission is unlikely to have a significant contribution (see for e.g., Guillot et al. 2016). Moreover, no such thermal emission has been detected in the X-ray spectrum of this pulsar (Bogdanov et al. 2008)','2016MNRAS.463.2612G, 2008ApJ...689..407B'),(955,'\nPrior','\ndistance prior','The radio timing of the pulsar provided a prior on the pulsar distance (see Fonseca et al. 2021). Specifically a Skewed-Normal distribution was used with parameters: skewnorm.pdf(D, 1.7, loc = 1.002, scale = 0.227). See Riley et al. 2021.','2021ApJ...915L..12F, 2021ApJ...918L..27R'),(956,'\nPrior','\nabsorption prior','A prior on the interstellar absorption was used in this analysis, with a neutron hydrogen column density Nh in the range 0 to 10x10^20 cm^-2, i.e, a flat prior (see discussion in Riley et al. 2021).','2021ApJ...918L..27R'),(957,'\nPrior','\nmass prior','A prior on the pulsar mass resulted from the pulsar timing measurements of the Shapiro delay.  The mass of 2.08+/-0.04 Msun was used as a prior in this analysis. More specifically, a joint prior distribution with the inclination i was used (see Table 1 in Riley et al. 2021) since the mass and cos(i) are correlated in the analyses of Fonseca et al. 2021.','2021ApJ...915L..12F, 2021ApJ...918L..27R'),(958,'\nPrior','\ninclination prior','A prior on the pulsar\'s inclination i with respect to Earth was used in this analysis.  More specifically, a joint prior distribution with the mass was used (see Table 1 in Riley et al. 2021) since the mass and cos(i) are correlated in the analyses of Fonseca et al. 2021.','2021ApJ...915L..12F, 2021ApJ...918L..27R'),(959,'\nSpot pattern',' \ntwo circular spots','The assumed spot geometrical pattern of this analysis was that of two circular spots (not allowed to overlap), see Miller et al. 2021.','2021ApJ...918L..28M'),(960,'\nPrior','\ndistance prior','The radio timing of the pulsar provided a prior on the pulsar distance (see Fonseca et al. 2021). Specifically an asymmetric normal distribution was used (See Table 1 and Section 3.3 in Miller et al. 2021).','2021ApJ...915L..12F, 2021ApJ...918L..28M'),(961,'\nPrior','\nabsorption prior','A prior on the interstellar absorption was used in this analysis, with a neutron hydrogen column density Nh in the range 0 to 10x10^20 cm^-2, i.e, a flat prior (see discussion in Miller et al. 2021).','2021ApJ...918L..28M'),(962,'\nPrior','\nmass prior','A prior on the pulsar mass resulted from the pulsar timing measurements of the Shapiro delay.  The mass of 2.08+/-0.07 Msun was used as a prior in this analysis (Fonseca et al. 2021, Miller et al. 2021).','2021ApJ...915L..12F, 2021ApJ...918L..28M'),(963,'\nPrior','\ninclination prior','A prior on the pulsar\'s inclination i with respect to Earth was used in this analysis. A flat prior with boundaries 82.5 degrees and 92.8 degrees was used (see Table 1 in Miller et al. 2021). See also Fonseca et al. 2021.','2021ApJ...915L..12F, 2021ApJ...918L..28M'),(964,'\nMagnetic field','\nnon-magnetic','This analyses also assume emission from a low-magnetic field neutron stars as expected for low-mass X-ray binaries (Di Salvo & Burderi 2003), however not measured for quiescent low-mass X-ray binaries in globular clusters. The atmosphere model is that of a non-magnetised atmosphere, which is a good approximation as B-field effect (modified opacities) become important above 1e10 G (Kaminker et al., 1983; Zavlin et al., 1996).','2003A&A...397..723D, 1983Ap&SS..91..167K, 1996A&A...315..141Z'),(965,'\nRotation','\nnon-rotating','The relativistic effects of rotation on the emergent spectrum are neglected in this analysis. However, in the absence of detected pulsations, the rotation frequency for this neutron star is unknown, and the the effects of rotation on the radius may reach a few percent, see Baubock et al. 2015. ','2015ApJ...799...22B'),(966,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2018MNRAS.476.4713S, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(967,'\nInterstellar medium','\nsolar abundances','The modelling of the x-ray absorption (with the tbabs model) assumes solar abundances for the interstellar medium.','2000ApJ...542..914W'),(968,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster M13 (d = 7.7 kpc) used in this analysis was obtained from a systematic study of Galactic globular cluster (population synthesis and dynamical studies, McLaughlin & van der Marel 2005).','2005ApJS..161..304M'),(969,'\nCalibration uncertainties','\nCross-calibration factors','To account for the uncertainties in the calibration between detectors, the authors employed cross-calibration multiplicative factors (often used in joined X-ray spectral analyses between data from multiple detectors/telescopes).','2018MNRAS.476.4713S'),(970,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2022ApJ...941...76V, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(971,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster M28 (d = 5.5 kpc) used in this analysis was obtained from the catalog of Galactic globular clusters  of Harris 1996 (updated in 2010).','1996AJ....112.1487H, 2010arXiv1012.3224H'),(972,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster M28 (d = 5.5 kpc) used in this analysis was obtained from the catalog of Galactic globular clusters  of Harris 1996 (updated in 2010).','1996AJ....112.1487H, 2010arXiv1012'),(973,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2016ApJ...826..162E, 2020MNRAS.495.4508E'),(974,'\nPrior','\ndistance prior','The distance to the globular cluster M30 (d = 8.2 +/- 0.62 kpc, O\'Malley et al 2017) used in this analysis was obtained from the main sequence fitting method, and the uncertainties include all sources of uncertainties (theoretical, photometric, metallicity and reddening estimates, O\'Malley et al 2017).','2017ApJ...838..162O'),(975,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2007ApJ...671..727W, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(976,'\nInterstellar medium','\nsolar abundances','The modelling of the x-ray absorption (with the phabs model) assumes photoelectric absorption cross-sections of Verner et al. 1996, and the solar abundances of Anders & Grevesse 1989.','1996ApJ...465..487V, 1989GeCoA..53..197A'),(977,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster NGC2808 (d = 9.6 kpc) used in this analysis was obtained from the catalog of Galactic globular clusters  of Harris 1996 (updated in 2010).','1996AJ....112.1487H, 2010arXiv1012.3224H'),(978,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2014MNRAS.444..443H, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(979,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster NGC 5139 (Omega Centauri, d = 5.3 kpc) used in this analysis was obtained after from a literature review of distance measurements to this cluster (see Section 1.3 of Heinke et al. 2014).','2014MNRAS.444..443H'),(980,'\nCalibration uncertainties','\nCross-calibration factors','To account for the uncertainties in the calibration between detectors, the authors employed cross-calibration multiplicative factors (often used in joined X-ray spectral analyses between data from multiple detectors/telescopes).','2014MNRAS.444..443H'),(981,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2013ApJ...772....7G, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(982,'\nPrior','\ndistance prior','The distance to the globular cluster NGC6304, d = 6.22+/-0.26 kpc (Recio-Blanco et al. 2005), used in this analysis was obtained from the horizontal branch fitting method.','2005A&A...432..851R'),(983,'\nCalibration uncertainties','\nadded systematics','To account for the instrument response uncertainties, 3% systematic uncertainties were added to each spectral bin, following Guillot et al. 2013.','2013ApJ...772....7G'),(984,'\nPrior','\ndistance prior without uncertainties','The distance to the globular cluster NGC 6397 (d = 2.51 kpc) used in this analysis was obtained after from a literature review of distance measurements to this cluster (see Section 1.3 of Heinke et al. 2014).','2014MNRAS.444..443H'),(985,'\nEmitting fraction','\nuniform full surface','The analysis assumes that the full surface is emitting uniformly at the same temperature. However, if the presence of hot regions are neglected, this can bias the measurement of the size of the emitting area (Elshamouty et al. 2016), see discussion in Echiburú et al. 2020.','2016ApJ...831..184B, 2016ApJ...826..162E, 2020MNRAS.495.4508E'),(986,'\nPrior','\ndistance prior','The distance to the globular cluster 47 Tuc, d = 4.53(+0.08)(-0.04) kpc, used in this analysis was obtained after from a literature review of distance measurements to this cluster (see Section 3.5 of Bogdanov et al. 2016).  The uncertainties were accounted for using a top-hat prior with the 1-sigma uncertainties.','2016ApJ...831..184B'),(987,'\nCalibration uncertainties','\nadded systematics','To account for the instrument response uncertainties, 3% systematic uncertainties were added to each spectral bin, following Guillot et al. 2013.','2013ApJ...772....7G, 2016ApJ...831..184B'),(988,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `assumptions_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `auth_group` VALUES (8,'Cold MSP'),(4,'NS Mass'),(2,'NS Spin'),(5,'NS-NS_mergers'),(6,'PPM'),(7,'qLMXB'),(9,'Thermal INSs'),(3,'Transiently Accreting NS'),(10,'Type-I X-ray bursts');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$jIhPfL8hS5HpsIPk704mnS$0tHtY0TSJt3JQKMWYbyOYkitJhE/hTwJ3G88SWFmpkc=','2023-06-21 09:20:59.807159',1,'root','','','',1,1,'2023-04-24 14:57:09.161937'),(2,'pbkdf2_sha256$600000$zrvy554j2FYIO1SwrxLuc1$oE09WJ9lIMo6S3LruGjkL3ydrCxM5Izgsu9bP/c9jGU=','2023-04-26 08:35:18.741259',0,'vincent','','','',0,1,'2023-04-26 07:31:16.000000'),(3,'pbkdf2_sha256$600000$HKNXHsshde3Ww35HEqk3Lp$HQougSfuRKwN48usmwnlXXiaQgwWqSLmX7jEFQ425A4=','2023-06-09 07:22:24.599195',0,'v','','','',0,1,'2023-05-04 12:38:15.000000'),(4,'pbkdf2_sha256$600000$moFzAIdW9KH0dviUIjl2xe$YOsyEAzDFkRUYHggv/lGuGBoNWJKoiH8JVV7iQkusdU=','2023-05-15 07:28:08.805407',0,'t','','','',0,1,'2023-05-09 08:10:03.000000'),(5,'pbkdf2_sha256$600000$Syr00a8j2MWUKwm9s0c4ty$u+9lkyZW5MLVVyREfZgyTmLqgbbxJ4YBZtbFQdy3GE4=','2023-05-15 14:54:45.123993',0,'usertest','','','',0,1,'2023-05-15 14:53:58.000000'),(6,'pbkdf2_sha256$600000$trlTMsBRkLlVDYxoSzcao4$OwD5NSyA7Pu+mij4umFL+CtLvRXtW6QO1ELqiyT0++I=','2023-08-03 13:07:27.829828',0,'sg','','','',0,1,'2023-05-17 07:45:34.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constrain_ns` (
  `id_Constrain` int NOT NULL AUTO_INCREMENT,
  `ConstrainType` enum('MCMC samples','Posterior samples','Quantiles','mean +/- 1 sigma','Probability distribution','Chi2 contours') NOT NULL,
  `constrainvariable` enum('M','R','M-R','F','L','M-L') NOT NULL,
  `ConstrainVersion` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_Constrain`)
) ENGINE=InnoDB AUTO_INCREMENT=307 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constrain_ns`
--

LOCK TABLES `constrain_ns` WRITE;
/*!40000 ALTER TABLE `constrain_ns` DISABLE KEYS */;
INSERT INTO `constrain_ns` VALUES (300,'MCMC samples','M-R',1),(301,'mean +/- 1 sigma','M',1),(302,'mean +/- 1 sigma','M',2),(303,'Posterior samples','M-R',1),(304,'Probability distribution','M-R',1),(305,'Chi2 contours','M-R',1),(306,'mean +/- 1 sigma','F',1);
/*!40000 ALTER TABLE `constrain_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `django_session` VALUES ('4xa2dkp01kzrq02f5jxftzjrigmlyzi0','.eJxVjEEOwiAQRe_C2hAGHAou3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIirDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqt9dmycUYnhd64jOQyOMdRgzXMRSEm8AYKFK8Lki3shwhaxQEzcAHx_gDHZzd2:1qOaf5:pk2OJ76DiU1B5GfGBEVm7gmFu_Uk_ewpUQPFAgOK8WI','2023-08-09 09:18:27.340606'),('af27azqe98h45c353p5lyxjur8dwoe4k','.eJxVjEEOwiAQRe_C2hAGHAou3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIirDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqt9dmycUYnhd64jOQyOMdRgzXMRSEm8AYKFK8Lki3shwhaxQEzcAHx_gDHZzd2:1qBu5K:hxT7PptW9h3rECEFLdZUbgYXvHNK-H0bi3SUqeLClQA','2023-07-05 09:25:06.914202'),('om5wkj5b5clpviqbxzl9h6ixahn1j81b','.eJxVjEEOwiAQRe_C2hAGHAou3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIirDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqt9dmycUYnhd64jOQyOMdRgzXMRSEm8AYKFK8Lki3shwhaxQEzcAHx_gDHZzd2:1qRY35:bB9BwOoqZFdaywk1LJTlZIfpFL9OtPQL7VBzQJd4LA8','2023-08-17 13:07:27.831255'),('y33pqcs67pamc8qjntp7z1v9avs4d503','.eJxVjDsOwjAQBe_iGllr5M-Gkp4zWGvvggPIluKkirg7iZQC2jczb1WRlrnEpcsUR1YXZdTpd0uUX1J3wE-qj6Zzq_M0Jr0r-qBd3xrL-3q4fweFetlqQmGXPVIOAJ4pWXByRhqIMWVEIHvHAB5AQh7IihFjHaBDTpvi1ecL-NI4MQ:1qBEOH:2-d4IvR_kZj-RWp6NODkQlx9adY1s6ftBgeKjhieQ2g','2023-07-03 12:53:53.536921');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `method_ns`
--

DROP TABLE IF EXISTS `method_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `method_ns` (
  `id_Method` int NOT NULL AUTO_INCREMENT,
  `Method` enum('Pulsar timing','Thermal emission','Phase-resolved thermal emission') NOT NULL,
  `Method_Specific` text NOT NULL,
  `ProcessinfInfo` text NOT NULL,
  `DataDate` text NOT NULL,
  PRIMARY KEY (`id_Method`)
) ENGINE=InnoDB AUTO_INCREMENT=543 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `method_ns`
--

LOCK TABLES `method_ns` WRITE;
/*!40000 ALTER TABLE `method_ns` DISABLE KEYS */;
INSERT INTO `method_ns` VALUES (527,'Thermal emission','Spectral fitting (FUV and Xray data)','See Kargalstev2004, Durant2012, Guillot2016','FUV (Kargalstev2004 + Durant2012), X-ray (Rosat, up to 0.3 keV)'),(528,'Thermal emission','Spectral fitting (FUV and Xray data)','See Kargalstev2004, Durant2012, Guillot2016','FUV (Kargalstev2004 + Durant2012), X-ray (Guillot2016, Rosat, up to 0.3 keV)'),(529,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo2 packages','NANOGrav 15-year (2008-2022)'),(530,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo2 packages','NANOGrav 11-year (2008-2016)'),(531,'Pulsar timing','PK Parameters (Shapiro)','psrchive and Tempo packages','GBT 20131214-20200406 and CHIME 20190203-20200506'),(532,'Phase-resolved thermal emission','Phase-resolved spectral timing','NICERDAS v5, CALDB 20181105 (optmv7), see Bogdanov et al. 2019 for processing details','NICER (July 2017 to December 2018)'),(533,'Phase-resolved thermal emission','Phase-resolved spectral timing','NICERDAS v6, CALDB v20200202, see Wolff et al. 2021 for processing details','NICER (Sept. 2018 to April 2020) and XMM-Newton (Oct. 2019)'),(534,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.9 & CALDB v4.7.3; SAS v15.0.0','ROSAT data (1992), XMM-Newton (2002, 2016), Chandra (2006)'),(535,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.13','Chandra (2002, 2008, 2015)'),(536,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.10 and CALDB v.4.8.2','Chandra (2001, 2017)'),(537,'Thermal emission','Spectral fitting (X-ray data)','SAS v7.0','XMM-Newton (2005)'),(538,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.5, SAS 13.0','Chandra (2000, 2012), XMM-Newton (2001)'),(539,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.9 (reprocessing in 2017)','Chandra (2010)'),(540,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.5','Chandra (2000, 2002, 2007)'),(541,'Thermal emission','Spectral fitting (X-ray data)','CIAO v4.7 & CALDB v4.6.7','Chandra (2000, 2002, 2014, 2015)'),(542,'Pulsar timing','Frequency measurement','psrchive and Tempo packages','June 2004 to May 2005');
/*!40000 ALTER TABLE `method_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_ns`
--

DROP TABLE IF EXISTS `model_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model_ns` (
  `id_Model` int NOT NULL AUTO_INCREMENT,
  `DependenciesPrimary` varchar(60) DEFAULT NULL,
  `DependenciesSecondary` varchar(60) DEFAULT NULL,
  `DependenciesDescription` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `DependenciesReferences` text,
  PRIMARY KEY (`id_Model`)
) ENGINE=InnoDB AUTO_INCREMENT=573 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_ns`
--

LOCK TABLES `model_ns` WRITE;
/*!40000 ALTER TABLE `model_ns` DISABLE KEYS */;
INSERT INTO `model_ns` VALUES (533,'atmosphere','Gonzalez2019','The atmosphere model used in this analysis was calculated for low-temperature atmosphere (<10^5.5 K) and includes the effect of plasma.','2019MNRAS.490.5848G '),(534,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using absorption tables based on the tbabs model of Wilms et al. 2000 (updated in 2016).','2000ApJ...542..914W'),(535,'\nredenning','\nClayton2003','The frequency-dependent reddening has been implemented based on results of Clayton et al. 2003 (Fig. 1).','2003ApJ...585..464C'),(536,'\nhot spots model','\n2 blackbodies','The contribution of the two hot spots to the X-ray spectrum analysed (<0.3 keV) was included using 2 blackbody components.','2019MNRAS.490.5848G'),(537,'\nredenning','\nClayton2003','The frequency-dependent reddening has been implemented based on results of Clayton et al. 2003 (Fig.1).','2003ApJ...585..464C'),(538,'\nhot spots model','\nignored','The contribution of the hot spots to the X-ray spectrum analysed (<0.3 keV) was ignored.','2019MNRAS.490.5848G'),(539,'Shapiro delay','m_c sini parametrization','The Shapiro delay is estimated using the traditional Mcomp and sini parametrization.','Agazie et al. 2023, 2023ApJL..951...L9'),(540,'Shapiro delay','m_c sini parametrization','The Shapiro delay is estimated using the traditional Mcomp and sini parametrization.','Arzoumanian et al. 2018, 2018ApJS..235...37A'),(541,'Dispersion measure','DMX','Three different piece-wise DMX models were employed in the analysis of Fonseca et al. 2021 and the averaged mass from these 3 analyses was reported.','Fonseca et al. 2021, 2021ApJ...915L..12F'),(542,'atmosphere','nsx','The atmosphere model used in this analysis is the nsx model (Ho and Heinke 2009) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2019).','2009Natur.462...71H, 2019ApJ...887L..21R'),(543,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 (updated in 2016) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2019).','2000ApJ...542..914W, 2019ApJ...887L..21R'),(544,'\nray-tracing','\noblate Schwarzschild and Doppler','The ray-tracing model accounting for the trajectory of photons and other effects of gravity adopts the Schwarzschild metric, assumes an oblate neutron star (using the oblateness-frequency relation of AlGendy and Morsink (2014), and includes the Doppler effects. The full ray-tracing model is described in Bogdanov et al. 2019 (Paper II).','2014ApJ...791...78A, 2019ApJ...887L..26B'),(545,'\neos dependence','\noblateness','The oblateness-frequency relation of AlGendy and Morsink (2014) is EOS-independent. However, it was quantified from nucleonic EOS.  Different interior compositions may affect this relation, and therefore the ray-tracing calculations.','2014ApJ...791...78A'),(546,'\nbackground','\nno assumed background','In this analysis, no a-priori background was assumed (see Riley et al. 2019).','2019ApJ...887L..21R'),(547,'\nsampler','\nmultinest','For the inference, the multinest sampler was used (Feroz & Hobson 2008, Feroz et al. 2009, Buchner et al. 2014) with the following parameters:  1000 live points, Inverse hypervolume expansion factor (q) 0.8,  Termination condition: 0.1 (see Riley et al. 2019).','2008MNRAS.384..449F, 2009MNRAS.398.1601F, 2014A&A...564A.125B, 2019ApJ...887L..21R'),(548,'atmosphere','nsx','The atmosphere model used in this analysis is the nsx model (Ho and Heinke 2009) available under the form of precalculated tables.','2009Natur.462...71H'),(549,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 (updated in 2016) available under the form of precalculated tables.','2000ApJ...542..914W'),(550,'\nbackground','\nno assumed background','In this analysis, no a-priori background was assumed (see Miller et al. 2019).','2019ApJ...887L..24M'),(551,'\nsampler','\nhybrid PT-emcee + multinest','For the parameter estimation, an hybrid sampler was used, with the complementary advantages of multinest (Feroz & Hobson 2008, Feroz et al. 2009, Buchner et al. 2014) and of the parallel-tempering emcee (Foreman-Mackey et al. 2013).  The initial sampling of the parameter space was performed with multinest (1000 live points, efficiency of 0.01, and tolerance of 0.1). Then the high-likelihood points of this initial sampling were then explored with PT-emcee (with 1000 walkers and default temperature ladder). See Miller et al. 2019 for details.','2008MNRAS.384..449F, 2009MNRAS.398.1601F, 2014A&A...564A.125B, 2013PASP..125..306F, 2019ApJ...887L..24M'),(552,'atmosphere','nsx','The atmosphere model used in this analysis is the nsx model (Ho and Heinke 2009) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2021).','2009Natur.462...71H, 2021ApJ...918L..27R'),(553,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 (updated in 2016) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2021).','2000ApJ...542..914W, 2021ApJ...918L..27R'),(554,'\nbackground','\nno assumed background','In this analysis, no a-priori background was assumed for the NICER data. However, the XMM-Newton phase-averaged spectrum used in the analysis is associated with a background spectrum (measured on the same CCD near the pulsar).  Therefore, in the joint analysis of NICER data with XMM-Newton, the total phase-averaged flux inferred for NICER is constrained by the phase-averaged XMM flux. In practice, this constrains the inferred NICER background. See Riley et al. 2021 for more details. See also Salmi et al. 2022 for more analyses on the NICER background.','2021ApJ...918L..27R, 2022ApJ...941..150S'),(555,'\nsampler','\nmultinest','For the inference, the multinest sampler was used (Feroz & Hobson 2008, Feroz et al. 2009, Buchner et al. 2014) with the following parameters:  40000 live points, Inverse hypervolume expansion factor 1/0.1,  Termination condition: 0.1 (see Riley et al. 2021).','2008MNRAS.384..449F, 2009MNRAS.398.1601F, 2014A&A...564A.125B, 2021ApJ...918L..27R'),(556,'atmosphere','nsx','The atmosphere model used in this analysis is the nsx model (Ho and Heinke 2009) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2021).','2009Natur.462...71H'),(557,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 (updated in 2016) available under the form of precalculated tables (see Zenodo associated with Riley et al. 2021).','2000ApJ...542..914W'),(558,'\nbackground','\nno assumed background','In this analysis, no a-priori background was assumed for the NICER data. However, the XMM-Newton phase-averaged spectrum used in the analysis is associated with a background spectrum (measured on the same CCD near the pulsar).  Therefore, in the joint analysis of NICER data with XMM-Newton, the total phase-averaged flux inferred for NICER is constrained by the phase-averaged XMM flux. In practice, this constrains the inferred NICER background. See Riley et al. 2021 for more details. See also Salmi et al. 2022 for more analyses on the NICER background.','2021ApJ...918L..28M, 2022ApJ...941..150S'),(559,'\nsampler','\nhybrid PT-emcee + multinest','For the parameter estimation, an hybrid sampler was used, with the complementary advantages of multinest (Feroz & Hobson 2008, Feroz et al. 2009, Buchner et al. 2014) and of the parallel-tempering emcee (Foreman-Mackey et al. 2013).  The initial sampling of the parameter space was performed with multinest (1000 live points, efficiency of 0.01, and tolerance of 0.1). Then the high-likelihood points of this initial sampling were then explored with PT-emcee (with 1000 walkers and default temperature ladder). See Miller et al. 2021 for details.','2008MNRAS.384..449F, 2009MNRAS.398.1601F, 2014A&A...564A.125B, 2013PASP..125..306F, 2021ApJ...918L..28M'),(560,'atmosphere','nsatmos','The atmosphere model used in this analysis is the nsatmos model (Heinke et al. 2006) available under the form of precalculated tables in Xspec, directly usable for spectral analyses.','2006ApJ...644.1090H'),(561,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 (updated in 2016) available in Xspec.','2000ApJ...542..914W'),(562,'atmosphere','nsx','The atmosphere model used in this analysis is the nsx model (Ho and Heinke 2009) available under the form of precalculated tables in Xspec, directly usable for spectral analyses.','2009Natur.462...71H'),(563,'\npile-up model','\npileup','Because of the brightness of the source, photons may pile-up on the detectors -- more than 1 photons incident on the same pixel without the readout time frame, and detected as a single photon with the sum of the energies.  This effect, which may distort the spectrum (toward higher energies) may be accounted for with an instrument-specific pile-up model (\'pileup\' in Xspec, Davis 2001).','2001ApJ...562..575D'),(564,'\nextra component','\npowerlaw','To account for a possible excess of photons at high-energy (> 2 keV), an addition power-law component was added (with fixed index of 1.5) and free normalisation (see Guillot et al. 2013).','2013ApJ...772....7G, 2020MNRAS.495.4508E'),(565,'atmosphere','phabs','The atmosphere model used in this analysis is the nsatmos model (Heinke et al. 2006) available under the form of precalculated tables in Xspec, directly usable for spectral analyses.','2006ApJ...644.1090H'),(566,' \nabsorption','\nnsatmos','The absorption of X-rays was calculated using phabs absorption model available in Xspec (Arnaud et al. 1996).','1996ASPC..101...17A'),(567,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000 available in Xspec.','2000ApJ...542..914W'),(568,'\nextra component','\npowerlaw','To account for a possible excess of photons at high-energy (> 2 keV), an addition power-law component was added (with fixed index of 1.5) and free normalisation (see Guillot et al. 2013).','2013ApJ...772....7G, 2014MNRAS.444..443H'),(569,'\nextra component','\npowerlaw','To account for a possible excess of photons at high-energy (> 2 keV), an addition power-law component was added (with fixed index of 1.5) and free normalisation (see Guillot et al. 2013).','2013ApJ...772....7G'),(570,'\npile-up model','\npileup','Depending on the brightness of an X-ray source, photons may pile-up on the detectors -- more than 1 photons incident on the same pixel without the readout time frame, and detected as a single photon with the sum of the energies.  This effect, which may distort the spectrum (toward higher energies) may be accounted for with an instrument-specific pile-up model (\'pileup\' in Xspec, Davis 2001). However, it was found to be negligible for this particular source.','2001ApJ...562..575D'),(571,'\nabsorption','\ntbabs','The absorption of X-rays was calculated using tbabs absorption model of Wilms et al. 2000  available in Xspec.','2000ApJ...542..914W'),(572,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `model_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `name_ns`
--

DROP TABLE IF EXISTS `name_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=500 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `name_ns`
--

LOCK TABLES `name_ns` WRITE;
/*!40000 ALTER TABLE `name_ns` DISABLE KEYS */;
INSERT INTO `name_ns` VALUES (485,'PSR J0437-4715','Cold MSP','PSR J0437-47','Psr',69.3158310000,-47.2523730000,NULL,NULL),(486,'PSR J1614-2230','NS mass','PSR J1614-2230','Psr',243.6521120000,-22.5086690000,NULL,NULL),(487,'PSR J0740+6620','NS mass','PSR J0740+6620','Psr',115.1908290000,66.3426670000,NULL,NULL),(488,'PSR J0030+0451','PPM','PSR J0030+0451','Psr',7.6142820000,4.8610310000,NULL,NULL),(489,'PSR J0740+6620','PPM','PSR J0740+6620','Psr',115.1908290000,66.3426670000,NULL,NULL),(490,'M13_qlmxb','qLMXB','2XMM J164143.6+362758','LXB',250.4323380000,36.4660670000,NULL,NULL),(491,'M28_qlmxb','qLMXB','CXOGlb J182432.8-245208','LXB',276.1367540000,-24.8689610000,NULL,NULL),(492,'M30_qlmxb','qLMXB','CXOGlb J214022.1-231045','LXB',325.0923380000,-23.1794580000,NULL,NULL),(493,'NGC 2808','qLMXB','NGC 2808 C2','X',138.0068750000,-64.8500000000,NULL,NULL),(494,'NGC5139_qLMXB','qLMXB','CXOU J132619.7-472910','X',201.5824830000,-47.4862530000,NULL,NULL),(495,'NGC6304_qLMXB','qLMXB','CXOU J171432.9-292748','X',258.6372080000,-29.4633330000,NULL,NULL),(496,'NGC_6397_qlmxb','qLMXB','CXOGlb J174041.4-534004','LXB',265.1727833000,-53.6678972000,NULL,NULL),(497,'47TucX5_qLMXB','qLMXB','CXOGlb J002400.9-720453','LXB',6.0040330000,-72.0814390000,NULL,NULL),(498,'47TucX7_qLMXB','qLMXB','CXOGlb J002403.4-720451','LXB',6.0145580000,-72.0810940000,NULL,NULL),(499,'PSR J1748-2446ad','NS spin','PSR J1748-2446ad','Psr',267.0204170000,-24.7677780000,NULL,NULL);
/*!40000 ALTER TABLE `name_ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns`
--

DROP TABLE IF EXISTS `ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `ns` VALUES ('Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy','qdsdsqdsqdsq.txt',434,485,528,300),('Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy','qdsdsqdsqdsq.txt',434,485,527,300),
('NS_Mass_PSRJ0740+6620_2020_mass_shapiro_1.txt','qdsdsqdsqdsq.txt',437,487,531,301),
('NS_Mass_PSRJ1614-2230_NANOgrav11yr_mass_shapiro_1.txt','qdsdsqdsqdsq.txt',436,486,530,302),
('NS_Mass_PSRJ1614-2230_NANOgrav15yr_mass_shapiro_2.txt','qdsdsqdsqdsq.txt',435,486,529,301),
('NS_Spin_PSRJ1748-2446ad_2005_spin_1.txt','qdsdsqdsqdsq.txt',449,499,542,306),
('PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt','qdsdsqdsqdsq.txt',439,488,532,303),
('PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt','qdsdsqdsqdsq.txt',438,488,532,303),
('PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt','qdsdsqdsqdsq.txt',441,489,533,303),
('PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt','qdsdsqdsqdsq.txt',440,489,533,303),
('qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',448,497,541,305),
('qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt','qdsdsqdsqdsq.txt',448,498,541,305),
('qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',448,498,541,305),
('qLMXB_M13_qLMXB_2018_massradius_helium_1.txt','qdsdsqdsqdsq.txt',442,490,534,304),
('qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',442,490,534,304),
('qLMXB_M28_qLMXB_2022_massradius_helium_1.txt','qdsdsqdsqdsq.txt',443,491,535,305),
('qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',443,491,535,305),
('qLMXB_M30_qLMXB_2020_massradius_helium_1.txt','qdsdsqdsqdsq.txt',444,492,536,300),
('qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',444,492,536,300),
('qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',445,493,537,305),
('qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',446,494,538,305),
('qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',447,495,539,305),
('qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt','qdsdsqdsqdsq.txt',446,496,540,305),
('qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt','qdsdsqdsqdsq.txt',446,496,540,305);
/*!40000 ALTER TABLE `ns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns_to_assumptions`
--

DROP TABLE IF EXISTS `ns_to_assumptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ns_to_assumptions` (
  `id_ns_to_assumptions` int NOT NULL AUTO_INCREMENT,
  `id_Assumptions` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_assumptions`),
  UNIQUE KEY `Uni_cons` (`id_Assumptions`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_assumptions_ibfk_1` FOREIGN KEY (`id_Assumptions`) REFERENCES `assumptions_ns` (`id_Assumptions`),
  CONSTRAINT `ns_to_assumptions_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=3377 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ns_to_assumptions`
--

LOCK TABLES `ns_to_assumptions` WRITE;
/*!40000 ALTER TABLE `ns_to_assumptions` DISABLE KEYS */;
INSERT INTO `ns_to_assumptions` VALUES (3227,929,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),(3355,929,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3362,929,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3285,929,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3299,929,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3311,929,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3323,929,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3329,929,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3336,929,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3343,929,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3236,930,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3228,930,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3229,931,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3238,932,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3230,932,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3239,933,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3231,933,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3240,934,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3232,934,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3241,935,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3233,935,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3234,936,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(3235,937,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3369,937,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3292,937,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3305,937,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3317,937,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3349,937,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3237,938,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(3242,939,'NS_Mass_PSRJ1614-2230_NANOgrav15yr_mass_shapiro_2.txt'),
(3243,940,'NS_Mass_PSRJ1614-2230_NANOgrav11yr_mass_shapiro_1.txt'),
(3244,941,'NS_Mass_PSRJ0740+6620_2020_mass_shapiro_1.txt'),
(3254,942,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3245,942,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3274,942,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3263,942,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3255,943,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3246,943,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3275,943,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3264,943,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3256,944,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3247,944,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3276,944,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3265,944,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3257,945,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3248,945,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3277,945,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3266,945,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3258,946,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3249,946,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3278,946,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3267,946,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3250,947,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3260,948,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3251,948,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3261,949,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3252,949,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3253,950,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(3259,951,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3262,952,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(3268,953,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3280,954,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3269,954,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3270,955,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3271,956,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3272,957,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3273,958,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(3279,959,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3281,960,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3282,961,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3283,962,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3284,963,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(3356,964,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3370,964,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3363,964,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3293,964,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3286,964,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3306,964,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3300,964,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3318,964,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3312,964,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3324,964,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3330,964,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3337,964,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3350,964,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3344,964,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3357,965,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3371,965,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3364,965,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3294,965,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3287,965,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3307,965,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3301,965,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3319,965,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3313,965,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3325,965,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3331,965,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3338,965,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3351,965,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3345,965,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3295,966,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3288,966,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3359,967,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3373,967,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3366,967,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3296,967,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3289,967,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3309,967,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3303,967,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3321,967,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3315,967,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3333,967,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3340,967,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3353,967,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3347,967,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3297,968,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3290,968,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3298,969,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(3291,969,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(3308,970,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3302,970,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3304,971,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(3310,972,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(3320,973,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3314,973,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3322,974,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(3316,974,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(3326,975,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3327,976,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3328,977,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(3332,978,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3352,978,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3346,978,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3334,979,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3335,980,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(3339,981,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3341,982,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3342,983,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(3354,984,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(3348,984,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(3358,985,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3372,985,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3365,985,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3360,986,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3374,986,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3367,986,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3361,987,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(3375,987,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(3368,987,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(3376,988,'NS_Spin_PSRJ1748-2446ad_2005_spin_1.txt');
/*!40000 ALTER TABLE `ns_to_assumptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ns_to_model`
--

DROP TABLE IF EXISTS `ns_to_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ns_to_model` (
  `id_ns_to_model` int NOT NULL AUTO_INCREMENT,
  `id_Model` int NOT NULL,
  `FileName` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ns_to_model`),
  UNIQUE KEY `Uni_con_mod` (`id_Model`,`FileName`),
  KEY `FileName` (`FileName`),
  CONSTRAINT `ns_to_model_ibfk_1` FOREIGN KEY (`id_Model`) REFERENCES `model_ns` (`id_Model`),
  CONSTRAINT `ns_to_model_ibfk_2` FOREIGN KEY (`FileName`) REFERENCES `ns` (`FileName`)
) ENGINE=InnoDB AUTO_INCREMENT=1451 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ns_to_model`
--

LOCK TABLES `ns_to_model` WRITE;
/*!40000 ALTER TABLE `ns_to_model` DISABLE KEYS */;
INSERT INTO `ns_to_model` VALUES (1377,533,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(1373,533,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),(1378,534,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(1374,534,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(1375,535,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(1376,536,'Cold_MSP_PSRJ0437-4715_2019_massradius_hydrogen_1.npy'),
(1379,537,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(1380,538,'Cold_MSP_PSRJ0437-4715_2019_massradius_helium_1.npy'),
(1381,539,'NS_Mass_PSRJ1614-2230_NANOgrav15yr_mass_shapiro_2.txt'),
(1382,540,'NS_Mass_PSRJ1614-2230_NANOgrav11yr_mass_shapiro_1.txt'),
(1383,541,'NS_Mass_PSRJ0740+6620_2020_mass_shapiro_1.txt'),
(1384,542,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1385,543,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1392,544,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1386,544,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1404,544,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1398,544,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1393,545,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1387,545,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1405,545,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1399,545,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1388,546,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1389,547,'PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1.txt'),
(1390,548,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1391,549,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1394,550,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1395,551,'PPM_PSRJ0030+0451_2019_massradius_2spots_Miller_1.txt'),
(1396,552,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1397,553,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1400,554,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1401,555,'PPM_PSRJ0740+6620_2021_massradius_STU_Riley_1.txt'),
(1402,556,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1403,557,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1406,558,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1407,559,'PPM_PSRJ0740+6620_2021_massradius_2spots_Miller_1.txt'),
(1441,560,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(1444,560,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(1408,560,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(1412,560,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(1418,560,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(1428,560,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(1431,560,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(1435,560,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(1411,561,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(1409,561,'qLMXB_M13_qLMXB_2018_massradius_hydrogen_1.txt'),
(1416,561,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(1413,561,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(1423,561,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(1419,561,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(1432,561,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(1447,562,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(1410,562,'qLMXB_M13_qLMXB_2018_massradius_helium_1.txt'),
(1415,562,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(1422,562,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(1438,562,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(1443,563,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(1449,563,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(1446,563,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(1417,563,'qLMXB_M28_qLMXB_2022_massradius_helium_1.txt'),
(1414,563,'qLMXB_M28_qLMXB_2022_massradius_hydrogen_1.txt'),
(1425,563,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(1421,563,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(1424,564,'qLMXB_M30_qLMXB_2020_massradius_helium_1.txt'),
(1420,564,'qLMXB_M30_qLMXB_2020_massradius_hydrogen_1.txt'),
(1426,565,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(1427,566,'qLMXB_NGC2808_qLMXB_2007_massradius_hydrogen_1.txt'),
(1448,567,'qLMXB_47TucX7_qLMXB_2016_massradius_helium_1.txt'),
(1429,567,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(1439,567,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(1436,567,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(1430,568,'qLMXB_NGC5139_qLMXB_2014_massradius_hydrogen_1.txt'),
(1440,568,'qLMXB_NGC6397_qLMXB_2014_massradius_helium_1.txt'),
(1437,568,'qLMXB_NGC6397_qLMXB_2014_massradius_hydrogen_1.txt'),
(1433,569,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(1434,570,'qLMXB_NGC6304_qLMXB_2017_massradius_hydrogen_1.txt'),
(1442,571,'qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1.txt'),
(1445,571,'qLMXB_47TucX7_qLMXB_2016_massradius_hydrogen_1.txt'),
(1450,572,'NS_Spin_PSRJ1748-2446ad_2005_spin_1.txt');
/*!40000 ALTER TABLE `ns_to_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref_ns`
--

DROP TABLE IF EXISTS `ref_ns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ref_ns` (
  `id_Ref` int NOT NULL AUTO_INCREMENT,
  `Author` varchar(30) NOT NULL,
  `RefYear` int NOT NULL,
  `Short` varchar(50) NOT NULL,
  `Bibtex` text NOT NULL,
  `DOI` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `RepositoryDOI` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DataLink` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id_Ref`)
) ENGINE=InnoDB AUTO_INCREMENT=450 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref_ns`
--

LOCK TABLES `ref_ns` WRITE;
/*!40000 ALTER TABLE `ref_ns` DISABLE KEYS */;
INSERT INTO `ref_ns` VALUES (434,'Gonzalez-Canuilef',2019,'2019MNRAS.490.5848G','@ARTICLE{2019MNRAS.490.5848G,\n       author = {{Gonz{\\\'a}lez-Caniulef}, Denis and {Guillot}, Sebastien and {Reisenegger}, Andreas},\n        title = \"{Neutron star radius measurement from the ultraviolet and soft X-ray thermal emission of PSR J0437-4715}\",\n      journal = {\\mnras},\n     keywords = {dense matter, equation of state, plasmas, stars: atmospheres, stars: neutron, pulsars: individual (PSR J0437-4715), Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2019,\n        month = dec,\n       volume = {490},\n       number = {4},\n        pages = {5848-5859},\n          doi = {10.1093/mnras/stz2941},\narchivePrefix = {arXiv},\n       eprint = {1904.12114},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.5848G},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1093/mnras/stz2941',NULL,NULL),(435,'Agazie',2023,'2023ApJL..951...L9','@ARTICLE{2018ApJS..235...37A,\n       author = {{Arzoumanian}, Zaven and {Brazier}, Adam and {Burke-Spolaor}, Sarah and {Chamberlin}, Sydney and {Chatterjee}, Shami and {Christy}, Brian and {Cordes}, James M. and {Cornish}, Neil J. and {Crawford}, Fronefield and {Thankful Cromartie}, H. and {Crowter}, Kathryn and {DeCesar}, Megan E. and {Demorest}, Paul B. and {Dolch}, Timothy and {Ellis}, Justin A. and {Ferdman}, Robert D. and {Ferrara}, Elizabeth C. and {Fonseca}, Emmanuel and {Garver-Daniels}, Nathan and {Gentile}, Peter A. and {Halmrast}, Daniel and {Huerta}, E.~A. and {Jenet}, Fredrick A. and {Jessup}, Cody and {Jones}, Glenn and {Jones}, Megan L. and {Kaplan}, David L. and {Lam}, Michael T. and {Lazio}, T. Joseph W. and {Levin}, Lina and {Lommen}, Andrea and {Lorimer}, Duncan R. and {Luo}, Jing and {Lynch}, Ryan S. and {Madison}, Dustin and {Matthews}, Allison M. and {McLaughlin}, Maura A. and {McWilliams}, Sean T. and {Mingarelli}, Chiara and {Ng}, Cherry and {Nice}, David J. and {Pennucci}, Timothy T. and {Ransom}, Scott M. and {Ray}, Paul S. and {Siemens}, Xavier and {Simon}, Joseph and {Spiewak}, Ren{\\\'e}e and {Stairs}, Ingrid H. and {Stinebring}, Daniel R. and {Stovall}, Kevin and {Swiggum}, Joseph K. and {Taylor}, Stephen R. and {Vallisneri}, Michele and {van Haasteren}, Rutger and {Vigeland}, Sarah J. and {Zhu}, Weiwei and {NANOGrav Collaboration}},\n        title = \"{The NANOGrav 11-year Data Set: High-precision Timing of 45 Millisecond Pulsars}\",\n      journal = {\\apjs},\n     keywords = {binaries: general, gravitational waves, parallaxes, proper motions, pulsars: general, stars: neutron},\n         year = 2018,\n        month = apr,\n       volume = {235},\n       number = {2},\n          eid = {37},\n        pages = {37},\n          doi = {10.3847/1538-4365/aab5b0},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2018ApJS..235...37A},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/acda9a',NULL,NULL),(436,'Arzoumanian',2018,'2018ApJS..235...37A','@ARTICLE{2018ApJS..235...37A,\n       author = {{Arzoumanian}, Zaven and {Brazier}, Adam and {Burke-Spolaor}, Sarah and {Chamberlin}, Sydney and {Chatterjee}, Shami and {Christy}, Brian and {Cordes}, James M. and {Cornish}, Neil J. and {Crawford}, Fronefield and {Thankful Cromartie}, H. and {Crowter}, Kathryn and {DeCesar}, Megan E. and {Demorest}, Paul B. and {Dolch}, Timothy and {Ellis}, Justin A. and {Ferdman}, Robert D. and {Ferrara}, Elizabeth C. and {Fonseca}, Emmanuel and {Garver-Daniels}, Nathan and {Gentile}, Peter A. and {Halmrast}, Daniel and {Huerta}, E.~A. and {Jenet}, Fredrick A. and {Jessup}, Cody and {Jones}, Glenn and {Jones}, Megan L. and {Kaplan}, David L. and {Lam}, Michael T. and {Lazio}, T. Joseph W. and {Levin}, Lina and {Lommen}, Andrea and {Lorimer}, Duncan R. and {Luo}, Jing and {Lynch}, Ryan S. and {Madison}, Dustin and {Matthews}, Allison M. and {McLaughlin}, Maura A. and {McWilliams}, Sean T. and {Mingarelli}, Chiara and {Ng}, Cherry and {Nice}, David J. and {Pennucci}, Timothy T. and {Ransom}, Scott M. and {Ray}, Paul S. and {Siemens}, Xavier and {Simon}, Joseph and {Spiewak}, Ren{\\\'e}e and {Stairs}, Ingrid H. and {Stinebring}, Daniel R. and {Stovall}, Kevin and {Swiggum}, Joseph K. and {Taylor}, Stephen R. and {Vallisneri}, Michele and {van Haasteren}, Rutger and {Vigeland}, Sarah J. and {Zhu}, Weiwei and {NANOGrav Collaboration}},\n        title = \"{The NANOGrav 11-year Data Set: High-precision Timing of 45 Millisecond Pulsars}\",\n      journal = {\\apjs},\n     keywords = {binaries: general, gravitational waves, parallaxes, proper motions, pulsars: general, stars: neutron},\n         year = 2018,\n        month = apr,\n       volume = {235},\n       number = {2},\n          eid = {37},\n        pages = {37},\n          doi = {10.3847/1538-4365/aab5b0},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2018ApJS..235...37A},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/1538-4365/aab5b0',NULL,NULL),(437,'Fonseca',2021,'2021ApJ...915L..12F','@ARTICLE{2021ApJ...915L..12F,\n       author = {{Fonseca}, E. and {Cromartie}, H.~T. and {Pennucci}, T.~T. and {Ray}, P.~S. and {Kirichenko}, A. Yu. and {Ransom}, S.~M. and {Demorest}, P.~B. and {Stairs}, I.~H. and {Arzoumanian}, Z. and {Guillemot}, L. and {Parthasarathy}, A. and {Kerr}, M. and {Cognard}, I. and {Baker}, P.~T. and {Blumer}, H. and {Brook}, P.~R. and {DeCesar}, M. and {Dolch}, T. and {Dong}, F.~A. and {Ferrara}, E.~C. and {Fiore}, W. and {Garver-Daniels}, N. and {Good}, D.~C. and {Jennings}, R. and {Jones}, M.~L. and {Kaspi}, V.~M. and {Lam}, M.~T. and {Lorimer}, D.~R. and {Luo}, J. and {McEwen}, A. and {McKee}, J.~W. and {McLaughlin}, M.~A. and {McMann}, N. and {Meyers}, B.~W. and {Naidu}, A. and {Ng}, C. and {Nice}, D.~J. and {Pol}, N. and {Radovan}, H.~A. and {Shapiro-Albert}, B. and {Tan}, C.~M. and {Tendulkar}, S.~P. and {Swiggum}, J.~K. and {Wahl}, H.~M. and {Zhu}, W.~W.},\n        title = \"{Refined Mass and Geometric Measurements of the High-mass PSR J0740+6620}\",\n      journal = {\\apjl},\n     keywords = {Neutron stars, Pulsars, General relativity, Compact objects, Binary pulsars, 1108, 1306, 641, 288, 153},\n         year = 2021,\n        month = jul,\n       volume = {915},\n       number = {1},\n          eid = {L12},\n        pages = {L12},\n          doi = {10.3847/2041-8213/ac03b8},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJ...915L..12F},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/ac03b8',NULL,NULL),(438,'Riley',2019,'2019ApJ...887L..21R','@ARTICLE{2019ApJ...887L..21R, author = {{Riley}, T.~E. and {Watts}, A.~L. and {Bogdanov}, S. and {Ray}, P.~S. and {Ludlam}, R.~M. and {Guillot}, S. and {Arzoumanian}, Z. and {Baker}, C.~L. and {Bilous}, A.~V. and {Chakrabarty}, D. and {Gendreau}, K.~C. and {Harding}, A.~K. and {Ho}, W.~C.~G. and {Lattimer}, J.~M. and {Morsink}, S.~M. and {Strohmayer}, T.~E.},  title = \"{A NICER View of PSR J0030+0451: Millisecond Pulsar Parameter Estimation}\",  journal = {\\apjl},  keywords = {Matter density, Rotation powered pulsars, Millisecond pulsars, Pulsars, X-ray stars, Neutron stars, Neutron star cores, Nuclear astrophysics, 1014, 1408, 1062, 1306, 1823, 1108, 1107, 1129, Astrophysics - High Energy Astrophysical Phenomena, Astrophysics - Solar and Stellar Astrophysics, Nuclear Theory}, year = 2019, month = dec,volume = {887}, number = {1}, eid = {L21},pages = {L21},doi = {10.3847/2041-8213/ab481c}, archivePrefix = {arXiv},  eprint = {1912.05702}, primaryClass = {astro-ph.HE},adsurl = {https://ui.adsabs.harvard.edu/abs/2019ApJ...887L..21R}, adsnote = {Provided by the SAO/NASA Astrophysics Data System}}','10.3847/2041-8213/ab481c','10.5281/zenodo.3386448','https://zenodo.org/record/3386448'),(439,'Miller',2019,'2019ApJ...887L..24M','@ARTICLE{2019ApJ...887L..24M,\n       author = {{Miller}, M.~C. and {Lamb}, F.~K. and {Dittmann}, A.~J. and {Bogdanov}, S. and {Arzoumanian}, Z. and {Gendreau}, K.~C. and {Guillot}, S. and {Harding}, A.~K. and {Ho}, W.~C.~G. and {Lattimer}, J.~M. and {Ludlam}, R.~M. and {Mahmoodifar}, S. and {Morsink}, S.~M. and {Ray}, P.~S. and {Strohmayer}, T.~E. and {Wood}, K.~S. and {Enoto}, T. and {Foster}, R. and {Okajima}, T. and {Prigozhin}, G. and {Soong}, Y.},\n        title = \"{PSR J0030+0451 Mass and Radius from NICER Data and Implications for the Properties of Neutron Star Matter}\",\n      journal = {\\apjl},\n     keywords = {X-ray sources, Millisecond pulsars, Neutron stars, Neutron star cores, 1822, 1062, 1108, 1107, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},\n         year = 2019,\n        month = dec,\n       volume = {887},\n       number = {1},\n          eid = {L24},\n        pages = {L24},\n          doi = {10.3847/2041-8213/ab50c5},\narchivePrefix = {arXiv},\n       eprint = {1912.05705},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2019ApJ...887L..24M},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/ab50c5','10.5281/zenodo.3473466','https://zenodo.org/record/3473466/files/J0030_2spot_RM.txt?download=1'),(440,'Riley',2021,'2021ApJ...918L..27R','@ARTICLE{2021ApJ...918L..27R,\n       author = {{Riley}, Thomas E. and {Watts}, Anna L. and {Ray}, Paul S. and {Bogdanov}, Slavko and {Guillot}, Sebastien and {Morsink}, Sharon M. and {Bilous}, Anna V. and {Arzoumanian}, Zaven and {Choudhury}, Devarshi and {Deneva}, Julia S. and {Gendreau}, Keith C. and {Harding}, Alice K. and {Ho}, Wynn C.~G. and {Lattimer}, James M. and {Loewenstein}, Michael and {Ludlam}, Renee M. and {Markwardt}, Craig B. and {Okajima}, Takashi and {Prescod-Weinstein}, Chanda and {Remillard}, Ronald A. and {Wolff}, Michael T. and {Fonseca}, Emmanuel and {Cromartie}, H. Thankful and {Kerr}, Matthew and {Pennucci}, Timothy T. and {Parthasarathy}, Aditya and {Ransom}, Scott and {Stairs}, Ingrid and {Guillemot}, Lucas and {Cognard}, Ismael},\n        title = \"{A NICER View of the Massive Pulsar PSR J0740+6620 Informed by Radio Timing and XMM-Newton Spectroscopy}\",\n      journal = {\\apjl},\n     keywords = {Millisecond pulsars, Rotation powered pulsars, Pulsars, Radio pulsars, X-ray astronomy, Neutron stars, 1062, 1408, 1306, 1353, 1810, 1108, Astrophysics - High Energy Astrophysical Phenomena, Astrophysics - Solar and Stellar Astrophysics, Nuclear Theory},\n         year = 2021,\n        month = sep,\n       volume = {918},\n       number = {2},\n          eid = {L27},\n        pages = {L27},\n          doi = {10.3847/2041-8213/ac0a81},\narchivePrefix = {arXiv},\n       eprint = {2105.06980},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJ...918L..27R},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/ac0a81','10.5281/zenodo.4697625','https://zenodo.org/record/4697625'),(441,'Miller',2021,'2021ApJ...918L..28M','@ARTICLE{2021ApJ...918L..28M,\n       author = {{Miller}, M.~C. and {Lamb}, F.~K. and {Dittmann}, A.~J. and {Bogdanov}, S. and {Arzoumanian}, Z. and {Gendreau}, K.~C. and {Guillot}, S. and {Ho}, W.~C.~G. and {Lattimer}, J.~M. and {Loewenstein}, M. and {Morsink}, S.~M. and {Ray}, P.~S. and {Wolff}, M.~T. and {Baker}, C.~L. and {Cazeau}, T. and {Manthripragada}, S. and {Markwardt}, C.~B. and {Okajima}, T. and {Pollard}, S. and {Cognard}, I. and {Cromartie}, H.~T. and {Fonseca}, E. and {Guillemot}, L. and {Kerr}, M. and {Parthasarathy}, A. and {Pennucci}, T.~T. and {Ransom}, S. and {Stairs}, I.},\n        title = \"{The Radius of PSR J0740+6620 from NICER and XMM-Newton Data}\",\n      journal = {\\apjl},\n     keywords = {X-ray sources, Millisecond pulsars, Neutron stars, Neutron star cores, 1822, 1062, 1108, 1107, Astrophysics - High Energy Astrophysical Phenomena, General Relativity and Quantum Cosmology, Nuclear Experiment, Nuclear Theory},\n         year = 2021,\n        month = sep,\n       volume = {918},\n       number = {2},\n          eid = {L28},\n        pages = {L28},\n          doi = {10.3847/2041-8213/ac089b},\narchivePrefix = {arXiv},\n       eprint = {2105.06979},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJ...918L..28M},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/2041-8213/ac089b','10.5281/zenodo.4670689','https://zenodo.org/record/4670689/files/NICER%2BXMM-relative_J0740_RM.txt?download=1'),(442,'Shaw',2018,'2018MNRAS.476.4713S','@ARTICLE{2018MNRAS.476.4713S,\n       author = {{Shaw}, A.~W. and {Heinke}, C.~O. and {Steiner}, A.~W. and {Campana}, S. and {Cohn}, H.~N. and {Ho}, W.~C.~G. and {Lugger}, P.~M. and {Servillat}, M.},\n        title = \"{The radius of the quiescent neutron star in the globular cluster M13}\",\n      journal = {\\mnras},\n     keywords = {stars: neutron, globular clusters: general, globular clusters: individual: M13, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2018,\n        month = jun,\n       volume = {476},\n       number = {4},\n        pages = {4713-4718},\n          doi = {10.1093/mnras/sty582},\narchivePrefix = {arXiv},\n       eprint = {1803.00029},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2018MNRAS.476.4713S},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}\n\n       author = {{Servillat}, M. and {Webb}, N.~A. and {Lewis}, F. and {Knigge}, C. and {van den Berg}, M. and {Dieball}, A. and {Grindlay}, J.},\n        title = \"{A Dwarf Nova in the Globular Cluster M13}\",\n      journal = {\\apj},\n     keywords = {globular clusters: individual: M13 NGC 6205, novae, cataclysmic variables, stars: dwarf novae, X-rays: general, Astrophysics - Solar and Stellar Astrophysics, Astrophysics - Astrophysics of Galaxies, Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2011,\n        month = jun,\n       volume = {733},\n       number = {2},\n          eid = {106},\n        pages = {106},\n          doi = {10.1088/0004-637X/733/2/106},\narchivePrefix = {arXiv},\n       eprint = {1103.4638},\n primaryClass = {astro-ph.SR},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2011ApJ...733..106S},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1093/mnras/sty582',NULL,NULL),(443,'Vurgun',2022,'2022ApJ...941...76V','@ARTICLE{2022ApJ...941...76V,\n       author = {{Vurgun}, Eda and {Linares}, Manuel and {Ransom}, Scott and {Papitto}, Alessandro and {Bogdanov}, Slavko and {Bozzo}, Enrico and {Rea}, Nanda and {Garc{\\\'\\i}a-Senz}, Domingo and {Freire}, Paulo and {Stairs}, Ingrid},\n        title = \"{The Neutron Star Population in M28: A Joint Chandra/GBT Look at Pulsar Paradise}\",\n      journal = {\\apj},\n     keywords = {Neutron stars, Millisecond pulsars, Low-mass x-ray binary stars, 1108, 1062, 939, Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2022,\n        month = dec,\n       volume = {941},\n       number = {1},\n          eid = {76},\n        pages = {76},\n          doi = {10.3847/1538-4357/ac9ea0},\narchivePrefix = {arXiv},\n       eprint = {2211.01067},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2022ApJ...941...76V},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/1538-4357/ac9ea0',NULL,NULL),(444,'Echiburu',2020,'2020MNRAS.495.4508E','@ARTICLE{2020MNRAS.495.4508E,\n       author = {{Echibur{\\\'u}}, C.~S. and {Guillot}, S. and {Zhao}, Y. and {Heinke}, C.~O. and {{\\\"O}zel}, F. and {Webb}, N.~A.},\n        title = \"{Spectral analysis of the quiescent low-mass X-ray binary in the globular cluster M30}\",\n      journal = {\\mnras},\n     keywords = {stars: neutron, globular clusters: individual: M30, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},\n         year = 2020,\n        month = jul,\n       volume = {495},\n       number = {4},\n        pages = {4508-4517},\n          doi = {10.1093/mnras/staa1456},\narchivePrefix = {arXiv},\n       eprint = {2005.11345},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2020MNRAS.495.4508E},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1093/mnras/staa1456',NULL,NULL),(445,'Webb',2007,'2007ApJ...671..727W','@ARTICLE{2007ApJ...671..727W,\n       author = {{Webb}, Natalie A. and {Barret}, Didier},\n        title = \"{Constraining the Equation of State of Supranuclear Dense Matter from XMM-Newton Observations of Neutron Stars in Globular Clusters}\",\n      journal = {\\apj},\n     keywords = {Dense Matter, Equation of State, globular clusters: individual ({\\ensuremath{\\omega}} Cen), Galaxy: Globular Clusters: Individual: Messier Number: M13, Galaxy: Globular Clusters: Individual: NGC Number: NGC 2808, Stars: Neutron, X-Rays: Stars, Astrophysics},\n         year = 2007,\n        month = dec,\n       volume = {671},\n       number = {1},\n        pages = {727-733},\n          doi = {10.1086/522877},\narchivePrefix = {arXiv},\n       eprint = {0708.3816},\n primaryClass = {astro-ph},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2007ApJ...671..727W},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1086/522877',NULL,NULL),(446,'Heinke',2014,'2014MNRAS.444..443H','@ARTICLE{2014MNRAS.444..443H,\n       author = {{Heinke}, C.~O. and {Cohn}, H.~N. and {Lugger}, P.~M. and {Webb}, N.~A. and {Ho}, W.~C.~G. and {Anderson}, J. and {Campana}, S. and {Bogdanov}, S. and {Haggard}, D. and {Cool}, A.~M. and {Grindlay}, J.~E.},\n        title = \"{Improved mass and radius constraints for quiescent neutron stars in {\\ensuremath{\\omega}} Cen and NGC 6397}\",\n      journal = {\\mnras},\n     keywords = {dense matter, stars: neutron, globular clusters: individual: NGC 6397, globular clusters: individual: NGC 5139, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},\n         year = 2014,\n        month = oct,\n       volume = {444},\n       number = {1},\n        pages = {443-456},\n          doi = {10.1093/mnras/stu1449},\narchivePrefix = {arXiv},\n       eprint = {1406.1497},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..443H},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1093/mnras/stu1449',NULL,NULL),(447,'Guillot',2013,'2013ApJ...772....7G','@ARTICLE{2013ApJ...772....7G,\n       author = {{Guillot}, Sebastien and {Servillat}, Mathieu and {Webb}, Natalie A. and {Rutledge}, Robert E.},\n        title = \"{Measurement of the Radius of Neutron Stars with High Signal-to-noise Quiescent Low-mass X-Ray Binaries in Globular Clusters}\",\n      journal = {\\apj},\n     keywords = {globular clusters: individual: M28 M13 NGC 5139 NGC 6304 NGC 6397, stars: neutron, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena, Astrophysics - Solar and Stellar Astrophysics},\n         year = 2013,\n        month = jul,\n       volume = {772},\n       number = {1},\n          eid = {7},\n        pages = {7},\n          doi = {10.1088/0004-637X/772/1/7},\narchivePrefix = {arXiv},\n       eprint = {1302.0023},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2013ApJ...772....7G},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1088/0004-637X/772/1/7',NULL,NULL),(448,'Bogdanov',2016,'2016ApJ...831..184B','@ARTICLE{2016ApJ...831..184B,\n       author = {{Bogdanov}, Slavko and {Heinke}, Craig O. and {{\\\"O}zel}, Feryal and {G{\\\"u}ver}, Tolga},\n        title = \"{Neutron Star Mass-Radius Constraints of the Quiescent Low-mass X-Ray Binaries X7 and X5 in the Globular Cluster 47 Tuc}\",\n      journal = {\\apj},\n     keywords = {dense matter, equation of state, globular clusters: individual: 47 Tucanae, stars: neutron, Astrophysics - High Energy Astrophysical Phenomena, Nuclear Theory},\n         year = 2016,\n        month = nov,\n       volume = {831},\n       number = {2},\n          eid = {184},\n        pages = {184},\n          doi = {10.3847/0004-637X/831/2/184},\narchivePrefix = {arXiv},\n       eprint = {1603.01630},\n primaryClass = {astro-ph.HE},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2016ApJ...831..184B},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.3847/0004-637X/831/2/184',NULL,NULL),(449,'Hessels',2006,'2006Sci...311.1901H','@ARTICLE{2006Sci...311.1901H,\n       author = {{Hessels}, Jason W.~T. and {Ransom}, Scott M. and {Stairs}, Ingrid H. and {Freire}, Paulo C.~C. and {Kaspi}, Victoria M. and {Camilo}, Fernando},\n        title = \"{A Radio Pulsar Spinning at 716 Hz}\",\n      journal = {Science},\n     keywords = {ASTRONOMY},\n         year = 2006,\n        month = mar,\n       volume = {311},\n       number = {5769},\n        pages = {1901-1904},\n          doi = {10.1126/science.1123430},\n       adsurl = {https://ui.adsabs.harvard.edu/abs/2006Sci...311.1901H},\n      adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}','10.1126/science.1123430',NULL,NULL);
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

-- Dump completed on 2023-08-04 15:08:03
