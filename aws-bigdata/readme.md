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

![im](https://image.slidesharecdn.com/analyzing-real-time-streaming-d5157d72-01dd-4cf4-b1ac-986f841eb01e-1836541165-170717165601/95/analyzing-realtime-streaming-data-with-amazon-kinesis-19-638.jpg?cb=1500310572)

**Destination can be**

- S3
- Redshift
- ElasticSearch

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/kinesis-firehose.JPG?raw=true)

- It is a service that serves as a tool for the ingestion of streaming data from various data sources to the data sinks in a secure way. It can handle an ample amount of data stream workloads and scale accordingly.

- When we get started with Kinesis Data Firehose, we first have to register a delivery stream, and It is the source of streaming data that we will save. Firehouse also provides the functionality to convert the streaming data chunks into other data formats so that it is easy to query or store in the data lake or data warehouse. Next, we define a lambda function in case we want to perform such a data transformation. Firehose comes with pre-configured AWS Lambda blueprints and templates that make it even easy to implement it. Last and the final step is selecting the data source and the data format we want to store the data. It automatically scales up and scales down depending upon the velocity of the data streams.

- Kinesis Data Firehose is primarily made for a data pipeline where we want to store the streaming records to a data lake, in case you want to do processing or any analysis on the streaming data in real-time AWS Kinesis data analytics service is the best suited. Here is the list of supported data sources and sinks - **Data sources -** Streaming data from AWS Kinesis Agent, Firehose PUT API's, AWS IOT, CloudWatch Logs, CloudWatch Events. **Data sinks-** Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon Elasticsearch Service (Amazon ES), and Splunk. AWS Kinesis Data Analytics.

#### kinesis firehose data flow

- For **Amazon S3 destinations**, streaming data is delivered to your S3 bucket. If data transformation is enabled, you can optionally back up source data to another Amazon S3 bucket.

- For **Amazon Redshift destinations**, streaming data is delivered to your S3 bucket first. Kinesis Firehose then issues an Amazon Redshift copy command to load from your S3 bucket to your Amazon Redshift cluster. If data transformation is enabled, you can optionally back up source data to another Amazon S3 bucket. Note that you need to configure your Amazon Redshift cluster to be publicly accessible and unblock the Kinesis Firehose IP addresses. Also note that Kinesis Firehose doesn't delete the data from your S3 bucket after loading it to your Amazon Redshift cluster. 
- For **Amazon Elasticsearch destinations**, streaming data is delivered to your Amazon Elasticsearch cluster and can optionally be backed up to your S3 bucket concurrently. There are a number of limits within [Amazon Kinesis Firehose service](https://cloudacademy.com/course/aws-big-data-specialty-data-collection/kinesis-wrap-up/) you need to be aware of.

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/firehose-data-flows.JPG?raw=true)



## Difference between stream and firehose

![im](https://image.slidesharecdn.com/analyzing-real-time-streaming-d5157d72-01dd-4cf4-b1ac-986f841eb01e-1836541165-170717165601/95/analyzing-realtime-streaming-data-with-amazon-kinesis-22-638.jpg?cb=1500310572)

# Snowball

AWS Snowball is a service that **provides secure, rugged devices**, so you can bring AWS computing and storage capabilities to your edge environments, and transfer data into and out of AWS. Those rugged devices are commonly referred to as AWS Snowball or AWS Snowball Edge devices.

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/sowball_architecture.JPG?raw=true)

# AWS Big Data Specialty - Processing

## What You'll Learn

- Course Intro: What to expect from this course
- Amazon Elastic MapReduce Overview: In this lesson, we discuss how EMR allows you to store and process data
- Amazon Elastic MapReduce Architecture: In this lesson, you’ll learn about EMR’s clustered architecture.
- Amazon Elastic MapReduce in Detail: In this lesson, we’ll dig deeper into EMR storage options, resource management, and processing options.
- Amazon Elastic MapReduce Reference Architecture: Best practices for using EMR.
- Amazon Lambda Introduction: This lesson will kick off our discussion of Lambda and how it’s used in Big Data scenarios.
- Amazon Lambda Overview: This lesson discusses how Lambda allows you to run code for virtually any type of application or backend service with no administration.
- AWS Lambda Architecture: In this lesson, we’ll discuss generic Lambda architecture and Amazon’s serverless service.
- AWS Lambda in Detail: In this lesson, we’ll dig into Events and Service Limits.
- AWS Lambda Reference Architecture: In this lesson, we'll look at a real-life scenario of how lambda can be used.

## EMR Overview

With Amazon EMR, you can leverage multiple data stores, including Amazon S3, the Hadoop Distributed File System (HDFS), and Amazon DynamoDB.

Amazon EMR is targeted at providing processing patterns at a speed and scale that relational databases cannot achieve. 

Amazon EMR is primarily designed to deliver batch orientated processing. As well as processing data, Amazon EMR can also store data. When choosing a big data storage solution from within the available AWS service offerings, it is important to determine whether the data sources we are primarily storing contain structured, semi structured, or unstructured data. This will typically drive the decision on which AWS service is the best for that data pattern or use case.

Amazon EMR is primarily designed to manage semi structured data, and it is designed for schema on read. Schema on read is where you apply the structure to the data you are using as you read it, so we're effectively creating and applying the structure within your code rather than defining the structure in the database before you load it. Amazon EMR provides a framework that allows you to easily create, customize, and manage big data processing clusters based on the Apache Hadoop ecosystem. EMR stands for Elastic MapReduce. Underlying your EMR environment is a cluster of Amazon EC2 instances that house the Hadoop ecosystem of open source applications you need to access, process, and manage large volumes of data.

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/emr-architecture.JPG?raw=true)

- Each EMR cluster will have only one master node
- The Core Node is a Slave Node, which stores data in the Hadoop Distributor File System, or HDFS and also runs tasks. 
- A Task Slave Node only runs tasks, it does not store data. Task Nodes are optional when you're creating an EMR Cluster.
- When scaling down your EMR environment you cannot remove Core Nodes but you can remove Task Nodes. This is because Core Nodes hold the data, so if you were to remove them you would lose that data. Whereas Task Nodes do not hold data so they can be used to scale your Cluster computer power up and down. 

You are able to use different components at each of the layers but they all have pros and cons and they will change how your Amazon EMR solution will work or behave.

- The key three layers you need to worry about for your EMR Cluster are what you use for storage, processing and access
- An important option to note is that there are two launch modes you can use when creating your EMR environment, a Persistent Cluster and a Transient Cluster.
- When you select Cluster as the launch mode, the EMR Cluster is created as a Persistent Cluster and continues running until you decide to terminate it. When you select Step Execution, you define what steps you want the EMR environment to run. Those steps drive the applications that are automatically installed when you create the Cluster. Once those steps are executed, the Cluster is automatically terminated.
- Options
  - The first thing you need to decide is what storage component you want to use. You have three choices. You can use the Hadoop Distributed File System or HDFS, the EMR file system or EMRFS, or a local file system. We will talk through each of these storage options and details in a few minutes. The Resource Management layer is responsible for managing the Cluster resources and scheduling the jobs for processing data.
  - The next thing to choose is the processing engine you wish to use. At this time there are currently four choices: Hadoop MapReduce with TEZ, Presto, Hbase or Spark.
  - The last layer to decide on is the applications and tools that will sit on top of the EMR storage and processing engine to allow you to enter it with a required data and code. Amazon EMR supports many applications, such as Hive, Pig and the Spark streaming libraries to provide capabilities such as using high level languages to concern processing workloads,
- 

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/emr-detailed_architecture.JPG?raw=true)

![im](https://d1.awsstatic.com/Image_Thumbs/emr/DetailsPage_EMR-Diagram.f8045894990ffff76cb92421d82523675e1f7139.png)

### EMR Storage options

| ile system                           | Prefix                   | Description                                                  |
| :----------------------------------- | :----------------------- | :----------------------------------------------------------- |
| HDFS                                 | `hdfs://` (or no prefix) | HDFS is a distributed, scalable, and portable file system for Hadoop. An advantage of HDFS is data awareness between the Hadoop cluster nodes managing the clusters and the Hadoop cluster nodes managing the individual steps. For more information, see [Hadoop documentation](http://hadoop.apache.org/docs/stable).HDFS is used by the master and core nodes. One advantage is that it's fast; a disadvantage is that it's ephemeral storage which is reclaimed when the cluster ends. It's best used for caching the results produced by intermediate job-flow steps. |
| EMRFS                                | `s3://`                  | EMRFS is an implementation of the Hadoop file system used for reading and writing regular files from Amazon EMR directly to Amazon S3. EMRFS provides the convenience of storing persistent data in Amazon S3 for use with Hadoop while also providing features like Amazon S3 server-side encryption, read-after-write consistency, and list consistency.**Note**Previously, Amazon EMR used the `s3n` and `s3a` file systems. While both still work, we recommend that you use the `s3` URI scheme for the best performance, security, and reliability. |
| local file system                    |                          | The local file system refers to a locally connected disk. When a Hadoop cluster is created, each node is created from an EC2 instance that comes with a preconfigured block of preattached disk storage called an *instance store*. Data on instance store volumes persists only during the life of its EC2 instance. Instance store volumes are ideal for storing temporary data that is continually changing, such as buffers, caches, scratch data, and other temporary content. For more information, see [Amazon EC2 instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html). |
| (Legacy) Amazon S3 block file system | `s3bfs://`               | The Amazon S3 block file system is a legacy file storage system. We strongly discourage the use of this system.**Important**We recommend that you do not use this file system because it can trigger a race condition that might cause your cluster to fail. However, it might be required by legacy applications. |

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/emr-storage.JPG?raw=true)

### EMR Resource Management

YARN stands for Yet Another Resources Negotiator and is the architectural center of Hadoop that allows multiple data processing engines to execute their code. By default, Amazon EMR uses YARN to centrally manage cluster resources from multi data processing frameworks. Amazon EMR also has an agent on each node which administers YARN components, keeping the clusters healthy and communications with the Amazon EMR service.

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/emr-resource-management.JPG?raw=true)

### EMR Processing Options

The Apache Hadoop MapReduce provides three core components; one, the end-user MapReduce API for programming the desired MapReduce duplications, two, the MapReduce framework which is the runtime implementation of various phases such as the met phase, the sort, shuffle, merge, aggregation and reduces; and three, the MapReduce system which is the back end of the structure required to run the user's MapReduce duplication, manage the cluster resources and schedule thousands of concurrent jobs.

- The job tracker was responsible for resource management, managing the work nodes called task trackers. Task trackers track resource consumption and availability as well as also job life cycle management such as scheduling individual tasks of the job, tracking progress and providing fault tolerance for tasks. The task tracker had simple responsibilities, launching or tearing down tasks on order from the job tracker and to provide task status information to the job tracker periodically.
- The reduce function combines the intermediate results, applies additional algorithms and produces the final output. 
- An Hbase system comprises a set of tables. **Each table contains rows and columns much like a traditional database**. Each table must have an element defined as a primary key and allto Hbase tables must use this primary key. An Hbase column represents an attribute of an object. For example, the table storing diagnostic logs from servers in your environment where each room might be a log report. **A typical column is such a table would be the timestamp of when the log report was written** or perhaps the server name where the record originated. Hbase works as seamlessly with Hadoop, sharing its file system and serving as a direct input and output to the MapReduce framework and execution engine. 

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/emr-processing_options.JPG?raw=true)

### When to use EMR?

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/use-emr.JPG?raw=true)

## Lambda

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/lambda-use-case.JPG?raw=true)

### Lambda Architecture

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/lambda_architecture.JPG?raw=true)

### Lambda Events

![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/aws-bigdata/lambda-events.JPG?raw=true)

## SmartNews Built a Lambda Architecture on AWS to Analyze Customer Behavior and Recommend Content

![im](https://dmhnzl5mp9mj6.cloudfront.net/bigdata_awsblog/images/SmartNewsImage1a.png)

Key observation from this architectures:

- To make data platform sustainable, they decided to completely separate the compute and storage layers. They adopted [Amazon S3](https://aws.amazon.com/s3/) for file storage and [Amazon Kinesis Streams](https://aws.amazon.com/kinesis/streams/) for stream storage. Both services replicate data into multiple  Availability Zones and keep it available without high operation costs.  We don’t have to pay much attention to the storage layer and we can  focus on the computation layer that transforms raw data to a valuable  output.
- Amazon S3 and Amazon Kinesis Streams let us run multiple compute layers  without complex negotiations. After data is stored, everyone can consume it in their own way

### Input data

- User activity logs include more than 60 types of activities to  understand user behavior such as which news articles are read. After we  receive logs from the mobile app, all logs are passed to [Fluentd](http://www.fluentd.org/), an OSS log collector, and forwarded to Amazon S3 and Amazon Kinesis Streams. If you are not familiar with Fluentd, see [Store Apache Logs into Amazon S3](https://docs.fluentd.org/v/0.12/articles/apache-to-s3) and [Collect Log Files into Kinesis Stream in Real-Time](https://docs.fluentd.org/how-to-guides/kinesis-stream) to understand how Fluentd works.
- Our recommended practice is adding the flush_at_shutdown parameter. If set to true, Fluentd waits for the buffer to flush at shutdown. Because our  instances are scaled automatically, it’s important to store log files on Amazon S3 before terminating instances.
- In addition, monitoring Fluentd status is important so that you know when bad things happen. We use [Datadog](https://www.datadoghq.com) and some Fluentd plugins. Because the [Fluent-plugin-flowcounter](https://github.com/tagomoris/fluent-plugin-flowcounter) counts incoming messages and bytes per second, we post these metrics to [Dogstatsd ](http://docs.datadoghq.com/guides/dogstatsd)via [Fluent-plugin-dogstatsd](https://github.com/ryotarai/fluent-plugin-dogstatsd). An example configuration is available in a [GitHub Gist post](https://gist.github.com/takus/1658aaa853f8d0d3d5c4ca1b5ba3ed20). After metrics are sent to Datadog, we can visualize aggregated metrics across any level that we choose. The following graph aggregates the number of records per data source.
  - 

### Batch layer

- This layer is responsible for various ETL tasks such as transforming  text files into columnar files (RCFile or ORCFile) for following  consumers, generating machine learning features, and pre-computing the  batch views.

- We run multiple [Amazon EMR](https://aws.amazon.com/elasticmapreduce) clusters for each task. Amazon EMR lets us run multiple heterogeneous [Hive](https://hive.apache.org) and [Spark](http://spark.apache.org) clusters with a few clicks. Because all data is stored on Amazon S3, we can use [Spot Instances](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-plan-spot-instances.html) for most tasks and adjust cluster capacity dynamically. It  significantly reduces the cost of running our data processing system.
- When using a cron scheduler, a developer needs to write additional code  to handle dependencies such as waiting until the previous task is done,  or failure handling such as retrying failed tasks or specifying timeouts for long-running tasks. We use [Airflow](https://github.com/airbnb/airflow), an open-sourced task scheduler, to manage our ETL tasks. We can define ETL tasks and dependencies with Python scripts.

### Serving layer

The serving layer indexes and exposes the views so that they can be queried.

- We use [Presto](https://prestodb.io/) for this layer. Presto is an open source, distributed SQL query engine for running interactive queries against various data sources such as Hive tables on S3, MySQL on Amazon RDS, Amazon Redshift, and Amazon Kinesis Streams. Presto converts a SQL query into a series of task stages and processes each stage in parallel. Because all processing occurs in memory to reduce disk I/O, end-to-end latency is very low: ~30 seconds to scan billions of records.
- With Presto, we can analyze the data from various perspectives. 

### Speed layer

- Like the batch layer, the speed layer computes views from the data it receives. The difference is latency. Sometimes, the low latency adds variable outputs for the product.
- For example, we need to detect current trending news by interest-based clusters to deliver the best stories for each user. For this purpose, we run [Spark Streaming](http://spark.apache.org/streaming).
- User feedback in Amazon Kinesis Streams is joined on the interest-based user cluster data calculated in offline machine learning, and then the output metrics for each news article. These metrics are used to rank news articles in a later phase. What Spark Streaming does in the above figure looks something like the following:

![im](https://dmhnzl5mp9mj6.cloudfront.net/bigdata_awsblog/images/SmartNewsImage5.PNG)

### Output data

- [Chartio](https://chartio.com/) is a commercial business intelligence (BI) service. Chartio enables every member (including non-engineers!) in the company to create, edit, and refine beautiful dashboards with minimal effort. 
- Because Chartio supports various data sources such as Amazon RDS (MySQL, PostgreSQL), Presto, PipelineDB, [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/) (successor to Amazon Elasticsearch Service), you can start using it easily.

# References

- https://www.xenonstack.com/blog/aws-big-data
- https://aws.amazon.com/blogs/big-data/how-smartnews-built-a-lambda-architecture-on-aws-to-analyze-customer-behavior-and-recommend-content/