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



## Reference

- [Refining Access to Branches in AWS CodeCommit](https://aws.amazon.com/blogs/devops/refining-access-to-branches-in-aws-codecommit/)
- 