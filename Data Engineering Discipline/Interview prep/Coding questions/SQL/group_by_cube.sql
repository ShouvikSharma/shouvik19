create table A (created_date date, city varchar, apps integer);
insert into A (created_date,city,apps)
values
('2024-01-01','Chicago',1),
('2024-01-01','Mumbai',1),
('2024-01-01','Chicago',2),
('2024-01-02','Chicago',1),
('2024-01-02','Mumbai',1),
('2024-01-02','Chicago',2);

#### gives the total combination by city for each and every date
select 
created_date,
isnull(city,
case when
grouping(city)=0
then 'UNKNOWN'
ELSE 
'ALL' END,
count(1)
from
A
group by
created_date,cube(city)