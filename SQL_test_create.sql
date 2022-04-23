--Create new databases
--Requires admin
CREATE DATABASE testdb;
CREATE DATABASE dummydb;

--Check which databases exist with command:
SHOW DATABASES;

--Drop a database
--Requires admin
DROP DATABASE dummydb;

--Create full backup
BACKUP DATABASE testdb
TO DISK = 'testdb.db';
--Or back up diffs only
BACKUP DATABASE testdb
TO DISK = 'testdb-diff.db'
WITH DIFFERENTIAL;

--Create a new table
CREATE TABLE Cats (
	CatID int,
	CatName varchar(255),
	HumanName varchar(255),
	Age int
);

--Or copy a table
CREATE TABLE Kittens AS
	SELECT CatID, CatName, HumanName
	FROM Cats
	WHERE Age < 1
;

--Drop a table
DROP TABLE Kittens;

--TRUNCATE deletes table data while maintaining the table (& its structure)
-- Won't do anything here as the Cats table has no data yet
TRUNCATE TABLE Cats;

--Modify a table with ALTER
ALTER TABLE Cats
ADD Address1 varchar(255);
--Can add or drop columns here
ALTER TABLE Kittens
DROP COLUMN HumanName;
--Or even alter column datatype (ALTER COLUMN or MODIFY COLUMN depending on SQL program)
ALTER TABLE Cats
MODIFY COLUMN Age datetime(0);

/* Columns can have additional data constraints
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables. One/multiple field(s) in a table (the parent/referenced table) that refer to the primary key in another table (the child table)
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly */

--Usage: 
ALTER TABLE Cats
MODIFY COLUMN CatID int PRIMARY KEY; --Primary key is both UNIQUE and NOT NULL
--(and there can only be one primary key, though it can consist of multiple fields)

--CHECK and DEFAULT can be used when creating tables or when altering them
ALTER TABLE Cats
ADD CHECK (Age >= 0);

CREATE TABLE Dogs (
	DogName varchar(255),
	Age int,
	RecordCreated date DEFAULT GETDATE() --Default value if nothing entered is the current date
);

--Create a unique index
CREATE UNIQUE INDEX DogID
ON Dogs (DogName);

--You can also drop contraints
ALTER TABLE Dogs
DROP INDEX DogName;

--Perhaps you'd prefer an auto-incrementing field that generates a unique number automatically when a new record is inserted. This is often the primary key
--It's 1-indexed by default, but you could say AUTO_INCREMENT=0 if you're too embedded in Python to count from 1
CREATE TABLE Hamsters (
	HamsterID int NOT NULL AUTO_INCREMENT,
	HamsterName varchar(255),
	HumanName varchar(255),
	Age int,
	PRIMARY KEY (HamsterID)
);

--Now we can add a new hamster without having to specify a HamsterID: that will be created automatically
INSERT INTO Hamsters (HamsterName, HumanName, Age)
VALUES ("Penny", "Aloysius Parker", 2);

/* There are many different formats for dates (of course...)
	DATE - format YYYY-MM-DD
	DATETIME - format: YYYY-MM-DD HH:MI:SS
	TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
	YEAR - format YYYY or YY

	You are better using DATE than DATETIME unless you really need the times */

--You can also create a view: a virtual table based on result sets
CREATE VIEW dashboard AS
SELECT CatName, HumanName FROM Cats
WHERE CatName NOT NULL;
--You then query the view as before
SELECT * FROM dashboard;
--You can also use `CREATE OR REPLACE VIEW` instead of `CREATE VIEW` if needed
--And `DROP VIEW`
DROP VIEW dashboard;

/* WARNING:
	SQL injection is placement of malicious code in SQL statements via web page inputs
	So use SQL parameters... not user text inputs /*