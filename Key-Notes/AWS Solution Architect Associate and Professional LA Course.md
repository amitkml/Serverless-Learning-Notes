[TOC]

# Region

![1604549225642](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604549225642.png)

# Edge Location

we can sometime develop lamba at edge location like for IOT device. This is called lambda at Edge.

![1604549346305](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604549346305.png)

# Interact with AWS

![1604549440289](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604549440289.png)

# Core Infrastructure and Services

![1604895163633](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604895163633.png)



# AWS Fundamentals

![1597225300747](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597225300747.png)



## Security

### IAS

![1589373747623](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589373747623.png)

## PaaS

![1589373890018](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589373890018.png)

### SaaS

![1589373987154](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589373987154.png)

## High Availability vs. Fault Tolerance

Knowing the difference between Fault Tolerance (FT) and High Availability (HA) can help you avoid costly and, in some cases, critical errors. 

![1589374374969](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589374374969.png)

## RPO vs. RTO

Recovery Point Objective (RPO) and Recovery Time Objective (RTO).

![1589374975238](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589374975238.png)

## Scaling

Implementing an effective scaling process in AWS is an essential skill for any solutions architect.

### Vertical Scaling

![1589378505566](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589378505566.png)

### Horizontal Scaling

- requires data to be separated in their corresponding pool

![1589378690801](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589378690801.png)

## Tiered Application Design

Designing tiered applications and understanding tiered architecture are both essential skills for an effective solutions architect.

- Monolithic application has all the presentation, logic and data are in same compute unit and hence it can only be horizontally scaled.
- 2nd diagram represents how we have presentation running in single unit, logic is running in three compute unit and data application is running two compute unit. So it has been possible to horizontally scale.

![1589378986437](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589378986437.png)

## Encryption

Encryption is a process used extensively in AWS. This lesson introduces the fundamentals of encryption and includes a short demonstration of basic encryption.

```
echo "Cats are Amazing" > hiddenmessage.txt
gpg -c hiddenmessage.txt
cat hiddenmessage.txt.gpg
# this clears the cached password
echo RELOADAGENT | gpg-connect-agent
gpg -o output.txt hiddenmessage.txt.gpg
rm hiddenmessage.txt.gpg
rm output.txt
gpg --gen-key
gpg --armor --output pubkey.txt --export 'Adrian'
gpg --armor --output privkey.asc --export-secret-keys 'Adrian'
gpg --encrypt --recipient 'Adrian' hiddenmessage.txt
gpg --output decrypted.txt --decrypt hiddenmessage.txt.gpg
```

![1589392881169](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589392881169.png)

## Architecture Odds and Ends

- Cost-effective architecture
- Secure architecture
- Application session state
- Undifferentiated heavy lifting

![1589393847176](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589393847176.png)

## AWS Accounts

AWS accounts are more than just a way to log in and access AWS services — they are a crucial AWS feature that AWS solutions architects can use to implement secure and high-performance systems. In this video, we will talk about the capabilities of AWS accounts, including:

- Authentication
- Authorization
- Billing

**Root User**

![1589394512392](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589394512392.png)

![1589394651592](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589394651592.png)

![1589394717185](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589394717185.png)

## AWS Physical and Networking Layer

AWS manages a high-performance, reliable, and cost-effective global infrastructure platform.

**Region is local grouping of infrastructure and this is done from local regulation aspect. If one region fails then also it does not impact other regions. This also gives flexibility of company line netflix to operate globally. It also gives flexibility of data separation across region unless we want to do in separate way.**

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Infrastructure](https://www.infrastructure.aws/)
- [General](https://docs.aws.amazon.com/general/latest/gr/rande.html)

![1589394858563](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589394858563.png)

![1589395816517](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589395816517.png)

## Well-Architected Framework

<https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf>

- Generalized design principle
- Using automation for architecture testing 
- Drive architecture using data
- Applying security in all layers
- using login for tracing
- Implement automatically without intervention 

**Pillars are design principles in following area**

![1589395961339](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589395961339.png)

![im](https://devopedia.org/images/article/99/2184.1530439228.jpg)

![im](https://cloud.epam.com/site/develop/blog/2017/a=w=s_well_architected_review/wa_pillars.png)

![im](https://volansys.com/wp-content/uploads/2019/03/VOLANSYS-Pillars-of-AWS-Well-Architected-update-1.png)

## Elasticity

horizontal and vertical scaling by diving into elasticity (automated horizontal scaling) 

**Scaling**

- Vertical

  - We purchase capacity based on estimated demand. It means increasing capacity of existing server memory or cpu. Cant do granular adjustment of capacity as per load. Either we have more capacity or we have less w.r.t to demand

  ![1589427666748](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589427666748.png)

  

- horizontal

![1589427803844](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589427803844.png)

- Elastic

![1589427895009](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589427895009.png)

**elastic**

![im](https://miro.medium.com/max/3004/1*HldsGHvKzHoyiJwqiDbl1A.png)

# AWS Product Fundamentals

## Console Tour and Navigation

![im](https://miro.medium.com/max/680/0*BT4ZoPv48yy9S75i.jpg)

## Introduction to S3

Simple Storage Service, or S3, is an object storage product provided by AWS. It's one of the most widely-used and flexible AWS services. **Note**: [S3 now supports Same-Region Replication](https://aws.amazon.com/about-aws/whats-new/2019/09/amazon-s3-introduces-same-region-replication/)

**When and why S3 to be used as file?** S3 is good to share objects across aws and it auto scalable. It can be used scalable manner for bulk files in public cloud. **Mounting S3 as network drive is extremely difficult and inflexible.** S3 is NOT Block storage and it is fie storage.

It is Object based storage service and not block based. It is ideal fir storing files but not for storing OS and thus it cant be used as storage for EC2 instance. Data within S3 is stored as key value pair with its metadata.

Every object in S3 is uniquely identified by Object key which is a sequence of UTF8 characters. S3 internally stores the file sequentially. So filename impacts file retrieval. So it is good practice to have date-time etc unique as file prefix. AWS uses Object Key and Version id combination to uniquely identify a file. 

**Note: S3 no longer supports bucket names with uppercase letters or underscores.**

![1589429084615](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589429084615.png)

![1589430278688](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589430278688.png)

## Introduction to CloudFormation

It is an automation product within AWS. CloudFormation allows a Solutions Architect to design and declare infrastructure in advance — creating a template that can be used to consistently deploy infrastructure in AWS. It uses **Infrastructure as code** product. It uses template file as either json or yml file.

**CloudFormation is a powerful automation product within AWS. It can be used to create simple or complex sets of infrastructure any number of times.**

- Aim is infrastructure automation
- Template contains definition of logical resources
- These templates used to create a stack. stack is combination of logical resources and it creates physical resources. So stack creates physical resources for every logical resources.

![1589430724441](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589430724441.png)

**stack creates multiple events as part of physical resource creation**

![1589514954418](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589514954418.png)

![1589515312230](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589515312230.png)

### Lesson Files

- [GitHub Lesson Files](https://github.com/linuxacademy/content-aws-csa2019/tree/master/lesson_files/01_aws_sa_fundamentals/introduction_to_cloudformation)
- [CloudFormation Template](https://s3.amazonaws.com/cloudformation-templates-us-east-1/WordPress_Single_Instance.template)
- [CloudFormation Resource Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)

# AWS Organizations

AWS Organizations is useful for businesses that need to manage multiple accounts. It provides the following features:

Used to manage multiple aws accounts rather than each aws account individually.

- Consolidated billing
- Service control policies (SCPs)
- Account creation
- Simplified role switching

![1599980749381](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599980749381.png)

![1599980821536](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599980821536.png)

![1600003571197](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600003571197.png)

![1600004957309](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600004957309.png)

## AWS Organistaion - LA Professional

![1600666039872](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600666039872.png)

![1600666468575](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600666468575.png)

### Service Control Policies

**So remember, service control policies inherit downwards. Now, there is one exception to this, and that's the master account. Master accounts could be placed anywhere inside in a TBS organization. On While service control policies can be applied to this account, the effect of being applied won't be so. To all intents and purposes, you need to ignore the master account. Master accounts are not affected in any way by service control policies. And so, from a best practice perspective, what I found toe work really well is avoid using the master account. For any services within your AWS deployment, you can use the master account for account and for billing purposes. So in my case, I do log in to my master account, and then I roll switch into any of my member accounts. But I don't have resource is in this master account**

SCP can have

- define what actions can be taken (ALLOW statement)
- define what actions can be taken (it overrides previous one if allowed) (DENY Statement)
- If there is no explicit Allow then by default it is deny.

![1600668885687](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600668885687.png)

### AWS Support Tiers

![1600669950193](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600669950193.png)

### AWS Account Limits

Example....

![1600669763541](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600669763541.png)

**Some of these limits can be changed by raising SR with AWS but some are not. So how they impact Solution Architect in designing solution.**

#### Links

<https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information> <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>
<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html>

### AWS Config

![1600673651826](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600673651826.png)

**Sample AWS Config Output on changing attributes of EC2**

![1600675144406](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600675144406.png)

### AWS Service Catalog

Applicable for bigger company and helps to implement AWS It service catalog policies.![1600675593291](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600675593291.png)

#### Links

<https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamenduser.html>

# IAM (Identity and Access Management)

It has 

- Authentication
- Autorization

## Authentication

- who am I

![1603091490985](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091490985.png)

## Authorization

- What i can do based on permission defined in policies. Policies are defined in json files.
- Logically group users by creating groups as shown below
- Every group will have associated policy
- Group will have associated users

![1603091603460](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091603460.png)

## How it works?

![1603692225330](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603692225330.png)



Common use is to manage

- Users
- Roles
- Groups
- IAM Access Policies
- API keys
- Password Policies
- Authentication attributes 9user name, password, keys, mfa and password policies)

Identity and Access Management, known as IAM, is one of the key services within AWS. It controls access to the AWS API endpoints that are used by the console UI, command line tools, and any applications wanting to utilize AWS.

We get root user when we create an AWS account. Basically this user has information on billing, define new users, security roles etc.

- IAM is universal and does not apply to region.
- New users have **No Permission** when created.
- New users are assigned **Access Key and Secret Access Key**  when they are created and they are not same as password. These Keys are used for accessing from API and CLI.

![1597325482617](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597325482617.png)

**IAM users and roles are real identities and that means they have resource ARN. So such identity can be accessed by using ARN. Groups are not real identities and they don't have ARN.**



![1590744200576](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590744200576.png)

**IAM Best Practices**

![im](https://image.slidesharecdn.com/sec302-151008030741-lva1-app6891/95/sec302-iam-best-practices-to-live-by-19-638.jpg?cb=1445013916)

![1590747390895](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590747390895.png)

**IAM Password Policy**

![im](https://dmhnzl5mp9mj6.cloudfront.net/security_awsblog/images/clm-BlogPicture1-v2-2.PNG)

ARN is an unique number for every resource. ARN always begin with ARN and the partition, then list the service, list the region , list the account id, resource type and resource

![1589519156255](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589519156255.png)

**Handles authentication and authorization.**

![1589518641176](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589518641176.png)

## IAM Users

IAM users are one identity provided by IAM.

![1592648556770](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592648556770.png)

![1592649531578](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592649531578.png)



## IAM Policies

IAM policies are JSON documents that **either allow or deny access to combinations of actions and resources**.

![1603695016075](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603695016075.png)

### More on Policies

**Lets understand the following policy which only allows read operation on any S3 bucket.**

- Effect of Allow means it will allow and not deny
- Action of Get and List mean it will allow to read’
- S3::  before Get and List allows operation only on S3 resource
- Resource of * means that all resources are allowed but since we have S3::Get and S3::List so effectively only READ operation on S3 resources are allowed and other resources are not allowed.

![1603695465666](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603695465666.png)

**Policy can be attached with uses, roles and groups as shared below…**

![1603091842893](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091842893.png)

**It can be attached with an Identity (profile and so it is called Identity Policy) and it can be attached with Resource (S3 bucket and so called resource policy)**.

- Policy document consist of multiple statements and every statement have
  - Effect means allow or deny
  - Action means one or more api call on resource (what to allow)
  - Resource means which resource means (single arn or multiple arn or wildcard to allow or)
- ![1603091812334](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091812334.png)
- 

![1589532454675](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589532454675.png)

SID is statement id and effect is "Allow" here and it is on specific resource name as shared above. Policies can be attached with role, users and they are called in-line policy. 	

Lets review the above IAM policy. It has effect of **Allow** and it is going to allow on resource DDB named **CatPics** and then action element describes what are the actions to be allowed on that DDB. **Another sample policy is**

![1589532845205](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1589532845205.png)

![1592648179750](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592648179750.png)

**sample policy for accessing S3**

![1590748708167](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590748708167.png)

**Lets take the example of following two scenarios**

- Three users need to access a S3 bucket. So we could have createdS3 Full Access policy separately for all three users as shown above but this method is not flexible. However best method is to create the group and attach the policy with group. Now this group can be associated with user.
- There is a EC2 instance shown below which is accessing S3 bucket and so here the IAM role and policy attached to the role. *IAM roles are preferred approach so that one AWS Service can access another AWS service*.

**Key here is that IAM Policy can be attached with IAM Role or Users directly or Groups**

![1590749382798](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590749382798.png)

## IAM Roles

**We can allow AWS resources like EC2 or to non-AWS account users to take actions on our AWS account using IAM Roles.** IAM roles are a required component of allowing AWS resources to take actions on other AWS services

![1603697246772](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603697246772.png)

- No credentials associated
- An API available to assume the role for temporary time and temp credentials is achieved by assuming the role

  ![1603697276993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603697276993.png)

![1603092061698](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092061698.png)

**Here EC2 instance will assume the role to fetch details.**

![1603092180098](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092180098.png)

**Here users from another AWS account will assume role and access into another AWS one. It is temporary session toke with access key, secret key and duration of that access which they get when they assume role.**

**IAM not for application and this is resource level permission and not for OS or application. There are other ways for application access.**

![1603092243364](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092243364.png)

## IAM Groups

IAM groups allow for large-scale management of IAM users. This way, policies can be applied to groups and impact collections of similar users.[IAM Groups not real identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) `Note that a group is not truly an "identity" in IAM because it cannot be identified as a Principal in a permission policy. It is simply a way to attach policies to multiple users at one time.`

### Example

- Three users have been mapped with Group Dev
- Group Dev has IAM policy attached for S3 full access

![1603696474143](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603696474143.png)

Following diagram shows Group:Admin has IAM policy attached. It also shows that user Ashley has policy attached. Group can have inline policy or managed policy attached.

![1592649690475](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592649690475.png)

![1592650264034](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592650264034.png)

## IAM Access Keys

Access keys consist of access key IDs and secret access keys. Access keys are the long-term credentials used to authenticate to AWS for anything but the console UI. ![1592650688742](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592650688742.png)

**Users can have maximum two access key irrespective of their status.** User name, password and access key are called long term keys and they don't expire. Access key dont allow to authenticate from UI and only it is used from CLI.

![1592650982305](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592650982305.png)

## Creating an IAM User and Setting Up the CLI

Steps are:

- Adding an IAM user
- Adding MFA to that IAM user
- Creating an access key pair
- Installing the CLI tools on Windows, Linux, and MacOS

### Windows Tools Install

1. Visit: [AWS Command Line Interface](https://aws.amazon.com/cli/).
2. Download and run the 64-Bit installer, accepting all defaults.
3. Open the command prompt, and verify tools are installed using `aws`.
4. Run `aws configure` and enter the access key ID and secret access key you noted down earlier in the lesson, with `us-east-1` as the region and `json` as the default output format.

### Linux Install (Tested on CentOS)

```
sudo yum install epel-release
sudo yum install python-pip
sudo pip install awscli
```

Run `aws configure` and enter the access key ID and secret access key you noted down earlier in the lesson, with `us-east-1` as the region and `json` as the default output format.

### Testing

```
aws s3 ls
```

## IAM Roles

IAM roles are one of the more difficult identity types to understand in AWS. ![1592651521338](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592651521338.png)

- Roles cant be used to login

- Roles dont have access key and no long term credentials

- Roles is only useful when i have an identity (user details)

- pattern when roles useful

  - Used when sudden access required
  - EC2 may have a role to access S3 folder. This means EC2 instance don't need an user regular credentials
  - Similarly a lambda function may have an role to use to interact with other aws service.
  - **Lets have we have two company and each of them 2000 users. Now company got merged and all these 4000 users need access in our aws instance. So one approach is to create new 2000 users into our aws which is quite a lot admin work; another approach is create an IAM roles and define a trust policy. Then assume other company 2000 users to take that role into our aws instance.**
  - **Role is like a fire marshal where wen a person takes that role then gets additional powers but till they are fire marshal.**

  Role is also related **web identity federation**.

  ![1592653748350](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592653748350.png)

### Exam Tips

![1600612307482](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600612307482.png)

## Security Token Service

AWS STS can help us to avoid potential security risks such as embedding long-term API credentials. 

![1603704629587](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603704629587.png)

## IAM API Keys

AWS API keys are one of the most fundamental tools in your AWS Developer toolbox and understanding how to provision them and how they work is critical to making sure you'll be able to interact with the AWS environment using powerful tools like the AWS CLI and AWS SDKs.

Learn more about Instance Metadata and Userdata here: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval>

![1603705142915](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603705142915.png)



## AWS Inspector

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of detailed assessment reports which are available via the Amazon Inspector console or API.

## Cognito Essentials

![1603733469539](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603733469539.png)

## Shared Security responsibility

![1603091170457](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091170457.png)

## Security

![1603091321155](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091321155.png)

![1603091298469](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603091298469.png)

## IAM Best Practises

![1603092372310](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092372310.png)![1603092398225](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092398225.png)



## IAM - SA

**Managed policies can be used to attach with hundreds of IAM users. How we do?**

- Create managed policy
- create a group
- Attach the policy with the group
- Open the group and associate users with the group

![1597589944896](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597589944896.png)

Policy

- Identity Policy
  - Attached with IAM users, group
- Resource Policy

### Identity Policy

**Policies support condition also which gives extra condition to statement.**

![1597593596180](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597593596180.png)

**Here is another Identity policy document where we can add date-time check also.** 

![1597639373039](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597639373039.png)

In order to have greater flexibility, we can add variables into IAM policies which can support system variables. **All the variable does is call and get the system variable to literally replace it.**

![1597594202472](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597594202472.png)

### Resource Policy

Every bucket has bucket policy which is called resource policy. **So even if the Identity policy allows the user to have access into bucket but if the bucket policy for the bucket has deny then it will not be allowed.**

**sample resource policy**

- here principal is required for resource policy. principal is specifies the resource name on which resource policy is applied. **principal is not mandatory for identity policy.**

![1597639729343](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597639729343.png)

These role credentials have expiry as shared below.

![1597659354854](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597659354854.png)

### Revoking roles for a paritcular use

First we need to revoke ..

![1597659818126](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597659818126.png)

**and then after revoke it will be as below..a new permission policy created...**

 ![1597659960203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597659960203.png)![1597659889099](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597659889099.png)



Then we assume the role as shared below...

![1597660247656](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597660247656.png)



### Files used in lesson

<https://github.com/linuxacademy/aws-csa-pro-2019/tree/master/01_accounts/IAM/Identity-and-resource-policies>

### Lesson Links

<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html>
<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>
<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html>

### IAM Roles and Temporary Security Credentials

This video demonstrates the IAM role architecture. It details TRUST and PERMISSIONS policies, how role assumption operates and how temporary security credentials can be utilized within AWS. Roles can be attached to EC2 instance or other IAM users and then they get permission by assuming the role to work.

**Every role has trust policy document attached and it allows or deny while assuming that role.** Here is a sample role where IAM user 568398962038 is allowed to assume this role. Trust policy is required when you are assuming the role.

![1597643019018](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597643019018.png)

![1597642888807](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597642888807.png)

**Similarly Roles has permission attached which defines what are the actions i can take.** Permisison is always checked.

![1597644177071](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597644177071.png)

#### More on Roles

![1597642132946](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597642132946.png)

#### Lesson Links

<https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html>

#### Cross-Account Access: Resource Permissions vs. Cross-Account Roles

This lesson evaluates a few alternative ways of accessing a resource in an external account, with a focus on the security and architecture differences.

![1597661740910](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597661740910.png)



##### Lesson Links

- [Granting Cross-Account Permissions Example](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-8)
- [IAM Policies and Bucket Policies and ACLs! Oh, My! (Controlling Access to S3 Resources)](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

# AWS SQS

AWS Simple Queue Service (SQS) is a distributed queuing service application where we can add and read messages over the Internet.

AWS SQS can be accessed via Web Services API and AWS SDK, which is available for different programming languages.

![1597225415037](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597225415037.png)

![1597225760218](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597225760218.png)

**Here the first one is short poll while the last one is long poll.**

![1597226193993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597226193993.png)



## Standard Queue

Standard queue is the default queue type supported by AWS SQS. It doesn’t restrict the number of transactions per second, and it ensures that messages are delivered at least once. This type of queue is used when there aren’t any critical events that need to be processed by consumer applications since there may be duplicate messages that need to be handled in the application.

## FIFO Queue

In FIFO queues, Amazon SQS also provides content-based deduplication. Content-based deduplication allows SQS to distinguish the contents of one message from the contents of another message using the message body. This helps eliminate duplicates in referential systems such as those that manage pricing

![im](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2017/03/28/QueueTypes-1.jpg)

The order of messages leaving a FIFO queue is governed by three rules:

1. Return the oldest message where no other message in the same message group is currently in-flight.
2. Return as many messages from the same message group as possible.
3. If a message batch is still not full, go back to rule 1.

![im](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2018/05/14/sqs_fifo_blog_img7-1-1024x341.png)



```
Name: TradeStatus.fifo

URL: https://sqs.us-west-2.amazonaws.com/12345678/TradeStatus.fifo

The scripts below are in Python2.

import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='TradeStatus.fifo')

try:
    userInput = raw_input("Please enter file name: ")
except NameError:
    pass

with open(userInput, 'r') as myfile:
    data=myfile.read()

response = queue.send_message(
    MessageBody=data,
    MessageGroupId='messageGroup1'
)

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
The following Python code receives the message from the TradeStatus.fifo queue and deletes the message when it’s received. Afterward, the message is no longer available.

import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='TradeStatus.fifo')

# Process messages by printing out body
for message in queue.receive_messages():
    # Print out the body of the message
    print('Hello, {0}'.format(message.body))

    # Let the queue know that the message is processed
    message.delete()
Note: In Python, you need only the name of the queue.
```

### Advantage

- High Availability: AWS SQS provides high availability for sending and receiving messages as they are stored on distributed servers.
- Authentication: To access the queue, permission is necessary at the queue level. The users can access the queue based on AWS IAM.
- Visible Timeout: When a consumer reads a message from the queue, it hides the message that is being processed so that no other consumer processes it.
- Delay Messages: Delay of messages can be configured at the queue level as well as at the message level while sending messages.
- Cost: AWS charges only for the API requests that are made to SQS so there are no fixed costs attached with AWS SQS.

### Lesson Links	

- [Policy Evaluation Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

Simple Queue Service (SQS) provides standard or FIFO queues as a service. It helps applications scale by allowing decoupling of application components and inter-process, -service, and -server messaging.

It can have resource policy to indicate who can add messages into Q.

![1594142372069](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594142372069.png)

![1594142404350](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594142404350.png)

![1594142769079](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594142769079.png)

## Lesson Commands

```
aws sqs get-queue-attributes --queue-url https://URL --attribute-names All
aws sqs send-message --queue-url https://URL --message-body "INSERTMESSAGE"
aws sqs receive-message --queue-url https://URL
aws sqs delete-message --queue-url https://URL --receipt-handle "INSERTHANDLE"
aws sqs receive-message --wait-time-seconds 10 --max-number-of-messages 10 --queue-url https://URL
aws sqs --region us-east-1 receive-message --wait-time-seconds 10 --max-number-of-messages 10 --queue-url https://URL
aws sqs delete-message --queue-url https://URL --receipt-handle "INSERTHANDLE"
```

## More on SQS

Getting message from SQS

- Long Poll
  - Much more efficient
  - It will wait till polling time is not over and read again to return 10 messages
- Short Poll
  - It will return immediate

"receipt-handle" value for the queued message is required for deleting from SQS as shared below.

![1594143734880](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594143734880.png)

Message in queue gets hidden till visibility period is not over once it is read. If the reader of the queue does not delete the message from SQS after reading then message will appear again in SQS.

## Simple Queue Service (SQS) - SA Course

This lesson looks at the architecture of SQS, restablishes some of the key concepts, and discusses at a high level the differences between SQS and Kinesis from an architectural perspective.

![1597225377817](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597225377817.png)

## Key Facts

![1597342295100](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597342295100.png)

![1597342335750](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597342335750.png)

![1597342259356](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597342259356.png)

## Exam Tips

![1597343185542](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343185542.png)





# AWS Networking

## VPC

- Default VPC created whenever we create AWS account
- Subnet is a sub-section of network
- Hierarchy is
  - AWS Cloud which encompasses of HA, Availability zone etc
    - Virtual Public Cloud. So within AWS Cloud, we can have multiple VPC. **VPC is capable of spanning into multiple availability zones**.
      - SubNet. So within a VPC, we can have multiple SubNet.
        - Resources. Resources are placed under their own corresponding subnet.

![im](https://s3.amazonaws.com/apnblog/2016+Blog+Images/VPC+Pt+2/VPC+Peering.png)

## Route53

![1600601119672](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600601119672.png)

Steps:

- Register a domain

- Once domain gets approved then we can see the same within hosted zone

  - "Record " set under domain allows create "A record". This is where we define DNS Record.

  ![1600608524148](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600608524148.png)

- a

## Internet Gateways and Route Tables

- Internet Gateway allows application(resources) running within VPN to access public internet. It is highly scalable.

  - No bandwidth constraint in internet gateway

- Internet Gateway will be associated with VPC. This is 1:1 relationship.

- Route table directs where traffic should go. Default VPC always has main route table.

- Route table always point to IGW.

  ![1590754305987](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590754305987.png)

  

  

![im](https://docs.aws.amazon.com/vpc/latest/userguide/images/internet-gateway-overview-diagram.png)



![1590754730047](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590754730047.png)

![1590754925691](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590754925691.png)

## VPC Subnets, Security Groups, and NACLs

- Public subnet has access into Internet. This is possible because in route table for them they have IGW attached.

![1590755665733](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590755665733.png)

**Example where FTP not allowed and http allowed** . NACL is stateless.

![1590755850440](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590755850440.png)

NACL has inbound and outbound separate rules. Rules are executed from lowest to highest.  Each of the rule gets evaluated independently and gets applied on traffic regardless of next rule.

- Default NACL has  by default all type of traffic allowed.
- For new NACL by default everything denied.

![1590756059007](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590756059007.png)

- Security groups are associated at instance level and not at subnet level.

### VPC SA Professional

#### IP Subnetting basic

>  **subnet masks lying between 8- 15 are A class masks, from 16- 23 are B class and 24-32 are C class masks.** 

- Class A includes 0-127 where 0 and 127 are reserved, the default subnet mask **for this class is /8** .

- Class B includes 128-191 in their first octet, and the default subnet mask for **this class is /16**

- Class C deals with 192-224 in their first octet and the default subnet mask for **this class is /24**

> Now once you see it, lets tackle some real life questions. Lets find the no of subnets and valid hosts for **192.168.10.10/18**
>
> See this ? its a C class IP address having a mask of B class (*as the mask lies between 16-24*) now, in order to find the number of subnets, use the following formulae -
>
> > **2 ^ (What mask you have been provided – default mask of the IP address given)**
> >
> > > 2^(18-16) –>  2^(2) –>  4 subnets
> > >
> > > Now for calculating the no.of hosts, use the below formulae -
> >
> > > **2^(32- what mask you have been provided) –2**
> > >
> > > > 2^(32-18)-2 -> 2^(14)-2 –> 16384-2 –> 16382 hosts

HERE 255.255.0.0 is being shared as IP Subnet mask and private subnet can have 

![1603120034009](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603120034009.png)



#### VPC Basics

Provides isolated network domain and each VPC are completely separated one.

- Every account has a default VPC in every region when created
- VPC are region based and they are completely separated unless we configure communication between them
- There can be only one default VPC and can have multiple non-default VPC
- VPC are highly available by design and so they occupy all AZ in the region
- VPC contain subnets. Resources are attached with subnet and not wit VPC.

![1600697942519](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600697942519.png)

![1600688845423](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600688845423.png)![1600688870731](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600688870731.png)

![1600701923468](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600701923468.png)

##### Lesson Links

[IP Subnetting the Easy Way](https://www.theprohack.com/2012/01/ip-subnetting-easy-way.html)

##### Lesson Files

[vpc_us_east_1_cfn.json](https://github.com/linuxacademy/aws-csa-pro-2019/blob/master/02_networking/1_vpcbasics/vpc_us_east_1_cfn.json)
[vpc_anotherregion_cfn.json](https://github.com/linuxacademy/aws-csa-pro-2019/blob/master/02_networking/1_vpcbasics/vpc_anotherregion_cfn.json)

#### AWS Resource Access Manager (RAM)

AWS Resource Access Manager (RAM), a service that allows the sharing of AWS resources between accounts. This lesson focuses on using it to share VPC subnets between accounts in an organization.

**Following points are critical**

- Enable sharing to get billing discount for aws org and resource sharing across aws account across organisation
- AZ Name and AZ Id mapping. what i see AZ name in my aws account, you may see different one.as shared in here. Remember AZ name is not constant across aws account but AZ id is constant across aws account.![1600706873724](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600706873724.png)
- Owner and Participant. If I am sharing my VPN from an aws account to you into another aws account then i am the owner and you are participant.

##### Lessons Links

- Enabling RAM - <https://console.aws.amazon.com/ram/home#Setting>

- Working with AZ IDs - <https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html>

- What Is AWS RAM? - <https://docs.aws.amazon.com/ram/latest/userguide/what-is.html>

- VPC Sharing - <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html>

#### VPC Routing

 VPC router, and explains how they are influenced by route tables, route priority, and route propagation.

![1600707935668](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600707935668.png)

- Every VPC has VPC Router

#### Network Access Control Lists (NACLs)

- Provides stateless security filtering for subnet. It is stateless because it cant distinguish between incoming and outgoing traffic of a session and ephemeral port rules are required to allow response traffic.

- A subnet can have only one associated NACL. We can have either default NACL or custom NACL associated with subnet.

- NACL is called firewall of subnet

- Has two rules

  - Inbound
  - Outbound

- NACL rules are being evaluated as per rule number.![1600783506162](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600783506162.png)

- Can explicitly DENY traffic which is not possible in security group

- NACL only takes effected when traffic enters or exit the subnet. It does not get triggered when traffic within two resources in same subnet

- NACL deals with IP, IP Range and CIDR block and they cant refer logical resources or aws services, other Network resources, security group

  

### Security Groups (SGs)

This lesson steps through the architecture of VPC Security Groups (SG), focusing on the benefits, and compares their features to Network Access Control lists (NACLs).

- Security group applies when traffic goes out and in from Network interfaces. EC2 can have multiple network interfaces. Each network interfaces can have its security group.
- Every network interfaces has a default security group. Security group has Inbound and Outbound rule section.
- Have implicitly deny and we cant add explictly deny from any IP.
- SG Processing has no order .
- ![1600787399401](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600787399401.png)
- Ability to reference other logical aws security group (other security group)



![1600784280687](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600784280687.png)

### Public vs. Private Subnets, Internet Gateways, and IP Addressing: Part 1

- Internet Gateway
  - It is a type of NAT and it uses static IP to translate. It is a static NAT. It translates from variable private address to public static IP.
  - BASTIAN host can talk to IGW and IGW then translates the BAASTIAN host IP address to external IP address and send communication to external one.
- NAT Gateway
  - Provide network translation. Translate from one IP to another one. SO it maintains record for both side and does the translation.
  - If we want any private instance (EC2) talk to public internet then we dont allow such private instance talk to IGW. Thats why we have NAT gateway. So multiple EC2 instances can speak to NAT gateway and then NAT Gateway translates all these variable private address to fixed external address and send communication to public internet. 
  - **Need to have elastic public IP address. Elastic IP is a static one and does not change.**
  - **They are resilient inside availability zone but is not highly available. So if that AZ gone down then not necessarily resources from other region will be able to communicate with NAT gateway. So in order to achieve true HA, we have NAT gateway in every AZ.**
  - 
- Bastian Host
  - **Has dynamic public IP address. So start and stop will get new address.**
- what is Public and Private subnet? AWS does not make distinction between them. A   private sub nets A really just sub nets with a slightly different configuration. It's really all about that configuration. A private subnet is a sub net in its default configuration. It has an AP version for side range optionally an Ip version six range associated with it. But it can't communicate with the public Internet and it can't communicate with n AWS Public zone service is so service is such as s3,dynamodb, sqs, es and S and cloudwatch.
- A subnet by default is private. So how we make that public?
  - **VPC needs to have internet gateway attached.**
  - **Subnet needs to have route table associated with it that should contain a default route pointing at Internet gateway**. Route table gets created per VPC. So Route table needs to be associated with VPC. After pointing to IGW then go into route table association tab and associate subnet with that.
- aa

![1600787914985](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600787914985.png)



##### Lesson Links

[Connect to Amazon EC2 Using Putty Private Key on Windows](https://linuxacademy.com/blog/linux/connect-to-amazon-ec2-using-putty-private-key-on-windows/)

### Egress-Only Gateways

- Every IPV6 address in aws by default publicly routable
- 

![1600790756507](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600790756507.png)

#### Lesson Links

[IPv6 Subnet Cheat Sheet and IPv6 Cheat Sheet Reference](https://www.crucial.com.au/blog/2011/04/15/ipv6-subnet-cheat-sheet-and-ipv6-cheat-sheet-reference/)
[IPv6 Subnetting - Overview and Case Study](https://community.cisco.com/t5/networking-documents/ipv6-subnetting-overview-and-case-study/ta-p/3125702)

### VPC Flow Logs

- Allows to have traffic metadata
- Flow log allows to log "Accept","Reject" or "All" traffic logged
- Allows to push the logs to CW or S3 bucket
- IAM role needs to be associated

![1600791398068](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600791398068.png)

# AWS Compute -Elastic Compute Cloud (EC2)

## Fundamentals

![1606373623667](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606373623667.png)

![1606374691138](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606374691138.png)

![1606374900470](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606374900470.png)

![1600086744005](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600086744005.png)

EC2, an Infrastructure-as-a-Service (IaaS) product. EC2 is a core AWS product that provides virtual machines known as instances.

EC2 is ideal for:

- Monolithic applications
- Consistent, long-running compute scenarios
- Applications that require full OS/runtime installations
- Services, endpoints, and/or applications that require high availability

- It is similar to OS which does work. It is a virtual computer and a software based. Provides scalable computing capacity.

- Computing services

  - EC2

    - Instance type is similar to CPU; processing power

    - AMI is software package which is required to launch instance. Is a template for software, OS and other softwires required to run.

    - EBS(Elastic Block Storage) is similar to our C drive or D drive in windows. we can have a EBS Volume for application and another separate one for application data.

    - Network adapter is IP address into windows PC. Allows internet access. EC2 address gets network adapter; hence IP.

    - Security group; it is a EC2 instance level security and same to PC firewall 

    - RAM

    - Purchasing options

      - On-demand 

        - Purchase any time, provision any time and terminate any time. Most expensive but flexible. billed per hour.

      - Reserved

        - Purchased for 1 of 3 year at significant discount. Does not matter if instance is running or not.

      - Spot Instance

        - Purchased based on bidding. You bid with a price and give us to get unused instances available. They are charged by min. Instance provisioned the moment price is lower than bid price and charging starts. Instance will get terminated when price is higher than the bid price.

        

  - Lambda

  **AMI**

  ![k](https://i.ytimg.com/vi/HBf_DvrVW2c/maxresdefault.jpg)

  **EC2 Instance Type**

![im](https://www.helenanderson.co.nz/wp-content/uploads/2019/04/ec2.png)

![1590759999884](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590759999884.png)

![1590760298638](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590760298638.png)

![1590760392508](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590760392508.png)

**Multiple instances and their security rules** . A Security Group can be used to explicitly allow traffic on the instance level. Since you can’t explicitly deny traffic in Security Group, it will **implicitly** deny traffic to an instance when an allow rule is not present.

![1590760540669](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590760540669.png)

## EC2 details

We need to create Key pair before creating instance. Public key is with AWS and private part is downloaded and required to authenticate with EC2 instance.

![1604898618294](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604898618294.png)

EC2 runs within a networking instance which is called VPC. So it needs to be setup first. Default VPC is a prebuilt VPC which is created by AWS with all default services. very EC2 instance stays within its own VPC and subnet and availability zone.

- Instance store volume - attached with instance and if host changes due to restart then it is created as new

- Elastic Balance Structure volume - persistent and stables

![1592663394878](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592663394878.png)

## EC2 Architecture: Part 2

- ECS integrate with cloud watch
- you can install  an agent within EC2 instance and attach with CW to monitor memory and CPU consumption etc
- ECS default monitoring time limit is 5 min 

EC2 instance key pair. Two part of key, it has public and private. Private part is downloadable once. Every EC2 instance runs within a VPC.



![1600008696606](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600008696606.png)

![1600009095902](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600009095902.png)

**Instance Store Volume:**

- Non persistent
- Store high performance data
- Once EC instance started then we loose Instance store volume data



### Further links

- [EC2 Status Checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)
- [Instance States & Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- [Instance Hibernate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)

EC2 instance is attached with Cloud watch and has un-built

- CPU Utilistation
- Disk Read
- Disc Read Operation
- Disk Writes
- Disc Write Operations
- Network In
- Network Out
- Network Packets In(count)
- Network Packets Out (Count)

## Instance Types and Sizes

Being able to select the correct family, type, and size of each instance is an essential skill for a solutions architect.

![1606378137662](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606378137662.png)

### Lesson Links

- [Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Nitro Hypervisor](https://www.youtube.com/watch?v=e8DVmwj3OEs)

## EC2 Instance configuration details



## EC2 Storage Architecture

will discuss instance store volumes and Elastic Block Store (EBS), the network-based block storage provider used by EC2. EBS provides a range of volume types with varying performance and use cases. Understanding how to use EBS volumes versus instance store volumes is essential for the exam and for real-world usage.

![1600013196024](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600013196024.png)

### Lesson Links

- [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)

## EBS Snapshots

EBS volumes occupy a single Availability Zone (AZ), and while they do replicate within this AZ, this replication isn’t shared to other AZs. This makes EBS volumes vulnerable to AZ failure. E**BS snapshots not only provide data backup capabilities but also enable you to move your data to other AZs and regions**.

![1600018537793](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600018537793.png)

### Lesson Links

- [How Incremental Snapshots Work](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

## Security Groups

Security groups are an essential part of the EC2 and VPC security toolset. They operate like a virtual firewall, controlling traffic originating from or destined for a network interface (or an instance).

In this lesson, we will explore the capabilities of security groups, discuss their one key limitation, and learn what "stateful" means.

![1600062264435](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600062264435.png)



### Lesson Links

[User Data](https://github.com/linuxacademy/content-aws-csa2019/blob/master/lesson_files/03_compute/Topic1_Fundamentals/05_SecurityGroups/userdata1.txt)

## Instance Metadata

Instance metadata can be used to access information about an instance from the instance. It allows applications running within EC2 to have visibility into their environment. In this lesson, we will discuss the key architecture considerations for using metadata.

![1600080424324](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600080424324.png)

### Lesson Links

- [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

## AMI

AMIs (Amazon Machine Images) are used to launch instances in AWS. AWS supplies AMIs that cover most standard operating systems (Linux and Windows), and AMIs containing commercial software are available on the AWS Marketplace. Additionally, custom AMIs can be created by AWS customers and used directly or shared with other accounts.

![1600088993664](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600088993664.png)

## Bootstrap

Bootstrapping is the process of providing "build" directives to an EC2 instance. Bootstrapping in EC2 uses user data and can take in shell script-style commands or cloud-init directives.

This lesson walks through both at a high level.

![1600092410735](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600092410735.png)

#### Lesson Links

- [cloud-init Documentation](https://cloudinit.readthedocs.io/en/latest/)

## Instance ENI, IP, and DNS

EC2 instances can be configured with or without public IPv4/6 IP addressing. Based on this configuration, the instance has a selection of public and private IPs and DNS names. 

![1600095062619](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600095062619.png)

## Instance Roles

Instance roles are IAM roles that can be associated with EC2 instances using instance profiles. 

![1600096677006](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600096677006.png)

## EC2 Concepts LA Professional

![1601034281515](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601034281515.png)

### Creating and Using AMIs

![1601367951966](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601367951966.png)

### Virtualization and EC2 Instance Type: Deep Dive

![1601372931652](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601372931652.png)

![1601373244729](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601373244729.png)

### ECS 2 Storage and snapshot

This lesson evaluates instance store volumes, EBS volumes, and EBS snapshots. It shows their features, patterns, anti patterns, and differences.

![1601448806701](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601448806701.png)

**EBS Storage**

![1601448936934](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601448936934.png)

**EBS can be attached to only one EBS instance and cant be shared across multiple EC2 instance. EBS can be decoupled from one EC2 instance and attached to another EC2 instance but EBS cant be made shared resource. S3 offers much higher durability, multiple AZ than EBS. If AZ failed then EBS fails and we cant move an EBS from one AZ to another AZ. We can use snapshot to create one more EBS in different AZ.**

![1601449069288](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601449069288.png)

**EBS Snapshots**

![1601450555353](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601450555353.png)



#### Lesson Links

[Instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
[EC2 and EBS Performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html) [EBS Volume Types and Performance Information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)

### EC2 Instance Profiles and Roles

This lesson looks at Instance profiles, the method of attaching IAM roles to EC2 instance. Instance profile is automatically created when we have an associated IAM role with EC2 instance during EC2 creation from GUI. So it is **Instance profile** which links IAM role and application running in EC2 instance. Only a single instance profile can be attached EC2 instance can be attached.

![1601457136244](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601457136244.png)

### HPC and Placement Groups

This lesson looks at the architecture of placement groups, focusing on the different types of placement groups, and the situations when you would use each.

![1601457913256](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601457913256.png)

#### Lesson Links

[Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)  

### Custom Logging to CloudWatch

This lesson looks at the additional logging metrics and capabilities that the CWAgent adds to cloudwatch monitoring on EC2.

![1601458507988](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601458507988.png)



#### Lesson Links

[Installing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance-fleet.html)
[Configuring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)
[JSON Configuration For Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html)

### EC2 Pricing/Purchasing oPTION

![1603086554939](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603086554939.png)

### VPC Examples

![1603086778815](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603086778815.png)

![1603086810842](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603086810842.png)

### Reboot and Stop and restart of EC2

![1603089969343](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089969343.png)



# Exam Lesson Links

### Exam

- [AWS Solutions Architect Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [Sample Questions](https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Solutions_Architect_Associate_Sample_Questions.pdf)
- [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS_Certified_Solutions_Architect_Associate-Exam_Guide_EN_1.8.pdf)

### Whitepapers

- [Encrypting Data at Rest](http://d1.awsstatic.com/whitepapers/AWS_Securing_Data_at_Rest_with_Encryption.pdf)
- [Web Application Hosting in the AWS Cloud](https://d0.awsstatic.com/whitepapers/aws-web-hosting-best-practices.pdf?refid=em_)
- [Migrating AWS Resources to a New AWS Region](http://d0.awsstatic.com/whitepapers/aws-migrate-resources-to-new-region.pdf?refid=70138000001adyu)
- [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/)
- [Elastic Load Balancing FAQs](https://aws.amazon.com/elasticloadbalancing/faqs/)
- [AWS Elastic Beanstalk FAQs](https://aws.amazon.com/elasticbeanstalk/faqs/)

### Identity YouTube Video

[IAM](https://www.youtube.com/watch?v=YQsK4MtsELU)

### Compute YouTube Videos

[ELB](https://www.youtube.com/watch?v=VIgAT7vjol8) [Lambda](https://www.youtube.com/watch?v=QdzV04T_kec)
[EKS](https://www.youtube.com/watch?v=EDaGpxZ6Qi0)
[VMware](https://www.youtube.com/watch?v=RStQrGmHqy0)

### Storage YouTube Videos

[S3 and Glacier](https://www.youtube.com/watch?v=rHeTn9pHNKo) [S3, EFS, and EBS](https://www.youtube.com/watch?v=gidUa4lJd9Y)

### Database YouTube Videos

[RDS](https://www.youtube.com/watch?v=HuvUD7-RyoU)
[DynamoDB Video 1](https://www.youtube.com/watch?v=HaEPXoXVf2k)
[DynamoDB Video 1](https://www.youtube.com/watch?v=eTbBdXJq8ss) [Aurora](https://www.youtube.com/watch?v=2WG01wJIGSQ)

### Networking YouTube Videos

[VPC](https://www.youtube.com/watch?v=fnxXNZdf6ew)
[Transit Gateway: Video 1](https://www.youtube.com/watch?v=yQGxPEGt_-w)
[Transit Gateway: Video 2](https://www.youtube.com/watch?v=ar6sLmJ45xs)
[VPN](https://www.youtube.com/watch?v=qmKkbuS9gRs)
[DNS](https://www.youtube.com/watch?v=D1n5kDTWidQ)

### Analytics, Streaming, IoT YouTube Video

[Redshift](https://www.youtube.com/watch?v=TJDtQom7SAA)

# AWS Instance Scheduler

![1605069420942](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069420942.png)

# EMR and Hadoop

![1605069486489](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069486489.png)



# AWS Storage Services

## S3

Amazon S3 (Simple Storage Service) is a **online** and **bulk upload storage** service that allows the upload of virtually any type of file. Amazon Simple Storage Service (S3) classifies objects that are uploaded into storage classes. Each storage class has a durability and availability rating, as well as different requirements for minimum billable storage duration.

![1605069301416](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069301416.png)

![1590764127507](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590764127507.png)

### Sizing

![1605069357941](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069357941.png)

### Leverage

![1605069564802](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069564802.png)



## EBS and EBS Lifecycle

- EBS has to be provisioned not like S3. 
- EBS is block storage and costly w.r.t S3

![1603089277857](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089277857.png)

![1603089165675](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089165675.png)![1603089399843](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089399843.png)



![im](https://jayendrapatil.com/wp-content/uploads/2020/02/S3-Storage-Classes-v2.png)

- It is block based storage service
- Root level folders are bucket and underneath buckets are called folder
- Files stored in buckets are referred as objects

![1600017089681](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600017089681.png)

![1603089454035](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089454035.png)

![1603089495558](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089495558.png)

### EBS Use case

![1603089611764](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089611764.png)

## Difference between EBS and S3

![1603089698474](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089698474.png)

## Instance storage

Only during lifecycle of instance.

![1603089833405](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089833405.png)

## Difference between EBS and Instance storage

![1603089902987](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603089902987.png)





# AWS Storage Gateway

AWS storage services may be integrated into a customer's on-premises environment using Storage Gateway. The Storage Gateway service uses a virtual machine or hardware device to facilitate the transfer of data to AWS. 

![im](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2019/11/23/Use-case-1-More-on-premises-backups-to-the-cloud.png)

![1590764458011](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590764458011.png)

# Elasticity and Scaling EC2

## Auto Scaling

**AWS Auto Scaling** is a service that automatically monitors and adjusts compute resources to maintain performance for applications hosted in the **Amazon Web Services** (**AWS**) public cloud. As demand spikes, the **AWS Auto Scaling** service can automatically scale those resources, and, as demand drops, scale them back down.

- we create collections of EC2 instances, called Auto scaling groups. we can specify min number of instances into each Auto Scaling groups.
- We can define scaling policies that can launch or terminate instances as demand increases or come down.

![im](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2017/04/18/CDBG-topology.png)

### ![1590767656770](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590767656770.png)

# Content Delivery and Domain Name System (DNS)

## DNS

Route 53 provides domain name registration and management services to AWS. ![1590768532105](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590768532105.png)

![im](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/how-route-53-routes-traffic.png)

## Cloud Fronts

- CloudFront is the AWS content delivery network (CDN). 

- CloudFront caches content at edge locations around the globe to provide fast access to it for users located all over the world. 
- Provides faster access and additional security as contents are duplicated near accessed location. So any traffic will be always diverted into location of cloudfront and hence ciber attack will also be diverted there.

![1600365868938](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600365868938.png)

**See below how cloud front is used for accessing content.**

- Customer requests example.com 
- web browser route the traffic to internet
- Internet route the traffic to Route 53 as it is the owner of domain
- Route 53 has a dummy entry for cloud front for the same domain and it will route the traffic to cloud front. 
- Cloudfront will share the content. if the content is not available in cloud front then it will be downloaded through cloud front origin in nearest cloud front.
- Data stays in edge location till expiry period is not over.

![1590819286275](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590819286275.png)

Here is the FAQ on cloud front and Route 53.

![1590819637265](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590819637265.png)

# Monitoring, Logging, and Notifications

## Monitoring and Logging

### Cloudwatch

CloudWatch is the AWS monitoring tool, and it can be integrated with other AWS services to provide detailed monitoring, alarms, and notifications.

![1597822467427](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597822467427.png)

CloudWatch can have alarm created and then it is integrated with AWS Simple Notification Service (SNS) to trigger notification when alarm is raised.

- Monitor metrices for all aws resources

- create and monitor custom metrices

- create custom dashboard for east viewing

- Monitor and store logs

- Set alarm and events ( and trigger action based on them; trigger can be restart EC2 Instance, terminate EC2 instance etc)
  - Billing Alarm
  - EC2 Instance CPU utilization alarm
  - Lambda error alarm
  - No of objects in S3 Buckets
  - Size of Objects in S3 Buckets

  ![1590820588275](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590820588275.png)

  

  ![im](https://cloudonaut.io/images/2019/09/screenshot-cloudwatch-dashboard.png)

  

#### Cloud Watch Events

![1601658703394](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601658703394.png)



#### Metrics and Alarms

**We can create metric and then associate an alarm with that. Metric allows to do string/pattern search within cloud watch log group.**

![1597822900370](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597822900370.png)

#### Logs

CloudWatch Logs forms part of the wider CloudWatch product and offers log ingestion, searching, management, and metric filter functionality. CloudWatch Logs is used by many AWS services for log storage and can be extended for custom applications and on-premises servers. This lesson walks through the product's architecture with a quick demo.

![1597844541391](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597844541391.png)

**We can export log groups or stream also as shared below..**

![1597847908012](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597847908012.png)



#### Lesson Links

- [AWS Services That Publish CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)
- [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

### CloudTrail

Many times for governance and compliance reasons, organizations are required to maintain a record of administrative actions taken within the environment. AWS CloudTrail may be used to monitor and log administrative actions taken by IAM users.

![1597848207159](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597848207159.png)

**Trail can be applied to a specific region or all region. By default cloudtrail stores logging into eventhistory for 90 days but if we want to store the logging history into some other place or do something then we need to define trail. trail allows event history to be pushed into S3 or lambda.**

![1597848611342](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597848611342.png)

CloudTrail is a critical product within AWS, as it provides full API/account activity logging across all regions in an account and (optionally) all accounts within an AWS Organization.

**Cloud trail is not realtime one and trail delivers periodically.**

**Any API Call within AWS account are logged into CloudTrail.**

CloudTrail stores the event details for 90 days into event history as shared below.

![1597848402137](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597848402137.png)

### VPC Flow Logs

VPC Flow Logs can be enabled on a VPC, subnet, or ENI level and monitor traffic metadata for any included interfaces. 

You can attach VPC Flow logs monitoring:

- With VPC (If we apply VPC Flow log at this level then it gets applied automatically to following two level)
- With VPC  specific Subnet
- Directly with networking interface

Flow logs monitor:

- Source and destination IP addresses

- Source and destination ports

- Protocol

- Bytes

- Start and end

- ALLOW or REJECT status

  

![1597853557946](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597853557946.png)

### Difference between Cloud watch and CloudTrail

**CloudWatch** *focuses on the activity of AWS services and resources, reporting on their health and performance.* use Amazon CloudWatch to collect and track metrics, collect and monitor log files, set alarms, and automatically react to changes in your AWS resources.

**CloudTrail** *is a log of all actions that have taken place inside your AWS environment.*AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With 
CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis,resource change tracking, and troubleshooting.

**CloudWatch:** *“What is happening on AWS?” and logging all the events for a particular service or application.*

**CloudTrail:** *“Who did what on AWS?” and the API calls to the service or resource.*

![im](https://mk0digitalcloud3kwjy.kinstacdn.com/wp-content/uploads/2019/03/CloudWatch-vs-CloudTrail-1024x481.jpg)

Cloud Trail Observations

- Matt shutdown the X EC2 instance
- James modified pku S3 bucket permission

## Notification Services

 Amazon SNS provides notification services that can be triggered by other AWS services. As an example, CloudWatch alarms may trigger SNS notifications to be sent. 

- Triggers automated notifications

  - SMS
  - Email
  - HTTP Endpoints

  SNS Basics:

  - Topics
    - Label and group different end points that you send message to
  - Subscriptions
    - Endpoint that a topic sends message to
  - Publishers
    - Agent who is triggering the SNS

  So once we publish a message for a topic, anyone who is subscribed to this topics will be be notified.

  **Following one shows how we can have different SNS topic and have their corresponding SQSQ and consumer.'**

![im](https://miro.medium.com/max/1400/1*DRrTtdyah9NHwR0VCm6MWA.png)

**Following ones show how a EC2 instance crash can be detected to send notification.**

![1590826046992](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590826046992.png)

# Database Services

## Relational Database Service (RDS) and DynamoDB

- RDS for **SQL** database (Relational DB)
- DynamoDB is for **No-SQL** database (Non Relational DB)

**RDS is SQL based service and has following SQL DB options to select**

- AWS Aura
- MySQL
- MariaDB
- PostgreSQL
- Oracle
- MS SQL Server

**DynamoDB is a fast and flexible NO-SQL DB service and unlike RDS , DynamoDB does not offer multiple software options**. It supports both document and key-value(json like) store model. DynamoDB is similar to

- MongoDB
- Oracle NoSQL
- Cassandra DB

![im](https://mk0digitalcloud3kwjy.kinstacdn.com/wp-content/uploads/2019/03/Amazon-Database-Use-Cases-1024x873.jpg)

![1590827686815](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590827686815.png)

## ElastiCache and Redshift

In addition to RDS and DynamoDB, AWS also offers two database services for (1) data caching and (2) data warehousing.

The operational database in this example is Amazon DocumentDB—a fast, reliable, and fully managed database service that makes it easy to set up, operate, and scale MongoDB-compatible databases in the cloud. **For the caching layer, use Amazon ElastiCache, which makes it easy to set up, manage, and scale distributed in-memory cache environments in the AWS**. **ElastiCache provides a high performance, resizable, and cost-effective in-memory cache, while removing complexity associated with deploying and managing a distributed cache environment. ElastiCache is compatible with both the Redis and Memcached engines.**

![im](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2019/10/01/Caching-for-performance-A.jpg)

**AWS Redshift is datawarehouse database service designed to handle pb of data.

![i](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2018/02/09/Cerberus3.png)

![1590835708128](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590835708128.png)

# Serverless Compute -Lambda

AWS offers serverless compute with a service called Lambda. What is Lambda.![1590836027517](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590836027517.png)

![1602673762919](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602673762919.png)



## Serverless and Event-Driven Architectures

Serverless and event-driven architecture are essential to grasp for production usage of AWS and the Solutions Architecture Associate exam. In this lesson, we look at what event-driven architecture is and how it differs from a polling-style architecture. Moving on, we look at the two components of serverless: Back-end as a Service (BaaS) and Function as a Service (FaaS).

![1593355797639](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593355797639.png)

**Above picture shows a traditional system where we have constant polling.  Here, most of the time these sensors will be reporting same temperature and hence there will not be event triggered and hence it is not useful one. This is why the following picture shows event driven architecture.**

![1593355989549](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593355989549.png)

**Here is how serverless architecture will work.** Here function works as service and it is fast. It fast compare to EC2 service and container. This is event driven architecture and we pay only for time when function is running. So it is more on-demand compute.

![1593356186590](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593356186590.png)



## Lambda Essentials: Part 1

Lambda is an essential service in AWS. It's a Function-as-a-Service product that is a key part of event-driven and serverless architectures. This lesson walks through Lambda architecture in detail, both from a theoretical and practical perspective.

The lesson looks at:

- Functions
- Runtimes
- Runtime environments
- Code upload
- Execution roles
- Logging
- Resources
- Event structure
- Triggers

![1593366031891](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593366031891.png)

#### Lesson Files

[GitHub Repository Files](https://github.com/linuxacademy/content-aws-csa2019/tree/master/lesson_files/03_compute/Topic4_Serverless/lambda)

## Lambda Essentials: Part 2

A sample lambda which gets triggered when a file is placed into source S3 and then the lambda moves the file into destination S3.

![1593367024217](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593367024217.png)

**Command to package the lambda function in order to upload in aws**

```

mkdir /tmp/lambdafunction
cp lambda_handler.py /tmp/lambdafunction
cd /tmp/lambdafunction
wget https://files.pythonhosted.org/packages/ae/2a/0a0ab2833e5270664fb5fae590717f867ac6319b124160c09f1d3291de28/Pillow-5.4.1-cp37-cp37m-manylinux1_x86_64.whl
unzip Pillow-5.4.1-cp37-cp37m-manylinux1_x86_64.whl
rm -rf Pillow-5.4.1.dist-info
zip -r9 lambda.zip PIL lambda_handler.py
```

## Serverless Video Upload architecture

![1595872736134](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595872736134.png)

## Lambda Indepth Architecture - Part 1

This lesson goes into depth on the architecture of AWS Lambda - looking at how it can be used as part of a serverless architecture.

![1595874138088](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595874138088.png)

### Lambda worker model

A sanbox for each of lambda run time. So it can be warm start where existing sanbox is used or cold start where new sanbox is being created during runtime start.



![1595874364928](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595874364928.png)

## Lesson Files

[Lambda](https://github.com/linuxacademy/aws-csa-pro-2019/tree/master/04_compute/lambda)

### Lesson Links

[AWS Lambda Under the Hood](https://www.youtube.com/watch?v=QdzV04T_kec)

## Lambda Layers

This lesson looks at the architecture and architectural implication of Lambda layers.

![1595876283536](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595876283536.png)



### Lesson Links

[Custom runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html)
[Creating a custom runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-walkthrough.html)
[AWS Lambda cpp](https://github.com/awslabs/aws-lambda-cpp)
[Including library dependencies in a layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path)

## EC2 and Lambda comparism

**Solution using EC2**

![1590836140038](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590836140038.png)

**Same above solution is done with Lambda.**

![1590836217298](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590836217298.png)

![1590841222977](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590841222977.png)

## Exam tips

![1597326397069](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597326397069.png)

## Version Control with Lambda

Allows 

- to publish one or more version of lambda function
- to work with different version in development workflow in prod, beta and prod
- Each version has unique ARN and it is immutable (cant be changed)

Qualified and Unqualified ARN

- Qualified
  - Function ARN with version suffix
- Unqualified
  - Function ARN without version suffix

![1597336743012](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597336743012.png)

**Alias can help us to distribute the load across two version and so we can do A/B testing.**

![1597337160128](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597337160128.png)

![1597337900658](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597337900658.png)

## Lambda Invocation Types

![1601656966003](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601656966003.png)

### Async Invocation

![1601657599334](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601657599334.png)

### SYNC Invocation

Need return result and order is must.

![1601657646004](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601657646004.png)

### Push Event Model

![1601657717113](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601657717113.png)

### Pull Event Model

![1601657799959](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601657799959.png)

## Lambda Concurrency

### Stream based

![1601658020045](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601658020045.png)

### Non Stream based

![1601658110505](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601658110505.png)

![1601658365308](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601658365308.png)



## Lambda Logging

![1601654506201](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601654506201.png)

![1601655335954](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601655335954.png)

![1601656793011](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601656793011.png)

### CloudWatch Events

CloudWatch Events is a very powerful feature within AWS, and Lambda can utilize these events to invoke our functions. 

#### Event pattern rule

Here we hare created cloudwatch rule which will look for "EC2 Spot Instance Interruption Warning" and call our lambda function defined in function field of the CW rule. This lambda function will then trigger the EBS Snapshot. The EBS snapshot will be then store in S3 bucket.

![1601659151052](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601659151052.png)

### Scheduled Expression Rule for Cloud watch rule

![1601659440069](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601659440069.png)

## Lambda Programming

![1602674197886](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602674197886.png)



# Serverless Compute - API Gateway 

API Gateway is a massively important service in AWS, both for real-world usage and for the exam. It allows the creation, management, and optimization of highly scalable API endpoints. API Gateway is a key component of serverless architectures in AWS. In this two-part lesson, we explore the architecture using an example `Calculator` demo to illustrate the key service components. API Gateway can integrate with other AWS services, including Lambda, to provide API logic.

![1597326608952](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597326608952.png)

![1600447939622](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600447939622.png)

API Gateway acts as a "front door" for applications to access data, business logic, or functionality from your backend services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, any web application, or real-time communication applications.

![im](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/Product-Page-Diagram_Amazon-API-Gateway-How-Works.png)

## Features of API Gateway

Amazon API Gateway offers features such as the following:

- Support for stateful ([WebSocket](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)) and stateless ([HTTP](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) and [REST](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)) APIs.
- Powerful, flexible [authentication](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) mechanisms, such as AWS Identity and Access Management policies, Lambda authorizer functions, and Amazon Cognito user pools.
- [Developer portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-developer-portal.html) for publishing your APIs.
- [Canary release deployments](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html) for safely rolling out changes.
- [CloudTrail](https://docs.aws.amazon.com/apigateway/latest/developerguide/cloudtrail.html) logging and monitoring of API usage and API changes.
- CloudWatch access logging and execution logging, including the ability to set alarms. For more information, see [Monitoring REST API execution with Amazon CloudWatch metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html) and [Monitoring WebSocket API execution with CloudWatch metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html).
- Ability to use AWS CloudFormation templates to enable API creation. For more information, see [Amazon API Gateway Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-reference-apigateway.html) and [Amazon API Gateway V2 Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-reference-apigatewayv2.html).
- Support for [custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).
- Integration with [AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) for protecting your APIs against common web exploits.
- Integration with [AWS X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html) for understanding and triaging performance latencies.

### API Gateway Canary Support

![1600448273203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448273203.png)

![1600448543616](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448543616.png)

![1600448581949](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448581949.png)

![1600448604275](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448604275.png)



## API Gateway Part 1

![1593370365335](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593370365335.png)

![1593370535238](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593370535238.png)

![1600448185505](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448185505.png)

![1600448214055](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600448214055.png)



## Lesson Files

- [GitHub Repo Files](https://github.com/linuxacademy/content-aws-csa2019/tree/master/lesson_files/03_compute/Topic4_Serverless/apigateway)

## Lesson Links

- [AWS Documentation - Calculator API](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-lambda.html)
- [More on API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

## API Gateway Part 2

![1597326954961](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597326954961.png)

Steps for creating API through API gateway

- API Gateway

- Resource
  - Resource Nmae
  - Path

- Method. It should be created under  selected method.
  - Get
  - Integration Type
    - Lambda
    - HTTP
    - Mock
    - aws service
    - vpc link
- Deploy API

![1593880685134](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593880685134.png)

## API Gateway advanced

This lesson looks at how API Gateway can be used in AWS architectures for a serverless API implementation.

![1595876898095](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595876898095.png)

### Lesson Links

[Operating Your Serverless API](https://www.youtube.com/watch?v=tIfqpM3o55s)
[API gateway caching](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)
[HTTP integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-http-integrations.html)
[Proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html)

## API Import

![1597340231821](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597340231821.png)

## SOAP Web Service Passthrough

![1597340455377](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597340455377.png)

## API Caching

![1597327022515](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597327022515.png)

![1597327264088](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597327264088.png)

![1597327283087](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597327283087.png)

# Step Functions

Step Functions is a product that can act as the glue between microservices in AWS. It allows for the orchestration of Lambda functions, human interaction, and other AWS resources in a visual workflow way. It offers features similar to Simple Workflow Service (SWF) but does so without any long-running compute instances such as EC2.

![1593964551215](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593964551215.png)

Here is sample state diagram that is being shown for step function.

![1593965610106](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593965610106.png)

## Workflow Orchestration Step Functions - SA

This lesson evaluates and compares Simple Workflow Service and Step Functions — products designed to implement workflow orchestration within AWS. Simple Workflow Service has been depreciated, so this lesson evaluates how Step Functions delivers the same functionality in a serverless way.

![1597339663421](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597339663421.png)



![1597258087332](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597258087332.png)

**step function flow**

![1597258253928](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597258253928.png)



## Lesson Files

[GitHub Repo Lesson Files](https://github.com/linuxacademy/content-aws-csa2019/tree/master/lesson_files/03_compute/Topic4_Serverless/StepFunctions)

# Security and Compliance Services

Unlike a traditional on-premises data center, hosting your data/application on the AWS cloud creates a situation where security and compliance responsibilities must be shared. 

![im](https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)

**Shared Controls** – Controls which apply to both the  infrastructure layer and customer layers, but in completely separate  contexts or perspectives. In a shared control, AWS provides the  requirements for the infrastructure and the customer must provide their  own control implementation within their use of AWS services. Examples  include:

- Patch Management – AWS is responsible for patching and  fixing flaws within the infrastructure, but customers are responsible  for patching their guest OS and applications.
- Configuration Management – AWS maintains the configuration  of its infrastructure devices, but a customer is responsible for  configuring their own guest operating systems, databases, and  applications.
- Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.

**Customer Specific** – Controls which are solely the  responsibility of the customer based on the application they are  deploying within AWS services. Examples include:

- Service and Communications Protection or Zone Security which  may require a customer to route or zone data within specific security  environments.

## Security and Compliance on AWS

Many organizations have requirements for validating that the environment is not vulnerable to attackers. Penetration testing is used for this validation. 

![1590841594120](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590841594120.png)

**See here how cloud front is saving main instance from hackers.** Users are only touching CloudFront and not actually allowing user to touch instance directly.

![1590841694521](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590841694521.png)

## AWS Key Management Service

If you have data you need to encrypt on AWS, the AWS Key Management Service (KMS) is responsible for creating and managing encryption keys. KMS also integrates with other AWS services. 

![im](https://lirp-cdn.multiscreensite.com/b15b3612/dms3rep/multi/opt/download+%281%29-960w.jpeg)

![1590842002011](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590842002011.png)

## AWS Key Management Service (KMS) - LA Professional

This lesson looks at AWS Key Management Service (KMS), a part of IAM which provides key management services in addition to associated generation, encryption, and decryption operations.

**KMS is integrated throughout AWS with a variety of different services and is an important service to understand to effectively secure different components of your applications**. 

**Note**: KMS is now a separate AWS Service and NOT in the IAM portion of the AWS Console.

![1603726960644](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603726960644.png)

- Decryption
- re-encryption
- Key generation
- KMS Provides role separation. So S3 dont store any sensitive info about Keys and thus we can allow data and S3 bucket full right to someone but we can deny access to that admin for KMS. So now key maintenance role is being separated and delegated to KMS.
- Customer managed Key (CMK) never leaves KMS and only way we communicate is through API. Key always remains in KMS HW.
- KMS is region based service.
- Key generation command takes name and region name as input. So in response as below, we get Key Id and Key ARN. These two are used to communicate with KMS API to encrypt and decrypt.![1600792568594](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600792568594.png)
- we define alias for key which is nothing but a short code and point towards CMK. KMS region based and hence in theory same alias can be used in two different region.![1600796288267](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600796288267.png)
- CMK is not used for data encryption because it can store only upto 4K. KMS is used to interact with data encryption key as shared in diagram below.![1600796730893](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600796730893.png)
- KMS uses **Envelope Encryption** approach.![1600798557594](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600798557594.png)
- 

![1600792281063](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600792281063.png)



### How to encrypt and decrypt by KMS

Steps in Python

- import boto3
- define a kms client by boto3.client(‘kms’)
- define a key_id where it should always be alias/aliasname which was created
- define a variable which has sensitive information
- call kms.encrypt and pass the key_id and plain text variable which has sensitive info
- then store encrypt password from return value of earlier step

![1603729161989](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603729161989.png)



### Lesson Files

- [KMS commands](https://github.com/linuxacademy/aws-csa-pro-2019/blob/master/03_security/01_kms/kmscommands.txt)

### Lesson Links

- [Wikipedia FIPS_140-2 article](https://en.wikipedia.org/wiki/FIPS_140-2)
- [Importing keys](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html)
- [Enveloping](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)
  [Protecting Encrypted Data Integrity](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/)
- [Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html)
- [Compliance](https://aws.amazon.com/kms/details/#compliance)

## AWS Certificate Manager

![1601027510655](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601027510655.png)

## AWS Directory Service

![1601030012339](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601030012339.png)



# Database Considerations

![1603097083903](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097083903.png)

# GuardDuty

![1604420778449](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604420778449.png)![1604420811790](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604420811790.png)![1604420937082](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604420937082.png)

# Detective

![1604420966909](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604420966909.png)![1604421095065](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604421095065.png)

# Inspector

![1604421115681](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604421115681.png)

# Security Service Use case

https://docs.aws.amazon.com/guardduty/latest/ug/s3_detection.html



![1604421160848](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604421160848.png)

![1604421299003](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604421299003.png)

# AWS Database Services

## Database Services

![image](https://image.slidesharecdn.com/introtoawsdatabaseservices-140329115711-phpapp01/95/introduction-to-aws-database-services-56-638.jpg?cb=1396094317)

## Migration

![1604557439528](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557439528.png)

# DynamoDB

## Relational vs RDS

![1604557160806](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557160806.png)

![1604557223264](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557223264.png)

## Dynamo DB



![1600621590113](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600621590113.png)

![1600621624374](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600621624374.png)



## DynamoDB Essentials: Part 1

DynamoDB is a NoSQL web-scale public database delivered as a service by AWS. It uses the wide-column engine and can scale to nearly infinite performance levels if configured correctly. This section covers the product's high-level architecture, including:

- Tables
- Keys
- Items and attributes
- Item GETs and PUTs

**Each item needs an unique value which is Primary Key. Partition key can consist with Partition key or it can be composite with Primary Key and Sort Key. Partition key knows as hash key. Sort key known as range key.**

It is a regional service and so every table in a region should be unique in that specific AWS account.

![1592715121645](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592715121645.png)

The ARN of DDB has region name, AWS account Id and then DDB name. 

![1592749604993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592749604993.png)

**Item can have varying structure in terms of attribute.** Key and attribute total size will need to be 400 KB in size. So when we read an item then we have to read all 400KB item that is full particular item and when i am writing then i need to write full 400kb item. No way, i can read/write partial of an item. Simplest operation are GetItem or PutItem. to get value of an Item, i need to pass the primary key which can be comsoite one.

![1592750170730](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592750170730.png)

## DynamoDB Essentials: Part 2 — Query and Scan

DynamoDB is a NoSQL web-scale public database delivered as a service by AWS. It uses the wide-column engine and can scale to nearly infinite performance levels if configured correctly. This lesson covers the product's high-level architecture, including:

- Scan operation
- Query operation
- Filters

To access a table inside DynamoDB, you either need to give **an IAM user, role, or group in the same account access to that table** using identity policies.Or alternatively, if you want identities outside of your account to access DynamoDB then you need to have created a role inside your account and allow an external identity or anonymous identities to assume that role.

So unlike S3, you can't apply resource level permissions. So you can't control permissions directly on a table.

DynamoDB is resilient on a regional basis. So when you create a table, DynamoDB stores at least three replicas of any data in that table when you use the service.

So when you write to DynamoDB, you actually get a HTTP status code of 200 when you've written data to DynamoDB and it's acknowledged that it has stored it persistently. So if you get a status code 200 that's more applicable if you use in the APIs directly.

DynamoDB handles the replication between the storage devices. So DynamoDB can survive the failure of an availability zone without any additional configuration. 

scan is the most flexible of all of the operations inside DynamoDB. It doesn't actually need to be passed anything. You can simply run a scan operation on a table without any additional parameters and if you do that, it's going to list or retrieve every item in that table. 

Query operations  allow you to perform lookups on the table without having to read every item. filters based on either the partition key or the sort key. So query can only ever retrieve data for one single partition key.  It allows to retrieve for one primary key.

![1592752297184](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592752297184.png)

## DynamoDB Essentials: Part 3

DynamoDB is a NoSQL web-scale public database delivered as a service by AWS. It uses the wide-column engine and can scale to nearly infinite performance levels if configured correctly. This lesson covers the product's high-level architecture, including:

- Point-in-time recovery
- Backups
- Encryption
- Global tables
  - Steps
    - Stream to be enabled
    - Add replica table
    - Add region
  - Now it is a multi-region,  multi-master replication. With DynamoDB, you can read and write to all of the tables and it employs a last writer wins conflict resolution protocol. So if you've got three tables and you write to all three of them with the same item then **whatever gets written to last wins** the conflict and so that data is replicated to all of the other tables. 
  - You can only enable global tables and tables which are empty.
  - So by default, any tables that you create inside DynamoDB operate in a specific AWS region.
- Monitoring
  - Now DynamoDB does come with full integration with CloudWatch, which means you have access to a complete set of metrics about the table and accesses to that table. 

it's a web scale application, if it mentions ID federation, which is something we haven't yet covered, they're all keywords that would point me in the direction of DynamoDB.

## DynamoDB Performance and Billing

DDB is a server less database service. DynamoDB has a number of capacity modes including:

- On-demand
- Provisioned
- Provisioned with Auto Scaling

DDB initially starts with one partition and when volume of data increases then DDB increases number of partitions. Each partition has one leader node and two non-leader node.

![1592753926265](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592753926265.png)

![1592755010390](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592755010390.png)

**Eventually consistent read is much cheaper than strongly consistent reading.**

![1592755758819](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592755758819.png)

![1603096403837](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603096403837.png)



### Extra Reading

- [How to Calculate Read and Write Capacity for DynamoDB](https://www2.linuxacademy.com/howtoguides/20310-how-to-calculate-read-and-write-capacity-for-dynamodb/)
- [Concepts](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html)
- [Time To Live: How It Works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html)
- [Using IAM Policy Conditions for Fine-Grained Access Control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html)

## DynamoDB Streams and Triggers

DynamoDB Streams is a feature enabled on a per-table basis that creates a rolling 24-hour record of changes to items in a table.

Streams can be configured with one of four views:

- Keys only
- New image
- Old image
- New and old images

Lambda can be used to implement a scalable way to implement triggers by invoking whenever a new record is added to the stream.

![1592760293826](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592760293826.png)

## Operations Supported

![1603096799297](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603096799297.png)

## Read and Write Mode

![1603096765041](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603096765041.png)



## Same use case architecture

![1603096838372](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603096838372.png)

## DynamoDB Indexes: Part 1 — LSI

![1603096710070](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603096710070.png)

Local secondary indexes (LSIs) allow an alternative `view` of a table's data to be created, using the same partition key but with an alternative sort key. It cant be used when table does not have sort key.![1592761439028](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592761439028.png)

## DynamoDB Indexes: Part 2 — GSI

Global secondary indexes (GSIs) allow data in a table to be presented using an alternative partition and sort key. GSIs can be used to support alternative data access patterns, allowing efficient use of query operations.

**It is not mandatory to define sort key with GSI.** global secondary indexes are in some way separated from the table that they're linked with so you can allocate individual  read capacity and write capacity units to the global secondary index itself. Any settings that you set on the table are independent from the GSI. You can specify read and write capacity units, or you can apply auto scaling read capacity and auto scaling write capacity. You've got that flexibility and that's important because a lot of the time GSIs have a completely different access. 

**they have their own performance settings and the data that's stored in the table is actually replicated asynchronously to the global secondary index. It's a separate set of data. So there is the potential that the index will lag behind data updates to the table.** What it also means is you can't perform strongly consistent reads on the global secondary index. It has to be eventually consistent and as well as that first GSI,

## Serverless Architecture with Dynamo DB

- Each row is called an Item in DDB
- Event can be DDB insert, Update, delete etc
- During creation of DDB, only primary key is mandatory and sort key is optional

https://www.loom.com/share/815a208178b449129f6174df44f78da7

![1603100168642](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603100168642.png)

### What is DDB?

![1603100207971](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603100207971.png)

### AWS Database Services

![1604557358810](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557358810.png)

![1603100529799](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603100529799.png)



### How Dynamo DB Works?

![1603100832712](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603100832712.png)

![1603100911035](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603100911035.png)

**partitions are managed by AWS.**

### Local secondary Index

- when we are choosing same primary key but sort key is different

![1603102382784](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603102382784.png)



### Global Secondary Index

- when we are choosing diff partition key
- When we need query based on different key which is not there in primary and sort key
- when we perform operation (read/write), we need to provide partition key in hash key. But there can be scenario when our preference is to do operation based on other key then we need GSI to achieve same performance.
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

![1603102420099](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603102420099.png)

### Dynamo DB Streams

- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html
- 

![1603102798654](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603102798654.png)![1603103037196](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603103037196.png)![1603105155742](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105155742.png)

### Build Resilient Client  Behavior

- Handle error 500 when DDB query fails
- 

![1603103789652](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603103789652.png)

### DDB Access Control

![1603103883672](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603103883672.png)

### Global Tables

![1603103983197](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603103983197.png)

### Dynamo DB Accelerator

- Better performance than standard DDB for read operation. Performance of DAX is micro sec whereas DDB performance is mili sec.

![1603104245323](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104245323.png)

### Backup and Restore

![1603104283410](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104283410.png)

### Monitoring and Troubleshooting

![1603104464078](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104464078.png)

### Uniform workload

- selection of primary key critical. Partition key should be equally distributed across partitions to ensure equal load
- Total throughput is divided equally across partitions
- So we don't want one partition to be extra hot which will make some of the throughput in cold partition unused

![1603104607201](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104607201.png)![1603104690113](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104690113.png)

### Use of Index

![1603104755781](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104755781.png)

### DDB Table Create logic

- dont go for complex table and rather make multiple table

![1603104932457](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603104932457.png)

### Serverless Architecture Pattern

![1603105019849](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105019849.png)

### Time Series Data - Architecture

#### Requirement

![1603105269745](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105269745.png)

#### Initial Solution

![1603105343765](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105343765.png)

#### Final Solution (But where is still issue?)

![1603105418180](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105418180.png)

###### Cost Consideration

- Cost is very high for above solution

![1603105578963](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105578963.png)

#### Optimized solution

- Do bulk insert and define batch size is important
- Use TTL to manage lifecycle of data
- Use compression during insert

![1603105722835](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105722835.png)

### Scaling consideration

![1603105747936](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603105747936.png)

## Dynamo DB SA Course

DynamoDB is a Database as a Service product that's accessible **within a VPC (using a VPC endpoint or internet gateway) and using public endpoints. DynamoDB is a key-value database with extensions to that feature set. It's capable of operating at huge scale and integrating with many other services**.

**Only Sort key and primary Key are mandatory.**

![1597663530307](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597663530307.png)

**Note: Filter does not reduce amount of data is being read. It still queries same amount of rows and then apply filter. So always apply sort key to reduce to read unit while reading DDB. Scan also consumes consume full read capacity of DDB.**

- With Query we can pickup only one partition key
- With scan, we can pickup multiple partition key

![1597664426306](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597664426306.png)





### Lesson Links

- [General Guidelines for Secondary Indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general.html)
- [Read Consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)

## Dynamo DB seminar

First 1 hour recorded in https://www.loom.com/share/815a208178b449129f6174df44f78da7



![1602581910938](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602581910938.png)



![1602582369863](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602582369863.png)



### How DDB Works?

The partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

The sort key of an item is also known as its range attribute. The term range attribute derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

![1602582602066](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602582602066.png)

![1602582962583](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602582962583.png)

### Consistency

Write is always consistent but not read. Eventual consistent read.

**Eventual consistent read**

![1602583305240](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583305240.png)

**strongly consistent read**

![1602583345567](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583345567.png)

### Read and Write Capacity Unit

Have adaptive capacity also.https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html

![1602583439798](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583439798.png)![1602583584203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583584203.png)

![1602583669795](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583669795.png)

### Secondary Batch Index

![1602583817180](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583817180.png)

![1602583879020](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602583879020.png)



**Provides strong consistency read and provide eventual consistent read.**

### Global Secondary Index

**Do not provide strong consistency read. Only provide eventual consistent read. Can be created and deleted at will.**

![1602584118392](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602584118392.png)

### DynamoDB Stream

Similar to kinesis stream.

![1602584293733](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602584293733.png)

![1602584418577](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602584418577.png)

















### DDB Migration

![1602587198323](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587198323.png)

### Serverless Building Blocks and a SOlution

https://www.loom.com/share/cd919243f746426196af2f794249388f

![1602587433654](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587433654.png)

![1602587610416](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587610416.png)

![1602587641587](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587641587.png)



**Better Architecture**

![1602587690464](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587690464.png)

**Cost calculation and see how hight**

![1602587746554](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587746554.png)

**Can we do better??**

![1602587833278](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587833278.png)

#### Scaling Operation of DDB

![1602587888205](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1602587888205.png)



### Questions



# S3 Architecture and Features

In Object store, either we store entire or nothing.

![1603087292620](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603087292620.png)

![1603087550088](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603087550088.png)

![1592667979433](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592667979433.png)

## Permissions

S3 permissions can be applied using identity policies, resource policies, and ACLs. This lesson introduces each and explains the basic implementation and architecture.

![1595081074833](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595081074833.png)

**Here is a sample identity policy attached to IAM users.**

![1595081256102](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595081256102.png)

### Lesson Links

- [How Do I Edit Public Access Settings for S3 Buckets?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-bucket.html)
- [Controlling Access to S3 Resources](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

## S3 Facts

![1603087353984](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603087353984.png)

## Use cases

![1603087512397](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603087512397.png)

## Transferring Data to S3

This lesson looks at single PUT upload and multipart upload, including when to use both.

**Highly Recommended Reading for the Certification**

- [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)
- [S3 Data Consistency](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html#BasicsKeys)

![1595355468969](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595355468969.png)

## Encryption

S3 is capable of encrypting objects — either allowing the customer to manage keys or providing an end-to-end solution. This lesson evaluates the options available for encryption:

- SSE-C
- SSE-S3
- SSE-KMS

Additionally, the lesson reviews the default encryption setting for S3 buckets.

![1595355918495](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595355918495.png)



### Lesson Links

- [Blog post on the bucket policy to control allowed encryption types](https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## Static Websites and CORS

Static web hosting is a great way to implement simple websites or provide static offloading for existing web servers.

![1595518740385](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595518740385.png)

![1595518855385](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595518855385.png)



### Lesson Links

- [CORS](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)

### Bucket Policy Sample

```
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
    }
  ]
}
```

## S3 Object Versioning

Versioning is a feature allowing multiple versions of an object to exist in an S3 bucket. Versioning needs to be enabled at a bucket level, meaning every object is given an object ID. When objects are deleted, a version ID is added rather than actually deleting the object.

![1597168236280](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597168236280.png)

Can be applied on new or existing bucket.

![1600413614911](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600413614911.png)

This lesson details the architecture and features of versioning as well as MFA Delete.

![1595526686229](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595526686229.png)

**See below. when we delete a file from S3 where version is enabled, it basically mark a delete tag and we still have the files in version control. So it hides it from read. I can delete this delete marker and file will be available again.**

![1595526928214](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595526928214.png)

**Remember when versioning enabled**

- Put Object creates a new version
- Delete Object sets/adds a delete marker for newly created version 3
- Delete Object Version 3 will delete that particular version permanently

![1600414071319](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600414071319.png)

![1600419006951](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600419006951.png)



### Lesson Links

- [Deleting Object Versions](https://docs.aws.amazon.com/AmazonS3/latest/dev/DeletingObjectVersions.html)
- [Using MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html)

## Presigned URLs

Presigned URLs allow access to objects on a temporary basis. They are created, and the bearer of the URL has the same level of authorization as the creator.

![1595527194834](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595527194834.png)

![1595527402382](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595527402382.png)

## S3 Security

![1603088289903](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088289903.png)



## SA S3 Architecture

![1596190102845](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1596190102845.png)

**S3 is object storage system and not a file storage system. File storage operate using file system as base entity. Files are blocks of binary data and metadata are stored in file system. Object storage is a flat and no hierarchy. Object contains its own metadata along with name.**

![1596190208688](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1596190208688.png)

### S3 Static Web Hosting

![1596215988365](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1596215988365.png)

### S3 Object concepts

![1596216223593](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1596216223593.png)

### S3 and Bucket Policy

Remember bucket has IAM Policy and then we have Bucket permission which can override that. When you create a bucket by default, all these options are turned on so it will block any public access being defined on the bucket. This didn't used to be the case. **So even if you create a bucket and even if you grant public access to an object in that book it than this public access settings dialog can veto that so it can prevent public access to the bucket. Now also be aware that this is defined at a bucket level, but also we can define public access settings for the account so there are account defaults and there are bucket defaults.**

  

![1597166547697](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597166547697.png)

After that account level S3 bucket policy is there which can veto any bucket policy and IAM roles.

![1597166620366](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597166620366.png)

#### Lesson Links

- [Amazon S3 Data Consistency Model](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html#ConsistencyModel)
- [Hosting a Static Website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
- [Listing Keys Hierarchically Using a Prefix and Delimiter](https://docs.aws.amazon.com/AmazonS3/latest/dev/ListingKeysHierarchy.html)
- [Bucket Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)

### S3 Storage Tiers, Intelligent-Tiering, and Lifecycle Policies

This lesson walks through the storage tiers available in S3 in addition to evaluating Intelligent-Tiering and Lifecycle policies.

![1597167124652](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597167124652.png)

![1597167836897](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597167836897.png)

#### Lesson Links

- [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)

### S3 Object Locking

**Versioning is pre-requisite of Object locking.**

![1600430299034](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600430299034.png)

![1600431204482](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600431204482.png)

**This diagram shows that we have Compliance lock for the period of t0 to t10 (up to 10 days) and then in between from t3 till t-12 we have the Legal Hold locking enabled. So this means we can have two locking in parallel. At T12 the legal hold locking is getting disabled.**

![1600431434219](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600431434219.png)



### S3 Versioning and Lifecycle Policies

![1603088432199](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088432199.png)

![1603088493210](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088493210.png)



![1600419124386](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600419124386.png)

**Following rules will allow non-current version files to be deleted...**

![1600419335628](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600419335628.png)

![1600428950574](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600428950574.png)



### Controlling Access to S3 Buckets

This lesson evaluates the various ways to control access to an S3 bucket: **ACLs, identity policies, and bucket policies**. It also looks at how presigned URLs can be used to grant time-limited access to resources using the creator's permissions.

![1597168894530](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597168894530.png)

**Bucket Policy enables non authenticated identity users to access buckets. You can have only one bucket policy but it can have multiple statements. Each statement can have key and value. It is resource policy and so not attached to any identity. Remember, IAM users have their own Identity policy and bucket have their own resource policy.**

- Principal value of * means anyone/any identity can access the bucket
- Effect value "Allow" means to allow action of "s3:GetObject" on the bucket. 
- This all means public read access and this is what static web hosting bucket has

![1597207405242](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597207405242.png)

### Lesson Links

- [Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html)
- [Uploading Objects Using Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html)

### S3 Replication

![1600429431531](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600429431531.png)

** S3 Replication Cross Accounts: Destination bucket owner must add source bucket owner to replicate data by adding details in destination bucket policy.**

![1600429582188](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600429582188.png)

![1600429799785](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600429799785.png)

![1597213653624](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597213653624.png)

This lesson looks at the replication architecture in S3 provided by cross-region replication (CRR). Its features and limitations are evaluated from a solutions architecture perspective. cross region replication is essentially a feature w**here you can take one bucket a source S3 bucket and you can replicate any objects that are created, updated or deleted in that source bucket to a destination bucket and the destination bucket needs to be in a different AWS region, so cross region replication, or CRR s one way**. So it only occurs from the source bucket to the destination bucket does not occur in the opposite direction, and it's not retroactive. Not applicable for old objects and gets applied for all new objects after CRR created on bucket. **CRR requires versioning. Has flexibility to defines rules based on file prefix or tag. We cant do CRR for files which are encrypted by customer managed keys**

![1597214080231](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597214080231.png)

**By default CRR maintains file storage class and Object ownership as per source but we have option to change this.**

![1600430065716](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600430065716.png)

![1600430163787](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600430163787.png)



### Object Encryption

S3 is capable of encrypting objects — either allowing the customer to manage keys or providing an end-to-end solution. This lesson evaluates the options available for encryption:

- SSE-C (Server side encryption with client managed keys)
- SSE-S3 (S3 Managed Keys)
- SSE-KMS (AWS Key management services, managed keys)

![1600105202570](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600105202570.png)

This lesson looks at the various object-level encryption options available within S3: SSE-S3, SSE-C, and SSE-KMS. Additionally, we'll evaluate bucket default encryption options and how a bucket policy can be used to insist on certain object encryption settings.

- Client side encryption/Encryption in Transit

  - Encrypt before pushing to S3. Manage of key and encryption process are client responsibility

- Server side encryption

  - S3 is responsible for encryption and decryption. From client perspective assuming we have access then we are sending un-encrypted files while uploading and downloading. Communication can have SSL although.

  ![1597220181404](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597220181404.png)

### S3 Pricing

![1603088611648](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088611648.png)

![1600104728090](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600104728090.png)



![1600104856095](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600104856095.png)

![1600412540546](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600412540546.png)![1603088895460](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088895460.png)

![1603088677287](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603088677287.png)

### Optimizing S3 Performance

Simple Storage Service (S3) is an object storage system capable of an extreme level of performance with its default configuration. This lesson looks at some of the ways to enhance and improve performance even further, including:

- Multipart upload
- Transfer Acceleration
- Object naming

![1597220997346](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597220997346.png)

#### Lesson Links

- [Amazon S3 Transfer Acceleration — Speed Comparison](http://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html?region=us-east-1&origBucketName=secretcatpics)

- [Request Rate and Performance Guidelines](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)

- [How Do I Enable Transfer Acceleration for an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-transfer-acceleration.html)

- [Requirements for Using Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html#transfer-acceleration-requirements)

  

### Glacier Architecture

S3 Glacier is an isolated product most commonly understood to be a type of S3 storage tier. In reality, Glacier is used to support these S3 tiers but can also be used as its own product with a valuable set of features.

This lesson details the architecture of the product when used in isolation.

#### Lesson Links

- [Amazon S3 Glacier Data Retrieval Policies](https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html)
- [Retrieving Vault Metadata in Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html)
- [Downloading a Vault Inventory in Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html)
- [Amazon S3 Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html)
- [Working with Archives in Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html)

# CloudFront

## CloudFront Architecture: Part 1

CloudFront is an essential component for global applications. As a content delivery network, CloudFront is designed to ensure the efficient delivery of content from local edge locations distributed globally.

This lesson will walk through the architecture of CloudFront and briefly show its implementation.

![1595527833081](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1595527833081.png)

### Lesson Links

- [CloudFront Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

### Bucket Policy

```
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::ac-globalcats/*"
      ]
    }
  ]
}
```

# EBS Volume

**Same as any system volume disc. It is "Highly Available" and "Automatically replicated within same AZ by default" to protect hardware failures. Dynamically increases capacity and type of volume with no downtime.**

Types

- GP2 (General Purpose SSD) : 3 IOPS per GB upto maximum 16,000 IOPS per volume. Good for boot volume, development and test where latency is not factor. Durability: 99.99%
- Provisioned IOPS SSD (IO1) : 50 IOPS per GB and upto 64000 per volume.  Most expensive and high performance, I/O intensive operation. Durability: 99.99%
- Provisioned IOPS SSD (IO2) : 500 IOPS per GB and upto 64000 per volume.  Latest generation and higher durability. Durability: 99.9999%
- Throughput HDD (st1):  Low cost HDD Volume.  Throughput 40 MB/s per TB. Great for frequently accessed, ETL, Log processing. Cost effective one. Not allowed to be Boot volume.
- Cold HDD (sc1): Cheapest. Throughput : 12 MB/s per TB. Good for cold data.

![1600523835903](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600523835903.png)

![1600524605034](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600524605034.png)

We can even create a volume from snapshot. In this case the volume type will be exact same as snapshot.![1600525315924](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600525315924.png)

# Elastic Load Balancer

Autoscaling group is a logical combination of EC2 instances and define a metrices for this.

- Ex: Whenever my CPU instance is > 70% then add one more EC2 instance
- ELB works in hand =by-hand with auto scaling group to distribute load across EC2 instances

![1603097440877](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097440877.png)

**All metrices gets to cloud watch and it raises an alarm whenever metrices breaches and auto scaling gets triggered to add one more EC2 instance**

![1603097499840](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097499840.png)

![1603097575074](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097575074.png)



## Application load balancer (At OSI Layer 7)

- Route the request at application at OSI layer 7. Here we hit the http traffic which is top most layer and based on content of my request, we use ALB to route the request.
- 

![1600600503079](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600503079.png)

![1603097648320](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097648320.png)

## Network Load balancer (OSI Layer 4) - Used in PROD for latency

- Operate at transport level
- 

![1600600556590](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600556590.png)

![1603097769318](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097769318.png)



## Classic load balancer  - Legacy one

![1600600605021](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600605021.png)![1600600686783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600686783.png)

**Classic Load Balancer uses X-forward" and thats why to get public IP address we need to look into x-forward-header.**![1600600840091](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600840091.png)

## Load Balancer Comparism

![1603097859293](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603097859293.png)

## Elastic Load Balancer

A **load balancer** serves as the single point of contact for clients. The **load balancer** evenly distributes incoming **application** traffic across multiple targets, such as **EC2** instances , in multiple Availability Zones. This increases the availability & fault tolerances of **application**. You add one or more listeners to your **load balancer**.

![im](https://jayendrapatil.com/wp-content/uploads/2016/04/screen-shot-2016-04-05-at-7-54-34-am.png)

**But what happens if traffic demand is so high that active servers can't handle?** That's when Auto scaling can be used. Auto Scaling groups add elasticity and scalability to ELB functionality.

![1590767911701](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1590767911701.png)

## Exam Tips

![1600600894793](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600600894793.png)

# VPC

## Flow Log

**VPC Flow Logs** is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your **VPC**. **Flow log** data can be published to Amazon **CloudWatch Logs** or Amazon S3. After you've created a **flow log**, you can retrieve and view its data in the chosen destination.

![im](https://miro.medium.com/max/521/1*p0ZHXBA-69vQYZcOxJVjFg.png)

# Security Hub

AWS Security Hub provides you with a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices.

Security Hub collects security data from across AWS accounts, services, and supported third-party partner products and helps you analyze your security trends and identify the highest priority security issues.

![1592851021070](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592851021070.png)



# AWS Application arhcitecture

![1592853657854](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592853657854.png)

![1592853883467](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592853883467.png)

![1592853935123](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592853935123.png)

![1592853986852](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592853986852.png)



# Simple Notification Service (SNS)

![1597343258148](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343258148.png)



![1597226641133](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597226641133.png)

Simple Notification Service (SNS) is a key part of AWS application integration products. It provides a pub/sub-based notification system, which supports a wide range of subscriber endpoint types.

![im](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2017/07/25/messaging-fanout-for-serverless-with-sns-diagram1-1024x615.png)

**Above complicated architecture can be easily replaced by SNS with multiple topics.**

![im](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2017/07/25/messaging-fanout-for-serverless-with-sns-diagram2-1024x615.png)

![1593972517577](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593972517577.png)

![1593972589705](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593972589705.png)

It is highly resilient service and available within a region. It falls back to AZ when failover needed. It is a public aws service and has a public endpoint. To access this within VPC, we need NAT Gateway & Internet Gateway or VPC Gateway. **It has resource policy and we can support either owner to publish the topic or everyone.**

![1593972958367](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1593972958367.png)

## SNS - SA 

This lesson evaluates SNS and how it can be used with other services, such as SQS, to implement more complex architectures.

![1597226662541](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597226662541.png)

**Fan Out Architecture**: This is the architecture when multiple SQS are subscribed to same topic of SNS and so then we can have each of the SQS have their own lambda to work on. So basically we are creating multiple subscription and then in endpoint attaching SQS ARN. So now one SNS topic has multiple subscription and each of the subscription has different SQS ARN added  into end point. **See the above architecture where we have multiple subscriber attached with a topic and then multiple SQSQ associated.**

![1597227260437](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597227260437.png)

![1597343463246](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343463246.png)



## Exam Tips

![1597343512900](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343512900.png)

## References

- 10-minute Tutorial: [How to Send Fanout Event Notifications](https://aws.amazon.com/getting-started/tutorials/send-fanout-event-notifications/)
- Amazon SNS Developer Guide:

  - [Sending Amazon SNS Messaging to Amazon SQS Queues](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html)
  - [Sending Amazon SNS Messaging to HTTP/HTTPS Endpoints](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html)
- AWS Compute Blog:  [Fanout S3 Event Notifications to Multiple Endpoints](https://aws.amazon.com/blogs/compute/fanout-s3-event-notifications-to-multiple-endpoints/)



## SES vs SNS

![1597343572349](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343572349.png)

![1597343622169](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343622169.png)

![1597343654224](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343654224.png)

## Exam Tips

![1597343724185](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597343724185.png)

# Elastic Transcoder

Elastic Transcoder is a service that performs "serverless" transcoding of media between formats. By default, it works using a manual job submission system but can be expected to operate in an event-driven way.

![1594144064848](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594144064848.png)

Elastic Encoder:

![1594746636459](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594746636459.png)

- pipeline
  - It is job queue.
  - we generally have more than one pipeline for each different priority processing.
- Job
  - One job can generate upto 30 output file. Format of output(encoding) are defined in preset.
- output file

# Analytics

## Athena

Amazon Athena is a serverless query engine capable of reading a wide range of data formats from S3. Athena uses a schema-on-read approach to allow SQL-like queries against non-relational data.

- Schema is not a physical one and it is how you want the data to look like
- Schema is only used when we read data and schema have virtual table 
- point athena at data and query through schema.
- athena used serverless data processing

![1594747849706](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594747849706.png)

## Elastic MapReduce (EMR)

Elastic MapReduce is an AWS-managed implementation of the Apache Hadoop ecosystem of products. This lesson walks through the high-level architecture of the product.'

![1594748674863](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594748674863.png)

# Kinesis and Firehose

Kinesis and Kinesis Data Firehose are two essential pieces of any high-performance streaming architecture. This lesson walks through the architecture, integration options, and common use cases of both products.

- **Real-Time:** Amazon Kinesis enables you to ingest, buffer and process data in real-time. One can easily derive insights in just a few seconds or else minutes.
- **Fully Managed:** Amazon Kinesis can easily run the streaming applications and can be fully managed without any requirement of infrastructure management.
- **Scalable:** Amazon Kinesis can easily handle any amount of streaming data and can easily process data from thousands of sources with a low level of latencies

![1594748935674](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594748935674.png)

**Data persist till 24 hrs which is rolling window. Once the rolling window is over then data gets dropped.**



![1594749096635](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594749096635.png)

![im](https://mindmajix.com/blogs/images/Amazon%20kinesis.png)

**Performance is related to no shard. SQS is designed for one processor is reading from queue and processing, deleting. It does not support multiple processor reading same message from same queue. Kinesis can hold message for 24 hrs even though it is read by consumer which is differntiates from SQS.**

![1594750712561](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594750712561.png)

![1594750979783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594750979783.png)

## Kinesis Streams

- Consists of shard
- 5 transaction per sec upto read 

![1597344022645](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597344022645.png)



![1597344226971](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597344226971.png)



## Kinesis Firehose

- does not retain data like kinesis stream. As soon as data arrived, it analyzed the data and push that to S3.
- Used to send data to elastic search cluster

![1594751161024](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594751161024.png)

## Kinesis stream - LA SA Professional

Kinesis is a product within AWS designed to ingest a huge amount of real-time streaming data. It's capable of scaling from low loads to an infinite amount due to its shard architecture. This lesson details the architectural components of Kinesis.

**Main difference with SQSQ is that SQS is meant for single set of entity to put the request into Queue and single set of processing node from receiving node. But kinesis stream supports multiple sender and receiver. Kinesis is designed to accept huge no of realtime requests from producers.**

For more on video vs data streams in Kinesis, see: <https://aws.amazon.com/kinesis/video-streams/faqs/> <https://aws.amazon.com/kinesis/data-streams/faqs/>

![1601288979033](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601288979033.png)

![1601289357476](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601289357476.png)

Producers needs to know data source name and partition key to push data into kinesis stream. It has by default 24 hrs retention.

![1601289549164](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601289549164.png)

Kinesis stream

- Shard (By increasing, we get higher output)
- Data retention (By increasing data retention, the storage of kinesis stream gets increased)
- KMS Encryption (Any of data in stream during retention period can be subjected to server side encryption). So this means consumer need to have Kinesis permission to read from stream and KMS permission for decryption.
- By default, we have stream level metrices and we can enable shard level statistics
- Default retention period if 1 day and it can be increased to 7 days.
- KINESIS is a **public space service inside AWS**, and that means that it does. public zone end points. So if you are wanting to interact with kinesis inside a VpC, maybe you've got a fleet of easy two instances that you want to act as consumers. You do need to make sure that **VPC includes the appropriate networking resource is inside that vpc** You do have the ability, though, to configure VPC end points to provide access to kinesis without that external infrastructure requirements. 

## Kinesis Firehose - LA SA Professional

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk. This lesson walks through this architecture and discusses some of the features from an architectural perspective.

![1601304823551](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601304823551.png)

![1601304842021](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601304842021.png)

## Kinesis Analytics - LA SA Professional

![1601306083907](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601306083907.png)

Can read from source and we can have "Record pre-processing with lambda"

- Kinesis stream
- Kinesis firehose delivery stream

![1601359016092](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601359016092.png)



# Redshift

**It is column based database.**

![1594751412375](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1594751412375.png)



# Build a Simple Serverless Website with Route 53, API Gateway, Lambda and S3

- First ensure S3 bucket name available. **Bucket name and domain name will require to be same**
  - Make the S3 bucket enabled for static web site hosting
- Domain need to be registered through Route 53
- Configure our lambda functions
  - Add triggers as API Gateway
    - Provide
      - API Name
      - stage
      - security
- Configure API Gateway
  - Add method of "Get"
    - Define Integration type from Lambda, mock etc
  - Deploy
- a

# X-Ray

![1597339918009](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597339918009.png)

![1597339983405](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597339983405.png)

![1597340041324](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597340041324.png)



# CloudFormation

## Overview

This lesson provides a brief architectural refresher on CloudFormation. Input of CF contains a json or yml file which should bare minimum contain resource details.

![1597498413318](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597498413318.png)

**All stack operation generate a set of events.**

![1597498604993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597498604993.png)

Cloudformation has logical and physical resources. Logical resources comes from input json file resource section as shared below from a cloud formation input file. Then cloudformation takes this input file and for each of the logical resources, it creates the physical resources.

![1597499526720](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597499526720.png)

![1597499607949](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597499607949.png)

### Lesson Files

- [Download the necesssary file from the course GitHub repository.](https://github.com/linuxacademy/aws-csa-pro-2019/tree/master/09_deployment_and_operations/01_CloudFormationOverview)

### Related Courses

- [AWS CloudFormation Deep Dive](https://linuxacademy.com/cp/modules/view/id/157)

## Stack Updates

This lesson evaluates the update behavior of CloudFormation for changes to logical resources.

- Add new logical logical resources
- Delete existing logical resources
- Update existing logical resources

![1597564926683](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597564926683.png)



### Lesson Files

- [Download the necessary file from the course GitHub repository.](https://github.com/linuxacademy/aws-csa-pro-2019/tree/master/09_deployment_and_operations/02_StackUpdates)

## Template Portability and Reuse

This lesson looks at methods to improve the portability and reuse of CloudFormation templates.

### Lesson Files

- [Download the necessary files from the course GitHub repository.](https://github.com/linuxacademy/aws-csa-pro-2019/tree/master/09_deployment_and_operations/03_Portability_and_reuse)

### Lesson Links

- [Pseudo Parameters Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)
- [Intrinsic Function Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html)

### Related Courses

- [AWS CloudFormation Deep Dive](https://linuxacademy.com/cp/modules/view/id/157)

# In-Memory Caching

## DAX

DynamoDB Accelerator (DAX) is an in-memory cache **specifically designed for DynamoDB.** It supports caching eventually consistent reads for items and query results and reduces the latency from single-digit milliseconds to microseconds. DAX is ideal for latency-sensitive applications or for read-heavy workloads on consistent data sets. **DAX works within VPC.**

Application that requires data based on micro sec or requires same pattern of large data from DDB they are ideal candidate of using DAX. **If the application requires strongly consistent data then DAX cant be used.** DAX only supports read caching and if the application is write intensive then DAX should not be used.

**Cache Types:**

- Item Cache has retention period of 5 min default TTL. It from GetItem and BatchGetItem.
- Query Cache : It gets into when we are doing Query by partition key or during scan operation by parameters.



![1597854981660](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597854981660.png)

## ElastiCache

ElastiCache is an in-memory cache that provides the Memcached and Redis caching engines. Helps to offload the reading data from DB and store user session data. So moving session data from application to elasticcache helps application to become stateless.

![1597856949312](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597856949312.png)

### Elastic Cache - LA SA Professional

- Fully managed in-cache data store
- Helps in scalability of application specially for read operation
- 

![1601365870846](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601365870846.png)



 # Container-Based Compute and Microservices

## Docker Essentials

we'll begin our container compute review by taking a look at Docker. We will go over how containers work, discuss when and where you should consider using them. You'll explore the process of installing Docker while creating and running a container on an EC2.

![1597857579059](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597857579059.png)

## ECS

Elastic Container Service (ECS) is a managed container solution available from AWS. It can operate in either EC2 mode, in which EC2 instances running as Docker hosts are visible in your account, or Fargate mode, in which AWS manages the container hosts. This lesson demonstrates how Fargate mode can be used to host the `containercat` container.

![1597859431842](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597859431842.png)



### Lesson Resources

- [Lesson Files on GitHub](https://github.com/linuxacademy/content-aws-csa2019/tree/master/lesson_files/03_compute/Topic5_Containers/Docker)

### Lesson Links

- [Container Cat](https://hub.docker.com/r/acantril/containercat)

### Lesson Commands

```
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

sudo yum install git
git clone https://github.com/linuxacademy/content-aws-csa2019.git

cd content-aws-csa2019/lesson_files/03_compute/Topic5_Containers/Docker/
docker build -t containercat .
docker images --filter reference=containercat
docker run -t -i -p 80:80 containercat

docker login --username YOUR_USER
docker images
docker tag IMAGEID YOUR_USER/containercat
docker push YOUR_USER/containercat
```

### Ordering and DB Service

![1605243396390](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243396390.png)

### EC2 Ways Task Definition

![1605243623359](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243623359.png)![1605243696076](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243696076.png)



These are clusters and are collection of EC2 instances. They are region based.

![1605243842197](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243842197.png)

![1605243895807](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243895807.png)

![1605244343960](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605244343960.png)

### Fargate Ways Task Definition

![1605243750398](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605243750398.png)

### Task Defintions

![1605244447627](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605244447627.png)



# Global DNS (Route 53) 

## Fundamentals

Route 53 provides DNS functionality within AWS, and this lesson acts as a foundation for future lessons that require DNS knowledge.

![1597859967747](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597859967747.png)

![1597860053873](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597860053873.png)



### Lesson Links

- [DNS Root Servers](https://www.iana.org/domains/root/servers)
- [DNS Root Database](https://www.iana.org/domains/root/db)

## Domain Registration

This lesson walks through the process that occurs behind the scenes during domain registration. The lesson uses a real example and explains what Route 53 and domain operator process that occurs at each step.

## Private vs. Public Hosted Zones

A DNS zone is a portion of the global DNS database that contains records and configuration for one or more domains. This lesson looks at public and private zones that are provided by Route 53. The lesson also demonstrates split zone DNS and evaluates when it should be used.

![1597945665820](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597945665820.png)

### Lesson Links

- [Public Cats User Data](https://raw.githubusercontent.com/linuxacademy/content-aws-csa2019/master/lesson_files/04_networking/Topic4_DNSFundamentals/PrivatePublicZones/PublicCats/userdata.txt)
- [Private Cats User Data](https://raw.githubusercontent.com/linuxacademy/content-aws-csa2019/master/lesson_files/04_networking/Topic4_DNSFundamentals/PrivatePublicZones/PrivateCats/userdata.txt)

## Record Set Types

This lesson provides a high-level summary of the different record types available within DNS and some Route 53-specific enhancements. Particularly, we look at:

- A records
- AAAA records
- CNAME records
- MX records
- NS records
- TXT records
- Alias record types

![1597945898150](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597945898150.png)




# RDS 

## Essential

Relational Database Service (RDS) provides databases as a service using the following engines:

- MySQL
- PostgreSQL
- MariaDB
- Oracle
- Microsoft SQL
- Aurora

![1597947264539](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597947264539.png)

This set of lessons introduces the architecture fundamentals of RDS and demonstrates an example implementation.

Here is the [CloudFormation template for the lesson](https://raw.githubusercontent.com/linuxacademy/content-aws-csa2019/master/lesson_files/06_databases/02_RDS/rds_essentials/vpc.yaml).

Here are the commands used to install WordPress:

```
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
sudo cp wp-config-sample.php wp-config.php
sudo nano wordpress/wp-config.php
sudo cp -r wordpress/* /var/www/html/

sudo chown -R apache /var/www
sudo chgrp -R apache /var/www
sudo chmod 2775 /var/www
sudo find /var/www -type d -exec sudo chmod 2775 {} \;
sudo find /var/www -type f -exec sudo chmod 0664 {} \;
sudo systemctl restart httpd
```

![1597947508217](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597947508217.png)

### Lesson Links

- [Working with DB Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)
- [Working with Option Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)
- [Amazon RDS for MySQL Pricing](https://aws.amazon.com/rds/mysql/pricing/)
- [Identity and Access Management in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html)
- [Limits for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)
- [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
- [Connecting to Your Linux Instance from Windows Using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)

## RDS Backup

RDS supports manual snapshot-based backups as well as automatic point-in-time recovery-capable backups with a **1- to 35-day retention period**. This lesson walks through the architecture, features, and limitations of both methods.

**It creates brand new DB during backup restore and does not restore on existing DB.**

![1597984088009](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597984088009.png)

## RDS Resiliency: Multi-AZ

 Multi-AZ architecture of RDS — a way of adding high availability failover to a database.

![1597984883980](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597984883980.png)

## RDS Read Replicas

RDS read replicas offer the ability to scale an RDS database from a read workload perspective and improve the ability to recover from serious failures either within the region or internationally.

![1597985811873](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597985811873.png)

### Lesson Links

- [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)

## Aurora

![1604557109302](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557109302.png)



# VPN and Direct Connect

## DirectConnect

![1604558821749](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604558821749.png)

## VPC VPN (IPsec)

VPC VPN (also known as Hardware VPN) is a virtual network solution to connect a VPC to a non-AWS network, such as on-premises or data center. It is a highly available solution that can be configured to use either static or Border Gateway (BGW) routing. This lesson introduces the architecture and demonstrates how a VPC VPN is configured.

![1597987917625](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597987917625.png)

![1597991012771](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597991012771.png)



# AWS Elastic Search

It is mainly for realtime data and value of data diminishes as time goes. So we need to consider cost of holding of data and ROI of data holding.

![1599022785509](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599022785509.png)

![1599022903167](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599022903167.png)

![1599022979780](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599022979780.png)

![1599023066469](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599023066469.png)

![1599023265775](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599023265775.png)

So we enable customers to store old log files at reduces cost and at same time provide the ability to same query and analysis on same old data. within service itself data is stored in S3 in highly durable store (Hot data node). Ultra warm uses S3 and have some local caching, adaptive pre-caching to improve performance further.

![1599023516286](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599023516286.png)

![1599024061186](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599024061186.png)

![1599024475077](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599024475077.png)

![1599024533403](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599024533403.png)

![1599024601040](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599024601040.png)

# CloudFront

## CloudFront Architecture: Part 1

CloudFront is an essential component for global applications. As a content delivery network, CloudFront is designed to ensure the efficient delivery of content from local edge locations distributed globally.

![1599667899690](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599667899690.png)



![1599667356657](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599667356657.png)



## Lesson Links

- [CloudFront Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

### Bucket Policy

```
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::ac-globalcats/*"
      ]
    }
  ]
}
```

# EFS and SFX

- EFS for Linux workload.
- shared file system and can be mounted on EC2 instance

![1604558976519](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604558976519.png)



# Virtual Private Cloud (VPC) and Subnets

This lesson walks through VPC architecture:

- VPC region
- VPC IPv4 CIDR
- VPC tenancy
- VPC subnets

![1599671792302](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599671792302.png)

## SubNet

- VPC can have many subnet
- Private services stays under subnet.
- Image VPC as datacenter and subnet is a floor in that data-center
- Subnet cant span across AZ. Each subnet is homed in a single AZ
- Default VPC create subnet into all AZ of that region
- 

![1599842364366](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599842364366.png)

## Routing and Internet Gateway

This lesson discusses routing within a VPC, specifically looking at:

- Public and private subnets
- Internet gateways
- Route tables
- Local routes
- Default routes
- Auto-assign public IP
- Static Network Address Translation (SNAT)

**An internet gateway is attached to only one VPC AND VICE-VERSA.** Every route table is aaaociated with VPC.

![1599920790111](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599920790111.png)

![1599921300449](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599921300449.png)

## Bastion Host/JumpBox

A bastion host (also known as a JumpBox) provides a locked-down entry point to a secure or fully private VPC. It's a common feature of many AWS architectures and, as such, it's essential to understand for the exam and production usage.

For a new way to securely connect to instances without having to use a bastion or open SSH ports, see: <https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html>

![1599923090797](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599923090797.png)

**Security group is set of firewall rules that control traffic for our EC2 instance.  If we want to setup a web server and allow internet traffic to reach our instance, add rules that allow unrestricted access to HTTP and HTTPS port. **

![1599923991520](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599923991520.png)

## NAT, NAT Instance, and NAT Gateway: Part 1

NAT (network address translation) is a process where the source or destination attributes of an IP packet are changed. Static NAT is the process of 1:1 translation where an internet gateway converts a private address to a public IP address. Dynamic NAT is a variation that allows *many* private IP addresses to get outgoing internet access using a smaller number of public IPs (generally one). Dynamic NAT is provided within AWS using a NAT gateway that allows private subnets in an AWS VPC to access the internet.

This lesson walks through the NAT gateway architecture, including:

- NAT gateway core functionality
- NAT gateway high availability

![1599924430056](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599924430056.png)

NAT (network address translation) is a process where the source or destination attributes of an IP packet are changed. Static NAT is the process of 1:1 translation where an internet gateway converts from a private address to a public IP address. Dynamic NAT is a variation that allows *many* private IP addresses to get outgoing internet access using a smaller number of public IPs (generally one). Dynamic NAT is provided within AWS using a NAT gateway that allows private subnets in an AWS VPC to access the internet.

This lesson walks through the NAT gateway architecture including:

- NAT gateway core functionality
- NAT gateway high availability
- Route table configuration
- Public IP addressing (EIP)

### Lesson Links

- [SSH Agent Forwarding](https://aws.amazon.com/blogs/security/securely-connect-to-linux-instances-running-in-a-private-amazon-vpc/)
- [NAT Gateway and NAT Instance Comparison](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html)
- [SSH Agent Forwarding](https://aws.amazon.com/blogs/security/securely-connect-to-linux-instances-running-in-a-private-amazon-vpc/)
- [NAT Gateway and NAT Instance Comparison](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html)

## Network ACLs

Network access control list (NACL) is a layer 4 filtering product within AWS VPCs that can be attached to a subnet. NACLs process data as it enters and leaves VPC subnets and authorizes traffic to be *allowed* or *denied* based on protocol/IP/CIDR and port range.

This lesson walks through the architecture of a NACL and discusses the unique features it offers. We'll discuss the limitation of NACL versus security groups and other security entities.

![1599929218804](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599929218804.png)

![1599930127805](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1599930127805.png)

## VPC Peering

VPC peering is a feature that allows isolated VPCs to be connected at layer 3. VPC peering uses a *peering connection*, which is a gateway object linking two VPCs.

![1600103334052](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600103334052.png)



# Elastic Cache

![1600622000122](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600622000122.png)

## Redis



## Memcached

# Advanced Identity in AWS

## Identity Federation

- AssumeRole

- AssumeRoleWithWebidentity

- AssumeRoleWithSAML

  

![1600682102097](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600682102097.png)

![1600683804015](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600683804015.png)

![1600683985398](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600683985398.png)

**AssumeRoleWithSAML** can be used with AWS Console.

![1600684454043](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600684454043.png)

**Here Auditor is from another AWS Account and using role too access other aws account.**

![1600684765566](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600684765566.png)

**Here Jess is using ADFS web federated identity.**

![1600685943754](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600685943754.png)

**Here user authentication used by google.**

![1600686008480](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600686008480.png)

### Lesson Links

<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html> <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_cognito.html>

## IAM Permissions Boundaries

This lesson introduces the concepts of IAM permissions Boundaries a way of restricting effective permissions. Permission boundary maximum permission allowed and then subjected to IAM user roles and policies to get actual.

**Here we can see IAM users have policy attached to allow access to S3, Cloudwatch and EC2 while permission boundary only allows S3 and SQS. So the overlap boundary ones which is S3 will only be allowed to access for the IAM user.**

![1600686293648](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600686293648.png)

### Lesson Links

<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>

## Policy Evaluation Logic

process AWS follow to evaluate effective permissions for a given Identity accessing a given resource. Here Org Boundaries are imposed by **Service control policies**. Here  "Role Policies" means assuming role by API.

![1600686867098](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600686867098.png)



### Further Reading

<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>

# AWS WAF

This lesson reviews the architecture of AWS WAF together with Shield Standard and Shield Advanced, three network attack mitigation products available within AWS.

Can be coupled with traffic coming on following..These are services occupying in aws edge.

- Cloudfront
- API Gateway
- ELB

![1601278111981](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601278111981.png)

![1601278311027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601278311027.png)

![1601278405344](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601278405344.png)

We can create condition even to detect IP address and then refer the same into rule. Rules can be

- Regular Rule (Normal ones)
- Rate based rule (Frequency based, ex: **Allowing request only from a specific IP, Detection of request flooding from a specific set of IP**)

> Rules can have condition which can support

> - Geo match
> - Cross site scripting
> - IP address
> - size constraints
> - SQL Injection
> - string and regex matching

## Lesson Links

[Features](https://aws.amazon.com/shield/features/)
[Use case](https://docs.aws.amazon.com/waf/latest/developerguide/aws-shield-use-case.html)
[Getting started](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html)

# AWS Shield

![1601287434763](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601287434763.png)

# AWS GuardDuty

This lesson introduces Guard Duty architecture at a very high level, just covering basic exam requirements. Can access across data sources in aws and can ingest data from all aws sources and provide recommendation in AWS Guard duty console or by generating cloud watch console. It can be used also in AWS Organisation. Guard duty master account is not same as guard duty in aws org.

Support trusted IP address in order to avoid threat generation.



![1601288238352](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601288238352.png)

## Lesson Links

[What is GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

# AWS Redshift

Redshift is a petabyte scale data warehousing and data analysis solution available within AWS. Historically, provisioning a data warehousing solution was expensive and took time. Redshift data warehouses can be created for long-running analysis workloads, or they could be provisioned for one-off projects that can consequently be torn down after completion. This lesson walks through the architecture of Redshift.

- **Redshift is column based database.**

- **No of files from S3 for load and unload should always be multiple of Slices to achieve parallel computing.**
- **We can resize the cluster. Classic cluster (we can change type of node and change no of node) and Elastic resize (we can change no of node and quicker)**
- We can change cluster parameter after it got created.![1601360538483](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601360538483.png)
- We can define/change snapshot setting
-  ![1601360639155](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601360639155.png)



![1601359241471](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601359241471.png)

![1601359343133](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601359343133.png)

## Architecture

![1605069621450](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605069621450.png)



## Lesson Links

- [AWS re:Invent 2018: Deep Dive and Best Practices for Amazon Redshift](https://www.youtube.com/watch?v=TJDtQom7SAA)
- [Distribution Styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html)
- [Current RedShift Node Types](https://aws.amazon.com/redshift/pricing/#Amazon_Redshift_node_types)

## Disaster Recovery in Redshift

- Cross region snapshots shd be used![1601361002328](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601361002328.png)

- Can do full cluster restore or table restore

  

# How to Prepare for the Exam

## Lesson Links & Further Watching/Reading

### AWS SA Pro Sample Questions

[SAP-C01 Sample Questions](https://d0.awsstatic.com/training-and-certification/docs/AWS_certified_solutions_architect_professional_examsample.pdf)

### White Papers

[AWS Securing Data at Rest with Encryption](https://d0.awsstatic.com/whitepapers/aws-securing-data-at-rest-with-encryption.pdf) [AWS Web Hosting Best Practices](https://d0.awsstatic.com/whitepapers/aws-web-hosting-best-practices.pdf?refid=em_) [AWS Migrate resources to a new Region](http://d0.awsstatic.com/whitepapers/aws-migrate-resources-to-new-region.pdf?refid=70138000001adyu) [EC2 FAQs](https://aws.amazon.com/ec2/faqs/) [ELB FAQs](https://aws.amazon.com/elasticloadbalancing/faqs/) [Elastic Beanstalk FAQs](https://aws.amazon.com/elasticbeanstalk/faqs/)

### Identity

**IAM:** <https://www.youtube.com/watch?v=YQsK4MtsELU>

### Compute

**ELB:** <https://www.youtube.com/watch?v=VIgAT7vjol8> **Lambda:** [https://www.youtube.com/watch?v=QdzV04T\_kec](https://www.youtube.com/watch?v=QdzV04T%5C_kec) **EKS:** <https://www.youtube.com/watch?v=EDaGpxZ6Qi0> **VMware:** <https://www.youtube.com/watch?v=RStQrGmHqy0>

### Storage

**S3 & Glacier:** <https://www.youtube.com/watch?v=rHeTn9pHNKo> **S3, EFS, & SBS:** <https://www.youtube.com/watch?v=gidUa4lJd9Y>

### Database

**RDS:** <https://www.youtube.com/watch?v=HuvUD7-RyoU> **DynamoDB:** <https://www.youtube.com/watch?v=HaEPXoXVf2k> <https://www.youtube.com/watch?v=eTbBdXJq8ss> **Aurora:** <https://www.youtube.com/watch?v=2WG01wJIGSQ>

### Networking

**VPC:** <https://www.youtube.com/watch?v=fnxXNZdf6ew> **Transit Gateway:** [https://www.youtube.com/watch?v=yQGxPEGt\_-w](https://www.youtube.com/watch?v=yQGxPEGt%5C_-w) <https://www.youtube.com/watch?v=ar6sLmJ45xs> **VPN:** <https://www.youtube.com/watch?v=qmKkbuS9gRs> **DNS:** <https://www.youtube.com/watch?v=D1n5kDTWidQ>

### Analytics, Streaming, IOT

**Redshift:** <https://www.youtube.com/watch?v=TJDtQom7SAA>

# Cloud Trail

![1601886672314](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886672314.png)

![1603092448634](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603092448634.png)



# Migrating Data to AWS with Snowball and Snowmobile

Snowball, Snowball Edge, and Snowmobile are three products designed to migrate huge amounts of data into AWS. This lesson details the key features and use cases of each.

## Lesson Links

- [What Is an AWS Snowball Device?](https://docs.aws.amazon.com/snowball/latest/ug/whatissnowball.html)
- [How AWS Snowball Works with the Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/how-it-works.html)
- [Best Practices for the AWS Snowball Edge Device](https://docs.aws.amazon.com/snowball/latest/developer-guide/BestPractices.html)
- [AWS Snowball Device Differences](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html)

# Elasticsearch

Elasticsearch is an AWS implementation of the ELK stack (Elasticsearch, Logstash, and Kibana) as a service. This lesson walks through the architecture of Elasticsearch and highlights the important architectural considerations around high availability, cost, performance, and scaling.

## Lesson Links

**Elasticsearch Courses**

- [Elastic Stack Essentials](https://linuxacademy.com/cp/modules/view/id/193)
- [Elasticsearch Deep Dive](https://linuxacademy.com/cp/modules/view/id/213)

# Data Pipeline Essentials

Data Pipeline is a service that allows you to architect serverless pipelines to move and optionally transform data. This lesson details the high-level architecture of the service and provides a quick and simple demo.

## Lesson Links

- [Pipeline Definition](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-pipeline-definition.html)
- [Data Nodes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-datanodes.html)
- [Activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-activities.html)



# CloudFormation Deep Dive

## Infrastructure as Code

![1604557715793](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604557715793.png)

## CloudFormation Essentials

Infrastrucre as code is base here. **All resources like VPC, Kinesis stream, NAT Gateway, S3 are coded into templates. Then templates creates stack.**

## Introduction to JSON

Cloudformation templates can be written in json.

![1601663208087](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601663208087.png)![1601663316901](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601663316901.png)![1601663426536](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601663426536.png)

![1601663490379](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601663490379.png)

### A Cloud formation sample json template

**A VPC formation template**

![1601664366907](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601664366907.png)

## Introduction to YAML

![1601709475883](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601709475883.png)![1601709818942](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601709818942.png)

- See below. in YAML, two - means they are list. So in json they are mentioned as {} whereas in YAML they are mentioned as - .

  

![1601709594720](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601709594720.png)

![1601709858602](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601709858602.png)

## CloudFormation and IAM

![1601710036492](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601710036492.png)![1601710093639](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601710093639.png)

![1601710210999](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601710210999.png)

![1601710269876](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601710269876.png)

**Here are two templates**

![1601710380337](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601710380337.png)

### Sample Template File

More details can be found from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

# AWS Essentials Training

![1601872554453](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601872554453.png)

![1601873014806](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601873014806.png)



## Core Infratructures

![1601873524401](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601873524401.png)

## Cloud Computing

![1601874263753](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874263753.png)

## Foundation services

![1601874424249](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874424249.png)

### EC2

**It is an unmanaged services in AWS. We need to scale up and maintain the services. EC2 by default deployed launched/deployed in single AZ and we need to make this fault tolerant.**

**Same EBS Volume cant be attached to multiple EC2 Instance. If we have such requirement then we can use EFS - Elastic File system which is a shared one and allow multiple EC2 instance to access.**

An Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations. An AMI includes the following: One or more EBS snapshots, or, for instance-store-backed AMIs, a template for the root volume of the instance (for example, an operating system, an application server, and applications). Launch permissions that control which AWS accounts can use the AMI to launch instances. A block device mapping that specifies the volumes to attach to the instance when it's launched.

![1601876716661](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601876716661.png)![1601876751965](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601876751965.png)![1601876868483](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601876868483.png)![1601876959443](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601876959443.png)![1601877555063](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601877555063.png)

![1601877972936](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601877972936.png)



#### Instance Metadata

![1601878100386](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601878100386.png)

#### User data / Bootstrap data

It is a script which gets executed during EC2 instance boot up and configurable within user data. They are executed only once per EC2 instance.

![1601878199419](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601878199419.png)



![1601878283706](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601878283706.png)

#### EC2 Purchasing Options

**Dedicated Instance and Dedicated Hosts are client specific isolated hardware and driven by compliance. .Here HW is not shared and dedicated for client only. So ideally same HW can have multiple EC2 instances of different client but dedicated instances and dedicated hosts dont allow that due to compliances (Like HIPPA etc where they tell HW cant be shared with other clients). If we stop and start EC2 instance then we may get dedicated HW and we may get new MAC address but dedicated host ensure same physical binding is maintained. Dedicated host is applicable for software license which are tied up with physical HW**

![1601878644942](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601878644942.png)

### Network Service - VPC

<https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>

![1601879285371](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601879285371.png)

![1601879350387](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601879350387.png)

#### VPC Design

**AWS VPC can be created from /16 to /28 CIDR blocks. So we will get IP address 2(power 16) or 2 (Power of 32-28) IP address. we then reserve 5 address in each subnet which are Base Address/Network Address, Default Gateway/VPC Router, DNS, AWS Future reserve, Broadcast Address. IPV4 is 32 bit address.**

Here is a sample design,,,,

![1601880341504](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601880341504.png)

One IGW can be attached to one VPC only. They have Public and Private route table attached. Private route table attached to private Subnet and Public route table gets attached to public subnet.[1601880149181]![1601880169074](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601880169074.png)



## IAM

![1601885714078](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601885714078.png)

![1601885846192](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601885846192.png)

### IAM Details

![1601885954120](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601885954120.png)

![1601886024452](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886024452.png)

### IAM Authorization

![1601886126041](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886126041.png)

![1601886438206](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886438206.png)

![1601886487905](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886487905.png)

## Platform Services

![1601874486014](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874486014.png)

## Region and AZ

![1601874686915](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874686915.png)![1601874712490](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874712490.png)

## High Availability using multiple AZ

![1601874788123](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874788123.png)

## Services running Edge Location

![1601874913075](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601874913075.png)

Check www.calculator.aws.com for any billing estimation.

## Database

### RDS

![1601886896894](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601886896894.png)

![1601887016132](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887016132.png)

![1601887035413](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887035413.png)

**DB Creation steps**

- Create **Private Subnet group** for DB. Use here Private subnet during creation.
- Create Database. Need to choose template and configure credentials setting, We can create new security group during DB creation and attach with DB.

![1601887431091](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887431091.png)

![1601887448906](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887448906.png)

![1601887461857](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887461857.png)

![1601887482580](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887482580.png)



### Dynamo DB

**Completely managed by AWS. Every item will have its own attributes. Primary Key and sort Key are essentials for DDB.**

![1601887568895](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887568895.png)

**Read and Write capacity are must for DDB definition.**

![1601887757582](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601887757582.png)







## AWS Elasticity and management

![1601888659364](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601888659364.png)

![1601888680281](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601888680281.png)

### Application load balancer

**Works on layer 7 which is application OSI Layer. We always need to create atleast in two AZ which is ensured by AWS.**

![1601888790587](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601888790587.png)

### Network Load Balancer

**Works on layer 4 which is transport layer of OSI. **



![1601888886336](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601888886336.png)



**Which load balancer gives you better throughput??**

- Network load balancer because it works on layer 4 and connection to client does not need to move to layer 7 which is application layer. 

### Load balancer comparism

<https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html>

![1601889039562](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601889039562.png)

### Auto Scaling

![1601889668915](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601889668915.png)

![1601889693454](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601889693454.png)

## AWS Trusted Advisor

![1601889754230](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601889754230.png)

![1601889844264](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601889844264.png)

![1601890067839](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601890067839.png)

# AWS IOT

Video recording in https://www.loom.com/share/5f4455f651554252b3f41805f0c119d7

## IOT Components

![1601960055747](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960055747.png)



## IOT Device Gateway

![1601959865706](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601959865706.png)

## IOT Rule Engine

![1601959890260](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601959890260.png)

## IOT Device Shadow

It is like a dummy device.

![1601959930384](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601959930384.png)

## IOT Registry

It is like a database for all connected IOT device. This DB will have all metadata for all connected devices. It can scale to billions of devices.

![1601959993093](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601959993093.png)

## IOT Thing

Logical representation of a device.

![1601960248215](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960248215.png)![1601960284133](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960284133.png)

![1601960313048](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960313048.png)

## Device Security

![1601960507375](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960507375.png)

## Message Broker

![1601960555396](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960555396.png)

![1601960626086](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1601960626086.png)





# Automation with Boto 3 and Lambda 

## Introduction to Boto3

![image-20201015095401741](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015095401741.png)

Boto3 is the AWS SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. Boto provides an easy-to-use, object-oriented API, as well as low-level access to AWS services.

```sh
pip3 install boto3 --user
pip install awscli boto3 --upgrade --user
```

The `--upgrade` option tells `pip` to upgrade any requirements that are already installed. The `--user` option tells `pip` to install the program to a subdirectory of your user directory to avoid modifying libraries used by your operating system.

You may need to add the user directory to your `PATH`, for example, `~/Library/Python/3.7/bin`.

Run the following command at the terminal, and add it to your `.bashrc`, `.zshrc`, or other shell configuration file:

```
export PATH=~/Library/Python/3.7/bin:$PATH
```

### Configuring your AWS environment

Obtain your AWS access key and secret access key from the AWS Management Console. Run the following command:

```sh
aws configure
```

This sets up a text file that the AWS CLI and Boto3 libraries look at by default for your credentials: `~/.aws/credentials`.

The file should look like this:

```text
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

## Test Your Credentials

### AWS CLI

Run the following command:

```sh
aws sts get-caller-identity
```

The output should look like this:

```json
{
    "UserId": "AIDAJKLMNOPQRSTUVWXYZ",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/devuser"
}
```

### Boto3

Run `python3` interactively:

```sh
python3
```

Run the following commands:

```text
>>> import boto3
>>> sts = boto3.client('sts')
>>> sts.get_caller_identity()
```

The output should look like this:

```text
{'UserId': 'AIDAJKLMNOPQRSTUVWXYZ', 'Account': '123456789012', 'Arn': 'arn:aws:iam::123456789012:user/devuser', 'ResponseMetadata': {'RequestId': '3e310806-50c9-11e9-93ae-dbac86675630', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '3e310806-50c9-11e9-93ae-dbac86675630', 'content-type': 'text/xml', 'content-length': '404', 'date': 'Wed, 27 Mar 2019 19:48:06 GMT'}, 'RetryAttempts': 0}}
```

Quit using `exit()` or **Ctrl+D**:

```text
>>> exit()
```

## Stopping EC2 Instances Nightly

Our aim here is to stop the EC2 instance every night to reduce cost. This can be done for development and test EC2 instance to reduce cost.

In this diagram, we'll look at an effective cost-saving technique: shutting down EC2 instances on a nightly basis. If you consider a development team of around 130 people, each using `m4.large` instances, this can save you well over $2,000 per month in usage fees.

Download the source code for this lesson [here](https://github.com/linuxacademy/content-lambda-boto3/tree/master/EC2/Stopping-EC2-Instances-Nightly).

- First lambda is being called from cloud watch. This lambda is time bound one and is being iterating through all region to find out required EC2 instance to shut down. This lambda need to IAM execution role for shutting down EC2 instance and talk to cloud watch.

![image-20201015154744871](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015154744871.png)

## Backing Up EC2 Instances

we'll demonstrate an alternative to the EBS Lifecycle Manager by creating an EBS backup solution from scratch. This solution consists of a pair of Lambda functions: one to perform the EBS snapshots, and the other to prune stale snapshots.

- Lambda function scheduled daily to backup. 

![image-20201015162946311](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015162946311.png)

Here for the EC2 instance which needs to be backed up having a tag backup set to True.

![image-20201015163617232](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015163617232.png)

**Lambda Policy Roles**

![image-20201015195108606](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015195108606.png)



**Remember same logic can be achieved by EC2 Lifecycle manager which has some drawback. It takes 1 hr after policy creation to start. It is based on tag and if any of the tag is part of lifecycle policy then same tag cant be used for any other policy. All the old snapshot taken as part of EC2 lifecycle manager policy needs to be manually deleted. we can only create snapshot by lifecycle manager at every 12 or 24 hour only.**



![image-20201015163133831](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015163133831.png)

## Removing Unattached EBS Volumes

- Here volume should be for the account id

![image-20201015195859164](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015195859164.png)

Deleting detached EBS volumes on a regular basis can help lower your AWS bill. In this lesson, we'll demonstrate a technique for deleting unattached EBS volumes across regions with Lambda, Boto3, and a CloudWatch rule.

Download the full source code for this lesson [here](https://github.com/linuxacademy/content-lambda-boto3/tree/master/EC2/Removing-Unattached-EBS-Volumes).

Changing the root volume of an EC2 instance to persist:

```sh
aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --block-device-mappings file://mapping.json
```

JSON file (remember to replace the value for `DeviceName` with the correct value for your device name):

```json
[{
  "DeviceName": "/dev/xvda",
  "Ebs": {
    "DeleteOnTermination": false
  }
}]
```

## Deregistering Old AMIs

Deregistering old, unused AMIs on a regular basis can help lower your AWS bill. In this lesson, we'll demonstrate a technique for deregistering AMIs older than a certain age across regions with Lambda, Boto3, and a CloudWatch rule.

- Here AMI images should be owned by Owner

![image-20201015200339392](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015200339392.png)

Download the full source code for this lesson [here](https://github.com/linuxacademy/content-lambda-boto3/tree/master/EC2/Deregistering-Old-AMIs).

## AWS Instance Scheduler

The AWS Instance Scheduler is a solution that automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances.

![image-20201015200637492](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015200637492.png)

The Instance Scheduler leverages AWS resource tags and AWS Lambda to automatically stop and restart instances across multiple AWS regions and accounts on a customer-defined schedule. The solution is easy to deploy and can help reduce operational costs. For example, an organization can use the Instance Scheduler in a production environment to automatically stop instances every day outside of business hours. For customers who leave all of their instances running at full utilization, this solution can result in up to 70% cost savings for those instances that are only necessary during regular business hours (weekly utilization reduced from 168 hours to 50 hours).

### Deployment

Sign in to the AWS Management Console and click the button below to launch the AWS CloudFormation template.

[![Stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Faws-instance-scheduler%2Flatest%2Finstance-scheduler.template)

You can also [download the template](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/EC2/AWS-Instance-Scheduler/aws-instance-scheduler.json) as a starting point for your own implementation.

## Working with DynamoDB Tables

![image-20201015201440200](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015201440200.png)

- LSI needs to be created when DDB Created
- GSI can be created later of DDB creation

![image-20201015201735015](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015201735015.png)

**DDB Stream**

![image-20201015202002057](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015202002057.png)



### Installing Boto3 for Python 3 in Cloud9:

```
sudo pip-3.6 install boto3
```

### Clone the GitHub repository for this course:

```
git clone https://github.com/linuxacademy/content-lambda-boto3.git
```

### Boto3 DynamoDB documentation:

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

### Scheduling DynamoDB Backups

![1604493576629](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604493576629.png)

Additional Information and Resources

Make sure you are in the `us-east-1` region.

Refer to the following resources:

- Lambda execution role policy from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Scheduling-DynamoDB-Backups/lambda_execution_role.json) on GitHub
- Lambda function Python source code from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Scheduling-DynamoDB-Backups/lambda_function.py) on GitHub

## Simple Storage Service (S3)

### Resizing Images

we'll go over how to create a Lambda function that will automatically resize images uploaded to an S3 bucket.

![image-20201015202520463](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015202520463.png)

#### Pillow

https://pypi.org/project/Pillow/

Download the `Pillow-5.4.1-cp37-cp37m-manylinux1_x86_64.whl` file, and extract the wheel file in the same folder as `lambda_handler.py`:

```sh
unzip Pillow-5.4.1-cp37-cp37m-manylinux1_x86_64.whl
```

The `Pillow-5.4.1.dist-info` isn't needed:

```sh
rm -rf Pillow-5.4.1.dist-info
```

Zip the `PIL` directory along with `lambda_handler.py`:

```sh
zip -r9 lambda.zip PIL lambda_handler.py
```

Upload `lambda.zip` to AWS Lambda.

### Importing CSV Files into DynamoDB

we'll talk about how to bulk import data from CSV files into DynamoDB. We will create a trigger from an S3 bucket, invoking a Lambda function on upload. The Lambda function will parse the CSV data, and using Boto3, import this data into DynamoDB.

- Insert into DDB happening in batch
- Lambda function is getting triggered whenever file gets uploaded into S3

![image-20201015202804851](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015202804851.png)

### Transcribing Audio

we will learn how to automate Amazon Transcribe, parsing out its raw JSON data and storing transcription results in S3. This solution consists of two Lambda functions and a CloudWatch event.

- Cloudwatch rule will be created which will have service name “Transcribe” and Event Type will be “Transcribe Job State Change” and status to “COMPLETED”.

![image-20201015204141280](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015204141280.png)

![image-20201015202950746](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015202950746.png)

**TranscribeAudio Lambda**

![image-20201015203630668](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015203630668.png)

**ParseTranscription Lambda**

![image-20201015203857075](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015203857075.png)

**Cloud Watch Rule**

![image-20201015204301327](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015204301327.png)

### Detecting Faces with Rekognition

 we will learn how to build our own facial recognition service by combining the capabilities of Amazon Rekognition with Lambda, S3, and DynamoDB.

![image-20201015204718954](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015204718954.png)

## Simple Queue Service (SQS)

In this lesson, we'll look at a common use case where we invoke a Lambda function that is triggered by SQS. Whenever a message is placed in the queue, the Lambda function will be triggered, reading the contents of that message and inserting its data as a record into DynamoDB.

### Create a DynamoDB Table

```sh
aws dynamodb create-table --table-name Message \
  --attribute-definitions AttributeName=MessageId,AttributeType=S \
  --key-schema AttributeName=MessageId,KeyType=HASH \
  --billing-mode=PAY_PER_REQUEST
```

### Create an SQS Queue

```sh
aws sqs create-queue --queue-name Messages
```

### Sending Messages to SQS

Run the provided script `send_message.py` to send messages to SQS.

**Example**: Send a message containing random text to the `Messages` queue every 0.1 second (10 messages per second):

```
./send_message.py -q Messages -i 0.1
```

Press **Ctrl+C** to quit.

### Lesson Links

Send Messages to SQS: https://github.com/linuxacademy/content-lambda-boto3/tree/master/SQS/Triggering-Lambda-from-SQS

Faker: https://pypi.org/project/Faker/

![image-20201015205408637](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015205408637.png)





## Automating Security

### Enabling VPC Flow Logs

[VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) enable you to capture information about the IP traffic going to and from network interfaces in your VPC.

By default, VPC flow logs are not enabled. However, in our scenario, let's say you have a policy that requires they be enabled for any new VPC that gets created in your account.

In this lesson, we will automate the creation of VPC flow logs whenever a new VPC is created.

- `lambda_function.py` creates VPC flow logs for the VPC ID in the event.
- `event-pattern.json` is the CloudWatch Rule event pattern for monitoring the `CreateVpc` API call.
- `test-event.json` is a sample CloudTrail event that can be used with the Lambda function, as it contains the VPC ID.

![image-20201015205811346](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015205811346.png)

```
#### Create an IAM Role with Permission to Log to CloudWatch Logs

1. Allow the VPC Flow Logs service to assume this role:

   ```sh
   aws iam create-role --role-name VPCFlowLogsRole --assume-role-policy-document file://trust-policy.json
```

   Note the ARN for `VPCFlowLogsRole`.

   **Example:** `arn:aws:iam::123456789012:role/VPCFlowLogsRole`

2. Grant this role permission to access CloudWatch Logs:

   ```sh
   aws iam put-role-policy --role-name VPCFlowLogsRole --policy-name VPCFlowLogsPolicy --policy-document file://vpc-flow-logs-iam-role.json
   ```

#### Create the Lambda Function

- Name: **EnableVPCFlowLogs**
- Runtime: **Python 3.7**
- Role: **Create a custom role** (use `lambda_execution_role.json`)
- Code: `lambda_function.py`

#### Create a CloudWatch Event Rule to Trigger Lambda

1. Select **Event Pattern**.

   - Service Name: **EC2**
   - Event Type: **AWS API Call via CloudTrail**
   - Specific operation(s): **CreateVpc**

2. Event Pattern:

   ```json
   {
       "source": [
           "aws.ec2"
       ],
       "detail-type": [
           "AWS API Call via CloudTrail"
       ],
       "detail": {
           "eventSource": [
               "ec2.amazonaws.com"
           ],
           "eventName": [
               "CreateVpc"
           ]
       }
   }
   ```

3. Click **Add target** and select the **EnableVpcFlowLogs** Lambda function.

4. Click **Configure details**.

#### Create a New VPC

1. Run the following command:

   ```sh
   aws ec2 create-vpc --cidr-block 172.20.0.0/16 --region us-east-2`
   ```

2. Wait up to a minute for the CloudWatch rule to invoke the Lambda function.
```

### Responding to Invalid SSH Logins

![image-20201015210340829](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015210340829.png)



In this lesson, we'll explore a real-world scenario in which an EC2 instance is experiencing multiple failed SSH logins, and we want to automatically take the instance offline in response to this potential security event.

Use the Web Server Log Group and the Invalid SSH Login metric filter to trigger a CloudWatch alarm set for 2 data points within 1 minute.

This alarm should publish to an alarm notification SNS topic and send you an email as well as trigger the Lambda function to stop the instance.

```
#### Configure the EC2 Instance

- The EC2 instance must have an IAM role that can communicate with both CloudWatch and Systems Manager.

##### Create an IAM Instance Role

1. Select **IAM > Create Role > AWS Service > EC2 > Next: Permissions**.
2. Select the **CloudWatchAgentAdminPolicy** managed policy.
3. Select the **AmazonSSMManagedInstanceCore** managed policy.
4. Name the role "CloudWatchAgentAdminRole".

##### Launch the EC2 Instance

1. Select **Amazon Linux 2**.
2. Create or select a security group with SSH (port 22) open to the public (`0.0.0.0/0`).

##### Attach the IAM Role to the Instance

1. Assign the *CloudWatchAgentAdminRole* IAM role to the EC2 instance.

##### Install CloudWatch Agent using Systems Manager

- Run command: `AWS-ConfigureAWSPackage`
- Action: **Install**
- Name: **AmazonCloudWatchAgent**

##### Configure the CloudWatch Agent

1. Run the CloudWatch Agent Configuration Wizard.

2. Create a new session using SSM Session Manager.

   ```sh
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
   ```

   **Note: Do not select CollectD, unless you already installed it using `sudo yum install collectd`.**

3. Specify `/var/log/secure` at the "Do you want to monitor any log files?" prompt.

##### Validate the Configuration

```
​```sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
​```
​```

##### Create an SNS Topic

- The CloudWatch Alarm will notify this topic, and the topic will trigger the Lambda function.
- Topic name: **AlarmNotificationTopic**

##### Configure the CloudWatch Alarm

##### Add a Metric Filter to the Web Server Log Group

1. Click **Secure** log group.

2. Click **Create metric filter**.

   Filter pattern: `[Mon, day, timestamp, ip, id, status = Invalid*]`

3. Click **Test pattern**.

4. Click **Assign metric**.

   - Filter name: `InvalidSSHLogin`
   - Metric namespace: `SSH`
   - Metric name: `InvalidSSHLogin`

5. Click **Create filter**.

##### Create Alarm

- Metric filter: SSH/InvalidSSHLogin

1. Click **Create alarm**.
   - Name: **InvalidSSHLoginAlarm**
   - Description: `Invalid login attempts >2 in 1 min for instance `*<append instance ID>*

**Note: The description is critical, as the instance ID at the end is used by the Lambda function to stop the instance.**

Whenever `InvalidSSHLogin` >= `2` for 1 out of 1 datapoints

##### Subscribe to the SNS Topic

1. Select **AlarmNotificationTopic** and click **Create alarm**.

##### Create IAM Role for Lambda Function

1. Create the role `LambdaStopInstances` using policy `lambda_execution_role.json`.

##### Create Lambda function

- Name: **StopInstance**
- Role: **StopInstancesRole**

##### Trigger Lambda from SNS

1. Select **Trigger > SNS > AlarmNotificationTopic**.

##### Trigger the CloudWatch Alarm

1. Make 3 invalid SSH login attempts within 2 minutes.
2. Verify that the `secure` log contains the `Invalid user` string.
3. Verify that the CloudWatch alarm is set.
4. Verify that the CloudWatch Log for the Lambda function ran.
5. Verify that the EC2 instance is stopped.
```



### Making Public S3 Objects Private

![image-20201015211251443](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015211251443.png)

```
Create an S3 Bucket
Create the S3 bucket:

aws s3 mb s3://123456789012-everything-must-be-private
aws s3 mb s3://123456789012-bucket-for-my-object-level-s3-trail
Apply a bucket policy:

aws s3api put-bucket-policy \
--bucket 123456789012-bucket-for-my-object-level-s3-trail \
--policy file://bucket_policy.json
Create a CloudTrail Trail and Start Logging

Run the following command:

aws cloudtrail create-trail \
--name my-object-level-s3-trail \
--s3-bucket-name 123456789012-bucket-for-my-object-level-s3-trail

aws cloudtrail start-logging --name my-object-level-s3-trail

Create the event selectors:

aws cloudtrail put-event-selectors \
--trail-name my-object-level-s3-trail \
--event-selectors file://event_selectors.json
Create an IAM Execution Role for Lambda
Create the IAM role:

aws iam create-role \
--role-name AllowLogsAndS3ACL \
--assume-role-policy-document file://trust_policy.json
Define the access policy:

aws iam put-role-policy \
--role-name AllowLogsAndS3ACL \
--policy-name AllowLogsAndS3ACL \
--policy-document file://access_policy.json

Create a Lambda Function
For a PutObjectAcl API event, the function gets the bucket and key name from the event. If the object is not private, then it makes the object private by making a PutObjectAcl call.

Zip the Lambda function:

zip -r9 RemediateObjectACL.zip lambda_function.py
Create the Lambda function:

aws lambda create-function \
--function-name RemediateObjectACL \
--zip-file fileb://RemediateObjectACL.zip \
--role arn:aws:iam::123456789012:role/AllowLogsAndS3ACL \
--handler lambda_function.lambda_handler \
--runtime python3.7 \
--environment Variables={BUCKET_NAME=123456789012-everything-must-be-private}

Allow CloudWatch events to invoke Lambda:

aws lambda add-permission \
--function-name RemediateObjectACL \
--statement-id AllowCloudWatchEventsToInvoke \
--action 'lambda:InvokeFunction' \
--principal events.amazonaws.com \
--source-arn arn:aws:events:us-east-2:123456789012:rule/S3ObjectACLAutoRemediate

Create a CloudWatch Events Rule
Create the rule:

aws events put-rule \
--name S3ObjectACLAutoRemediate \
--event-pattern file://event_pattern.json
Set the Lambda function as the target:

aws events put-targets \
--rule S3ObjectACLAutoRemediate \
--targets Id=1,Arn=arn:aws:lambda:us-east-2:123456789012:function:RemediateObjectACL
Testing
Run the following command:

aws s3api put-object \
--bucket 123456789012-everything-must-be-private \
--key MyPersonalInfo

aws s3api get-object-acl \
--bucket 123456789012-everything-must-be-private \
--key MyPersonalInfo
The above should return 1 grantee, the owner (you). This indicates that the object is private.

Add public read access, violating our policy:

aws s3api put-object-acl \
--bucket 123456789012-everything-must-be-private \
--key MyPersonalInfo \
--acl public-read
Quickly check access again:

aws s3api get-object-acl \
--bucket 123456789012-everything-must-be-private \
--key MyPersonalInfo
You will see another grantee, allowing everyone to read the object:

{
  "Grantee": {
    "Type": "Group",
    "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
  },
  "Permission": "READ"
}
Describe the ACL again, and you'll see the Lambda function has removed public read access. Verify this in CloudWatch Logs.

Cleanup
aws events remove-targets --rule S3ObjectACLAutoRemediate --ids "1"
aws events delete-rule --name S3ObjectACLAutoRemediate
aws lambda delete-function --function-name RemediateObjectACL
aws iam delete-role-policy --role-name AllowLogsAndS3ACL --policy-name AllowLogsAndS3ACL
aws iam delete-role --role-name AllowLogsAndS3ACL
aws cloudtrail delete-trail --name my-object-level-s3-trail
aws s3 rb s3://123456789012-bucket-for-my-object-level-s3-trail --force
aws s3 rb s3://123456789012-everything-must-be-private --force
```

### Automating Resource Tagging

how to automate the tagging of EC2 instances and their corresponding resources using a Lambda function with CloudTrail and CloudWatch. The function will ensure that users can work only on those resources that they have created based on resource tags. This is enforced via an IAM policy.

Try working with EC2 instances that are untagged or owned by other users, and observe the "Access Denied" errors.

**What Next?**

- Now that you know you can tag resources with a Lambda function in response to events, you can apply the same logic to other resources such as RDS databases or S3 buckets. With resource groups, each user can focus on just their resources, and the IAM policy provided in this lesson ensures that no unauthorized action is possible on someone else's instance.

- Additionally, tags are useful in custom billing reports to project costs and determine how much money each individual owner is spending. You can activate the Owner tag from the Cost Allocation Tags section of your billing console to include it in your detailed billing reports. For more information, see Applying Tags.

![image-20201015211815901](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015211815901.png)



```
In this lesson, we'll learn how to automate the tagging of EC2 instances and their corresponding resources using a Lambda function with CloudTrail and CloudWatch. The function will ensure that users can work only on those resources that they have created based on resource tags. This is enforced via an IAM policy.

Create the IAM Policy
This policy allows Start/Stop/Reboot/Terminate for EC2 instances where the tag Owner matches the current requester's user ID.

Run the following command:

aws iam create-policy \
--policy-name TagBasedEC2RestrictionsPolicy \
--policy-document file://TagBasedEC2RestrictionsPolicy.json
Note the policy ARN.

Attach IAM Policy to Group
Create a group called developers:

aws iam create-group --group-name developers
Attach the policy to the group:

aws iam attach-group-policy \
--policy-arn arn:aws:iam::123456789012:policy/TagBasedEC2RestrictionsPolicy \
--group-name developers
Create an IAM Role for the Lambda Function
Create the IAM role:

aws iam create-role \
--role-name LambdaAllowTaggingEC2Role \
--assume-role-policy-document file://trust_policy.json
Define the access policy:

aws iam put-role-policy \
--role-name LambdaAllowTaggingEC2Role \
--policy-name LambdaAllowTaggingEC2Policy \
--policy-document file://access_policy.json
Create the Lambda Function
Create the function TagEC2Resources.
Create a CloudWatch Rule
Create the rule:

aws events put-rule \
--name AutoTagResources \
--event-pattern file://event_pattern.json
Set the Lambda function as the target:

aws events put-targets \
--rule AutoTagResources \
--targets Id=1,Arn=arn:aws:lambda:us-east-2:123456789012:function:TagEC2Resources
Create an EC2 Instance as User
Create an EC2 instance as an administrative/root user. Observe the Owner tag.


```

### Rotating IAM Access Keys

![image-20201015212104700](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015212104700.png)

We will create a Lambda function that revokes user access keys periodically to enforce rotation and mitigate risk.

The Lambda function will perform the following:

- Collect IAM users using pagination
- Scan each user for existing IAM access keys older than 90 days
- Deactivate the keys
- Send email alerts to the administrator

Scheduled CloudWatch Rule:

- Triggers the Lambda function to run (e.g., weekly)

![image-20201015212245040](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015212245040.png)![image-20201015212418025](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015212418025.png)

Amazon Simple Email Service (Amazon SES)

Be sure to use an [SES-verified email address](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) to ensure proper delivery of emails.

SES API endpoints are not available in all regions. Go [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region) for a list of supported endpoints.

## AWS Config

we'll create a custom AWS Config rule to find outdated EC2 instance types. Moving off these old instance types can help us reduce costs and improve performance.



![image-20201015212530398](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015212530398.png)



```
Create a Lambda Function
Create a role called "LambdaCheckInstanceTypeRole" and specify AWS Config Rules permissions as the policy template.

Create the Lambda function CheckInstanceType. Note the ARN for the next steps.

Create an AWS Config Rule
In the AWS Config console, select Rules, then click the Add rule button.
Next, click Add custom rule.
Name: DesiredInstanceTypes.
Description: Checks that all EC2 instances are of the type specified.
AWS Lambda function ARN: (Copy and paste from the Lambda Console. It should look something like this: arn:aws:lambda:us-east-1:123456789012:function:CheckInstanceType)
Trigger type: Configuration changes
Scope of changes: Resources
Resources: EC2: Instance
Rule parameters:
Key: desiredInstanceType
Value: t2.micro, or a comma-separated list (e.g, t2.micro,t3.micro). Note: Any values not in this list will evaluate to noncompliant.
Click Save.

```

## Building a Contact Form with API Gateway and SES

This lesson demonstrates a web page with a typical contact form. Using API Gateway and a Lambda function as a backend for this form, we will send the form post contents via email using SES, and also write the contact data to DynamoDB.

### Source code for this lesson

https://github.com/linuxacademy/content-lambda-boto3/tree/master/WebApps/Contact-Form

### Lambda function

Create a function named **ContactEmail**.

### API Gateway

Create an API named **ContactEmailAPI**.

### Create Method

1. Select **POST** and check the check mark.
   - *Integration Type*: Lambda Function
   - *Use Lambda Proxy Integration*: Checked (stores request data in `event`)
   - *Lambda region*: Same region as Lambda function
   - *Lambda function\*: **ContactEmail**

### Enable CORS

1. Select the **POST** method
2. Under **Actions**, select **Enable CORS**
3. Leave the default options and click on **Enable CORS and replace existing CORS headers**
4. Click **Yes, replace existing values**

### Deploy API

1. Under **Actions**, select **Deploy API**
   - Deployment stage: **[New stage]**
   - Stage name: **prod**
2. Note the **Invoke URL** and update `form.js`.

### Test locally

```sh
cd Contact-Form
python3 -m http.server
```

Navigate to [http://localhost:8000](http://localhost:8000/)

## Working with Lambda Layers

Lambda layers allow functions to easily share code. Upload a layer once, and reference it from any function. Layers can contain anything (dependencies, data, configuration files, etc.) and can be shared publicly or with specific AWS accounts. Collect common components in a ZIP file and upload as a Lambda layer. A function may reference up to 5 layers.

![image-20201015213134408](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015213134408.png)

```

```

1. Create a new virtual environment using Pipenv and install the required libraries:

   ```sh
   pipenv --python 3.7
   pipenv shell
   pipenv install requests
   ```
```

   Note: If you are on macOS, you can install Pipenv using Homebrew:

   ```sh
   brew install pipenv
```

   On Amazon Linux, or another environment, you can install using `pip`:

   ```sh
   pip3 install pipenv --user
   ```

2. Create the ZIP deployment package:

   ```sh
   PY_DIR='build/python/lib/python3.7/site-packages'
   # Create temporary build directory
   mkdir -p $PY_DIR
   # Generate requirements file
   pipenv lock -r > requirements.txt
   # Install packages into the target directory
   pip install -r requirements.txt --no-deps -t $PY_DIR
   cd build
   # Zip files
   zip -r ../requests_layer.zip .
   cd ..
   # Remove temporary directory
   rm -r build
   ```

3. Create the Lambda layer.

   ```sh
   aws lambda publish-layer-version \
   --layer-name requests \
   --compatible-runtimes python3.7 \
   --zip-file fileb://requests_layer.zip
   ```

   Note the `LayerArn` in the output.

## Automating CodeCommit Change Notifications

we'll demonstrate how to receive detailed email notifications about file changes and commit messages when a code update is pushed to CodeCommit. A code reviewer may subscribe to the SNS topic and recieve updates for any changes.

![image-20201015213545371](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015213545371.png)

**Create the CodeCommit Repository**

```sh
aws codecommit create-repository --repository-name ChangeNotification
```

Note the `cloneUrlHttp` and `Arn` values in the response.

**Create and Subscribe to the SNS Topic**

```sh
aws sns create-topic --name CodeCommitChangeNotification

aws sns subscribe \
--topic-arn arn:aws:sns:us-east-1:123456789012:CodeCommitChangeNotification \
--protocol email \
--notification-endpoint my-email@example.com
```

**Create an IAM Lambda Execution Role**

1. Add `AWSLambdaBasicExecutionRole`.

2. Add the following policy: `LambdaCodeCommitSnsPolicy`.

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Effect": "Allow",
           "Action": [
           "codecommit:*",
           "sns:*"
           ],
           "Resource": "*"
       }]
   }
   ```

**Create the Lambda Function**

1. Name it "CodeCommitChangeNotification".

2. Set the following environment variables:

   `REPOSITORY_NAME` = `ChangeNotification`

   `SNS_TOPIC_ARN` = `arn:aws:sns:us-east-1:123456789012:CodeCommitChangeNotification`

**Create the CloudWatch Event Rule**

This rule will detect branch or repository changes.

1. Choose **Event Pattern**.

   - Service Name: **CodeCommit**
   - Event Type: **CodeCommit Repository State Change**

2. Select **Specific resource(s) by ARN**, and enter the CodeCommit Repository ARN.

3. Select the **referenceCreated** and **referenceUpdated** events.

   Event Pattern:

   ```json
   {
   "source": [
       "aws.codecommit"
   ],
   "detail-type": [
       "CodeCommit Repository State Change"
   ],
   "resources": [
       "arn:aws:codecommit:us-east-1:123456789012:ChangeNotification"
   ]
   }
   ```

4. Under *Target*, select the **CodeCommitChangeNotification** function.

**Commit a Change**

1. Create and commit a file.
2. Edit the file and commit it.

## Publishing Custom Metrics from Lambda

CloudWatch custom metrics are coded into your applications and can be used to report custom business and operational data. In this lesson, we will learn how to publish custom CloudWatch metric data from a Lambda function, reporting several key performance indicators (KPIs). These data can help us monitor progress toward sales, marketing, and customer service goals.

![image-20201015213808847](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015213808847.png)

Install the demo app using the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/). You can find the instructions for installing the AWS SAM CLI [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

**Create the Lambda Deployment Package**

1. Run the following command:

   ```
   cd shopping-cart-app
   ```

2. Create an S3 bucket in the location where you want to save the packaged code. (If you want to use an existing S3 bucket, skip this step.)

   ```sh
   aws s3 mb s3://123456789012-shopping-cart-app
   ```

3. Create the deployment artifacts with dependencies.

   ```sh
   sam build
   ```

4. Create the Lambda function deployment package by running the following `package` AWS SAM CLI command at the command prompt:

   ```sh
   sam package \
       --output-template-file packaged.yaml \
       --s3-bucket 123456789012-shopping-cart-app
   ```

5. In the AWS SAM CLI, use the `deploy` command to deploy all of the resources that you defined in the template.

   ```sh
   sam deploy \
       --template-file packaged.yaml \
       --stack-name shopping-cart-app \
       --capabilities CAPABILITY_IAM
   ```

**Locate the API Gateway Endpoint URLs**

1. Open the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation.
2. Choose the AWS CloudFormation stack that you created in the preceding step from the list.
3. Under **Outputs**, note the API Gateway endpoint URLs.
4. Browse each one and observe the JSON responses.

**Generate Traffic**

Using the API Gateway endpoint URLs from the previous step, generate traffic against each of these endpoints.

1. Run an HTTP testing tool like [vegeta](https://github.com/tsenart/vegeta) to generate traffic to your API gateway endpoints.

2. Modify `URLs.txt` to use the endpoint URLs in your account.

3. Run a test for 60 minutes.

   ```sh
   cat URLS.txt | vegeta attack -duration=60m | tee results.bin | vegeta report
   ```

**View Custom Metrics**

You may view custom metric data while a load test is in progress.

1. Open the CloudWatch Console at https://console.aws.amazon.com/cloudwatch.
2. Navigate to **Metrics**.
3. Under **All metrics**, select **ShoppingCartApp**.
4. Select **Metrics with no dimensions**.
5. Select **ItemsAddedToCart**, **OrderTotal**, and **ViewProduct**.

## Tracing with X-Ray

we're going to learn about tracing our application with AWS X-Ray.

We are going to deploy a sample [Flask](http://flask.pocoo.org/) application that is instrumented with the X-Ray SDK, make some sample requests, and then examine the traces and service maps in the AWS Management Console.

Zappa GitHub Repo: https://github.com/Miserlou/Zappa

![image-20201015213942916](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015213942916.png)



**Create a DynamoDB Table**

1. Create a table called `Flask` with a primary partition key called `key`.

   ```sh
   aws dynamodb create-table --table-name Flask \
     --attribute-definitions AttributeName=key,AttributeType=S \
     --key-schema AttributeName=key,KeyType=HASH \
     --billing-mode=PAY_PER_REQUEST
   ```

**Configure [Zappa](https://github.com/Miserlou/Zappa)**

1. Run the following command:

   ```sh
   cd example
   pipenv --python 3.7
   pipenv shell
   pipenv install aws-xray-sdk flask zappa requests
   pipenv lock -r > requirements.txt
   zappa init
   ```

2. Add the following property to `zappa_settings.json`:

   ```json
   "xray_tracing": true
   ```

3. Deploy the application.

   ```sh
   zappa deploy
   ```

**Enable X-Ray Tracing for API Gateway**

In this step, we will interact with the API Gateway Console to enable X-Ray tracing.

1. Sign in to the AWS Management Console and open the API Gateway Console at https://console\.aws\.amazon\.com/apigateway/.
2. Select your API (e.g., `example-dev`).
3. Select **Stages**.
4. Choose the name of your deployment stage (e.g., `dev`).
5. On the **Logs/Tracing** tab, select the **Enable X-Ray Tracing** box.
6. Click **Save Changes**.
7. Navigate to the endpoint in your browse

## Creating Slack Notifications for CloudWatch Alarms

![image-20201015214218132](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201015214218132.png)

**Configure Webhooks in Slack**

1. Create a Slack app: https://api.slack.com/apps/new

2. Search for and select **Incoming Webhooks**.

3. Set **Activate Incoming Webhooks** to **On**.

4. Select **Add New Webhook to Workspace**.

5. Choose the default channel where messages will be sent and click **Authorize**.

6. Note the webhook URL from the **Webhook URLs for Your Workspace** section. For example: `https://hooks.slack.com/services/T0HABCGK/BDEFG93SS/BeBSKJHDHmWwyv2SYV4apv1O`

   ```sh
   WEBHOOK_URL=https://hooks.slack.com/services/T0HABCGK/BDEFG93SS/BeBSKJHDHmWwyv2SYV4apv1O
   ```

7. Test the webhook:

   ```sh
   curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' $WEBHOOK_URL
   ```

**Create an SNS Topic**

```sh
aws sns create-topic --name high-cpu-alarm
```

Note the **TopicArn**.

**Create a CloudWatch Alarm**

1. Send notifications to the SNS topic when CPU utilization > 40%:

   ```sh
   aws cloudwatch put-metric-alarm \
       --alarm-name cpu-mon \
       --alarm-description "Alarm when CPU exceeds 40%" \
       --metric-name CPUUtilization \
       --namespace AWS/EC2 \
       --statistic Average \
       --period 60 \
       --evaluation-periods 1 \
       --threshold 40 \
       --comparison-operator GreaterThanThreshold \
       --dimensions Name=InstanceId,Value=i-12345678901234567 \
       --alarm-actions arn:aws:sns:us-east-1:123456789012:high-cpu-alarm \
       --unit Percent
   ```

**Create an SSM Parameter**

```sh
aws ssm put-parameter --cli-input-json '{"Type": "SecureString", "KeyId": "alias/aws/ssm", "Name": "SlackWebHookURL", "Value": "'"$WEBHOOK_URL"'"}'
```

**Create a Lambda Execution Role**

1. Attach the following managed policies:
   - AmazonSSMFullAccess
   - AWSLambdaBasicExecutionRole

**Create a Lambda Function**

1. Use the SNS topic as a trigger.

**Stress the CPU**

```sh
# Install Extra Packages for Enterprise Linux
sudo amazon-linux-extras install epel
# Install stress
sudo yum install -y stress
# Beat it up for 5 mins
stress --cpu 2 --timeout 300s
```

# Cloud watch and AWX X-Ray Logging

![image-20201016112148967](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112148967.png)![image-20201016112208252](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112208252.png)

## Cloud Watch Built in Metrices

![image-20201016112305562](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112305562.png)

![image-20201016112441336](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112441336.png)

## Cloudwatch Logs

![1603734277060](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1603734277060.png)



![image-20201016151341577](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016151341577.png)



![image-20201016112637546](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112637546.png)

## Cloud Watch Embedding Metrices

![image-20201016112924993](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016112924993.png)

![image-20201016113102511](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113102511.png)

![image-20201016113155504](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113155504.png)

## AWS X-Ray tracing

![image-20201016113319170](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113319170.png)

![image-20201016113522007](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113522007.png)

## Cloud Watch Service Lens

![image-20201016113630853](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113630853.png)

![image-20201016113716213](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016113716213.png)

## Troubleshooting Flow

![image-20201016114126351](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016114126351.png)

## FAQ

- Can we feed data from cloud watch? we have subscription filter.

## Lambda Extension

- Extended during initializing the container
- 

# Infrastructure as Code(IAS)

![image-20201016120421848](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016120421848.png)

![image-20201016120505717](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016120505717.png)

![image-20201016120524610](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016120524610.png)

# Step Functions

- Encapsulate error logic and retry logic
- cron is a time based job scheduler
- 

![image-20201016141737721](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016141737721.png)

![image-20201016142119836](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016142119836.png)

**Lets see how we can manage metrices?**

![image-20201016142156416](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016142156416.png)![image-20201016142559050](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016142559050.png)![image-20201016142743021](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016142743021.png)

## Push Event Architecture

**We use Event Bridge instead of cron job..** This is a push event architecture…

![image-20201016143202329](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016143202329.png)

![image-20201016143245561](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\image-20201016143245561.png)





# Re-Invent 2020

![1606841751783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606841751783.png)

![1606842497745](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606842497745.png)

[New for AWS Lambda – 1ms Billing Granularity Adds Cost Savings](http://feedproxy.google.com/~r/AmazonWebServicesBlog/~3/-rbrFFJWnzc/)



![1606842550642](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606842550642.png)

[Preview: AWS Proton – Automated Management for Container and Serverless Deployments | Amazon Web Services](http://feedproxy.google.com/~r/AmazonWebServicesBlog/~3/7A6FEfOsEW4/)

[Preview: AWS Proton – Automated Management for Container and Serverless Deployments](http://feedproxy.google.com/~r/AmazonWebServicesBlog/~3/7A6FEfOsEW4/)

![1606842597783](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606842597783.png)

[EC2 Update – D3 / D3en Dense Storage Instances](http://feedproxy.google.com/~r/AmazonWebServicesBlog/~3/03PiOf7Ih0s/)

[Announcing Amazon EC2 Mac instances for macOS](https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-ec2-mac-instances-for-macos/)



# AWS Pricing Model

![1600679489791](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1600679489791.png)

AWS provides several tools to help customers estimate and manage costs. In this lesson, we will review several of these tools, including the TCO calculator, simple calculator, and Cost Explorer.

![im](https://www.anchor.com.au/wp-content/uploads/2016/07/aws-cost-modesl.jpg)

# Application Services for Associate AWS Solution Architects

This my notes from LA course https://linuxacademy.com/cp/modules/view/id/600

## Business Problem

As a solutions architect, we have been tasked with 10 requirements from Scuba Syndrome.

In our first course, Designing Resilient Architectures for Associate AWS Solutions Architects, we completed the first two requirements for Scuba Syndrome:

1. Create a development account and a production account along with an AWS organization.
2. Create a new security account, so we have a total of three AWS accounts.

In the second supporting course, we completed four more requirements:

1. Build a multi-tier VPC.
2. Create a VPC peering connection.
3. Create a WordPress blog.
4. Review connectivity options.

In the third course, we completed one more requirement:

1. Review the storage options available in AWS.

In the fourth course, we completed another requirement:

1. Review ways to add high availability and scalability to our website.

![1610980518588](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610980518588.png)

## Application, Analytics, and Operations

### Simple Queue Service (SQS) Overview

![1610981657850](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610981657850.png)

![1610981740723](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610981740723.png)

**Once we read the message from SQS, then message will become invisible from SQS foe visibility time-out and then it will become available again into SQS once visibilitytimeout is over. So ideally once we have read the message from SQS then we should delete from queue in order to avoid duplicate processing.**

![1610981984977](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610981984977.png)

We have **two different types of SQS** and they have quite significant differences among them.

![1610982121096](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610982121096.png)

Basic Advantage of SQS are:

![1610982187076](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610982187076.png)

## Simple Notification Service (SNS) Overview

a public AWS service that's highly available, durable, and secure pub/sub messaging service. Since it's a public service, you need network connectivity to ensure it's accessible.

![1610985367151](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610985367151.png)

**SNS Key points**

- Encryption

  - Enable/Disable

- Access Policy

  - Basic

    - Publisher
      - Everyone
      - Owner
      - Only specified AWS accounts
    - Subscriber
      - Everyone
      - Owner
      - Only specified AWS accounts
      - Only requesters with certain Endpoints

  - Advanced

    

- Delivery Retry Policy (Optional)

  - Number retry
  - retry interval
  - maximum delay
  - min delay retries
  - max delay retries
  - retry backoff function

- Delivery status logging (Optional)

  - logging status can be to
    - Lambda
    - SQS
    - HTTP/S
    - Platform Application endpoint

- IAM Role

- Tags (Optional)

![1610987328557](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610987328557.png)

## Step Functions Overview

Step Functions — a product that lets you build long-running serverless workflow-based applications within AWS and that integrates with many AWS services. **Used long running serverless flow.**

![1610987607255](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610987607255.png)

Following are readily available state function templates available to start with..

![1610988378203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988378203.png)

## Elastic Transcoder Overview

 Elastic Transcoder — a service that allows you to convert your media files from one format to another. Popular for delivering media files to mobile devices. 

![1610988593039](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988593039.png)

It needs a pipeline whereby we need to define from which bucket the Transcoder will read for processing. ![1610988722248](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988722248.png)![1610988756044](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988756044.png)![1610988797399](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988797399.png)![1610988818612](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988818612.png)

**Then, we need to define Jobs with above parameters. Job can take source files and generate one or more destination file.**

![1610988864496](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610988864496.png)

## Athena vs. Redshift

Athena uses **Schema on read** and during query of S3 buckets, we need to define the schema to use and it will then parse the data as per schema. So like traditional, DB whereby we first need to manipulate the data as per schema, is not required here in Athena.

Athena uses schema on read. **we can define columns, fields etc but schema is not persistent. It applies only when we read**.

![1610989181971](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1610989181971.png)

Redshift is a column based and petabyte scale data warehouse. It is cluster based architecture with leader node and compute node.

![1611118174607](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611118174607.png)

## Elastic MapReduce (EMR) Overview

EMR will most likely not heavily feature on the certification exam, but it is important to know what it is to help you identify correct answers.

It is cluster based product. ![1611118297952](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611118297952.png)![1611118369038](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611118369038.png)

## Difference between EMR and Athena

![1611118445685](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611118445685.png)![1611122855274](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611122855274.png)

## Kinesis Overview

![1611122939750](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611122939750.png)

![1611123120524](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611123120524.png)

**Kinesis Firehose allows us for data transformation and push into S3. Its source can be Kinesis data stream or directly put or other sources.**

![1611123409730](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611123409730.png)



## Amazon MQ Overview

![1611123724411](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611123724411.png)

## Securing Your Application Tiers

![1611123949648](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611123949648.png)

## Scaling EC2 Using SQS

In this scenario, you're a solutions architect at an e-commerce firm. The company runs flash sales from time to time, and when there's a **spike** in orders, the fulfillment backend can struggle to meet demand. **One way to solve the problem is to overprovision EC2 instances in the fulfillment system to provide headroom to process all the orders**. However, this can be very costly, since you'll have unused capacity when the traffic subsides. What if there's a better way? Well, there is, and this is the problem you'll solve here. In this lab, you will learn to **create Auto Scaling rules for EC2 based on the number of messages in an SQS queue**.

- Create CloudWatch Alarms
  - Create scale-out and scale-in alarms using the SQS `ApproximateNumberOfMessagesVisible` metric.
- Create Simple Scaling Policies
  - Create scale-out and scale-in policies using the two CloudWatch alarms.
- Observe the Auto Scaling Group's Behavior in CloudWatch
  - Use CloudWatch metrics to observe the behavior of the SQS `ApproximateNumberOfMessagesVisible` metric over time.

![1611124894110](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611124894110.png)

![1611126574106](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611126574106.png)

## Triggering Lambda from Amazon SQS


  This Lambda function will process messages from the SQS queue and insert the message data as records into a DynamoDB table.

- Download the Lambda execution role IAM policy [here (<https://github.com/julielkinsfembotit/SQSLambdaTriggers/blob/master/lambda_execution_role.json)>.
- Download the Lambda function source code [here] (<https://github.com/julielkinsfembotit/SQSLambdaTriggers/blob/master/lambda_function.py)>.

![1611296858525](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611296858525.png)

## Creating Your Own Serverless Reminder on AWS with Step Functions, API Gateway, Lambda, and S3

Will interact with several AWS services (including AWS Step Functions, API Gateway, AWS Lambda, and S3) to create a reminder serverless application using a static website hosted on S3. You will also integrate the SNS and SES services into your code (but don't worry — we will walk through it all together).

![1611302410439](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611302410439.png)

https://github.com/JulieElkinsAWS/LALabs

**Create Three Lambda Functions**

Create the `sms`, `email`, and `api_handler` Lambda functions in the AWS console:

- Navigate to the Lambda portion of the AWS console.
- Create a function.
- Select **Python3.7** and the existing role for the function.
- Copy code from the GitHub link for the function you are creating: Create the `sms`, `email`, and `api_handler` Lambda functions in the AWS console.
- Navigate to the Lambda portion of the AWS console.
- Create a function.
- Select **Python3.7** and the existing role for the function.
- Copy code from the GitHub link for the function you are creating: <https://github.com/julielkinsfembotit/LALabs>.
- Repeat for `sms` and `email` functions
- For the API handler function go ahead and create the function, but don't forget to go back and update the **SFN_ARN** value in the code!

**check_circleCreate a State Machine**

Create a Step Functions State Machine using the AWS Console:

- Navigate to the Step Functions portion of the console
- Copy the code from the GitHub repository here - <https://github.com/julielkinsfembotit/LALabs>
- Remember to make sure you review the code and understand it!
- Add in the Lambda Function ARNs for the task states of the state machine that require them (make sure to use the appropriate function).
- Create the state machine!

**check_circleCreate an API Gateway**

Create an API Gateway API to integrate with your state machine and your reminder functions:

- Navigate to the API Gateway Console.
- Create a new API from scratch (turn on CORS for it too).
- Create a new resource called **reminders**.
- Add a POST method to the **reminders** resource.
- Configure the POST method with a Lambda proxy integration and your API handler function.
- Deploy your API.
- Copy down the API Gateway API URL for later.

check_circleCreate a Static Website Hosted in S3

- Navigate to the AWS S3 Console.
- Create an S3 bucket.
- Upload static site files to S3 from GitHub: <https://github.com/julielkinsfembotit/LALabs>.
- Configure the bucket as a static website bucket.

## Lambda Functions with S3 Event Triggers

Lambda event triggers are extremely useful for automating serverless workflow, as they help trigger Lambda code/logic and have use cases from monitoring to processing online purchase orders and emailing receipts. In this lab, we'll create a Lambda function from scratch and create an S3 event trigger to execute our Lambda logic.

![1611301945683](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611301945683.png)

#### Learning Objectives

- Create IAM Role for Lambda

```
aws iam create-role --role-name LambdaIAMRole --description "Lambda Role" --assume-role-policy-document file://lambda_assume_role_policy.json --region us-east-1
```

- Create a Policy for the Lambda Function and Attach It to Role

```
## Add a policy
aws iam create-policy --policy-name LambdaRolePolicy --policy-document file://lambda_execution_policy.json --region us-east-1

## Attach the policy to the role, replacing <POLICY_ARN> with the policy ARN included in the output of the previous command
aws iam attach-role-policy --role-name "LambdaIAMRole" --policy-arn <POLICY_ARN> --region us-east-1
```

- Create SNS Topic and Subscribe Your Email Address to It

```
## create sns topic
 aws sns create-topic --name LambdaTopic --region us-east-1
 
## Subscribe an endpoint — for example, your email address — to your topic so that when you publish to the topic, notifications will be sent to your email address. Replace <TOPIC_ARN> with the topic ARN included in the output of the previous command:

 aws sns subscribe --protocol "email" --topic-arn <TOPIC_ARN> --notification-endpoint <EMAIL_ADDRESS> --region us-east-1
```



- Modify Lambda Function with SNS Topic ARN and Zip it into Lambda Deployment Package

- Create Lambda Function

- Add Lambda Permission for S3 Service to Invoke Function

```
## Add Lambda permission, replacing <ARN_S3_BUCKET> with the ARN of the S3 bucket provided on the lab page:

aws lambda add-permission --action lambda:InvokeFunction --principal s3.amazonaws.com --statement-id LabS3Trigger --function-name my-lambda --source-arn "<ARN_S3_BUCKET>"
```

- Enable and Add Notification Configuration to S3 Bucket

```
vim bucket-trigger-notification.json

## Add your Lambda function ARN, which was included in the output when you created your Lambda function.

## Enable the notification configuration on the S3 website bucket, replacing <S3_BUCKET_NAME> with the bucket name provided on the lab page:
aws s3api put-bucket-notification-configuration --bucket <S3_BUCKET_NAME> --notification-configuration file://bucket-trigger-notification.json
```



- Verify Configuration by Uploading a File to Provided S3 Bucket
  

## Querying Data in Amazon S3 with Amazon Athena

![1611300922755](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611300922755.png)

Create a Table from S3 Bucket Metadata

1. Navigate to Amazon Athena.

2. Create a table from S3 bucket data using the following values:

   - *Database:* **aws_service_logs**

   - *Table Name:* **cf_access_optimized**

   - *Location of Input Data Set:* **s3:///**

   - *Data Format:* **Parquet**

   - Bulk add columns using this data:

     ```
     time timestamp, location string, bytes bigint, requestip string, method string, host string, uri string, status int, referrer string, useragent string, querystring string, cookie string, resulttype string, requestid string, hostheader string, requestprotocol string, requestbytes bigint, timetaken double, xforwardedfor string, sslprotocol string, sslcipher string, responseresulttype string, httpversion string
     ```

3. Create the following partitions:

   - Column Name: year
   - Column Name: month
   - Column Name: day

4. Click **Create table**.

check_circleAdd Partition Metadata

1. Open a new query tab

2. Run the following query:

   ```
    MSCK REPAIR TABLE aws_service_logs.cf_access_optimized`
    `
   ```

3. Verify the partitions were created with the following query:

   ```
    SELECT count(*) AS rowcount FROM aws_service_logs.cf_access_optimized
    `
   ```

4. Run the following query:

   ```
   SELECT * FROM aws_service_logs.cf_access_optimized LIMIT 10`
   ```

check_circleQuery the Total Bytes Served in a Date Range

1. Perform the following query:

   ```sql
   SELECT SUM(bytes) AS total_bytes
   FROM aws_service_logs.cf_access_optimized
   WHERE time BETWEEN TIMESTAMP '2018-11-02' AND TIMESTAMP '2018-11-03'
   ```

1. Observe the value for `total_bytes` equals `87310409`.

  

## AWS Deployment

![1611144121340](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611144121340.png)

### Cloud Formation



![1611139061202](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611139061202.png)

![1611143073342](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611143073342.png)

### Elastic Beanstalk Overview

![1611143453843](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611143453843.png)

### OpsWorks Overview

Here stacks are made up of layers. So we can have app layer, database layer etc. **Each of these layers can have their own recipe**.

![1611143808539](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611143808539.png)

![1611144064308](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611144064308.png)

## Serverless

### Step function

![1625729485854](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1625729485854.png)

![1625729278927](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1625729278927.png)

![1625729297398](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1625729297398.png)

![1625729695586](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1625729695586.png)



### Lambda

It can store output into EFS or DDB as lambda is stateless.

![1611144664188](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611144664188.png)![1611145041638](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145041638.png)

### API Gatewaty

![1611145167406](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145167406.png)![1611145221166](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145221166.png)

## Hybrid Environments

### Web Identity Federation and Cognito Overview

![1611147072546](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611147072546.png)

- Cross Account Role
- Identity Federation
- Web Identity Federation

![1611145380339](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145380339.png)

**Here we are assuming role to access AWS from another AWS or identity provider. Sometime this is called AWS Cross-Account role.**

![1611145452642](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145452642.png)

![1611145659880](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145659880.png)

![1611145773083](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611145773083.png)



![1611146185321](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611146185321.png)

![1611146239099](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611146239099.png)

![1611147203167](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611147203167.png)

### AWS VPN

With the AWS VPN service, we can configure a hardware VPN that is a highly available virtual private connection between our VPC and on-premises network.

![1611222559997](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222559997.png)

![1611215238562](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611215238562.png)

**Steps are:**

- **Create customer gateway** (It is best to create a customer gateway for every physical on-premise customer router)
  - Dynamic/static routing
- Create Virtual Private Gateway (similar to NAT gateway)
- Create site to site VPN connection
- 

![1611147336391](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611147336391.png)![1611147426438](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611147426438.png)

#### Design approaches

**No Availability**

![1611215599908](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611215599908.png)

Here two TUNNEL end points are located into different AZ.  dual Tunnel will require dynamic routing.

![1611222381082](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222381082.png)

Here we have 4 tunnel to have full HA.

![1611222482898](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222482898.png)

![1611222639949](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222639949.png)

### Direct Connect Overview

![1611222903108](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222903108.png)

![1611222930219](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611222930219.png)

![1611223021048](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611223021048.png)



## EFS

For AWS Lambda, we recommend using the regional EFS.  This allows both compute and storage to be elastic at a regional level. However, if the customer has a use case that can be satisfied with EFS One Zone, they can use it with AWS Lambda.

S3 has a One Zone storage class. EFS One Zone will have both a One Zone standard storage class, and a One Zone Infrequent Access storage class.

Lifecyle management is supported within regional of One Zone storage classes. 

Amazon EFS backups are always encrypted. The AWS KMS encryption key for Amazon EFS backups is configured in the AWS Backup vault that the Amazon EFS backups are stored in. You can read additional information here: <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>

When  you create a new file system using the Amazon EFS console, API, SDK, or the EC2 Launch Instance Wizard. From the Amazon EFS console, click on ‘Create File System’, select ‘Single-AZ’, and pick an AZ to create a file system with recommended settings, including Automatic Backup and a default Lifecycle Management policy.  There is no mechanism to "switch" a One Zone file system to a Regional file system.  

![1612886838275](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612886838275.png)

![1612886860942](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612886860942.png)

![1612886928448](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612886928448.png)

![1612887255495](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612887255495.png)

![1612887314184](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612887314184.png)

![1612887368953](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612887368953.png)

![1612887577946](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612887577946.png)

![1612887641466](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612887641466.png)



# Exam Questions

![1612953523876](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612953523876.png)

![1612954025721](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1612954025721.png)



# Building and Deploying Docker Containers to Fargate with Terraform and ADO

![1611932680295](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611932680295.png)

![1611932718744](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611932718744.png)

![1611932738630](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611932738630.png)

![1611932818122](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611932818122.png)

![1611933225501](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611933225501.png)

![1611933499234](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611933499234.png)

![1611933914731](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1611933914731.png)

terraform: <https://dev.azure.com/CSGDevOpsAutomation/journey-orchestration/_git/fargate-cop-demo>

go application container: <https://dev.azure.com/CSGDevOpsAutomation/journey-orchestration/_git/fargate-cop-demo>



# Serverless Meetup

## Event Driven Serverless Microservices

A design pattern for building Serverless applications as a collection of microservices that provides flexibility, modularity and performance. By combining the strengths of microservices while simultaneously removing the infrastructure burden downside of them with Serverless, we get the best of both worlds combined together beautifully.

![1627105420407](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627105420407.png)![1627105540497](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627105540497.png)![1627106024326](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106024326.png)![1627106105207](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106105207.png)![1627106160839](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106160839.png)

**Lets look at this architecture to understand more about serverless.**

![1627106265597](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106265597.png)![1627106357933](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106357933.png)![1627106381607](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106381607.png)![1627106393106](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106393106.png)

**Now lets break w.r.t AWS services the above architecture.**

![1627106426381](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106426381.png)

Now, lets look at a complex service…Order service which needs customer service micro service also…

**Approach 1:**

![1627106620270](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106620270.png)

Here we have hard dependency between customer and order service..

![1627106658676](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106658676.png)

**Approach 2:**

we can keep a projection of customer data (only customer who needs order) into order service also. So customer and order micro service are now independent. we get resiliency and both micro service are not closely linked. No talking to other micro service. 

![1627106731843](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106731843.png)

![1627106845943](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106845943.png)

![1627106951623](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106951623.png)![1627106987419](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627106987419.png)![1627107186569](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627107186569.png)

## More with Less on Serverless

Building enterprise products from scratch is a complex and challenging process. It involves weaving all aspects of business, product, technology, people and processes to create value. Engineering practices must evolve to deliver high quality output in a short span of time to be able to penetrate the market and iterate development over the feedback loops.

![1627109209673](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627109209673.png)![1627109777039](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627109777039.png)![1627109899587](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627109899587.png)![1627111055227](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627111055227.png)![1627111665271](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627111665271.png)



![1627111693639](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627111693639.png)

![1627112292952](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627112292952.png)



![1627112311185](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627112311185.png)

![1627112696981](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1627112696981.png)



# Reference

- https://tutorialsdojo.com/aws-cheat-sheets/
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithDynamo.html
- 



