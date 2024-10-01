
#####    https://leetcode.com/problems/sales-person/

# Write your MySQL query statement below
with cte as
(
select 
O.sales_id
from
Orders O
inner join
Company C
on O.com_id = C.com_id

where
C.name = 'Red'
)
select
S.name
from
SalesPerson S
left join
cte C
on
S.sales_id = C.sales_id
where
C.sales_id is null
group by 1