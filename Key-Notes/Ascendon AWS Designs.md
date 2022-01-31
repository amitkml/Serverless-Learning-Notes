# ARC Diameter Request Logging

![1604556501335](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1604556501335.png)

# Tax Event File Process

https://confluence.csgicorp.com/display/Ascendon/Tax+Event+File+Process+-+Architecture

![1605263845533](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605263845533.png)

# DynamoDB backup - restore

Refer https://confluence.csgicorp.com/display/CDCS/DynamoDB+backup+-+restore

This page explains the use of AWS data pipelines to backup and restore dynamoDB tables across regions when needed.

All tests were carried out on the csg-ascendon-dbss account, and there are data pipelines deployed for nonprod environments, but they are currently inactive. In order to test the restore part, it is necessary to have the basic build of the DR site in eu-west-1 (Ireland), due to subnet requirements for the EMR. However, the process of backup and restore using data pipelines has been tested successfully on the csg-ascendon-dbss account.

# Architecture

The architecture used for backup and restore uses AWS data pipelines.

![1606222469848](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606222469848.png)

# Implementation

## All pipelines were implemented using CloudFormation, the templates currently reside on the nonprod repository <https://bitbucket.csgi.com/projects/ADBS/repos/cf_tele2_nonprod/browse/cf_infra/data_pipelines> .

## Requirements

There are a few requirements to implement data pipelines, these changes will need to be implemented in the production repo.

### Bucket

A bucket to put the backups was created: tele2-dr-backups-nonprod-eu-central-1-kyapgxnfotxrgjhs . <https://bitbucket.csgi.com/projects/ADBS/repos/cf_tele2_nonprod/browse/cf_setup/stack_s3.yaml#505>

### Endpoints

There are 3 new bucket arn to add to the endpoints.yaml file in the VPC stack: (currently lines 104-106)

"arn:aws:s3:::datapipeline*"

"arn:aws:s3:::*elasticmapreduce*"

"arn:aws:s3:::dynamodb-dpl*"

<https://bitbucket.csgi.com/projects/ADBS/repos/cf_tele2_nonprod/browse/cf_infra/vpc/endpoints.yaml#104>

### Initial roles and instance profile

The data pipeline requires 2 roles and 1 instance profile that are used when creating the EMR and also by the EC2 instances run by the EMR, these 2 roles and instance profile can be set for new projects as default roles to be used by dynamoDB data pipelines. 

I placed them under cf_initial/**initial_roles.yaml**, the resource names are: DataPipelineDefaultResourceRole, DataPipelineDefaultRole, and DataPipelineInstanceProfile; currently lines 357 to 502. <https://bitbucket.csgi.com/projects/ADBS/repos/cf_tele2_nonprod/browse/cf_initial/initial_roles.yaml#357>

## CloudFormation Stack

<https://bitbucket.csgi.com/projects/ADBS/repos/cf_tele2_nonprod/browse/cf_infra/data_pipelines>

The command to run the stack has been placed on the nonprod account: [Tele2 Non-Prod Account#ProdAccount-DRBackupsDynamoDB](https://confluence.csgicorp.com/display/CDCS/Tele2+Non-Prod+Account#Tele2NonProdAccount-ProdAccount-DRBackupsDynamoDB)

# Backup

Once the pipelines are created, they'll be active and start taking backups of the dynamoDB tables into the DR S3 bucket, the daily operations should verify the backups continue running without errors.

# Restore

The restore process needs to be validated for Tele2, currently all restore tests were conducted on the csg-ascendon-dbss accounts, between eu-central-1 and eu-west-1.

# ARC Usage Rule Info During new Usage Rule



![1607404119955](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1607404119955.png)



# Interaction with the Billing Gateway Service

https://confluence.csgicorp.com/display/Ascendon/Interaction+with+the+Billing+Gateway+Service

![1607675080811](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1607675080811.png)

***Please note that the above is simplified and doesn't include more granular components of the services*** 

1. ARC Offline delivers an event file to the ARC output cdrs bucket
2. ARC Offline publishes an SNS notification cross-account to the AGL EventFileEventMessage topic
3. AGL is subscribed and receives the notification from EventFileEventMessage
4. AGL reads the event file cross-account from the ARC Offline output cdrs bucket
5. AGL processes the file and enriches it with GL information
6. AGL completes processing of the file and writes the resulting event file cross-account to ARM in native .evt format
7. AGL publishes a notification cross-account to the ARC FileTracking SNS topic
8. ARM polls the S3 bucket for any new event files from AGL
9. ARM processes any incoming event files, rates events and produces reports
10. ARM publishes a notification cross-account to the ARC FileTracking SNS topic



![1607675116019](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1607675116019.png)

***Please note that the above is simplified and doesn't include more granular components of the services*** 

1. ARC Offline delivers an event file to the ARC output cdrs bucket
2. ARC Offline publishes an SNS notification cross-account to the AGL EventFileEventMessage SNS topic
3. AGL is subscribed and receives the notification from AGL EventFileEventMessage
4. AGL reads the event file cross-account from the ARC Offline output cdrs bucket
5. AGL processes the file and enriches it with GL information
6. AGL completes processing of the file and writes the resulting event file cross-account to ARM in JSON format
7. AGL publishes a notification cross-account to the ARC FileTracking SNS topic
8. AGL publishes a notification to the ABG EventFileEventMessage SNS topic
9. ABG is subscribed and receives the notification from ABG EventFileEventMessage
10. AGL reads the event file cross-account from the ARM bucket
11. ABG processes the file
12. ABG completes processing of the file and writes the resulting event file cross-account to ARM in native .evt format
13. ARM polls the S3 bucket for any new event files from ABG
14. ARM processes any incoming event files, rates events and produces reports
15. ARM publishes a notification cross-account to the ARC FileTracking SNS topic

# Tele2 SSR Fargate Support

![1607956178894](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1607956178894.png)

https://confluence.csgicorp.com/display/TTP/Tele2+SSR+Fargate+Support