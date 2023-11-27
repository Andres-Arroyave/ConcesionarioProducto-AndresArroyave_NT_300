-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-11-2023 a las 02:01:10
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbconcesionario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alquileres`
--

CREATE TABLE `alquileres` (
  `Id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `placa` varchar(20) NOT NULL,
  `fecha_alquiler` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `fecha_devolucion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alquileres`
--

INSERT INTO `alquileres` (`Id`, `usuario_id`, `placa`, `fecha_alquiler`, `fecha_devolucion`) VALUES
(1, 3, 'ABZ145', '2023-10-27 18:00:07', '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autos`
--

CREATE TABLE `autos` (
  `placa` varchar(20) NOT NULL,
  `Referencia` varchar(225) NOT NULL,
  `Marca` varchar(225) NOT NULL,
  `Estado` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `autos`
--

INSERT INTO `autos` (`placa`, `Referencia`, `Marca`, `Estado`) VALUES
('ABZ145', 'Onix', 'Chevloret', 'prestado'),
('KLM455', 'Corvette', 'Chevrolet', 'disponible'),
('ONJ674', 'Clio', 'Renault', 'disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Id` int(11) NOT NULL,
  `Username` varchar(225) NOT NULL,
  `Password` varchar(225) NOT NULL,
  `Rol` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id`, `Username`, `Password`, `Rol`) VALUES
(1, 'Andres', '1', 'asesor'),
(2, 'Cristian', '222', 'usuario'),
(3, 'Juan', '333', 'usuario'),
(4, 'Alexander', '2', 'asesor'),
(5, 'Pablo', '3', 'asesor');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alquileres`
--
ALTER TABLE `alquileres`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_Prestamos_Usuarios` (`usuario_id`),
  ADD KEY `FK_Prestamos_Autos` (`placa`);

--
-- Indices de la tabla `autos`
--
ALTER TABLE `autos`
  ADD PRIMARY KEY (`placa`) USING BTREE;

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alquileres`
--
ALTER TABLE `alquileres`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alquileres`
--
ALTER TABLE `alquileres`
  ADD CONSTRAINT `FK_Prestamos_Autos` FOREIGN KEY (`placa`) REFERENCES `autos` (`placa`),
  ADD CONSTRAINT `FK_Prestamos_Usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
