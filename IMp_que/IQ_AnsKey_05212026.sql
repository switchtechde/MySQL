USE PRACTICE;
#CRATE TABLE SQL Practice Questions
#Question 1
 #   Create an employees table to store:
  #  employee id
   # employee name
    #salary
    #city
    CREATE TABLE EMP (emp_ID INT,emp_name VARCHAR(50) , Salary int, City VARCHAR(50));

#Question 2
    #Create a students table to store:

    #student id
    #student name
    #date of birth
    #marks
    #email
CREATE TABLE STUDENTS( student_id int,student_name VARCHAR(50),dob date, marks int,email VARCHAR(100));

#Question 3
 #   Create a departments table to maintain:

  #  department id
   # department name
    #location

Create table departments (department_id int, department_name varchar (50), location varchar(100));

#Question 4
 #   Create a products table to store:
  #  product id
   # product name
    #category
    #price
create table products (product_id int not null unique,product_name varchar (50),category varchar (40),price int);

#  Question 5
 #   Create a books table for library management.
  #  Store:

   # book id
    #book name
    #author name
    #publication year
create table library_management (book_id int,book_name varchar(50),author_name varchar (50),publication_year int);

#Question 6
 #   Create a customers table where:
  #  customer id should not be null
   # email should be unique
    #city default value should be Pune
    create table customers(customers_id int not null ,email varchar (100) unique,city varchar(20) default'pune');

#Question 7
 #   Create an employees table where:

  #  emp_id should be Primary Key
   # salary should not be null

   create table employees (emp_id int primary key ,emp_name varchar (50),city varchar (50),salary int not null);

#Question 8
 #   Create a users table where:

  #  username should be unique
   # password cannot be null

create table users(user_id int , user_name varchar(50) unique, password varchar (50) not null);
#Question 9

 #   Create a vehicles table where:
  #  vehicle number should be unique
   # owner name should not be null

create table vehicles(vehicle_id int,owner_name varchar (50) not null ,vehicle_number int unique);
#Question 10
 #   Create a transactions table with:
  #  transaction id
   # customer id
    #transaction amount
    #transaction date
    #transaction type
create table transactions(transaction_id int,customer_id int,transaction_amount int ,transaction_date date,transaction_type varchar (50));

#Relationship Based Questions

#Question 11
 #   Create customers and orders tables with proper Primary Key and Foreign Key relationship.
 create table customer (id int primary key  , name varchar(60),city varchar(50));
 CREATE TABLE customer_orders (order_id INT,order_name VARCHAR(80),city VARCHAR(50));

#Question 12
 #   Create departments and employees tables where employees belong to departments.
#Question 13
 #   Create products and categories tables using Foreign Key relationship.
#Question 14
 #   Create students and courses tables with relationship.
#Question 15
 #   Create authors and books tables where books belong to authors.


#Question 16
 #   Create an employee_attendance table to store:

  #  attendance id
   # employee id
    #attendance date
    #attendance status

create table employee_attendance (attendance_id int not null unique,employee_id int not null unique ,attendance_date date,attendance_status varchar (50));

#Question 17
 #   Create a bank_transactions table for banking system.

  #  Store:

   # transaction id
    #account number
    #amount
    #transaction type
    #transaction timestamp

create table bank_transactions ( transaction_id int,account_number int,amount int ,transaction_type varchar (50),transaction_timestamp timestamp);
#Question 18
 #   Create an ecommerce_orders table for online shopping platform.

  #  Store:

   # order id
    #customer id
    #product id
    #quantity
    #total amount
    #order date

   create table ecommerce_orders(order_id int, customer_id int , product_id int,quantity varchar (40),total_amount int,order_date date);

#Question 19
 #   Create a vehicle_services table for automobile domain.

  #  Store:
   # service id
    #vehicle number
   # service date
   # service cost
    #service center

    create table vehicle_services(service_id int,vehicle_number int, service_date date, service_cost int,service_center varchar (100));

#Question 20
 #   Create a pipeline_execution_logs table for Data Engineering pipeline monitoring.
  #  Store:

   # pipeline id
    #pipeline name
    #execution start time
    #execution end time
    #status
    #error message

    create table pipeline_execution_logs (pipeline_id int , pipeline_name varchar(50),execution_start_time timestamp ,execution_end_time timestamp,status varchar(50),error_message varchar(100));

    -- =========================================
-- Question 1
-- Topic      : DROP TABLE
-- Difficulty : Beginner
drop table emp;

-- =========================================
-- Question 2
-- Topic      : DROP TABLE
-- Difficulty : Beginner
DROP TABLE students;

-- =========================================
-- Question 3
-- Topic      : TRUNCATE TABLE
-- Difficulty : Beginner
-- =========================================
TRUNCATE TABLE customers;
-- =========================================
-- Question 4
-- Topic      : TRUNCATE TABLE
-- Difficulty : Beginner
  TRUNCATE TABLE products;
-- =========================================
-- Question 5
-- Topic      : DROP DATABASE
-- Difficulty : Intermediate
create database practives;

DROP DATABASE practives;

-- =========================================
-- Question 6
-- Topic      : DROP COLUMN
-- Difficulty : Intermediate
CREATE TABLE EMP (emp_ID INT,emp_name VARCHAR(50) , Salary int, City VARCHAR(50));

ALTER TABLE emp DROP COLUMN emp_id;
-- =========================================
-- Question 7
-- Topic      : DROP CONSTRAINT
-- Difficulty : Intermediate
CREATE TABLE customer1 (ID INT,name VARCHAR(50) , email VARCHAR(50) unique);

ALTER TABLE customer1 DROP CONSTRAINT email;

-- =========================================
-- Question 8
-- Topic      : TRUNCATE TABLE
-- Difficulty : Intermediate
TRUNCATE TABLE transactions;
-- =========================================
-- Question 9
-- Topic      : DROP TABLE
-- Difficulty : Advanced

DROP TABLE transactions ;
-- =========================================
-- Question 10
-- Topic      : DROP & TRUNCATE
-- Difficulty : Advanced

DROP TABLE emp;

TRUNCATE TABLE employees;
-- =========================================
-- Question 1
-- Topic      : RENAME
-- Difficulty : Beginner

ALTER TABLE emp RENAME TO employee_details;
-- =========================================
-- Question 2
-- Topic      : RENAME COLUMN
-- Difficulty : Beginner
ALTER TABLE emp RENAME COLUMN emp_name TO employee_name;

-- =========================================
-- Question 3
-- Topic      : RENAME TABLE
-- Difficulty : Intermediate
ALTER TABLE students RENAME TO student_del;
-- =========================================
-- Question 4
-- Topic      : RENAME COLUMN
-- Difficulty : Intermediate

ALTER TABLE bank_transactions RENAME COLUMN account_number TO amount_num;
-- =========================================
-- Question 5
-- Topic      : RENAME
-- Difficulty : Advanced

ALTER TABLE pipeline_execution_logs RENAME TO pipeline_logs;

-- =========================================
-- Question 1
-- Topic      : ALTER TABLE
-- Difficulty : Beginner

-- Add email column in employees table
Alter table emp add column email varchar (50);
-- =========================================
-- Question 2
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add phone_number column in customers table
Alter table customers add column phone_number int ;

-- =========================================
-- Question 3
-- Topic      : ALTER TABLE
-- Difficulty : Beginner

-- Add date_of_joining column in employees table
Alter table emp add column date_of_joining int;
-- =========================================
-- Question 4
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Rename column emp_name to employee_name
-- in employees table
Alter table emp Rename column emp_name to employee_name;
-- =========================================
-- Question 5
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Modify salary datatype in employees table
Alter table emp modify column salary varchar(40);

-- =========================================
-- Question 6
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add NOT NULL constraint on salary column
Alter table emp modify column salary  varchar (70) not null;
-- =========================================
-- Question 7
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add UNIQUE constraint on email column
Alter table STUDENTS modify column email varchar(100) unique;
-- =========================================
-- Question 8
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add PRIMARY KEY on product_id column
Alter table products modify column product_id int primary key ;
Alter table products modify column product_name varchar (50) unique ;

-- =========================================
-- Question 9
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add DEFAULT value 'Pune' for city column
Alter table emp modify column city varchar (100) default ' pune';
-- =========================================
-- Question 10
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Drop phone_number column from customers table
Alter table customers drop column phone_number;
-- =========================================
-- Question 11
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Rename table students to student_details
Alter table students Rename student_details;
-- =========================================
-- Question 12
-- Topic      : ALTER TABLE
-- Difficulty : Intermediate
-- =========================================

-- Add Foreign Key in orders table

-- =========================================
-- Question 13
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Increase size of product_name column
Alter table products modify column product_name varchar (100) ;
-- =========================================
-- Question 14
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================
-- Drop UNIQUE constraint from customers table
Alter table customer modify column id int unique;
Alter table customer drop constraint id ;

-- =========================================
-- Question 15
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add created_at column in orders table
Alter table customer_orders add column created_at varchar (80);
-- =========================================
-- Question 16
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Rename transactions table to bank_transactions
Alter table transactions Rename bank_transaction;
-- =========================================
-- Question 17
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add CHECK constraint on salary column
desc table emp;
show tables;
ALTER TABLE employee_details MODIFY COLUMN salary INT CHECK (salary > 40000);
-- =========================================
-- Question 18
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Drop city column from employees table
Alter table emp drop column city;

-- =========================================
-- Question 19
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================

-- Add status column in pipeline_execution_logs table
Alter table pipeline_execution_logs add column pip_status varchar (60);

-- =========================================\
-- Question 20
-- Topic      : ALTER TABLE
-- Difficulty : Advanced
-- =========================================
-- Modify amount datatype in bank_transactions table
Alter table bank_transactions modify column amount varchar (60);
Alter table bank_transactions modify column amount varchar (80);

