# Serverless Architecture Examples

This notebook will contain several architectures examples on AWS serverless.

## Simple OTP service

This post describes how to implement a simple One Time Password (OTP) system with AWS Serverless services which can be used as a part of two step verification.

Below tools and technologies used to build this application.

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [API Gateway](https://aws.amazon.com/api-gateway/)
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [Simple Email Service - SES](https://aws.amazon.com/ses/)
- [Amplify Web Hosting](https://aws.amazon.com/amplify/hosting/)
- [VueJS](https://vuejs.org/) for frontend
- Deploy with [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

![im](https://camo.githubusercontent.com/6f260a259596779af910bd0aef4cc7d20440b3364949dd98f0889af203dcc6ac/68747470733a2f2f7075627564752e6465762f696d616765732f6f74702d736572766963652e706e672363656e746572)

## How it works

1. In this scenario, I used a login form, which is developed with VueJS and hosted using Amplify static web hosting.
2. User will enter their email and password and once the credentials are validated, an API endpoint is called to execute “Generate OTP” Lambda function which generates a 6 digit code along with a session id.
3. Once the code and session id is generated, “Generate OTP” Lambda will save these data into a DynamoDB table.
4. Then only the session id will be returned as the response of the API end point.
5. DynamoDB streams are enabled in the table. So, once the data are saved, it will trigger the “Send Email” Lambda function.
6. Within the “Send Email” Lambda function, it will call the Simple Email Service (SES) to send out an email with the generated code to the email address provided.
7. Meanwhile in the frontend side, once the session id is received to from the API, 2nd form is presented to enter the code, which is emailed to the given address.
8. Once user enters the code and submit, it will validate the code along with the session id using another API gateway endpoint which proxy to “Verify OTP” Lambda function.
9. In “Verify OTP” Lambda function, it query the DynamoDB table with the given session id and code and returns the success or error responses.

## Key points/Lessons learnt

1. Here I enabled DynamoDB TTL to delete the entries after specific time to prevent fill out the table very quickly. However DynamoDB will not delete your record immediately when the TTL is expired. It is deleted eventually and AWS only guarantees it to be deleted within 48 hours. Because of this, when verifying the OTP code, it has to consider the same *“expiredAt”* field which used to set TTL.
2. When design the DynamoDB table, I used sessionId + OTP code as a primary key to easily query the required record. So, when verifying the code, I query by primary key with this combination in the DynamoDB table.
3. When using DynamoDB steam as a trigger for Lambda, it get triggers for all the DynamoDB events (ex: insert, delete, update). So, within the Lambda function, had to filter out only the *INSERT* events using *“eventName”* of the record.
4. To send out emails, I have used AWS’s own Simple Email Service (SES). However, you need to first verify your sending email address in order to send emails to any address. This can be done with a support request.
5. Here, I used Amplify static web hosting to host the frontend of the application. I have used Amplify features - the auto deployments when Github repository modified and custom domain name set up only with few button clicks.
6. I have used AWS SAM to deploy the backend resources. The expiry time of the OTP and no of digits in the OTP code can be configured at the deployment time.

## How to set up

### Prerequisites

- AWS cli
- AWS SAM cli
- Set up and verified SES send email address

#### Backend

1. Clone the repository: <https://github.com/pubudusj/simple-otp>

2. Run

   ```
   sam init && sam deploy -g
   ```

After providing your stack information and AWS environment parameters, this will create the backend stack. Copy the ApiBaseUrl output value.

#### Frontend

1. Copy the .env.example into .env file and add the ApiBaseUrl value as *VUE_APP_API_BASE_URL*.
2. You may zip the whole frontend directory and use that in Amplify web hosting, or authorise your GitHub repository to automatically deploy the application when a git push is made.
3. If you need to run the frontend in local, navigate to frontend directory and run `npm run serve`

#### To Delete the stack

To remove the backend, run `sam delete`.