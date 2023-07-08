# Creating Kinesis Data Stream with AWS CLI




```sh
aws <service> <action>

aws kinesis

aws kinesis create-stream help


            create-stream
          --stream-name <value>

        --stream-name (string)
          A name to identify the stream. The stream name is scoped to the Ama-
          zon Web Services account used by the application  that  creates  the
          stream.  It  is  also scoped by Amazon Web Services Region. That is,
          two streams in two different Amazon Web Services accounts  can  have
          the  same  name. Two streams in the same Amazon Web Services account
          but in two different Regions can also have the same name.


aws kinesis create-stream --stream-name  my-cli-stream --shard-count 1


aws kinesis describe-stream --stream-name my-cli-stream
{
    "StreamDescription": {
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "StartingHashKey": "0",
                    "EndingHashKey": "340282366920938463463374607431768211455"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber": "49642440508930214513090187760726760919720265384565145602"
                }
            }
        ],
        "StreamARN": "arn:aws:kinesis:eu-west-1:374366843190:stream/my-cli-stream",
        "StreamName": "my-cli-stream",
        "StreamStatus": "ACTIVE",
        "RetentionPeriodHours": 24,
        "EnhancedMonitoring": [
            {
                "ShardLevelMetrics": []
            }
        ],
        "EncryptionType": "NONE",
        "KeyId": null,
        "StreamCreationTimestamp": "2023-07-08T07:30:32+01:00"
    }
}


```


```bash
pat@pat-GE62-2QF:~$ aws kinesis delete-stream --stream-name my-cli-stream
pat@pat-GE62-2QF:~$ aws kinesis describe-stream --stream-name my-cli-stream
{
    "StreamDescription": {
        "Shards": [],
        "StreamARN": "arn:aws:kinesis:eu-west-1:374366843190:stream/my-cli-stream",
        "StreamName": "my-cli-stream",
        "StreamStatus": "DELETING",
        "RetentionPeriodHours": 24,
        "EnhancedMonitoring": [
            {
                "ShardLevelMetrics": []
            }
        ],
        "EncryptionType": "NONE",
        "KeyId": null,
        "StreamCreationTimestamp": "2023-07-08T07:30:32+01:00"
    }
}
```
