$$$ https://github.com/doocs/leetcode/blob/main/solution/0500-0599/0569.Median%20Employee%20Salary/README_EN.md

with cte as
(
select
id,
company,
salary,
row_number() over (partition by company order by salary) as row_number,
count(id) over (partition by company) as n
from
Employee
)

select
id,company,salary
from
cte
where
row_number >= (n/2)
and
row_number <= (n/2+1)