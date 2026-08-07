# E-commerce Practice Dataset (Flipkart / Amazon style)

A 5-table star schema, deliberately messy, so you can practice PySpark the way you'd actually use it
on an online-retail data pipeline.

## Files (CSV + JSON for each)
| Table | Rows | Type | Role |
|---|---|---|---|
| `customers` | ~3,040 | Dimension | who bought |
| `products` | 600 | Dimension | what was sold |
| `orders` | ~9,100 | Fact (header) | one row per order |
| `order_items` | ~27,080 | Fact (line item) | one row per product per order |
| `reviews` | 5,000 | Fact | ratings/text tied to customer + product |

**Special: `orders.json` has the line items nested inside each order** (`items: [...]`) — this mirrors
how a real e-commerce API/event stream looks, and is exactly what you'll `explode()` in practice.
`orders.csv` and `order_items.csv/json` give you the same data pre-flattened, for straightforward joins.

**Parquet:** same limitation as last time — no `pyarrow`/network in this sandbox. Once you're in your
own PySpark environment:
```python
for name in ["customers", "products", "orders", "order_items", "reviews"]:
    spark.read.option("header", True).option("inferSchema", True).csv(f"{name}.csv") \
         .write.mode("overwrite").parquet(f"{name}_parquet")
```

## Schema (join keys)
```
customers.customer_id ──< orders.customer_id
products.product_id   ──< order_items.product_id
orders.order_id        ──< order_items.order_id
customers.customer_id ──< reviews.customer_id
products.product_id   ──< reviews.product_id
```

## What's intentionally messy

| Feature | Where | Practice target |
|---|---|---|
| Whitespace/case issues in names | `customers.customer_name` | `trim()`, `initcap()` |
| Nulls scattered around | email, phone, age, gender, rating, delivery_days | `isNull`, `fillna`, `coalesce` |
| Malformed emails | `customers.email` | regex validation, `rlike()` |
| Negative price (rare, on purpose) | `products.price` | data-quality checks, `when/otherwise` |
| Duplicate customer signups (~40) | `customers` | `dropDuplicates()` |
| Duplicate order events (~100) | `orders` | dedup by `order_id`, keep-latest patterns |
| Cancelled / Returned / Pending orders | `orders.order_status`, `order_items.item_status` | filtering, conditional aggregation |
| Nested line items | `orders.json` | `explode()`, flattening nested arrays of structs |
| Discounts | `products.discount_pct`, `orders.discount_amount` | derived columns, revenue-after-discount calcs |
| Free-text reviews (some null) | `reviews.review_text` | string functions, basic text/NLP prep, null handling |
| Wide date range (2019–2026) | `signup_date`, `order_date`, `review_date` | `to_date`, `year()/month()`, time-based trends, retention-style analysis |

## Suggested progression
1. **Load all 5 tables**, `printSchema()` each, compare CSV vs JSON schema inference
2. **Clean** customers (trim names, validate emails/phones) and products (fix negative prices)
3. **Explode** `orders.json` items and reconcile the totals against the flat `order_items` table
4. **Join** the star: `orders` + `customers` + `order_items` + `products` → one wide table
5. **Revenue analytics** — monthly revenue, revenue by category/city, AOV (average order value), effect of `discount_pct` on `rating`/sales
6. **Customer analytics** — top spenders, premium vs non-premium behavior, RFM-style scoring (recency/frequency/monetary) using window functions
7. **Product analytics** — best/worst rated products, join with `reviews` to compare stated `rating` vs actual review sentiment (positive/neutral/negative by keyword)
8. **Operations** — cancellation/return rate by category or payment mode, average `delivery_days` by city
9. **Write out** partitioned Parquet (e.g., by `order_status` or `category`) and inspect the folder layout

Want a 6th table — like a `payments`/`refunds` log, or a clickstream/browsing-events table for
funnel analysis — say the word and I'll add it.
