
##  Containers-as-a-Service (CaaS) to Platform-as-a-Service (PaaS) to finally Functions-as-a-Service (FaaS)
![im](https://miro.medium.com/max/1313/0*zze0hX-MxMukYBf9.png)

## fargate or Lambda applications
- [Getting it right between EC2, Fargate and Lambda](https://medium.com/thundra/getting-it-right-between-ec2-fargate-and-lambda-bb42220b8c79)
- [Deploy your Python app with AWS Fargate — A Tutorial](https://towardsdatascience.com/deploy-your-python-app-with-aws-fargate-tutorial-7a48535da586)
- [Python Webscraping in a Docker Container](https://medium.com/analytics-vidhya/python-webscraping-in-a-docker-container-aca2a386a3c0)

### Compare fargate and EC2
- For example, with Fargate you no longer have to worry about patching similar to EC2, but you still have to update your underlying containers. 
- Additionally, even though with Fargate you can escape from EC2 orchestration, you still have to register your containers on the ECS service as Fargate is managed via ECS, which does add more operational complexity.
- When to select Fargate
  - When your application is latency-sensitive.
  - When your application needs inter-container communication or is storage-intensive.
  - When you need support for long-running scheduled jobs (>15 mins).
  - When your application serves predictable high customer traffic.
  - When you need more choices on the runtime environment.
  - When you have a large/batch workload and you’re looking for less operation load.
  - When you don’t need complete control of your compute instances but need control of the compute environment — CPU and memory configs.
- When to select Lambda
  - When you have event-driven workloads, that is, when the application needs to trigger action on an event.
  - When your application requires the ability to handle unknown demand.
  - When you need managed operational and administrative activities like monitoring fleet health, applying security patches to the underlying compute resources, monitoring and logging your code, etc.
  - When you need managed provisioning, capacity scaling, high availability, and utilization.
  - When your application deployment package size ≤ 50 MB and execution time ≤ 15 minutes.
  - When you are focused on cost optimization.
