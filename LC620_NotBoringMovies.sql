# Write your MySQL query statement below
select id, movie, description, rating
from Cinema
where id mod 2 <> 0 and description not like "boring"
order by rating desc;
