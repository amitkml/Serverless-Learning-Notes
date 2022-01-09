# 	DynamoDB

![im](https://miro.medium.com/max/700/1*Kyz3EGX-PfkxAbDHxkJzpg.jpeg)

DynamoDB is a **serverless**, **fully managed** **NoSQL** (non-relational) database service designed for Online Transactional Processing (OLTP) workloads.

**Amazon DynamoDB Indexes**: There are two types of indexes in DynamoDB, a Local Secondary Index (LSI) and a Global Secondary Index (GSI). In an LSI, a range key is mandatory, while for a GSI you can have either a hash key or a hash+range key. GSIs span multiple partitions and are placed in separate tables. DynamoDB supports up to five GSIs. While creating a GSI, you need to carefully choose your hash key because that key will be used for partitioning.

Which is the right index type to use? Here are two considerations: LSIs limit item size to 10 GB, and GSIs offer only eventual consistency.

When you create a table, **you define a partition key attribute to uniquely identify each item in the table, so that no two items can have the same key. You can also assign other attributes, like a sort key attribute**.

- DynamoDB charges for reading, writing, and storing data, along with any optional features you choose to enable. 
- DynamoDB has two capacity modes: provisioned and on-demand. Each comes with specific billing options for processing reads and writes on your tables.

![img](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/cXzArv9hAxbwHQbl_rI32Zx9c9ZDEzzNa.png)

- Flexible Schema
- JSON document or key-value data structures
- Supports event-driven programming
- Accessible via AWS Management Console, CLI, and SDK
- Availability, durability, and scalability built-in
- Scales horizontally
- Provides fine-grained access control
- Integrates with other AWS services

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/79bFyjrAYjHhbAJw_1y2DBgAOSjBCGoIs.png)

### **Mobile application backend architecture**

Social mobile applications are more popular than ever. This architecture provides one solution for allowing a mobile application to automatically notify a user’s friends when the user’s status changes.

  ![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640088000/t5XL5-QPyMMM7sHIvFifyQ/tincan/6d1b98bb483485f132e3e1735ddf2966846c6434/assets/umY0rQKX8HypF6IN_mz2iDJq3Vn33K1av.png)



### **IoT sensor data capture architecture**

Capturing data from thousands of Internet of Things (IoT) sensors can be a challenge. This architecture represents one solution to this challenge.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640088000/t5XL5-QPyMMM7sHIvFifyQ/tincan/6d1b98bb483485f132e3e1735ddf2966846c6434/assets/sPEn6_Im24hW1FlU_HbOWTg9VGAyMq0GU.png)  

## What are the advantages of DDB?

Here is the list of some of the benefits of using Amazon DynamoDB:

- It is a managed service where there is no need to hire the experts or worry about installation, setup, cluster etc.,
- It is scalable.
- It provides the users high throughput at very low latency.
- It is durable and highly available.
- It is flexible and allows dynamic tables creation that includes multi-valued attributes.
- It is cost-effective.

## What are Non-relational database?

The Non-Relational databases are NoSQL databases.

These databases are categorized into four groups, and they are:

- Key-value stores
- Graph stores
- Column stores
- Document stores

## What are queries supported by DDB?

- It supports GET/PUT operation using the user-defined primary key.
- It provides flexible querying by letting query a non-primary key attribute using local secondary indexes and Global secondary indexes.
- It allows quick reads and writes data for an item associated with single attribute partition primary key.
- It allows you to use the Query API to retrieve all the items for a single composite partition-sort key across a range of sort keys.

## What are API’s provided by DDB?

- CreateTable
- UpdateTable
- DeleteTable
- DescribeTable
- ListTables
- WRITE
  - PutItem
  - BatchWriteItem
  - UpdateItem
  - DeleteItem
- READ
  - GetItem
  - BatchGetItem.
  - Query
  - Scan

## What are DDB entries?

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/seOWJMr2T-n6H08J__HfmFR___hWj9RYQ.png)

## What is Partition and Sort Primary Key?

**Partition Primary Key**
**The primary key consists of a single attribute, the partition key**.  In this example, the primary key is the SensorId attribute. Each sensor has exactly one location expressed in terms of latitude and longitude.

DynamoDB builds an unordered index on this primary key attribute. 

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/8SaHwlHdjv5zqTDn_yiQY-zS62gTqdyi7.png)

**Partition and Sort Primary Key**
**The primary key is comprised of the partition key plus the sort key**. In this example, the primary key is  made up of the SensorID and Time attributes. For each SensorId, there may be multiple items corresponding to sensor readings at different times. 

DynamoDB builds an unordered index on the partition key attribute and a sorted index on the sort key attribute. 

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/_X3alR10FxtmYF5G_fZviIM5UXltxeJjN.png)

## How to design Amazon DynamoDB global secondary indexes?

**GSI can have primary and sort key different from Primary table index,**

With nonrelational databases, the approach for designing a schema proceeds in reverse. You use a “query first” approach to identify the queries the applications need before designing the database schema. Data is therefore explicitly stored the way that the application needs to use it, increasing query efficiency.

If you also want to add flexibility to your queries, you can use [global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general.html) with [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). When you use global secondary indexes on a DynamoDB table, you can query data flexibly in other dimensions, using nonkey attributes.

![im](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2019/03/14/designingglobalsecondaryindexes_800x400.png)

Let’s look at an example to see how an application-specific query translates to table queries. Let’s say an online shopping website stores all of the orders of a customer in an **Orders** table with OrderId as the partition key. The table also stores other data about the order such as OrderDate, CustomerId, and Status. The following table shows some of the common application-specific questions and their corresponding table queries.

| **Application specific question**                            | **Table query**                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Find all orders for a customer sorted by order date          | Filter all orders in the **Orders** table by `CustomerId` and then sort by `OrderDate` |
| Get orders for a given customer within a given date range    | Filter all orders in the **Orders** table by `CustomerId` and then filter by range query on `OrderDate` |
| Find all pending orders for a customer                       | Filter all orders in the **Orders** table by `CustomerId` and then filter by `Status` as Pending |
| Find all pending orders for a customer that are more than five days old | Filter all orders in the **Orders** table by `CustomerId` and then filter by `Status` as `Pending` and range query of `OrderDate < CurrentDate-5` |
| Get `OrderId`, `OrderDate`, and `Status` for all orders of a customer | Filter all orders in the **Orders** table by `CustomerId` and get their `OrderId`, `OrderDate`, and `Status` |

The following table shows an example, using the online shopping website stores data used earlier.

| **Table query**                                              | **Candidate partition key** | **Candidate sort key**                | **Attribute projections**  |
| ------------------------------------------------------------ | --------------------------- | ------------------------------------- | -------------------------- |
| Filter all orders in the **Orders** table by `CustomerId` and then sort by `OrderDate` | CustomerId                  | OrderDate                             |                            |
| Filter all orders in the **Orders** table by `CustomerId` and then filter by range query on `OrderDate` | CustomerId                  | OrderDate                             |                            |
| Filter all orders in the **Orders** table by `CustomerId` and then filter by `Status` as `Pending` | CustomerId                  | Status                                |                            |
| Filter all orders in the **Orders** table by `CustomerId` and then filter by `Status` as `Pending` and range query of `OrderDate < CurrentDate-5` | CustomerId                  | Status:OrderDate (composite sort key) |                            |
| Filter all orders in the **Orders** table by `CustomerId` and get their `OrderId`, `OrderDate`, and `Status` | CustomerId                  |                                       | OrderId, OrderDate, Status |

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/XzjqZpoSAIDFH8nE_ma4sx04g7iu2WkqZ.png)

### Optimize candidate fields for cost and performance

You should optimize the candidate fields you identify for each query for cost and performance, before you use them in a global secondary index schema.

**Optimize candidate fields for cost**

Every global secondary index is provisioned independently and maintains its own copy of the data separately from the base table. As a result, sharing indexes to answer more than one query helps reduce the cost of maintaining an index.

Answering the following questions can help you design the best schema and optimize for cost.

1. **Can I use a single global secondary index to answer multiple queries?**Sometimes multiple queries can be answered by using a single global secondary index. Some of the common use cases in which global secondary indexes can be reused are:

All the global secondary indexes must include a partition key, with the option of a sort key. The index key schema can differ from the table, and index key attributes can use any top-level string, number, or binary table attributes.

![im](https://miro.medium.com/max/700/1*-tLu4J1g4g78Ibv66EOpZQ.jpeg)

## What is max GSI per DDB?

You are allowed to create a maximum of 20 global secondary indexes per table.

## What is Local Secondary Index?

An index with the same partition key as the table but different sort key is called local secondary index. A local secondary index is considered to be “local” because every partition of a local secondary index is scaled to a table partition which contains the same partition key.

**Local Secondary Indexes:** There are instances where application needs to access an **alternate Sort key rather than your base table’s primary key**. To give your application a choice of sort keys, you can create one or more local secondary indexes on an Amazon DynamoDB table and issue Query or Scan requests against these indexes.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/1LcpEOsQNywxvEf1_l0WEQQq7hiwqUKRs.png)

- LSI must be created when you create the table

![im](https://miro.medium.com/max/700/1*cp4zA1LiiSxO4Y7ZLhYk9A.jpeg)

## What is Dynamo DB Streams?

DynamoDB Streams makes change data capture from database available on an event stream. One of the use cases for processing DynamoDB streams is to index the data in ElasticSearch for full text search or doing analytics.

- A DynamoDB stream is an ordered flow of information about changes to a table. 
- The records in the stream are strictly in the order in which the changes occurred. 
- Each change contains exactly one stream record. A stream record is available for 24 hours.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/9NeDQ_peihxS-bdf_JGSUniX6g5UW8R1k.png)

Refer the article https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html

- an event-driven mechanism that enables developers to define Java or JavaScript functions that run outside the database in response to specific data changes in your DynamoDB tables. 
- Specifically, these functions are configured and executed as AWS Lambda functions, giving you the ability to scale on the fly and only pay for the fractions of the computing seconds consumed. All you need to do is register the [AWS Lambda function](http://aws.amazon.com/lambda/) that needs to be executed in response to a specific data change in the DynamoDB table. 
- Lambda and DynamoDB take care of the rest. DynamoDB creates a stream and pushes the data to the trigger code. Lambda automatically creates and manages the resources needed to handle the trigger. 
- Since the Lambda function executes on hosts that are different from that of the DynamoDB table, both the DynamoDB table and Lambda function scale independently, thus isolating the risk of errant triggers

![im](https://www.allthingsdistributed.com/images/dynamodbstreams.png)

![im](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/StreamsAndTriggers.png)

## How security enabled for DDB?

DDB utilizes IAM for DDB table and data access. All DB has encryption in rest enabled by default.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/aH_4CG3aXCLWdEFX_B3s2mna-CO1Zuvvf.jpg)

Enable CloudTrail so that DynamoDB control operations (create table, update table, etc.) are available for later analysis.

- Use the CloudWatch metrics provided by DynamoDB to monitor table performance.
- Set alarms for pertinent metrics out of acceptable range.

## Is Index mandatory for DDB?

DynamoDB does not require you to configure indexing on tables, but it is recommended. DynamoDB allows you to add one or more secondary indexes to aid in query performance. You can add up to 20 global secondary indexes and up to 5 local secondary indexes per table.

## What is DynamoDB Accelerator DAX?

![im](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/dax_high_level.png)

**DynamoDB Accelerator Operations**

- Eventual Read operations
  - If DAX has the item available (a *cache hit*), DAX returns the item without accessing DynamoDB.
  - If DAX does not have the item available (a *cache miss*), DAX passes the request through to DynamoDB. When it receives the response from DynamoDB, DAX returns the results to the application. But it also writes the results to the cache on the primary node.
- Strongly Consistent Read operations
  - DAX passes the request through to DynamoDB. The results from DynamoDB are not cached in DAX. but simply returned
- For Write operations
  - Data is first written to the DynamoDB table, and then to the DAX cluster.
  - Operation is successful only if the data is successfully written to *both* the table and to DAX.

**DAX cluster has two distinct caches – Item cache and Query cache.**

- Item cache
  - Item remains in the DAX item cache, subject to the Time to Live (TTL) setting and the least recently used (LRU) algorithm for the cache
  - DAX provides write-through cache, keeping the DAX item cache consistent with the underlying DynamoDB tables.
- Query cache
  - DAX caches the results from Query and Scan requests in its query cache
  - Query and Scan results don’t affect the item cache at all, as the result set is saved in the query cache – not in the item cache.
  - Writes to Item cache don’t affect the Query cache
- Item and Query cache has a default 5 minutes TTL setting.

## What is DDB read consistency?

Consistency is the ability to read data with the understanding that all prior writes will be reflected in the results returned.

- Often this is referred to as read-after-write consistency. Writes by definition are consistent, but reads can be “strongly” consistent or “eventually” consistent. This choice is made by the client each time a read request is made.

- Eventual consistency is the default behavior, with strong consistency available as an option for each read operation. We can walk through an example of the difference with this diagram. The client writes an update to Key1, and it is durably persisted.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/Qntlc9mCQxPojyf2_EG0FLrG4WMYPiJtl.png)


## What is Read and Write Capacity?

**Read and Write Capacity Units**
Throughput is specified in terms of:

-  read capacity units (RCU) - the number of strongly consistent reads per second of items up to 4 KB in size
- write capacity units (WCU) -  the number of 1 KB writes per second

## How we handle DDB resilient behavior?

**Handle 400 and 500 Error Codes Gracefully**

For more information about handling DynamoDB errors, see: http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html

Handle 400 and 500 error codes gracefully to ensure a smooth customer experience.

For some 400 errors, you should fix the issue before re-submitting the request. For example:

- There was a problem with the request.
- Some required parameters were missing.

For other 400 errors, you can retry until the request succeeds. For example:

- Provisioned throughput was exceeded.

You can retry 500 errors until the request succeeds. For example

- An internal server error occurred.
- The service was unavailable

## How to calculate Target Utilization in DynamoDB table

ynamoDB provides an [Autoscaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) option for managing throughput capacity. With autoscaling you define a minimum, maximum and target utilization.

DynamoDB Autoscaling will then vary the provisioned throughput between the maximum and mimumum bounds set. It will aim to keep this throughput provision at the utilization capacity.

> Target utilization is the ratio of consumed capacity units to provisioned capacity units, expressed as a percentage

A good starting point is to ask why not set target utilization to 100%? This sounds efficient, because you will only be paying for the throughput you use. But there is a problem to this:

> DynamoDB auto scaling modifies provisioned throughput settings only when the actual workload stays elevated (or depressed) for a sustained period of several minutes

So, imagine your target utilization is 100% and you have increased demand on your table for 15 minutes. For the first 5 minutes you might be saved by [burst capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html#bp-partition-key-throughput-bursting), in the second lot of 5 minutes you are likely to see database read/write failures as your throughput is exceeded, and then after around 10 minutes Autoscaling should kick in and increase your throughput.

In summary, **your target utilization should be a function of how quickly your throughput capacity changes, and how averse you are to throttling.**

## What is Amazon DynamoDB global tables?

Global tables build on the global Amazon DynamoDB footprint to provide you with a fully managed, multi-region, and multi-active database that delivers fast, local, read and write performance for massively scaled, global applications. Global tables replicate your DynamoDB tables automatically across your choice of AWS Regions.

Refer to https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables.tutorial.html

**How it works**?

When you create a DynamoDB global table, it consists of multiple replica tables (one per AWS Region) that DynamoDB treats as a single unit. Every replica has the same table name and the same primary key schema. When an application writes data to a replica table in one Region, DynamoDB propagates the write to the other replica tables in the other AWS Regions automatically.

![Diagram showing how global tables work](https://d1.awsstatic.com/product-marketing/DynamoDB/DynamoDB_Global-Tables-01.dad2508b80e8b7c544fe1a94a2abd3f770b789da.png)

For example, suppose that you have a large customer base spread across three geographic areas—the US East Coast, the US West Coast, and Western Europe. Customers can update their profile information by using your application. Without a managed replication solution, you could write code to replicate data changes among the tables for each of these Regions. However, doing this would be a time-consuming and labor-intensive effort.

**Instead of writing your own code, you could create a global table referencing your three Region tables and DynamoDB would then automatically replicate data changes among those tables so that changes to one Region would seamlessly propagate to the other Regions. In addition, if one of the AWS Regions were to become temporarily unavailable, your customers could still access the same data in the other Regions**

## What is TTL?

Amazon DynamoDB Time to Live (TTL) allows you to define a per-item timestamp to determine when an item is no longer needed. Shortly after the date and time of the specified timestamp, DynamoDB deletes the item from your table without consuming any write throughput. TTL is provided at no extra cost as a means to reduce stored data volumes by retaining only the items that remain current for your workload’s needs.

TTL is useful if you store items that lose relevance after a specific time. The following are example TTL use cases:

- Remove user or sensor data after one year of inactivity in an application.
- Archive expired items to an Amazon S3 data lake via Amazon DynamoDB Streams and AWS Lambda.
- Retain sensitive data for a certain amount of time according to contractual or regulatory obligations.

For more information about TTL, see these topics:

- [Using Time to Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-before-you-start.html).
- [Time to Live: How It Works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html).
- [Enabling Time to Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html).

## How DDB Backup and Restore happens?

Amazon DynamoDB provides on-demand backup and restore capabilities. When you create an on-demand backup, a time marker of the request is cataloged. 

The backup is created asynchronously by applying all changes until the time of the request to the last full table snapshot. Backup requests are processed instantaneously and become available for restore within minutes.

Each time you create an on-demand backup, the entire table data is backed up. All backups in DynamoDB work without consuming any provisioned throughput on the table.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/IvgksuX8Ge5i3WEK_rj0UWPvuxjiJFAMu.png)

## What are design consideration of DDB?

The partition key determines the distribution of data across the partitions where data is stored. The total throughput provisioned for a table is divided equally across partitions.

When you make a large number of consecutive reads or consecutive writes to a narrow range of partition keys, the same partitions are accessed repeatedly (hot partitions). The throughput allocated to remaining partitions remains unused.

To achieve **maximum read and write throughpu**t, implement your read and write operations as follows:

- Choose the partition key carefully to avoid hot spots.
- Consider concatenating a random number or a calculated value to the partition key when writing data to ensure distribution of partition keys. For example, you might concatenate the sum of the ASCII values of each character in the partition key.
- Distribute reads and writes across multiple partitions.

 ![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/X17odh0usOzwUQTl_xLdJxJyb3NsXOdaH.jpg)

## How you manage Hot and Cold data in DynamoDB?

Consider access patterns for your data. For example, you might have an Orders table with a partition key of customer id and sort key of timestamp. Your application probably accesses the latest order data most of the time. It might rarely access data about very old orders.

**In such cases, consider breaking the time series data into separate tables**. **Store the frequently accessed “hot” data in a separate table with higher throughput. Store rarely accessed “cold” data in tables with lower throughpu**t.

You can even move the old data to other storage options such as an Amazon S3 bucket and delete the table that contains the old data.

![img](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/zLRSR8BZToQjUy0p_RLATg2_UcXnyO9ad.jpg)

## How we manage large attributes in DDB?

Ideally you want to keep items small, and DynamoDB imposes limits on the size of an item.  There are several ways to address this:

![img](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/CFMLqaD5YZM5UxX1_YLx4Ieqc7xZ_oHmw.png)

- Consider storing large attribute values in Amazon S3
- Compress large values before storing in DynamoDB.
- Break up large attributes across multiple items.

## How to Use Optimistic Locking with Version Number in DDB for read/update?

Use optimistic locking with a version number as described below to make sure that an item has not changed since the last time you read it. This approach is also known as the read-modify-write design pattern or optimistic concurrency control.

![Maintain a version number to check that the item has not been updated between the last read and update.](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/rKo8x8vM44rT0Lcy_4QmB61JkCCKiCDbk.jpg)

Maintain a version number to check that the item has not been updated between the last read and update.

1. Read the item and remember the version number (versionNum = 0).
2. Make the state transition in memory after validating information (accountLocked = N if currentLoginTime > lastFailedLoginTime + 24 hours).
3. Increment the version number (versionNum = 1).
4. Write the item with updated attributes (accountLocked = N and versionNum = 1). Use a conditional expression to perform a write only if the item has not changed since it was last read.
5. If the condition fails, start over from step 1.

## What are the best practice for LSI and GSI?

Local secondary indexes consume storage and the table's provisioned throughput. Keep the size of the index as small as possible.

- Use indexes sparingly.
- Choose projections carefully.
- Project only those attributes that you request frequently. 
- Take advantage of sparse indexes.

GSI acts like any other table - choose a partition key and sort key that will distribute reads across multiple partitions.

- Take advantage of sparse indexes.
- Create a global secondary index with a subset of table’s attributes for quick lookups.
- Use as an eventually consistent read replica.

## How GSI updates works and what is GSI backpressure?

Throttling on a GSI affects the base table in different ways, depending on whether the throttling is for read or for write activity:

- When a GSI has insufficient read capacity, the base table isn't affected.
- When a GSI has insufficient write capacity, write operations don't succeed on the base table or any of its GSIs.

![im](https://image.slidesharecdn.com/designpatternsusingamazondynamodb-sfloft2016-160210184742/95/design-patterns-using-amazon-dynamodb-15-638.jpg?cb=1455219214)

**Resolution**

To prevent throttling, do the following:

- Be sure that the provisioned write capacity for each GSI is equal to or greater than the provisioned write capacity of the base table. To modify the provisioned throughput of a GSI, use the [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html) operation. If automatic scaling is turned on for the base table, then it's a best practice to apply the same settings to the GSI. You can do this by choosing **Copy from base table** in the DynamoDB console. For best performance, be sure to turn on **Use the same read/write capacity settings for all global secondary indexes**. This option allows DynamoDB auto scaling to uniformly scale all the global secondary indexes on the base table. For more information, see [Enabling DynamoDB auto scaling on existing tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html#AutoScaling.Console.ExistingTable).
- Be sure that the GSI's partition key distributes read and write operations as evenly as possible across partitions. This helps prevent hot partitions, which can lead to throttling. For more information, see [Designing partition keys to distribute your workload evenly](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html).

## What are options for Migrating an Existing Data to DynamoDB

 When migrating existing application data to DynamoDB, typically the API changes, as does the item model. If you can't afford down-time, you have a couple of options for migrating your data to DynamoDB:
 Live Migration

**Typical live migration steps include:**

1. Create DynamoDB table(s).
2. Modify application to write to both source and DynamoDB.
3. Perform a back-fill.
4. Verify.
5. Modify application to read from DynamoDB.
6. Modify application to write to DynamoDB only.
7. Shut down deprecated datastore.    

For exporting, transforming and importing data (such as for a back-fill), there are a number of popular options you can consider: AWS Data Pipeline, AWS Glue, and Amazon EMR with Hive (using the DynamoDB connector.

**AWS Data Migration Service (DMS)**

DMS is a service which can move data from a source (Cassandra, MongoDB, and a number of relational databases) to DynamoDB.

DMS can be used to make an initial copy of the full dataset, and then continue to update DynamoDB tables with any ongoing changes. When you are comfortable that the application is ready to make the switch, you deploy a new version of your software which uses the SDK to connect to DynamoDB instead.

Remember that this is an opportunity to optimize your design – you will want to remodel your data to better fit the DynamoDB service – particularly if migrating from a relational database.

## What are serverless architecture Patterns?

### DDB stream and Lambda

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/slPoKN8jjuhdZoam_bGLZD8FbnRuQYLuD.png)

The stream is sharded to scale out as throughput grows, and Lambda scales automatically to process data and push it to the next step. Any “write” activity can become a trigger and Lambda can filter and take actions based on the change. 

This serverless example illustrates using DynamoDB streams with Lambda to feed data from DynamoDB to other services (perhaps as part of a pipeline which could include a data lake).

### **Querying in Microservice Architectures**

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640091600/gy_Gw1DONQhxsTSKj7jazg/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/zsD3zFjuBe-Z5pd9_IjwUDFO2Ni33NZ9R.png)

**Challenges**

- Data is segregated in different microservices’ databases.
- Operational view of data does not satisfy querying needs.

**Solution**

- Separate operational and querying views
- Polyglot persistence: use the right database for the job
- Command Query Responsibility Segregation (CQRS)

### Time Series Data Example

The requirement is to collect and store temperature readings from potentially thousands of sensors. We also need to be able to quickly (<10ms) retrieve a reading for a given sensor and timestamp. We need to keep these for 30 days, after which they can be deleted.

**Initial Solution**

We implement this by having the sensors place their readings into a Kinesis Stream. We configure a Lambda function which polls the stream, and writes the readings into a DynamoDB table with SensorID as partition key, and timestamp as Sort Key.

Finally, we use a TTL attribute which is essentially timestamp plus 30 days. DynamoDB will delete those records for us after a month has passed.

![img](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640102400/IoG6MvjE4DyVEdNy9la61w/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/bxY9Mb9_D5Lu5Tj5_VwDYbOMIZnAHrrEC.png)

**Solution Architecture**

From the left, you can see the sensors pushing their readings to the Kinesis Stream. Lambda functions read from the stream and insert into the DynamoDB table.

Metrics are emitted to CloudWatch which we use for our operational monitoring. We keep the expired temperature readings for potential long-term analysis – as the recent readings expire via TTL, we use a triggered Lambda function to push them to Kinesis Firehose, which writes them to S3.

Users access a static website (hosted on S3) and authenticate via Cognito to query the temperature data from DynamoDB.

![im](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640102400/IoG6MvjE4DyVEdNy9la61w/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/jLdYok_lhcH5zmXv_vzjIblzfvYHzziZm.png)

**Cost Considerations**

Data rate: 100,000 data points per second

Data storage: 1 month’s worth = ~2.5 TB

Estimated cost:

- Lambda: $2K – $5K per month
- Kinesis: 100,000 records -> 100 shards -> ~$5K per month
- DynamoDB: 100,000 WCU’s -> $50K per month

Where is the problem? 

- DynamoDB Write Capacity Unit (WCU) is 1 KB
- Our scenario:
  - Storing data points ~50 B in size
  - Write capacity utilization per write: 50/1024 * 100% = 4.88%



**Revised Solution**

Let's try some queue-based load-leveling.  We can group multiple data points into a single item, saving on WCUs. Using the Lambda batch size, we can batch the data points into a single List attribute – and we can also use BatchWriteItem to improve our connection efficiency. We could also consider compressing the data. We’ll still rely on TTL for expiry.

How much does the revised design save us? If we look just at the DynamoDB WCUs, aggregating 10 data points per item saves us 90% of the cost. The difference over a year is more than $500k. We can save a lot by storing multiple data points in a single item.

![img](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1640102400/IoG6MvjE4DyVEdNy9la61w/tincan/bc1b00d1f241fed423cc99458cce9deb1976c143/assets/DyCpCwJbI76QdiCY_41N_eE8oW3Prd9_y.png)

**Scaling Considerations**

**Adding more sensors:** 

- Kinesis: you need to add more shards 
- Lambda: scales automatically based on Kinesis shards 
- DynamoDB: scales automatically for space and throughput
  - Auto Scaling increases and decreases provisioned capacity as needed
  - For large spikes, provision capacity explicitly
  - Time-to-live (TTL) automatically deletes expired data without consuming provisioned capacity

**Adding more events per sensor:**

- Lambda function creates “denser” DynamoDB items
- More data points stored in each DynamoDB item

  

# Event Bridge

## What is Event Bridge?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/event_bridge.JPG?raw=true)

## Share some sample demo use case for event bridge?

- schedule cron to call lambda
- Invoke targets when pattern matching using “Predefined pattern by service”
  - When ec2 instance stops then lambda gets called
- Invoke target when event pattern matching “using custom patterns”
  - when custom event pattern matches then call lambda

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/event_bridge_demo.JPG?raw=true)

# Fargate and ECS

## What is container?

Hence, ***a\*** ***container\*** is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

## What is Docker?

Docker is a company that provides software (also called **Docker**) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/). This entire process of managing hundreds and thousands of containers to keep the application up and running is known as **container orchestration**

## What are components of fargate?

- A **Task** is one or more containers that are to be scheduled together by ECS.

- A **Service** is like an Auto Scaling group for tasks. It defines the number of tasks to run across the cluster, where they should be running, automatically associates them with a load balancer, and horizontally scales based on metrics that you define like memory utilization, etc.

- Another important AWS service is **Elastic Container Registry(ECR)**, It is a registry to store, manage our container images.

## What is AWS Elastic Container Service (ECS)?

Amazon Elastic Container Service (Amazon ECS) is Amazon’s home-grown container orchestration platform. The idea behind ECS is similar to Kubernetes *(both of them are orchestration services)*.

ECS is an AWS-native service, meaning that it is only possible to use on AWS infrastructure. On the other hand, **EKS** is based on Kubernetes, an open-source project which is available to users running on multi-cloud (AWS, GCP, Azure) and even On-Premise.

Irrespective of whichever container orchestration service you are using (ECS or EKS), there are two ways you can implement the underlying infrastructure:

- Manually manage the cluster and underlying infrastructure such as Virtual Machines / Servers / (also known as EC2 instances in AWS).

- Serverless — Absolutely no need to manage anything. Just upload the container and that’s it. ← **This is AWS Fargate.**

![img](https://miro.medium.com/max/700/1*k4famzZ1w2Ee5XMHRo1Ggw.png)

## What is advantage of fargate?

Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. You only pay for the resources required to run your containers, so there is no over-provisioning and paying for additional servers.

There is no best answer as to which approach is better. The choice between going serverless or manually managing an EC2 cluster depends on the use-case. Some pointers that can assist with this choice include:

**ECS EC2 (Manual Approach)**

- You are all-in on AWS.
- You have a dedicated Ops team in place to manage AWS resources.
- You have an existing footprint on AWS i.e. you are already managing EC2 instances

**AWS Fargate**

- You do not have huge Ops team to manage AWS resources.
- You do not want operational responsibility or want to reduce it.
- Your application is stateless *(A stateless app is an application that does not save client data generated in one session for use in the next session with that client)*.

## Explain how fargate and ECS related?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/ECS-Container.JPG?raw=true)

- push docker container image into ECR
- Create a cluster with fargate as option
- Create the task within cluster with fargate type
  - add container details within task
- Now run the task

# Elastic Cache

## What is Amazon ElastiCache?

Amazon ElastiCache is an in-memory key-value store which is capable of supporting two key-value engines – Redis and Memcached. It is a fully managed and zero administrations which are hardened by Amazon. With the help of Amazon ElastiCache, you can either build a new high-performance application or improve the existing application. You can find the various application of ElastiCache in the field of Gaming, Healthcare, etc.

## What is the use of Amazon ElastiCache?

The performance of web applications could be improved with the help of the caching of information that is used again and again. The information can be accessed very fast using in-memory-caching. With ElastiCache there is no need of managing a separate caching server. You can easily deploy or run an open source compatible in-memory data source with high throughput and low latency.

## What are the benefits of Amazon ElastiCache?

There are various benefits of using Amazon ElastiCache some of which are discussed below:

- The cache node failures are automatically detected and recovered.
- It can be easily integrated with other AWS so as to provide a high performance and secured in-memory cache.
- As most of the data is managed by ElastiCache such as setup, configuration, and monitoring so that the user can focus on other high-value applications.
- The performance is enhanced greatly as it only supports the applications which require a very less response time.
- The ElastiCache can easily scale itself up or scale down according to the need.

## What is an ElastiCache cluster?

A cluster is a collection of nodes. When you have a Memcached node then the nodes can be in multiple availability zones and in case of Redis cluster there is only a single node i.e. the master node and does not support data partitioning.

![ElastiCache Cluster](https://www.whizlabs.com/blog/wp-content/uploads/sites/2/2018/11/elasticache.png)

## Explain the types of engines in ElastiCache.

There is two type of engine supported in Elasticache: Memcached and Redis.

##### Memcached

It is a popular in-memory data store which the developers use for the high-performance cache to speed up applications. By storing the data in memory instead of disk Memcached can retrieve the data in less than a millisecond. It works by keeping every value of the key for every other data to be stored and uniquely identifies each data and lets Memcached quickly find the record.

##### Redis

Today’s applications need low latency and high throughput performance for real-time processing. Due to the performance, simplicity, and capability of redis, it is most favored by the developers. It provides high performance for real-time apps and sub-millisecond latency. It supports complex datatypes i.e. string, hashes, etc and has a backup and restore capabilities. While Memcached supports key names and values up to 1 MB only Redis supports up to 512 MB.