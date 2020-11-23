-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 23-11-2020 a las 20:15:43
-- Versión del servidor: 8.0.22
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `cit_id` int NOT NULL COMMENT 'identificador de la cita',
  `con_id` int NOT NULL COMMENT 'identificador del contacto',
  `cit_lugar` text NOT NULL COMMENT 'lugar de la cita',
  `cit_fecha` date NOT NULL COMMENT 'fecha de la cita',
  `cit_hora` time NOT NULL COMMENT 'hora de la cita',
  `cit_descripcion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tabla de las citas con los contactos';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactos`
--

CREATE TABLE `contactos` (
  `con_id` int NOT NULL COMMENT 'identificador del contacto',
  `con_nombre` varchar(50) NOT NULL COMMENT 'nombre del contacto',
  `con_apellido` varchar(50) NOT NULL COMMENT 'apellido del contacto',
  `con_direccion` varchar(250) NOT NULL COMMENT 'dirección del contacto',
  `con_telefono` varchar(20) NOT NULL COMMENT 'teléfono del contacto',
  `con_email` varchar(25) NOT NULL COMMENT 'correo electrónico del contacto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tabla de los contactos de la agenda';

--
-- Volcado de datos para la tabla `contactos`
--

INSERT INTO `contactos` (`con_id`, `con_nombre`, `con_apellido`, `con_direccion`, `con_telefono`, `con_email`) VALUES
(1, 'Juan Miguel', 'Diaz Perez', 'Calle 3ra 20-50 ', '3124565656', 'jmiguel@mail.com'),
(2, 'Ana Juliana', 'Hernandez Riaño', 'Autonorte 170-34', '3115434343', 'ajuliana@mail.com'),
(3, 'Pedro ', 'Parrado', 'trans 34 56-97', '3117898989', 'pparrado@mail.com'),
(4, 'José', 'Higuera', 'Trans 12 67-98', '3145678900', 'jhiguera@mail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`cit_id`),
  ADD KEY `fk_citas_contactos` (`con_id`);

--
-- Indices de la tabla `contactos`
--
ALTER TABLE `contactos`
  ADD PRIMARY KEY (`con_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `cit_id` int NOT NULL AUTO_INCREMENT COMMENT 'identificador de la cita', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `contactos`
--
ALTER TABLE `contactos`
  MODIFY `con_id` int NOT NULL AUTO_INCREMENT COMMENT 'identificador del contacto', AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `fk_citas_contactos` FOREIGN KEY (`con_id`) REFERENCES `contactos` (`con_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
