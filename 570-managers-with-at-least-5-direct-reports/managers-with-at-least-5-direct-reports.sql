# Write your MySQL query statement below
SELECT name
FROM(
    SELECT e.managerId
    FROM Employee e
    GROUP BY managerId
    HAVING COUNT(e.managerId) >= 5
    ) as m
INNER JOIN Employee e
ON m.managerId = e.id