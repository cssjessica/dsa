# Write your MySQL query statement below
-- select customer_id
-- from Customer 
-- group by customer_id
-- having count(distinct product_key) = (select count(distinct product_key) from Product)

with t1 as (select distinct customer_id, product_key from Customer)

select customer_id
from t1
group by customer_id
having count(product_key) = (select count(distinct product_key) from Product)
