[TOC]

# A ML OPS Solution

**MLOps Basics By Raviraja Ganta :**

Week 0: Project Setup 
https://lnkd.in/eUCcbD9n

Week 1: Model monitoring - Weights and Biases 
https://lnkd.in/eCtCgms5

Week 2: Configurations - Hydra 
https://lnkd.in/e_56nreH

Week 3: Data Version Control - DVC 
https://lnkd.in/eXahvheT

Week 4: Model Packaging - ONNX 
https://lnkd.in/eyvgERP6

Week 5: Model Packaging - Docker 
https://lnkd.in/e3SyiXEb

Week 6: CI/CD - GitHub Actions 
https://lnkd.in/eaRh2ifB

Week 7: Container Registry - AWS ECR 
https://lnkd.in/ebnmqfTz

Week 8: Serverless Deployment - AWS Lambda 
https://lnkd.in/eB4TJk4n

Week 9: Prediction Monitoring - Kibana 
https://lnkd.in/eNNMU28s

Week 10: Summary 
https://lnkd.in/eZ6j5DZZ

Github Code https://lnkd.in/eJPFmYys

# What is ML OPS?

![im](https://blogs.nvidia.com/wp-content/uploads/2020/09/1-MLOps-NVIDIA-invert-final-672x356.jpg.webp)

# ML OPS Code Management

## How we can put the code in one place?

Yes, ML is experimental by nature, and so applying source control may not feel as straightforward as it is for other software systems. 

- Unlike other software systems, versioning the code is only half of the job when it comes to ML, because the pipeline also relies on datasets. Ideally, you don’t want to be versioning your datasets via your source control service, and so you can instead leverage [the versioning capabilities offered by S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) for example. That way, whenever a new dataset arrives, you’re certain that you would be using it in your pipeline while also keeping track of the exact version of the data
- 

# ML OPS

## What is the difference between ML and software development?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/Software-ML-Goals.JPG?raw=true)

## What are lifecycle of data?

They are

- Labelling
- Feature space coverage
- Minimal dimensionality
- Maximum predictive data
- Race conditions

## What is ML Pipeline?

ML OPS Pipeline is usually DAGS

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/ml-pipeline.JPG?raw=true)

## What are data importance?

- Importance of data qualiy
- data pipeline
- data collection and monitoring

## What is data drift?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/data-gradual.JPG?raw=true)

## What are data issues?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/data_issues.JPG?raw=true)

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/dataset-shift.JPG?raw=true)

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/dataset_skew-detection.JPG?raw=true)

## How we can Data Validation with TensorFlow eXtended (TFX)?

![im](https://dzlab.github.io/assets/2020/11/20201103-tfx-components.svg)

Refer article https://dzlab.github.io/ml/2020/11/03/tfx-data-validation/

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/tfdv_skew_detection.JPG?raw=true)

Tensorflow Data Validation (TFDV) can analyze training and serving data to:

- compute descriptive [statistics](https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto/v0/statistics.proto),
- infer a [schema](https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto/v0/schema.proto),
- detect [data anomalies](https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto/v0/anomalies.proto).

The core API supports each piece of functionality, with convenience methods that build on top and can be called in the context of notebooks.

Refer https://www.tensorflow.org/tfx/data_validation/get_started

# Monitor, optimize, and maintain ML solutions

## ML Project Lifecycle



![im](https://i0.wp.com/neptune.ai/wp-content/uploads/Model-monitoring-ML-Lifecycle.png?resize=1024%2C216&ssl=1)

 ML model traditionally degrade over time. A model is at its best just before being deployed to production. **This is why deployment should not be your final step.**

![im](https://lh5.googleusercontent.com/Q0I7t01N4BPBpYGvsDvYwXK81sOQGBHO3mJaBqZ56VTAU4OkL1pFHoX6fjOyP1_rlfYBd8dZfCnVHu7UgBO6UYNkvYIErMJc17e_8FqcFQB6NnC1x-2ZKr37GYPj3SMNgY9jHIdf)

## Why you need to monitor your Machine Learning models in production

let’s look at some of the challenges your model will encounter in production:

| SL   | Production Challenge          | Key Questions                                                |
| ---- | ----------------------------- | ------------------------------------------------------------ |
|      | Data distribution changes     | Why are there sudden changes in the values of my features?   |
|      | Model Ownership in Production | Who owns the model in production? The DevOps team? Engineers? Data Scientists? |
|      | Training-Serving Skew         | Why is the model giving poor results in production despite our rigorous testing and validation attempts during development? |
|      | Model/Concept drift           | Why was my model performing well in production and suddenly the performance dipped over time? |
|      | Concerted adversaries         | How can I ensure the security of my model? Is my model being attacked? |
|      | Model Readiness               | How will I compare results from a newer version(s) of my model against the in-production version(s)? |
|      | Pipeline health issues        | Why does my training pipeline fail when executed? Why does a retraining job take so long to run? |
|      | Underperforming system        | Why is the latency of my predictive service very high? Why am I getting vastly varying latencies for my different models? |
|      | Data Quality Issues           | How can I ensure the production data is being processed in the same way as the training data was? |

### Goal of Monitoring models

goal of monitoring your models in production is:

- To  detect problems with your model and the system serving your model in  production before they start to generate negative business value,
- To take action by triaging and troubleshooting models in production or the inputs and systems that enable them,
- To ensure their predictions and results can be explained and reported, 
- To ensure the model’s prediction process is transparent to relevant stakeholders for proper governance, 
- Finally, to provide a path for maintaining and improving the model in production.

### What could go wrong?

You can monitor what could go wrong with your machine learning model in production at two levels:

- **Functional level monitoring** – monitoring model performance, inputs (data), and outputs (predictions).
- **Operational level monitoring** – monitoring at system and resource level. 

As a data scientist, you’re primarily responsible for monitoring at this level. You’re mostly monitoring the performance of your model in relation to the inputs, as well as the prediction results, and what goes
on in the model while learning in production.

![im](https://i0.wp.com/neptune.ai/wp-content/uploads/Functional-Monitoring.png?resize=606%2C771&ssl=1)

### Functional Level Monitoring

#### Data

##### Data quality issues

Data quality (integrity) issues mostly result from changes in the  data pipeline. To validate production data integrity before it gets to  the model, we have to monitor certain metrics based on data properties.  This way, if the input data isn’t what we expect or what we think the  model expects, an alert can be triggered for the data team or service  owner to take a look. The primary goal of monitoring here is to flag any data quality issue, either from the client or due to an unhealthy data pipeline, before the data is sent to your model (which  would generate unreliable predictions in response. Some of the trackable causes of data quality issues are

- **Preprocessing production data**
- **Changes to the source data schema** 
- **Data loss/corruption at the source**

**Data quality issue detection techniques**

- Testing input data for duplicates,
- Testing input data for missing values,
- Catching syntax errors,
- Catching data type and format errors,
- Checking schema for semantic errors in terms of feature names,
- Effective [data profiling](https://en.wikipedia.org/wiki/Data_profiling) for complex dependencies in the data pipeline,
- General integrity checks; does the data meet the requirements of downstream services or consumers?

**Possible solutions after detecting data quality issues**

- Provide an alert following a schema change.
- Ensure proper data validation practices are implemented by data owners. 

##### Data/feature drift

Monitoring your input is  perhaps the most vital aspect of functional monitoring. It could inform  you ahead of time about the changing landscape and context around the  business case you’re solving. Models aren’t intelligent enough to adjust  to a changing world unless they’re constantly retrained and updated. 

Data  drift refers to a meaningful change in distribution between the  training data and production data. Changes in input data distribution  will affect model performance over time, although it’s a slower process  than in the case of data quality issues

![im](https://lh5.googleusercontent.com/W-HeYHaGNKdLB1ugiguBsTSrA5lu_5aGF_9Nrq7MSXt46ibymAp0SvMZs79I7bSSL9cGQ_5z1SWRJ_kOWUF-O8d-0S0-JwG5IL4Gj6zchJ6tTK6CWwYcrm2wGIEogDeDUkC2wFah)

While it’s possible to monitor this drift at the level of the entire dataset, it is often advisable to monitor it at the feature level. 

**Feature/attribute drift**

Monitoring at the feature level is often the best way to detect issues with input data.

Feature drift can occur due to data quality issues or general changes in the real world, like changes in the preferences of business customers. An example of feature/attribute drift is illustrated below, where a 
historical set of attributes are used as a baseline and newer attributes are compared so that changes in the distribution of the attributes can be detected.

**Data drift detection techniques**

To detect data drift, perform [distribution tests](https://itrcweb.org/gsmc-1/Content/GW%20Stats/5%20Methods%20in%20indiv%20Topics/5%206%20Distributional%20Tests.htm) by measuring distribution changes using distance metrics:

- Basic  statistical metrics you could use to test drift between historical and  current features are; mean/average value, standard deviation, minimum  and maximum values comparison, and also correlation. 
- For continuous features, you can use divergence and distance tests such as [Kullback–Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), [Kolmogorov-Smirnov statistics](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) (widely used), Population Stability Index (PSI), [Hellinger distance](https://en.wikipedia.org/wiki/Hellinger_distance), and so on.

##### Outliers

Monitoring outliers in your input  data is crucial, but also very tricky. You’re monitoring extreme and  anomalous events that may be one-off events or a group of one-off  events. This can inevitably affect model performance, as outliers don’t  have sufficient learnable structure across the entire dataset, which  will cause the model to return an unreliable response as it won’t quite  “connect the dots” from your production data.

**Outlier detection**

- Use the tests we discussed in the previous section to determine if values and distributions of features are *drastically different* from normal benchmark periods—very noticeable drifts.
- Analyze if the features your model is most sensitive to—the most important features your model learned after training—have changed drastically.
- Use unsupervised learning methods to categorize model inputs and predictions, allowing you to discover cohorts of anomalous examples and predictions. Some platforms use AutoML to detect outliers that your test can’t catch.

**Possible solutions after outlier detection**

- Perform  data slicing methods on sub-datasets to check model performance for  specific subclasses of predictions. You can automate this process as  your model makes and logs predictions to an [evaluation store](https://neptune.ai/product) using your monitoring tool.

#### Model

##### Monitoring model drift

Model drift, or [concept drift](https://neptune.ai/blog/concept-drift-best-practices),  happens when the relationship between features and/or labels—in cases  of supervised or unsupervised learning solutions—no longer holds because  the learned relationship/patterns have changed over time.

![im](https://i0.wp.com/neptune.ai/wp-content/uploads/Concept-Drfit.png?resize=998%2C485&ssl=1)

Model drift happens because the real-world changes (consequently the  ground truth/target the model has been trained to predict)—the answers  to business questions are always evolving. What holds today may no  longer hold tomorrow, and we’re expected to reflect this fact in our  machine learning applications.

Model drift can be gradual, like  when the business climate changes and evolves naturally, and it can also  be sudden—as in cases when extreme events suddenly disrupt all  operations.

![im](https://lh6.googleusercontent.com/Dta2VRoMmiOjb1wCAeGoNCWZibzWk7siOpNdlbMETQmalIujpdxV--8dhDsQWy8QQ3GRCmIVSxah_Z9Q5dDaueWK6898XFiHaKY_ZoiAYCA9X4xX6VNOGnq3jJb8EGaqwdaMNL3H)

**Model drift can happen in different ways**

- **Instantaneous model drift:** Happens when there’s a sudden drop in model performance over time.
- **Gradual model drift:** *Most common type of model drift* happens as a result of the natural consequences of a dynamic, changing, and evolving business landscape. It
- **Recurring model drift:** This is the result of seasonal events that are periodic and recurring over a year
- **Temporary model drift:** This is quite difficult to detect by rule-based methods and is often detected using unsupervised methods. It happens due to strange, one-off events such as adversarial attacks.

**Model drift detection**

- Monitoring predictive performance (with evaluation metrics) of your model is reduced over time. By setting a predictive metrics threshold, you can confirm if your model consistently returns unreliable results and then analyze the **prediction drift** (changes in prediction results over time) from there.
- Monitoring data drift can give you a heads-up on whether you should analyze your model for degradations or drifts.

**Possible solutions after detecting model/concept drift**

- Keep monitoring and retraining deployed models according to your business reality. If your business objectives and environment change frequently, you may want to consider automating your system to schedule and execute retraining at predefined intervals compared to more stable businesses.
- If retraining your models doesn’t improve performance, you may want to consider remodeling or redeveloping models from scratch.

##### Model configuration

- Training dataset location and version,
- Test dataset location and version,
- Hyperparameters used,
- Default feature values,
- Dependencies  and their versions; you want to monitor changes in dependency versions  to easily find them for root cause analysis when model failure is caused  by dependency changes,
- Environment variables,
- Model type (classification vs regression),
- Model author,
- Target variable name,
- Features to select from the data,
- Code and data for testing scenarios,
- Code for the model and its preprocessing.

##### Model versions

Monitoring model versions in production are critical if you want to be sure that the right version is deployed. Version history should be logged to an evaluation store alongside model predictions, this way problems will be easier to tie to model version.

##### Concerted adversaries

This is especially common with machine learning applications in credit risk and financial institutions in general—for example, fraudsters may attempt to fool a model that is tasked with detecting suspicious credit card transactions. 

Other applications susceptible to adversarial attacks include:

- media companies adopting AI to detect fake news and other inappropriate content, 
- general applications that deal with audio or image recognition.

**You can monitor your system for adversarial attacks by:**

- Using  the same steps you use to flag inputs with outlier events because  adversarial threats don’t follow a pattern, they’re atypical events.

#### Predictions (Output)

Monitoring model output in production is not just the best indicator of model performance, but it also tells us if business KPIs are being met. In terms of model predictions, the most important thing to monitor is 
model performance in line with business metrics.

[metrics for a classification model](https://neptune.ai/blog/evaluation-metrics-binary-classification) include:

- Accuracy
- Confusion Matrix,
- ROC-AUC Score,
- Precision and Recall Scores,
- F1-Score.

[Metrics for a regression model](https://machinelearningmastery.com/regression-metrics-for-machine-learning/) include:

- Root Mean Square Error (RMSE),
- R-Squared and Adjusted R-Square Metrics,
- Mean Absolute Error (MAE),
- Mean Absolute Percentage Error (MAPE).

Calculating the model metrics above is only possible when you have the ground truth available. 

##### Model evaluation metrics

Using metrics to evaluate model performance is a big part of monitoring your model in production. Different metrics can be used here, such as classification, regression, clustering, reinforcement learning, and so on.

We typically evaluate the model using predefined model scoring metrics (accuracy, AUC, precision, etc) when you have a ground truth/label to compare your model with.

A basic example would be:

“Will this user click on this ad?” 

If  a user clicks on the ad, then the actual (label) is yes. An aggregation  of the comparison between your model’s predictions (if they clicked on  the ad or not) and what the correct solution is can give you an overview  of how well your model is doing in production. There’s real-time  feedback in this case because your system can tell almost immediately if  a user clicked an ad or not. A comparison could look like this:

![img](https://lh5.googleusercontent.com/fjRFNGCV1wSPdS7-tdgv-FFJO2j4V-SNaZNDpew6v6uqWWplpJBXcr5NRL7Y4k-jP5gP7kaadfitIk98vUiPrUWJN8uiwZybikMrXqEu6Ul4DwGTG6LUur0UlwgqKVPt8uu19Gis)

**Sometimes, you might have situations where your ground truth is influenced by your model’s predictions.** 

- For example, if you build a loan approval model to predict which customer will likely repay a loan, your model might perform well by appropriately approving loans for customers that will rightly pay back (that is, agreeing with the ground truth). But how do we know for sure that the customers it didn’t approve wouldn’t have paid you back? Well, the ground truth might not be the most appropriate source of truth on the performance of such a model.

![im](https://lh3.googleusercontent.com/z-wRX1FekAqLXRJnS5G8naTQXJACI5or9cXIIsxJkApS9xWOKxUU_CBbqfjl8mThVsM475NVmAxpQGQy_CgH4PO2H4b95HaPI_K5gM1aZ-urNcSkH9DAHehoJC3HI4oQfuVbT_3N)

At 1, a part of the production data (input data) is channeled to the  ground truth service which typically involves real-time ground truth  generated by your system (for example, logging if a user clicked on an  ad when the model predicted they would), a human label annotator, or  other data labeling vendors for more complicated tasks (such as  confirming if a customer repaid a loan at the stipulated time, or  confirming if a transaction was fraudulent or legitimate after  contacting a customer). 

The event id that tracks prediction and  model details is tagged with that ground truth event and logged to a  data store. The data is then ingested into the monitoring platform,  which computes the model performance metric given the model’s prediction  and the actual label.

### Operational Level Monitoring

Monitoring at the operations and system level is primarily the responsibility of the IT operations people or the DevOps team. 

At this level, you’re mostly monitoring the resources your model runs on (and runs in) in production and making sure that they’re healthy. Resources such as pipeline health, system performance metrics (I/O, disk
utilization, memory and CPU usage, traffic, things that ops people typically care about), and cost.

![im](https://i0.wp.com/neptune.ai/wp-content/uploads/Operational-Monitoring.png?resize=601%2C601&ssl=1)

#### System Performance Monitoring

Monitoring your system/application performance can help you answer questions such as:

- Does this application meet uptime requirements? 
- Is it serving requests quickly enough? 
- Is it efficiently utilizing resources and saving costs? 
- How about changes in code dependencies, can it handle it? 
- Does it meet scalability requirements? 
- What are its serving limitations? 

##### Metrices

- **CPU/GPU utilization**  when the model is computing predictions on incoming data from each API  call; tells you how much your model is consuming per request.
- **Memory utilization** for when the model caches data or input data is cached in memory for faster I/O performance.
- Number of **failed requests** by an event/operation.
- Total number of **API calls**.
- **Response time** of the model server or prediction service.

#### System reliability

Here, we’re monitoring the infrastructure and network uptime. How many clusters are running, which of the machines are running, and everything related to infrastructure. 

#### Pipelines

Monitor the health of your data and model pipeline. Unhealthy data pipelines can affect data quality, and your model pipeline leakages or unexpected changes can easily generate negative value.

If you’re charged with the responsibility of monitoring your data  pipeline, here are some metrics and factors you may want to track:

- **Input data**  – are the data and files in the pipeline with the appropriate  structure, schema, and completeness? Are there data validation tests and  checks in place so that the team can be alerted in case of an oddity in  ingested data? Monitor what comes into the data pipeline to keep it  healthy.
- **Intermediate workflow steps** – are the inputs and outputs of every task and flow in the [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph)  as expected, in terms of the number of files and file types? How long  does a task take to run in the pipeline? This could be the data  preprocessing task, or the validation task, or even the data  distribution monitoring task.
- **Output data** – is  the output data schema as expected by the machine learning model in  terms of features and feature embeddings? What’s the typical file size  expected from an output file?
- **Data quality metrics**  – tracking the statistical metrics according to the data that flows in.  This could be basic statistical properties of the data such as mean,  standard deviation, correlation, and so on, or distance metrics (such as  KL divergence, Kolmogorov-Smirnov statistic). The statistical metric  used will be mostly dependent on the dimension of data expected; a  couple of features or several features.
- Scheduled run time of a job, actual run time, how long it took to run, and the state of the job (successful, or failed job?).

#### Cost

You need to keep an eye out for how much it’s costing you and your organization to host your entire machine learning application, including data storage and compute costs, retraining, or other types of 
orchestrated jobs.

## What to monitor based on your MLOps maturity level?

**You are currently at level 0 in your MLOps maturity stage**

- Being at this level means that you’re training and deploying models manually. 

![im](https://lh3.googleusercontent.com/ZR_LO5ZdZ9la1ydBBXXXiGiDGR6jypa0awPTW3ZTkggXXVwvTYFlAnvbNuazl42-8pxhsteRGQqxssAz_7SpP-XftXpWXtwiIq_9F1kf7aIkDKPCx-W6WkJwzXhx_8oXVd_7F5LE)

**You are currently at level 1 in your MLOps maturity stage**

- Being at this level means that you have automated the machine learning pipeline to enable continuous training of your machine learning models based on triggers that have been set by criteria or a defined threshold.

![im](https://lh4.googleusercontent.com/p5JX-bq99EQKoBzUFuL1dIH9iGmT37QKf3cmV6IQURBOZ2ah2Keq8hqc8L1wgBW3f4H_n2dzXKqxi7RF6J8lHF-pzXVh2u4NxMxO9He90A18staPHD6OA-0kSoSNqmtLw0pcwyVu)

#### You are currently at level 2 in your MLOps maturity stage

- Being at this level indicates that you’re completely mature in your MLOps implementation and pretty much the entire pipeline is a [robust, automated CI/CD system](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#mlops_level_2_cicd_pipeline_automation). Your training, validation, and deployment phases are all automated in a complimentary feedback loop.

![im](https://lh3.googleusercontent.com/psNffpp8FwThF6jIhzAyzkj9dzJWs_iJgHqUnmEUJAc8w8gpDPji9YieKrrNsdOzYlBXS5a_L136DeUNsturbOS7f5_almE1N79P9CPPkaT2_cc_CE0SjAV_4Xon4mTEUam2aR6b)

## Explain a possible deployment setup without ML OPS?

The arrows with a dotted border mean that progression to the next step depends upon
a condition in the current step. For example, in the model validation step, machine learning engineers must ensure that the model meets a minimum benchmark in performance before pushing a model class to
the repository.

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/ML-WO-MLOPS.JPG?raw=true)

**Problems in above manual step:**

- The first thing to realize is that the entire experimental stage is manual, meaning data scientists and machine learning engineers must repeat those steps every time.
- models must frequently be retrained so that they are always up to date with current trends in user data. Unfortunately, when the entire process of analyzing new trends, training, testing, and validating data is manual, this may require significant resources over time, which may become unfeasible
  for a company without the resources to spare.

## Explain deployment setup of a machine learning model with automation via pipelines?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/MLOPS-Pipeline.JPG?raw=true)



In this setup, we will be introducing a system to thoroughly test pipeline components before they are packaged and ready to deploy. This will ensure continuous integration of pipeline code along with continuous delivery of pipelines, crucial elements of the automation process that the previous setup
was missing.

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/mlops-ci-cd.JPG?raw=true)

With pipelines and machine learning models, some examples of testing include:

- Does the validation testing procedure lead to correct tuning of the hyperparameters?
- Does each pipeline component work correctly? Does it output the expected element? For example,
  after model evaluation, does it correctly begin the validation step? (Alternatively, if model evaluation
  goes after model validation, does the evaluation step correctly initiate?)
- Is the data processing performed correctly? Are there any issues with the data post-processing
  that would lead to poor model performance? Avoiding this outcome is for the best since it would
  waste resources having to fix the data processing component. If the business relies on rapid pipeline
  deployment, then avoiding this type of scenario is even more crucial.
- Does the data processing component correctly perform data scaling? Does it correctly perform
  feature engineering? Does it correctly transform images?
- Does the model analysis work correctly? You want to make sure that you’re basing decisions
  on accurate data. If the model truly performs well but faults in the model analysis component of the
  pipeline lead the data scientist/machine learning engineer to believe the model isn’t performing that
  well, then it could lead to issues where pipeline deployment is slowed down.

# ML Flow Questions

Refer the article https://aws.amazon.com/blogs/machine-learning/managing-your-machine-learning-lifecycle-with-mlflow-and-amazon-sagemaker/

**Refer**

 https://github.com/dmatrix/mlflow-workshop-part-1

https://github.com/dmatrix/mlflow-workshop-part-2

https://github.com/dmatrix/mlflow-workshop-part-3



## What is ML Flow?

MLflow is an open-source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. It includes the following components:

- **Tracking** – Record and query experiments: code, data, configuration, and results
- **Projects** – Package data science code in a format to reproduce runs on any platform
- **Models** – Deploy ML models in diverse serving environments
- **Registry** – Store, annotate, discover, and manage models in a central repository

## What is ML Flow design philosophy?

![im](https://image.slidesharecdn.com/mlflow-meetup-july-2018-180723162128/95/mlflow-infrastructure-for-a-complete-machine-learning-life-cycle-7-638.jpg?cb=1532362957)

## What are ML Flow components?

![im](https://miro.medium.com/max/1531/1*SCobTA76kxbY5xDFjv8TOg.png)

## How does MLflow tracking work?

The MLflow Tracking component is an API and UI for logging parameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results. MLflow Tracking lets you log and query experiments using Python, REST, R API, and Java API APIs.

![im](https://files.speakerdeck.com/presentations/3f9111d30f344e089607b0df6787b160/slide_29.jpg)

![im](https://user-images.githubusercontent.com/1117597/101094048-a3769900-3570-11eb-86b7-d146c21fa67f.png)

## How MLFlow backend stores works?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/mlflow-backend-store.JPG?raw=true)

## What are MLFlow API’s?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/mlflow-api.JPG?raw=true)

## How to run MLFlow in AWS?

Refer to https://towardsdatascience.com/how-to-use-mlflow-on-aws-to-better-track-machine-learning-experiments-bbcb8acded65

https://aws.amazon.com/blogs/machine-learning/managing-your-machine-learning-lifecycle-with-mlflow-and-amazon-sagemaker/

## What are MLFlow project components?

![im](https://dzlab.github.io/assets/2020/08/20200809-mlflow-projects.png)

We need to tell MLflow the structure of our project by declaring the steps and the required dependencies through the following YAML files.

- `MLproject` this is a special file where each step is declared, how it should be called as well as its inputs. For instance, in our case the file would look like this:

```
name: multistep

conda_env: conda.yaml

entry_points:
  download:
    command: "python download.py"

  process:
    parameters:
      file_path: path
    command: "python process.py --file-path {file_path}"

  train:
    parameters:
      data_path: path
    command: "python train.py --data-path {data_path}"

  main:
    parameters:
      input1: {type: int, default: 1000000}
    command: "python main.py --input1 {input1}"
```



- `conda.yaml` is another special file that can be used to declare the conda environment needed to run the steps in this pipeline.

```
name: multistep
channels:
  - defaults
dependencies:
  - python=3.6
  - requests
  - ...
  - pip:
    - tensorflow==2.0.0
    - mlflow>=1.0
```

The project structure should look like this:

```
.
├── MLproject
├── conda.yaml
├── download.py
├── main.py
├── process.py
└── train.py
```

## Share some example of keras deployment by mlflow?

![im](https://github.com/amitkml/Transformer-DeepLearning/blob/main/images/mlflow-keras-example.JPG?raw=true)

## What are key in mlflow?

- Creating experiments
- model and metric logging
- Comparing model metrics
- Model Registry
- Local deployment

```python
mlflow.log_param("batch_size", batch_size)
mlflow.log_param("num_epochs", num_epochs)
mlflow.log_param("learning_rate", learning_rate)
mlflow.log_metric("eval_acc", eval_acc)
mlflow.log_metric("auc_score", auc_score)

mlflow.log_artifact("sklearn_roc_plot.png")

mlflow.pytorch.log_model(model, "PyTorch_MNIST")
```

## What are requirement for mlflow in aws?

- must have the AWS command line interface (CLI) installed and have your credentials configured. the AWS CLI lets you connect to your AWS workspace.
- must have an Identity and Access Management (IAM) execution role defined that grants SageMaker
  access to your S3 buckets.
- must have Docker installed and working properly. Verify that you can build Docker images.
  - It is essential to have Docker working on your system because without it, MLFlow cannot build
    the Docker container image to push to the AWS ECR.
- a

## How MLFlow works in aws?

Refer the article https://aws.amazon.com/blogs/machine-learning/managing-your-machine-learning-lifecycle-with-mlflow-and-amazon-sagemaker/

- In the following sections, we show how to deploy MLflow on [AWS Fargate](https://aws.amazon.com/fargate) and use it during your ML project with [Amazon SageMaker](https://aws.amazon.com/sagemaker). We use SageMaker to develop, train, tune, and deploy a Scikit-learn based ML model (random forest) using the [Boston House Prices dataset](https://scikit-learn.org/stable/datasets/index.html#boston-dataset). During our ML workflow, we track experiment runs and our models with MLflow.

**High level steps are:**

Refer github https://github.com/aws-samples/amazon-sagemaker-mlflow-fargate

- Host a serverless MLflow server on Fargate
- Set [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) and [Amazon Relational Database Service](http://aws.amazon.com/rds) (Amazon RDS) as artifact and backend stores, respectively
- Track experiments running on SageMaker with MLflow
- Register models trained in SageMaker in the MLflow Model Registry
- Deploy an MLflow model into a SageMaker endpoint

You can set a central MLflow tracking server during your ML project. By using this remote MLflow server, data scientists will be able to manage experiments and models in a collaborative manner. 

- An MLflow tracking server also has two components for storage: a `backend store` and an `artifact store`. 
- This implementation **uses an Amazon S3 bucket as artifact store and an Amazon RDS instance for MySQL as backend stor**e.

![im](https://github.com/amitkayal/amazon-sagemaker-mlflow-fargate/raw/main/media/architecture-mlflow.png)

**Running an MLflow tracking server on a Docker container**

- By default, the server runs on port `5000`, so we expose it in our container. Use `0.0.0.0` to bind to all addresses if you want to access the tracking server from other machines
- We install `boto3` and `pymysql` dependencies for the MLflow server to communicate with the S3 bucket and the RDS for MySQL database

```
FROM python:3.8.0

RUN pip install \
    mlflow \
    pymysql \
    boto3 & \
    mkdir /mlflow/

EXPOSE 5000

## Environment variables made available through the Fargate task.
## Do not enter values
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --default-artifact-root ${BUCKET} \
    --backend-store-uri mysql+pymysql://${USERNAME}:${PASSWORD}@${HOST}:${PORT}/${DATABASE}
```

### How to host n MLflow tracking server with Fargate?

You can refer https://aws.amazon.com/blogs/compute/building-deploying-and-operating-containerized-applications-with-aws-fargate/

- Fargate is an easy way to deploy your containers on AWS. It allows you to use containers as a fundamental compute primitive without having to manage the underlying instances. 
- to specify an image to deploy and the amount of CPU and memory it requires.
- The MLflow container first needs to be built and pushed to an [Amazon Elastic Container Registry](http://aws.amazon.com/ecr/) (Amazon ECR) repository.
- The container image URI is used at registration of our [Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html#ECS_AWSCLI_Fargate_register_task_definition). The ECS task has an [AWS Identity and Access Management](http://aws.amazon.com/iam) (IAM) role attached to it, allowing it to interact with AWS services such as Amazon S3.
- The Fargate service is set up with autoscaling and a network load balancer so it can adjust to the required compute load with minimal maintenance effort on our side.
- When running our ML project, we set `mlflow.set_tracking_uri(`*<load balancer uri>*`)` to interact with the MLflow server via the load balancer.

The following Python API command allows you to point your code running on SageMaker to your MLflow remote server:

```python
import mlflow
mlflow.set_tracking_uri('<YOUR LOAD BALANCER URI>')
```

Connect to your notebook instance and set the remote tracking URI. The following diagram shows the updated architecture.

![img](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/12/05/ML-1367-6.jpg)

The following code demonstrates how you can use those API calls in your `train.py` script:

```sql
# set remote mlflow server
mlflow.set_tracking_uri(args.tracking_uri)
mlflow.set_experiment(args.experiment_name)

with mlflow.start_run():
    params = {
        "n-estimators": args.n_estimators,
        "min-samples-leaf": args.min_samples_leaf,
        "features": args.features
    }
    mlflow.log_params(params)
    
    # TRAIN
    logging.info('training model')
    model = RandomForestRegressor(
        n_estimators=args.n_estimators,
        min_samples_leaf=args.min_samples_leaf,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    # ABS ERROR AND LOG COUPLE PERF METRICS
    logging.info('evaluating model')
    abs_err = np.abs(model.predict(X_test) - y_test)

    for q in [10, 50, 90]:
        logging.info(f'AE-at-{q}th-percentile: {np.percentile(a=abs_err, q=q)}')
        mlflow.log_metric(f'AE-at-{str(q)}th-percentile', np.percentile(a=abs_err, q=q))

    # SAVE MODEL
    logging.info('saving model in MLflow')
    mlflow.sklearn.log_model(model, "model")
```

Your `train.py` script needs to know which MLflow `tracking_uri` and `experiment_name` to use to log the runs. You can pass those values to your script using the hyperparameters of the SageMaker training jobs. See the following code:

```sql
# uri of your remote mlflow server
tracking_uri = '<YOUR LOAD BALANCER URI>' 
experiment_name = 'boston-house'

hyperparameters = {
    'tracking_uri': tracking_uri,
    'experiment_name': experiment_name,
    'n-estimators': 100,
    'min-samples-leaf': 3,
    'features': 'CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT',
    'target': 'target'
}

estimator = SKLearn(
    entry_point='train.py',
    source_dir='source_dir',
    role=role,
    metric_definitions=metric_definitions,
    hyperparameters=hyperparameters,
```

# Building, automating, managing, and scaling ML workflows using Amazon SageMaker Pipelines

Refer the article https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/

#  Amazon SageMaker Model Monitor

Amazon SageMaker Model Monitor helps you maintain high quality  machine learning (ML) models by automatically detecting and alerting on  inaccurate predictions from models deployed in production.

The accuracy of ML models can deteriorate over time, a  phenomenon known as model drift. Many factors can cause model drift such  as changes in model features. The accuracy of ML models can also be  affected by concept drift, the difference between data used to train  models and data used during inference.

![im](https://miro.medium.com/max/1400/1*FnxFcRnXFnLqbAOuT3EoEQ.png)

![im](https://miro.medium.com/max/1400/1*AeHl0T_VMs2T6SLXxA_BsQ.png)

Model Monitor provides the following types of monitoring:

- [Monitor Data Quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html) - Monitor drift in data quality.
- [Monitor Model Quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html) - Monitor drift in model quality metrics, such as accuracy.
- [Monitor Bias Drift for Models in Production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html) - Monitor bias in you model's predictions.
- [Monitor Feature Attribution Drift for Models in Production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html) - Monitor drift in feature attribution.

![im](https://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mmv2-architecture.png)

To enable model monitoring, you take the following steps, which follow the path of the data through the various data collection, monitoring, and analysis processes:

- Enable the endpoint to capture data from incoming requests to a trained ML model and the resulting model predictions.
- Create a baseline from the dataset that was used to train the model. The baseline computes metrics and suggests constraints for the metrics. Real-time predictions from your model are compared to the constraints, and are reported as violations if they are outside the constrained values.
- Create a monitoring schedule specifying what data to collect, how often to collect it, how to analyze it, and which reports to produce.
- Inspect the reports, which compare the latest data with the baseline, and watch for any violations reported and for metrics and notifications from Amazon CloudWatch.

Note:

- Model Monitor currently supports only tabular data.
- Model Monitor currently supports only endpoints that host a single model and does not support monitoring multi-model endpoints. For information on using multi-model endpoints, see [Host Multiple Models with Multi-Model Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html).

Refer https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker-ModelMonitoring.html for more details.

To enable data capture for monitoring the model data quality, you specify the new capture option called `DataCaptureConfig`. You can capture the request payload, the response payload or both with this configuration. The capture config applies to all variants. Go ahead with the deployment.

```
from sagemaker.model_monitor import DataCaptureConfig

endpoint_name = "DEMO-xgb-churn-pred-model-monitor-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
print("EndpointName={}".format(endpoint_name))

data_capture_config = DataCaptureConfig(
    enable_capture=True, sampling_percentage=100, destination_s3_uri=s3_capture_upload_path
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m4.xlarge",
    endpoint_name=endpoint_name,
    data_capture_config=data_capture_config,
)
```

# Reference

- [What Is MLOps?](https://blogs.nvidia.com/blog/2020/09/03/what-is-mlops/)

