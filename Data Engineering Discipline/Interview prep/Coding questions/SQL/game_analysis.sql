# https://leetcode.com/problems/game-play-analysis-iv/description/

with cte as
(
select 
player_id,
event_date,
ROW_NUMBER() over (partition by player_id order by event_date) as "row_num"
from 
Activity
)
select 

round(
count(distinct case when B.player_id is not null then A.player_id end)
/
count(distinct A.player_id),2) as "fraction"
from
cte A 
left join
cte B
on 
A.player_id = B.player_id
and
A.event_date = DATE_ADD(B.event_date, INTERVAL -1 DAY)
and 
A.row_num = 1 

