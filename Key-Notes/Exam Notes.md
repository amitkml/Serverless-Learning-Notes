

# AWS ML Exam Notes

[TOC]

![IM](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/ML_Exam.JPG?raw=true)



# Exam Notes - ML Whitepapers

![1631203149917](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631203149917.png)



## Managing ML Projects

### Documenting the Data Catalog and Pipeline

A simple method of identifying potential challenges is to clearly diagram the data pipeline used to build the model, showing where all data is from and how it is transformed. The following is an example of how to annotate the pipeline diagram with this information:

-  Major data cleaning operations performed
- Records dropped, either as an actual count or as a percentage
- Major issues found with the data, for example, “duplicate records found and dropped”
- Assumptions made at the time, for example, “data was extracted for US only, other countries are assumed to be similar”

![img](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/pipeline-error.JPG?raw=true)

characteristics of the source data can also be captured in a Data Catalog table, such as Table 1. This catalog documents the current understanding of the data source, communicates to stakeholders the sources to be used and some basic facts about them, and helps identify potential mismatches, concerns, or clarify misunderstandings. For example, in Table 1, the change in storage format of data source #2 potentially adds a conversion or regularization task to the task list.

| Source                    | Contents                                                     | Duration                       | Quantity                | Comments                                                     |
| ------------------------- | ------------------------------------------------------------ | ------------------------------ | ----------------------- | ------------------------------------------------------------ |
| Data source #1: data lake | Clickstream data                                             | Jan 2018–Jan 2019              | 1.6M                    | User IP address only; user name not known                    |
| Data source #2: data lake | Order history                                                | June 1 2016–Oct 3 2018         | 55k orders              | Format stored in changed on Jan 1 2018
Final order only (not change history)
Orders with errors are deleted |
| Sensor data               | Readings from factory sensors. Streaming data is batched and stored | 90 days history retention only | 50/sec; 5k/sec expected | Data cleaning unknown; is perceived outlier data being dropped? |

You should also create diagrams of the pipeline and data catalog to be used in production. **Make note of the similarities and differences between the two pipelines**.

- If they are the same, then they are likely subject to the same errors. Are these errors important?
- If they are not the same, then different sources, different processing has been applied. Do any of these differences impact the model? How do you know?

The **more data sources that are involved**, the more **disparate the data sources** that are to be merged, and the **more data transformation steps** that are involved, the more complex the data quality challenge becomes.

### Estimating Impact of Data Quality

Frequently, there are many individual cleaning and transformation steps performed before the data is used for ML training.

Examples are:

- When merging data, data might be dropped if no direct key match is found.
- Records with null or extreme values might be dropped.

**How do you ensure that the model’s performance in production will be similar**? Here are two approaches that work together: comparing statistics, and validating the model against unclean data inputs.

### Validate Model Against Unclean Data Inputs

A simple but powerful technique to validate your data model is to take a subset of data that was eliminated during every cleaning or transformation step from the raw data, and compare it to the data eventually used to train the model, and send those items to the ML inference endpoint. Then, assess the resulting inferences.

- Does the endpoint **provide reasonable responses in all cases**? 
- Use the results to identify where checks and error handling should be added. **Should error handling be added to the inference endpoint**?
- Or, should the applications that are calling the inference endpoints be required to identify and **remove problematic inputs, or handle problematic outputs**?

### Assessing Economic Value

- An additional aspect of the ML project is assessing the cost of errors. Implicit with the speed and volume that many ML models address, is that human intervention and oversight that might exist today are removed. 
  - What is the **cost of errors**? 
  - If there is a cost for each error, **how much tolerance is there**, before the economic model ceases to be positive?
- If **model drift occurs**, the number of errors might increase. How serious a problem is that?

As shown in Figure 3, calculating error costs can show that an otherwise well-performing model (based on otherwise good metrics) might not be economically feasible.

![error](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/Impact_Error_Costs.JPG?raw=true?)

An example of such an approach is shown in [Training models with unequal economic error costs using Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/training-models-with-unequal-economic-error-costs-using-amazon-sagemaker/) .19 Here, the differential costs of errors changes the ML model used to predict breast cancer, producing fewer false negatives (undesirable and expensive) at the cost of more false positives, while still producing a cheaper model overall.

### Using Scorecards to Manage and Mitigate Risk

The sample scorecards are separated into five topics:

- **Project context** – Addresses the social, business, and regulatory environment of the project
- **Financial** – Identifies the costs and benefits of the problem you are trying to solve with ML, and of the ML system you are developing
- **Data quality** – Highlights areas that are frequently problematic in ML projects, and that can easily mislead the project—missing a signal that exists in the data or believing a signal exists where there is none—if not identified and addressed
- **Project processes** – Addresses processes in the ML project that are easily overlooked in the excitement of developing and testing the algorithm and identifying promising results
- **Summary** – Captures the key risk areas to bring to executive attention

## Machine Learning Foundations: Evolution of ML and AI

### AWS and Machine Learning

- The first layer shows AI Services, which are intended for builders creating specific
  solutions that require prediction, recommendation, natural language, speech, vision, or
  other capabilities. These intelligent services are created using machine learning, and
  especially deep learning models, but do not require the developer to have any
  knowledge of machine learning to use them.
- 

![svc](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/AWS-ML-Services.JPG?raw=true)

| AWS Service               | Purpose                                                      |
| ------------------------- | ------------------------------------------------------------ |
| Amazon Forecast           | Amazon Forecast is a fully managed service that delivers highly accurate forecasts, and is based on the same technology used at Amazon.com. You provide historical data plus
any additional data that you believe impacts your forecasts. Amazon Forecast examines
the data, identifies what is meaningful and produces a forecasting model. |
| Amazon Personalize        | Amazon Personalize makes it easy for developers to create individualized product and content recommendations for customers using their applications. You provide an activity stream from your application, inventory of items you want to recommend and potential demographic information from your users. Amazon Personalize processes and examines the data, identifies what is meaningful, selects the right algorithms, and trains and optimizes a personalization model. |
| Amazon Lex                | Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational
interactions. With Amazon Lex, the same deep learning technologies that power
Amazon Alexa are now available to any developer, enabling you to quickly |
| Amazon Lex                | Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational
interactions. With Amazon Lex, the same deep learning technologies that power
Amazon Alexa are now available to any developer, enabling you to quickly and easily
build sophisticated, natural language, conversational bots (“chatbots”). |
| Amazon Comprehend         | Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. Amazon Comprehend
identifies the language of the text; extracts key phrases, places, people, brands, or
events; understands how positive or negative the text is and automatically organizes a
collection of text files by topic. |
| Amazon Comprehend Medical | Amazon Comprehend Medical is a natural language processing service that extracts relevant medical information from unstructured text using advanced machine learning
models. You can use the extracted medical information and their relationships to build
or enhance applications |
| Amazon Translate          | Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable language translation. Neural machine translation is a form of language translation automation that uses deep learning models to deliver more accurate and more natural sounding translation than traditional statistical and rule-based translation algorithms. Amazon Translate allows you to localize content - such as websites and applications - for international users, and to easily translate large volumes of text efficiently. |
| Amazon Polly              | Amazon Polly is a service that turns text into lifelike speech, allowing you to create applications that talk, and build entirely new categories of speech-enabled products.
Amazon Polly is a Text-to-Speech service that uses advanced deep learning
technologies to synthesize speech that sounds like a human voice. |
| Amazon Transcribe         | Amazon Transcriber is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications. Using the
Amazon Transcribe API, you can analyze audio files stored in Amazon S3 and have the
service return a text file of the transcribed speech. |
| Amazon Rekognition        | Amazon Rekognition makes it easy to add image and video analysis to your applications. You just provide an image or video to the Rekognition API, and the service
can identify the objects, people, text, scenes, and activities, as well as detect any
inappropriate content. Amazon Rekognition also provides highly accurate facial analysis and facial recognition. You can detect, analyze, and compare faces for a wide variety of user verification, cataloging, people counting, and public safety use cases. |
| Amazon Textract           | Amazon Textract automatically extracts text and data from scanned documents and forms, going beyond simple optical character recognition to identify contents of fields in forms and information stored in tables |

### Amazon SageMaker

- Fully-managed machine learning (ML) service that enables developers and data scientists to quickly and easily build, train, and deploy machine learning models at any scale.

- SageMaker sets up and manages environments for training, and provides hyperparameter optimization with Automatic Model Tuning to make the model as accurate as possible
- SageMaker deployments run models spread across availability zones to deliver high performance and high availability

### Amazon SageMaker GroundTruth

- Helps build data sets quickly and accurately using an active learning model to label data combing machine learning and human interaction to make the model progressively better.

### SageMaker Neo

- Sagemaker Neo allows you to deploy the same trained model to  multiple platforms. Using machine learning, Neo optimizes the performance and size of the model and deploys to edge devices containing the Neo runtime. 

### Amazon EMR/EC2 with Spark/Spark ML

- provides a managed Hadoop framework that makes it easy, fast, and cost-effective to process vast amounts of data across dynamically scalable Amazon EC2 instances. 
- Spark and Spark ML can also be run on Amazon EC2 instances to pre-process data, engineer features or run machine learning models

## Augmented AI: The Power of Human and Machine
### Challenges for agencies dealing with benefits programs

- Customer/Beneficiary experience: Legacy benefits systems often provide poor consumer
  experience as they cannot scale to meet the surge during an open enrollment or
  during a crisis situation. AWS cloud offers multiple options to help address these
  challenges.
- Workforce productivity: Benefits application documents can include federal tax forms, pay stubs, SSN, and etc. These documents are in multiple formats. such as PDFs and images, and are submitted from various sources such as the web, mail-in, and contact centers. The work force spends a significant amount of time to review, process, and validate these documents. AWS offers multiple services including Amazon Augmented AI, to address these challenges through process automation.
- Data scale, size, privacy and security: For example, Healthcare.gov alone handled over 10.7 Million applications during the 2019 open enrollment period. AWS provides multiple storage options
  including the Amazon Simple Storage Service (Amazon S3) to address this challenge.
- Large call volumes:  For example, the Social Security Administration (SSA) handled over 50 Million calls5 during FY-2019. AWS has a number of services including Amazon Connect, and Amazon Lex to enable these capabilities.
- Insights into program operations: Having access to data-driven insights enables agencies to build programs and advocate for innovative policy changes to better serve constituents. AWS provides a number of analytics and AI/ML services to address these challenges.

### High level framework to address challenges with benefits enrollment

![im](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/framework_challenge_framework.JPG?raw=true)

| Outcome                                                     | AWS Service                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| Improve beneficiary/customer experience                     | Agencies can enable self-service and automated communications on web, mobile, and through contact centers using AWS services such as **Amazon Pinpoint, Amazon Lex and Amazon Polly**. Using these capabilities, beneficiaries can obtain their case status, execute routine tasks, such as a PIN resets, or obtain general information on claims. |
| Provide centralized storage with Data Lakes                 | There are a variety of options to gather the data from the beneficiaries on claims and applications. These options include standard web, mobile communications combined with AWS services such as **Amazon Kinesis Data Streams and Amazon Kinesis Data Firehose for streaming data, or the AWS Transfer Family service for batch data ingestion and storage into data lakes**.The [Data Lake solution](https://aws.amazon.com/solutions/data-lake-solution/) automatically crawls data sources, identifies data formats, and then suggests schemas and transformations, so you don’t have to spend time handcoding data flows. For example, **if you upload a series of claims and application documents to Amazon S3; AWS Glue, a fully managed extract, transform and load (ETL) tool, can scan these documents to identify the schema and data types present in these files**. This metadata is then stored in a catalog to be used in subsequent transforms and queries |
|                                                             | The [AWS Lake Formation](https://aws.amazon.com/lake-formation/) service builds on the existing data lake solution by enabling you to set up a secure data lake within days. Once you define where your lake is located, Lake Formation collects and catalogs this data, moves the data into Amazon S3 for secure access, and cleans and classifies the data using machine learning algorithms.
Additionally, user-defined tags or meta-data about the documents such as SSN cards, bank statements, driver’s licenses, or other claims data is stored in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), a key-value document database, to add business-relevant context to each dataset. You can browse available datasets or search on dataset attributes and tags to quickly find and access the documents in S3. |
|                                                             | **To summarize, Amazon S3 combined with AWS Glue and AWS Lake Formation act as a centralized data lake for storing documents from multiple sources with disparate data formats. Amazon DynamoDB provides fast access to these documents by storing the document meta-data (e.g. claimant ID, document storage location in S3, etc.).** |
| Extract relevant information from application documents     | Amazon Textract can help **extract text** and dat a from scanned documents and images without the need for any custom coding; Amazon Rekognition can be used for **image analysis for user verification**  authentication purposes.          The extracted information can be stored in databases such as DynamoDB, Amazon Elasticsearch, or Amazon Kendra, to enable the case managers
with query capabilities. |
| Enhance Case worker and Manager’s productivity              | An ideal way to deal with this challenge is to introduce AI and ML into the entire application process and augment the human workforce with process automation and have human intervention only as needed. |
| Build review / approval work-flow automation                | [Amazon Augmented AI (A2I)](https://aws.amazon.com/augmented-ai/) makes it easy to build process automation and workflows required for human review of ML predictions. Many machine learning applications require humans to review low-confidence predictions to ensure the results are correct. Amazon A2I provides built-in human review workflows for common machine learning use cases, such as text extraction from documents. Using this service, **you can allow human reviewers to**
**step in when a model is unable to make a high-confidence prediction or to audit its predictions** on an ongoing basis. **AWS customers are implementing A2I with Textract to improve the efficiency of their document processing by combining the speed, efficiency and cost savings of ML with A2I in order to include human-in-the-loop validation to ensure accuracy** of results. |
| Build Machine Learning models to identify anomalies / fraud | Amazon SageMaker is a fully managed service that provides developers and data scientists with the ability to build, train, and deploy machine learning (ML) models quickly. SageMaker makes it easy to deploy your trained model into production with a single click so that you can start generating predictions on the claims and application data. This is not only useful in training models with accurate vs. inaccurate applications but also in flagging any suspicious or fraudulent application patterns or anomalous activities. |
| Build intelligent contact centers                           | **Deploy scalable Omni channel contact centers**: *Amazon Connect* is an easy to use Omni channel cloud contact center that helps companies provide superior customer service at a lower cost. Amazon Connect provides a seamless experience across voice and chat for your customers and agents. This includes one set of tools for skills-based routing, powerful real-time and historical analytics, and easy-to-use intuitive management tools.              **Provide AI-powered speech analytics**: *Amazon Contact Lens* (currently in preview) is a set of machine learning (ML) capabilities integrated into Amazon Connect. With Contact Lens for Amazon Connect, contact center supervisors can better understand the sentiment, trends, and compliance risks of customer conversations to effectively train agents, replicate successful interactions, and identify crucial feedback on benefits/claimant services. Additionally, Amazon Transcribe and Amazon Transcribe Medical provide speech-to-text capabilities. Recorded speeches can be converted to text and analyzed for further insights.                                                                             **Develop self service capabilities**:  *Amazon Lex* is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition for converting speech to text, and natural language understanding to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. **Provide language translation capabilities**: *Amazon Translate* can be used to convert text from one language to another (e.g. Spanish to English). Using Amazon Transcribe and Translate together, calls in one language can be first transcribed and then translated into a different language.                               **Build effective campaign management strategies**: *Amazon Pinpoint* helps the agencies engage with public by sending them personalized, timely and relevant communications via email, SMS and other channels. |
| Improve operational efficiencies                            | Program leadership can get **deep insights via operational dashboards** that can be built using Amazon QuickSight which is a cloud powered business intelligence service. Additionally,                                                                     Amazon Forecast can be used to **forecast enrollment** models and budgets.          Agencies can also proactively **identify fraud**, waste and abuse within the benefits programs using services such as Amazon Fraud Detector, |

### Reference Architecture and Best Practices

![img](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/Reference_Architecture.JPG?raw=true)

Following are the AWS services will be used to achieve this **Reference Architecture**.

![im](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/aws_services.JPG?raw=true)

### Augmented AI Reference Workflow

Amazon A2I helps to **integrate** Amazon Textract, Amazon Rekognition, or a custom ML model into your workflow. When you create a **flow definition** you will be able to **specify conditions, such as confidence thresholds, that will trigger a human review**. 

The following diagram provides a high-level reference workflow to enhance case managers’ / case workers’ productivity; A2I is built into the workflow and human review is only needed when a document’s confidence level falls below a certain threshold.

![im](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/a2i_workflow.JPG?raw=true)

## Machine Learning Lens - AWS Well-Architected Framework

### E2E ML Process

![im](https://github.com/amitkml/AWS-MachineLearning/blob/main/img/E2E_ML_Process.JPG?raw=true)

#### Business Goal Identification

For an ML-based approach to be successful, having an abundance of relevant, high-quality data that is
applicable to the algorithm that you are trying to train is essential. Carefully evaluate the availability
of the data to make sure that the correct data sources are available and accessible.

Apply these best practices:

- Understand business requirements
- Form a business question
- Determine a project’s ML feasibility and data requirements
- Evaluate the cost of data acquisition, training, inference, and wrong predictions
- Review proven or published work in similar domains, if available
- Determine key performance metrics, including acceptable errors
- Define the machine learning task based on the business question
- Identify critical, must have features

#### ML Problem Framing

Apply these best practices:

- Define criteria for a successful outcome of the project
- Establish an observable and quantifiable performance metric for the project, such as accuracy,
  prediction latency, or minimizing inventory value
- Formulate the ML question in terms of inputs, desired outputs, and the performance metric to be
  optimized
- Evaluate whether ML is a feasible and appropriate approach
- Create a data sourcing and data annotation objective, and a strategy to achieve it
- Start with a simple model that is easy to interpret, and which makes debugging more manageable

#### Data Collection

- AWS provides you with a number of ways to ingest data in bulk from static resources, or from new,
  dynamically generated sources, such as websites, mobile apps, and internet-connected devices. 
- For example, you can build a highly scalable data lake using Amazon Simple Storage Service (Amazon S3). To easily set up your data lake, you can use AWS Lake Formation.

- You can physically transfer petabytes of data in batches using AWS Snowball, or, if you have
  exabytes of data, by using AWS Snowmobile.
- use Amazon Kinesis Data Firehose to collect and ingest multiple streaming-data sources.
- Use a centralized approach to store your data, such as a data lake.
- Confirm the availability of the data, both quantity and quality

#### Data Preparation

AWS provides several services that you can use to annotate your data, extract, transfer, and load (ETL)
data at scale. 

- Start with a small, statistically valid set of sample data for data preparation
- Iteratively experiment with different data preparation strategies
- Implement a feedback loop during the data cleaning process that provides alerts for anomalies
  through the data preparation steps
- Enforce data integrity continuously
- Take advantage of managed ETL services

**Data preparation applies not only to the training data used for building a machine learning model,**
**but also to the new business data that is used to make inferences against the model after the model is deployed. Typically, the same sequence of data processing steps that you apply to the training data is also applied to the inference requests.**

- **Amazon SageMaker** is a *fully managed service* that encompasses the *entire ML workflow* to label
  and prepare your data, choose an algorithm, train it, tune and optimize it for deployment, and make
  prediction

- **Amazon SageMake**r Ground Truth offers easy *access to public and private human labelers* and provides *built-in workflows* and user interfaces for common labeling tasks. It uses a machine learning model to *automatically label raw data* to produce high-quality training datasets quickly at a fraction of the cost of manual labeling. Data is *only routed to humans if the active learning model cannot confidently label it*. The service provides *dynamic custom workflows*, job chaining, and job tracking to save time on subsequent ML labeling jobs by using the output from previous labeling jobs as the input to new labeling jobs.
- **AWS Glue** is a fully managed *extract, transform, and load (ETL)* service that can be used to *automate*
  the ETL pipeline. AWS Glue *automatically discovers and profiles your data* with the Glue Data Catalog,
  recommends and generates ETL code to transform your source data into target schemas, and runs the
  ETL jobs on a *fully managed, scale-out Apache Spark environment to load your data to its destination*. It
  also enables you to set up, orchestrate, and monitor complex data flows.

- **Amazon EMR** provides a *managed Hadoop framework* that makes it easy and fast to process *vast*
  *amounts of data across dynamically scalable Amazon EC2 instances*.

- **Amazon SageMaker** Inference Pipeline deploys pipelines so that you can pass raw input data and
  execute pre-processing, predictions, and post-processing on both real-time and batch inference requests. Inference pipelines enable you to *reuse existing data processing functionality*.

### Data Visualization and Analytics

A key aspect to understanding your data is to identify patterns.AWS provides several services that you can use to visualize and analyze data at scale.

Apply these best practices:

- Profile your data (categorical vs. ordinal vs. quantitative visualization)
- Choose the correct tool or combination of tools for your use case (such as data size, data complexity,
  and real-time vs. batch)
- Monitor your data analysis pipeline
- Validate assumptions about your data

- **Amazon SageMaker** provides a hosted Jupyter notebook environment that you can use to visualize and analyze data. Project Jupyter is an open-source web application that allows you to create visualizations and narrative text, as well as perform data cleaning, data transformation, numerical simulation, statistical modeling, and data visualization.
- **Amazon Athena** is a fully managed interactive query service that you can use to query data in Amazon
  S3 using ANSI SQL operators and functions. Amazon Athena is serverless and can scale seamlessly to
  meet your querying demands.
- **Amazon Kinesis Data Analytics** provides real-time analytic capabilities by analyzing streaming data to
  gain actionable insights. The service scales automatically to match the volume and throughput of your
  incoming data.
- **Amazon QuickSight** is a cloud-powered business intelligence (BI) service that provides dashboards and visualizations. The service automatically scales to support hundreds of users and offers secure sharing and collaboration for storyboarding. Additionally, the service has built-in ML capabilities that provide out-of-the-box anomaly detection, forecasting, and what-if analysis.

### Feature Engineering

Every unique attribute of the data is considered a feature. Feature engineering is a process to select and transform variables when creating a predictive model using machine learning or statistical modeling. **Feature engineering typically includes feature creation,feature transformation, feature extraction, and feature selection**.

- **Feature creation** identifies the features in the dataset that are relevant to the problem at hand.
- **Feature transformation** manages replacing missing features or features that are not valid. Some
  techniques include forming Cartesian products of features, non-linear transformations (such as
  binning numeric variables into categories), and creating domain-specific features.
- **Feature extraction** is the process of creating new features from existing features, typically with the
  goal of reducing the dimensionality of the features.
- **Feature selection** is the filtering of irrelevant or redundant features from your dataset. This is usually
  done by observing variance or correlation thresholds to determine which features to remove.

**Amazon SageMaker provides a Jupyter notebook environment with Spark and scikit-learn preprocessors that you can use to engineer features and transform the data. From Amazon SageMaker, you can also run feature extraction and transformation jobs using ETL services, such as AWS Glue or Amazon EMR. In addition, you can use Amazon SageMaker Inference Pipeline to reuse existing data processing functionality**.

Apply these best practices:

- Use domain experts to help evaluate the feasibility and importance of features
- Remove redundant and irrelevant features (to reduce the noise in the data and reduce correlations)
- Start with features that generalize across contexts
- Iterate as you build your model (new features, feature combinations, and new tuning objectives)

### Model Training

- A training algorithm computes several metrics, such as training error and prediction accuracy. 

- A classification algorithm can be measured by a confusion matrix that captures true or false positives and true or false negatives, while a regression algorithm can be measured by root mean square error (RMSE).

- The number and type of hyperparameters in ML algorithms are specific to each model. Some examples of commonly used hyperparameters are: Learning Rate, Number of Epochs, Hidden Layers, Hidden Units, and Activation Functions. Hyperparameter tuning, or optimization, is the process of choosing the optimal model architecture.
- Amazon SageMaker provides several popular built-in algorithms that can be trained with the training
  data that you prepared and stored in Amazon S3.
- Sagemaker allows custom training and the custom algorithm should be containerized using Amazon ECS and Amazon ECR.
- You can choose to train on a single instance or on a distributed cluster of instances. The infrastructure
  management that is needed for the training process is managed by Amazon SageMaker
- **Amazon SageMaker**
  - Automated training
  - hyperparameter tuning job
  - pre-built in algo
  - custom training
- **Amazon SageMaker Debugger**
  - provides visibility into the ML training process by monitoring, recording, and analyzing data that captures the state of a training job at periodic intervals.
  - it can automatically detect and alert you to commonly occurring errors, such as gradient values getting too large or too small.
- **Amazon SageMaker Autopilot**
  - It allows you to build classification and regression models simply by providing training data in tabular format.
  - This capability explores multiple ML solutions with different combinations of data preprocessors, algorithms, and algorithm parameter settings, to find the most accurate model.
  - Amazon SageMaker Autopilot selects the best algorithm from the list of high-performing algorithms that it natively supports. It also automatically tries different parameter settings on those algorithms to get the best model quality. 
  - You can then directly deploy the best model to production, or evaluate multiple candidates to trade off metrics like accuracy, latency, and model size.
- **AWS Deep Learning AMI and AWS Deep Learning Containers**
  - AWS Deep Learning AMI has popular deep learning frameworks and interfaces preinstalled, such as TensorFlow, PyTorch, Apache MXNet, Chainer, Gluon, Horovod, and Keras
- **Amazon EMR**
  - Has distributed cluster capabilities
  - Has an option for running training jobs on the data that is either stored locally on the cluster or in Amazon S3.

### Model Evaluation and Business Evaluation

- Evaluate your model using historical data (offline evaluation) or live data (online evaluation).
- Model validation can be performed using Amazon SageMaker, AWS Deep Learning AMI, or Amazon EMR.



# Sagemaker Training

## Spot Training

According to AWS, with massive growth in Cloud Compute, the unused  capacity is pretty substantial, and as customers, we should take  advantage of it.

AWS offers this unused capacity as spot-capacity  at a steep discount (over 80% - actual discount varies slightly based on  instance type and size). So, you can get a current instance type for a  discount, or you can opt for a much bigger instance type (3-4 times  larger)

One drawback with spot instances is that it can be  terminated anytime by AWS with a two-minute notice. That’s because if  there is more need for on-demand instances, AWS will terminate spot  instances and make the capacity available for on-demand use (just one  example, there are other scenarios where AWS may step-in and terminate  spot).

In general, with a spot, you have a better chance of getting an instance when you are flexible about instance type and size.

The nice thing is SageMaker does handle spot-interruptions and can resume the training when capacity is available

Couple of things to note when using spot instances:

· You need to set the use_spot_instance flag to true in the estimator

·  It is a good idea to configure checkpointing. With checkpointing, the  model artifacts are periodically saved during the training process. So,  your training state is saved when the spot instance is terminated. When  the spot capacity becomes available, a new instance can resume training  from where it was stopped earlier

· You also need to specify  maximum wait time for training job – spot is not guaranteed. So, you can  specify how long to wait before aborting the job. Max run time is  configurable that tells how long the training job can run

· In the  job output, training seconds tell you how long the job took. Billable  seconds is the time you are billed for after applying spot discounts.  For an on-demand instance, training seconds and billable seconds will  almost be the same. For spot instance, you would see a much smaller  number for billable seconds.

Here is a good example of using spot instances:

<https://github.com/aws-samples/amazon-sagemaker-managed-spot-training/blob/main/xgboost_built_in_managed_spot_training_checkpointing/xgboost_built_in_managed_spot_training_checkpointing.ipynb>

<https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html>

# S3 Notes

- prefix is a common string pattern used in S3 to group files at Organization level. The word **contracts** when followed by the delimiter / would tell S3 to treat a file with a name like **contracts/acme.pdf** as an object that should be grouped together with a second file named **contracts/dynamic.pdf**
- Multipart Upload will be used automatically when the upload is initiated by the AWS CLI or a high-level API, but you’ll need to manually break up your object if you’re working with a low-level API. Multipart Upload **breaks a large object into multiple smaller parts** and transmits them individually to their S3 target. If **one transmission should fail, it can be repeated without impacting the others**.
- Use encryption keys to protect data when it is at rest within S3. We can use AWS encrypted API endpoint for data transfer. Data at rest can be 

```python

```

aa

# Serverless ETL

![1629135354511](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629135354511.png)

![1629135421320](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629135421320.png)![1629136774204](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629136774204.png)



![1629136253327](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629136253327.png)

![1629136321979](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629136321979.png)![1629276035619](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629276035619.png)



## Glue- Use case

![1629309384969](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629309384969.png)

- Serverless ETL
- The knowledge and architecture of a typical ETL project
- The prerequisite setup of AWS parts to use AWS Glue for ETL
- Knowledge of how to use AWS Glue to perform serverless ETL
- How to edit ETL processes created from AWS Glue

# Region and AZ

![1629382937972](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629382937972.png)

# VPC and Cloud

![1629382992287](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629382992287.png)

## Direct Connect

It is a wired connection between client and customer VPC.

- Guaranteed bandwidth
- Consistent Latency
- Highest reliability

![1629384841184](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629384841184.png)

## VPN

It is cheaper than direct connect. Here one side we can see customer VPN and in other side we have AWS VPN.

- Data is encrypted and tunneled over the internet
- As this is VPN, so we can have private IP over the tunnel. So this allows us to have private IP over internet
- No Bandwidth gurantee
- Variable Latency

![1629385089590](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629385089590.png)

# Storage

- volatile storage
  - goes away with reboot. Ex: instance storage
- non-volatile storage
  - stays there after system rebooted
  - high performance storage
  - Block storage (EBS)
    - data is chopped into multiple blocks
    - each block has its identifier
    - blocks are stored where it is most efficient
  - Object storage(S3)
    - data is chopped into multiple objects
    - each obj has unique id
    - each obj has metadata
  - File Storage
    - Attaches to computer
    - uses standard file system NTFS
    - Mounted by device in network

## Object Storage(S3)

- Lifecycle management enables cost optimization
- 

![1629445394079](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629445394079.png)

![1629445771527](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629445771527.png)



### S3 versioning

![1629445916514](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629445916514.png)

### S3 MFA based Object delete

![1629446394375](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446394375.png)



### S3 encryption

![1629446538249](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446538249.png)

![1629446693027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446693027.png)

![1629446763489](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446763489.png)

![1629446784501](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446784501.png)

### Tuning S3

- Pre-signed URL
- Multi-part upload
- Cross region replication

![1629446901717](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446901717.png)

![1629446953227](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629446953227.png)

**Multi-part upload**

- Recommended when file size > 100 MB

![1629447018927](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447018927.png)

**S3 Cross region replication**

- helps user to access data depending on how close they are to that region
- helps to backup data

![1629447107011](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447107011.png)

## Instance Storage

- Attached to an EC2 instance

![1629447305783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447305783.png)



## Elastic Block Storage

![1629447491348](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447491348.png)![1629447584508](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447584508.png)

**EBS is backed up via snapshot**

![1629447745919](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447745919.png)

## Storage Gateway

![1629447904005](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629447904005.png)

# Snowball

![1629448044517](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629448044517.png)

# EC2 - Computing

EC2 are same as virtual machines

- Accelerated  computing family (P and G type instances) come with GPUs, and these are  ideal for algorithms that are optimized for GPUs. 

- General  Purpose family are some of the lowest cost instances and offer balanced  performance and memory configuration (T and M type instances). 

- Compute  Optimized family comes with the latest generation CPUs and is a higher  performance system. These are suitable for CPU intensive model training  and hosting (C type instances).  

- Memory-optimized family are optimized for workloads that process large datasets in memory (R type instances).  

- Besides,  the sagemaker also has Elastic Inference Acceleration (partial GPUs)  that provides fractional GPU capacity at a fraction of the cost of  accelerated computing family.  

- Elastic inference Acceleration is  suitable for inference workloads that can benefit from GPUs and can be  easily added to other instance families.



![1629471095443](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471095443.png)

![1629471137758](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471137758.png)![1629471233870](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471233870.png)![1629471310255](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471310255.png)![1629471405552](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471405552.png)![1629471443812](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471443812.png)![1629471610481](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471610481.png)![1629471729685](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471729685.png)

**EC2 instance is secured by security group. Network ACL keeps unwanted traffic out of subnet and security group keeps unwanted traffic out of EC2.**

![1629471817714](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471817714.png)

![1629471892952](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471892952.png)![1629471934892](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629471934892.png)

Each EC2 needs its own subnet as each EC2 will have its own IP address.

![1629472200753](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629472200753.png)

# Database

![1631776804661](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776804661.png)



![1631776855802](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776855802.png)





![1631776874220](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776874220.png)



![1631777023498](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777023498.png)![1631777173858](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777173858.png)





![1629482380620](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629482380620.png)

![1629482882248](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629482882248.png)

**NOSQL is eventually consistent and that means if I am writing into DB then if someone reading immediately then data may not be available to read. we get enormous flexibility with this.**

## Relational DB

![1631777369834](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777369834.png)

![1631777394380](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777394380.png)‘

![1631777477963](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777477963.png)



![1631777525534](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777525534.png)

### Aurora

- Traditional system uses standby to copy into different AZ but aurora does that automatically as shown below.

![1631777688578](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777688578.png)



![1631777743489](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777743489.png)

It can support upto 15 read replica and in case of primary down it can make one read replica as primary. failover is quite rapid in this case and typically within 60 sec. In case the aurora DB does not have read replica configured then it will launch new primary instance.



![1631777797713](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631777797713.png)



## DynamoDB



![1631862140306](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631862140306.png)

- simple primary key (single attribute)
  - Access data by partition key
- composite primary key (primary key and sort key)

**Here it is shown how the partition key goes through hash function to map partition key.**

![1631864365385](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631864365385.png)

**Here is how we can store in DDB and primary key is year and title. DDB has two type pf primary key.**

![1631862191276](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631862191276.png)

![1631865100399](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865100399.png)



![1631865127662](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865127662.png)

![1631865197294](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865197294.png)

![1631865224110](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865224110.png)

![1631976171930](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631976171930.png)![1631976551893](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631976551893.png)![1631976775756](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631976775756.png)









![1629483056136](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483056136.png)![1629483122200](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483122200.png)![1629483149338](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483149338.png)![1629483178734](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483178734.png)

![1629483213052](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483213052.png)

## Cassandra and Mongo DB

![1631865328061](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865328061.png)

![1631865379563](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865379563.png)



![1631865401520](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865401520.png)

## ElasticCache

![1631866172697](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631866172697.png)



- helps in achieving sub-ms performance.

![1631865553582](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865553582.png)

### Mem-cached

![1631865924024](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865924024.png)

### Redis

![1631865977705](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865977705.png)![1631866145393](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631866145393.png)





## DDB and Elastic Cache

Here is an example where DDB and Elastic Cache being used together. Frequently changing data are stored in elastic cache.

![1631865781493](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631865781493.png)



## Redshift (AWS Datawarehouse)

![1629483338586](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483338586.png)

![1629483464748](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483464748.png)![1629483498541](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483498541.png)![1629483527439](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483527439.png)

## Datalake

![1629483597504](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483597504.png)

## Database Optimisation

![1629483650081](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483650081.png)

![1629483737113](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483737113.png)![1629483787945](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483787945.png)

![1629483820985](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483820985.png)

## DB Encryption

![1629483885607](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629483885607.png)

## DB Performance Optimisation

![1629484057405](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484057405.png)

### Scaling out DDB

![1629484096391](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484096391.png)

### Scaling out RDS

**By having multiple read replica, we can point our queries to read replica while writing application is working on master. So in this way, we are not impacting CPU of master database. we can have upto 4 read-replica. we use read replica when lot of read applications.**



![1629484154776](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484154776.png)![1629484323720](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484323720.png)

#### Database caching

##### Improving read activities

![1629484541438](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484541438.png)

**Used to reduce read activities.**

- cache timeout
- how to manage when DB entries are updated and cache is having wrong data

![1629484382989](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484382989.png)

![1629484508353](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484508353.png)

##### Improving write activities

![1629485035162](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485035162.png)



![1629484701171](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484701171.png)![1629484747890](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484747890.png)

![1629484769702](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629484769702.png)

### High Availability of DB

![1629485137818](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485137818.png)![1629485161545](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485161545.png)

# IAM

![1629825315601](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629825315601.png)

![1629825342669](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629825342669.png)

## IAM Sample Policy Syntax

An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows:

```
{
  "Statement":[{
    "Effect":"effect",
    "Action":"action",
    "Resource":"arn",
    "Condition":{
      "condition":{
        "key":"value"
        }
      }
    }
  ]
```

There are various elements that make up a statement:

- **Effect:** The *effect* can be `Allow` or `Deny`. By default, IAM users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.
- **Action**: The *action* is the specific API action for which you are granting or denying permission.
- **Resource**: The resource that's affected by the action. To specify a resource in the statement, you need to use its Amazon Resource Name (ARN).
- **Condition**: Conditions are optional. They can be used to control when your policy will be in effect.

As you create and manage IAM policies, you might want to use the [IAM Policy Generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-generator) and the [IAM Policy Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).

## Sample Identity based policy

- Attached to the user and we know who is the user

![1629825575713](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629825575713.png)

## Resource Based Policy

- Here we have explicitly resource specified

- Resource based policies are required for cross account based permission

  

![1629880846698](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629880846698.png)

## Types of Policies

![1629881066590](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629881066590.png)

## User and Policy relationship

- IAM is eventual consistent and any changes into policy takes some time to reflect.

![1629881145242](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629881145242.png)

![1629912394760](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629912394760.png)

## Application Access

![1629961399507](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961399507.png)

![1629961440195](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961440195.png)

![1629961462593](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961462593.png)

![1629961483984](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961483984.png)

![1629961519119](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961519119.png)

### Cross Account Based Access

![1629961635463](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629961635463.png)

![1629963261246](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629963261246.png)

## Types of Identies

![1629963632495](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629963632495.png)

![1629963710158](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629963710158.png)

![1629963771630](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629963771630.png)

![1629963838658](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629963838658.png)



# VPC

![1629485306588](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485306588.png)

![1629485440143](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485440143.png)

![1629485548239](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485548239.png)

![1629485579199](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485579199.png)

**AWS Concepts**

![1629485621024](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485621024.png)



![1629485654897](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485654897.png)

![1629485902197](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629485902197.png)

## NAT

**Legacy One - NAT Instance**

![1629486140267](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486140267.png)

![1629486022906](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486022906.png)

**New and Recommended One - NAT Instance**

![1629486298734](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486298734.png)

![1629486259741](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486259741.png)

![1629486414864](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486414864.png)

## VPC Endpoint

This is way to connect other VPC or other AWS Services over the AWS network.

![1629486518328](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486518328.png)

## VPC Peering

![1629486662532](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486662532.png)

![1629486756869](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486756869.png)

![1629486780902](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486780902.png)

## CloudHub

![1629486863287](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486863287.png)

## Network ACL

It keeps unwanted traffic out of subnet.

![1629487109061](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487109061.png)

![1629486909240](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629486909240.png)

![1629487015001](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487015001.png)![1629487050664](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487050664.png)

## Security Groups

**Order of rules does not matter and it evaluates all the rules first and then decide.**

![1629487317583](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487317583.png)

## Network Optimization

![1629487462223](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487462223.png)

### Placement Group

![1629487494114](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487494114.png)

![1629487560147](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487560147.png)

![1629487610131](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487610131.png)

### Route 53

![1629487669669](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487669669.png)

![1629487918117](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629487918117.png)



![1629488029861](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629488029861.png)![1629488108176](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629488108176.png)

#### Routing Policies

- Simple Routing Policy

- Fail-over Routing Policy

- Weighted Routing Policy

- Latency Routing Policy

- Geo-Location Routing Policy

- Multi-Value Routing Policy

This is the default Routing Policy. This routing policy **randomly selects** the routing path and does not take the resource status (health) into account. Can be used **across regions** (See Figure 01).

![im](https://miro.medium.com/max/831/1*KTmaVfLyHPQ-r4xn0gp1XA.png)

This is the “Active-Passive” fail-over, which is primarily used for disaster recovery. 

![im](https://miro.medium.com/max/773/1*XJwCk1p1eykCQ46SzcVjIA.png)

This allows you to split the traffic based on different weights assigned. This approach is heavily used in [**Blue Green Deployments**](https://martinfowler.com/bliki/BlueGreenDeployment.html)

**Blue Green Deployment***: You can use this approach while bringing a software product from the final stage of testing to live production. This is also known as the “cut over”. With this approach, it ensures you have two production environments as identical as possible. At any given point you can switch the traffic to one of the endpoints depending on your requirement*

![im](https://miro.medium.com/max/858/1*nvKnfD9kkDi5DD1m65zamg.png)

This policy will be used, when you have resources in multiple regions and you want to route traffic to resources that provides the best latency.

The response to the request is purely measured by latency and not by the distance to the region of the resource.

![im](https://miro.medium.com/max/779/1*ylNNr5iXHThD0Yfpj1LN8w.png)

Irrespective of other factors such as latency, this routing policy basically concentrate only on the geographic location. For example, even the geographic location has very high latency, Route 53 always stick to the geographic location only.

This is good for situations, where there are statutory limitations on the geographic locations such as GDPR. If you create separate records for overlapping geographic regions — priority goes to the closest geographic location. Firstly, it looks for the closest location → then, the closest Region → If not the “Default location”, which is transparent to you and given by AWS.

![im](https://miro.medium.com/max/848/1*wEkEGeBGD7IiR0oKJlHN1g.png)

Unlike Simple Routing Policy, where you can specify multiple IP addresses for a single “A” record set, with Multi-value routing policy you are need to create multiple “A” record sets for each IP address that you define. With this approach you are able to monitor each endpoint better than the simple routing policy by having a health check attached to each record set.

All the IP addresses are randomly returned to the client just like in Simple Routing policy.

![im](https://miro.medium.com/max/764/1*L5P5Dknd_WHlkGTkCavPPw.png)



![1629488214636](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629488214636.png)![1629488283557](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629488283557.png)

### Load Balancer

![im](https://media.amazonwebservices.com/blog/2016/alb_con_splash_1.png)

![1629489101560](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489101560.png)![1629489419075](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489419075.png)

**AWS Elastic Load Balancer.**

![1629489489517](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489489517.png)

#### Network Load Balancer

![1629489590270](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489590270.png)

#### Application Load Balancer

![1629489650877](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489650877.png)

# Security

![1629824977898](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629824977898.png)

## EC2

![1629825031417](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629825031417.png)

## S3

- Storage Classes
- Versioning
- Age-Based Retention
- Tiered storage
- Replication
- Encryption with S3 and KMS managed keys



![1629825064331](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629825064331.png)

## VPC

![1629489765897](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489765897.png)

![1629489802020](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489802020.png)

![1629489877929](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629489877929.png)

## IAM

![1629490082923](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629490082923.png)

![1629490164139](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629490164139.png)

## Roles and Security Token

![1629520318496](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629520318496.png)![1629520424839](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629520424839.png)

![1629520487074](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629520487074.png)

![1629520605089](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629520605089.png)

![1629521134152](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521134152.png)![1629521364240](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521364240.png)



![1629521297267](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521297267.png)

![1629521396180](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521396180.png)

![1629521492512](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521492512.png)

![1629521790906](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521790906.png)

# SQS

![1629521862404](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521862404.png)

![1629521952303](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521952303.png)![1629521986598](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629521986598.png)

# SNS

![1629522079967](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522079967.png)![1629522131049](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522131049.png)

![1629522434727](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522434727.png)

![1629522101952](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522101952.png)

# EMR

![1629522602253](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522602253.png)

# Kinesis

![1629522645067](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522645067.png)

![1629522764457](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522764457.png)

![1629522777653](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522777653.png)

![1629522819628](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522819628.png)

![1629522884136](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522884136.png)![1629522919436](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629522919436.png)

![1629523020196](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523020196.png)

# ECS

![1629523154533](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523154533.png)

![1629523288496](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523288496.png)

# Elastic Kubernetes Service

![1629523512932](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523512932.png)

# Elastic Beanstalk

![1629523567526](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523567526.png)

# EBS Encryption

![im](https://img-c.udemycdn.com/redactor/raw/2020-01-09_19-54-20-36bdd0b44e056e5e60d0de8f5d3b6535.png)

- EBS encryption offers a straight-forward encryption solution for your  EBS resources…Encryption operations occur on the servers that host EC2  instances, ensuring the security of both data-at-rest and  data-in-transit between an instance and its attached EBS storage.”

- You have a choice of using EBS managed encryption keys or specifying your own Customer Master Key (CMK).

- In the case of EBS managed keys, EBS will use your account specific master key to encrypt and decrypt the volume.

- With  Customer Master Key, you have the flexibility to use create and use  your own keys. So, you could have one set of volumes encrypted with one  CMK and another set of volumes encrypted with a different CMK.

- With  CMK, you can set fine grained access control policies on who is allowed  access to the CMK. In general, CMK is recommended for sensitive  workloads.

- The benefit of EBS volume encryption is: all data from  host computer to the volume is encrypted, all data at rest is encrypted,  any snapshot that is taken is also encrypted and if you restore the  volume, the volume is also encrypted.

- You have the option to use a different encryption key when copying the snapshots and when restoring volumes.

# AWS Support Plans

- Basic
- Developer (suitable when evaluating solution)
- Business Support (when we have production)
- Enterprise (Run mission critical workload in aws)

![1631776680510](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776680510.png)

![1631776520543](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776520543.png)

![1631776567808](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776567808.png)

![1631776635040](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631776635040.png)



# Cloudwatch

![1629523943046](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523943046.png)![1629523989039](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629523989039.png)

# CloudTrail

It is an auditing service. Provides audit log of things ocured.

![1629548473316](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629548473316.png)

# AWS Config

Constant monitoring over infrastructure.

![1629548547469](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629548547469.png)

![1629548580476](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629548580476.png)

# CloudFront

![1629548672881](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629548672881.png)

![1629548726298](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629548726298.png)

![1629549025942](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549058220.png)

# Lambda

![1629549087217](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549087217.png)

![1629549130314](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549130314.png)

![1629549155705](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549155705.png)

### Lambda now supports event filtering for Amazon SQS, Amazon DynamoDB, and Amazon Kinesis as event sources

AWS Lambda now provides content filtering options for SQS, DynamoDB and Kinesis as event sources. With event pattern content filtering, customers can write complex rules so that their Lambda function is only triggered by SQS, DynamoDB, or Kinesis under filtering criteria you specify. This helps reduce traffic to customers’ Lambda functions, simplifies code, and reduces overall cost.

Customers can specify up to 5 filter criteria when [creating](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html) or [updating](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateEventSourceMapping.html) the event source mappings for their Lambda functions triggered by SQS, DynamoDB or Kinesis. The filters are combined using OR logic by default. In other words, an event/payload meeting any of the filtering criteria defined will be passed on to trigger a Lambda function while an event/payload not matching any of the filtering criteria will be dropped. This feature helps reduce function invocations for microservices that only use a subset of events available, removing the need for the target Lambda function or downstream applications to perform filtering. 

Content filtering is available in all commercial regions that AWS Lambda is available. There is no additional cost for using this feature beyond the standard price for AWS Lambda.

# Step Function

![1629549180394](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549180394.png)

![1629619584716](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629619584716.png)

![1629619759030](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629619759030.png)

There are eight states that your state machine can be in at any time.Let me go over these individually. 

- The Pass State is basically a debugging state or one to be used when first creating your machine. It allows you to pass its input value straight through to its output, as well as add a fixed result 

- The Task State. This is where the work actually happened. With a task, you define a resource you wish Step Functions to run as well as a timeout period. For example, you could plug in your Lambda function here to run some code. This state is used often as a sub state (or action)  within other states.

- The Choice State - given an input, the state machine chooses the correct output. Basically, an if then operation where you can run further application logic.

- Wait - the state machine will pause and can wait until a specific time or until x amount of time has passed. This might be useful if you wanted an email for fire out at 8am everyday for example.

- Succeed - simply the termination of the state machine in a successful fashion. Can be a part of a choice state for example to end the state machine.

- Fail - also a termination state for the state machine, in a failed way. Fail states must have an error message and a cause.

- Parallel State -  Executes a group of states as concurrently as possible and waits for each branch to terminate before moving on. The results of each parallel branch are combined together in an array-like format and will be passed onto the next state.

- Map State - allows you to iterate through a list of items and perform tasks on them. You can also define the number of concurrent items being worked on at one time. Think of this like a for loop for processing data.

Using combinations of these states to create your specific state machines - allows you to build some very dynamic and impressive serverless solutions that can scale extremely well.

**The state machine might look something like this.**

- Upon taking in an input image the first step would be to extract any metadata about the image if possible. This would be a task state.

- The output from that task can be sent onto the next state which would check to see if the image format is supported. This state is a choice state 

- From there we either find that the image is unsupported and the operation fails or we move onto storing this metadata. Storing would be another task.

- We can then send the image off to Amazon Rekognition to generate our tags and create a thumbnail in parallel. This would be a parallel state.

- Finally, we would add the rekotags to the image itself or into a database and associate them later. 

And then the state machine ends.

![1629620113633](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629620113633.png)

![1629620177171](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629620177171.png)



# CloudFormation

![1629549223131](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549223131.png)![1629549275774](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549275774.png)

# AWS Certificate Manager

![1629549412044](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549412044.png)

# Cost Management - AWS Cloud

![1629549545401](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549545401.png)![1629549605561](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549605561.png)![1629549672512](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549672512.png)

# AWS Budget

![1629549740314](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549740314.png)

# Trusted Advisor

![1629549771224](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549771224.png)

# High Availability

![1629549842617](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549842617.png)![1629549910169](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1629549910169.png)





















































# Quick Notes

- Use SageMakerVariantInvocationsPerInstance metric and configure Autoscaling to add capacity when requests exceed 1500.  The predefined SageMakerVariantInvocationsPerInstance metric is a per-minute metric. So, we need to convert request per second to request per minute. Max request per second per instance = 50.  Max request per minute per instance = 50 * 60 = 3000.  With a safety factor of 0.5, Max request per minute per instance = 3000 * 0.5 = 1500.  Reference: 
  https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html
- Create a new endpoint configuration to use the new instance type and apply it to the endpoint. SageMaker implements this change with no downtime. The existing endpoint configurations are read-only. So, you would need to create a new endpoint configuration.
- With multiple production variants, you can specify an initial weight in the endpoint configuration for each variant. If you like to adjust the weight, you can directly update the endpoint weight for each variant. For example, after completing A/B testing, you can route all traffic to the chosen variant by adjusting the weight of all other variants to 0.
- SageMaker Experiments automatically tracks the inputs, parameters, configurations, and results of your iteration as trials.  **You can compare active experiments with past experiments to identify** 
  **opportunities for further incremental improvements**.
- With Polly, you can use Speech Synthesis Markup Language (SSML) to “control aspects of speech, such as pronunciation, volume, pitch, speed rate, etc.”  Reference: https://aws.amazon.com/polly/
- With Comprehend, you can analyze a document to extract entities and key phrases along with confidence scores.  You can use it to provide a summary of the talking points of a document.  Seq2Seq algorithm supported by SageMaker is another algorithm that you could for this purpose.
- “SageMaker Ground Truth offers easy access to public and private human labelers [also called as Mechanical Turks] and provides them with built-in workflows and interfaces for common labeling tasks. 
  Additionally, SageMaker Ground Truth can lower your labeling costs by up to 70% using automatic labeling, which works by training Ground Truth from data labeled by humans so that the service learns to label data independently.”  Reference: https://aws.amazon.com/sagemaker/groundtruth/, 
  https://blog.mturk.com/aws-introduces-a-new-way-to-label-data-for-machine-learning-with-mturk-2f9c19866a98
- Training error is much worse than human-level error. So, this model has high-bias and underfitting the data. Validation error is much worse than the training error. So, this model has high-variance and overfitting the data. Training error is much worse than human-level error and validation error is worse than the training error. So, this model has high-bias and high-variance
- An Amazon S3 Glacier (S3 Glacier) vault can have one resource-based vault access policy
  and one Vault Lock policy attached to it. A *Vault Lock policy* is a vault access policy that you can lock. Using a Vault Lock policy can help you enforce regulatory and compliance requirements. Amazon S3 Glacier provides a set of API operations for you to manage the Vault Lock policies, see [Locking a Vault by Using the Amazon S3 Glacier API](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-how-to-api.html). 
- The model performs well with training and validation data.  However,test performance is worse.  This could indicate test and validation datasets are from different distributions.  So, collect more data that 
  is similar to test set and use it for validation.
- The validation error is much worse than training error.  So, model is overfitting the training data. We need to reduce the complexity of the model.  Regularization will reduce the weights and help in avoiding overfitting.  Early stopping would prevent a model from getting too complex.  Adding more data will help when training and validation set  are from different distribution.  Training longer would make the problem worse as the model will increase in complexity and memorize the training data.
- The training error is much worse than human-level error.  So, we need to increase the complexity of
  the model as it is underfitting.  One option is to train the model longer
- AWS Sagemaker Clarify can help explain how **models make predictions**. It uses a model-agnostic feature-attribution approach to explain how a model arrived at a particular prediction. The SageMaker Clarify is the unified capability for detecting bias and explaining how the model came up with the prediction. Clarify can check for bias during data preparation, after model training, and in your deployed model
- The definition of model fairness depends on the **specific use case and circumstances**. An organization may consider using AI in different areas of its operations (customer service, inventory management, human resource management, manufacturing, and so forth).  So, a single definition of fairness may not be feasible
- **Ground Truth is a service for labeling the training data.  Since the data is not confidential**, you 
  can reduce the labeling time by using Mechanical Turk. With Mechanical Turk, you can crowdsource the labeling task to a large remote workforce.With the Private workforce option, you can distribute the labeling work among your employees. Finally, you can hire a third-party labeling service provider. The last two options are suitable for confidential customer data
- SageMaker Studio extends standard Jupyter instance-based notebook in a few different ways. Studio
  is integrated with AWS Single Sign-On (SSO). You can use your corporate credentials to access your Studio notebook (no need for AWS user credentials).  You can easily share your notebook with your peers and colleagues. Each user gets an isolated home directory in EFS file share. The user home directory is automatically mounted into all studio notebooks that you use. So, you can access your files from any instance. Various storage options are discussed later in the "Storage for Servers" section.
- **SageMaker Debugger helps you track your training job and identify issues such as CPU, GPU, Disk IO,** **Network, Memory bottlenecks, Model issues such as Overfitting**. Metrics are visualized using SageMaker Studio along with remediation advice. Data Wrangler is a data analysis and preparation tool for machine learning applications
- With Auto pilot, you need to provide a tabular dataset and specify the target column to predict 
  (regression, binary classification, and multi-class classification). Auto Pilot will automatically explore the dataset, do feature engineering, and explore different solutions to find the best model. It will automatically try multiple algorithms such as linear models, XGBoost, and Deep Learning. You can directly deploy the trained model to production.
- Use a data parallel approach with a larger instance type. **When working with large datasets, you may** **run into a situation where the time to train a model is too long**. One solution is to increase the number of CPUs and GPUs in the training instance. Another option is to scale by using multiple instances. AWS recommends that you try a larger instance before trying to increase the number of instances.  Data parallel is the most common approach to distributed training. A model parallel approach is used with large models that won’t fit in a node’s memory in one piece.
- Users are granted access to explicitly allowed resources.  Default deny applies to all other resources
- Yes, IAM User can belong to multiple groups. No, IAM does not allow nesting or hierarchy of groups
- Group is not considered identity, and you cannot grant access to a group in a resource-based 
  policy.  With Resource-based policy, you can grant access to users, roles and other accounts
- Credentials must not be shared. Each employee must have their own user and credentials.  As a 
  best practice, MFA must be enabled for administrative actions.
- Access Key credentials are required to interact with AWS programmatically.
- For Corporate identities, you can enable single sign-on using SAML 2.0 based federation or Microsoft 
  Active Directory-based federation. Users can then access the AWS resources using their corporate credentials.
- Cognito service is useful for social identify federation and maps authenticated users to a role.  
  Users are issued temporary credentials to access the resources.  Cognito supports federation mechanisms like OAuth 2.0, SAML 2.0, OpenID Connect.
- With AWS Organizations, you centrally **enforce the corporate policies using Service Control Policy**.  With Service Control Policy, you can define what regions are allowed and limit access to the account only for those regions.  Besides, you can define what instance types are allowed and other policies.  CloudTrail is an audit trail that helps in investigating issues after the fact
- **Attribute-Based Access Control (ABAC) is an authorization strategy that defines permissions based on attributes (or tags)**.  You can structure polices to allow operations when the principal's tag matches the resource tag. This approach is useful in an environment that is growing or changing rapidly.  For example, you can check the cost center of an employee with that of the resource and allow access only if the cost center's match.  RBAC, on the other hand, requires ongoing maintenance to update the resource list.
- For the **EC2 instance, IAM Role is the recommended mechanism for managing access**.  You can attach the required policy to the IAM Role for DynamoDB access.  Storing access key credentials is not recommended as they are long term credentials, and you need to safeguard the credentials from accidental leakage.  DynamoDB does not support resource-based policy.
- Policy evaluation looks at all applicable policies (including service control policy and permission boundaries).  In this case, policy evaluation logic looks at identity-based and resource-based policies 
  before deciding if an action is allowed.  User has full access through the admin group membership.  However, the bucket policy denies all write requests.  So, only read requests are allowed.
- With Lambda, you must choose the amount of memory needed to execute your function.  Based on the memory configuration, proportional CPU capacity is allocated.  You can also increase the timeout for up to a maximum of 15 minutes.
- You can enable S3 versioning to keep the older version of the objects. You can create life cycle policies to remove the older version after 30 days.  Cross-region can help in protecting against accidental deletion and disaster recovery by keeping a copy of data in a different region. But it is more expensive as a full copy of your bucket is maintained in another region.  Moving the deleted objects to another bucket is unnecessary and requires other components.
- **LDA  and NTM are used for topic modeling; however, they are unsupervised and  generally used in exploratory setting for understanding data.**  You  have the flexibility to specify the number of topics – however, the  algorithms automatically assign topics – it may not match with what we  consider as topics: travel, food, transportation, and so forth.  It will  automatically generate appropriate topics. For example, LDA/NTM may come with a topic that groups travel and food together.  For  this problem, Comprehend service can be used to train a classifier that  can map text content to a topic. Seq2Seq is used for translation,  summarization and so forth.
- As described in the below article, batch size and learning rate should be adjusted by the same factor.  In a deep learning network, the loss curve is very complex and has several local minima.  Imagine you need to find the deepest point in a large land area, and you don’t know where the deepest point is or how deep it is.  You would come across smaller valleys (local minima), and we don’t want to conclude a small valley as the deepest point incorrectly. Our goal is for the optimization algorithm to explore different areas to find the deepest valley (global minima).  Large batch sizes appear to cause the model to get stuck in local minima whereas smaller batch sizes make the algorithm jump out of local minima and go towards global minima. **To minimize the effect of large batches, when increasing batch size, you also need to increase the learning rate by the same factor**.  Similarly, if you decrease the batch size, you need to reduce the learning rate by the same factor. Reference: 
  https://aws.amazon.com/blogs/machine-learning/the-importance-of-hyperparameter-tuning-for-scaling-deep-learning-training-to-multiple-gpus/
- For Infrastructure as a Service (IaaS) products like EC2, the customer who launched the instance is responsible for adequately patching the instance. **AWS is responsible for keeping AMI up-to-date.  Once the EC2 instance is launched, only the customer can patch the instance**. Reference: Security is Job Zero https://youtu.be/T7MnJOfOVcY
- During ML model training, if the target attribute is missing, Amazon ML rejects the corresponding record. If the target attribute is present in the record, but a value for another numeric attribute is missing, then Amazon ML overlooks the missing value. In this case, Amazon ML creates a substitute attribute and sets it to 1 to indicate that this attribute is missing. This allows Amazon ML to learn patterns from the occurrence of missing values.
- ROC AUC metric considers **True Positive Rate and False positive Rates at all possible cutoff thresholds**.  It is a useful metric for binary classifiers.  However, they are not suitable for highly imbalanced datasets as ROC curve considers only true positive and false positive rates.  ROC does not account for negatives and does not measure the performance well.  **Instead precision-recall curve is used for imbalanced datasets**.
- XGBoost requires all numeric features. Tree-based algorithms can handle features with different scales. It also handles numeric categorical features (does not require one-hot encoding). However, XGBoost also supports One-hot encoded features. For a binary feature like Lawn (yes or no), only label encoding is needed (i.e., convert to 0 and 1). Y**ou should not perform one-hot encoding on binary features. For non-binary categorical features, you can test with label encoding first and then optionally, test performance with one-hot encoding**.
- For time-series forecasting, o**ur objective is to predict the values in the future**.  To get a realistic assessment of model performance, you need to split the dataset based on time. **Set aside the first 70-80% for training and keep the most recent data (toward the end) for testing the accuracy of predictions.  Random shuffling is not recommended for time series forecasting**
- **Decision Tree-based algorithms like XGBoost automatically handles correlated features, numeric features on a different scale, and numeric-categorical variables**. Other algorithms like a neural network and the linear model would require features on a similar scale and range, and you need to keep only one feature in every highly correlated feature pairs and one-hot encode categorical features.

# Normalization and Standardization

- “The normalization transformer normalizes numeric variables to have a mean of zero and variance of one.”

- StandardScaler - “Standardize features by removing the mean and scaling to unit variance.”

# Encryption

![1630345269913](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630345269913.png)![1630345321464](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630345321464.png)





# Datalake and Streaming

![1631467599693](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631467599693.png)



![1631433819332](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631433819332.png)

![1631433876575](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631433876575.png)

![1631441180202](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441180202.png)

**With Kinesis Firehose, you can quickly ingest streaming data from a variety of sources and convert to Parquet and ORC formats.  For conversion to other formats, you can use Firehose transformation using** **Lambda**.  Firehose can also backup original records in S3.  Firehose can deliver to S3 and you can use Glue ETL to convert to Parquet.  However, this option involves additional components and scheduled jobs.  You can write a custom application to consolidate and do the transformation before writing to S3 and this option takes lot more development and maintenance effort



## datalake more

![1631462633560](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462633560.png)![1631462654184](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462654184.png)





# Kinesis streaming and batch processing

![1631441542564](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441542564.png)

![1631441591709](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441591709.png)

![1631441631122](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441631122.png)![1631441660980](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441660980.png)![1631441692101](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441692101.png)![1631441721126](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441721126.png)

# Data format and conversion

**Parquet is a columnar storage format that transparently compresses data**. It is a very efficient format for querying a subset of columns across a large number of records.  Avro is an efficient binary format that uses row storage and optimized for use cases that need to access the entire row.  JSON and CSV are text formats that use Row storage.



![1631441781206](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441781206.png)![1631441830293](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631441830293.png)

![1631462668841](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462668841.png)

![1631462694286](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462694286.png)

![1631462706903](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462706903.png)

# In-Place Query

This is S3 based datastore query. Athena is serverless and charge is based on amount of data transfer.

**With Athena, you can query the data in S3 using SQL.  You can either create the table structure in Glue Catalog or let the Glue Crawler collect the metadata and create the table.  Athena automatically** **provisions the resources required for running queries.  Redshift Spectrum also provides a capability similar to Athena; however, the query is executed in your Cluster.  So, you would need to provision the servers.  EMR Hive and Spark are also good options, but it would require provisioning your cluster, and you would also need to figure out how to load the data to the cluster**.

![1631462786428](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462786428.png)![1631462822637](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462822637.png)![1631462881403](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462881403.png)

# Streaming data Query

![1631462909727](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462909727.png)

# Datalake Analytics workload services

![1631462930907](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631462930907.png)![1631463008882](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463008882.png)

















# Monitoring and Optimisation

## Monitoring

![1631463120929](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463120929.png)

![1631463132640](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463132640.png)

![1631463303616](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463303616.png)

![1631463318961](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463318961.png)

## Cost Optimization

![1631463374356](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463374356.png)![1631463863630](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463863630.png)

![1631463963214](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463963214.png)![1631463994963](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631463994963.png)

![1631464023999](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631464023999.png)



**S3 Intelligent tiering storage class automatically moves object between frequent and in-frequent tiers.  It is suitable for use cases for which the access pattern is unpredictable**.  S3 standard storage also meets this requirement, but it is also the most expensive option.  S3 Standard IA also meets this requirement, but this has a separate retrieval fee in addition to storage cost.  Standard IA is not recommended for objects that need to be frequently read.  S3 Glacier is the lowest priced option but data is not immediately accessible and the retrieval time can range from minutes to hours



# Security and Protection

![1631466457526](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466457526.png)![1631466478293](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466478293.png)



## Policies

- In the bucket level policy, you can **limit access to the bucket from a specific network**.  Placing IP restrictions in User Policy or Role is not foolproof as some other user or system with access to S3 can read the data from anywhere.  Bucket Level policy allows us to enforce this requirement in a single place.  **Storage Gateway extends S3 to your on-premises datacenter**.  However, the S3 bucket is still accessible to other users.

![1631466510906](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466510906.png)

![1631466551454](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466551454.png)![1631466608139](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466608139.png)

## Encryption

- S3 Server-side encryption using KMS Keys will meet this requirement. You can enable encryption settings as part of Bucket configuration, and all objects are automatically encrypted. Client-Side encryption is useful for scenarios where you want to encrypt and decrypt at the client and store the encrypted object in S3.

In the below figure, **if S3 bucket is made public then anyone can decrypt the objects by default key**.

![1631466694030](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466694030.png)

In order to avoid the above limitation, following approach is recommended where only whoever has customer managed key in KMS are allowed to decrypt the objects.

**With S3 Server Side Encryption using Customer Master Key, the user needs permission to access the bucket or object and the customer master key. So, even when the bucket is made public, only the users who have access to the customer master key can access the object. However, with default keys, S3 automatically decrypts data for anyone who has permission to access the bucket.**

![1631466820399](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466820399.png)

Another approach is where client itself manages keys and send encrypted data over the https.

![1631466914784](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466914784.png)

## Datalake protection

## Durability

Durability – S3 replicates data across multiple availability zones and multiple devices in each availability zone. Cross-Region Replication is used for disaster recovery by keeping a copy of your bucket in another 
region.  Versioning protects from accidental and malicious deletes. Server-Side encryption is used for storing the data encrypted at rest.

**CloudWatch is the monitoring service that you can use to monitor your Data Lake**.  CloudTrail is used for capturing an audit trail of all API actions in your account and who performed it.  IAM is used for managing 
access permissions.  Autoscaling is used for maintaining required capacity, and it uses CloudWatch to trigger changes to infrastructure

![1631466937438](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466937438.png)

S3 achieves this high durability by having data replicated into three AZ and in multiple devices within each AZ.

![1631466989412](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631466989412.png)



## Protection against undesired modification

![1631467404698](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631467404698.png)

## Data Replication

![1631467446477](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631467446477.png)

## Object Read access based on Tagging

![1631467511406](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631467511406.png)









# Models

## Factorization Machines

Factorization Machines is a popular algorithm to build powerful recommender systems.

![1630303743058](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630303743058.png)

## Hyperparameter Tuning

![1630311384116](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630311384116.png)

![1630311513411](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630311513411.png)![1630311704181](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630311704181.png)

![1630311527605](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630311527605.png)![1630311711410](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630311711410.png)

## Regularization

- In practice, L2 is more recommended
- 

![1630322602398](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630322602398.png)![1630322930190](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630322930190.png)![1630322979323](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630322979323.png)

## Comprehend

- Amazon Comprehend is a natural language processing (NLP) service that uses ML to help you uncover
  insights and relationships in your unstructured text data. 
- First, the service identifies the language of the text. Then, it extracts key phrases, places, people, brands, and events. It analyzes text using tokenization and parts of speech, and because the service understands how positive or negative the text is, can automatically organize a collection of text files by topic.

## Lex

- Is a service for building conversational interfaces into any application using voice and text.
- Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR)
  for converting speech to text, and natural language understanding (NLU) to recognize the intent of
  the text.

## Polly

- service that turns text into lifelike speech.
-  is a text-to-speech service that uses advanced deep learning technologies to synthesize speech that sounds like a human voice.

## Rekognition

- provides highly accurate facial analysis and facial recognition on images and video that you provide.
- You can detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases

## Comprehend

- helps to extract insights from unstructured text.
- "**Custom Comprehend**: The Custom Classification and 
  Entities APIs can train a custom NLP model to categorize text and 
  extract custom entities. Asynchronous inference requests are measured in
  units of 100 characters, with a 3 unit (300 character) minimum charge 
  per request. You are charged $3 per hour for model training (billed by 
  the second) and $0.50 per month for custom model management. For 
  synchronous Custom Classification and Entities inference requests, you 
  provision an endpoint with the appropriate throughput. You are charged 
  from the time that you start your endpoint until it is deleted."

## Translate

- Translate is a text translation service. We can provide documents or strings of text in various languages and get it back in a different language.



## Textract

- Generally, we convert the documents into images in order to detect bounding boxes around the texts in images. We then apply character recognition technique to read the text from it. Textract does all this for you, and also extracts text,tables, forms, and other data for you with minimal effort. If you get low-confidence results from Amazon Textract, then Amazon A2I is the best solution

## Transcribe

- add speech-to-text capability to applications

## Lex

- build a chatbot using Amazon Lex


## Personalize

![1631978027702](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631978027702.png)

![1631978197613](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631978197613.png)

![1631978506723](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631978506723.png)



## DeepAR

![1630330116632](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630330116632.png)![1630332036393](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630332036393.png)



![1630330437148](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1630330437148.png)





# AWS Power Hour Notes

## 09-Aug-2021

![1628518215847](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628518215847.png)

**Mind map:**

![ik](https://media-exp1.licdn.com/dms/image/C4E22AQFOHpU8Iy7iCQ/feedshare-shrink_800/0/1628348589277?e=1631145600&v=beta&t=PzeaeTSbK78g2oPlGVEKoMyU4XKCAFbxlWIR84o-jGc)



## Questions

![1628518490299](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628518490299.png)

**The following is allowed if VPC peering is done. It can handle multi region failure.**

![1628518798431](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628518798431.png)

**Routing Policies:**

so they are not he same . latency based routing will take into account he latency between the user and the resource. Geoproximity will take into account he actual location of the user. so they could evaulate to different values.

Refer https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

![1628519042238](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628519042238.png)

![1628519510160](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628519510160.png)

**Read replica or primary secondary??**

![1628519874869](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628519874869.png)

![1628520222891](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628520222891.png)

![1628520508320](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628520508320.png)

![1628520855332](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628520855332.png)



![1628695826162](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1628695826162.png)

# Sagemaker Training and Hosting

![1631640282049](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631640282049.png)

## Built-in Algo Training

![1631640480644](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631640480644.png)



## Built-in Model Hosting

![1631640543550](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631640543550.png)

## Custom Model Hosting and training

- custom model needs to packaged as container that meets sagemaker specification
- need to store the image into ECR

![1631640739089](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631640739089.png)



## Popular framework based model training and hosting

- here prebuilt container is used for popular framework
- It has local mode and this means we can run in sagemaker notebook to quickly identify any issues wrt to integration of buckets, container etc.

![1631717136089](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717136089.png)

### Framework hosting

![1631717219654](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717219654.png)

![1631717339874](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717339874.png)

### Container folder structure

![1631717434951](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717434951.png)![1631717478445](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717478445.png)![1631717539352](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717539352.png)

![1631717584503](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717584503.png)



![1631717607688](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717607688.png)![1631717651962](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717651962.png)![1631717708107](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631717708107.png)

# Streaming data analytics

We can use AWS Kinesis Data Analytics to author SQL code that continuously reads and processes data in near real time. When using data in real time we speak of the `hot path` for the data. "Hot", meaning that you want to do something with the data while it is still hot from just being produced.

The government publishes the traffic data every minute as a big blob of `xml` data, containing the information for all 4500 measurement locations in Flanders. We immediately convert this data into the `JSON` format and divide it into in per-location measurement events. This preprocessing is achieved using `AWS Lambda`.  As the focus of this blog post is to discuss real-time analytics, we  will not go deeper into the particulars of how we used Lambda to  accomplish this.

The per-location measurement events are then streamed over `Firehose`.
This `Firehose` is used as an input for our `Kinesis Data Analytics` application, which will provide real-time insights. Next, the results of our real-time analytics with `Kinesis Data Analytics` are sent to a `Kinesis Data Stream`, which can then be used by a `Lambda` to, for example, generating traffic jam alerts or saving the results in `DynamoDB`.

![im](https://drlafy0xqh6wj.cloudfront.net/images/2020-07-22-kinesis-data-analytics/kinesis-data-analytics-flow-overview.png)

Kinesis Analytics continuously reads data from your Kinesis stream or Kinesis Firehose delivery stream.  For each batch of records that it retrieves, the Lambda processor subsystem manages how each batch gets passed to your Lambda function.  Your function receives a list of records as input.  Within your function, you iterate through the list and apply your business logic to accomplish your preprocessing requirements (such as data transformation).

- Enrichment

  - In some scenarios, you may need to enhance your streaming data with  additional information, before you perform your SQL analysis.  Kinesis  Analytics gives you the ability to use data from Amazon S3 in your  Kinesis Analytics application, using the Reference Data feature.  However, you cannot use other data sources from within your SQL query.

    To add dynamic data to your streaming data, you can preprocess  with a Lambda function, and retrieve the data from the data store of  your choosing.  

    

- Transformation
  - Because Kinesis Analytics uses SQL to analyze your data, the  structure of your streaming records must be mapped to a schema.  If your  records are JSON or CSV, Kinesis Analytics automatically creates a  schema.  However, if your JSON records contain complex nested arrays,  you may need to customize how the record structure is mapped to a  flattened schema.  Further, Kinesis Analytics is unable to automatically  parse formats such as GZIP, protobuf, or Avro.
  - If your input records are unstructured text, Kinesis Analytics creates a schema, but it consists of a single column representing your entire record.  To remedy these complexities, use Lambda to transform and convert your streaming data so that it more easily maps to a schema that
    can be queried by the SQL in your Kinesis Analytics application.



![im](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2017/10/05/preprocessing-data-kinesis-1.gif)



![1633499257860](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633499257860.png)

## Cloud Watch and Athena

![1633502006132](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633502006132.png)

## Cloud Trail and Athena

![1633502028742](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633502028742.png)



# AWS Machine learning CSG Session

![1631684187776](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631684187776.png)

![1631685141083](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631685141083.png)![1631685237443](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631685237443.png)

![1631687276067](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631687276067.png)![1631687589829](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631687589829.png)![1631688060727](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631688060727.png)

## AI/ML AWS

![1631688700962](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631688700962.png)

![1631688783121](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631688783121.png)

## AWS Content Analysis services

### Transcribe

![1631692080171](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692080171.png)![1631692163503](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692163503.png)

### Comprehend

![1631692333070](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692333070.png)![1631692429250](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692429250.png)

### Translate

![1631692513931](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692513931.png)

### Rekognition

![1631692539540](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692539540.png)![1631692659218](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692659218.png)

### Content analysis solution

![1631692843927](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631692843927.png)



## AI-ML In Telecom

![1631770969538](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631770969538.png)![1631771166899](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771166899.png)![1631771296654](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771296654.png)![1631771494357](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771494357.png)

![1631771707732](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771707732.png)

![1631771785947](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771785947.png)

![1631771918962](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631771918962.png)

![1631772011448](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772011448.png)

![1631772033059](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772033059.png)

![1631772131661](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772131661.png)

![1631772247211](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772247211.png)

![1631772373994](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772373994.png)

![1631772511038](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772511038.png)

![1631772676488](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772676488.png)

![1631772774627](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772774627.png)

![1631772914766](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631772914766.png)

![1631773182832](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631773182832.png)

![1631773352437](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631773352437.png)



# AWS Community Asia Pac Event

## DynamoDB Simplified: Mental Model to Approach DynamoDB Data Modelling

![1634879021159](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879021159.png)

![1634879076697](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879076697.png)

**So rather than searching every time, he decided to rearrange the files as per department. So he spends initial effort to create departmental box and keep them separately so that he does not need to go through all the files.**

![1634879207543](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879207543.png)

**Next time, principal asks a student file specifically rather than whole department file. Hoe the peon will handle now as the files are arranged in department wise**. So how he handles future request.

**He then decided to arrange files alphabetically within each department.**

![1634879331545](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879331545.png)

So now he can support

- files department wise
- files student wise

**Now, principal asking get me files for all students who plays basketball. How the peon will handle?** He also thinks principal may ask tomorrow principal may ask files for students playing cricket, kabadi etc. How he will handle future request?

**The pen then go through all the files and see if students played any batch and keep the photocopy into another box. So main files stays in department box but another duplicate copy stays into box play wise.**

![1634879521249](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879521249.png)

![1634879586121](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879586121.png)



Now apply in DDB all these.



![1634879626340](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879626340.png)

**Basically based on access pattern, we are creating partition key based on department id. but we dont have way to file one individual student file**

![1634879735232](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879735232.png)

So we add here sort key as name as department key will not be unique for each record.

- So here by applying partition key (Department Id) and sort key (name) we can get a file for a student directly.

![1634879793473](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634879793473.png)



When pattern is not supported by partition key, we create an index GSI which is copy of main table which will have different partition key and sort key

whenever we write in DDB, It will see if the record has sports then it will also insert into GSI. During query we need to specific if we need from primary key or GSI. This GSI will reduce cost greatly and we dont need to do scanning which will retrieve all the data for scanning.

![1634881882762](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634881882762.png)



![1634882047418](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882047418.png)

## Explainable AI with Amazon SageMaker Clarify

![1634882457193](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882457193.png)

![1634882476156](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882476156.png)

![1634882501783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882501783.png)

![1634882575875](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882575875.png)

![1634882667176](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882667176.png)

![1634882698186](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882698186.png)

![1634882721531](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882721531.png)

![1634882808509](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634882808509.png)

![1634885180673](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634885180673.png)

![1634885217986](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634885217986.png)

## S3 Security - The Attack and Defense

![1634885695154](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634885695154.png)

## Chaos Engineering

![1634886285516](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634886285516.png)



![1634886318569](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634886318569.png)

![1634886348440](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634886348440.png)

## AWS Glue Data Brew - Introduction



# Data Science in AWS - Workshop

github available https://github.com/data-science-on-aws/workshop

https://www.datascienceonaws.com/?mn=h32BeYNvqA1z6VSlXIw58Va2lS4CPC_Upoid.7aP01TjQarRjIOnr



## What is sagemaker?

![1634575082311](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575082311.png)



## NLP@AWS Contract Review



Blog posts (part 1 & part 2): https://towardsdatascience.com/how-to-set-up-a-machine-learning-model-for-legal-contract-review-fe3b48b05a0e & https://towardsdatascience.com/how-to-set-up-a-machine-learning-model-for-legal-contract-review-part-2-6ecbbe680ba



https://www.datascienceonaws.com/

![1634573112797](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573112797.png)

![1634573265097](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573265097.png)

![1634573465357](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573465357.png)

![1634573588462](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573588462.png)

![1634573617038](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573617038.png)

paper link https://arxiv.org/abs/2103.06268

![1634573947685](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634573947685.png)

![1634574237755](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634574237755.png)



Sample app for prediction

![1634574372255](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634574372255.png)

https://aws.amazon.com/ec2/instance-types/

- "Have you used Kubflow, MLflow, or Sagemaker Piplines? and if yes, where did you use them? and how many model version you have?" - not for this demo. we would use those tools if we were to put this model into production
- “so each new question requires model re-training?” - No, we train the model on all questions at the same time.  If we were to add new questions, with new data, that would require retraining



## Computer vision @aws

![1634574957477](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634574957477.png)

![1634575260955](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575260955.png)

![1634575347660](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575347660.png)

![1634575508832](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575508832.png)

![1634575656893](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575656893.png)

![1634575695448](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575695448.png)

![1634575898823](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575898823.png)

![1634575915672](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575915672.png)

![1634575999658](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634575999658.png)

![1634576206636](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634576206636.png)

![1634576280782](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1634576280782.png)





# AWS CodeGuru

![1631597635595](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631597635595.png)

![1631597675366](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631597675366.png)

![1631597763800](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631597763800.png)

![1631597840443](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631597840443.png)

![1631597972029](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631597972029.png)

![1631598064592](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598064592.png)

![1631598164106](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598164106.png)

![1631598187968](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598187968.png)

![1631598200836](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598200836.png)

![1631598286324](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598286324.png)

![1631598775468](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631598775468.png)

![1631599055103](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631599055103.png)

![1631599097920](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631599097920.png)![1631599146224](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631599146224.png)![1631599303014](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631599303014.png)









