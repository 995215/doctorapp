CREATE Database doctor_app;

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `appoinmentid` int NOT NULL AUTO_INCREMENT,
  `appointmentname` varchar(45) NOT NULL,
  `appointmentdate` varchar(45) NOT NULL,
  `appointmentdoctorname` varchar(45) NOT NULL,
  `appointmentemail` varchar(45) NOT NULL,
  `appointmenttext` varchar(45) NOT NULL,
  PRIMARY KEY (`appoinmentid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,'alagesh','22/02/2022','ravi','ala23@gmail.com','checkup'),(2,'siva','25/02/2022','prasanna','siva@gmail.com','checkup'),(3,'siva','22/05/2022','arun','siva12@gmail.com','checkup'),(4,'test','2022-02-10','1','easwarancg65@gmail.com','test'),(5,'test','2022-02-02','sasi','easwarancg65@gmail.com','test'),(6,'priya','2022-02-10','prasanna','easwarancg65@gmail.com','checkup'),(7,'siva','22/05/2022','raja','siva12@gmail.com','checkup'),(8,'ravi','2022-02-10','kumar','easwarancg65@gmail.com','test'),(9,'divya','2022-02-10','ram','easwarancg65@gmail.com','test'),(10,'siva','22/05/2022','arun','siva12@gmail.com','checkup');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `doctorid` int NOT NULL AUTO_INCREMENT,
  `doctorname` varchar(45) NOT NULL,
  `doctordegree` varchar(45) NOT NULL,
  `doctorspecification` varchar(45) NOT NULL,
  `doctorstarttime` varchar(45) NOT NULL,
  `doctorendtime` varchar(45) NOT NULL,
  PRIMARY KEY (`doctorid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'prasanna','mbbs','hreat','10:30am','2:00pm'),(2,'ravi','bds','dental','11:00am','1:00pm'),(3,'kumar','bhms','hemeopathy','9:00am','12:00pm'),(4,'sasi','bams','ayurvedia','10:00am','12:30pm'),(5,'ram','bds','dental','2:00am','5:00pm');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `home_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_user` (
  `doctorid` int NOT NULL AUTO_INCREMENT,
  `doctorname` varchar(45) NOT NULL,
  `doctornumber` varchar(20) NOT NULL,
  `doctorappointment` varchar(45) NOT NULL,
  PRIMARY KEY (`doctorid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_user`
--

LOCK TABLES `home_user` WRITE;
/*!40000 ALTER TABLE `home_user` DISABLE KEYS */;
INSERT INTO `home_user` VALUES (1,'ram','889977553366','22/02/2022'),(2,'ravi','6789017656','24/02/2022');
/*!40000 ALTER TABLE `home_user` ENABLE KEYS */;
UNLOCK TABLES;

