
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age INT
);

INSERT INTO employees VALUES
(1,'Rahul','IT',50000,25),
(2,'Amit','HR',40000,30),
(3,'Neha','IT',60000,27),
(4,'Priya','Finance',55000,29),
(5,'Karan','HR',45000,32),
(6,'Sneha','IT',70000,26),
(7,'Rohit','Finance',48000,31),
(8,'Anjali','Sales',52000,28),
(9,'Vikas','Sales',51000,35),
(10,'Pooja','IT',65000,24);

select * from employees;
#questions
#find total salary paid to all employees.
 select sum(salary) as total_salary from employees;

#find average salary of employees.
 select avg(salary) as total_salary from employees;

#find highest salary.
 select max(salary) as total_salary from employees;

#find lowest salary.
select min(salary) as total_salary from employees;

#find total employees count.
 select count(*) as total_emps from employees;

#find average age of employees.
 select avg(age) as avg_emp_age from employees;

#find maximum age.
 select max(age) as avg_emp_age from employees;

#find minimum age.
 select min(age) as avg_emp_age from employees;

#find total salary of it department employees.
 select sum(salary) as it_dept_salary from employees where department = 'it';

#find total employees whose salary is greater than 50000.
 select count(salary) as salary_more_than_50k from employees where salary > 50000;

#GROUP BY Sample Data
CREATE TABLE orders (
    order_id INT,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    category VARCHAR(50),
    amount INT,
    order_month VARCHAR(20)
);

INSERT INTO orders VALUES
(101,'Rahul','Mumbai','Electronics',12000,'Jan'),
(102,'Amit','Pune','Clothing',3000,'Jan'),
(103,'Neha','Mumbai','Electronics',15000,'Feb'),
(104,'Priya','Delhi','Furniture',20000,'Feb'),
(105,'Karan','Pune','Clothing',4000,'Mar'),
(106,'Sneha','Mumbai','Furniture',18000,'Mar'),
(107,'Rohit','Delhi','Electronics',22000,'Apr'),
(108,'Anjali','Mumbai','Clothing',3500,'Apr'),
(109,'Vikas','Pune','Furniture',25000,'May'),
(110,'Pooja','Delhi','Electronics',27000,'May');

#GROUP BY Questions
#find city wise total sales amount.
 select city, count(*) as city_wise_total_sales from orders group by city;

#find category wise total sales.
 select category, count(*) as city_wise_total_sales from orders group by category;

#find month wise revenue.
 select order_month, sum(amount) as monthly_revenue from orders group by order_month;

#find city wise order count.
 select city, count(*) as total_orders from orders group by city;

#find category wise average order amount.
 select category, avg(amount) as  ave_ord_amt from orders group by category;

#find maximum sales amount category wise.
 select category, max(amount) as  ave_ord_amt from orders group by category;

#find minimum order amount city wise.
select category, min(amount) as  ave_ord_amt from orders group by category;

#find customer wise total purchase amount.
 select customer_name, sum(amount) as total_amt_cust_wise from orders group by customer_name;

#find month wise average sales.
 select order_month, count(*) as total_sales_mon_wise from orders group by order_month;

#find category wise order count.
 select category, count(*) as total_odr_cat_wise from orders group by category;

#find city wise maximum order amount.
 select city, max(amount) as city_max_ord from orders group by city;

#find month wise minimum sales amount.
 select order_month, min(amount) as min_sales from orders group by order_month;

#find customer wise total orders.
 select customer_name, count(*) as cust_wise_odr from orders group by customer_name;

#find city wise average order amount.
 select city, avg(amount) as avg_city_wise_spend from orders group by city;

#find category wise minimum amount.
 select category, min(amount) as cat_min_spend from orders group by category;

#find category wise maximum amount.
 select category, max(amount) as cat_max_spend from orders group by category;

#find month wise total orders.
 select order_month, count(*) as total_mon_odr from orders group by order_month;

#find customer wise average purchase amount.
 select customer_name, avg(amount) as avg_amt from orders group by customer_name;

#find city wise total customers.
 select city, count(customer_name) as total_clients from orders group by city;

#find category wise total revenue.
 select category, sum(amount) as total_cat_rvn from orders group by category;

#GROUP BY + WHERE Sample Data
CREATE TABLE sales (
    sale_id INT,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    region VARCHAR(50),
    sales_amount INT,
    sales_year INT
);

INSERT INTO sales VALUES
(1,'Rahul','IT','West',50000,2025),
(2,'Amit','HR','North',30000,2024),
(3,'Neha','IT','West',70000,2025),
(4,'Priya','Finance','South',45000,2025),
(5,'Karan','Sales','East',35000,2024),
(6,'Sneha','IT','West',80000,2025),
(7,'Rohit','Finance','South',60000,2025),
(8,'Anjali','Sales','East',40000,2025),
(9,'Vikas','HR','North',38000,2024),
(10,'Pooja','IT','West',90000,2025);

select * from sales ;

#GROUP BY + WHERE Questions
#find department wise total sales where sales_year is 2025.
 select department, count(*) as total_sales from sales where sales_year = 2025 group by department;

#find region wise total sales where sales amount is greater than 40000.
 select region, count(*) as total_sales from sales where sales_amount > 40000 group by region;

#find department wise employee count where sales year is 2024.
 select department, count(*) as total_emp from sales where sales_year = 2024 group by department;

#find region wise average sales where department is it.
 select region, avg(sales_amount) as avg_sales from sales where department = 'it' group by region;

#find department wise maximum sales where sales year is 2025.
 select department, max(sales_amount) from sales where sales_year = 2025 group by department ;

#find region wise minimum sales where sales amount exceeds 35000.
 select region, min(sales_amount) as min_sales_amt from sales where sales_amount > 35000 group by region;

#find employee count department wise where region is west.
 select department, count(*) as total_egn_emp from sales where region = 'west' group by department;

#find department wise total sales where department is finance.
select department, sum(sales_amount) as total_dept_sales from sales where department = 'finance' group by department;

#find region wise total sales where sales year is 2025.
 select region, sum(sales_amount) as total_rgn_sales from sales where  sales_year = 2025 group by region;

#find department wise average sales where sales amount is greater than 50000.
 select department, avg(sales_amount) as avg_sales_amt from sales where sales_amount > 50000 group by department;

#group by + where + having sample data

create table transactions (
    txn_id int,
    branch_name varchar(50),
    account_type varchar(50),
    customer_city varchar(50),
    amount int,
    txn_year int
);

insert into transactions values
(1,'andheri','savings','mumbai',50000,2025),
(2,'virar','current','mumbai',80000,2025),
(3,'borivali','savings','pune',30000,2024),
(4,'andheri','current','delhi',90000,2025),
(5,'virar','savings','mumbai',70000,2025),
(6,'borivali','current','pune',40000,2024),
(7,'andheri','savings','delhi',60000,2025),
(8,'virar','current','mumbai',120000,2025),
(9,'borivali','savings','pune',50000,2025),
(10,'andheri','current','delhi',110000,2025);

#group by + where + having questions
#find branch wise total transaction amount where txn_year is 2025 and total amount is greater than 1 lakh.
 select branch_name, sum(amount) as total_br_amt from transactions where txn_year = 2025 group by branch_name having total_br_amt > 1;

#find city wise transaction count where account type is savings and count exceeds 2.
 select customer_city, count(*) as city_wise_total_txn from transactions where account_type = 'savings' group by customer_city having city_wise_total_txn > 2;

#find account type wise average amount where txn_year is 2025 and average amount exceeds 60000.
 select account_type, avg(amount) as ac_wise_txn_amt from transactions where txn_year = 2025 group by account_type having ac_wise_txn_amt > 60000;

#find branch wise maximum transaction where account type is current and maximum amount exceeds 1 lakh.
 select branch_name, max(amount) as max_txn_amt from transactions where account_type = 'current' group by branch_name having max_txn_amt > 100000;

#find city wise total amount where txn_year is 2025 and total amount exceeds 2 lakhs.
 select customer_city, sum(amount) as city_wise_total from transactions where txn_year = 2025 group by customer_city having city_wise_total > 200000;

#find branch wise transaction count where amount is greater than 50000 and count exceeds 2.
select branch_name, count(*) as br_wise_total from transactions where amount > 50000 group by branch_name having br_wise_total > 2;

#find account type wise total amount where txn_year is 2025 and total exceeds 3 lakhs.
 select account_type, sum(amount) as ac_wise_total_txn from transactions where txn_year = 2025 group by account_type having ac_wise_total_txn > 300000;

#find city wise minimum transaction where account type is current and minimum amount exceeds 50000.
 select customer_city, min(amount) as min_txn_city_wise from transactions where account_type = 'current' group by customer_city having min_txn_city_wise > 50000;

#find branch wise average amount where txn_year is 2025 and average amount exceeds 70000.
 select branch_name, avg(amount) as br_wise_avf_amt from transactions where txn_year = 2025 group by branch_name having br_wise_avf_amt > 70000;

#find account type wise transaction count where txn_year is 2025 and count exceeds 3.
 select account_type, count(*) as ac_wise_total_txn from transactions where txn_year = 2025 group by account_type having ac_wise_total_txn > 3;
