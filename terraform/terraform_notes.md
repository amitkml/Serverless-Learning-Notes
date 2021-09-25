# DynamodDB

## Samples with count

![1631101047304](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1631101047304.png)

## IAM Role to access from other AWS Account



```yaml
resource aws_iam_role_policy document_output_s3_access_role_policy {
  count  = (length(var.services_trusted_accounts) != 0) ? 1 : 0
  name   = "document-output-s3-access-role-policy"
  role   = aws_iam_role.document_s3_access_role[count.index].id
  policy = <<EOF
{
  "Version":"2008-10-17",
  "Statement":[
  {
    "Effect": "Allow",
    "Action": [
      "s3:GetAccessPoint",
      "s3:GetAccountPublicAccessBlock",
      "s3:ListAllMyBuckets",
      "s3:ListAccessPoints",
      "s3:ListJobs"
    ],
    "Resource": "*"
  },
  {
    "Effect": "Allow",
    "Action": [
      "s3:Get*",
      "s3:List*"
  ],
    "Resource": [
      "arn:aws:s3:::${var.environment_id}-document-output-files",
      "arn:aws:s3:::${var.environment_id}-document-output-files/*",
      "arn:aws:s3:::${var.environment_id}-document-transfer/",
      "arn:aws:s3:::${var.environment_id}-document-transfer/*"
    ]
  }]
}
EOF
}

```

```yaml
resource aws_iam_role document_s3_access_role {
  name  = "${var.environment_id}-document-output-s3access"
  count = (length(var.services_trusted_accounts) != 0) ? 1 : 0
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": ${jsonencode(
  formatlist("arn:aws:iam::%s:root", var.services_trusted_accounts),
)}
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
EOF
}

```

