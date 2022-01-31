[TOC]



# Compute Domains

![1613477102389](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613477102389.png)

![1613477140815](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613477140815.png)

### EC2

Amazon Elastic Compute Cloud (EC2) is one of the most popular AWS services. EC2 allows you to launch different types of cloud instances and pay for them with a pay-per-use model. EC2 allows you to have operating system level control of your computing resources while running in Amazon’s computing environment. Amazon EC2 reduces the time required to obtain and boot new server instances from days or weeks to minutes. This allows you to quickly scale capacity, both up and down, as your computing requirements change. Amazon EC2 allows you to build and configure your instances as you like, from your desired operating system to your applications.

![1613477281192](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613477281192.png)

![1613477347496](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613477347496.png)

![1613557860827](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613557860827.png)

![1613560122602](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613560122602.png)

![1613560945993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613560945993.png)

![1613561012648](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613561012648.png)

![1613561064535](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613561064535.png)

![1613561116985](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613561116985.png)

#### EC2 Instance Tenancy

![1613561673134](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613561673134.png)

#### Storage Options

![1613565478935](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565478935.png)

![1613565627944](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565627944.png)

#### EC2 Security

![1613565682980](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565682980.png)

![1613565718775](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565718775.png)![1613565845676](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565845676.png)![1613565907738](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613565907738.png)

### Connecting to EC2

Start PuTTYgen. (no installation is required) 

3. Click **Load** and browse to the location of the private key file that you want to convert (for example keypair.pem). By default, PuTTYgen displays only files with a .ppk extension. You'll need to change the drop-down adjacent to **File name** to **All Files** in order to see your PEM file:

 ![alt](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/blobid2-33284b50-e60d-4adc-9ca0-80400a29ba75.png)

 

4. Select your .pem key file and click **Open**. PuTTYgen displays the following message:

![alt](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/blobid4-183da0e6-7348-4594-8dd0-69ea3f7056df.png)

 

5. Click **OK**. PuTTYgen displays a dialog with information about the key you loaded, including the public key and the fingerprint. 

6. Click **Save private key** to save the key in PuTTY's format. Do NOT select a passphrase. (Additional security is not required.) Be sure to save your private key somewhere secure.

1. Open your Terminal application 

2. Run the following ssh command: 

```
ssh -i /path/to/your/keypair.pem user@server-ip
```

- `server-ip` is the Public IP of your server, found on the **Description** tab of the running instance in the EC2 Console
- `user` is the remote system user (ec2-user for Amazon Linux) that will be used for the remote authentication. In this Lab, you must use **ec2-user**.

Note that the Amazon Linux AMIs typically use `ec2-user` as a username. Other popular Linux distributions use the following user names:

- Debian: admin
- RedHat: ec2-user
- Ubuntu: ubuntu

Assuming that you selected the Amazon Linux AMI, your assigned public IP is 123.123.123.123, and your keypair (named "keypair.pem") is stored in /home/youruser/keypair.pem, the example command to run is: 

```
ssh -i /home/youruser/keypair.pem ec2-user@123.123.123.123
```

### Instructions (Windows Users)

Windows has no SSH client, so you must install one. This part of the Lab Step will use PuTTY (freely available [here](http://www.putty.org/) on their website) and a previously converted PEM key (converted from PPK using PuTTYgen).

 

1. Open PuTTY and insert the EC2 instance public IP Address in the **Host Name** field:

![PuTTY: Insert Instance IP](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/putty-connect-step1-4ba34dd1-377c-4f0c-9bd2-c6e63c909cc4.jpg)



2. Navigate to **Connection** > **SSH** > **Auth** in the left pane and then select the downloaded private key in PPK format:

![PuTTY: Select PPK Key](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/putty-connect-step2-8c3b46af-7039-465f-a830-8974d6b20252.jpg)

After a few seconds, you will see the authentication form. 

 Login as *ec2-user* and you will see the EC2 server welcome banner and be placed in the Linux shell:

![alt](https://assets.cloudacademy.com/bakery/media/uploads/blobid0-2e0e20fd-e8ff-433b-acc7-a323f92bb06e.png)

**List all instance metadata by issuing the following command:**

[Copy code](https://cloudacademy.com/lab/create-your-first-amazon-ec2-instance/getting-the-ec2-instance-metadata/?context_id=180&context_resource=lp#)

```
curl -w "\n" http://169.254.169.254/latest/meta-data/
[ec2-user@ip-172-31-22-236 ~]$ curl -w "\n" http://169.254.169.254/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
[ec2-user@ip-172-31-22-236 ~]$

## Enter the following commands to extract specific metadata associated with your running instance: 

[ec2-user@ip-172-31-22-236 ~]$ curl -w "\n" http://169.254.169.254/latest/meta-data/security-groups
amit-launch-wizard-1

[ec2-user@ip-172-31-22-236 ~]$ curl -w "\n" http://169.254.169.254/latest/meta-data/hostname
ip-172-31-22-236.us-west-2.compute.internal
[ec2-user@ip-172-31-22-236 ~]$
```

## ECS - Elastic COntainer service

This service allows you to run Docker-enabled applications packaged as containers across a cluster of EC2 instances without requiring you to manage a complex and administratively heavy cluster management system.  

![1613566532333](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613566532333.png)

![1613566685800](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613566685800.png)

![1613566784779](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613566784779.png)

![1613566858183](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613566858183.png)

![1613566960573](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613566960573.png)

## ECR - Amazon Elastic Container Registry

![1613567106643](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567106643.png)![1613567125994](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567125994.png)![1613567177782](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567177782.png)![1613567244835](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567244835.png)![1613567872589](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567872589.png)![1613567885148](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567885148.png)![1613567943676](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567943676.png)![1613567959851](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567959851.png)![1613567986574](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613567986574.png)

## EKS - Amazon Elastic Container Service for Kubernetes

**Resources referenced within this lecture:**

[Introduction to Kubernetes](https://cloudacademy.com/course/introduction-to-kubernetes/)

[Install Kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)

IAM Authenticator:

\- [Linux](https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/linux/amd64/aws-iam-authenticator)

\- [MacOS](https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/darwin/amd64/aws-iam-authenticator)

\- [Windows](https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/windows/amd64/aws-iam-authenticator.exe)

[Configuration map to joing the Worker Node to the EKS Cluster](https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2019-02-11/aws-auth-cm.yaml)

[Introduction to EKS](https://cloudacademy.com/course/introduction-to-aws-eks/)

![1613568084669](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613568084669.png)![1613568698271](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613568698271.png)

![1613568745828](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613568745828.png)![1613568787248](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613568787248.png)

![1613632034846](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613632034846.png)



## AWS Elastic Beanstalk

AWS Elastic Beanstalk is an AWS managed service, that allows you to upload the code of your web application along with environment configurations, which will then allow Elastic Beanstalk to automatically provision and deploy the appropriate and necessary resources required within AWS to make the web application operational. 

**Resources referenced within this lecture:**

[Lab: Deploy a PHP Application using AWS Elastic Beanstalk](https://cloudacademy.com/amazon-web-services/labs/deploy-php-application-using-elastic-beanstalk-26/)

[Lab: Run a controlled deploy with AWS Elastic Beanstalk](https://cloudacademy.com/amazon-web-services/labs/run-controlled-deploy-aws-elastic-beanstalk-43/)

![1613569098112](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569098112.png)![1613569142980](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569142980.png)![1613569174913](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569174913.png)

### Elastic Beanstalk Components

![1613632107362](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613632107362.png)

![1613569237862](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569237862.png)![1613569309448](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569309448.png)![1613569342826](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569342826.png)![1613569919293](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569919293.png)![1613569952356](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569952356.png)![1613569993696](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613569993696.png)![1613570018897](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613570018897.png)

![1613570099746](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613570099746.png)

### Beanstalk Workflow

![1613570288341](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613570288341.png)



## AWS Lambda

**Resources referenced within this lecture:**

[AWS Lambda Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html#supported-event-source-s3)

[Understanding AWS Lambda to Run and Scale your Code](https://cloudacademy.com/course/understanding-aws-lambda-to-run-scale-code/)

[Lab: Introduction to AWS Lambda](https://cloudacademy.com/amazon-web-services/labs/introduction-aws-lambda-22/)

[Lab: Process Amazon S3 events with AWS Lambda](https://cloudacademy.com/amazon-web-services/labs/aws-lambda-s3-events-55/)

[Lab: Automating EBS snapshots with AWS Lambda](https://cloudacademy.com/amazon-web-services/labs/automating-ebs-snapshots-lambda-and-cloudwatch-events-45/)



![1613630407250](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613630407250.png)![1613630533302](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613630533302.png)![1613630744164](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613630744164.png)![1613630815494](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613630815494.png)

## AWS Batch

As the name suggests, this service is used to manage and run Batch computing workloads within AWS. Before we go any further, I just want to quickly clarify what Batch computing is. 

Batch computing is primarily used in specialist use cases which require a vast amount of [compute](https://cloudacademy.com/course/compute-fundamentals-for-aws/introduction-to-aws-compute-fundamentals/) power across a cluster of compute resources to complete batch processing executing a series of jobs or tasks.

**There are effectively five components that make up AWS Batch service which will help you to start using the service, these being:**

![1613631106094](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631106094.png)



![1613632231087](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613632231087.png)

![1613631154032](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631154032.png)![1613631205295](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631205295.png)![1613631250286](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631250286.png)![1613631303650](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631303650.png)![1613631317067](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631317067.png)

## Amazon Lightsail

This is another [compute](https://cloudacademy.com/course/compute-fundamentals-for-aws/introduction-to-aws-compute-fundamentals/) service that in some respect closely resembles EC2 out of all the other compute resources we have covered so far. Amazon Lightsail is essentially a virtual private server, A VPS, backed by AWS infrastructure, much like an EC2 instance but without as many configurable steps throughout its creation. 

**Resources referenced within this lecture:**

[Amazon Lightsail dashboard](https://lightsail.aws.amazon.com/ls/webapp/home/resources)

![1613631436222](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631436222.png)![1613631476999](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631476999.png)![1613631651426](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631651426.png)

## Summary

![1613631769027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631769027.png)![1613631800682](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631800682.png)

![1613631823517](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631823517.png)

![1613631880586](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631880586.png)

![1613631908991](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631908991.png)![1613631924220](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1613631924220.png)



# Amazon Elastic Block Store (EBS) 

EBS provides **persistent** and **durable block level storage**. As a result, EBS volumes offer far more flexibility with regards to managing the data when compared to data stored on instance store volumes. EBS volumes can be attached to your EC2 instances, and are primarily used for data that is rapidly changing that might require a specific Input/Output operations Per Second rate, also known as IOPS.

EBS volumes are **independent of the EC2 instance**, meaning that they exist as two different resources. They are logically attached to the instance instead of directly attached like instance store volumes. From a connectivity perspective, **only a single EBS volume can only ever be attached to a single EC2 instance**. However, **multiple EBS volumes can be attached to a single instance**.

Due to the EBS ability to enforce persistence of data, it doesn't matter if your instances are intentionally or unintentionally stopped, restarted, or even terminated, the data will remain intact when configured to do so. EBS also offers the **ability to provide point in time backups of the entire volume** as and when you need to. These backups are known as **snapshots** and you can **manually invoke a snapshot** of your volume at any time, or use Amazon CloudWatch events to perform an automated schedule of backups to be taken at a specific date or time that can be recurring.



# Basics and Fundamentals of Serverless


  ![1614606453316](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614606453316.png)

![1614606548696](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614606548696.png)

![1614606668490](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614606668490.png)

![1614606861503](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614606861503.png)

![1614609097217](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614609097217.png)

# VPC

An AWS Virtual Private Cloud (VPC) is the fundamental backbone of application architecture inside of AWS. A VPC is designed to mimic private on-premises data centers and corporate networks and provides the network framework in which you will be building applications. However, before you learn about all the various networking components in a VPC, let's discuss and learn about the basic essentials.

![1614610104307](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610104307.png)

Here is how it looks like…

![1614610394199](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610394199.png)

![1614610312331](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610312331.png)

![1614610486294](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610486294.png)

![1614610516120](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610516120.png)

![1614610770106](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1614610770106.png)

















































