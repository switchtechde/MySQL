create table Student(
	Student_id int ,
    student_name varchar(30),
    Email varchar(100),
    DOB date,
    Gender varchar(10),
    Created_at timestamp
);

Select * from Student;



-- insert data  as Single Rows 
insert into Student(Student_id,student_name,Email,DOB,Gender,Created_at)
values(1,'Shreyash','shreyash@gmail.com','1995-05-05','M','2026-05-13 20:39:15');

-- insert data  as Multiple Rows 
insert into Student(Student_id,student_name,Email,DOB,Gender,Created_at)
values
(2,'Rohit','rohit@gmail.com','1995-07-07','M','2026-05-13 20:39:15'),
(3,'Divya','Divya@gmail.com','1995-08-08','F','2026-05-13 20:39:15'),
(4,'Snagita','sangita@gmail.com','1995-09-09','F','2026-05-13 20:39:15');

insert into Student(Student_id,student_name,Email,Gender,Created_at)
values(5,'Akshay','Akshay@gmail.com','M','2026-05-13 20:39:15');


create table Student_details(
	Student_id int ,
    student_name varchar(30),
    Email varchar(100),
    DOB date,
    Gender varchar(10),
    Created_at timestamp
);

Select * from Student_details;

Insert into Student_details(Student_id,student_name,Email,DOB,Gender,Created_at)
select Student_id,student_name,Email,DOB,Gender,Created_at  from Student;


insert into Student()
values(1,'Shreyash','shreyash@gmail.com','1995-05-05','M','2026-05-13 20:39:15');

insert into Student(Email,Gender,DOB,Student_id,student_name)
values(5,'Akshay','shreyash@gmail.com','M','2026-05-13 20:39:15');



-- 'Constraints ';

drop table Student_test;

create table Student_test(
	Student_id int not null,
    student_name varchar(30),
    Email varchar(100) not null unique,
    DOB date,
    Gender varchar(10),
    State varchar(20) default "maharastra",
    Created_at timestamp
);

select * from Student_test;

 


insert into Student_test(Student_id,student_name,Email,DOB,Gender,Created_at)
values(1,'Shreyash','shreyash@gmail.com','1995-05-05','M','2026-05-13 20:39:15');

insert into Student_test(Student_id,student_name,Email,DOB,Gender,Created_at)
values(2,'Shreyash','shreyash3@gmail.com','1995-05-05','M','2026-05-13 20:39:15');


insert into Student_test(Student_id,student_name,DOB,Gender,Created_at)
values(2,'Shreyash','1995-05-05','M','2026-05-13 20:39:15');


insert into Student_test(Student_id,student_name,DOB,Gender,Created_at)
values(3,'Shreyash','1995-05-05','M','2026-05-13 20:39:15');



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


insert into Student_test(Student_id,student_name,Email,DOB,Gender,Created_at)
values(5,'Shreyash','shreyash2@gmail.com','1995-05-05','M','2026-05-13 20:39:15');

insert into Student_test(student_name,Email,DOB,Gender,Created_at)
values('Shreyash','shreyash3@gmail.com','1995-05-05','M','2026-05-13 20:39:15');