# Lambda Deep Dive

This course briefly summarizes my understanding/Learning from Linux Academy "Deep Dive into Lambda" course.

## Understand more

Refer [The Lambda Cipher](https://www.lucidchart.com/documents/view/4ec7e6c2-e99c-44f2-aad6-7fb7fbceb988/fB.lPxz788ce) to more in-depth understanding and better visualization on this.



## What is Lambda and Serverless Arhcitecture

### Versions and Aliases

A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the `Publish` parameter to create version `1` of your function from its initial configuration.

### Lambda

- Serverless computation platform
- Primary focus in is code
- Infrastructure handling happens is in background and separated from developer
- Event driven

![1583610486430](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583610486430.png)

![1583610726998](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583610726998.png)

![1583610891156](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583610891156.png)

### Event-driven architecture

![1583611288678](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583611288678.png)

![1583611394707](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583611394707.png)

### Lambda Limitations and Retries

AWS Imposed

- memory allocation range
  - minimum of 1 28 and then a max 3000 and eight megabytes
- Disc capacity limited to 512 MB which is actually access this slash temp directory from lambda
-  max you can go to his 300 seconds for execution duration
- event call(invoke request body payload size) is limited to six megabytes and an asynchronous events call is 128 KB
- Count of executions per region which is now limited to  1000.
- Max amount of code that can put into a deployment package and put in the Lambda is 50 megabytes, and then the total size of all packages per region is 75 GB.
- we have the total size of environment variables

![1583612026165](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583612026165.png)

![1583612275404](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583612275404.png)

### Lambda Creation

![1583771647632](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583771647632.png)

**You can see we have a Web browser accessing a static outlined_flag website on S3 bucket that makes an API gateway call toe are lame to function, whic**h then returns the response and gives it back to the browser. And that's a pretty simple set up. 

![1583775282196](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583775282196.png)

### Creating a Function using the Console Part

It can be created from

- AWS CLI
- Lambda Console
- SAM Local

Lambda creation can happen

- From scratch
- Blueprints
- Serverless application repository

# Using Lambda Function with Amazon S3

Amazon S3 service is used for file storage, where you can upload or remove files. We can trigger AWS Lambda on S3 when there are any file uploads in S3 buckets. AWS Lambda has a handler function which acts as a start point for AWS Lambda function. The handler has the details of the events. In this chapter, let us see how to use AWS S3 to trigger AWS Lambda function when we upload files in S3 bucket.

## Steps for Using AWS Lambda Function with Amazon S3

To start using AWS Lambda with Amazon S3, we need the following −

- Create S3 Bucket
- Create role which has permission to work with s3 and lambda
- Create lambda function and add s3 as the trigger.

## Example

Let us see these steps with the help of an example which shows the basic interaction between Amazon S3 and AWS Lambda.

- User will upload a file in Amazon S3 bucket
- Once the file is uploaded, it will trigger AWS Lambda function in the background which will display an output in the form of a console message that the file is uploaded.
- The user will be able to see the message in Cloudwatch logs once the file is uploaded.

The block diagram that explains the flow of the example is shown here −



## Creating S3 Bucket

Let us start first by creating a s3 bucket in AWS console using the steps given below −

### Step 1

Go to Amazon services and click **S3** in storage section as highlighted in the image given below −



### Step 2

Click S3 storage and **Create bucket** which will store the files uploaded.



### Step 3

Once you click **Create bucket** button, you can see a screen as follows −



### Step 4

Enter the details **Bucket name, Select the Region** and click **Create** button at the bottom left side. Thus, we have created bucket with name : **workingwithlambdaands3**.



### Step 5

Now, click the bucket name and it will ask you to upload files as shown below −



Thus, we are done with bucket creation in S3.

## Create Role that Works with S3 and Lambda

To create role that works with S3 and Lambda, please follow the Steps given below −

### Step 1

Go to AWS services and select IAM as shown below −



### Step 2

Now, click **IAM -> Roles** as shown below −



### Step 3

Now, click **Create role** and choose the services that will use this role. Select Lambda and click **Permission** button.



### Step 4

Add the permission from below and click **Review**.



### Step 5

Observe that we have chosen the following permissions −



Observe that the Policies that we have selected are **AmazonS3FullAccess, AWSLambdaFullAccess** and **CloudWatchFullAccess**.

### Step 6

Now, enter the Role name, Role description and click **Create Role** button at the bottom.



Thus, our role named **lambdawiths3service** is created.

## Create Lambda function and Add S3 Trigger

In this section, let us see how to create a Lambda function and add a S3 trigger to it. For this purpose, you will have to follow th Steps given below −

### Step 1

Go to AWS Services and select Lambda as shown below −



### Step 2

Click **Lambda** and follow the process for adding **Name**. Choose the **Runtime, Role** etc. and create the function. The Lambda function that we have created is shown in the screenshot below −



### Step 3

Now let us add the S3 trigger.



### Step 4

Choose the trigger from above and add the details as shown below −



### Step 5

Select the bucket created from bucket dropdown. The event type has following details −



Select **Object Created (All)**, as we need AWS Lambda trigger when file is uploaded, removed etc.

### Step 6

You can add Prefix and File pattern which are used to filter the files added. For Example, to trigger lambda only for .jpg images. Let us keep it blank for now as we need to trigger Lambda for all files uploaded. Click **Add** button to add the trigger.



### Step 7

You can find the the trigger display for the Lambda function as shown below −



Let’s add the details for the aws lambda function. Here, we will use the online editor to add our code and use nodejs as the runtime environment.

### Step 8

To trigger S3 with AWS Lambda, we will have to use S3 event in the code as shown below −

```
exports.handler = function(event, context, callback) {
   console.log("Incoming Event: ", event);
   const bucket = event.Records[0].s3.bucket.name;
   const filename = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
   const message = `File is uploaded in - ${bucket} -> ${filename}`;
   console.log(message);
   callback(null, message);
};
```

Note that the event param has the details of the S3event. We have consoled the bucket name and the file name which will get logged when you upload image in S3bucket.

### Step 9

Now, let us save the changes and test the lambda function with S3upload. The following are the code details added in AWS Lambda −



### Step 10

Now, let us add the role, memory and timeout.



### Step 11

Now, save the Lambda function. Open S3 from Amazon services and open the bucket we created earlier namely **workingwithlambdaands3**.

Upload the image in it as shown below −



### Step 12

Click **Upload** button to add files as shown −



### Step 13

Click **Add files** to add files. You can also drag and drop the files. Now, click **Upload** button.



Thus, we have uploaded one image in our S3 bucket.

### Step 14

To see the trigger details, go to AWS service and select **CloudWatch**. Open the logs for the Lambda function and use the following code −

```
exports.handler = function(event, context, callback) {
   console.log("Incoming Event: ", event);
   const bucket = event.Records[0].s3.bucket.name;
   const filename = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
   const message = `File is uploaded in - ${bucket} -> ${filename}`;
   console.log(message);
   callback(null, message);
};
```

The output you can observe in Cloudwatch is as shown −



AWS Lambda function gets triggered when file is uploaded in S3 bucket and the details are logged in Cloudwatch as shown below −



![1584022903136](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1584022903136.png)

# Creating a Simple AWS Lambda Function

## Introduction

In this hands-on lab, we will create and customize Python3-based Lambda functions from within the console.

## Solution

Log in to the live AWS environment using the credentials provided. Make sure you're in the N. Virginia (`us-east-1`) region throughout the lab.

All of the code used in the lesson is [available for download here](https://raw.githubusercontent.com/linuxacademy/content-lambda-deep-dive/master/section_2/live_act_1/lambda_function.py).

### Create a Lambda Function within the AWS Lambda Console

1. Navigate to Lambda.

2. Click **Create a function**.

3. Make sure the

    

   Author from scratch

    

   option at the top is selected, and then use the following settings:

   - Basic information

     :

     - *Name*: **HelloWorld**
     - *Runtime*: **Python3.6**

   - Permissions

     :

     - Select **Choose or create an execution role**.
     - *Execution role*: **Use an existing role**
     - *Existing role*: **lambdarole**

4. Click **Create function**.

5. On the *HelloWorld* page, scroll to the *Function code* section.

6. Delete the existing code there, and enter the [code from GitHub](https://raw.githubusercontent.com/linuxacademy/content-lambda-deep-dive/master/section_2/live_act_1/lambda_function.py).

7. Click **Save**.

### Create a Test Event and Manually Invoke the Function Using the Test Event

1. In the dropdown next to *Test* at the top of the Lambda console, select **Configure test events**.
2. In the dialog, select **Create new test event**.
3. Select the **Hello World** event template.
4. Give it an event name (e.g., "Test").
5. Replace the current code there with the [provided JSON code](https://raw.githubusercontent.com/linuxacademy/content-lambda-deep-dive/master/section_2/live_act_1/test_event.json), and then click **Create**.
6. Click **Test** to verify the function's success.

### Verify That CloudWatch Has Captured Function Logs

1. Navigate to CloudWatch.
2. Select **Logs** in the left-hand menu.
3. Select the log group with your function name in it.
4. Select the log stream within the log group.
5. Verify the output is present and correct.

# Using the AWS CLI to Create an AWS Lambda Function

**It is an console application to interact different AWS services without logging into AWS applications.**




## Create your Lambda function with the AWS CLI and verify it exists using the console:

- SSH into the provided instance.
- Create a local zip file containing the Node.js code.
- Run the AWS CLI Lambda command to create a function (using the zipped file).
- Update the configuration settings for the function (256 MB, 5 Sec Timeout).
- Verify that the function shows within AWS.

## Using the AWS CLI, invoke the function you just created:

- Use the AWS CLI Lambda command to invoke the function you created.
- Verify it was invoked using the monitoring section of the AWS Lambda console.
- Check the CloudWatch Logs for the proper logging.

## To create a Lambda function

The following `create-function` example creates a Lambda function named `my-function`.

```
aws lambda create-function \
    --function-name my-function \
    --runtime nodejs10.x \
    --zip-file fileb://my-function.zip \
    --handler my-function.handler \
    --role arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-tges6bf4
```

Contents of `my-function.zip`: This file is a deployment package that contains your function code and any dependencies.

Output:

```
{
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "CodeSha256": "PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=",
    "FunctionName": "my-function",
    "CodeSize": 308,
    "RevisionId": "873282ed-4cd3-4dc8-a069-d0c647e470c6",
    "MemorySize": 128,
    "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
    "Version": "$LATEST",
    "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4",
    "Timeout": 3,
    "LastModified": "2019-08-14T22:26:11.234+0000",
    "Handler": "my-function.handler",
    "Runtime": "nodejs10.x",
    "Description": ""
}
```

For more information, see [AWS Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html) in the *AWS Lambda Developer Guide*.

![1585126653218](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585126653218.png)

```
C:\Amit Stuff\Analytic\Deep Learning\Training Materials - AWS\Lambda Deep DIve>aws lambda create-function --function-name lambda_function_cli --runtime nodejs10.x --zip-file fileb://lambda_function_cli.zip --handler lambda_function_cli --role arn:aws:iam::196038177036:role/service-role/linuxacademy-amit-lambda-s3-role-zehi6jap
{
    "FunctionName": "lambda_function_cli",
    "FunctionArn": "arn:aws:lambda:us-east-2:196038177036:function:lambda_function_cli",
    "Runtime": "nodejs10.x",
    "Role": "arn:aws:iam::196038177036:role/service-role/linuxacademy-amit-lambda-s3-role-zehi6jap",
    "Handler": "lambda_function_cli",
    "CodeSize": 589,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2020-03-31T17:45:58.297+0000",
    "CodeSha256": "xXVA8kgTHRR8270QWycS1afE2RFidF/An/ggu9H/p/M=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "22722386-32ab-4e67-bccc-04d366420f1d",
    "State": "Active",
    "LastUpdateStatus": "Successful"
}

```



## List all lambda functions

aws lambda list-functions

![1585127151515](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585127151515.png)

## Some more activity with CLI

Let’s create a python function called “add” and run it on AWS

```
$ mkdir aws_functions
$ cd aws_functions
$ mkdir add
$ cd add# Create out nice little function
$ vim main.py
---main.py---# Simple as it gets
def add(event, context):
    return event['a'] + event['b']
----# zip function -> main.zip
$ zip main.zip main.py
```

Nice! now we need to push this up to AWS lambda.

If you don’t already have the AWS command line interface (CLI) [you can install it with pip](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) like so.

```
$ sudo pip install awscli --ignore-installed six
# installation stuff
```

Now we create a AWS CLI user. This user is our entry into AWS. Refer [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-iam-new-user-group.html) for more help.

```
# Create a user group 'lambda_group'
$ aws iam create-group --group-name lambda_group# Create a user 'lambda_user'
$ aws iam create-user --user-name lambda_user# Add our user to the group
$ aws iam add-user-to-group --user-name lambda_user --group-name lambda_group# Create a password for this user
$ aws iam create-login-profile --user-name lambda_user --password My!User1Login8P@ssword# Create an CLI access key for this user
$ aws iam create-access-key --user-name lambda_user# Save the Secret and Access Key's some where safe
```

AWS allows users to perform operations defined by a policy. We are going to create a custom policy and pass it to our user.

```
# Create our policy granting all the lambda functionality
$ vim lambda_policy.json
---lambda_policy.json---
{
   "Version": "2012-10-17",
   "Statement": [{
       "Effect": "Allow",
       "Action": [
          "iam:*",
          "lambda:*"
       ],
       "Resource": "*"
   }]
}# Grant this policy to our lambda_user
$ aws iam put-user-policy --user-name lambda_user --policy-name lambda_all --policy-document file://lambda_policy.json
```

Next we will configure our AWS cli to this user.

```
$ aws configure --profile lambda_user> AWS Access Key ID [None]: <your_key>
> AWS Secret Access Key [None]: <your_secret>
> Default region name [None]: us-west-2 
> Default output format [None]: json # AWS stores this at ~/.aws/   
# go check it out  # Make sure you can connect
$ aws ec2  describe-regions
...
```

Good, we are almost there. Lambda functions also need a role. The role specifies what actions the function instance is capable of.

```
$ vim basic_lambda_role.json
---basic_lambda_role.json---
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": { "AWS" : "*" },
        "Action": "sts:AssumeRole"
    }]
}$ aws iam create-role --role-name basic_lambda_role --assume-role-policy-document file://basic_lambda_role.json
...
# Hold on to "ARN" e.g:
"Arn": "arn:aws:iam::1234567:role/basic_lambda_role"
```

Next we are going to push our add function up onto aws.

```
$ aws lambda create-function \ 
--region us-west-2 \
--function-name add \
--zip-file fileb://main.zip \
--role <your_arn>\
--handler main.add \
--runtime python2.7 \
--profile lambda_user
```

Voila! And now to invoke it…

```
$ aws lambda invoke \
--invocation-type RequestResponse \
--function-name add \
--region us-west-2 \
--log-type Tail \
--payload '{"a":1, "b":2 }' \
--profile lambda_user \
outputfile.txt# Voila!!
$ cat outputfile.txt
3
```

## Event Trigger Mapping Create and Update

Only KInesis and DDB are the two stream event source from CLI....

![1585716806879](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585716806879.png)![1585716847052](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585716847052.png)

**Here UUID needs to be passed in update function..**

![1585717085251](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585717085251.png)

## Adding lambda permission

![1585720791194](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585720791194.png)

## Cloud Watch Log Monitoring

aws logs describes all the functions related to cloud watch...SO they have

- describe-log-groups
- describe-log-streams
- get-log-events

**Log groups.....**

```
C:\Amit Stuff\Analytic\Deep Learning\Training Materials - AWS\Lambda Deep DIve>aws logs describe-log-groups
{
    "logGroups": [
        {
            "logGroupName": "/aws/lambda/lambda_function",
            "creationTime": 1584033780065,
            "metricFilterCount": 0,
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/lambda_function:*",
            "storedBytes": 2929
        },
        {
            "logGroupName": "/aws/lambda/lambda_function_cli",
            "creationTime": 1585124959104,
            "metricFilterCount": 0,
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/lambda_function_cli:*",
            "storedBytes": 4327
        },
        {
            "logGroupName": "/aws/lambda/test",
            "creationTime": 1585126199333,
            "metricFilterCount": 0,
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/test:*",
            "storedBytes": 0
        }
    ]
}
```

**Log Streams**

```

C:\Amit Stuff\Analytic\Deep Learning\Training Materials - AWS>aws logs describe-log-streams --log-group-name /aws/lambda/lambda_function_cli | more
{
    "logStreams": [
        {
            "logStreamName": "2020/03/25/[$LATEST]391ca74dafe040dcbda4e7a92cf4b0ca",
            "creationTime": 1585124995211,
            "firstEventTimestamp": 1585124995305,
            "lastEventTimestamp": 1585124995308,
            "lastIngestionTime": 1585125004381,
            "uploadSequenceToken": "49597026422084045866098667010918156045275269602658836146",
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/lambda_function_cli:log-stream:2020/03/25/[$LATEST]391ca74dafe040dcbda4e7a92cf4b0ca",
            "storedBytes": 445
        },
        {
            "logStreamName": "2020/03/25/[$LATEST]437f6d6686a346fcbec4d4ca82ab07bf",
            "creationTime": 1585125967246,
            "firstEventTimestamp": 1585125967344,
            "lastEventTimestamp": 1585125980494,
            "lastIngestionTime": 1585125980543,
            "uploadSequenceToken": "49605122274547900653353343460802189776614896029074178802",
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/lambda_function_cli:log-stream:2020/03/25/[$LATEST]437f6d6686a346fcbec4d4ca82ab07bf",
            "storedBytes": 2154
        },
        {
            "logStreamName": "2020/03/25/[$LATEST]85e699f7f9ce4b319858c8759d26f53a",
            "creationTime": 1585124959134,
            "firstEventTimestamp": 1585124959136,
            "lastEventTimestamp": 1585124959138,
            "lastIngestionTime": 1585124968210,
            "uploadSequenceToken": "49603586740926027481545138141854458099365727815176905506",
            "arn": "arn:aws:logs:us-east-1:196038177036:log-group:/aws/lambda/lambda_function_cli:log-stream:2020/03/25/[$LATEST]85e699f7f9ce4b319858c8759d26f53a",
            "storedBytes": 434
        },
```

**Getting log events**

```
C:\Amit Stuff\Analytic\Deep Learning\Training Materials - AWS>aws logs get-log-events --log-group-name /aws/lambda/lambda_function_cli --log-stream-name 2020/03/25/[$LATEST]8b765d5c22b0428eac86b649912941d2
{
    "events": [
        {
            "timestamp": 1585125693468,
            "message": "START RequestId: fb600fb7-c447-427b-8a64-a676a47dafe8 Version: $LATEST\n",
            "ingestionTime": 1585125702532
        },
        {
            "timestamp": 1585125693469,
            "message": "[ERROR] Runtime.MalformedHandlerName: Bad handler 'lambda_function_cli': not enough values to unpack (expected 2, got 1)",
            "ingestionTime": 1585125702532
        },
        {
            "timestamp": 1585125693471,
            "message": "END RequestId: fb600fb7-c447-427b-8a64-a676a47dafe8\n",
            "ingestionTime": 1585125702532
        },
        {
            "timestamp": 1585125693471,
            "message": "REPORT RequestId: fb600fb7-c447-427b-8a64-a676a47dafe8\tDuration: 2.07 ms\tBilled Duration: 100 ms\tMemory Size: 128 MB\tMax Memory Used: 49 MB\tInit Duration: 130.05 ms\t\n",
            "ingestionTime": 1585125702532
        }
    ],
    "nextForwardToken": "f/35349484197740927579372865399974096353618272421344641027",
    "nextBackwardToken": "b/35349484197674025343777273530549489198800327336826699776"
}

```

## Implementing an use case from CLI - S3 Bucket Notification

Our use case here is to implement a lambda function which will have event triggered from a S3 bucket whenever the S3.put event gets triggered into the S3 bucket by placing event files...

![1585723352767](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585723352767.png)

So our steps from CLI will be....

- Create functions
  - create-function
- Add permission for your event
  - add-permission
- Create event source

My test functions and buckets were already created. So I have started from 2nd step....This steps is for adding permission to my lambda.

```
C:\Amit Stuff\Analytic\Deep Learning\Training Materials - AWS>aws lambda add-permission --function-name "test" --statement-id "S3toLambda001" --action "lambda:InvokeFunction" --principal s3.amazonaws.com --source-arn "arn:aws:s3:::linuxacademy-lambda-amit"
{
    "Statement": "{\"Sid\":\"S3toLambda001\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-1:196038177036:function:test\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::linuxacademy-lambda-amit\"}}}"
}
```

This is how lambda function Lambda function **resource based policy** will be updated... **Note** 

- statement-id is mapped with sid in policy

```
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "S3toLambda001",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:196038177036:function:test",
      "Condition": {
        "ArnLike": {
          "AWS:SourceArn": "arn:aws:s3:::linuxacademy-lambda-amit"
        }
      }
    }
  ]
}
```

**Now create the even source...**

![1585735799421](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585735799421.png)

## Implementing an use case from CLI - Kinesis Stream Notification

Our use case here is to configure a Kinesis stream as an Event Source as shared below...

![1585737295798](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585737295798.png)

Our steps will remain same and they will be

- Create functions

  - create-function

- Add permission for your event

  - add-permission

- Create event source

  - create-event-source-mapping

  **Event Source Mapping**

  ![1585759766495](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585759766495.png)

## Lambda Invoke

Here invocation type is Event and hence this is async. So the status code is returned as 202.

![1585760232954](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585760232954.png)



# AWS SAM CLI AND SAM Local

This allows local testing of AWS Lambda functions without production deployment...

![1585761477459](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585761477459.png)

**NEED TO ADD**

# Lambda with Cloud Formation

![1585762543329](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585762543329.png)



# Cloud Watch Events and Lambda

## Intro

Cloud watch event is an almost real time event that is recorded by cloudwatch, and it could be used to trigger other AWS service is, and in our case, specifically AWS Lambda. Following are two different types of CW events can be used to trigger lambda functions...

- CW Events
- Scheduled Events

## Associating CW Rules and Lambda

**A sample Lambda Trigger:**

![Image](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2017/01/25/Diagram1-012417-MT.png)

**Dynamic ETL Pipeline Using AWS Step Functions and Lambdas**

![k](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2017/12/05/SGK_Arch_Diagram_Resized-1.png)

## Schedule Lambda On Cron Expression Triggers

The Cron expressions are created, evaluated and triggered using Cloudwatch Management Console. The possible cron expressions for AWS Lambda are discussed in [this](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html) link. In this blog, you can see that Lambda is triggered, based on Cron expressions.

There are two ways to create Cron expressions triggers, demonstrated below.

**First**, go to Cloudwatch Management Console > Rules > Schedule. Specify the desired Cron expressions and Add target to a pre-created Lambda Function.

![CloudWatch Rules](https://static1.tothenew.com/blog/wp-content/uploads/2017/05/cron-rules.png)

The cron expression can be validated in CloudWatch Console > Rules.

![cron-cw](https://static1.tothenew.com/blog/wp-content/uploads/2017/05/cron-cw.png)

It will serve as a centralized place for keeping and monitoring of all the cron expressions used in the infrastructure.

## Attributes of Events

![1585070251680](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585070251680.png)

Events has following components....

- Targets
- Rules
- Events

### Cloud Watch Alarms



![1585118227563](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1585118227563.png)

# References

- <https://www.simform.com/serverless-examples-aws-lambda-use-cases/>
- 