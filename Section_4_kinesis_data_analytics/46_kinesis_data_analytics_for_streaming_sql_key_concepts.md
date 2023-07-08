# Kinesis data analytics for streaming SQL key concepts

- AWS recommends KDS for Apache Flink for new projects
- Provides SQL-lite interface for doing Stream processing
  - Closely resembles ANSI 2008 SQL standard
  - Think of your queries as continuously executing operations if updating result sets
  - Streams are conceptually through of as tables which you join, filter, group and aggregate
  - Results of queries can be used to build other in-application streams and used in other queries or sent to a destination such another Kinesis Data Stream (then on to Lambda) or Kinesis Data Firehose (and into S3, Redshift, Elastic Search, Splunk)
  - Can join against static reference CSV data in S3

- Constructs are streams and pumps
  - Streams define the schema of a table like data structure through which data flows
  - Pumps are defined through the act of selecting data from one stream and feeding data into another

--- 

