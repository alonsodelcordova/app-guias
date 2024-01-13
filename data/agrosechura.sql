CREATE DATABASE agrosechura;

use agrosechura;

-- Table structure for table `cargo`
CREATE TABLE `cargo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cargo` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_cargo` (`nombre_cargo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `cargo` VALUES 
(1,'Gerente','2024-01-12 21:07:19'),
(2,'Secretaria','2024-01-12 21:07:19'),
(3,'admin','2024-01-12 21:07:19');


-- Table structure for table `oficina`
CREATE TABLE `oficina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_oficina` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_oficina` (`nombre_oficina`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `oficina` VALUES 
(1,'piura','simbila','2024-01-12 21:14:59'),
(2,'lIMA','AV. BRAZIL - LIMA','2024-01-12 21:17:52');


-- Table structure for table `tipo_moneda`
CREATE TABLE `tipo_moneda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_moneda` varchar(20) NOT NULL,
  `prefijo` varchar(3) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_moneda` (`nombre_moneda`),
  UNIQUE KEY `prefijo` (`prefijo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `tipo_moneda` VALUES (1,'SOLES','PEN','2024-01-12 21:17:32');


-- Table structure for table `vehiculo`
CREATE TABLE `vehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marca_vehiculo` varchar(30) NOT NULL,
  `modelo_vehiculo` varchar(15) NOT NULL,
  `placa_vehiculo` varchar(15) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `placa_vehiculo` (`placa_vehiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `vehiculo` VALUES (1,'Hyanday','HUCG','CAC-890','2024-01-12 22:08:12');


-- Table structure for table `transportista`
CREATE TABLE `transportista` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ruc` varchar(20) NOT NULL,
  `denominacion` varchar(50) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `numero_licencia` varchar(20) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_licencia` (`numero_licencia`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `transportista` VALUES (1,'1012313123','Juan Torres','Juan Lucas','Torres perez','GY090','2024-01-12 22:07:47');



-- Table structure for table `motivo_traslado`
CREATE TABLE `motivo_traslado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_motivo` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_motivo` (`nombre_motivo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `motivo_traslado` VALUES 
(1,'Venta','2024-01-12 22:08:39'),
(2,'Ingreso de Producto','2024-01-12 22:08:49'),
(3,'Translado de Almacenes','2024-01-12 22:09:00');


-- Table structure for table `cliente`
CREATE TABLE `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `razon_social` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(20) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_documento` (`numero_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `cliente` VALUES 
(1,'Donato Stuck','RUC','1231214212312312','Huancayo -peru','2024-01-12 22:06:04'),
(2,'Juenter SAC','RUC','2013123123123','Lima - Perù','2024-01-12 22:06:30');




-- Table structure for table `persona`
CREATE TABLE `persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(8) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `primer_apellido` varchar(50) NOT NULL,
  `segundo_apellido` varchar(50) NOT NULL,
  `estado_civil` varchar(1) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `numero_celular` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `persona` VALUES 
(1,'76838078','Alonso','Cordova','Sanchez','S','M','910231321','alonso@gmail.com','piura - peru','2024-01-12 21:07:19'),
(2,'15161718','CARLOS','fernandex','humbo','S','M','912331231','carlos@gmail.com','Av. Lima 456 - piura','2024-01-12 21:33:22');




-- Table structure for table `usuario`
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cargo` int(11) NOT NULL,
  `id_oficina` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `password` varchar(256) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `id_cargo` (`id_cargo`),
  KEY `id_oficina` (`id_oficina`),
  KEY `id_persona` (`id_persona`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`id_oficina`) REFERENCES `oficina` (`id`),
  CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `usuario` VALUES 
(1,3,1,1,'alonso','pbkdf2:sha256:260000$KiWqRjkYKM5ZjgpP$df90897b9fcd38f7ce13d0057cfaa6fed765735e6f3d2ac34c1e733dedf16fd6','2024-01-12 21:07:19','A'),
(2,2,1,2,'carlos','pbkdf2:sha256:260000$WIfoyhTcLpkytM9Z$dc1665119bc5216d9c6f2a10192ae16b3ccabde063ce581234b4079c2e98e562','2024-01-12 21:33:45','A');




-- Table structure for table `pregunta`
CREATE TABLE `pregunta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) NOT NULL,
  `pregunta` varchar(100) NOT NULL,
  `respuesta` varchar(100) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `pregunta_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `pregunta` VALUES (1,1,'¿Nombre de tu mamá?','juana','2024-01-12 21:14:59');



-- Table structure for table `factura`
CREATE TABLE `factura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_factura` varchar(10) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_tipo_moneda` int(11) NOT NULL,
  `fecha_emision` datetime DEFAULT NULL,
  `observacion` text NOT NULL,
  `estado` varchar(1) NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_factura` (`numero_factura`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_tipo_moneda` (`id_tipo_moneda`),
  CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`),
  CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`id_tipo_moneda`) REFERENCES `tipo_moneda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `factura` VALUES 
(1,'123',1,1,'2024-01-13 00:00:00','asdasd','A',100),
(2,'nuevo',1,1,'2024-01-08 00:00:00','asdasd','A',100),
(3,'122',1,1,'2024-01-11 00:00:00','roca','A',1000),
(4,'345',2,1,'2023-11-07 00:00:00','adasd','A',12),
(5,'342',1,1,'2023-12-12 00:00:00','','A',5000);



--
-- Table structure for table `guia_remision`
--

CREATE TABLE `guia_remision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_inicio` datetime DEFAULT NULL,
  `id_oficina` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_factura` int(11) NOT NULL,
  `id_transportista` int(11) NOT NULL,
  `id_vehiculo` int(11) NOT NULL,
  `id_motivo_traslado` int(11) NOT NULL,
  `punto_destino` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_oficina` (`id_oficina`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_factura` (`id_factura`),
  KEY `id_transportista` (`id_transportista`),
  KEY `id_vehiculo` (`id_vehiculo`),
  KEY `id_motivo_traslado` (`id_motivo_traslado`),
  CONSTRAINT `guia_remision_ibfk_1` FOREIGN KEY (`id_oficina`) REFERENCES `oficina` (`id`),
  CONSTRAINT `guia_remision_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`),
  CONSTRAINT `guia_remision_ibfk_3` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id`),
  CONSTRAINT `guia_remision_ibfk_4` FOREIGN KEY (`id_transportista`) REFERENCES `transportista` (`id`),
  CONSTRAINT `guia_remision_ibfk_5` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculo` (`id`),
  CONSTRAINT `guia_remision_ibfk_6` FOREIGN KEY (`id_motivo_traslado`) REFERENCES `motivo_traslado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `guia_remision` VALUES 
(1,'2024-01-13 00:00:00',1,2,1,1,1,1,'Lima'),
(2,'2024-01-09 00:00:00',1,2,2,1,1,2,'Piura');



--
-- Table structure for table `descripcion_guia`
--

CREATE TABLE `descripcion_guia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(300) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `unidad_medida` float NOT NULL,
  `peso` float NOT NULL,
  `id_guia_remision` int(11) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_guia_remision` (`id_guia_remision`),
  CONSTRAINT `descripcion_guia_ibfk_1` FOREIGN KEY (`id_guia_remision`) REFERENCES `guia_remision` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `descripcion_guia` VALUES 
(1,'Rocas Fosforica',5,50,250,1,'2024-01-13 07:32:10'),
(2,'Roca Fosforica',100,50,5000,2,'2024-01-13 08:15:51');









