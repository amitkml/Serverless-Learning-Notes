

[TOC]

## Workflow

![1605847863099](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605847863099.png)

## What is Comprehend?

- Text has to be in supported language in UTF format.

![im](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2019/04/03/analyze-twitter-comprehend-sagemaker-1.gif)

## Approaches

![1605857436596](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605857436596.png)

## Use cases

![1605857537107](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605857537107.png)

## NLP Basics

### Document Classifier

![1605858397919](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605858397919.png)

### Confidence Scores

- It is an probability.
- Each company takes confidence score and compare with confidence threshold (determined by business) to find out accuracy.



![1605858630010](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605858630010.png)![1605858774133](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605858774133.png)

### Language Detection

- A SYNC API call that provides two digit language code for the specified text.

![1605865866189](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605865866189.png)

![1605865961097](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605865961097.png)

#### Request Format

![1605866064098](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605866064098.png)

#### Response Format

![1605866153831](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605866153831.png)

#### CLI Demo

```
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice, valid choices are:

batch-detect-dominant-language           | batch-detect-entities
batch-detect-key-phrases                 | batch-detect-sentiment
batch-detect-syntax                      | classify-document
create-document-classifier               | create-endpoint
create-entity-recognizer                 | delete-document-classifier
delete-endpoint                          | delete-entity-recognizer
describe-document-classification-job     | describe-document-classifier
describe-dominant-language-detection-job | describe-endpoint
describe-entities-detection-job          | describe-entity-recognizer
describe-key-phrases-detection-job       | describe-sentiment-detection-job
describe-topics-detection-job            | detect-dominant-language
detect-entities                          | detect-key-phrases
detect-sentiment                         | detect-syntax
list-document-classification-jobs        | list-document-classifiers
list-dominant-language-detection-jobs    | list-endpoints
list-entities-detection-jobs             | list-entity-recognizers
list-key-phrases-detection-jobs          | list-sentiment-detection-jobs
list-tags-for-resource                   | list-topics-detection-jobs
start-document-classification-job        | start-dominant-language-detection-job
start-entities-detection-job             | start-key-phrases-detection-job
start-sentiment-detection-job            | start-topics-detection-job
stop-dominant-language-detection-job     | stop-entities-detection-job
stop-key-phrases-detection-job           | stop-sentiment-detection-job
stop-training-document-classifier        | stop-training-entity-recognizer
tag-resource                             | untag-resource
update-endpoint                          | help

C:\WINDOWS\system32>aws comprehend detect-dominant-language --text "Hello This is Amit"
{
    "Languages": [
        {
            "LanguageCode": "en",
            "Score": 0.9958519339561462
        }
    ]
}

```

![1605874753859](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605874753859.png)

## Sentiment Analysis

- Positive

- Negative

- Neutral

  

![1605883654307](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605883654307.png)

- DetectSentiment API call is a SYNC and provides sentiment for a text
- BatchDetectSentiment API  SYNC call provides sentiment of 25 text in dominant language

![1605884120285](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605884120285.png)

**Response**

![1605884214101](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605884214101.png)

### CLI Examples

Here is how we can call comprehend sync API DetectSentiment from CLI to understand sentiment.

- languageCode must satisfy constraint: Member must satisfy enum value set: [ar, hi, ko, zh-TW, ja, zh, de, pt, en, it, fr, es]
- languageCode needs to be passed with the text as shared below.
- Final sentiment value is populated into Sentiment key element and then from score we an derive the probability value.

```
C:\WINDOWS\system32>aws comprehend detect-sentiment --language-code="en" --text "I am really confused. How you do"
{
    "Sentiment": "NEGATIVE",
    "SentimentScore": {
        "Positive": 0.0019269874319434166,
        "Negative": 0.7861156463623047,
        "Neutral": 0.211948424577713,
        "Mixed": 8.903435627871659e-06
    }
}
```

 

## Syntax/POS Analysis

- It is part of speech identification for each of the text in a document.
- Covers following POS identification

![1606115043013](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606115043013.png)



![1606114906027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606114906027.png)



**Here is an example of syntax analysis..**

![1606115122652](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606115122652.png)

- DetectSyntax SYNC API inspects words to identify POS identification for one text.
- BatchDetectSyntax API inspects text looking for POS upto 25 samples of text in same dominant language.

### Request and Response format

![1606116748439](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606116748439.png)

![1606116792468](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606116792468.png)

## Advanced Text Analysis - Detect Entities

### Async Design approach

![1606133365325](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606133365325.png)

#### Request Format

![1606144896291](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606144896291.png)

- New IAM Role will need to be created for trusted entity Comprehend. During role creation, we need to select comprehend and create the role. So this ensures, that only comprehend service can assume this role.

![1606151560309](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606151560309.png)

## Detect Entities

Comprehend can detect following entities.

![1606152361535](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152361535.png)

### How it works?

![1606152619144](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152619144.png)

![1606152696763](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152696763.png)

#### API Call

![1606152734774](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152734774.png)

![1606152751042](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152751042.png)

![1606152763400](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606152763400.png)

#### Analysis of batch output

- jq is an open source uitlity to analyze json file.

![1606153682453](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606153682453.png)

### Training for custom Entities

- We need to define **custom Entity List OR annotation** to train comprehend for custom entities
- Below, first we are defining the custom entity list and also there we have defined new custom entity entity type (API, DATA_STRUCTURE)
- Otherwise
- we can define the annotation for these custom entities.
- Now train the new recognizer.

![1606153947735](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606153947735.png)

![1606153984735](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606153984735.png)

![1606154136525](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606154136525.png)

![1606154762607](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606154762607.png)

**Once trained then, we will have a ARN for our Recognizer which can be used for our detect entities.**

![1606154993176](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606154993176.png)

**Here is how we can refer from python**

![1606155108094](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155108094.png)

## Detecting Key Phrases

### Example

![1606155260422](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155260422.png)

![1606155325877](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155325877.png)

### Solution Architecture

![1606155378714](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155378714.png)

### API Inputs

![1606155406178](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155406178.png)

![1606155427597](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155427597.png)

![1606155454535](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155454535.png)

### Request and Response Format

- Request format is same as other start job
- Response format is bit similar but it echo a bit of entity detection

![1606155588043](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606155588043.png)

### Use case summary

![1606156054732](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156054732.png)

## Document Topic Analysis

### Aim

![1606156148370](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156148370.png)

### Topic Modelling

> Aim is to identify relevant and common terms and topics  in a series of documents.

### Workflow

![1606156283671](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156283671.png)

### What is Topic Groups?

- Consist of number, keyword and weightage. So here in this example, for topic group 1, we have two key word but their weights are different. The reason is Course can be happening without Pluralsight also but Pluralsight only deals with education.

![1606156315477](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156315477.png)

### Document to Topic Groups

- Here it is being show that in document 1, almost 56% of the keyword belong with Topic group 1. This is quite critical information and can lead lot of document advanced analysis. This tells which one is predominant topic.

![1606156521210](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156521210.png)

#### API

![1606157109083](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606157109083.png)

- API has optional parameter Number of Topic which helps to narrow down LDA process.



![1606157143807](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606157143807.png)





### LDA

![1606156698000](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156698000.png)

![1606156775910](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606156775910.png)

## Final Document Analysis

![1606157048027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606157048027.png)

![1606157567662](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1606157567662.png)

