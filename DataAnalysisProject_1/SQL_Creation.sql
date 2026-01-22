CREATE TABLE Customers (
CustomerID INT PRIMARY KEY ,
Name nvarchar(100) ,
Gender char(6) , 
BirthDate DATE , 
Phone nvarchar(20) , 
Email nvarchar(100) , 
City nvarchar(50)
); 


create table Branches (
 BranchID int primary key , 
 BranchName nvarchar(100) , 
 City nvarchar(50) , 
 Address nvarchar(200) , 

);

create table Products (
ProductID int primary key , 
ProductName nvarchar(100) , 
Category nvarchar(50) , 
Price DECIMAL(10, 2),
Supplier NVARCHAR(100)

);


create table Sales(
SaleID INT PRIMARY KEY,
    CustomerID INT,
    BranchID INT,
    SaleDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (BranchID) REFERENCES Branches(BranchID)
); 

CREATE TABLE SaleDetails (
    SaleID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    TotalPrice DECIMAL(10, 2),
    PRIMARY KEY (SaleID, ProductID),
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);