# SQL Syntax Reference

## Contents

1. SQL Statement Types
2. Data Types
3. CREATE DATABASE / TABLE
4. ALTER TABLE
5. DROP / TRUNCATE / RENAME
6. INSERT
7. SELECT
8. UPDATE
9. DELETE
10. JOINS
11. WHERE and Logical Operators
12. GROUP BY and HAVING
13. ORDER BY
14. SUBQUERIES
15. UNION
16. FUNCTIONS
17. TRANSACTIONS
18. INDEXES, VIEWS, and METADATA
19. MySQL Notes

---

## 1. SQL Statement Types

- DDL (Data Definition Language)
  - CREATE, ALTER, DROP, TRUNCATE, RENAME
- DML (Data Manipulation Language)
  - SELECT, INSERT, UPDATE, DELETE
- DCL (Data Control Language)
  - GRANT, REVOKE
- TCL (Transaction Control Language)
  - COMMIT, ROLLBACK, SAVEPOINT

---

## 2. Data Types

Common MySQL types:
- Numeric: `INT`, `SMALLINT`, `BIGINT`, `DECIMAL(p,s)`, `FLOAT`, `DOUBLE`
- String: `VARCHAR(n)`, `CHAR(n)`, `TEXT`, `TINYTEXT`, `MEDIUMTEXT`, `LONGTEXT`
- Date/Time: `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR`
- Binary: `BLOB`, `TINYBLOB`, `MEDIUMBLOB`, `LONGBLOB`
- Boolean: `BOOLEAN` (`TINYINT(1)`)

Column constraints:
- `NOT NULL`
- `NULL`
- `PRIMARY KEY`
- `UNIQUE`
- `DEFAULT value`
- `AUTO_INCREMENT`
- `CHECK(condition)`
- `FOREIGN KEY (column) REFERENCES parent_table(parent_column)`

---

## 3. CREATE DATABASE / TABLE

Create a database:
```
CREATE DATABASE sample_db;
CREATE DATABASE IF NOT EXISTS sample_db;
```

Create a table:
```
CREATE TABLE table_name (
  column1 datatype [constraint],
  column2 datatype [constraint],
  ...
);
```

Full example:
```
CREATE TABLE employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE,
  department_id INT,
  hire_date DATE DEFAULT CURRENT_DATE,
  salary DECIMAL(10,2) CHECK (salary >= 0),
  status VARCHAR(20) DEFAULT 'active',
  CONSTRAINT fk_dept FOREIGN KEY (department_id)
    REFERENCES departments(id)
);
```

Create table if not exists:
```
CREATE TABLE IF NOT EXISTS products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(200) NOT NULL
);
```

---

## 4. ALTER TABLE

Add column:
```
ALTER TABLE table_name
  ADD COLUMN column_name datatype [constraint];
```

Drop column:
```
ALTER TABLE table_name
  DROP COLUMN column_name;
```

Modify column type:
```
ALTER TABLE table_name
  MODIFY COLUMN column_name new_datatype;
```

Rename column:
```
ALTER TABLE table_name
  RENAME COLUMN old_name TO new_name;
```

Add a foreign key:
```
ALTER TABLE table_name
  ADD CONSTRAINT fk_name
  FOREIGN KEY (column_name)
  REFERENCES other_table(other_column);
```

---

## 5. DROP / TRUNCATE / RENAME

Drop a table:
```
DROP TABLE table_name;
DROP TABLE IF EXISTS table_name;
```

Remove all rows faster than `DELETE`:
```
TRUNCATE TABLE table_name;
```

Rename a table:
```
RENAME TABLE old_name TO new_name;
```

---

## 6. INSERT

Single row insert:
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

Multiple rows:
```
INSERT INTO employees (name, hire_date, salary)
VALUES
  ('Alice', '2025-01-15', 65000.00),
  ('Bob', '2025-02-01', 55000.00);
```

Insert from another query:
```
INSERT INTO archive_employees (id, name, salary)
SELECT id, name, salary
FROM employees
WHERE status = 'inactive';
```

MySQL upsert:
```
INSERT INTO products (id, name, price)
VALUES (1, 'Mouse', 19.99)
ON DUPLICATE KEY UPDATE price = VALUES(price);
```

---

## 7. SELECT

Basic select:
```
SELECT column1, column2
FROM table_name;
```

Select distinct values:
```
SELECT DISTINCT department_id
FROM employees;
```

With filtering and ordering:
```
SELECT id, name, salary
FROM employees
WHERE salary > 50000
ORDER BY salary DESC
LIMIT 10;
```

With offset:
```
SELECT *
FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;
```

---

## 8. UPDATE

```
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

Example:
```
UPDATE employees
SET salary = salary * 1.05,
    status = 'active'
WHERE hire_date < '2024-01-01';
```

---

## 9. DELETE

```
DELETE FROM table_name
WHERE condition;
```

Delete all rows:
```
DELETE FROM table_name;
```

Use caution: without `WHERE`, all rows are removed.

---

## 10. JOINS

Inner join:
```
SELECT e.id, e.name, d.name AS department
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

Left join:
```
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

Right join:
```
SELECT e.name, d.name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

Full outer join (MySQL uses UNION of LEFT and RIGHT):
```
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id
UNION
SELECT e.name, d.name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

Cross join:
```
SELECT e.name, d.name
FROM employees e
CROSS JOIN departments d;
```

Self join:
```
SELECT m.name AS manager, e.name AS employee
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

Natural join:
```
SELECT *
FROM tableA
NATURAL JOIN tableB;
```

---

## 11. WHERE and Logical Operators

```
SELECT *
FROM table_name
WHERE condition1
  AND condition2
  OR condition3
  AND NOT condition4;
```

Common operators:
- `=` equal
- `<>`, `!=` not equal
- `<`, `>`, `<=`, `>=`
- `BETWEEN value1 AND value2`
- `IN (value1, value2, ...)`
- `NOT IN (value1, value2, ...)`
- `LIKE 'pattern'`
- `IS NULL`, `IS NOT NULL`
- `EXISTS (subquery)`

Wildcards:
- `%` any number of characters
- `_` single character

Example:
```
SELECT *
FROM employees
WHERE name LIKE 'A%'
  AND department_id IN (1, 2, 3);
```

---

## 12. GROUP BY and HAVING

```
SELECT department_id, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;
```

Use `HAVING` to filter aggregated groups.

---

## 13. ORDER BY

```
SELECT *
FROM employees
ORDER BY department_id ASC, salary DESC;
```

---

## 14. SUBQUERIES

Scalar subquery:
```
SELECT name, salary
FROM employees
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
);
```

Correlated subquery:
```
SELECT e.name
FROM employees e
WHERE e.salary > (
  SELECT AVG(salary)
  FROM employees
  WHERE department_id = e.department_id
);
```

---

## 15. UNION

```
SELECT id, name FROM tableA
UNION
SELECT id, name FROM tableB;
```

Union all:
```
SELECT id, name FROM tableA
UNION ALL
SELECT id, name FROM tableB;
```

---

## 16. FUNCTIONS

String functions:
```
UPPER(text)
LOWER(text)
CONCAT(a, b, ...)
CONCAT_WS(separator, a, b, ...)
SUBSTRING(text, start, length)
SUBSTRING_INDEX(text, delimiter, count)
TRIM(text)
```

Numeric functions:
```
ROUND(number, decimals)
CEIL(number)
FLOOR(number)
ABS(number)
POWER(number, exponent)
MOD(a, b)
```

Date/time functions:
```
NOW()
CURDATE()
CURRENT_DATE
CURRENT_TIMESTAMP
DATE_ADD(date, INTERVAL n DAY)
DATE_SUB(date, INTERVAL n DAY)
DATE_FORMAT(date, format)
TIMESTAMPDIFF(unit, datetime1, datetime2)
```

Conditional functions:
```
CASE
  WHEN condition THEN result
  ELSE result
END
```

Example:
```
SELECT name,
  CASE
    WHEN salary >= 70000 THEN 'high'
    WHEN salary >= 50000 THEN 'medium'
    ELSE 'low'
  END AS salary_level
FROM employees;
```

Null-handling:
```
IFNULL(value, default)
COALESCE(value1, value2, ...)
```

Aggregate functions:
```
COUNT(column)
SUM(column)
AVG(column)
MIN(column)
MAX(column)
```

---

## 17. TRANSACTIONS

Start a transaction:
```
START TRANSACTION;
```

Commit changes:
```
COMMIT;
```

Rollback changes:
```
ROLLBACK;
```

Savepoint:
```
SAVEPOINT sp1;
ROLLBACK TO SAVEPOINT sp1;
```

Example:
```
START TRANSACTION;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;
```

---

## 18. INDEXES, VIEWS, and METADATA

Create an index:
```
CREATE INDEX idx_name ON table_name (column_name);
```

Drop an index:
```
DROP INDEX idx_name ON table_name;
```

Create a view:
```
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

Drop a view:
```
DROP VIEW view_name;
```

Show metadata:
```
SHOW DATABASES;
SHOW TABLES;
DESCRIBE table_name;
SHOW CREATE TABLE table_name;
```

---

## 19. MySQL Notes

- SQL keywords are not case-sensitive, but uppercase is common for readability.
- MySQL uses backticks for identifiers with spaces or reserved words: `` `column name` ``.
- Use `IF NOT EXISTS` or `IF EXISTS` to avoid errors when creating or dropping objects.
- `TRUNCATE TABLE` resets auto-increment counters in MySQL.
- Use `SET FOREIGN_KEY_CHECKS = 0;` before bulk loading or dropping foreign key tables, then `SET FOREIGN_KEY_CHECKS = 1;` after.
- Avoid `DELETE` without `WHERE` unless you want to remove all rows.
- In MySQL, `FULL OUTER JOIN` is not supported directly; use a `UNION` of `LEFT JOIN` and `RIGHT JOIN`.
