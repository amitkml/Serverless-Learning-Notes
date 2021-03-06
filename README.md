# Design and Delivery Tools
- Talk and share knowledge with co-workers, customers, students volunteers, users, community, customers, co-workers   https://www.talkyard.io/
- Design Tool - bit.ai
- Azure Devops - Pipeline for build, ADO board for deployment planning, work management. Retire jira
- [Google Cloud architecture diagramming tool](https://cloud.google.com/blog/topics/developers-practitioners/introducing-google-cloud-architecture-diagramming-tool)

# Serverless-Learning and AWS ML Learning Agenda

[Serverless on AWS](https://betterdev.blog/)


# AWS Billing and forecasting
- Cloudability : Online tool which can give visibility of spend and trends within an AWS account. 
- Monitoring/alarming : What can be setup to help track spend
- Forecast : Ensuring budget is thought about and included in the forecast for yearly spend for a project
- Responsibilities : Ensuring awareness of spend and ensuring we donโt have runaway costs eg lambda or s3. 

## Messaging Service (Decision Tree: choose the right AWS messaging service)
Refer the article https://betterdev.blog/decision-tree-sqs-sns-kinesis-eventbridge/
- ๐น SQS: Simple Queue Service (latency < 100ms)
Multiple producers and a single (parallelized) consumer. Each message is consumed only once. The consumer *pulls* messages.

-๐น SNS: Simple Notification Service (latency < 100ms)
One producer *pushes* messages to multiple consumers. For example, the same notification message is pushed to SMS, email, mobile app, etc. Each subscriber can have a filter and can consume only the messages with specified attributes.

-๐น Kinesis Data Streams (latency ~200ms)
Multiple producers, multiple distinct consumers. It is for streaming high volumes of data typical in data analytics. Each consumer pulls messages and tracks the last position in the stream that it has processed.

-๐น EventBridge (latency ~600ms)
Think of an event bus for truly decoupled (micro)services. Multiple producers, multiple consumers. Each subscriber can set a filter. Microservices, instead of calling other microservices, push messages to a single central bus. Each microservice listens for the types of messages it is interested in.
![im](https://media-exp1.licdn.com/dms/image/C5622AQH414IaHI8q1w/feedshare-shrink_2048_1536/0/1650256471047?e=2147483647&v=beta&t=Mmo7vQQ6JjJEu2hhvFYZrxadoFV9JuifaPEC0bchfpo)

# ML Notes
- https://aman.ai/read/
- https://aman.ai/watch/
- https://aman.ai/

## ML OPS
- https://github.com/zenml-io/zenml
- https://mlops.toys/#projects


## Generic ML 
- Frame ML problems
- Architect ML solutions
- Design data preparation and processing systems
- Develop ML models
- Automate & orchestrate ML pipelines
- Monitor, optimize, and maintain ML solutions
- Initial focus on Deep Learning and Transformers related to NLP (i.e. BERT, GPT)
- The requirements
- Excellent English skills - written & verbal

## AWS ML Learning agenda
- AWS Sagemaker
- Experience with ML and predictions
- Tensorflow and PyTorch in NLP
- Working with Real Time Data Flow
- Advanced proficiency with Python
- Amazon AWS platform
- AWS Sagemaker
- Lambda Function
- DynamoDB
- Atlassian agile collaboration tools - Jira & Confluence
- Zoom communication along with Gong.io AI-based call recording & analysis
- [New Serverless Transformers using Amazon SageMaker Serverless Inference and Hugging Face](https://www.philschmid.de/serverless-transformers-sagemaker-huggingface)

## AWS Learning Agenda
- Hands on experience in (any 6 points)
- End to end Cloud solution (AWS)  : In-Progress
- End to end Big data solution : AWS Big Data course completed
- Batch solution (aws glue/aws pipeline) : AWS Big data course complered
- Distributed compute solution (Spark, EMR)
- Analyze data through standard SQL (Athena) : AWS Big data course completed
- Functional solution (aws lambda) : AWS Couse done
- Distributed storage (redshift, S3) : S3 done by AWS Course
- Deep expertise in S3, Redshift, Spectrum, Glue, SQS, and SNS services.: Except Redshift all others are done
- Good in implement and manage AWS services covering compute (Ec2, lambda), network (VPC, endpoints, direct connect), identity and access management (IAM roles), storage and security services
- Good in creating and implementing Cloudformation templates and provision resources using Infra-as-code : Terraform course done
- Deep understanding of SQL Database technologies (RDS) and cloud-based analytics products (RedShift, Athena)
- Real-time solution (kafka, aws kinesis)
- DW-BI (Informatica, Oracle, Teradata)
- Demonstrated ability to think strategically about solutions to business, product, and technical challenges.
- Awareness of technology trends and how they impact the way businesses consume IT
- Support the Program in AWS deployments and innovative AWS solutions.
- Analyze user requirements, maintain operations documents, and propose high-level system architectures to develop system requirements specifications
- Design and arrangement of scalable, highly attainable, and fault tolerant systems on AWS.
-  Hands on experience in various cloud offerings such as Identity management Systems, Application Services, Serverless Code , NoCode Low code environments ,container orchestration ,DevOps etc
-  Preferred experience in S3, Glue, DynamoDB
- Assist with migration of architectures from the lab environment to the operational AWS environment.
- Experience building E2E Application right from backend database to persistent layer.
- Experience UI technologies Angular, react.js, Node.js or fullstack environment will be preferred.
- Experience with NoSQL technologies (MongoDB, Cassandra, Neo4j, Dynamodb, etc.)
- Elastic Search, Kibana, ELK, Logstash.: ELK STack course done
- Experience in developing Enterprise Software using Agile Methodology.
- Good understanding of Kafka, Redis, ActiveMQ, RabbitMQ, Solr etc.
- SaaS cloud-based platform exposure.
- Experience on Docker, Kubernetes etc.
- Ownership E2E design development and also quality enterprise product/application deliverable exposure
- A track record of setting and achieving high standards
- Strong understanding of modern technology architecture


## DEV OPS
- AWS Code Pipelines Experience with CI/CD and code management tools (Git, TFS, Jenkins, AWS Code Commit etc.)
- Writing infrastructure as code (CloudFormation, Terraform, AWS CDK ,Elastic Beanstalk, Code Suite)
- Linux/Windows administration, automated deployments, scripting (Bash/PowerShell/Python)
- Knowledgeable of configuration management frameworks such as Puppet, Chef or Ansible
- Familiarity with Continuous Integration, including experience with tools such as AWS Developer tools, AWS Code Pipelines
- Familiarity with Continuous Integration, including experience with tools such as AWS Developer tools, AWS Code Pipelines, AWS CodeBuild, AWS CodeDeploy
- Experience in implementing CICD pipeline for AWS project.
