# Write your MySQL query statement below

select u.name, sum(case when r.distance is null then 0 else r.distance end) as travelled_distance
from Users u
left join Rides r 
on u.id = r.user_id
group by u.name, user_id
order by travelled_distance desc, u.name
