# Write your MySQL query statement below
select wt2.id
from Weather wt1 inner join Weather wt2 
on wt1.recordDate = wt2.recordDate - interval 1 day
where wt1.temperature < wt2.temperature;