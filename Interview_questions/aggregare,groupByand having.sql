Aggregate Function Sample Data
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

Questions
Find total salary paid to all employees.
Find average salary of employees.
Find highest salary.
Find lowest salary.
Find total employees count.
Find average age of employees.
Find maximum age.
Find minimum age.
Find total salary of IT department employees.
Find total employees whose salary is greater than 50000.

GROUP BY Sample Data
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

GROUP BY Questions
Find city wise total sales amount.
Find category wise total sales.
Find month wise revenue.
Find city wise order count.
Find category wise average order amount.
Find maximum sales amount category wise.
Find minimum order amount city wise.
Find customer wise total purchase amount.
Find month wise average sales.
Find category wise order count.
Find city wise maximum order amount.
Find month wise minimum sales amount.
Find customer wise total orders.
Find city wise average order amount.
Find category wise minimum amount.
Find category wise maximum amount.
Find month wise total orders.
Find customer wise average purchase amount.
Find city wise total customers.
Find category wise total revenue.

GROUP BY + WHERE Sample Data
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

GROUP BY + WHERE Questions
Find department wise total sales where sales_year is 2025.
Find region wise total sales where sales amount is greater than 40000.
Find department wise employee count where sales year is 2024.
Find region wise average sales where department is IT.
Find department wise maximum sales where sales year is 2025.
Find region wise minimum sales where sales amount exceeds 35000.
Find employee count department wise where region is West.
Find department wise total sales where department is Finance.
Find region wise total sales where sales year is 2025.
Find department wise average sales where sales amount is greater than 50000.

GROUP BY + WHERE + HAVING Sample Data
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

GROUP BY + WHERE + HAVING Questions
Find branch wise total transaction amount where txn_year is 2025 and total amount is greater than 1 lakh.
Find city wise transaction count where account type is Savings and count exceeds 2.
Find account type wise average amount where txn_year is 2025 and average amount exceeds 60000.
Find branch wise maximum transaction where account type is Current and maximum amount exceeds 1 lakh.
Find city wise total amount where txn_year is 2025 and total amount exceeds 2 lakhs.
Find branch wise transaction count where amount is greater than 50000 and count exceeds 2.
Find account type wise total amount where txn_year is 2025 and total exceeds 3 lakhs.
Find city wise minimum transaction where account type is Current and minimum amount exceeds 50000.
Find branch wise average amount where txn_year is 2025 and average amount exceeds 70000.
Find account type wise transaction count where txn_year is 2025 and count exceeds 3.