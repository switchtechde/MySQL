-- =========================================
-- Question 1
-- Topic      : DROP TABLE
-- Difficulty : Beginner
-- =========================================

-- Drop employees table

DROP TABLE employees;

-- =========================================
-- Question 2
-- Topic      : DROP TABLE
-- Difficulty : Beginner
-- =========================================

-- Drop students table

DROP TABLE students;

-- =========================================
-- Question 3
-- Topic      : TRUNCATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Remove all records from customers table

TRUNCATE TABLE customers;

-- =========================================
-- Question 4
-- Topic      : TRUNCATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Remove all records from products table

TRUNCATE TABLE products;

-- =========================================
-- Question 5
-- Topic      : DROP DATABASE
-- Difficulty : Intermediate
-- =========================================

-- Drop company_database

DROP DATABASE company_database;

-- =========================================
-- Question 6
-- Topic      : DROP COLUMN
-- Difficulty : Intermediate
-- =========================================

-- Drop email column from employees table

ALTER TABLE employees
DROP COLUMN email;

-- =========================================
-- Question 7
-- Topic      : DROP CONSTRAINT
-- Difficulty : Intermediate
-- =========================================

-- Drop UNIQUE constraint from customers table

ALTER TABLE customers
DROP CONSTRAINT unique_email;

-- =========================================
-- Question 8
-- Topic      : TRUNCATE TABLE
-- Difficulty : Intermediate
-- =========================================

-- Remove all records from bank_transactions table

TRUNCATE TABLE bank_transactions;

-- =========================================
-- Question 9
-- Topic      : DROP TABLE
-- Difficulty : Advanced
-- =========================================

-- Drop vehicle_services table permanently

DROP TABLE vehicle_services;

-- =========================================
-- Question 10
-- Topic      : DROP & TRUNCATE
-- Difficulty : Advanced
-- =========================================

-- DROP TABLE:
-- Removes complete table structure and data permanently

DROP TABLE employees;

-- TRUNCATE TABLE:
-- Removes only data from table
-- Table structure remains same

TRUNCATE TABLE employees;

-- =========================================
-- Question 1
-- Topic      : RENAME
-- Difficulty : Beginner
-- =========================================

-- Rename employees table to employee_details

ALTER TABLE employees
RENAME TO employee_details;

-- =========================================
-- Question 2
-- Topic      : RENAME COLUMN
-- Difficulty : Beginner
-- =========================================

-- Rename emp_name column to employee_name
-- in employees table

ALTER TABLE employees
RENAME COLUMN emp_name TO employee_name;

-- =========================================
-- Question 3
-- Topic      : RENAME TABLE
-- Difficulty : Intermediate
-- =========================================

-- Rename students table to student_details

ALTER TABLE students
RENAME TO student_details;

-- =========================================
-- Question 4
-- Topic      : RENAME COLUMN
-- Difficulty : Intermediate
-- =========================================

-- Rename transaction_amount column to amount
-- in transactions table

ALTER TABLE transactions
RENAME COLUMN transaction_amount TO amount;

-- =========================================
-- Question 5
-- Topic      : RENAME
-- Difficulty : Advanced
-- =========================================

-- Rename pipeline_execution_logs table
-- to pipeline_logs

ALTER TABLE pipeline_execution_logs
RENAME TO pipeline_logs;