
# https://github.com/yennanliu/CS_basics/blob/master/leetcode_SQL/leetcodify-friends-recommendations.sql#L61C24-L75C94

-- Creating the Listens table
CREATE TABLE Listens (
    user_id INT,
    song_id INT,
    day DATE
);

-- Inserting data into the Listens table
INSERT INTO Listens (user_id, song_id, day) VALUES
(1, 10, '2021-03-15'),
(1, 11, '2021-03-15'),
(1, 12, '2021-03-15'),
(2, 10, '2021-03-15'),
(2, 11, '2021-03-15'),
(2, 12, '2021-03-15'),
(3, 10, '2021-03-15'),
(3, 11, '2021-03-15'),
(3, 12, '2021-03-15'),
(4, 10, '2021-03-15'),
(4, 11, '2021-03-15'),
(4, 13, '2021-03-15'),
(5, 10, '2021-03-16'),
(5, 11, '2021-03-16'),
(5, 12, '2021-03-16');

-- Creating the Friendship table
CREATE TABLE Friendship (
    user1_id INT,
    user2_id INT
);

-- Inserting data into the Friendship table
INSERT INTO Friendship (user1_id, user2_id) VALUES
(1, 2);

with cte as
(
select 
A.user_id as user_id, 
B.user_id as recommended_id,
count(distinct A.song_id)
from 
Listens A
inner join
Listens B
on
A.song_id = B.song_id
and 
A.day = B.day
and
A.user_id != B.user_id
group by 1,2
having count(distinct A.song_id) > 2
)
select
A.user_id,
A.recommended_id
from
cte A
left join
Friendship B
on
A.user_id = B.user1_id
and
A.recommended_id = B.user2_id
left join
Friendship C
on
A.user_id = C.user2_id
and
A.recommended_id = C.user1_id
where
B.user1_id is null
and
C.user1_id is null