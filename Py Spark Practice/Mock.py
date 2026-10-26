from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, StructType, StructField, IntegerType, StringType, DateType, FloatType
from pyspark.sql.functions import *

#Creating Spark Session
sparkSession = (SparkSession.builder
                .appName("Employee ETL")
                .getOrCreate())


#Manually defining schema for employee DataFrame
employee_Schema = StructType([StructField("emp_id", IntegerType(), True),
                    StructField("emp_name", StringType(), True),
                    StructField("email", StringType(), True),
                    StructField("gender", StringType(), True),
                    StructField("age", IntegerType(), True),
                    StructField("phone", StringType(), True),
                    StructField("city", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("address_street", StringType(), True),
                    StructField("address_pincode", StringType(), True),
                    StructField("dept_id", IntegerType(), True),
                    StructField("designation", StringType(), True),
                    StructField("salary", FloatType(), True),
                    StructField("bonus", FloatType(), True),
                    StructField("experience_years", IntegerType(), True),
                    StructField("rating", FloatType(), True),
                    StructField("manager_id", IntegerType(), True),
                    StructField("is_active", IntegerType(), True),
                    StructField("joining_date", DateType(), True),
                    StructField("login_timestamp", DateType(), True),
                    StructField("skills", StringType(), True)])

employees_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(employee_Schema)
                .load("D:\Coding\Switchtech\Repos\MySQL\Py Spark Practice\Files\Comapny_datafiles\employees.csv"))

#--------------------------------------------------------

'''employees_df.show(5, truncate = False)
print("Total EMployees : ", employees_df.count())'''

'''employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "dept_id").show(5, truncate= False)

employees_df1 = employees_df.selectExpr("""emp_id,emp_name,salary * 12 AS Annual_Salary""")

#------------------------------------

employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "dept_id").filter(
        col("salary") > 5000).show(5, truncate = False)'''

'''Filtered_employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date"
).withColumn(
    "Annual_Salary", col("salary") * 12
).withColumn(
    "Salary_Cat",when(col("salary") > 80001, "Grade A")
                .when(col("salary") > 50001, "Grade B")
                .when(col("salary") > 30001, "Grade C")
                .otherwise("Low")
).withColumn(
    "Employee_Display", concat(col("emp_name"), lit(" - "), col("City"), lit(" , ") ,col("salary"))
).withColumn(
    "email", upper(col("email"))
).withColumn(
    "emp_name", trim(col("emp_name"))
).withColumn(
    "Joining_year", year(col("joining_date"))
).withColumn(
    "Employee_Display", trim(col("Employee_Display"))
).filter(
    (col("email").isNotNull()) &
    (col("joining_date") >= date_sub(current_date(), 500))
).orderBy(col("salary").desc(), col("city").asc())

Filtered_employees_df.show(10, truncate = False)
print("Total Filtered Records : ", Filtered_employees_df.count())'''


#Find employees whose salary is greater than 70000.
'''employees_ftr_df = employees_df.select(
    "emp_id", "emp_name", "email", "dept_id", "salary", "city", "joining_date"
).filter(
    col("salary") > 70000
)

employees_ftr_df.show()
print("count: ", employees_ftr_df.count())'''

#Find employees who work in the IT department.
'''employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date"
).filter(
    col("dept_id") == 2
).show()'''

#Find employees who live in Pune.
'''employees_df = employees_df.select(
    "emp_id", "emp_name","city"
).filter(col("city") == "pune")

employees_df.show()
print("count: ", employees_df.count())'''

#Find employees whose experience is greater than 5 years.
employees_df = employees_df.select(
    "emp_id","emp_name", "email", "joining_date"
).withColumn(
    "experience", floor(date_diff(current_date(), col("joining_date")) / 365)
).where(
    col("experience") > 5
)

employees_df.show(truncate = False)
print("count : ",employees_df.count())

#Find employees whose salary is exactly 60000.
'''employees_df.select(
    "emp_id", "emp_name", "salary"
).filter(
col("salary").between(50000, 60000)
).show()'''

#Find employees who work in the HR department and live in Mumbai.\
employees_df = employees_df.select(
    "emp_id", "emp_name", "dept_id"
).where(
    (col("city") == "Mumbai") &
    (col("dept_id") == 3)
)
employees_df.show(truncate = False)
print("count : ",employees_df.count())
sparkSession.stop()