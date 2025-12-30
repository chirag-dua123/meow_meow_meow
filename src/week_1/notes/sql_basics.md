SQL Basics — Short Notes, Examples, and Practice Queries

## Short notes (common commands + examples)

- SELECT: read rows from a table.
	- Example: `SELECT * FROM Users;`

- WHERE: filter rows.
	- Example: `SELECT name, age FROM Users WHERE age > 30;`

- DISTINCT: unique values.
	- Example: `SELECT DISTINCT country FROM Users;`

- ORDER BY: sort results.
	- Example: `SELECT * FROM Users ORDER BY age DESC;`

- LIMIT / TOP: limit rows returned.
	- Example (SQLite/MySQL/Postgres): `SELECT * FROM Users LIMIT 10;`

- INSERT: add new row(s).
	- Example: `INSERT INTO Users (name, age) VALUES ('Alice', 29);`

- UPDATE: modify existing rows.
	- Example: `UPDATE Users SET age = 30 WHERE id = 1;`

- DELETE: remove rows.
	- Example: `DELETE FROM Users WHERE id = 42;`

- CREATE TABLE: define a new table.
	- Example:
		`CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);`

- ALTER TABLE: change table schema.
	- Example: `ALTER TABLE Users ADD COLUMN email TEXT;`

- DROP TABLE: remove a table.
	- Example: `DROP TABLE IF EXISTS TempData;`

- JOIN: combine rows from two tables.
	- Example (inner join):
		`SELECT u.name, o.total FROM Users u JOIN Orders o ON u.id = o.user_id;`

- GROUP BY: aggregate rows.
	- Example: `SELECT user_id, COUNT(*) FROM Orders GROUP BY user_id;`

- HAVING: filter aggregated groups.
	- Example: `SELECT user_id, SUM(total) as s FROM Orders GROUP BY user_id HAVING s > 100;`

## One-line definition

- Primary key: a column (or set of columns) that uniquely identifies each row in a table.

## Example tables (for practice queries)

- `Users(id, name, age, country)`
- `Orders(id, user_id, total, created_at)`
- `Products(id, name, price)`

## 5 Practice queries

1. Select users older than 30, newest first:
	 `SELECT id, name, age FROM Users WHERE age > 30 ORDER BY age DESC;`

2. Insert a new product:
	 `INSERT INTO Products (id, name, price) VALUES (101, 'Socks', 9.99);`

3. Increase price for a product:
	 `UPDATE Products SET price = price * 1.10 WHERE id = 101;`

4. Remove an old order by id:
	 `DELETE FROM Orders WHERE id = 1234;`

5. Total spent per user (join + group):
	 `SELECT u.id, u.name, SUM(o.total) AS total_spent FROM Users u JOIN Orders o ON u.id = o.user_id GROUP BY u.id, u.name ORDER BY total_spent DESC;`

-- End of notes


Primary key is a set of minimum fields in a table that is able to uniquely identify each record.

