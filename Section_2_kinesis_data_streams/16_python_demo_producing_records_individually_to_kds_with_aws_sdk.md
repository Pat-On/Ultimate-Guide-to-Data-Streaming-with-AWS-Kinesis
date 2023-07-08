# Python Demo Producing Record Individually to KDS with AWS SDK 

hashing in the Kinesis


Best effort to figuring out uniformly map data across shards
```
'abc123' -> hashed -> 21389745980125 % num_shards = 
```

this is used to not let `hot shard` become real


```
aws kinesis create-stream --stream-name my-put-record --shard-count 2
```

blah I forgot :D 
```
python -m pip install -r /path/to/requirements.txt
```