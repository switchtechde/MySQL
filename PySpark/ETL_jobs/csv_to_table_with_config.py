import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions  import *
from datetime import datetime

spark = SparkSession.builder \
    .appName("MySQL Write Test") \
    .config("spark.jars", r"D:\JDBC\mysql-connector-j-9.7.0.jar") \
    .getOrCreate()

current_date = datetime.now().strftime("%Y%m%d")

Folder_path = r"C:\Users\joshi\OneDrive\Desktop\SQL\Banking_dataset\transactions_"
transaction_df = spark.read.csv(f"{Folder_path}{current_date}.csv", header=True)

print("data read from source Location")
transaction_df2 = transaction_df.withColumn("Inserted_date", current_date())
print("added new col")
transaction_df2.show()

transaction_df2.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/Raw_layer") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "transaction_details") \
    .option("user", "root") \
    .option("password", "123456") \
    .option("batchsize", "1000") \
    .mode("append") \
    .save()

print("WRITE COMPLETED")

spark.stop()