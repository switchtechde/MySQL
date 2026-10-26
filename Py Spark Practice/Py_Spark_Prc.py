from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, StructType, StructField, IntegerType, StringType, DateType, FloatType, DoubleType, BooleanType, TimestampType
from pyspark.sql.functions import *
from pyspark.sql import Window

#Creating Spark Session
sparkSession = (SparkSession.builder
                .appName("Employee ETL")
                .getOrCreate())

#Spark Session Configuration
'''(SparkSession.builder
.appName("Employee ETL")
.master("local[*]")
.config("spark.sql.shuffle.partitions", "8")
.config("spark.executor.memory", "2g")
.config("spark.driver.memory", "2g")
.getOrCreate())

#checking Spark Session creted successfully or not
print("Spark Session Created Successfully")

#Spark Session Information
print("Spark Version: ", sparkSession.version)
print("Spark Context: ", sparkSession.sparkContext)
print("Spark UI Web URL: ", sparkSession.sparkContext.uiWebUrl)
print("Spark Application ID: ", sparkSession.sparkContext.applicationId)
print("Spark Application Name: ", sparkSession.sparkContext.appName)
print("Spark Master: ", sparkSession.sparkContext.master)
print("Spark Default Parallelism: ", sparkSession.sparkContext.defaultParallelism)
print("Spark Default Min Partitions: ", sparkSession.sparkContext.defaultMinPartitions)
print("Spark Default Shuffle Partitions: ", sparkSession.sparkContext.getConf().get("spark.sql.shuffle.partitions"))

print("Application Name :", sparkSession.conf.get("spark.app.name"))
print("Master :", sparkSession.conf.get("spark.master"))
print("Shuffle Partitions :", sparkSession.conf.get("spark.sql.shuffle.partitions"))

print("Spark Session Type: ", type(sparkSession))
print("Spark Context Type: ", type(sparkSession.sparkContext))'''
#------------------------------------------------------------------------------------------------------------------

#Employee DataFrame Creation
'''employees = [(101, "John Christopher Anderson", "IT", 60000),
            (102, "Alice", "HR", 55000),
            (103, "Bob", "Finance", 72000),
            (104, "David", "Sales", 50000),
            (105, "Emma", "IT", 85000)]

columns = ["EmpID", "EmpName", "Dept", "Salary"]

#creating DataFrame from list of tuples and column names
emp_df = sparkSession.createDataFrame(employees, columns)
emp_df.show()
#emp_df.show(3)
#emp_df.show(2, truncate=False)
#emp_df.printSchema()'''

#Student DataFrame Creation
'''students = [(1, "Praddyumna Ramratan Baghe", 27, "Male", "Alandi"),
            (2, "Sumit Laxman Ghate", 30, "Male", "Wadmukhwadi"),
            (3, "Abhishek Satling Guddodagi", 27, "Male", "Chikhali")]

columns = ["Sr.No", "Name", "Age", "Gender", "City"]

#creating DataFrame from list of tuples and column names
stud_df = sparkSession.createDataFrame(students, columns)
stud_df.show(truncate = False)
stud_df.printSchema()'''
#-----------------------------------------------------------------------------------

#Importing Data from CSV file to DataFrame
'''employees_df = sparkSession.read.csv("D:\Coding\Switchtech\Repos\MySQL\Py Spark Practice\Files\Comapny_datafiles\employees.csv"
                                     ,header = True, inferSchema = True)

employees_df.show(2, truncate = False)
employees_df.printSchema()
print(employees_df.count())

departments_df = sparkSession.read.csv("D:\Coding\Switchtech\Repos\MySQL\Py Spark Practice\Files\Comapny_datafiles\departments.csv",
                                      header = True, inferSchema = True)
departments_df.show(2, truncate = False)
print(departments_df.count())
departments_df.printSchema()'''
#------------------------------------------------------------------------------------------------------------------

#Manually defining schema for employee DataFrame
'''employees_Schema = StructType([StructField("emp_id", IntegerType(), True),
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
                .schema(employees_Schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Comapny_datafiles\\employees.csv"))


#Manually defining schema for departments DataFrame
departments_Schema = StructType([StructField("dept_id", IntegerType(), True),
                    StructField("dept_name", StringType(), True),
                    StructField("location", StringType(), True),
                    StructField("annual_budget", FloatType(), True)])

departments_df = (sparkSession.read
                  .format("csv")
                  .option("header", "true")
                  .option("inferSchema", "true")
                  .schema(departments_Schema)
                  .load("D:/Coding/Switchtech/Repos/MySQL/Py Spark Practice/Files/Comapny_datafiles/departments.csv"))'''
#========================================================================================================================

#Customer Schema
customer_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("customer_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("age", DoubleType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("signup_date", DateType(), True),
    StructField("is_premium_member", BooleanType(), True)
])

customers_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(customer_schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Online_Shopping_datafiles\\customers.csv"))

#Order Schema
orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("order_date", TimestampType(), True),
    StructField("order_status", StringType(), True),
    StructField("payment_mode", StringType(), True),
    StructField("shipping_city", StringType(), True),
    StructField("shipping_state", StringType(), True),
    StructField("order_total", DoubleType(), True),
    StructField("discount_amount", DoubleType(), True),
    StructField("delivery_days", DoubleType(), True)
])

orders_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(orders_schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Online_Shopping_datafiles\\orders.csv"))

'''#Order Item Schema
order_items_schema = StructType([
    StructField("order_item_id", IntegerType(), False),
    StructField("order_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("quantity", IntegerType(), True),
    StructField("unit_price", DoubleType(), True),
    StructField("line_total", DoubleType(), True),
    StructField("item_status", StringType(), True)
])

order_items_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(order_items_schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Online_Shopping_datafiles\\order_items.csv"))

#Product Schema
products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("brand", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("discount_pct", IntegerType(), True),
    StructField("rating", DoubleType(), True),
    StructField("num_ratings", IntegerType(), True),
    StructField("stock_qty", IntegerType(), True)
])

products_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(products_schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Online_Shopping_datafiles\\products.csv"))

#Review Schema
reviews_schema = StructType([
    StructField("review_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("rating", IntegerType(), True),
    StructField("review_text", StringType(), True),
    StructField("review_date", DateType(), True),
    StructField("verified_purchase", BooleanType(), True)
])

reviews_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("inferSchema", "False")
                .schema(reviews_schema)
                .load("D:\\Coding\\Switchtech\\Repos\\MySQL\\Py Spark Practice\\Files\\Online_Shopping_datafiles\\reviews.csv"))
'''
#=====================================================================================================================

'''customers_df.show(2, truncate = False)
print(customers_df.count())
orders_df.show(2, truncate = False)
print(orders_df.count())
order_items_df.show(2, truncate = False)
print(order_items_df.count())
products_df.show(2, truncate = False)
print(products_df.count())
reviews_df.show(2, truncate = False)
print(reviews_df.count())'''
#--------------------------------------------------------------------------------------------

'''employees_df = (sparkSession.read
                .format("csv")
                .option("header", "true")
                .option("delimiter", ",")
                .option("inferSchema", "False")
                .schema(employee_Schema)
                .option("nullValue", "NULL")
                .load("D:\Coding\Switchtech\Repos\MySQL\Py Spark Practice\Files\Comapny_datafiles\employees.csv"))

employees_df.show(2, truncate = False)
#employees_df.show(100)
print(employees_df.count())
#employees_df.printSchema()'''
#------------------------------------------------------------------------------------------------------------------

'''departments_df.show(2, truncate = False)
print(departments_df.count())
departments_df.printSchema()'''
#-----------------------------------------------------------------------------------------------------------------
#Select Query
#employees_df.select("emp_id", "emp_name", "email", "gender", "city", "dept_id", "salary").show(100, truncate = False)

'''employees_df.select(
            col("emp_id"),
            col("emp_name"),
            col("email"),
            col("gender"),
            col("city"),
            col("dept_id"),
            col("salary"),
            (col("salary") * 12).alias("annual_salary")).show(10, truncate = False)

employees_report = employees_df.select(
                    col("emp_id"),
                    col("emp_name").alias("name"),
                    col("city"),
                    (col("salary") * 12).alias("Annual_Salary"))

employees_report.show(10, truncate = False)'''
#---------------------------------------------------------------------------------------------

'''employees_df.selectExpr(
"""
emp_id,
emp_name,
city,
salary * 12 AS Annual_Salary
""").show(10)'''

#----------------------------------------------------------------------------------------------

#Filtering Data
'''employees_df.filter(
    col("salary") > 5000).show(3, truncate = False)

employees_df.where(
    col("city") == "Pune").show(3, truncate = False)

emp_trnasf = employees_df.filter(
    (col("city") == "Pune") &
    (col("salary") > 50000) &
    (col("gender") == "Male"))

emp_trnasf.show(5, truncate = False)
print(emp_trnasf.count())

emp_transf2 = employees_df.filter(
    (col("city") == "Pune") &
    (col("gender") == "Female") |
    (col("age") > 30))

emp_transf2.show(5, truncate = False)
print(emp_transf2.count())

emp_transf3 = employees_df.where(
    ~(col("city") == "Mumbai") &
    ~(col("gender") == "Male"))

emp_transf3.show(5, truncate = False)
print(emp_transf3.count())

emp_transf4 = employees_df.filter(
    col("city").isin("Pune", "Mumbai"))

emp_transf4.show(5, truncate = False)
print(emp_transf4.count())

emp_like = employees_df.where(
    (col("emp_name").startswith("P")) &
    (col("emp_name").endswith("a")) &
    (col("emp_name").contains("sh")))

emp_like.show(5, truncate = False)
print(emp_like.count())

emp_btw = employees_df.filter(
    (col("salary").between(50000, 75000)) &
    (col("rating").between(4,5))
)

emp_btw.show(5, truncate= False)
print(emp_btw.count())

emp_null_notNull = employees_df.filter(
    (col("city").isNotNull())
)

emp_null_notNull.show(5, truncate= False)
print(emp_null_notNull.count())

emp_null = employees_df.where(
    (col("email").isNull()))

emp_null.show(5, truncate= False)
print("Total Blank Emails : ", emp_null.count())

emp_date_Ftr = employees_df.filter(
    (col("joining_date") > "2025-12-31"))

emp_date_Ftr.show()
print(emp_date_Ftr.count())


emp_date_90 = employees_df.filter(
    (col("joining_date") >= date_sub(current_date(), 90)))


emp_date_90.show()
print(emp_date_90.count())'''

#Simple Task
'''emp_report = employees_df.select(
    "emp_name", "dept_id","salary", "city", "joining_date").filter(
        (col("dept_id") == 1) &
        (col("salary") >= 70000) &
        (col("city") == "Pune") &
        (col("joining_date") > "2020-12-31"))

emp_report.show()
print("Employee Report 1 : ", emp_report.count())

emp_report2 = employees_df.select(
    "emp_name", "dept_id","salary", "city", "joining_date").where(
        (col("dept_id").isin(1)) &
        (col("salary") >= 70000) &
        (col("city") == "Pune") &
        (col("joining_date").between("2020-12-31", current_date()))
    )

emp_report2.show()
print("Employee Report 2 : ", emp_report2.count())'''

#------------------------------------------------------------------------------------------
#With Column

'''employees_df = employees_df.select(
    "emp_name", "dept_id","salary", "city", "joining_date").withColumn(
        "Annual Salary", (col("salary") * 12))

employees_df.show(5, truncate = False)
print("Count : ", employees_df.count())

employees_df = employees_df.select(
    "emp_name", "dept_id", "salary", "city", "joining_date").withColumn(
        "Annual_Salary", (col("salary") * 12)).filter(
            (col("dept_id").isin(1,3)))

employees_df.show(truncate = False)
print("Total Employees  : ", employees_df.count())

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "Annual_salary", (col("salary") * 12)).filter(
            (col("salary") * 1.10).isNotNull() &
            (col("joining_date").between(current_date() - 90, current_date())))

employees_df.show(truncate = False)
print("Total Employees : ", employees_df.count())


employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "company", lit("Switchtech Pvt Ltd"))

employees_df.show()

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "emp_name", upper(col("emp_name")))

employees_df.show()

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "emp_name", upper(col("emp_name"))).withColumn("emp_name", trim(col("emp_name")))

employees_df.show(truncate = False)

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "email_length", length(col("email"))).filter(col("email").isNotNull())

employees_df.show()
print("Total EMployees : ",employees_df.count())

employees_df = employees_df.select(
        "emp_name", "email", "dept_id", "salary", "city", "joining_date"
    ).withColumn(
        "emp_city", concat_ws("-", col("emp_name"), col("city"))
    ).withColumn(
        "emp_city", trim(col("emp_city"))
    ).withColumn(
        "emp_city_len", length(col("emp_city"))
    ).withColumn(
        "email_length", length(col("email"))
    ).where(col("city").isNotNull())

employees_df.show(truncate = False)
print("Total Emps : ", employees_df.count())


employees_df = employees_df.select(
        "emp_name", "email", "dept_id", "salary", "city", "joining_date"
    ).withColumn(
        "Joining_year", year(col("joining_date"))
    ).withColumn(
        "Joining_month", month(col("joining_date"))
    ).withColumn(
        "joining_day", day(col("joining_date"))
    ).where(col("joining_date").between("2022-12-31", current_date()))

employees_df.show()
print("Total Emp : ", employees_df.count())

employees_df = employees_df.select(
        "emp_name", "email", "dept_id", "salary", "city", "joining_date"
    ).withColumn(
        "Salary_Cat", when(
            col("salary") >= 80000, "High").when(
                col("salary") >= 50000, "Moderate").when(
                    col("salary").isNull(), "Intern").otherwise(
                        "Low"))

employees_df.show()
print("count", employees_df.count())'''

#Employees Report
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
    "Employee_Display", concat_ws(" - ", col("emp_name"), col("City"))
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
).orderBy(col("salary").desc())

Filtered_employees_df.show(10, truncate = False)
print("Total Filtered Records : ", Filtered_employees_df.count())'''
#-------------------------------------------------------------------------------------------------------
#Order By, Sort

'''employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
        col("salary").isNotNull()).orderBy(
            col("salary").desc())

employees_df.show(100, truncate = False)
print("Total Emps : ", employees_df.count())

employees_df1 = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
        col("salary").isNotNull()).sort(
            col("salary").desc())

employees_df1.show()
print("Total Emps1 : ", employees_df1.count())

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
        col("salary").isNotNull()).sort(
            col("dept_id").asc(),
            col("salary").desc())

employees_df.show(truncate= False)

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").withColumn(
        "Annual_Salary", col("salary") * 12).filter(
            col("salary").isNotNull()).sort(
                col("dept_id").asc(),
                col("Annual_Salary").desc())

employees_df.show()

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
            col("salary").isNotNull()).sort(
                col("joining_date").desc())

employees_df.show()

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
         col("salary").isNotNull()).orderBy(
             col("salary").asc_nulls_first())

employees_df.show()

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
        col("salary").isNotNull()).orderBy(
            col("salary").asc_nulls_last())

employees_df.show(5, truncate = False)

employees_df = employees_df.select(
    "emp_name", "email", "dept_id", "salary", "city", "joining_date").filter(
        col("salary").isNotNull()).orderBy(
            col("salary").desc()).limit(5)

employees_df.show(truncate= False)'''
#-------------------------------------------------------------------------------------------------
#Distinct, dropDuplicates()

'''employees_df1 = employees_df.distinct()

#employees_df1.show()
print("total",employees_df1.count())

employees_df2 = employees_df.dropDuplicates()

#employees_df2.show()
print("total2", employees_df2.count())

employees_df = employees_df.dropDuplicates(["emp_id"])
employees_df.show()
print("total", employees_df.count())

employees_df = employees_df.groupBy("emp_id").count().filter(col("count") > 1 )

employees_df.show()
print("total", employees_df.count())'''
#------------------------------------------------------------------------------------------------

#aggregation

'''employees_df = employees_df.groupBy("dept_id").count().orderBy(col("dept_id").asc())
employees_df = employees_df.groupBy("dept_id").count().orderBy(col("count").desc())

employees_df.show()

employees_df.groupBy("dept_id").agg(count("salary")).show()
employees_df.groupBy("dept_id").agg(sum("salary")).show()
employees_df.groupBy("dept_id").agg(avg("salary")).show()
employees_df.groupBy("dept_id").agg(max("salary")).show()
employees_df.groupBy("dept_id").agg(min("salary")).show()


employees_df = employees_df.groupBy("dept_id").agg(
    count("*"), sum("salary"), avg("salary"), max("salary"), min("salary")).show()

employees_df = employees_df.groupBy("dept_id").agg(
   count("*").alias("total emp"), sum("salary").alias("total sal"),avg("salary").alias("avg sal"), max("salary").alias("highest sal"), min("salary").alias("lowest sal")).show()

employees_df = employees_df.groupBy("dept_id", "city").agg(
    count("*"), sum("salary"), avg("salary"), max("salary"), min("salary")).show()


employees_df = employees_df.groupBy("dept_id").agg(
    avg("salary").alias("Avg_Sal")).filter(col("Avg_Sal") > 50000).show()

employees_df = employees_df.groupBy("city").agg(
    avg("salary").alias("city_avg_sal")).filter(col("city_avg_sal") < 80000).show()

employees_df = employees_df.groupBy("dept_id").agg(
    sum("salary").alias("highest_salary_dept")).orderBy(col("highest_salary_dept").desc()).show()'''
#-----------------------------------------------------------------------------------------------------

#Joins
#employees_df.join(departments_df, "dept_id", "inner").show()

#employees_df.join(departments_df, employees_df.dept_id == departments_df.dept_id, "inner").show()

#InnerJoin 
'''emp_inr_jn = employees_df.alias("e").select(
                    "emp_id", "emp_name", "salary", "dept_id").join(
                        departments_df.alias("d").select(
                            "dept_id", "dept_name", "annual_budget"),col("e.dept_id") == col("d.dept_id"),"inner")
                            
emp_inr_jn.show()
print(emp_inr_jn.count())'''

#Left Join
'''emp_lft_jn = employees_df.alias("e").select(
                "emp_id", "emp_name", "salary", "dept_id", "city").join(
                    departments_df.alias("d").select(
                        "dept_id", "dept_name", "annual_budget"), col("e.dept_id") == col("d.dept_id"), "left")

emp_lft_jn.show()
print(emp_lft_jn.count())'''

#Right Join
'''emp_rgt_jn = employees_df.alias("e").select(
    "emp_id", "emp_name", "city", "dept_id", "salary").join(
    departments_df.alias("d").select(
        "dept_id", "dept_name", "annual_budget"), col("e.dept_id") == col("d.dept_id"), "right")

emp_rgt_jn.show()
print(emp_rgt_jn.count())'''


#Full Outer Join
'''emp_fl_otr_jn = employees_df.alias("e").select(
    "emp_id", "emp_name", "city", "dept_id", "email","salary").join(
        departments_df.alias("d").select(
            "dept_id", "dept_name"), col("e.dept_id") == col("d.dept_id"), "outer").filter(
                col("e.email").isNotNull() &
                col("e.salary").isNotNull()).orderBy(
                    col("e.salary").desc())

emp_fl_otr_jn.show(truncate = False)
print(emp_fl_otr_jn.count())'''
#----------------------------------------------------------------------------------------------

#Date & Timestamp

'''employees_df = employees_df.withColumn("joining_date", to_date(col("joining_date")))

employees_df.printSchema()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "city", "salary", "joining_date"
).withColumn(
    "Joining_Year", year(col("joining_date")))

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "city", "salary", "Joining_date"
).withColumn(
    "Joining_Year", year(col("joining_date"))
).withColumn(
    "Joining_Month", month(col("joining_date")))

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "city", "salary", "joining_date"
).withColumn(
    "Joining_Year", year(col("joining_date"))
).withColumn(
    "Joining_Month", month(col("joining_date"))
).withColumn(
    "Joining_Day", dayofmonth(col("joining_date"))
)

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "joining_year", year(col("joining_date"))
).withColumn(
    "joining_month", month(col("joining_date"))
).withColumn(
    "joining_day", day(col("joining_date"))
).withColumn(
    "processing_date", current_date()
).filter(
    (col("salary").isNotNull()) &
    (col("email").isNotNull()) &
    (col("salary") > 0)
).orderBy(
    col("salary").desc(),
    col("joining_date").asc()
)

employees_df.show()
print("Count : ", employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "joining_year", year(col("joining_date"))
).withColumn(
    "processing_date", current_date()
).withColumn(
    "processing_datetime", current_timestamp()
).filter(
    (col("salary") > 0) &
    (col("salary").isNotNull()) &
    (col("email").isNotNull())
)

employees_df.show()
print("count : ", employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "days_since_join", date_diff(current_date(), col("joining_date"))
)

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "probation_end_date", date_add(col("joining_date"), 180)
).orderBy(
    col("emp_id").asc()
)

employees_df.show()
print("count : ", employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "previous_date", date_sub(col("joining_date"), 30)
).orderBy(
    col("emp_id").asc()
)

employees_df.show()
print("count : ", employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "formatted_date", date_format(col("joining_date"), "dd-MMM-yy")
)

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).withColumn(
    "employee_experience", floor(date_diff(current_date(), col("joining_date")) / 365)
).filter(
    col("employee_experience") >= 3
)

employees_df.show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).filter(col("joining_date") > "2026-01-01")

employees_df.show()
print("total employees : ", employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).filter(
    col("joining_date") >= date_sub(current_date(), 30)
)

employees_df.show()
print(employees_df.count())'''
#------------------------------------------------------------------------------------------------------------

#Handling NULL val's

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).filter(
    col("salary").isNull()
)

employees_df.show()
print(employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "city", "salary", "joining_date"
).filter(
    col("email").isNull()
)

employees_df.show()
print(employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "city"
).filter(
    col("city").isNull()
)

print(employees_df.count())'''

'''employees_df = employees_df.select(
    count(when(col("email").isNull(), True)).alias("missing_email"), 
    count(when(col("salary").isNull(), True)).alias("missing_salary"),
    count(when(col("city").isNull(), True)).alias("missing_city")
)

employees_df.show()'''

'''employees_df = employees_df.fillna("unknown")

employees_df.show()'''

'''employees_df.fillna(
    {
        "salary" : 0,
        "is_active" : 0,
        "email" : "Yet to be Generated",
        "rating" : 0
    }
).show()'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "email", "salary", "is_active"
).withColumn(
    "email", coalesce(col("email"), lit("unknown"))
).withColumn(
    "is_active", coalesce(col("is_active"), lit(0))
)

employees_df.show()'''

'''employees_df = employees_df.dropna()
print(employees_df.count())'''

'''employees_df = employees_df.dropna(
    subset = [
        "email"
    ]
)

print(employees_df.count())'''


'''employees_df = employees_df.dropna(
    #how = "all",
    how = "any",
    subset = [
        "email",
        "salary"
    ]
)
print(employees_df.count())'''

'''employees_df = employees_df.select(
    "emp_id", "emp_name", "salary"
).withColumn(
    "salart_status", 
    when(
        col("salary").isNull(), "Missing"
    ).otherwise(
        "Available"))

employees_df.show(100)'''

'''employees_df = employees_df.filter(col("email") == "").show()
print(employees_df.count())'''

'''employees_df = employees_df.withColumn(
    "email", 
    when(col("city") == "", None)
    .otherwise(col("city")))'''
#--------------------------------------------------------------------------------------------------------------------------

#Window_function

'''customers_df.show(2, truncate = False)
print(customers_df.count())
orders_df.show(2, truncate = False)
print(orders_df.count())
order_items_df.show(2, truncate = False)
print(order_items_df.count())
products_df.show(2, truncate = False)
print(products_df.count())
reviews_df.show(2, truncate = False)
print(reviews_df.count())'''


#cust_order_df = customers_df.alias("c").join(orders_df.alias("o"), col("c.customer_id") == col("o.customer_id"), "inner")

'''cust_order_df.show()
print(cust_order_df.count())'''

#Row Number
'''rn_window_spec = Window.partitionBy("c.customer_id").orderBy("o.order_date")

sales_df = cust_order_df.withColumn(
    "row_number", row_number().over(rn_window_spec)
).filter(
    col("row_number") == 1
)

sales_df.show()'''

#Rank
'''r_window_spec = Window.orderBy(col("o.order_total").desc())

sales_df = cust_order_df.withColumn(
    "rank", rank().over(r_window_spec)
)

sales_df.show()'''

#Dense Rank
'''dr_window_spec = Window.orderBy(col("o.order_total").desc())

sales_df = cust_order_df.withColumn(
    "dense_rank", dense_rank().over(dr_window_spec)
)

sales_df.show()'''

#Example
'''window_spec = Window.partitionBy("c.customer_id").orderBy(col("o.order_total").desc())

result = cust_order_df.withColumn(
    "rank", rank().over(window_spec)
)

result.filter(
    col("rank") <=2
).show()

print(result.count())'''

#Lag
'''lag_window_spec = Window.partitionBy("c.customer_id").orderBy("o.order_date")

sales_df = cust_order_df.withColumn(
    "previous_amount", lag("o.order_total").over(lag_window_spec)
)

sales_df.show()'''

#Lead
'''lead_window_spec = Window.partitionBy("c.customer_id").orderBy("o.order_date")

sales_df = cust_order_df.withColumn(
    "next_amount", lead("o.order_total").over(lead_window_spec)
)

sales_df.show()'''

#Running Total
'''rt_window_spec = Window.partitionBy("c.customer_id").orderBy("o.order_date").rowsBetween(
    Window.unboundedPreceding, Window.currentRow)

sales_df = cust_order_df.withColumn(
"running_total", sum("o.order_total").over(rt_window_spec)
)

sales_df.show()'''

#Moving Average
'''mvag_window_spec = Window.partitionBy("c.customer_id").orderBy("o.order_date").rowsBetween(
    -2, 0
)

sales_df = cust_order_df.withColumn(
    "moving_average", avg("o.order_total").over(mvag_window_spec)
)

sales_df.show()'''
#=====================================================================================================================

#Data Write
cust_order_df = customers_df.alias("c").join(orders_df.alias("o"), col("c.customer_id") == col("o.customer_id"), "inner")


cust_order_df.show()
print(cust_order_df.count())

# Write to local CSV folder
cust_order_df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(r"D:\Coding\Switchtech\Repos\MySQL\Py Spark Practice\Files\Output_Files\PySpark_Files\CSV\customer_orders")

print("COmpleted code")













#Closing Spark Session
#sparkSession.stop()
