from pyspark.sql import SparkSession
from pyspark.sql.functions  import *
from pyspark.sql.window import Window


spark = SparkSession.builder \
    .appName("MySQL Write Test") \
    .config("spark.jars", r"D:\JDBC\mysql-connector-j-9.7.0.jar") \
    .getOrCreate()

# -----------------------------
# READ FROM MYSQL
# -----------------------------

# read Entire data 
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/Raw_layer") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "transaction_details") \
    .option("user", "root") \
    .option("password", "123456") \
    .load()

#read Specific data instead of reading all data




print("Source Data:")

df.show()
print("Source Row Count:", df.count())

df2 = df.withColumn("rn", row_number().over(Window.partitionBy("transaction_id").orderBy("transaction_date")))

df3 = df2.filter(col("rn") == 1)

print("transformed_data_count:", df.count())

df4 = df3.drop("rn")

df4.show()

# -----------------------------
# WRITE TO NEW MYSQL TABLE
# -----------------------------

df4.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/transformed_layer") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "transaction_details") \
    .option("user", "root") \
    .option("password", "123456") \
    .option("batchsize", "1000") \
    .mode("append") \
    .save()

print("WRITE COMPLETED")

spark.stop()

# read data from CSV of dataset banking_dataset and write it to MYSQL in database raw_layer 
# read data from raw_layer and peraform data cleaning and write it to conform layer 

