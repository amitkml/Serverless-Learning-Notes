### Checking that Elasticsearch is running

You can test that your Elasticsearch node is running by sending an HTTP request to port `9200` on `localhost`:

```
curl -X GET "localhost:9200/?pretty"
```

response will be as similar to following.

```
{
  "name" : "BLR-AA202394",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "pYm2eSPlTh-EUo8hcVce2A",
  "version" : {
    "number" : "7.15.2",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "93d5a7f6192e8a1a12e154a2b81bf6fa7309da0c",
    "build_date" : "2021-11-04T14:04:42.515624022Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

