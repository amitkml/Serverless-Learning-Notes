# AWS DevOPS Learning

## AWS Code Commit

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