# Kinesis Data Analytics: Streaming SQL Time aspects

- Since stream processing applications operate on continous onbound data then performing operations like counts, sums, minimums, maximums, ect.. are only possible on subset of ingested records divided across `windows` of time (seconds, minutes, hours, ect ...)
- Different Options Available for Time Semantics
  - `Row Time`: artificial pseudo time added to each event as it flows into KDA Streaming SQL in-application stream
  - `Event Time:` the time at which the event occurred in the world
  - `ingest time:` the time at which event was inserted into Kinesis data stream or kinesis data firehose

---

