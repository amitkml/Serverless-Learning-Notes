# Kibana and Elastic Search



## What is Kibana?

Kibana is a data visualization and exploration tool used for log and time-series analytics, application monitoring, and operational intelligence use cases. It offers powerful and easy-to-use features such as histograms, line graphs, pie charts, heat maps, and built-in geospatial support. Also, it provides tight integration with [Elasticsearch](https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-elasticsearch/), a popular analytics and search engine, which makes Kibana the default choice for visualizing data stored in Elasticsearch.Kibana works in sync with Elasticsearch and Logstash which together forms the so called **ELK** stack.



## What is ELK Stack?

**ELK** stands for Elasticsearch, Logstash, and Kibana. **ELK** is one of the popular log management platform used worldwide for log analysis. In the ELK stack, Logstash extracts the logging data or other events from different input sources. It processes the events and later stores them in Elasticsearch.

**Kibana** is a visualization tool, which accesses the logs from Elasticsearch and is able to display to the user in the form of line graph, bar graph, pie charts etc. The basic flow of ELK Stack is shown in the image here −

![ELK Stack](https://www.tutorialspoint.com/kibana/images/elk_stack.jpg)

Logstash is responsible to collect the data from all the remote sources where the logs are filed and pushes the same to Elasticsearch. Elasticsearch acts as a database where the data is collected and Kibana uses the data from Elasticsearch to represent the data to the user in the form of bargraphs, pie charts, heat maps as shown below −

![Elastic search](https://www.tutorialspoint.com/kibana/images/elastic_search.jpg)

## What is Elasticsearch

It is distributed document stores which means once the document is stored then it can be retrieved from any node of the cluster.

It shows the data on real time basis, for example, day-wise or hourly to the user. Kibana UI is user friendly and very easy for a beginner to understand. The following table gives a direct comparison between these terms−

![im](https://cdn-gcp.marutitech.com/wp-media/2017/06/b68fa448-what-is-elasticsearch-used-for.png)

| Elasticsearch | RDBMS    |
| ------------- | -------- |
| Cluster       | Database |
| Shard         | Shard    |
| Index         | Table    |
| Field         | Column   |
| Document      | Row      |

## Key Concepts

In Elasticsearch terms, Index = Database, Type = Table, Document = Row.

 

The key concepts of Elasticsearch are as follow

- Node
  - It refers to a single running instance of Elasticsearch.
- Cluster
  - It is a collection of one or more nodes. Cluster provides collective indexing and search capabilities across all the nodes for entire data.
- Index
  - It is a collection of different type of documents and their properties. Index also uses the concept of shards to improve the performance
- Document
  - It is a collection of fields in a specific manner defined in JSON format. Every document belongs to a type and resides inside an index. Every document is associated with a unique identifier called the UID.
- Shard
  - Indexes are horizontally subdivided into shards. This means each shard contains all the properties of document but contains less number of JSON objects than index. The horizontal separation makes shard an independent node, which can be store in any node.
- Replicas
  - Elasticsearch allows a user to create replicas of their indexes and shards.

## Rest API in EL

Every feature of Elasticsearch is exposed as a REST API:

1. **Index API** – Used to document the Index
2. **Get API** – Used to retrieve the document
3. **Search API** – Used to submit your query and get the result
4. **Put Mapping API** – Used to override default choices and define our own mapping

Elasticsearch has its own Query Domain Specific Language, where you specify the query in JSON format. Other queries can also be nested based on your need. Real projects require search on different fields by applying some conditions, different weights, recent documents, values of some predefined fields, and so on. All such complexity can be expressed through a single query. 

![im](https://cdn-gcp.marutitech.com/wp-media/2017/06/ed18c2ed-indexing-and-searching-in-elasticsearch.png)