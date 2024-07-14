# Write your MySQL query statement below
select emp.employee_id, emp.name, count(man.employee_id) as reports_count, round(avg(man.age), 0) as average_age
from Employees emp
join Employees man
on emp.employee_id = man.reports_to
group by emp.employee_id, emp.name
order by emp.employee_id, emp.name
