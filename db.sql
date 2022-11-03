-- Adminer 4.8.1 MySQL 8.0.30-0ubuntu0.20.04.2 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `video_app_db`;
CREATE DATABASE `video_app_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `video_app_db`;

DROP TABLE IF EXISTS `video_app`;
CREATE TABLE `video_app` (
  `username` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;

INSERT INTO `video_app` (`username`, `password`) VALUES
('John',	'1234'),
('lll',	'llll'),
('test',	'1234'),
('test2',	'1234'),
('test3',	'1234'),
('Test',	'1234'),
('damu',	'damu'),
('naseef',	'naseef');

-- 2022-11-03 17:59:53
