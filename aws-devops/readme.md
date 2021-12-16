# AWS DevOPS Learning

## AWS Code Commit

### Basic Overview

AWS CodeCommit is a fully-managed [source control](https://aws.amazon.com/devops/source-control/) service that hosts secure Git-based repositories. Git is an Open Source distributed source control system:

- Centralized repository for all of your code, binaries, images, and libraries.
- Tracks and manages code changes.
- Maintains version history.
- Manages updates from multiple sources.
- Enables collaboration.

CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure.You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.

- CodeCommit scales seamlessly.

- CodeCommit is integrated with Jenkins, CodeBuild and other CI tools.

- CodeCommit is one of the AWS continuous integration tools (CodeBuild compiles and test code):

![im](https://cdn-digicloud.pressidium.com/wp-content/uploads/2020/04/AWS-CodeCommit-and-CodeBuild-CI-1024x488.jpg)

You can transfer your files to and from AWS CodeCommit using HTTPS or SSH. Repositories are automatically encrypted at rest through AWS Key Management Service (AWS KMS) using customer-specific keys.

### Authorization

IAM policies for authorizing access for users/roles to repositories. CodeCommit only supports identity-based policies, not resource-based policies. You can attach tags to CodeCommit resources or pass tags in a request to CodeCommit.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `codecommit:ResourceTag/key-name`, `aws:RequestTag/key-name`, or `aws:TagKeys` condition keys.

### Code Commit Notifications

You can trigger notifications in CodeCommit using AWS SNS or AWS Lambda or AWS CloudWatch Event rules.

![im](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2020/01/17/p1.jpg)



![im](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7e1e7980-896b-46bf-aa4f-21276dc782fc/images/46f3d306-109d-4aa2-b5a8-6e52c3e459a1.png)



Use cases for notifications SNS / AWS Lambda:

- Deletion of branches.
- Trigger for pushes that happen in the master branch.
- Notify external build system.
- Trigger AWS Lambda function to perform codebase analysis.

Use cases for CloudWatch Event Rules:

- Trigger for pull request updates (created / updated / deleted / commented).
- Commit comment events.
- CloudWatch Event Rules go into an SNS Topic.

### Create a conditional policy in IAM

You’re going to create a policy in IAM that will deny API actions if  certain conditions are met. We want to prevent users with this policy  applied from updating a branch named **master**, but we  don’t want to prevent them from viewing the branch, cloning the  repository, or creating pull requests that will merge to that branch.  For this reason, we want to pick and choose our APIs carefully. Looking  at the [Permissions Reference](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html), the logical permissions for this are:

- GitPush
- PutFile
- MergePullRequestByFastForward

Now’s the time to think about what else you might want this  policy to do. For example, because we don’t want users with this policy  to make changes to this branch, we probably don’t want them to be able  to delete it either, right? So let’s add one more permission:

- DeleteBranch

![im](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2018/05/04/branch-policy1.png)

The branch in which we want to deny these actions is **master**. The repository in which the branch resides is *MyDemoRepo*. We’re going to need more than just the repository name, though. 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "codecommit:GitPush",
                "codecommit:DeleteBranch",
                "codecommit:PutFile",
                "codecommit:MergePullRequestByFastForward"
            ],
            "Resource": "arn:aws:codecommit:us-east-2:80398EXAMPLE:MyDemoRepo",
            "Condition": {
                "StringEqualsIfExists": {
                    "codecommit:References": [
                        "refs/heads/master"   
                    ]
                },
                "Null": {
                    "codecommit:References": false
                }
            }
        }
    ]
}
```

- First, change the repository ARN to the ARN for your repository and include the repository name. 
- Second, if you want to restrict access to a branch with a name different from our example, **master**, change that reference too.

Apply the policy to a group

1. In the IAM console, choose **Groups**, and then choose **Developers**.
2. On the **Permissions** tab, choose **Attach Policy**.
3. Choose **DenyChangesToMaster**, and then choose **Attach policy**.

![im](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2018/05/04/branch-policy2.png)



## AWS Code Build

AWS CodeBuild is **a fully managed continuous integration service that compiles source code**,
runs tests, and produces software packages that are ready to deploy. 
With CodeBuild, you don't need to provision, manage, and scale your own 
build servers.

![im](https://i.pinimg.com/originals/21/9a/d9/219ad9ee45f8a189074b5f87f686e9f9.png)

![im](https://miro.medium.com/max/624/1*gu4YU674fgqj1cgsQoXb3w.png)

## AWS CodeDeploy

AWS CodeDeploy is **a fully managed deployment service that automates software deployments**  to a variety of compute services such as Amazon EC2, AWS Fargate, AWS  Lambda, and your on-premises servers. You can use AWS CodeDeploy to  automate software deployments, eliminating the need for error-prone  manual operations.

![im](https://i.ytimg.com/vi/voWo0hF8mQQ/hqdefault.jpg)

A blue/green deployment is a deployment strategy wherein you create two separate, but identical environments. One environment (blue) is running the current application version, and one environment (green) is running the new application version. The blue/green deployment strategy increases application availability by generally isolating the two application environments and ensuring that spinning up a parallel green environment won’t affect the blue environment resources. This isolation reduces deployment risk by simplifying the rollback process if a deployment fails.

![im](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2021/07/19/bg-blog-EFS-4.jpg)

**The event flow in Figure 1 is as follows:**

1. A developer commits code changes from their local repo to the CodeCommit repository. The commit triggers CodePipeline execution.
2. CodeBuild execution begins to compile source code, install  dependencies, run custom commands, and create deployment artifact as per  the instructions in the [Build specification](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) reference file.
3. During the build phase, CodeBuild copies the source-code  artifact to Amazon EFS file system and maintains two different  directories for current (green) and new (blue) deployments.
4. After successfully completing the build step, CodeDeploy  deployment kicks in to conduct a Blue/Green deployment to a new Auto  Scaling Group.
5. During the deployment phase, CodeDeploy mounts the EFS file system on new EC2 instances as per the [CodeDeploy AppSpec](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html) file reference and conducts other deployment activities.
6. After successful deployment, a Lambda function triggers in order to store a deployment environment parameter in [Systems Manager parameter store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). The parameter stores the current EFS mount name that the application utilizes.
7. The [AWS Lambda](https://aws.amazon.com/lambda/) function updates the parameter value during every successful deployment with the current EFS location.

### Code deploy configuration

- Create IAM role with permission to read S3 and launch EC2
  - [AmazonS3ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonS3ReadOnlyAccess)
  - [AWSCodeDeployRole](https://console.aws.amazon.com/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSCodeDeployRole)
- Install code deploy agent
  - https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html
- configure code deploy application

### Working with deployment configurations in CodeDeploy            

When you deploy to an EC2/On-Premises compute platform, the deployment configuration specifies, through the use of a minimum healthy hosts value, the number or percentage of instances that must remain available at any time during a deployment. 

You can use one of the three predefined deployment configurations provided by AWS or
create a custom deployment configuration. For more information about creating custom
deployment configurations, see [Create a Deployment Configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html). If you don't specify a deployment configuration, CodeDeploy uses the CodeDeployDefault.OneAtATime deployment configuration.

| Deployment configuration      | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| CodeDeployDefault.AllAtOnce   | **In-place deployments**:                                                 Attempts to                                                 deploy an application  revision to as many instances as possible at once. The status                                                 of the overall  deployment is displayed as **Succeeded**                                                 if the application  revision is deployed to one or more of the instances. The status                                                 of the overall  deployment is displayed as **Failed** if                                                 the application revision  is not deployed to any of the instances. Using an example                                                 of nine instances,  CodeDeployDefault.AllAtOnce attempts to deploy to all nine                                                 instances at once. The  overall deployment succeeds if deployment to even a single                                                 instance is successful.  It fails only if deployments to all nine instances fail.                                                                                                  **Blue/green deployments**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Deployment to replacement environment: Follows the same deployment rules                                                             as CodeDeployDefault.AllAtOnce for in-place deployments.                                                                                                                                                                                                                                                                                                                                                       Traffic  rerouting: Routes traffic to all instances in the replacement                                                             environment  at once. Succeeds if traffic is successfully rerouted to at least                                                             one  instance. Fails after rerouting to all instances fails. |
| CodeDeployDefault.HalfAtATime | **In-place deployments**:                                                                                                                                                   Deploys to up to half  of the instances at a time (with fractions rounded                                                    down). The overall  deployment succeeds if the application revision is deployed to                                                    at least half of the  instances (with fractions rounded up). Otherwise, the                                                    deployment fails. In  the example of nine instances, it deploys to up to four                                                    instances at a time.  The overall deployment succeeds if deployment to five or more                                                    instances succeed.  Otherwise, the deployment fails.                                                                                                                                                    **Blue/green deployments**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Deployment to replacement environment: Follows the same deployment rules                                                             as CodeDeployDefault.HalfAtATime for in-place deployments.                                                                                                                                                                                                                                                                                                                                                       Traffic  rerouting: Routes traffic to up to half the instances in the                                                             replacement  environment at a time. Succeeds if rerouting to at least half of                                                             the  instances succeeds. Otherwise, fails. |
| CodeDeployDefault.OneAtATime  | **In-place deployments**:                                                                                                                                                   Deploys the application revision to only one instance at a time.                                                                                                  For deployment groups that contain more than one instance:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The overall  deployment succeeds if the application revision is deployed to                                                             all of the  instances. The exception to this rule is that if deployment to the                                                             last  instance fails, the overall deployment still succeeds. This is because                                                             CodeDeploy  allows only one instance at a time to be taken offline with the                                                              CodeDeployDefault.OneAtATime configuration.                                                                                                                                                                                                                                                                                                                                                      The overall deployment fails as soon as the application revision fails to                                                             be deployed to any but the last instance.                                                                                                                                                                                                                                                                                                                                                       In an  example using nine instances, it deploys to one instance at a time.                                                             The overall  deployment succeeds if deployment to the first eight instances is                                                             successful.  The overall deployment fails if deployment to any of the first                                                             eight  instances fails.                                                                                                                                                                                                                                                                                                                                                                                  For deployment groups that contain only one instance, the overall deployment                                                    is successful only if deployment to the single instance is successful.                                                                                                                                                   **Blue/green deployments**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Deployment to replacement environment: Follows same deployment rules as                                                             CodeDeployDefault.OneAtATime for in-place deployments.                                                                                                                                                                                                                                                                                                                                                       Traffic  rerouting: Routes traffic to one instance in the replacement                                                             environment  at a time. Succeeds if traffic is successfully rerouted to all                                                             replacement  instances. Fails after the very first rerouting failure. The                                                             exception to  this rule is that if the last instance fails to register, the                                                             overall  deployment still succeeds. |

### Lifecycle Event Hooks in CodeDeploy

Event hooks are configured on a file called Application Specification file (AppSpec). An **AppSpec file**  is nothing but a piece of a configuration file that can be written  using YAML or JSON, which defines how an application is deployed.  AppSpec file is available for deploying on three platforms:

1. **Amazon ECS Compute Platform**
2. **Amazon Lambda Compute Platform**
3. **Amazon EC2/On-premises Compute Platform**

Each of them has different hook events. For simplicity, we will be  looking at deploying on an EC2 instance. You can find the information  for the other two here:
 <https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-server>

Here is an overview of the lifecycle event hooks on an EC2/On-premises platform:

![Lifecycle Event Hooks in CodeDeploy1](https://td-mainsite-cdn.tutorialsdojo.com/wp-content/uploads/2020/08/Lifecycle-Event-Hooks-in-CodeDeploy1.png)

**Events** Here’s a brief description of the lifecycle events so you can decide  at which stage you are going to put custom actions as needed by your  deployments.

1. **Start** – This is the first event of the  lifecycle event. The CodeDeploy Agent automatically executes this for  you. This initiates the instance for deployment.
2. **ApplicationStop**  – it is the stage for running any scripts that will stop your old  application. For example, if you have a new version of an e-commerce web  application, let’s say v.1, this event will allow you to disable v.0  and prepare the instance to receive a new version, which in this case is  v.1.
3. **DownloadBundle –** During this event, the CodeDeploy Agent will pull the new version onto the instance.
4. **BeforeInstall** –  You can use this event to store the previous configuration of your old  install that you want to keep, decrypt files, and create a backup of the  current version.
5. **Install** – During this event, the CodeDeploy Agent will copy the revision files to a file destination that you specify.
6. **AfterInstall** – this event gives you the chance to change the configuration of your application before the application starts.
7. **ApplicationStart** – As the name implies, you use this event to turn on your application which is now v.1 instead of v.0.
8. **ValidateService** –  You can use this event to include any validation logic to determine that the deployment succeeded.
9. **End** –  This is the last event of the lifecycle event. This will notify the  central service that the deployment to the instance was successful.

**Things To Consider**

- **YAML is the only available** format for configuring AppSpec in EC2/On-premise.
- You can either use YAML or JSON for configuring AppSpec in ECS and Lambda.
- You need to **install the CodeDeploy Agent** for configuring AppSpec in EC2/On-premise.
- For ECS and Lambda, you can directly use the online editor.
- Referring to the diagram above, only the **blue-colored** events can be scripted. The rest are handled by the CodeDeploy Agent.

![im](https://www.oreilly.com/library/view/aws-certified-solutions/9781789130669/assets/c9d0ee58-7af7-4d09-9c33-0add2f9bec80.png)

## Blue/Green: Duplicate the whole environment and switch the URLs

Blue/Green  deployments simply replicate your current environment (blue), deploy  the new application to your new, cloned environment (green), and  redirect the traffic to the green one after deployment.

If the deployment fails, you terminate the green environment, and nothing will be affected.

If  something goes wrong after deployment, for example, your users  experience a problem in the new version, you can simply redirect the  traffic back to the old version. Hence, it would be wise to keep the old  environment running until you verify that the deployment is successful  and DNS propagation completed.

If everything goes well, you  terminate the old environment, and your cloned environment becomes your  new blue one. You repeat the same process in all new deployments. It is a  nearly zero-downtime deployment model and a best practice for  mission-critical applications.

### How to perform Blue/Green deployments on AWS Elastic Beanstalk?

As  you deploy application versions on a selected environment, Blue/Green  does not exist as a deployment type on Elastic Beanstalk deployments  because you need to duplicate the environment as a whole, including  Elastic Load Balancers. However, this is very simple on Elastic  Beanstalk, and actually, this simplicity is one of its strengths:

1)  You clone the current environment using AWS Management Console or AWS  CLI, or EB CLI. There is a feature for this. It will create a replica of  your environment alongside Elastic Load Balancers, Autoscaling Groups,  and other resources and deploy the current version on the new instances.

2)  After your new environment is ready, you deploy the new version on this  environment and verify that the deployment is successful.

![Elastic Beanstalk - Blue Green Deployments - Clone](https://blog.shikisoft.com/assets/images/post_imgs/eb-deployments/eb-blue-green-start.png)

3)  Once you are sure that everything is fine, you swap the URLs of the two  environments using AWS Management Console or AWS CLI, or EB CLI. Again,  Elastic Beanstalk provides a specific action for this. Then, the  traffic will start to flow to your new environment after the DNS  propagation completes.

![Elastic Beanstalk - Blue Green Success](https://blog.shikisoft.com/assets/images/post_imgs/eb-deployments/eb-blue-green-success.png)

### What are the prerequisites to apply Blue/Green?

First  of all, you are duplicating your environment and subject to AWS account  limits as in the immutable deployments. Hence, your EC2 instance limits  should cover the new instances launched.

Secondly and even more  importantly, your environment should not contain any RDS instances  managed by Elastic Beanstalk because the data will not be copied during  the clone operation. Even it had clonned, the two databases would not be  in sync during the swap phase. So, swapping URLs and pointing to an  empty database would not be feasible if you have an RDS database  resource in your Elastic Beanstalk environment.

## Rolling: Let’s be more cautious and deploy one by one!

You can mitigate `all fail` mode of `all at once` by rolling deployments and switch to `only one batch fails` mode. When you deploy in the `Rolling` mode, you also define the number of instances to be grouped in a batch. For example, let’s define the batch size as 1.

In the beginning, Elastic Beanstalk deploys the application version to the first batch and proceeds to next after it succeeds.

![Elastic Beanstalk - Rolling](https://blog.shikisoft.com/assets/images/post_imgs/eb-deployments/eb-rolling-process.png)

What  happens if the deployment fails? Only failed instance will be effected  and the effect on whole environment depends on when it failed.

- If  it failed in the first batch, the first instance will be down, and the  remaining instances will continue to serve the previous version.
- If  it failed in later batches, the failed instance will become unhealthy  and there will be two versions served by your environment: The new  version will be served by successful deployments until the failure and  the previous version will be served by instances the deployment  cancelled.

![Elastic Beanstalk - Failure](https://blog.shikisoft.com/assets/images/post_imgs/eb-deployments/eb-rolling-failure.png)

In  addition, your fleet size serving the application will be reduced by  the batch size, as failed instances will not be able to serve traffic.  But, you will not have downtime when compared to `all at once` deployments.

To  rollback, you need to cancel deployment using AWS Management Console or  AWS CLI or EB CLI and start redeployment of the known previous healthy  version on the environmen



## Reference

- [Refining Access to Branches in AWS CodeCommit](https://aws.amazon.com/blogs/devops/refining-access-to-branches-in-aws-codecommit/)
- 