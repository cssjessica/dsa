# Write your MySQL query statement below
with t1 as (select actor_id, director_id, count(actor_id) as count_coop
from ActorDirector
group by actor_id, director_id)

select actor_id, director_id
from t1
where count_coop >= 3
