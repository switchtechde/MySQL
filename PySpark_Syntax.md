# PySpark Syntax Reference

## Contents

1. PySpark Setup
2. SparkSession
3. Spark Data Types
4. DataFrame Creation
5. Reading Data
6. Writing Data
7. Inspecting DataFrames
8. Selecting and Filtering
9. Column Expressions
10. Aggregations and Grouping
11. Joins
12. Window Functions
13. DataFrame Transformations
14. Actions
15. SQL Queries
16. UDFs and Pandas UDFs
17. Partitioning and Caching
18. Performance and Tuning
19. Common Functions
20. Debugging and Metadata
21. Notes

---

## 1. PySpark Setup

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('MyApp') \
    .master('local[*]') \
    .config('spark.sql.shuffle.partitions', '8') \
    .getOrCreate()
```

Stop Spark:

```python
spark.stop()
```

Set a configuration dynamically:

```python
spark.conf.set('spark.sql.adaptive.enabled', True)
```

---

## 2. SparkSession

A `SparkSession` is the entry point for Spark SQL and DataFrame APIs.

```python
spark = SparkSession.builder \
    .appName('Example') \
    .config('spark.driver.memory', '2g') \
    .config('spark.executor.memory', '4g') \
    .getOrCreate()
```

Create or replace a temporary view:

```python
df.createOrReplaceTempView('employees')
```

Create a global temporary view:

```python
df.createGlobalTempView('employees_global')
```

---

## 3. Spark Data Types

Common Spark SQL data types:

- `StringType()`
- `IntegerType()`
- `LongType()`
- `FloatType()`
- `DoubleType()`
- `DecimalType(precision, scale)`
- `BooleanType()`
- `DateType()`
- `TimestampType()`
- `ArrayType(elementType)`
- `MapType(keyType, valueType)`
- `StructType([StructField(...)])`

Example schema:

```python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, DecimalType

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
    StructField('salary', DecimalType(10, 2), True),
    StructField('hire_date', DateType(), True)
])
```

---

## 4. DataFrame Creation

Create from a list of tuples:

```python
data = [(1, 'Alice', 65000), (2, 'Bob', 55000)]
df = spark.createDataFrame(data, ['id', 'name', 'salary'])
```

Create from `Row` objects:

```python
from pyspark.sql import Row

rows = [Row(id=1, name='Alice', salary=65000), Row(id=2, name='Bob', salary=55000)]
df = spark.createDataFrame(rows)
```

Create from RDD:

```python
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(['id', 'name', 'salary'])
```

Create with explicit schema:

```python
df = spark.createDataFrame(data, schema=schema)
```

---

## 5. Reading Data

CSV:

```python
df = spark.read.csv('data.csv', header=True, inferSchema=True)
```

CSV with options:

```python
df = spark.read.format('csv') \
    .option('header', True) \
    .option('inferSchema', True) \
    .option('sep', ',') \
    .option('nullValue', '') \
    .load('data.csv')
```

JSON:

```python
df = spark.read.json('data.json')
```

Parquet:

```python
df = spark.read.parquet('data.parquet')
```

ORC:

```python
df = spark.read.orc('data.orc')
```

JDBC:

```python
df = spark.read.format('jdbc') \
    .option('url', 'jdbc:mysql://localhost:3306/dbname') \
    .option('dbtable', 'employees') \
    .option('user', 'root') \
    .option('password', 'password') \
    .load()
```

---

## 6. Writing Data

Write CSV:

```python
df.write.mode('overwrite').csv('output.csv')
```

CSV with options:

```python
df.write.format('csv') \
    .option('header', True) \
    .option('sep', ',') \
    .mode('overwrite') \
    .save('output.csv')
```

Write Parquet:

```python
df.write.mode('overwrite').parquet('output.parquet')
```

Write ORC:

```python
df.write.mode('overwrite').orc('output.orc')
```

Write JSON:

```python
df.write.mode('overwrite').json('output.json')
```

Write to JDBC:

```python
df.write.format('jdbc') \
    .option('url', 'jdbc:mysql://localhost:3306/dbname') \
    .option('dbtable', 'employees') \
    .option('user', 'root') \
    .option('password', 'password') \
    .mode('append') \
    .save()
```

Save modes:
- `append`
- `overwrite`
- `ignore`
- `error` / `errorifexists`

---

## 7. Inspecting DataFrames

Show rows:

```python
df.show(5)
```

Print schema:

```python
df.printSchema()
```

Describe summary:

```python
df.describe().show()
```

Preview columns and types:

```python
df.columns
```

Count rows:

```python
df.count()
```

Schema fields:

```python
for field in df.schema:
    print(field.name, field.dataType, field.nullable)
```

---

## 8. Selecting and Filtering

Select columns:

```python
df.select('id', 'name').show()
```

Select with expressions:

```python
df.selectExpr('id', 'name', 'salary * 1.1 AS salary_with_bonus')
```

Filter rows:

```python
df.filter(df.salary > 50000).show()
```

Filter using SQL string:

```python
df.where("salary > 50000 AND department = 'sales'").show()
```

Filter with multiple conditions:

```python
df.filter((df.salary > 50000) & (df.department == 'Sales')).show()
```

Drop columns:

```python
df.drop('unnecessary_column')
```

Distinct values:

```python
df.select('department').distinct().show()
```

Limit rows:

```python
df.limit(10).show()
```

---

## 9. Column Expressions

Import functions:

```python
from pyspark.sql import functions as F
```

Basic expressions:

```python
df.withColumn('salary_with_bonus', F.col('salary') * 1.10)
```

Conditional logic:

```python
df.withColumn(
    'salary_level',
    F.when(F.col('salary') > 70000, 'high')
     .when(F.col('salary') > 50000, 'medium')
     .otherwise('low')
)
```

String operations:

```python
df.select(
    F.concat(F.col('first_name'), F.lit(' '), F.col('last_name')).alias('full_name'),
    F.upper(F.col('department')).alias('dept_upper')
)
```

Date operations:

```python
df.withColumn('year', F.year(F.col('hire_date')))
```

Type conversion:

```python
df.withColumn('salary_str', F.col('salary').cast('string'))
```

Create literals:

```python
df.withColumn('source', F.lit('online'))
```

---

## 10. Aggregations and Grouping

Aggregate functions:

```python
df.groupBy('department').agg(
    F.count('*').alias('count'),
    F.sum('salary').alias('total_salary'),
    F.avg('salary').alias('avg_salary'),
    F.max('salary').alias('max_salary'),
    F.min('salary').alias('min_salary')
)
```

Aggregate all rows:

```python
df.agg(
    F.count('*').alias('total_rows'),
    F.avg('salary').alias('avg_salary')
).show()
```

Group and filter aggregated results:

```python
df.groupBy('department').agg(F.avg('salary').alias('avg_salary'))
  .filter(F.col('avg_salary') > 60000)
  .show()
```

Rollup and cube:

```python
df.rollup('department', 'region').agg(F.sum('sales')).show()
```

---

## 11. Joins

Inner join:

```python
joined = df1.join(df2, df1.id == df2.employee_id, 'inner')
```

Left join:

```python
joined = df1.join(df2, df1.id == df2.employee_id, 'left')
```

Right join:

```python
joined = df1.join(df2, df1.id == df2.employee_id, 'right')
```

Full outer join:

```python
joined = df1.join(df2, df1.id == df2.employee_id, 'full')
```

Cross join:

```python
joined = df1.crossJoin(df2)
```

Broadcast join:

```python
from pyspark.sql.functions import broadcast
joined = df1.join(broadcast(df2), df1.id == df2.employee_id)
```

Join on multiple columns:

```python
joined = df1.join(df2, ['id', 'date'], 'inner')
```

---

## 12. Window Functions

Define a window:

```python
from pyspark.sql.window import Window
window = Window.partitionBy('department').orderBy(F.col('salary').desc())
```

Row number:

```python
df.withColumn('row_num', F.row_number().over(window)).show()
```

Rank and dense rank:

```python
df.withColumn('rank', F.rank().over(window))
  .withColumn('dense_rank', F.dense_rank().over(window))
```

Lead and lag:

```python
df.withColumn('prev_salary', F.lag('salary', 1).over(window))
  .withColumn('next_salary', F.lead('salary', 1).over(window))
```

Running totals:

```python
df.withColumn('salary_sum', F.sum('salary').over(window.rowsBetween(Window.unboundedPreceding, Window.currentRow)))
```

---

## 13. DataFrame Transformations

Select and transform:

```python
df2 = df.select('id', 'name', 'salary')
```

Repartition:

```python
df2 = df.repartition(4)
```

Coalesce:

```python
df2 = df.coalesce(1)
```

Sort:

```python
df.sort(F.col('salary').desc())
```

Drop duplicates:

```python
df.dropDuplicates(['name'])
```

Union:

```python
union_df = df1.union(df2)
```

Union distinct:

```python
union_df = df1.union(df2).distinct()
```

Intersect and subtract:

```python
intersect_df = df1.intersect(df2)
diff_df = df1.subtract(df2)
```

Replace values:

```python
df.na.fill({'salary': 0, 'department': 'unknown'})
```

---

## 14. Actions

Actions trigger execution:

```python
df.show()
df.count()
df.collect()
df.take(10)
df.first()
df.head(5)
df.describe().show()
df.write.mode('overwrite').parquet('output')
```

Use `collect()` carefully on large datasets.

---

## 15. SQL Queries

Register a temp view:

```python
df.createOrReplaceTempView('employees')
```

Execute SQL:

```python
result = spark.sql(
    """
    SELECT department, COUNT(*) AS total
    FROM employees
    WHERE salary > 50000
    GROUP BY department
    ORDER BY total DESC
    """
)
result.show()
```

Use SQL with DataFrame views:

```python
spark.sql('SELECT * FROM employees WHERE salary > 50000').show()
```

---

## 16. UDFs and Pandas UDFs

Regular UDF:

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def salary_level(salary):
    return 'high' if salary > 60000 else 'normal'

salary_level_udf = udf(salary_level, StringType())
df.withColumn('salary_level', salary_level_udf(F.col('salary')))
```

Pandas UDF:

```python
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import DoubleType
import pandas as pd

@pandas_udf(DoubleType())
def add_bonus(s: pd.Series) -> pd.Series:
    return s * 1.10

df.withColumn('salary_with_bonus', add_bonus(F.col('salary')))
```

Type hints for Pandas UDFs:

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

@pandas_udf(StructType([
    StructField('name', StringType()),
    StructField('salary', IntegerType())
]))
def split_name(pdf: pd.Series) -> pd.DataFrame:
    return pdf.str.split(' ', expand=True)
```

---

## 17. Partitioning and Caching

Cache a DataFrame:

```python
df.cache()
df.count()  # materialize cache
```

Persist with storage levels:

```python
df.persist()
```

Repartition by column:

```python
df2 = df.repartition('department')
```

Coalesce to fewer partitions:

```python
df2 = df.coalesce(1)
```

Write partitioned data:

```python
df.write.partitionBy('department').parquet('output')
```

---

## 18. Performance and Tuning

Use `explain()` to inspect the query plan:

```python
df.explain(True)
```

Broadcast small tables:

```python
from pyspark.sql.functions import broadcast
broadcasted = df1.join(broadcast(df2), 'id')
```

Use `persist()` when a DataFrame is reused multiple times.

Set shuffle partitions:

```python
spark.conf.set('spark.sql.shuffle.partitions', 8)
```

Avoid `collect()` on large datasets.

---

## 19. Common Functions

Date/time functions:

```python
F.current_date()
F.current_timestamp()
F.date_add(F.col('hire_date'), 7)
F.date_sub(F.col('hire_date'), 7)
F.datediff(F.col('end_date'), F.col('start_date'))
F.date_format(F.col('hire_date'), 'yyyy-MM-dd')
```

String functions:

```python
F.upper(F.col('name'))
F.lower(F.col('name'))
F.concat(F.col('first_name'), F.lit(' '), F.col('last_name'))
F.substring(F.col('name'), 1, 5)
F.trim(F.col('name'))
F.length(F.col('name'))
F.regexp_replace(F.col('name'), '\\s+', ' ')
```

Null handling:

```python
F.coalesce(F.col('middle_name'), F.lit(''))
F.when(F.col('column').isNull(), 'unknown').otherwise(F.col('column'))
```

Conditional:

```python
F.when(F.col('salary') > 70000, 'high')
 .when(F.col('salary') > 50000, 'medium')
 .otherwise('low')
```

Mathematical functions:

```python
F.round(F.col('salary'), 2)
F.abs(F.col('delta'))
F.sqrt(F.col('value'))
F.pow(F.col('value'), 2)
```

---

## 20. Debugging and Metadata

Show query plan:

```python
df.explain()
```

View columns:

```python
print(df.columns)
```

View schema in JSON:

```python
print(df.schema.json())
```

List Spark catalog tables:

```python
spark.catalog.listTables()
```

Clear cache:

```python
spark.catalog.clearCache()
```

---

## 21. Notes

- PySpark uses lazy evaluation: transformations are not executed until an action runs.
- Prefer built-in Spark functions over Python UDFs for better performance.
- Use `withColumn()` to add or replace columns.
- Use `selectExpr()` for SQL-style expressions.
- Use separate `repartition()` and `coalesce()` depending on whether you want more or fewer partitions.
- Temporary views last only for the Spark session; global views last across sessions using `global_temp`.
- Use `spark.stop()` to free resources when done.


Select and transform:

```python
df2 = df.select('id', 'name', 'salary')
```

Repartition:

```python
df2 = df.repartition(4)
```

Coalesce:

```python
df2 = df.coalesce(1)
```

Sort:

```python
df.sort('salary', ascending=False)
```

Drop duplicates:

```python
df.dropDuplicates(['name'])
```

Union:

```python
union_df = df1.union(df2)
```

---

## 11. SQL Queries

Register a temp view:

```python
df.createOrReplaceTempView('employees')
```

Run SQL:

```python
result = spark.sql(
    """
    SELECT department, COUNT(*) AS total
    FROM employees
    WHERE salary > 50000
    GROUP BY department
    ORDER BY total DESC
    """
)
result.show()
```

---

## 12. UDFs and Pandas UDFs

Regular UDF:

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def salary_level(salary):
    return 'high' if salary > 60000 else 'normal'

salary_level_udf = udf(salary_level, StringType())
df.withColumn('salary_level', salary_level_udf(F.col('salary')))
```

Pandas UDF:

```python
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import DoubleType
import pandas as pd

@pandas_udf(DoubleType())
def add_bonus(s: pd.Series) -> pd.Series:
    return s * 1.10

df.withColumn('salary_with_bonus', add_bonus(F.col('salary')))
```

---

## 13. Partitioning and Caching

Cache a DataFrame:

```python
df.cache()
df.count()  # materialize cache
```

Persist in memory and disk:

```python
df.persist()
```

Repartition by column:

```python
df2 = df.repartition('department')
```

Write partitioned data:

```python
df.write.partitionBy('department').parquet('output')
```

---

## 14. Common Functions

Date/time:

```python
F.current_date()
F.current_timestamp()
F.date_add(F.col('date'), 7)
F.date_sub(F.col('date'), 7)
F.datediff(F.col('end_date'), F.col('start_date'))
```

String:

```python
F.upper(F.col('name'))
F.lower(F.col('name'))
F.concat(F.col('first_name'), F.lit(' '), F.col('last_name'))
F.substring(F.col('name'), 1, 5)
F.trim(F.col('name'))
F.length(F.col('name'))
```

Null handling:

```python
F.coalesce(F.col('middle_name'), F.lit(''))
F.when(F.col('column').isNull(), 'unknown').otherwise(F.col('column'))
```

Conditional:

```python
F.when(F.col('salary') > 70000, 'high')
 .when(F.col('salary') > 50000, 'medium')
 .otherwise('low')
```

---

## 15. Notes

- PySpark operations are lazy; they execute only when an action runs (`show()`, `count()`, `write`).
- Use `explain()` to inspect the query plan.
- Prefer built-in functions over Python UDFs for better performance.
- Use `persist()` or `cache()` for DataFrames reused multiple times.
- Use `repartition()` to increase partitions and `coalesce()` to reduce them.
- Temporary views are session-scoped and disappear when the Spark session ends.
