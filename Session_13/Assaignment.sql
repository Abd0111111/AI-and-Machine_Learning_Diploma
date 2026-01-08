-- SQL Assignment Solutions

-- 1. Customers with more than one order
SELECT
    C.Name,
    COUNT(O.OrderID) AS TotalOrders
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.Name
HAVING COUNT(O.OrderID) > 1;

-- 2. Top 3 customers by total spending
SELECT TOP 3
    C.Name,
    SUM(O.TotalAmount) AS TotalSpent
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.Name
ORDER BY TotalSpent DESC;

-- 3. Products ordered by customers from Cairo only (no duplicates)
SELECT DISTINCT
    P.ProductName
FROM Products P
JOIN OrderDetails OD ON P.ProductID = OD.ProductID
JOIN Orders O ON OD.OrderID = O.OrderID
JOIN Customers C ON O.CustomerID = C.CustomerID
WHERE C.Region = 'Cairo';

-- 4. Average order value
SELECT AVG(TotalAmount) AS AverageOrderValue
FROM Orders;

-- 5. Customers who never purchased electronics
SELECT
    C.Name
FROM Customers C
WHERE C.CustomerID NOT IN (
    SELECT DISTINCT O.CustomerID
    FROM Orders O
    JOIN OrderDetails OD ON O.OrderID = OD.OrderID
    JOIN Products P ON OD.ProductID = P.ProductID
    WHERE P.Category = 'Electronics'
);

-- 6. Most expensive product purchased in each order
WITH RankedProducts AS (
    SELECT
        OD.OrderID,
        P.ProductName,
        P.Price,
        ROW_NUMBER() OVER(PARTITION BY OD.OrderID ORDER BY P.Price DESC) AS rn
    FROM OrderDetails OD
    JOIN Products P ON OD.ProductID = P.ProductID
)
SELECT
    OrderID,
    ProductName,
    Price
FROM RankedProducts
WHERE rn = 1;

-- 7. Percentage contribution of each product to total revenue
WITH ProductRevenue AS (
    SELECT
        P.ProductName,
        SUM(OD.Quantity * P.Price) AS Revenue
    FROM Products P
    JOIN OrderDetails OD ON P.ProductID = OD.ProductID
    GROUP BY P.ProductName
),
TotalRevenue AS (
    SELECT SUM(Revenue) AS TotalRev FROM ProductRevenue
)
SELECT
    PR.ProductName,
    PR.Revenue,
    (PR.Revenue / TR.TotalRev) * 100 AS PercentageContribution
FROM ProductRevenue PR
CROSS JOIN TotalRevenue TR
ORDER BY PercentageContribution DESC;

-- 8. Customers whose total spending is above overall average
WITH CustomerSpending AS (
    SELECT
        C.CustomerID,
        C.Name,
        SUM(O.TotalAmount) AS TotalSpent
    FROM Customers C
    JOIN Orders O ON C.CustomerID = O.CustomerID
    GROUP BY C.CustomerID, C.Name
),
AverageSpending AS (
    SELECT AVG(TotalSpent) AS AvgSpent FROM CustomerSpending
)
SELECT
    CS.Name,
    CS.TotalSpent
FROM CustomerSpending CS
CROSS JOIN AverageSpending AS ASAvg
WHERE CS.TotalSpent > ASAvg.AvgSpent;

-- 9. Products purchased only once across all orders
SELECT
    P.ProductName
FROM Products P
JOIN OrderDetails OD ON P.ProductID = OD.ProductID
GROUP BY P.ProductID, P.ProductName
HAVING SUM(OD.Quantity) = 1;

-- 10. Customer-level feature table
SELECT
    C.Name AS CustomerName,
    COUNT(O.OrderID) AS TotalOrders,
    SUM(O.TotalAmount) AS TotalSpending,
    AVG(O.TotalAmount) AS AverageOrderValue
FROM Customers C
LEFT JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.Name;