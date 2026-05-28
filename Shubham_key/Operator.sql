Create database Bank;

use Bank; 

CREATE TABLE employee_test (
    emp_id INT Unique Not Null,
    emp_name VARCHAR(50) Not Null,
    department VARCHAR(50) Not null,
    salary INT Not Null ,
    city VARCHAR(50) default 'Bangalore' ,
    experience INT 
);


INSERT INTO employee_test VALUES
(101, 'Rahul', 'IT', 55000, 'Pune', 3),
(102, 'Sneha', 'HR', 40000, 'Mumbai', 2),
(103, 'Amit', 'IT', 75000, 'Pune', 5),
(106, 'Neha', 'HR', 52000, 'Mumbai', 3),
(107, 'Vikas', 'Finance', 80000, 'Pune', 6),
(108, 'Pooja', 'IT', 30000, 'Delhi', 1);

Select * from employee_test Where Department = 'IT'; 

-- Arthematica Opertor 
Select 2+3 ; -- 5 
Select 5-3; -- 2
Select 5*2; -- 10
Select 8/2; -- 4
Select 7%2; -- 1

-- Create a new as Updated Salary Which Contain Add Of salary of 5000 each

Select * , (salary + 5000) as Updated_salary from employee_test;

-- Created a new col as Updated salary which should be less than 5000 of previous salary 
Select * , salary - 5000 as Updated_salary from employee_test;

-- Create a new column In which Exployee Should take 15% bonus Of their Salary 
Select * , (salary * 0.15) as bonus from employee_test;
 
-- Division 
Select * , Salary / 12 from employee_test;


-- Comparision Operator 

Select * from employee_test;

-- give me List Of Employee Whose salary is same as 55000

Select * from employee_test 
Where salary = 55000;


-- give me List Of Employee Whose salary is Greater  as 55000

Select * from employee_test 
Where salary > 55000;

-- give me List Of Employee Whose salary is Less  as 55000

Select * from employee_test 
Where salary < 55000;


-- give me List Of Employee Whose salary is Less  as 55000

Select * from employee_test 
Where salary <> 55000;
-- or
 
Select * from employee_test 
Where salary != 55000;

-- give me List Of Employee Whose salary is Less Than Equal to   as 55000

Select * from employee_test 
Where salary <= 55000;


-- give me List Of Employee Whose salary is Less Than Equal to   as 55000

Select * from employee_test 
Where salary >= 55000;

-- 
Select * from employee_test Where Department != 'IT'; 

-- 
Select * from employee_test Where Department <= 'IT'; 

-- Logical Operator 
Select * from employee_test ; 


-- Give me an Employee name Whose salary less than 50000 and they are belonging from IT department 

Select  * from employee_test 
Where salary < 50000  and department = 'IT';

-- Give me an Employee name Whose salary less than 50000 or  they are belonging from IT department 

Select  * from employee_test 
Where salary < 50000  or department = 'IT';


-- -- Give me an Employee name Whose salary less than 50000 and they are belonging from IT department  or They are belonging from Pue City 

Select * from employee_test 
Where salary < 50000 and department = 'IT' or City = 'Pune ';

Select * from employee_test 
Where (salary < 50000 and department ='IT') or City = 'Pune';

Select * from employee_test 
Where  department = 'IT' or City = 'Pune ' and Salary < 50000;


Select * from employee_test 
Where not (department = 'IT' and salary < 50000);


-- I need an Employee details who is Belonging from It or HR Department 
Select * from  employee_test 
Where salary In (40000,50000,55000,60000);

Select * from  employee_test 
Where salary between 40000 and 60000;

Select * from employee_test 
Where salary >= 40000 or  salary <=60000;

Select * from employee_test;

-- I need all that employee list Which are present In employee test 

Select * from employee_test 
Where emp_id  in (select emp_id from employee_test);

select emp_id from employee_test;