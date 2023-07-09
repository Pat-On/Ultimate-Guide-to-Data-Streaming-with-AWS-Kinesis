-- Multi-step application
-- Intermediate, in-application streams are useful for building 
-- advanced logic into stream processing applications.
--
--           .-----------------.    .-------------------.
--           |  Total Revenue  |    | Enrich By Labeling|
-- Source -> | Per Seller & 30 | -> |  Row Relative To  | -> Destination
--           |  Second Window  |    |  Previous Window  |
--           '-----------------'    '-------------------'
-- STREAM (in-application): a continuously updated entity that you 
--        can SELECT from and INSERT into like a TABLE
-- PUMP: an entity used to continuously 'SELECT ... FROM' a source 
--       STREAM, and INSERT SQL results into an output STREAM

CREATE OR REPLACE STREAM "SELLER_REVENUE_STREAM1" (
  "SELLER_ID"        VARCHAR(10),
  "WINDOWTIME"       TIMESTAMP,
  "REVENUE"          DECIMAL(7, 2)
);

CREATE OR REPLACE PUMP "SELLER_REVENUE_PUMP1" AS
INSERT INTO "SELLER_REVENUE_STREAM1"
SELECT STREAM
  "SOURCE_SQL_STREAM_001"."seller_id" AS "SELLER_ID",
  STEP("SOURCE_SQL_STREAM_001"."ROWTIME" BY INTERVAL '30' SECOND) AS "WINDOWTIME",
  SUM("SOURCE_SQL_STREAM_001"."product_quantity" * 
      "SOURCE_SQL_STREAM_001"."product_price" ) AS "REVENUE"
FROM "SOURCE_SQL_STREAM_001"
GROUP BY "SOURCE_SQL_STREAM_001"."seller_id",
    STEP("SOURCE_SQL_STREAM_001"."ROWTIME" BY INTERVAL '30' SECOND);


CREATE OR REPLACE STREAM "SELLER_REVENUE_STREAM2" (
  "SELLER_ID"       VARCHAR(10),
  "WINDOWTIME"      TIMESTAMP,
  "REVENUE"         DECIMAL(7, 2),
  "LAST_REVENUE"    DECIMAL(7, 2),
  "TREND"           VARCHAR(12)
);
CREATE OR REPLACE PUMP "SELLER_REVENUE_PUMP2" AS
INSERT INTO "SELLER_REVENUE_STREAM2"
SELECT STREAM
  t."SELLER_ID",
  t."WINDOWTIME",
  t."REVENUE",
  t."LAST_REVENUE",
  CASE 
      WHEN t."LAST_REVENUE" > t."REVENUE" THEN 'DECREASING'
      WHEN t."LAST_REVENUE" < t."REVENUE" THEN 'INCREASING'
      ELSE 'NO CHANGE'
  END AS "TREND"
  FROM (
    SELECT STREAM "SELLER_ID", "WINDOWTIME", "REVENUE",
      LAG("REVENUE", 1, 0) OVER WIN AS "LAST_REVENUE"
    FROM "SELLER_REVENUE_STREAM1"
    WINDOW WIN AS (PARTITION BY "SELLER_ID" ROWS 1  PRECEDING)
  ) t;
