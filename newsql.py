
import sqlite3 as 


CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Smith', 'John', '123 Main St', 'Anytown');

SELECT * FROM Persons;
