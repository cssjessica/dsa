# Write your MySQL query statement below
select name as Employee
from Employee as emp1
where managerId is not null and salary > (select salary from Employee as emp2 where id = emp1.managerId);
