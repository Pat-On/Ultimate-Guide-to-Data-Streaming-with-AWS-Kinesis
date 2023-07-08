# Python demo serverless lambda consumer

```bash
CloudFormation stack changeset
-----------------------------------------------------------------------------------------------------------------
Operation                    LogicalResourceId            ResourceType                 Replacement                
-----------------------------------------------------------------------------------------------------------------
+ Add                        KinesisOrdersStream          AWS::Kinesis::Stream         N/A                        
+ Add                        OrdersConsumerFunctionRole   AWS::IAM::Role               N/A                        
+ Add                        OrdersConsumerFunctionStre   AWS::Lambda::EventSourceMa   N/A                        
                             amRecordsBatch               pping                                                   
+ Add                        OrdersConsumerFunction       AWS::Lambda::Function        N/A                        
-----------------------------------------------------------------------------------------------------------------


```


sam logs --stack-name 