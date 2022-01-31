## High Level Services

![1576349269813](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1576349269813.png)

Latest list of services are available in [aws site](https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do). 

## List and Availability Zone

Each ***AWS Region*** is a separate geographic area. Each AWS Region has multiple, isolated locations known as ***Availability Zones***.  They are nothing but Data center. **An availability zone may be mapped with multiple datacenter sometime and in that scenario they are closely located**. 

Region is simply distinct Geographical area. Traditionally each region contains two  or more availability zone. 

We will always have more Edge Location than Region. Edge locations are endpoints of AWS which are used for caching and typically consist of CloudFront, Amazon CDN. **So lets say if an User of Australia is downloading a file from region of US then the file will be cached in edge location of Australia so that next time when any user from Australia downloading same file then it will be accessed from Australia Edge location.** 

Amazon RDS provides you the ability to place resources, such as instances, and data in multiple locations. Resources aren't replicated across AWS Regions unless you do so specifically.

![Image](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Con-AZ.png)

- Each AWS Region is completely independent
- Any Amazon RDS activity initiated (for example, creating database instances or listing available database instances) runs only in our current default AWS Region. The default AWS Region can be changed in the console, by setting the EC2_REGION environment variable, or it can be overridden by using the `--region` parameter with the AWS Command Line Interface. 
- RDS supports a special AWS Region called AWS GovCloud (US-West) that is designed to allow US government agencies and customers to move more sensitive workloads into the cloud.

## Required Components for Certified Associate Architect

- Compute
- Storage
- Database
- Network and Content Delivery
- Security, Identity and complicance
- Global Infratucture
- Basic of Machine Learning
- 



