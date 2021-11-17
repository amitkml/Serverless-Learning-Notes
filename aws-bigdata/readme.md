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