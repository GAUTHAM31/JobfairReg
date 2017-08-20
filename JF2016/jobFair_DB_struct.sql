-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 20, 2017 at 07:30 PM
-- Server version: 10.1.23-MariaDB-9+deb9u1
-- PHP Version: 7.0.19-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jobFair_DB`
--

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `short_name` varchar(50) NOT NULL,
  `available` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `participant`
--

CREATE TABLE `participant` (
  `timestamp` timestamp(6) NULL DEFAULT CURRENT_TIMESTAMP(6),
  `jobfairid` varchar(30) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `college` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `specialization` varchar(50) NOT NULL,
  `year` varchar(50) NOT NULL,
  `x-percentage` varchar(25) DEFAULT NULL,
  `x-board` varchar(25) DEFAULT NULL,
  `xii-percentage` varchar(25) DEFAULT NULL,
  `xii-board` varchar(25) DEFAULT NULL,
  `degree-percentage` varchar(50) DEFAULT NULL,
  `backlog` varchar(10) DEFAULT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `company1` varchar(25) DEFAULT NULL,
  `company2` varchar(25) DEFAULT NULL,
  `company3` varchar(25) DEFAULT NULL,
  `company4` varchar(25) DEFAULT NULL,
  `company5` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `participant`
--
ALTER TABLE `participant`
  ADD PRIMARY KEY (`email`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
