# Write your MySQL query statement below

-- get the time period for each process
with t1 as (select machine_id, round(max(timestamp) - min(timestamp), 3) as total_time
from Activity
group by machine_id, process_id)

-- get the average time from table with the time period
select machine_id, round(avg(total_time), 3) as processing_time
from t1
group by machine_id
