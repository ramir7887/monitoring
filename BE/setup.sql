create database monitoring;

use monitoring;

CREATE TABLE `monitoring`.`work_machine` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `` INT NULL,
  `time_request` DATETIME NULL, 
  `time_event` DATETIME NULL,
  `name_machine` VARCHAR(45) NULL,
  `name_parametr` VARCHAR(45) NULL,
  `parametr_name_in_attr` VARCHAR(45) NULL,
  `parametr_value` VARCHAR(45) NULL,
  `dop_info` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`));
  
  
  CREATE TABLE `monitoring`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `pass` VARCHAR(512) NOT NULL,
  `token` VARCHAR(250) NULL,
  `tokendate` DATETIME NULL,
  PRIMARY KEY (`iduser`));
