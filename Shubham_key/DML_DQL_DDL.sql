Use transiction ;
Drop table Student_test;

create table Student_test(
	Student_id int auto_increment UNIQUE,
    student_name varchar(50) not null ,
    Email varchar(100) not null unique,
    DOB date not null ,
    Gender varchar(10) not null ,
    State varchar(20) default "maharastra",
    Created_at timestamp
);


SELECT * FROM Student_test;

insert into Student_test(student_name,Email,DOB,Gender,Created_at)
values('Shreyash','shreyash@gmail.com','1995-05-05','M','2026-05-13 20:39:15');


insert into Student_test(student_name,Email,DOB,Gender,Created_at)
values('Ankita','Ankita@gmail.com','1995-05-05','F','2026-05-13 20:39:15');

insert into Student_test(student_name,Email,DOB,Gender,Created_at)
values('Shreyash','shreyash6@gmail.com','1995-05-05','M','2026-05-13 20:39:15');


Alter Command 
1) to add new column ;

alter table Student_test 
add column age int Check (age > 18);

select * from Student_test;

2) To Modify new column 

Change col datatyoe from date to varchar of DOB ;

alter table Student_test 
Modify Column  DOB varchar(15) not null ;


Change DOb to date_of_Birth ;

Alter table Student_test 
Rename column DOB to date_of_Birth;

4) Drop an Col_name ;

Alter table Student_test 
Drop column age;

Alter table Student_test 
add constraint  unique	 (student_name);

-- Drop 

select * from Student_test;
Drop table Student_test;

create database test;

show databases;

drop database test;

truncate ;

create table Student_test(
	Student_id int auto_increment UNIQUE,
    student_name varchar(50) not null ,
    Email varchar(100) not null unique,
    DOB date not null ,
    Gender varchar(10) not null ,
    State varchar(20) default "maharastra",
    Created_at timestamp
);

truncate table Student_test;

select * from Student_detail;

rename table Student_test to Student_detail ;

Show databases;

use sys;
Select * from Student_test;

Delete from Student_test

Where student_id = 5;

Delete from Student_test;

Update Student_test
Set  gender  = "female"  
Where gender  = 'F';


Update Student_test
Set  gender  = "female" , State = 'Delhi'
Where gender  = 'F';

Update Student_test
Set  State  = 'delhi';


select student_name from Student_test;

select student_name as name from Student_test;