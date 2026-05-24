-- =========================================
-- Question 1
-- Topic      : CREATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Create an employees table to store:
-- employee id
-- employee name
-- salary
-- city

CREATE TABLE employees
(
    emp_id INT,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2),
    city VARCHAR(50)
);

-- =========================================
-- Question 2
-- Topic      : CREATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Create a students table to store:
-- student id
-- student name
-- date of birth
-- marks
-- email

CREATE TABLE students
(
    student_id INT,
    student_name VARCHAR(100),
    dob DATE,
    marks DECIMAL(5,2),
    email VARCHAR(100)
);

-- =========================================
-- Question 3
-- Topic      : CREATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Create a departments table to maintain:
-- department id
-- department name
-- location

CREATE TABLE departments
(
    department_id INT,
    department_name VARCHAR(100),
    location VARCHAR(50)
);

-- =========================================
-- Question 4
-- Topic      : CREATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Create a products table to store:
-- product id
-- product name
-- category
-- price

CREATE TABLE products
(
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- =========================================
-- Question 5
-- Topic      : CREATE TABLE
-- Difficulty : Beginner
-- =========================================

-- Create a books table for library management.
-- Store:
-- book id
-- book name
-- author name
-- publication year

CREATE TABLE books
(
    book_id INT,
    book_name VARCHAR(150),
    author_name VARCHAR(100),
    publication_year INT
);

-- =========================================
-- Question 6
-- Topic      : Constraints
-- Difficulty : Intermediate
-- =========================================

-- Create a customers table where:
-- customer id should not be null
-- email should be unique
-- city default value should be Pune

CREATE TABLE customers
(
    customer_id INT NOT NULL,
    customer_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50) DEFAULT 'Pune'
);

-- =========================================
-- Question 7
-- Topic      : Constraints
-- Difficulty : Intermediate
-- =========================================

-- Create an employees table where:
-- emp_id should be Primary Key
-- salary should not be null

CREATE TABLE employees
(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2) NOT NULL
);

-- =========================================
-- Question 8
-- Topic      : Constraints
-- Difficulty : Intermediate
-- =========================================

-- Create a users table where:
-- username should be unique
-- password cannot be null

CREATE TABLE users
(
    user_id INT,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- =========================================
-- Question 9
-- Topic      : Constraints
-- Difficulty : Intermediate
-- =========================================

-- Create a vehicles table where:
-- vehicle number should be unique
-- owner name should not be null

CREATE TABLE vehicles
(
    vehicle_id INT,
    vehicle_number VARCHAR(50) UNIQUE,
    owner_name VARCHAR(100) NOT NULL
);

-- =========================================
-- Question 10
-- Topic      : CREATE TABLE
-- Difficulty : Intermediate
-- =========================================

-- Create a transactions table with:
-- transaction id
-- customer id
-- transaction amount
-- transaction date
-- transaction type

CREATE TABLE transactions
(
    transaction_id INT,
    customer_id INT,
    transaction_amount DECIMAL(12,2),
    transaction_date DATE,
    transaction_type VARCHAR(20)
);

-- =========================================
-- Question 11
-- Topic      : Foreign Key
-- Difficulty : Intermediate
-- =========================================

-- Create customers and orders tables
-- with proper Primary Key and Foreign Key relationship

CREATE TABLE customers
(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

-- =========================================
-- Question 12
-- Topic      : Foreign Key
-- Difficulty : Intermediate
-- =========================================

-- Create departments and employees tables
-- where employees belong to departments

CREATE TABLE departments
(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE employees
(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

-- =========================================
-- Question 13
-- Topic      : Foreign Key
-- Difficulty : Intermediate
-- =========================================

-- Create products and categories tables
-- using Foreign Key relationship

CREATE TABLE categories
(
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,

    FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
);

-- =========================================
-- Question 14
-- Topic      : Foreign Key
-- Difficulty : Intermediate
-- =========================================

-- Create students and courses tables
-- with relationship

CREATE TABLE courses
(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE students
(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    course_id INT,

    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

-- =========================================
-- Question 15
-- Topic      : Foreign Key
-- Difficulty : Intermediate
-- =========================================

-- Create authors and books tables
-- where books belong to authors

CREATE TABLE authors
(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100)
);

CREATE TABLE books
(
    book_id INT PRIMARY KEY,
    book_name VARCHAR(150),
    author_id INT,

    FOREIGN KEY (author_id)
    REFERENCES authors(author_id)
);

-- =========================================
-- Question 16
-- Topic      : CREATE TABLE
-- Difficulty : Advanced
-- =========================================

-- Create an employee_attendance table to store:
-- attendance id
-- employee id
-- attendance date
-- attendance status

CREATE TABLE employee_attendance
(
    attendance_id INT PRIMARY KEY,
    employee_id INT,
    attendance_date DATE,
    attendance_status VARCHAR(20)
);

-- =========================================
-- Question 17
-- Topic      : Banking Domain
-- Difficulty : Advanced
-- =========================================

-- Create a bank_transactions table
-- for banking system

CREATE TABLE bank_transactions
(
    transaction_id INT PRIMARY KEY,
    account_number VARCHAR(30),
    amount DECIMAL(12,2),
    transaction_type VARCHAR(20),
    transaction_timestamp TIMESTAMP
);

-- =========================================
-- Question 18
-- Topic      : E-Commerce Domain
-- Difficulty : Advanced
-- =========================================

-- Create an ecommerce_orders table
-- for online shopping platform

CREATE TABLE ecommerce_orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(12,2),
    order_date DATE
);

-- =========================================
-- Question 19
-- Topic      : Automobile Domain
-- Difficulty : Advanced
-- =========================================

-- Create a vehicle_services table
-- for automobile domain

CREATE TABLE vehicle_services
(
    service_id INT PRIMARY KEY,
    vehicle_number VARCHAR(30),
    service_date DATE,
    service_cost DECIMAL(10,2),
    service_center VARCHAR(100)
);

-- =========================================
-- Question 20
-- Topic      : Data Engineering
-- Difficulty : Advanced
-- =========================================

-- Create a pipeline_execution_logs table
-- for Data Engineering pipeline monitoring

CREATE TABLE pipeline_execution_logs
(
    pipeline_id INT,
    pipeline_name VARCHAR(100),
    execution_start_time TIMESTAMP,
    execution_end_time TIMESTAMP,
    status VARCHAR(20),
    error_message VARCHAR(255)
);