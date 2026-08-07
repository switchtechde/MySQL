from pyspark.sql.functions import *
from pyspark.sql import SparkSession

sparkSession = (SparkSession.builder
                .appName("Create DataFrame Demo")
                .master("local[*]")
                .getOrCreate())


employees = [
            (101, "John Christopher Anderson", "IT", 60000),
            (102, "Alice Johnson", "HR", 55000),
            (103, "Bob Smith", "Finance", 72000),
            (104, "David Wilson", "Sales", 50000),
            (105, "Emma Davis", "IT", 85000)
            ]

columns = [
            "employee_id",
            "employee_name",
            "department",
            "salary"
            ]

employee_df = sparkSession.createDataFrame(employees, columns)

employee_df.show()
employee_df.show(truncate=False)
employee_df.show(2)
employee_df.show(2, False)
employee_df.printSchema()


sparkSession.stop()