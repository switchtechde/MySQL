from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("JDBC_Test")
    .config(
        "spark.driver.extraClassPath",
        "D:/Coding/Switchtech/spark/jars/mysql-connector-j-9.7.0.jar"
    )
    .getOrCreate()
)

jdbc_url = (
    "jdbc:mysql://localhost:3306/dataengineeringpractice"
    "?useSSL=false"
    "&allowPublicKeyRetrieval=true"
    "&serverTimezone=UTC"
)

spark._jvm.java.lang.Class.forName(
    "com.mysql.cj.jdbc.Driver"
)

conn = spark._jvm.java.sql.DriverManager.getConnection(
    jdbc_url,
    "root",
    "Pixel@9792"
)

print("JDBC Connection Successful")

conn.close()
spark.stop()