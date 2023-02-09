-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pabd_moveis
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `endereco` varchar(100) DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES ('0000','Kelly','Campo Grande','64953728','kelly@gmail.com'),('1111','Ian','Paris','84576539','ian@gmail.com'),('1122','Jailson','Rio Branco','18972845','jailson@gmail.com'),('1144','Rafael','Recife','15474513','rafael@gmail.com'),('2222','Kaua','Mossoró','18537890','kaua@gmail.com'),('3333','Leonardo','Pindamonhangaba','51356522','leo@gmail.com'),('4444','Ronilson','Natal','58714265','ronilson@gmail.com'),('5555','Jussara','Barcelona','89201476','jussara@gmail.com'),('6666','Rita','São Paulo do Potengi','78598742','rita@gmail.com'),('7777','Maria','Jucurutu','31642789','maria@gmail.com'),('8888','Roberto','Macau','01245789','roberto@gmail.com'),('9999','Lucas','Touros','34680247','lucas@gmail.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cpf_cliente` varchar(11) DEFAULT NULL,
  `codigo_produto` varchar(11) DEFAULT NULL,
  `cpf_funcionario` varchar(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `qntd_compra` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_compra_produto_idx` (`codigo_produto`),
  KEY `fk_compra_funcionario_idx` (`cpf_funcionario`),
  KEY `fk_compra_cliente` (`cpf_cliente`),
  CONSTRAINT `fk_compra_cliente` FOREIGN KEY (`cpf_cliente`) REFERENCES `cliente` (`cpf`),
  CONSTRAINT `fk_compra_funcionario` FOREIGN KEY (`cpf_funcionario`) REFERENCES `funcionario` (`cpf`),
  CONSTRAINT `fk_compra_produto` FOREIGN KEY (`codigo_produto`) REFERENCES `produto` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,'1111','22','444','2021-01-09',1),(2,'1111','55','666','2021-01-09',1),(3,'1111','99','666','2021-02-01',2),(4,'2222','77','111','2021-02-09',2),(5,'2222','11','111','2021-02-09',3),(6,'3333','00','333','2021-02-25',1),(7,'4444','99','888','2021-03-05',3),(8,'5555','66','666','2021-03-05',4),(9,'6666','11','111','2021-03-15',2),(10,'7777','33','111','2021-03-20',1),(11,'8888','44','333','2021-03-20',1),(12,'9999','44','888','2021-03-20',2),(13,'0000','77','888','2021-03-30',2),(14,'8888','88','444','2021-04-01',3),(15,'1111','88','666','2021-04-01',3),(16,'2222','66','333','2021-04-01',4),(18,'1111','11','111','2021-06-07',2),(19,'6666','77','333','2021-06-21',2),(22,'1122','33','666','2021-07-02',1),(23,'5555','33','333','2021-07-05',1),(24,'1122','33','333','2021-07-11',1),(25,'1122','33','333','2021-07-12',1);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedor`
--

DROP TABLE IF EXISTS `fornecedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedor` (
  `cnpj` varchar(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `departamentos` varchar(200) DEFAULT NULL,
  `endereço` varchar(200) DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedor`
--

LOCK TABLES `fornecedor` WRITE;
/*!40000 ALTER TABLE `fornecedor` DISABLE KEYS */;
INSERT INTO `fornecedor` VALUES ('11111','Nyne','Quarto e Cozinha','Natal','79871654','nyne@gmail.com'),('22222','Valdemóveis','Sala','Natal','16238405','valde@gmail.com'),('33333','Filips Eletros','Cozinha','Mossoró','94732855','filips@gmail.com'),('44444','Ortobom','Quarto','Caraubas','97315794','ortobom@gmail.com'),('55555','Sitkauskas','Sala','São Paulo','99877564','sitkauskas@gmail.com');
/*!40000 ALTER TABLE `fornecedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `funcao` varchar(100) DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES ('000','Rebecca','Caixa',1200,'13461952','rebecca@gmail.com'),('111','João','Vendedor',1600,'86935648','joao@gmail.com'),('222','Bruno','Caixa',1200,'78694758','bruno@gmail.com'),('333','José','Vendedor',1600,'84638375','jose@gmail.com'),('444','Felipe','Vendedor',1600,'34215798','felipe@gmail.com'),('555','Gabriel','Gerente',3000,'15654891','gabriel@gmail.com'),('666','Guilherme','Vendedor',1600,'35798565','guilherme@gmail.com'),('777','Pedro','Caixa',1200,'34619163','pedro@gmail.com'),('888','Kamilly','Vendedor',1600,'34619344','kamilly@gmail.com'),('999','Clarissi','Caixa',1200,'98723131','clarissi@gmail.com');
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `codigo` varchar(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `descricao` varchar(400) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `qntd_estoque` int DEFAULT NULL,
  `cnpj_fornecedor` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`codigo`,`nome`),
  KEY `fk_fornece_idx` (`cnpj_fornecedor`),
  CONSTRAINT `fk_fornece` FOREIGN KEY (`cnpj_fornecedor`) REFERENCES `fornecedor` (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES ('00','Painel Lexus','Sala','Painel em MDF e com suporte para TV de 70\'\'.',2000,30,'55555'),('11','Roupeiro Paris','Quarto','Roupeiro com 6 portas e MDF',2000,48,'11111'),('22','Armário Cozinha Grécia','Cozinha','Armário com 3 gavetas e MDF',2500,45,'11111'),('33','Rack Florença','Sala','Rack com rodinhas e MDP',1500,46,'22222'),('44','Painel Hades','Sala','Painel com suporte para TV de 60\" e MDP',600,25,'22222'),('55','Microondas Arizona','Cozinha','Microondas com 40 litros de capacidade, preto',900,35,'33333'),('66','Geladeira Ragnar','Cozinha','Geladeira com 400 litros de capacidade, Inox com duas portas',3800,40,'33333'),('77','Colchão Master II','Quarto','Colchão de casal com molas.',1500,48,'44444'),('88','Colchão King IV','Quarto','Colchão king size, reforço lateral e com molas ensacadas.',3500,30,'44444'),('99','Home Theater Sibéria','Sala','Home Theater em MDF, com plateleiras de vidro e suporte para TV de até 80\'\'.',2800,35,'55555');
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-09 17:07:42
