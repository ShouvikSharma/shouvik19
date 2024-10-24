### important points to note

# Write your MySQL query statement below
with cte as
(
select
id,
salary,
dense_rank() over (order by salary desc) as row_num
from
Employee
)
select
max(salary) as SecondHighestSalary
from
cte
where
row_num = 2 

### for getting the null value its important to apply an aggregation on the salary field, eventhough its not necessary.
### another way of solving it would be using an inner query.

select
max(salary)
from
Employee
where
salary <
(
select max(salary)
from
Employee
)