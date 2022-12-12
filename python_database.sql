-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2022 at 06:31 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.0.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `ID` int(11) NOT NULL,
  `CATEGORY` varchar(50) NOT NULL,
  `ITMNAME` varchar(50) NOT NULL,
  `LOCATION` varchar(50) NOT NULL,
  `DATE` varchar(15) NOT NULL,
  `DESCRIPTION` varchar(100) NOT NULL,
  `FNAME` varchar(25) NOT NULL,
  `LNAME` varchar(25) NOT NULL,
  `EMAIL` varchar(25) NOT NULL,
  `CONTACT` varchar(25) NOT NULL,
  `CLNAME` varchar(50) NOT NULL,
  `CFNAME` varchar(50) NOT NULL,
  `CCONTACT` varchar(50) NOT NULL,
  `CEMAIL` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`ID`, `CATEGORY`, `ITMNAME`, `LOCATION`, `DATE`, `DESCRIPTION`, `FNAME`, `LNAME`, `EMAIL`, `CONTACT`, `CLNAME`, `CFNAME`, `CCONTACT`, `CEMAIL`) VALUES
(1, 'Type 1', 'c++ book', 'park', '12/9/22', '104 pages, color black ', 'Mark', 'Delacruz', 'mark@gmail.com', '09345354343', 'Monkey', 'Luffy', '5435345', 'monkey@gmail.com'),
(2, 'Type 2', 'realme', 'SM fairview', '12/9/22', 'Realme c5 with casing of color green', 'Michelle', 'Reyes', 'mich@yahoo.com', '09612523512', 'Montermoso', 'kevin', '0934343456', 'kevin@gmail.com'),
(11, 'Type 1', 'Aquaflask', 'manila ocean park', '12/9/22', '1 liter size, color green', 'Lovely', 'Lunoza', 'lovely@yahoo.com', '09656756755', 'Diocena', 'Andrew', '09345345634', 'and@gmail.com'),
(1115, 'Type 2', 'Hanabishi', 'Apartment', '12/9/22', 'stand-fand color blue', 'Noel', 'Brusko', 'noel@gmail.com', '09435345432', 'James', 'Diocena', '4546456', 'james@gmail.com'),
(1117, 'Type 1', 'Shoes', 'park', '12/9/22', 'Air jordan', 'Juan', 'Delacruz', 'juuan@gmail.com', '456456454', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `UserID` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`UserID`, `Username`, `Password`) VALUES
(1, 'Hays', 'ff'),
(2, 'GG', 'GG'),
(3, 'dd', 'dd'),
(4, 'dd', 'dd');

-- --------------------------------------------------------

--
-- Table structure for table `lost-item`
--

CREATE TABLE `lost-item` (
  `ID` int(11) NOT NULL,
  `Category` varchar(50) NOT NULL,
  `Item-Name` varchar(50) NOT NULL,
  `Loc-Lost_Item` varchar(50) NOT NULL,
  `Date` varchar(11) NOT NULL,
  `Item-Desc` varchar(100) NOT NULL,
  `F_Name` varchar(50) NOT NULL,
  `L_Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Contact_#` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lost-item`
--

INSERT INTO `lost-item` (`ID`, `Category`, `Item-Name`, `Loc-Lost_Item`, `Date`, `Item-Desc`, `F_Name`, `L_Name`, `Email`, `Contact_#`) VALUES
(11, '56', '56', '56', '56', '56', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `lost-item`
--
ALTER TABLE `lost-item`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1118;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `lost-item`
--
ALTER TABLE `lost-item`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=569;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
