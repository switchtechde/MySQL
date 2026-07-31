import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions  import *
from datetime import datetime
import json

spark = SparkSession.builder \
    .appName("MySQL Write Test") \
    .config("spark.jars", r"D:\JDBC\mysql-connector-j-9.7.0.jar") \
    .getOrCreate()

with open('config.json') as config_file:
    config=json.load(config_file)

current_date = datetime.now().strftime("%Y%m%d")

transaction_df = spark.read.csv(f"{config['Folder_path']}{current_date}.csv", header=True)

print("data read from source Location")
transaction_df2 = transaction_df.withColumn("Inserted_date", current_date())
print("added new col")
transaction_df2.show()

transaction_df2.write \
    .format("jdbc") \
    .option("url", config['raw_jdbc_url']) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", config['raw_table_name']) \
    .option("user",config['jdbc_user'] ) \
    .option("password", config['jdbc_password']) \
    .option("batchsize", "1000") \
    .mode("append") \
    .save()

print("WRITE COMPLETED")

spark.stop()