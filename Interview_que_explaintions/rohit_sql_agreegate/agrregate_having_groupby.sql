#Aggregate Function Sample Data
use class_homewok;
CREATE TABLE employees4 (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age INT
);

INSERT INTO employees4 VALUES
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
select*from employees4;
#Questions
#Find total salary paid to all employees.
select emp_name,  sum(salary)
from employees4 group by emp_name;

# Find average salary of employees.
select emp_name, avg(salary)
from employees4 group by emp_name;

#Find highest salary.
select  max(salary)
from employees4 ; 
#Find lowest salary.
select min(salary)
from employees4;

#from employees4 group by salary;
select salary
from employees4 group by salary;

#Find total employees count.
SELECT COUNT(emp_name)
FROM employees4;

#Find average age of employees.
select avg (age)
from employees4;
select * from employees4;



#Find maximum age.
select max(age)
from employees4;
#Find minimum age.
select min(age)
from employees4;
#Find total salary of IT department employees.
select sum(salary)
from employees4 where department = "it";

#Find total employees whose salary is greater than 50000.
select sum(salary)
from employees4 where salary > 50000;
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
select * from orders;
#GROUP BY Questions
#Find city wise total sales amount.
SELECT city, SUM(amount) AS total_sales
FROM orders group by city;
#Find category wise total sales.
select category, sum(amount)
from orders group by category;

#Find month wise revenue.
select order_month,sum(amount)
from orders group by order_month;

# Find city wise order count.
select city, count(*)
from orders group by city;

#Find category wise average order amount.
select category,avg(amount) as avg_order_amount
from orders group by category;
#Find maximum sales amount category wise.
select category , max(amount) as maximum_sale_amount
from orders group by category;

#Find minimum order amount city wise.
select city, min(amount)
from orders group by city;
#Find customer wise total purchase amount.
select customer_name, sum(amount)
from orders group by customer_name;
#Find month wise average sales.
select order_month, avg(amount)
from orders group by order_month;
#Find category wise order count.
select category ,count(*)
from orders group by category;
#Find city wise maximum order amount.
select city, max(amount)
from orders group by city;
#Find month wise minimum sales amount.
select order_month, min(amount)
from orders group by order_month;
#Find customer wise total orders.
select customer_name ,count(*) as total_order
from orders group by customer_name;
#Find city wise average order amount
select city, avg(amount) as avg_order_amt_by_city
from orders group by city;

#Find category wise minimum amount.
select category ,min(amount)
from orders group by category;
#Find category wise maximum amount.
select category ,max(amount)
from orders group by category;
#Find month wise total orders.
select order_month, count(*)
from orders group by order_month;
#Find customer wise average purchase amount.
select customer_name , avg(amount)
from orders group by customer_name;
#Find city wise total customers.
select city, count(*)
from orders group by city;
#Find category wise total revenue.
select category, sum(amount)
from orders group by category;
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

#GROUP BY + WHERE Questions
#Find department wise total sales where sales_year is 2025.
select department , sum(sales_amount)
from sales where sales_year = 2025 group by department;
#Find region wise total sales where sales amount is greater than 40000.
 select region, sum(sales_amount)
 from sales where sales_amount > 40000
 group by region;
#Find department wise employee count where sales year is 2024.
select department , count(*)
from sales where sales_year = 2024 
group by department;
#Find region wise average sales where department is IT.
select region, avg(sales_amount)
from sales where department = "IT"
group by region;
#Find department wise maximum sales where sales year is 2025.
select department, max(sales_amount)
from sales where sales_year=2025
group by department;
#Find region wise minimum sales where sales amount exceeds 35000.
select region, min(sales_amount)
from sales where sales_amount > 35000
group by region;
select * from sales;
#Find employee count department wise where region is West.
select department, count(*)
from sales where region = "west"
group by department;
#Find department wise total sales where department is Finance.
select department, sum(sales_amount)
from sales where department= "finance"
group by department;
#Find region wise total sales where sales year is 2025.
select region ,sum(sales_amount)
from sales where sales_year = 2025
group by region;
#Find department wise average sales where sales amount is greater than 50000.
select department, avg (sales_amount)
from sales where sales_amount > 50000 
group by department;


#GROUP BY + WHERE + HAVING Sample Data
CREATE TABLE transactions (
    txn_id INT,
    branch_name VARCHAR(50),
    account_type VARCHAR(50),
    customer_city VARCHAR(50),
    amount INT,
    txn_year INT
);


INSERT INTO transactions VALUES
(1,'Andheri','Savings','Mumbai',50000,2025),
(2,'Virar','Current','Mumbai',80000,2025),
(3,'Borivali','Savings','Pune',30000,2024),
(4,'Andheri','Current','Delhi',90000,2025),
(5,'Virar','Savings','Mumbai',70000,2025),
(6,'Borivali','Current','Pune',40000,2024),
(7,'Andheri','Savings','Delhi',60000,2025),
(8,'Virar','Current','Mumbai',120000,2025),
(9,'Borivali','Savings','Pune',50000,2025),
(10,'Andheri','Current','Delhi',110000,2025);
select * from transactions;
#GROUP BY + WHERE + HAVING Questions
#Find branch wise total transaction amount where txn_year is 2025 and total amount is greater than 1 lakh.
 select branch_name, sum(amount) as branch_wise_total_transaction
 from transactions where txn_year = 2025
 group by branch_name
 having sum(amount) > 100000;
 
 SELECT branch_name, SUM(amount) AS branch_wise_total_transaction
FROM transactions
WHERE txn_year = 2025
GROUP BY branch_name
HAVING SUM(amount) > 100000;

#Find city wise transaction count where account type is Savings and count exceeds 2.
select customer_city, count(*) as city_wise_transaction
from transactions where account_type = "savings" 
group by customer_city
having count(*) > 2;
select * from transactions;
#Find account type wise average amount where txn_year is 2025 and average amount exceeds 60000.
select account_type, avg(amount)
from transactions where txn_year = 2025
group by account_type
having avg(amount) > 60000;

#Find branch wise maximum transaction where account type is Current and maximum amount exceeds 1 lakh.
select branch_name, max(amount)
from transactions where account_type = "current"
group by branch_name
having max(amount) > 100000;
#Find city wise total amount where txn_year is 2025 and total amount exceeds 2 lakhs.
select customer_city, sum(amount) 
from transactions where txn_year = 2025
group by customer_city
having sum(amount) > 200000;
#Find branch wise transaction count where amount is greater than 50000 and count exceeds 2
select branch_name, count(*)
from transactions where amount > 50000
group by branch_name
having count(*) > 2;
#Find account type wise total amount where txn_year is 2025 and total exceeds 3 lakhs.
select account_type , sum(amount)
from transactions where txn_year = 2025
group by account_type
having sum(amount) > 300000;
#Find city wise minimum transaction where account type is Current and minimum amount exceeds 50000.
select customer_city, min(amount)
from transactions where account_type = "current" 
group by customer_city
having min(amount) > 50000;
#Find branch wise average amount where txn_year is 2025 and average amount exceeds 70000.
select branch_name, avg(amount)
from transactions where txn_year = 2025
group by branch_name
having avg(amount) > 70000;
#Find account type wise transaction count where txn_year is 2025 and count exceeds 3.
select account_type, count(*)
from transactions where txn_year = 2025
group by account_type
having count(*) > 3;