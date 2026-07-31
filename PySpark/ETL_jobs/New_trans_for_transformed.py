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

#read data from Raw_layer_table
raw_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/Raw_layer") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "transaction_details") \
    .option("user", "root") \
    .option("password", "123456") \
    .load()

raw_df.show()

#read data from Transformed_layer_table 
trans_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/transformed_layer") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "transaction_details") \
    .option("user", "root") \
    .option("password", "123456") \
    .load()

trans_df.show()

#read Specific data instead of reading all data

print("raw Count:", raw_df.count())

print("transformed Count:", trans_df.count())

Old_id_df = trans_df.select("transaction_id")

print("trans_id Count:", Old_id_df.count())

#Filtering only Those records Which are Not loaded 
Load_df = raw_df.join(Old_id_df, raw_df.transaction_id == Old_id_df.transaction_id, "left_anti")

Load_df.show()

print("load_DF Count:", Load_df.count())
#left Semi -It will give those Records Which aare matching with left and right dataframe and give Only those Column of Left dataframe 
#left Anti - It will give Only those records Which are not matching with left and right dataframe and give Only those Column of Left dataframe
Load_df.write \
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

