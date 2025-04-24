
INSERT INTO cargo VALUES 
(1,'Gerente','2024-01-12 21:07:19'),
(2,'Secretaria','2024-01-12 21:07:19'),
(3,'admin','2024-01-12 21:07:19');

INSERT INTO oficina VALUES 
(1,'piura','simbila','2024-01-12 21:14:59'),
(2,'lIMA','AV. BRAZIL - LIMA','2024-01-12 21:17:52');


INSERT INTO tipo_moneda VALUES (1,'SOLES','PEN','2024-01-12 21:17:32');

INSERT INTO vehiculo VALUES (1,'Hyanday','HUCG','CAC-890','2024-01-12 22:08:12');

INSERT INTO transportista VALUES (1,'1012313123','Juan Torres','Juan Lucas','Torres perez','GY090','2024-01-12 22:07:47');

INSERT INTO motivo_traslado VALUES 
(1,'Venta','2024-01-12 22:08:39'),
(2,'Ingreso de Producto','2024-01-12 22:08:49'),
(3,'Translado de Almacenes','2024-01-12 22:09:00');


INSERT INTO cliente VALUES 
(1,'Donato Stuck','RUC','1231214212312312','Huancayo -peru','2024-01-12 22:06:04'),
(2,'Juenter SAC','RUC','2013123123123','Lima - Perù','2024-01-12 22:06:30');


INSERT INTO persona VALUES 
(1,'76838078','Alonso','Cordova','Sanchez','S','M','910231321','alonso@gmail.com','piura - peru','2024-01-12 21:07:19'),
(2,'15161718','CARLOS','fernandex','humbo','S','M','912331231','carlos@gmail.com','Av. Lima 456 - piura','2024-01-12 21:33:22');

INSERT INTO usuario VALUES 
(1,3,1,1,'alonso','pbkdf2:sha256:260000$KiWqRjkYKM5ZjgpP$df90897b9fcd38f7ce13d0057cfaa6fed765735e6f3d2ac34c1e733dedf16fd6','2024-01-12 21:07:19','A'),
(2,2,1,2,'carlos','pbkdf2:sha256:260000$WIfoyhTcLpkytM9Z$dc1665119bc5216d9c6f2a10192ae16b3ccabde063ce581234b4079c2e98e562','2024-01-12 21:33:45','A');



INSERT INTO pregunta VALUES (1,1,'¿Nombre de tu mamá?','juana','2024-01-12 21:14:59');


INSERT INTO factura VALUES 
(1,'123',1,1,'2024-01-13 00:00:00','asdasd','A',100),
(2,'nuevo',1,1,'2024-01-08 00:00:00','asdasd','A',100),
(3,'122',1,1,'2024-01-11 00:00:00','roca','A',1000),
(4,'345',2,1,'2023-11-07 00:00:00','adasd','A',12),
(5,'342',1,1,'2023-12-12 00:00:00','','A',5000);


INSERT INTO guia_remision VALUES 
(1,'2024-01-13 00:00:00',1,2,1,1,1,1,'Lima'),
(2,'2024-01-09 00:00:00',1,2,2,1,1,2,'Piura');


INSERT INTO descripcion_guia VALUES 
(1,'Rocas Fosforica',5,50,250,1,'2024-01-13 07:32:10'),
(2,'Roca Fosforica',100,50,5000,2,'2024-01-13 08:15:51');









