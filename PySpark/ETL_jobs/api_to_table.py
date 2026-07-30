import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Create Spark Session
spark = SparkSession.builder \
    .appName("API_to_MySQL") \
    .getOrCreate()

# API URL
api_url = "https://jsonplaceholder.typicode.com/users"

# Fetch data from API
response = requests.get(api_url)

# Check API response
if response.status_code == 200:
    json_data = response.json()
else:
    raise Exception(f"API Failed with Status Code: {response.status_code}")

# Convert JSON to DataFrame
df = spark.createDataFrame(json_data)

# Add ETL Timestamp
df = df.withColumn("inserted_datetime", current_timestamp())

# Show Data
df.show(truncate=False)