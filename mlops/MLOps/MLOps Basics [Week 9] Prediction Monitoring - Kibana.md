# MLOps Basics [Week 9]: Prediction Monitoring - Kibana



## What is the need of monitoring?

Monitoring systems can help give us confidence that our systems are running smoothly and, in the event of a system failure, can quickly provide appropriate context when diagnosing the root cause.

Things we want to monitor during and training and inference are different. During training we are concered about whether the loss is decreasing or not, whether the model is overfitting, etc.

But, during inference, We like to have confidence that our model is making correct predictions.

There are many reasons why a model can fail to make useful predictions:

- The underlying data distribution has shifted over time and the model has gone stale. i.e inference data characteristics is different from the data characteristics used to train the model.
- The inference data stream contains edge cases (not seen during model training). In this scenarios model might perform poorly or can lead to errors.
- The model was misconfigured in its production deployment. (Configuration issues are common)

In all of these scenarios, the model could still make a `successful` prediction from a service perspective, but the predictions will likely not be useful. Monitoring machine learning models can help us detect such scenarios and intervene (e.g. trigger a model retraining/deployment pipeline).

The scope of this post to understand the basics of monitoring predictions.

There are different tools available for monitoring:

- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Fiddler](https://www.fiddler.ai/ml-monitoring)
- [EvidentlyAI](https://evidentlyai.com/)
- [Kibana](https://www.elastic.co/kibana/)

and many more...

I will be using `Kibana`.

In this post, I will be going through the following topics:

- `Basics of Cloudwatch Logs`
- `Creating Elastic Search Cluster`
- `Configuring Cloudwatch Logs with Elastic Search`
- `Creating Index Patterns in Kibana`
- `Creating Kibana Visualisations`
- `Creating Kibana Dashboard`

## Basics of Cloudwatch Logs

### What is Cloudwatch logs?

`Amazon CloudWatch Logs` is a service that collects and stores logs from your application and infrastructure running on AWS, provides the same features expected of any log management tool: real-time monitoring, searching and filtering, and alerts.

Let's see how to check the logs for the `lambda` we implemented in the last week.

- Go to the `MLOps-Basics` Lambda. Navigate to the `Monitor` section and `Logs` part. There will be a button indicating `View logs in cloudwatch`. Click on that.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcwl_1.png&w=3840&q=75)

- Now a new window will open (Cloudwatch) which contains the logs of the Lambda. This is the `Log group` corresponding to the lambda. Click on the top one.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcwl_2.png&w=3840&q=75)



- The logs corresponding to the latest stream will be visible as follows.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcwl_3.png&w=3840&q=75)



It will be hard to monitor the predictions using these logs. Having a dashboard containing the predictions and counts will be helpful to monitor. Let's see how to stream these logs to `Kibana` and visualise there.

## Creating Elastic Search Cluster

Let's create an `Elastic Search Cluster` which will be used to stream the logs.

- Sign in to the AWS Management Console and open the Elasticsearch Service at <https://console.aws.amazon.com/es/home>. Create a `New Domain`
- Choose the domain type as `Development and Testing` (change according to the needs)

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_1.png&w=3840&q=75)



- Give the domain a name. `mlops-cluster`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_2.png&w=3840&q=75)



- Choosing the instance type as `t2.small.elasticsearch` (since this is for demo).

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_3.png&w=3840&q=75)



- Choosing the Network configuration as `Public access` so that it can be shared across different people easily. (With VPC also it can be shared but it requires some more configuration.)

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_4.png&w=3840&q=75)



- Get the ip of the machine [using this link](https://whatismyipaddress.com/) and then add that in the domain access policy.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_5.png&w=3840&q=75)



- Since the instance chosen is `t2.small` it does not support `https` encryption. Deselect that option.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_6.png&w=3840&q=75)



- After reviewing everything create the instance. This will take some time (5mins +). Once the cluster is created, the status will be shown as `Active`.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_7.png&w=3840&q=75)



## Configuring Cloudwatch Logs with Elastic Search

### Creating a IAM role with necessary permissions

In order to stream logs to Elasticsearch cluster, Cloudwatch should have necessary permissions to write to ES Cluster. Let's a create a role with the permissions required.

- Go to the [IAM console](https://console.aws.amazon.com/iam/home) and `Roles` section. Click on `Create Role`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fiam_1.png&w=3840&q=75)



- Select the `AWS Service` and the use case as `Lambda`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fiam_2.png&w=3840&q=75)



- Search for `esfull` and select the `AmazonESFullAccess` policy.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fiam_3.png&w=3840&q=75)



- Give the role a name `mlops-cluster-role` and save it.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fiam_4.png&w=3840&q=75)



### Configuring Elasticsearch cluster to Cloudwatch logs

- Now that the role has created, go to the cloudwatch `Log Group` of the lambda. Under `Actions/Subscription Filters` there will be `Create Elasticsearch Subscription Filter`. Select it.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcf_1.png&w=3840&q=75)



- Select `mlops-cluster` under the Amazon ES cluster option. Select the `mlops-cluster-role` IAM Execution role.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcf_2.png&w=1920&q=75)



- Select the Log format as `JSON`, since we are printing the logs in Json format. Filter patterns will help in filtering the unnecessary logs and focus on the necessary ones. As a simple usecase, let's write the filter pattern as `prediction`. This will filter the logs which has prediction in it.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcf_3.png&w=1920&q=75)



- Test the filter pattern by select one of the latest log stream and then click `Test Pattern`. Now in the test results you can see only the prediction related logs.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fcf_4.png&w=1920&q=75)



- Cross check once the configuration and then create it.

## Creating Index Patterns in Kibana

Now that cloudwatch is configured with Elasticsearch, let's go to Kibana dashboard. Kibana link can be accessed as below:

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fes_8.png&w=3840&q=75)



- Go to the `Discover` section.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_1.png&w=1920&q=75)



- You might see page like this. In that case fire some queries so that some logs will be created.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_2.png&w=3840&q=75)



- Once few logs are there, the page will look like this. Click on `Create Index Pattern`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_3.png&w=3840&q=75)



- Add the index pattern as `cwl-*` which indicates all the Cloudwatch Logs.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_5.png&w=3840&q=75)



- Include the `@timestamp` field also

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_6.png&w=3840&q=75)



- Now we can see `prediction.label`, `prediction.label.keyword`, `prediction.score`, `text` in the extracted fields.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_7.png&w=3840&q=75)



- Once the pattern is created, the logs will be visible in `Discover`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_8.png&w=3840&q=75)



- Create a data table by selecting the relevant fields. I have selected the fields `prediction.label`, `prediction.label.keyword`, `prediction.score`, `text`..

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_12.png&w=1080&q=75)



- Save the data table by giving it a name.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_11.png&w=1920&q=75)



- Adjust the refresh time to 5 secs so that the latest logs will be fetched. Click on `Start`.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fip_10.png&w=1920&q=75)



## Creating Kibana Visualisations

Let's create some visualisations.

- Go to `Visualize` section in the Kibana.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_1.png&w=1080&q=75)



- Click on `Create new Visualization`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_2.png&w=3840&q=75)



- Select `Vertical Bar` (bar chart) as the type of visualization.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_3.png&w=1920&q=75)



- Select the input for visualisation as `MLOps Datatable`

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_5.png&w=3840&q=75)



- By default only Y-Axis is created with aggregation as Count. Let's create X-Axis.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_6.png&w=1920&q=75)



- Select the aggregation type as `Terms` and select the required field. Any custom label can also be provided.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_7.png&w=1200&q=75)



- Save the visualisation by giving it a title.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fvs_4.png&w=1200&q=75)



## Creating Kibana Dashboard

Dashboards can be created with the necessary visualisations.

- Go to the `Dashboard` section in the Kibana

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_1.png&w=750&q=75)



- Create new dashboard

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_2.png&w=1920&q=75)



- Click on `Add` button. This will open up a pane on the right side containing all the visualisations we have created till now.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_3.png&w=3840&q=75)



- Select the necessary visualisations and save the dashboard by giving it a name.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_4.png&w=1920&q=75)



- Now the dashboard contains the visualisations. These visualisations can be arranged according to the needs.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_5.png&w=3840&q=75)



- In order to share this dashboard, click on `share` button on top right, and `permalink`. Get the `Short URL` and share it with the concerned people.

![img](https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fmonitor%2Fdb_6.png&w=1080&q=75)



## 🔚

This concludes the post. We have seen how to monitor predictions using `Cloudwatch` & `Kibana`.

Complete code can also be found here: [Github](https://github.com/graviraja/MLOps-Basics)

## References

- [Youtube tutorial on Kibana dashboard with AWS Elasticsearch](https://www.youtube.com/watch?v=06nJRWOz5uc)
- [Jeremy Jordan Blog on Monitoring ML systems](https://www.jeremyjordan.me/ml-monitoring/#grafana)

## TAGS

[MLOPS](https://www.ravirajag.dev/tags/mlops)[DEEPLEARNING](https://www.ravirajag.dev/tags/deeplearning)[NLP](https://www.ravirajag.dev/tags/nlp)[DEPLOYMENT](https://www.ravirajag.dev/tags/deployment)[CONTAINER](https://www.ravirajag.dev/tags/container)[KIBANA](https://www.ravirajag.dev/tags/kibana)[MONITORING](https://www.ravirajag.dev/tags/monitoring)[AWS](https://www.ravirajag.dev/tags/aws)[SERVERLESS](https://www.ravirajag.dev/tags/serverless)[LAMBDA](https://www.ravirajag.dev/tags/lambda)

## PREVIOUS ARTICLE

[MLOps Basics [Week 8\]: Serverless Deployment - AWS Lambda](https://www.ravirajag.dev/blog/mlops-serverless)

[← Back to the blog](https://www.ravirajag.dev/blog)