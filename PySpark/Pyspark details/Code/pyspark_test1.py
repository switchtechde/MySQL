from pyspark.sql import SparkSession
from pyspark.sql.functions  import *

spark = SparkSession.builder \
    .appName("MySQL Write Test") \
    .config("spark.jars", r"D:\JDBC\mysql-connector-j-9.7.0.jar") \
    .getOrCreate()

# -----------------------------
# READ FROM MYSQL
# -----------------------------

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/student") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "student_test") \
    .option("user", "root") \
    .option("password", "123456") \
    .load()

print("Source Data:")
df.show()

print("Source Row Count:", df.count())

print("applying transformation ")

df2 =df.filter(col("age") > 23)
print("Source Row Count:", df2.count())

# -----------------------------
# WRITE TO NEW MYSQL TABLE
# -----------------------------

df2.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/student") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "student_write_test_3") \
    .option("user", "root") \
    .option("password", "123456") \
    .option("batchsize", "1000") \
    .mode("append") \
    .save()

print("WRITE COMPLETED")

spark.stop()

# read data from CSV of dataset banking_dataset and write it to MYSQL in database raw_layer 
# read data from raw_layer and peraform data cleaning and write it to conform layer 

