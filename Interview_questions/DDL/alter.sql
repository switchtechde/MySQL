-- =========================================
-- Question 1
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add email column in employees table
ALTER TABLE EMPLOYEES
ADD email VARCHAR(255);

-- =========================================
-- Question 2
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add phone_number column in customers table
ALTER TABLE CUSTOMERS
ADD phone_number VARCHAR(20);

-- =========================================
-- Question 3
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add date_of_joining column in employees table
ALTER TABLE EMPLOYEES
ADD date_of_joining DATE;

-- =========================================
-- Question 4
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Rename column emp_name to employee_name
-- in employees table
ALTER TABLE EMPLOYEES
RENAME COLUMN emp_name TO employee_name;

-- =========================================
-- Question 5
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Modify salary datatype in employees table
ALTER TABLE EMPLOYEES
MODIFY salary DECIMAL(10, 2);

-- =========================================
-- Question 6
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add NOT NULL constraint on salary column
ALTER TABLE EMPLOYEES
MODIFY salary DECIMAL(10, 2) NOT NULL;

-- =========================================
-- Question 7
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add UNIQUE constraint on email column
ALTER TABLE EMPLOYEES
ADD UNIQUE (email);

-- =========================================
-- Question 8
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add PRIMARY KEY on product_id column
ALTER TABLE PRODUCTS
ADD PRIMARY KEY (product_id);

-- =========================================
-- Question 9
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add DEFAULT value 'Pune' for city column
ALTER TABLE EMPLOYEES
ALTER city SET DEFAULT 'Pune';

-- =========================================
-- Question 10
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Drop phone_number column from customers table
ALTER TABLE CUSTOMERS
DROP COLUMN phone_number;

-- =========================================
-- Question 11
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Rename table students to student_details
ALTER TABLE STUDENTS
RENAME TO student_details;

-- =========================================
-- Question 12
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add Foreign Key in orders table
ALTER TABLE ORDERS
ADD CONSTRAINT fk_customer_id
FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id);

-- =========================================
-- Question 13
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Increase size of product_name column
ALTER TABLE PRODUCTS
MODIFY product_name VARCHAR(500);

-- =========================================
-- Question 14
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Drop UNIQUE constraint from customers table
ALTER TABLE CUSTOMERS
DROP INDEX email;

-- =========================================
-- Question 15
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add created_at column in orders table
ALTER TABLE ORDERS
ADD created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- =========================================
-- Question 16
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Rename transactions table to bank_transactions
ALTER TABLE transactions
RENAME TO bank_transactions;

-- =========================================
-- Question 17
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add CHECK constraint on salary column
ALTER TABLE EMPLOYEES
ADD CONSTRAINT chk_salary CHECK (salary > 0);

-- =========================================
-- Question 18
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Drop city column from employees table
ALTER TABLE EMPLOYEES
DROP COLUMN city;

-- =========================================
-- Question 19
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add status column in pipeline_execution_logs table
ALTER TABLE pipeline_execution_logs
ADD status VARCHAR(20) DEFAULT 'PENDING';

-- =========================================
-- Question 20
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Modify amount datatype in bank_transactions table
ALTER TABLE bank_transactions
MODIFY amount DECIMAL(15, 2);
