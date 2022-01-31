# Re-Invent Notes

[TOC]

# 2020



## Serverless Update - Lambda

### Lambda Extension

- Layers is about managing dependencies in a single place that are common to multiple functions

- layers = reuse, extensions = extending the functionality
- It runs inside lambda function
- plugging my own extensions joke as an example of what you could do with it: <https://twitter.com/benbridts/status/1329478756583559168>

![1606320466284](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320466284.png)![1606320543834](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320543834.png)

![1606320615401](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320615401.png)

![1606320649305](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320649305.png)

![1606320722636](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320722636.png)

![1606320810377](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320810377.png)

### VPC Endpoint for Lambda

- No need of NAT Gateway

  ![1606320901693](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320901693.png)

### AVX2 Lambda Support Update

![1606320980905](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606320980905.png)

![1606321057417](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321057417.png)

### AWS MQ as Lambda Source

![1606321114455](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321114455.png)

### Code signing for Lambda

![1606321174329](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321174329.png)

## Serverless - SNS

### SNS FIFO

**Kinesis --> SNS --> SQS Fan out --> Lambda pure Event sourcing goodness.**

![1606321288329](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321288329.png)

![1606321340344](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321340344.png)

## Serverless - MQ

![1606321384670](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321384670.png)

## Serverless - Event Bridge

### DLQ

![1606321450571](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321450571.png)

### Replay

![1606321613730](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321613730.png)

### Archive

![1606321661468](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321661468.png)

### Replay

![1606321676970](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321676970.png)

## Serverless Step Function

### Sync Express workflow

- Max 5 mins
- Expects reply back

![1606321701880](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321701880.png)

### Step Function - API Gateway

![1606321782104](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321782104.png)

## Serverless - SAM CLI

![1606321857594](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321857594.png)

## Serveless land

- Architecture reference for best contents

![1606321979851](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606321979851.png)

