
1) Create Input Kinesis Data Stream

aws kinesis create-stream --stream-name seller-sales --shard-count 1

2) Create Output Kinesis Data Stream

aws kinesis create-stream --stream-name seller-windowed-revenue --shard-count 1

3) Start Producing to Kinesis Input Stream

python producer.py seller-sales

4) Create KDA Streaming SQL Application

name it something like seller-revenue

5) Add SQL Application Code

6) Consume Data from Kinesis Output Stream

python consumer.py seller-windowed-revenue
