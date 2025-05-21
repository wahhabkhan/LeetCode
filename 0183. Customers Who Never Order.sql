# Write your MySQL query statement below
select name AS Customers
from Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId
where Orders.customerID IS NULL;