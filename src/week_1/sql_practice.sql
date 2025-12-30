select * from user where age > 25;
select user.name, sum(orders.spend) from user join orders on user.id = orders.user_id group by user.id;
SELECT users.id,
       users.name,
       COALESCE(SUM(orders.total), 0) AS total_spend
FROM Users
LEFT JOIN Orders ON orders.user_id = users.id
GROUP BY users.id, users.name
ORDER BY total_spend DESC
LIMIT 1;