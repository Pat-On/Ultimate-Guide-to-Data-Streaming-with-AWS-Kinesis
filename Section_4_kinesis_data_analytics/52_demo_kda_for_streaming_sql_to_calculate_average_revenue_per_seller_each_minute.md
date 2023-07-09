# Demo
## KDS for Streaming SQL to Calculate Average Revenue per Seller Each Minute

- Total window aggregation - kds-processor.sql


```SQL

CREATE OR REPLACE PUMP "SELLER_REVENUE_PUMP1" AS
INSERT INTO "SELLER_REVENUE_STREAM1"
SELECT STREAM
  "SOURCE_SQL_STREAM_001"."seller_id" AS "SELLER_ID",
  STEP("SOURCE_SQL_STREAM_001"."ROWTIME" BY INTERVAL '30' SECOND) AS "WINDOWTIME",
  SUM("SOURCE_SQL_STREAM_001"."product_quantity" * 
      "SOURCE_SQL_STREAM_001"."product_price" ) AS "REVENUE"
FROM "SOURCE_SQL_STREAM_001"
GROUP BY "SOURCE_SQL_STREAM_001"."seller_id",
-- definition of tumbling window with STEP function
    STEP("SOURCE_SQL_STREAM_001"."ROWTIME" BY INTERVAL '30' SECOND);

```