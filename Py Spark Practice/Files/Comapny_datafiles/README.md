# PySpark Practice Dataset

Two tables, deliberately messy, built to cover most of what you'll hit day-to-day in PySpark.

## Files
- `employees.csv` / `employees.json` — 6,210 rows (fact table)
- `departments.csv` / `departments.json` — 10 rows (dimension table, for joins)

**Parquet:** I couldn't write real `.parquet` files in this sandbox (no `pyarrow`/`pyspark` here and no
internet to install them). Since you'll have PySpark installed wherever you practice, generate it there —
it's one line and it's good practice anyway:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("practice").getOrCreate()

emp = spark.read.option("header", True).option("inferSchema", True).csv("employees.csv")
emp.write.mode("overwrite").parquet("employees_parquet")

dept = spark.read.option("header", True).option("inferSchema", True).csv("departments.csv")
dept.write.mode("overwrite").parquet("departments_parquet")
```

(Read `employees.json` instead if you want the nested `address` struct and real `skills` array to
carry over — CSV flattens those.)

## What's intentionally "dirty" (and why)

| Feature | Where | Practice target |
|---|---|---|
| Leading/trailing spaces, mixed case in names | `emp_name` | `trim()`, `lower()`/`initcap()`, `regexp_replace` |
| Missing values | `email`, `age`, `salary`, `rating`, `login_timestamp`, `manager_id`, `phone`, `gender` | `isNull()`, `fillna()`, `dropna()`, `coalesce()` |
| Malformed emails / short phone numbers | `email`, `phone` | regex validation, `rlike()`, data quality checks |
| Impossible values (age -5, 0, 150; negative salary) | `age`, `salary` | `when/otherwise` cleaning, filtering, outlier handling |
| ~150 exact duplicate rows | across `employees` | `dropDuplicates()`, `distinct()` |
| ~60 rows with same `emp_id` but updated `salary`/`designation`/`login_timestamp` | across `employees` | dedup-keep-latest patterns, window functions (`row_number()` over `emp_id` ordered by `login_timestamp`), basic SCD Type-2 thinking |
| Self-referencing `manager_id` | `employees` | self-joins, recursive-style hierarchy queries |
| `skills` as an array (JSON) / pipe-delimited string (CSV) | `skills` | `explode()`, `array_contains()`, `split()` |
| Nested `address` struct (JSON only) | `address.city/state/street/pincode` | struct field access, `.select("address.city")`, flattening nested JSON |
| Two related tables via `dept_id` | `employees` ↔ `departments` | `join()` (inner/left/right/outer), broadcast join practice |
| Dates as strings (`joining_date`, `login_timestamp`) spanning 2018–2026 | `employees` | `to_date()`, `to_timestamp()`, `datediff()`, `year()/month()`, window functions over time |
| Boolean column | `is_active` | filtering, casting |
| Skewed salary ranges by department | `salary` | `groupBy().agg()`, `avg/min/max/stddev`, department-wise analytics |

## Suggested progression
1. **Read & inspect** — schema inference vs explicit `StructType`, `printSchema()`, `show()`, `describe()`
2. **Clean** — trim/case names, fix nulls, filter out impossible ages/salaries, validate emails/phones with regex
3. **Dedup** — exact duplicates, then keep-latest-by-`emp_id` using `Window.partitionBy("emp_id").orderBy(col("login_timestamp").desc())`
4. **Transform** — `explode()` skills, flatten the JSON `address` struct, derive `tenure_years` from `joining_date`
5. **Join** — enrich `employees` with `departments` (dept name, location, budget); try broadcast join since `departments` is tiny
6. **Aggregate** — headcount and avg salary by department/city, active vs inactive split, top-rated employees per department (window function `rank()`)
7. **Write out** — partition by `dept_id` or `city` when writing Parquet, compare file layout with `.explain()`

Once this feels easy, tell me and I'll generate a second, larger "orders/transactions" fact table so you can practice star-schema joins and more advanced aggregations.
