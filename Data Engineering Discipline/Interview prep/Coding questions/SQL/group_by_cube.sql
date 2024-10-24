# https://www.db-fiddle.com/f/hp4rwFBHuM8d7VQ63RMxF2/0
# https://www.linkedin.com/feed/update/urn:li:activity:6772324656826478592?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6772324656826478592%2C6773005210102173696%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%286773005210102173696%2Curn%3Ali%3Aactivity%3A6772324656826478592%29

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