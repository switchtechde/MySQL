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
SELECT sum(SALARY) AS TOTAL_SALARY FROM EMPLOYEES;

Find average salary of employees.
SELECT avg(SALARY) AS TOTAL_SALARY FROM EMPLOYEES;

Find highest salary.
SELECT max(SALARY) AS TOTAL_SALARY FROM EMPLOYEES;

Find lowest salary.
SELECT min(SALARY) AS TOTAL_SALARY FROM EMPLOYEES;

Find total employees count.
SELECT count(*) AS TOTAL_EMPs FROM EMPLOYEES;

Find average age of employees.
SELECT AVG(age) AS AVG_EMP_AGE FROM EMPLOYEES;

Find maximum age.
SELECT max(age) AS AVG_EMP_AGE FROM EMPLOYEES;

Find minimum age.
SELECT min(age) AS AVG_EMP_AGE FROM EMPLOYEES;

Find total salary of IT department employees.
SELECT SUM(SALARY) AS IT_DEPT_SALARY FROM EMPLOYEES WHERE DEPARTMENT = 'IT';

Find total employees whose salary is greater than 50000.
SELECT count(SALARY) AS SALARY_MORE_THAN_50K FROM EMPLOYEES WHERE SALARY > 50000;

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
SELECT CITY, COUNT(*) AS CITY_WISE_TOTAL_SALES FROM ORDERS GROUP BY CITY;

Find category wise total sales.
SELECT CATEGORY, COUNT(*) AS CITY_WISE_TOTAL_SALES FROM ORDERS GROUP BY CATEGORY;

Find month wise revenue.
SELECT ORDER_MONTH, SUM(AMOUNT) AS MONTHLY_REVENUE FROM ORDERS GROUP BY ORDER_MONTH;

Find city wise order count.
SELECT CITY, COUNT(*) AS TOTAL_ORDERS FROM ORDERS GROUP BY CITY;

Find category wise average order amount.
SELECT CATEGORY, AVG(AMOUNT) AS  AVE_ORD_AMT FROM ORDERS GROUP BY CATEGORY;

Find maximum sales amount category wise.
SELECT CATEGORY, MAX(AMOUNT) AS  AVE_ORD_AMT FROM ORDERS GROUP BY CATEGORY;

Find minimum order amount city wise.
SELECT CATEGORY, MIN(AMOUNT) AS  AVE_ORD_AMT FROM ORDERS GROUP BY CATEGORY;

Find customer wise total purchase amount.
SELECT CUSTOMER_NAME, SUM(AMOUNT) AS TOTAL_AMT_CUST_WISE FROM ORDERS GROUP BY CUSTOMER_NAME;

Find month wise average sales.
SELECT ORDER_MONTH, COUNT(*) AS TOTAL_SALES_MON_WISE FROM ORDERS GROUP BY ORDER_MONTH;

Find category wise order count.
SELECT CATEGORY, COUNT(*) AS TOTAL_ODR_CAT_WISE FROM ORDERS GROUP BY CATEGORY;

Find city wise maximum order amount.
SELECT CITY, MAX(AMOUNT) AS CITY_MAX_ORD FROM ORDERS GROUP BY CITY;

Find month wise minimum sales amount.
SELECT ORDER_MONTH, min(AMOUNT) AS MIN_SALES FROM ORDERS group by ORDER_MONTH;

Find customer wise total orders.
SELECT CUSTOMER_NAME, COUNT(*) AS CUST_WISE_ODR FROM ORDERS GROUP BY CUSTOMER_NAME;

Find city wise average order amount.
SELECT CITY, AVG(AMOUNT) AS AVG_CITY_WISE_SPEND FROM ORDERS GROUP BY CITY;

Find category wise minimum amount.
SELECT CATEGORY, MIN(AMOUNT) AS CAT_MIN_SPEND FROM ORDERS group by CATEGORY;

Find category wise maximum amount.
SELECT CATEGORY, MAX(AMOUNT) AS CAT_MAX_SPEND FROM ORDERS group by CATEGORY;

Find month wise total orders.
SELECT ORDER_MONTH, COUNT(*) AS TOTAL_MON_ODR FROM ORDERS group by ORDER_MONTH;

Find customer wise average purchase amount.
SELECT CUSTOMER_NAME, AVG(AMOUNT) AS AVG_AMT FROM ORDERS GROUP BY CUSTOMER_NAME;

Find city wise total customers.
SELECT CITY, COUNT(CUSTOMER_NAME) AS TOTAL_CLIENTS FROM ORDERS GROUP BY CITY;

Find category wise total revenue.
SELECT CATEGORY, SUM(AMOUNT) AS TOTAL_CAT_RVN FROM ORDERS GROUP BY CATEGORY;

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
SELECT DEPARTMENT, COUNT(*) AS TOTAL_SALES FROM SALES WHERE SALES_YEAR = 2025 GROUP BY DEPARTMENT;

Find region wise total sales where sales amount is greater than 40000.
SELECT REGION, COUNT(*) AS TOTAL_SALES FROM SALES WHERE SALES_AMOUNT > 40000 GROUP BY REGION;

Find department wise employee count where sales year is 2024.
SELECT DEPARTMENT, COUNT(*) AS TOTAL_EMP FROM SALES WHERE SALES_YEAR = 2024 GROUP BY DEPARTMENT;

Find region wise average sales where department is IT.
SELECT REGION, AVG(SALES_AMOUNT) AS AVG_SALES FROM SALES WHERE DEPARTMENT = 'IT' GROUP BY REGION;

Find department wise maximum sales where sales year is 2025.
SELECT DEPARTMENT, max(SALES_AMOUNT) FROM SALES WHERE SALES_YEAR = 2025 GROUP BY DEPARTMENT ;

Find region wise minimum sales where sales amount exceeds 35000.
SELECT REGION, MIN(SALES_AMOUNT) AS MIN_SALES_AMT FROM SALES WHERE SALES_AMOUNT > 35000 GROUP BY REGION;

Find employee count department wise where region is West.
SELECT DEPARTMENT, COUNT(*) AS TOTAL_EGN_EMP FROM SALES WHERE REGION = 'WEST' GROUP BY DEPARTMENT;

Find department wise total sales where department is Finance.
SELECT DEPARTMENT, SUM(SALES_AMOUNT) AS TOTAL_DEPT_SALES FROM SALES WHERE DEPARTMENT = 'FINANCE' GROUP BY DEPARTMENT;

Find region wise total sales where sales year is 2025.
SELECT REGION, SUM(SALES_AMOUNT) AS TOTAL_RGN_SALES FROM SALES WHERE  SALES_YEAR = 2025 GROUP BY REGION;

Find department wise average sales where sales amount is greater than 50000.
SELECT DEPARTMENT, AVG(SALES_AMOUNT) AS AVG_SALES_AMT FROM SALES WHERE SALES_AMOUNT > 50000 GROUP BY DEPARTMENT;

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
SELECT BRANCH_NAME, sum(AMOUNT) AS TOTAL_BR_AMT FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY BRANCH_NAME HAVING TOTAL_BR_AMT > 1;

Find city wise transaction count where account type is Savings and count exceeds 2.
SELECT CUSTOMER_CITY, COUNT(*) AS CITY_WISE_TOTAL_TXN FROM TRANSACTIONS WHERE ACCOUNT_TYPE = 'SAVINGS' GROUP BY CUSTOMER_CITY HAVING CITY_WISE_TOTAL_TXN > 2;

Find account type wise average amount where txn_year is 2025 and average amount exceeds 60000.
SELECT ACCOUNT_TYPE, AVG(AMOUNT) AS AC_WISE_TXN_AMT FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY ACCOUNT_TYPE HAVING AC_WISE_TXN_AMT > 60000;

Find branch wise maximum transaction where account type is Current and maximum amount exceeds 1 lakh.
SELECT BRANCH_NAME, MAX(AMOUNT) AS MAX_TXN_AMT FROM TRANSACTIONS WHERE ACCOUNT_TYPE = 'CURRENT' GROUP BY BRANCH_NAME HAVING MAX_TXN_AMT > 100000;

Find city wise total amount where txn_year is 2025 and total amount exceeds 2 lakhs.
SELECT CUSTOMER_CITY, SUM(AMOUNT) AS CITY_WISE_TOTAL FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY CUSTOMER_CITY HAVING CITY_WISE_TOTAL > 200000;

Find branch wise transaction count where amount is greater than 50000 and count exceeds 2.
SELECT BRANCH_NAME, COUNT(*) AS BR_WISE_TOTAL FROM TRANSACTIONS WHERE AMOUNT > 50000 GROUP BY BRANCH_NAME HAVING BR_WISE_TOTAL > 2;

Find account type wise total amount where txn_year is 2025 and total exceeds 3 lakhs.
SELECT ACCOUNT_TYPE, SUM(AMOUNT) AS AC_WISE_TOTAL_TXN FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY ACCOUNT_TYPE HAVING AC_WISE_TOTAL_TXN > 300000;

Find city wise minimum transaction where account type is Current and minimum amount exceeds 50000.
SELECT CUSTOMER_CITY, MIN(AMOUNT) AS MIN_TXN_CITY_WISE FROM TRANSACTIONS WHERE ACCOUNT_TYPE = 'CURRENT' GROUP BY CUSTOMER_CITY HAVING MIN_TXN_CITY_WISE > 50000;

Find branch wise average amount where txn_year is 2025 and average amount exceeds 70000.
SELECT BRANCH_NAME, AVG(AMOUNT) AS BR_WISE_AVF_AMT FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY BRANCH_NAME HAVING BR_WISE_AVF_AMT > 70000;

Find account type wise transaction count where txn_year is 2025 and count exceeds 3.
SELECT ACCOUNT_TYPE, COUNT(*) AS AC_WISE_TOTAL_TXN FROM TRANSACTIONS WHERE TXN_YEAR = 2025 GROUP BY ACCOUNT_TYPE HAVING AC_WISE_TOTAL_TXN > 3;