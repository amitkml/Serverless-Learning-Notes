# Kubernetes



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