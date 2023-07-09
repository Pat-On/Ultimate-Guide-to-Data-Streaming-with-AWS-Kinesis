
1) Create Input Kinesis Data Stream

aws kinesis create-stream --stream-name seller-sales --shard-count 2

2) Create Output Kinesis Data Stream

aws kinesis create-stream --stream-name seller-windowed-revenue --shard-count 1

3) Start Producing to Kinesis Input Stream

python producer.py seller-sales

4) Create a AWS Glue Database

name it something like seller-revenue

5) Create Kinesis Data Analytics for Flink Notebook


6) Create Flink Source Table

%flink.ssql

CREATE TABLE seller_sales (
    customer_id       VARCHAR,
    order_id          VARCHAR,
    seller_id         VARCHAR,
    product_name      VARCHAR,
    product_code      VARCHAR,
    product_quantity  INTEGER,
    product_price     DOUBLE,
    proctime AS       PROCTIME()
) 
PARTITIONED BY (seller_id)
WITH (
    'connector'           = 'kinesis',
    'stream'              = 'seller-sales',
    'aws.region'          = 'us-east-1',
    'scan.stream.initpos' = 'LATEST',
    'format'              = 'json'
)

7) Create Flink Sink Table

%flink.ssql

CREATE TABLE seller_revenue (
    seller_id    VARCHAR,
    window_end   TIMESTAMP,
    sales        DOUBLE
) WITH (
    'connector'           = 'kinesis',
    'stream'              = 'seller-windowed-revenue',
    'aws.region'          = 'us-east-1',
    'scan.stream.initpos' = 'LATEST',
    'format'              = 'json'
)

8) Create a View of Seller Revenue Over 60 Second Windows

%flink.ssql(parallelism=1)

CREATE VIEW seller_revenue_vw AS
SELECT
    seller_id,
    TUMBLE_END(proctime, INTERVAL '30' SECONDS) AS window_end,
    SUM(product_quantity * product_price) AS sales
FROM seller_sales
GROUP BY
    TUMBLE(proctime, INTERVAL '30' SECONDS),
    seller_id


9) Get a Peek at the Data

%flink.ssql(type=update, refreshInterval=1000)

SELECT seller_id, sales, window_end
FROM seller_revenue_vw


10) Push Windowed Calculation Into Revenue Table / Output Kinesis Stream

%flink.ssql(parallelism=1)

INSERT INTO seller_revenue
SELECT
    seller_id,
    TUMBLE_END(proctime, INTERVAL '30' SECONDS) AS window_end,
    SUM(product_quantity * product_price) AS sales
FROM seller_sales
GROUP BY
    TUMBLE(proctime, INTERVAL '30' SECONDS),
    seller_id


11) Deploy KDA Application


12) Consume Data from Kinesis Output Stream

python consumer.py seller-windowed-revenue
