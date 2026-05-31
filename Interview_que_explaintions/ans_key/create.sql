
# Question 1)
   # Create an employees table to store: employee id employee name ,salary, city
# ans
create table employees (emp_id int unique not null,emp_name char (100) not null ,salary int not null ,city char not null
);

#question 2 )
# Create a students table to store: student id , student name, date of birth , marks , email
#ans
create table student (student_id int not null , student_name char(100) not null, date_of_birth int not null, marks int not null, email char(100)
);

#Question 3 )
# Create a departments table to maintain: department id department name location
#ANS
create table department (depart_id int unique not null , depart_name char(100) not null , location char (100) not null
);

# question 4)
# Create a products table to store: product id product name category price

create table products (product_id int unique not null, product_name char (100) not null, category int null, price float not null
);

# question 5)
# Create a books table for library management. Store: book id book name author name publication year

create table library_management(book_id int unique not null , book_name char(100) not null ,
 author_name char (100) , publication_year int not null);

 # questiom 6)
 # Create a customers table where: customer id should not be null email should be unique city default value should be Pune
 create table customer_table(customer_id int not null, email char (100) unique, city char(4) default 'pune' );

 # questiom 7
 #  Create an employees table where: emp_id should be Primary Key salary should not be null

 create table employeee_table (enp_id int primary key , salary float not null
 );

 # questiom 8
 #  Create a users table where: username should be unique password cannot be null
create table user_table( user_name char(50) unique , password char (50)  not null
);

# question 9
# Create a vehicles table where: vehicle number should be unique owner name should not be null

create table vehicle_table (vehical_number int unique not null, Owner_name char(50) not null
);

# question 10
# Create a transactions table with: transaction id
# customer id transaction amount transaction date transaction type Relationship Based Questions

create table trasaction_table (trasaction_id int unique not null, customer_id int unique not null,
 transaction_amt float not null , transaction_date date not null , trasaction_type char (50) not null
);

# question 11
 #Create an employee_attendance table to store: attendance id employee id attendance date attendance status

 create table employee_attendace (attendace_id int not null unique ,
 employee_id int not null unique , attendace_DATE date  ,  ATTENDACE_STATUS char(100) );

 # question 12
 #   Create a bank_transactions table for banking system.
 # Store: transaction id account number amount transaction type transaction timestamp

create table bank_transactions (transaction_id int not null unique ,
 account_number int not null unique , amount_transaction_type char(100) not null  ,  trasaction timestamp );

# question 13
#  Create an  table for online shopping platform.
# Store: order id customer id product id quantity total amount order date
create table ecommerce_orders (order_id  int not null unique , product_id int not null unique ,
 quantity int not null , total_amount decimal(10.2), order_date date
);

# question 14
# Create a vehicle_services table for automobile domain.
#Store: service id, vehicle number, service date ,service cost, service center
create table vehical_service ( service_id int not null unique, vehical_number int unique not null , service_date date, service_cost decimal(10.2),
service_center char(100)
);

# question 15
   # Create a pipeline_execution_logs table for Data Engineering pipeline monitoring.
   # Store: pipeline id ,pipeline name, execution start time, execution end time , status , error message
   create table pipeline_execution_logs(pipeline_id int not null unique ,pipeline_name char(100) not null, execution_start_time timestamp ,
   execution_end_time timestamp , status char(100) , error_message char (100));


#################### alter#########################
#Question 1
#-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add email column in employees table
alter table employees add column email_name char(100) not null ;

-- Question 2
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add phone_number column in customers table

alter table customer_table add column phone_number int not null;

-- Question 3
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Add date_of_joining column in employees table

alter table employeee_table add column date_of_joing int not null;

#Question 4
-- Topic      : ALTER TABLE
-- Difficulty : Beginner
-- =========================================

-- Rename column emp_name to employee_name
-- in employees table
alter table employees change  emp_name employee_name  char (100);

ALTER TABLE employees
CHANGE emp_name employee_name VARCHAR(50);

