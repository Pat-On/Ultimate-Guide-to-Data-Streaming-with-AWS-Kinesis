# Problems of GetRecords based SDK consumers


- consumed records need tracked in some external data store to avoid duplicate processing
- horizontal scaling through either multi-threading or multiple instances of the same application becomes hard (distributed computing is not easy)
- shard splitting and shard merging requires complex consumer logic
- cannot handle de-aggregation of KPL produced records




Usually better solutions
- Kinesis Client Library
- AWS consumers
- Kinesis Analytics applications (Streaming SQL / Apache Flink)