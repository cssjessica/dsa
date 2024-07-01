# Write your MySQL query statement below
select name
from SalesPerson 
where name not in (select sal.name
from SalesPerson sal
left join Orders o
on o.sales_id = sal.sales_id
left join Company com
on o.com_id = com.com_id
where com.name like 'RED')
