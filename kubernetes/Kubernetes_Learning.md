# Kubernetes

[TOC]

[^My Kubernetes Notes]: Kubernetes Learning

## Difference between JSON, YML and XML

![im](https://www.devopsschool.com/blog/wp-content/uploads/2021/07/Comparison-XML-JSON-YAML-1.jpg)

![im](https://www.devopsschool.com/blog/wp-content/uploads/2021/07/Comparison-XML-JSON-YAML-3.png)

![im](https://ipcisco.com/wp-content/uploads/2020/05/json-versus-xml-versus-yaml-1-540x540.jpg)

### YML Syntax

![im](https://linuxbuz.com/wp-content/uploads/2020/07/ansible-playbook-yaml-image4.png.webp)

![im](https://linuxbuz.com/wp-content/uploads/2020/07/ansible-playbook-yaml-image5-1.png.webp)

![im](https://linuxbuz.com/wp-content/uploads/2020/07/ansible-playbook-yaml-image6.png.webp)

![im](https://linuxbuz.com/wp-content/uploads/2020/07/ansible-playbook-yaml-image7.png.webp)

**Here we see dictionary within another dictionary.**

![1632123965632](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1632123965632.png)

![1632124047707](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1632124047707.png)

## Kubernetes Platform Concept

Kubernetes concepts are built around microservices architectures and I’ll explain these using the above image as a reference starting from right to left.

- A Service is a logical abstraction of *pods*.A Service is what is exposed outside the Kubernetes cluster. It has an IP address that does not change no matter how many pods are created or re-instantiated to support a particular *Service*.

- A pod is comprised of one or more strictly dependent containers sharing storage, network (e.g. IP address) and running options. Pods are the minimum deployable unit in Kubernetes and it runs in a single node. Kubernetes restart pods in case of pod failure and re-schedule them to other nodes in case of node failure.



![im](https://www.wwt.com/api/attachments/5c8152ffccf2270045b6ae92/file)

## Architecture

It is **declarative language** and not imperative. It is master and agent architecture. 

- Kubectl is a client which is talking to API server.

![1633689787204](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633689787204.png)

### PODS

- can have one or multi container
- each POD has its address

![1633690559219](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633690559219.png)![1633691220602](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633691220602.png)



### Replicaset

![1633690679621](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633690679621.png)

### Secrets

![1633690807411](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633690807411.png)

### Deployments

![1633690852771](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633690852771.png)



### DaemeonSets

![1633690900535](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633690900535.png)

### ingress

- it is a kind of controller and does traffic reroute
- Ingress is a type of loadbalancer

![1633691019270](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633691019270.png)

### cronJobs

![1633691073010](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633691073010.png)

### CRD

- Customer controller

![1633691098131](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633691098131.png)

### Namespace

![1633692257360](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633692257360.png)

#### storage

![1633694247617](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633694247617.png)



### volumeclaim in pod

![1633694279168](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1633694279168.png)



## Replicaset and pod

There is one major difference between replication controller and replica set. **ReplicaSet requires a selector definition.** The selector section helps the replica set identify what pods fall under it.

**But why would you have to specify what pods fall under it** if we have provided the contents of the pod definition file itself in the template ?
**It’s because replicas set can also manage pods that were not created as part of the replica at creation.**

**The matchLabels selector simply matches the labels specified under it to the labels on the pods.**

This way the replica set knows which pods to monitor. The same concept of labels and selectors is used in many other places throughout Kubernetes.

![im](https://miro.medium.com/max/1400/1*J7vyXmySTT25wuflaKkLvw.png)

![1632591404469](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1632591404469.png)

Let’s create a ReplicaSet that will ensure that we are having four pods serving Nginx. A YAML definition file for this controller may look as follows:

Let’s examine the definition file that was used to create our ReplicaSet:

- The apiVersion for this object is currently app/v1

- The kind of this object is ReplicaSet

- In the metadata part, we define the name by which we can refer to this ReplicaSet. We also define a number of labels through which we can identify it.

- The spec part is mandatory in the ReplicaSet object. It defines:

- - The number of replicas this controller should maintain. It default to 1 if it was not specified.
  - The selection criteria by which the ReplicaSet will choose its pods. Be careful not to use a label that is already in use by another controller. Otherwise, another ReplicaSet may acquire the pod(s) first. Also notice that the labels defined in the pod template (spec.template.metadata.label) cannot be different than those defined in the matchLabels part (spec.selector).
  - The pod template is used to create (or recreate) new pods. It has its own metadata, and spec where the containers are specified. You can refer to our article for more information about pods.	

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web
  labels:
	env: dev
	role: web
spec:
  replicas: 4
  selector:
	matchLabels:
  	  role: web
  template:
	metadata:
  	  labels:
    	    role: web
	spec:
  	  containers:
  	  - name: nginx
    	    image: nginx
```

### Is Our ReplicaSet The Owner Of Those Pods?

OK, so we do have four pods running, and our ReplicaSet reports that it is controlling four pods. In a busier environment, you may want to verify that a particular pod is actually managed by this ReplicaSet and not by another controller. By simply querying the pod, you can get this info:

```bash
kubectl get pods web-6n9cj -o yaml | grep -A 5 owner
```

The first part of the command will get all the pod information, which may be too verbose. Using grep with the -A flag (it takes a number and prints that number of lines after the match) will get us the required information as in the example:

```yaml
ownerReferences:
  - apiVersion: extensions/v1beta1
	blockOwnerDeletion: true
	controller: true
	kind: ReplicaSet
	name: web
```

### Scaling And Autoscaling ReplicaSets

You can easily change the number of pods a particular ReplicaSet manages in one of two ways:

1. Edit the controllers configuration by using `kubectl edit rs ReplicaSet_name` and change the replicas count up or down as you desire.
2. Use kubectl directly. For example, `kubectl scale --replicas=2 rs/web`. Here, I’m scaling down the ReplicaSet used in the article’s example to manage two pods instead of four. The ReplicaSet will get rid of two pods to maintain the desired count. If you followed the previous section, you may find that the number of running pods is three instead of two; as we isolated one of the pods so it is no longer managed by our ReplicaSet.

ReplicaSets can also be used to adapt the number of pods according to the CPU load that the node is having. To enable autoscaling for our web ReplicaSet, we can use the following command:

```yaml
kubectl autoscale rs web --max=5
```

Copy

This will use the [Horizontal Pod Autoscaler (HPA)](https://www.magalix.com/blog/kubernetes-autoscaling-101) with the ReplicaSet to increase the number of pods when the CPU load gets higher, but it should not exceed five pods. When the load decreases, it cannot have less than the number of pods specified before (two in our example).

### Deleting ReplicaSets

As with other [Kubernetes](https://www.magalix.com/blog/kubernetes-101-concepts-and-why-it-matters) objects, a ReplicaSet can be deleted by issuing a kubectl command like the following:

```bash
kubectl delete rs ReplicaSet_name
```

Copy

Alternatively, you can also use the file that was used to create the resource (and possibly, other resource definitions as well) to delete all the resources defined in the file as follows:

```bash
kubectl delete -f definition_file.yaml
```



## Kubernetes Networking Guide

![im](https://i0.wp.com/digitalvarys.com/wp-content/uploads/2019/10/image.png?w=1055&ssl=1)

There are five essential things to understand about networking in Kubernetes

- Communication between containers in the same pod
- Communication between pods on the same node
- Communication between pods on different nodes
- Communication between pods and services
- How does DNS work? How do we discover IP addresses?

![Kubernetes Networking Overview](https://matthewpalmer.net/kubernetes-app-developer/articles/networking-overview.png)

### Communication between containers in the same pod

First, if you've got two containers running in the same pod, how do they talk to each other?

This happens via `localhost` and port numbers. Just like when you’re running multiple servers on your own laptop.

This is possible because containers in the same pod are in the same network namespace – they share networking resources.

### What is a network namespace?

It’s a collection of network interfaces (connections between two pieces of equipment on a network) and routing tables (instructions for where to send network packets).

Namespaces are helpful because you can have many network namespaces on the same virtual machine without collisions or interference.

(You wouldn’t want all your pods to run containers that listen on port 3000 in the same namespace – they’d all collide!)

There’s a secret container that runs on every pod in Kubernetes. This container’s #1 job is to keep the namespace open in case all the other containers on the pod die. It’s called the `pause` container.

So, each pod gets its own network namespace. Containers in the same pod are in the same network namespace. This is why you can talk between containers via localhost and why you need to watch out for port conflicts when you’ve got multiple containers in the same pod.

![Networking Between Containers in Kubernetes](https://matthewpalmer.net/kubernetes-app-developer/articles/same-pod.gif)

### Communication between pods on the same node

Each pod on a node has its own network namespace. Each pod has its own IP address.

And each pod thinks it has a totally normal ethernet device called `eth0` to make network requests through. But Kubernetes is faking it – it’s just a virtual ethernet connection.

Each pod’s `eth0` device is actually connected to a virtual ethernet device in the node.

A virtual ethernet device is a tunnel that connects the pod’s network with the node. This connection has two sides – on the pod’s side, it’s named `eth0`, and on the node’s side, it’s named `vethX`.

Why the `X`? There’s a `vethX` connection for every pod on the node. (So they’d be `veth1`, `veth2`, `veth3`, etc.)

When a pod makes a request to the IP address of another node, it makes that request through its own `eth0` interface. This tunnels to the node’s respective virtual `vethX` interface.

But then how does the request get to the other pod?

The node uses a network bridge.

### What is a Network Bridge?

A network bridge connects two networks together. When a request hits the bridge, the bridge asks all the connected devices (i.e. pods) if they have the right IP address to handle the original request.

(Remember that each pod has its own IP address and it knows its own IP address.)

If one of the devices does, the bridge will store this information and also forward data to the original back so that its network request is completed.

In Kubernetes, this bridge is called `cbr0`. Every pod on a node is part of the bridge, and the bridge connects all pods on the same node together.

![Networking Between Pods in Kubernetes](https://matthewpalmer.net/kubernetes-app-developer/articles/pods-on-node.gif)

### Communication between pods on different nodes

But what if pods are on different nodes?

Well, when the network bridge asks all the connected devices (i.e. pods) if they have the right IP address, none of them will say yes.

(Note that this part can vary based on the cloud provider and networking plugins.)

After that, the bridge falls back to the default gateway. This goes up to the cluster level and looks for the IP address.

At the cluster level, there’s a table that maps IP address ranges to various nodes. Pods on those nodes will have been assigned IP addresses from those ranges.

For example, Kubernetes might give pods on node 1 addresses like `100.96.1.1`, `100.96.1.2`, etc. And Kubernetes gives pods on node 2 addresses like `100.96.2.1`, `100.96.2.2`, and so on.

Then this table will store the fact that IP addresses that look like `100.96.1.xxx` should go to node 1, and addresses like `100.96.2.xxx` need to go to node 2.

After we’ve figured out which node to send the request to, the process proceeds the roughly same as if the pods had been on the same node all along.

![Networking Between Nodes in Kubernetes](https://matthewpalmer.net/kubernetes-app-developer/articles/node-to-node.gif)

### Communication between pods and services

One last communication pattern is important in Kubernetes.

In Kubernetes, a service lets you map a single IP address to a set of pods. You make requests to one endpoint (domain name/IP address) and the service proxies requests to a pod in that service.

This happens via `kube-proxy` a small process that Kubernetes runs inside every node.

This process maps virtual IP addresses to a group of actual pod IP addresses.

Once `kube-proxy` has mapped the service virtual IP to an actual pod IP, the request proceeds as in the above sections.

### How does DNS work? How do we discover IP addresses?

DNS is the system for converting domain names to IP addresses.

Kubernetes clusters have a service responsible for DNS resolution.

Every service in a cluster is assigned a domain name like `my-service.my-namespace.svc.cluster.local`.

Pods are automatically given a DNS name, and can also specify their own using the `hostname` and `subdomain` properties in their YAML config.

So when a request is made to a service via its domain name, the DNS service resolves it to the IP address of the service.

Then `kube-proxy` converts that service's IP address into a pod IP address. After that, based on whether the pods are on the same node or on different nodes, the request follows one of the paths explained above.

### Service

#### Nodeport

Nodeport type exposed pod to external network with the same target port so user can access it using  worker node ip and port it is exposed. traffic will be sent to respective pod through service.

A **NodePort** Service exposes an app to the outside world via a port mapping on every node in the cluster. It looks like this in a YAML file:

![im](https://www.bogotobogo.com/DevOps/Docker/images/Docker-Kubeernetes-Pods-Services/three-ports-3.png)

![im](https://1.bp.blogspot.com/-cV8Kd8UMgHM/XrVgU3azgoI/AAAAAAAABwE/CI0MpWD4lgMyscBvMVCxTnOmv7XP1pvzQCLcBGAsYHQ/s640/kubernetes%2Bnodeport%2Bexamples.JPG)

![im](https://matthewpalmer.net/kubernetes-app-developer/articles/nodeport.png)

Here is the YAML file which shows how the nodeport and pod is linked by selector.

This time the YAML defines three ports:

- port
- targetPort
- nodePort

**port** and **targetPort** work the same as they do with ClusterIP Services. The **nodePort** is  a TCP/UDP port between 30,000 and 32,767 that is mapped on every  cluster node and exposes the Service outside of the cluster. Basically,  any client outside of the cluster can hit any cluster node on the  nodePort value (31111 in our example) and reach the ClusterIP Service  inside the cluster and eventually reach Pods/containers

![im](https://img1.wsimg.com/isteam/ip/ada6c322-5e3c-4a32-af67-7ac2e8fbc7ba/nodeport-yaml.png/:/rs=w:1280)

Services match a set of Pods using [labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels),  a grouping primitive that allows logical operation on objects in  Kubernetes. Labels are key/value pairs attached to objects and can be  used in any number of ways:

- Designate objects for development, test, and production
- Embed version tags
- Classify an object using tags

![im](https://d33wubrfki0l68.cloudfront.net/7a13fe12acc9ea0728460c482c67e0eb31ff5303/2c8a7/docs/tutorials/kubernetes-basics/public/images/module_04_labels.svg)

#### LoadBalancer

You can set a service to be of type `LoadBalancer` the same way you’d set `NodePort`—
specify the `type` property in the service’s YAML. There needs to be some external
load balancer functionality in the cluster, typically implemented by a cloud 
provider.

Kubernetes offers a **LoadBalancer Service**. This builds on top of *NodePort* and *ClusterIP* constructs and exposes a Service to the internet via one of your cloud’s native load balancers. 

It’s important to understand that a Kubernetes LoadBalancer Service  will build an internet-facing load balancer on your cloud platform as  well as all the constructs required to route traffic all the way back to  Pods/containers running in your Kubernetes cluster.

![im](https://1.bp.blogspot.com/-YnmfMJGiug4/XrVgaV8fKiI/AAAAAAAABwI/MfVvrEM9kh08NpbUU5CCQfnmjJ54FXs0wCLcBGAsYHQ/s640/kubernetes%2Bloadbalancer%2Bexamples.JPG)

![im](https://matthewpalmer.net/kubernetes-app-developer/articles/loadbalancer.png)

#### Ingress

`NodePort` and `LoadBalancer` let you expose a service by specifying that  value in the service’s `type`. Ingress, on the other hand, is a completely independent resource to your service. You declare, create and destroy it separately to your services. 

This makes it decoupled and isolated from the services you want to expose.  It also helps you to consolidate routing rules into one place.

The one downside is that you need to configure an Ingress Controller for your cluster. But that’s pretty easy—in this example, we’ll use the Nginx Ingress Controller.

![im](https://matthewpalmer.net/kubernetes-app-developer/articles/ingress.png)

#### ClusterIP

**In any given cluster node there can be multiple types of Pods viz**

- **Front-end pod**
- **Backend** pods
- **Redis** pods
- **Database** MySQL pods

Each of these types of **pods** lying within an internal cluster will have a different internal network IP, which is liable to change. In order, to talk to each other. For example, the front-end pod may be talking to the backend pods, backend pods, in turn, may require to talk to **Redis** pods, there is the requirement for a more reliable and efficient mechanism, **ClusterIP** is our friend here.

![im](https://miro.medium.com/max/2000/1*a8LWTD3acs-HIioTbcDf2Q.png)

As  can be clearly seen that whenever a front-end pod wants to communicate  with backend pods, it has to simply communicate to a ClusterIP service  named **backend**, which is a single endpoint  service managing the communication to all backend pods. Similarly, if  backend pods need to access the Redis cache service it has to make a  service call to cluster IP service named **Redis**, which will allow the backend pods to communicate to respective Redis pods.

**To summarize**: These common backend / Redis services are the **virtual IP’s** also known as C**lusterIP type service,** which effectively allows one pod type to communicat	e to another Pod type in the given cluster Node.

**my-cluster-ip-demo.yaml file:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: Backend
spec:
  type: ClusterIP
  ports:
    - targetPort: 80
      port: 80  selector:
    
      name: my-demo-pod 
      type: front-end-app
```

**my-demo-pod.yaml file :**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-demo-pod
  labels:
    app: my-test-pod 
    type: mobile-front-end-appspec:
  containers:  - name: nginx-container
    image: nginx
```

**So let’s first create a pod file as defined in our, my-demo-pod.yaml file above**

```
$ kubectl apply -f test-pod.yaml
```

**Output**:

Our pod file my-pod-demo has been created and running

![img](https://miro.medium.com/max/700/1*ccBDHne8lgoyMa9Md-sjRQ.png)

**Now that we have our pod file up and running, it’s time to create service as defined in our “my-cluster-ip-demo.yaml file “**

```yaml
$ kubectl create -f my-cluster-ip-demo.yaml
```

**Output:**

![img](https://miro.medium.com/max/2000/1*QibwJdEV9nS-fe5BoC2uwQ.png)

Our  service of type ClusterIP has been successfully created and has been  bound to our demo using pod using selector as s	hown below :

```
$ kubectl describe svc backend
```

![img](https://miro.medium.com/max/2000/1*NmuRSDDgp3lkEf7OHTmf1A.png)

## Microservice Architecture using Kubernetes

Lets take the following simplest example of micro services deployment.  it's just a simple
example of the various types of pieces and languages you might see (queues, persistent data, etc), and how to deal with them in Kubernetes at a basic level.

- A front-end web app in [Python](https://github.com/dockersamples/example-voting-app/blob/master/vote) or [ASP.NET Core](https://github.com/dockersamples/example-voting-app/blob/master/vote/dotnet) which lets you vote between two options
- A [Redis](https://hub.docker.com/_/redis/) or [NATS](https://hub.docker.com/_/nats/) queue which collects new votes
- A [.NET Core](https://github.com/dockersamples/example-voting-app/blob/master/worker/src/Worker), [Java](https://github.com/dockersamples/example-voting-app/blob/master/worker/src/main) or [.NET Core 2.1](https://github.com/dockersamples/example-voting-app/blob/master/worker/dotnet) worker which consumes votes and stores them in…
- A [Postgres](https://hub.docker.com/_/postgres/) or [TiDB](https://hub.docker.com/r/dockersamples/tidb/tags/) database backed by a Docker volume
- A [Node.js](https://github.com/dockersamples/example-voting-app/blob/master/result) or [ASP.NET Core SignalR](https://github.com/dockersamples/example-voting-app/blob/master/result/dotnet) webapp which shows the results of the voting in real time

![im](https://raw.githubusercontent.com/dockersamples/example-voting-app/master/architecture.png)

**Quick Notes about the architecture are:**

- voting app requires connection with redis app
- Worker app requires connection with redis and db app
- result app requires connection with db app 

**Steps are**

- Deploy PODS with replica sets
- Create Service (**ClusterIp**)
  - redis (This will allow voting and worker app to access redis app)
  - db (This will allow worker and result app to access db app)
- Create Service (Nodeport)
  - voting-app (will allow external users to access voting-app)
  - result-app (will allow external users to access result app)

![im](https://www.wwt.com/api/attachments/5c8152c1c4188b00483b1190/file)

## Kubernetes in AWS

It is called EKS in AWS and and managed service.

# References

- https://docs.microsoft.com/en-us/learn/modules/aks-workshop/?wt.mc_id=github_#AzureHappyHours_webinar_reactor
- https://aka.ms/YoutubeMFSTReactor