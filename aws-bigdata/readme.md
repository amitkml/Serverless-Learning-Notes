# AWS Big Data Specialty - Data Collection

- Introduction to Data Pipeline: In this lesson, we'll discuss the basics of Data Pipeline.
- AWS Data Pipeline Architecture: In this lesson, we'll go into more detail about the architecture that underpins the AWS Data Pipeline Big Data Service.
- AWS Data Pipeline Core Concepts: In this lesson, we'll discuss how we define data nodes, access, activities, schedules, and resources.
- AWS Data Pipeline Reference Architecture: In this lesson, we'll look at a real-life scenario of how data pipeline can be used.
- Introduction to AWS Kinesis: In this lesson, we'll take a top-level view of Kinesis and its uses.
- Kinesis Streams Architecture: In this lesson, we'll look at the architecture that underpins Kinesis.
- Kinesis Streams Core Concepts: In this lesson, we'll dig deeper into the data records.
- Kinesis Streams Firehose Architecture: In this lesson, we'll look at firehose architecture and the differences between it and Amazon Kinesis Streams.
- Firehose Core Concepts: Let's take a deeper look at some details about the Firehose service.
- Kinesis Wrap-Up: In this summary, we'll look at the differences between Kinesis and Firehose.
- Introduction to Snowball: Overview of the Snowball Service.
- Snowball Architecture: Let's have a look at the architecture that underpins the AWS Snowball big data service
- Snowball Core Concepts: In this lesson, we'll look at the details of how Snowball is engineered to support data transfer.
- Snowball Wrap-Up: A brief summary of Snowball and our course.

# Data Pipeline

## Steps

- Collect
  - aws data pipeline
  - aws kinesis
  - aws snowball
- store
  - S3
  - DDB
  - Glacier
- process
  - aws lambda
  - EMR
- analyze
  - Kinesis analytics
  - cloudwatch

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/aws-bigdata.JPG?raw=true)

## AWS Data Pipeline

AWS Data Pipeline helps you sequence, schedule, run, and manage recurring data processing workloads reliably and cost-effectively. This service makes it easy for you to design extract-transform-load (ETL) activities using structured and unstructured data, both on-premises and in the cloud, based on your business logic.

### processing patterns

- real time streaming - sub ms response time
- transactions - sub sec response time
- queued
- batch execution

### storage pattern

- structured : relational data: schema on write
- unstructured: media, binary etc: no schema
- semi structured: log files: schema on read

### How the Data Pipeline Works?

The main components of the Data pipeline are -

- Pipeline Definition
- Task Runner
- Pipeline Logging

#### Pipeline Definition

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/aws-pipeline.JPG?raw=true)

Data pipeline data nodes

- Dynamo DB
- RDS
- S3
- Redshift

![im](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/images/dp-ddb-export-template.png)

The pipeline can be created in 3 ways -

- Graphically, using the AWS console or AWS pipeline Architect UI.
- Textually, writing a JSON file format.
- Programmatically, using the AWS data pipeline SDK.

A Pipeline can contain the following components -

- **Data Nodes -** The section of input data for a task or the location where output data is to be collected.
- **Activities -** A description of work to perform on a program using a computational means and typically input and output data nodes.
- **Preconditions -** A conditional statement that must be true before action can run.
- **Scheduling Pipelines -** Marks the timing of a planned event, such as when an action runs.
- **Resources -** The computational resource that performs the work that a pipeline defines.
- **Actions -** An action that is triggered when specified conditions are met, such as the failure of an activity.

#### Pipeline Logging

Logging is an essential part of data pipelines as it provides an insight into the internal working of the pipeline. The logging is done to the AWS cloud trail, and we can see the logs. AWS data pipeline service leverages the following compute and storage services -

#### Storage Services

- **Amazon DynamoDB -** Fully managed NoSQL database with fast performance.
- **Amazon RDS -** It is a fully managed relational database that can accommodate large datasets. Has numerous options for the database you want, e.g., AWS aurora, Postgres, Mssql, MariaDB**.**
- **Amazon Redshift -** Fully managed petabyte-scale Data Warehouse.
- **Amazon S3 -** Low-cost highly-scalable object storage.

#### Compute Services

- **Amazon EC2 -** Service for scalable servers in AWS data center, can be used to build various types of software services.
- **Amazon EMR -** Service for distributed storage and compute over big data, using frameworks such as Hadoop and Apache Spark.

#### Type of pipeline activity

AWS Data Pipeline supports the following types of activities:

- [CopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-copyactivity.html)                                                                     Copies data from one location to another.                                                                                 

- [EmrActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emractivity.html)                                                                       Runs an Amazon EMR cluster.                                                                                 

- [HiveActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-hiveactivity.html)                                                                      Runs a Hive query on an Amazon EMR cluster.                                                                                 

- [HiveCopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-hivecopyactivity.html)                                                             Runs a Hive query on an Amazon EMR cluster with support for advanced data                                             filtering and support for [S3DataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-s3datanode.html) and [DynamoDBDataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-dynamodbdatanode.html).                                                                                                                           

- [PigActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-pigactivity.html)                                                                   Runs a Pig script on an Amazon EMR cluster.                                                                                 

- [RedshiftCopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-redshiftcopyactivity.html)                                                 Copies data to and from Amazon Redshift tables.                                                                                 

- [ShellCommandActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-shellcommandactivity.html)

  ​                                                                                    Runs a custom UNIX/Linux shell command as an activity.                                                                                 

- [SqlActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-sqlactivity.html)                                                                  Runs a SQL query on a database.                                                                                 

#### Data pipeline components

- data pipeline schedules
- data pipeline task runner
  - polls pipeline for tasks and executes them
- data pipeline preconditions
  - system managed preconditions
  - user managed preconditions

## Reference Architecture - Time series data

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/time-series-processing.JPG?raw=true)

## Best practices for making AWS Big Data pipelines

- Define clear IAM roles to protect your data and resources among various users
- The volume of data expected.
- The velocity of data, the rate at which it is coming.
- Variety of data that the pipeline will be supporting.
- The validity of data in the pipeline.
- Create separate VPC to keep the data, resources, and pipeline protected.
- Monitor the pipeline using AWS CloudWatch.
- Select the tool by Big data 4 V's defined above to optimize the cost accordingly.

# Kinesis

- kinesis streams
- kinesis firehose
- kinesis analytics

## Kinesis stream

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/kinesis-stream.JPG?raw=true)

![im](https://images.ctfassets.net/ee3ypdtck0rk/3Nj7dlXrWjY6QGLJ2WlLQy/37e85ae7a0581d31792dd05dd0830e50/Screen_Shot_2021-08-27_at_16.31.30.png?w=1853&h=1059&q=50&fm=webp)

- One Kinesis Data Stream is made up of multiple shards, where the number of shards provisioned determines the billing. 
- Producers create records of data and stream them to Kinesis. A record is a data blob: it is serialized as bytes up to 1MiB in size and can represent any kind of data. 
- A record comprises of
  - data block in base 64 encoding which is record/payload
  - partition key - specified by producer by algorithm. This determine in which shard the data will be placed. shard and partition key is mapped.
  - sequence number - This is assigned by kinesis when records are placed into kinesis shard. Sequence number for same partition key generally grows over the time.
- A record also contains a record key, which is used to group it into a specific shard. After being ingested into the stream, Kinesis adds a unique identifier for each record. 
- The number of shards is unlimited. For each shard, all the records that are streamed to it are ordered.

### Kinesis Data Streams Limits

- Producers:
  - Each shard ingests up to 1 MiB/second and 1000 records/second, otherwise a` ProvisionedThroughputException `will be thrown.
- Consumer:
  - Maximum total data read is 2MiB/second per shard.
    - 5 API calls/second per shard.
- Data retention
  - By default 24 hours, extendable to 7 days

## Why Adopting AWS Kinesis Data Firehose Matters?

**Destination can be**

- S3
- Redshift
- ElasticSearch

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/kinesis-firehose.JPG?raw=true)

- It is a service that serves as a tool for the ingestion of streaming data from various data sources to the data sinks in a secure way. It can handle an ample amount of data stream workloads and scale accordingly.

- When we get started with Kinesis Data Firehose, we first have to register a delivery stream, and It is the source of streaming data that we will save. Firehouse also provides the functionality to convert the streaming data chunks into other data formats so that it is easy to query or store in the data lake or data warehouse. Next, we define a lambda function in case we want to perform such a data transformation. Firehose comes with pre-configured AWS Lambda blueprints and templates that make it even easy to implement it. Last and the final step is selecting the data source and the data format we want to store the data. It automatically scales up and scales down depending upon the velocity of the data streams.

- Kinesis Data Firehose is primarily made for a data pipeline where we want to store the streaming records to a data lake, in case you want to do processing or any analysis on the streaming data in real-time AWS Kinesis data analytics service is the best suited. Here is the list of supported data sources and sinks - **Data sources -** Streaming data from AWS Kinesis Agent, Firehose PUT API's, AWS IOT, CloudWatch Logs, CloudWatch Events. **Data sinks-** Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon Elasticsearch Service (Amazon ES), and Splunk. AWS Kinesis Data Analytics.

# References

- https://www.xenonstack.com/blog/aws-big-data