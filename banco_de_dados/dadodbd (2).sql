-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: movebr
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Dumping data for table `contratos_fechados`
--

LOCK TABLES `contratos_fechados` WRITE;
/*!40000 ALTER TABLE `contratos_fechados` DISABLE KEYS */;
INSERT INTO `contratos_fechados` VALUES (3,3,'460.840.498-93'),(6,6,'460.840.498-93'),(7,7,'460.840.498-93');
/*!40000 ALTER TABLE `contratos_fechados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `historico_pagamentos`
--

LOCK TABLES `historico_pagamentos` WRITE;
/*!40000 ALTER TABLE `historico_pagamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_pagamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tb_alunos`
--

LOCK TABLES `tb_alunos` WRITE;
/*!40000 ALTER TABLE `tb_alunos` DISABLE KEYS */;
INSERT INTO `tb_alunos` VALUES (3,'Ivo Conceição Neto','https://movebr.blob.core.windows.net/fotos-movebr/20241129_101711_1682967364748.jfif','Diabetes','Sesi','André Bido Neto','Geriel Stocco','Rua Sebastião Fernandes Nogueira 45','(23) 54325-3455','(34) 45354-2545','Fernanda@gmail.com','tarde','2',NULL,NULL),(6,'Fernando Stocco','https://movebr.blob.core.windows.net/fotos-movebr/20241129_102033_f7199b3f4ff0dba5c7638d37f57bf397.jpg','Diabetes','Sesi','Fernanda Stocco','Geriel Stocco','Rua Sebastião Fernandes Nogueira 45','(23) 54325-3455','(34) 45354-2545','Fernanda@gmail.com','manha','1',NULL,NULL),(7,'Vinicius Amancio Da Silva','https://movebr.blob.core.windows.net/fotos-movebr/20241129_102347_1690243381814.jfif','Bronquite','Eeba','Maria Jósé','Geriel Da Silva','Avenida João Soares De Arruda 1220','(16) 99789-0045','(16) 99743-0473','Amancio@gmail.com','noite','3',NULL,NULL);
/*!40000 ALTER TABLE `tb_alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tb_alunos_clientes`
--

LOCK TABLES `tb_alunos_clientes` WRITE;
/*!40000 ALTER TABLE `tb_alunos_clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_alunos_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tb_motoristas`
--

LOCK TABLES `tb_motoristas` WRITE;
/*!40000 ALTER TABLE `tb_motoristas` DISABLE KEYS */;
INSERT INTO `tb_motoristas` VALUES ('Roberto Da Silva','460.840.498-93',NULL,NULL,NULL,NULL,'(16) 99646-5815','Roberto@gmail.com','Roberto4321.');
/*!40000 ALTER TABLE `tb_motoristas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `verificacao_pagamento`
--

LOCK TABLES `verificacao_pagamento` WRITE;
/*!40000 ALTER TABLE `verificacao_pagamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `verificacao_pagamento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29 10:27:59
