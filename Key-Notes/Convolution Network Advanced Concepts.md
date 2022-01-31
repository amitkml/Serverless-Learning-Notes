

[TOC]

# Convolution Neural Network Advanced Concepts

## Batch Normalization

Batch norm acts by removing the mean and normalizing the standard deviation of a channel of activations
$$
x
←
x
–
μ
(
x
)
/
σ
(
x
)
$$
Statistics μ(x),σ(x)μ(x),σ(x) are computed over pixels in an image *and* examples in a batch. They are frozen at test time. A learnable output mean β and standard deviation γ are usually applied, potentially undoing everything:
$$
x
←
(x
–
μ
(
x
)
/
σ
(
x
)
)
γ
+
β
$$
Empirically batch norm has been extremely successful especially for training conv nets. Many proposed alternatives have failed to replace it.

### Advantage

- it stabilises optimisation allowing much higher learning rates and faster training
- it injects noise (through the batch statistics) improving generalisation
- it reduces sensitivity to weight initialisation
- it interacts with weight decay to control the learning rate dynamics

![im](https://296830-909578-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2019/06/stress_test_lr-3.svg)

![im](https://296830-909578-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2019/06/Artboard-1-7-1-1.svg)

The learning rate, plotted first, is increased exponentially over time as a stress test. The second plot shows training accuracy.

It can be seen that the **network with batch norm is stable over a much larger range of learning rates (note the log scale on the x-axis in the second plot.)** The ability to use high learning rates allows training to proceed much more rapidly for the model with batch norm.

### Disadvantages

 Batch norm has several drawbacks:

- it’s slow (although node fusion can help)
- it’s different at training and test time and therefore fragile
- it’s ineffective for small batches and various layer types
- it has multiple interacting effects which are hard to separate.

## Image Normalization

## Image Equalization

## Regularization

## Group Convolution

Traditionally we build CNN layers one after another with increased no of filter as we get deeper. Reason for increasing no of Kernels as we go deeper is to learn more features. We build a layer with increasing no of FILTERS followed by bottleneck layer and again we repeat the same till we reach receptive field of the object.

Another contra thought process can be to **learn more no. of features, we could also create two or more models that train and back-propagate in parallel**. This process of using different set of convolution filter groups on same image is called as grouped convolution.

Ina  nutshell it means create a deep network with some number of layers and then replicate it so that there are more than 1 pathways for convolutions on a single image/batch of images. Alexnet is first one to use this type of network architecture.

![AlexNet](https://github.com/titu1994/Keras-ResNeXt/raw/master/images/Cardinality.PNG?raw=true)

![Image](https://cdn-images-1.medium.com/max/1000/1*arJJYgK-_7VcuKKX1TCKMA.png)

Such parallel network methodologies allows us to use parallel threading of GPU and each of the thread can go into parallel mode.

Advantage of Group Convolution:

- Allows us to have wider network rather than deeper network
- Training can be done through parallelism
  - Where we split the dataset into chunks and then we train on each chunk. Intuitively, each chunk can be understood as a mini batch used in mini batch gradient descent.
  - We try to parallelize the model such that we can take in as much as data as possible. Grouped convolutions enable efficient model parallelism, so much so that Alexnet was trained on GPUs with only 3GB RAM.

Keras2.0 has added new function GroupConv2d(https://tensorlayer.readthedocs.io/en/stable/modules/layers.html?highlight=GroupConv2d#tensorlayer.layers.GroupConv2d) to cater to group convolution but unfortunately i could not locate any corresponding Keras function for this.

```
>>> net = tl.layers.Input([8, 24, 24, 32], name='input')
>>> groupconv2d = tl.layers.QuanConv2d(
...     n_filter=64, filter_size=(3, 3), strides=(2, 2), n_group=2, name='group'
... )(net)
>>> print(groupconv2d)
>>> output shape : (8, 12, 12, 64)
```



## More on Depthwise Separable Convolution

# Image Augmentation Advanced Concepts

## Spatial Dropout

## CutOut

## Smart Augmentation

## Sample Pairing

It helps us to generate more input image as shared below. By using two images randomly selected from the training set, we can generate N^2 new samples. paper can be [found](https://t.co/YnORpOhu8H).

![Image](https://pbs.twimg.com/media/DTzRxqOUMAEyp77.jpg)

- Here is how a realistic data will looks like after **samplepairing**. We take same two image of same class and then apply sample pairing.

- Even though the training accuracy will not be high with **SamplePairing**, both the training and validation accuracy quickly improves when we stop the **SamplePairing** as the final fine-tuning phase of training. 

![1562781919313](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1562781919313.png)

## RECAP

## RL Based Image Augmentation Policy 	

## Mix-up

# Visualization of CNN Layers and Model Interpretability

## Building Block of Model Interpretability

Google Published analysis link is [Model Interpretability](http://distill.pub/2018/building-blocks)

**Aim**

- What individual neurons do in network rather than "what is interesting to network"
- Allow us to see how neurons in the middle of network are detectors of - shape, patches, building etc and help network classification layer to classify the object

*For example, we can see things like how a network detects a floppy ear, and then that increases the probability it gives to the image being a “Labrador retriever” or “beagle”*.

**Visualizations of neurons in GoogLeNet. Neurons in higher layers represent higher level ideas** ![Image](https://3.bp.blogspot.com/-H2TTi9QTprM/Wp7YRKxFeKI/AAAAAAAACbs/w9kffufxDlsTxQnT994tmV6sbTVoeB0XACLcBGAs/s640/image2.png)

 Normally, if we ask which neurons fire, we get something meaningless like “**neuron 538 fired a little bit**,” which isn’t very helpful even to experts. Our techniques make things more meaningful to humans by attaching visualizations to each neuron, so we can see things like “the floppy ear detector fired”. It’s almost a kind of MRI for neural networks.

[![img](https://4.bp.blogspot.com/-k-8_IPsExgU/Wp7dqHmlzDI/AAAAAAAACcg/sJINo6soS7stbMZUdGeM6eMukaU__-rSACLcBGAs/s640/SemanticDict2-ezgif-crop.gif)](https://4.bp.blogspot.com/-k-8_IPsExgU/Wp7dqHmlzDI/AAAAAAAACcg/sJINo6soS7stbMZUdGeM6eMukaU__-rSACLcBGAs/s1600/SemanticDict2-ezgif-crop.gif)

So not only can we see that the network detected a floppy ear, but we can also see how that increases the probability of the image being a labrador retriever.



![Image](https://3.bp.blogspot.com/-mW_HDbg0TAo/Wp7Y5htkXII/AAAAAAAACb8/liKR4U8sZIYlCsisYV-2AmuxNkX2OHnSgCLcBGAs/s640/image5.png)

[Lucid](https://github.com/tensorflow/lucid), a neural network visualization library building off our work on DeepDream. It allows you to make the sort of lucid feature visualizations we see above, in addition to more artistic DeepDream images.

These [notebook](https://github.com/tensorflow/lucid#notebooks) make it extremely easy to use Lucid to reproduce visualizations in our article! Just open the notebook, click a button to run code — no setup required!

| [![img](https://3.bp.blogspot.com/-flLB6dGguTM/Wp7ZGqNHVII/AAAAAAAACcE/8GAYagtus_sX3oqGY9KgxFqkvKwEctnPgCLcBGAs/s640/image3.png)](https://3.bp.blogspot.com/-flLB6dGguTM/Wp7ZGqNHVII/AAAAAAAACcE/8GAYagtus_sX3oqGY9KgxFqkvKwEctnPgCLcBGAs/s1600/image3.png) |
| ------------------------------------------------------------ |
| In colab notebooks you can click a button to run code, and see the result below.![Image](https://3.bp.blogspot.com/-flLB6dGguTM/Wp7ZGqNHVII/AAAAAAAACcE/8GAYagtus_sX3oqGY9KgxFqkvKwEctnPgCLcBGAs/s640/image3.png) |

## Master References

Standford University Deep Learning Video on CNN Layers visualization.

[![CNN](http://img.youtube.com/vi/6wcs6szJWMY/0.jpg)](http://www.youtube.com/watch?v=6wcs6szJWMY "CNN-Visualisation")





## GRAD-CAM

![GRAD](https://github.com/amitkayal/akDeepLearningMaster/blob/master/Guided-Back-Prop.JPG?raw=true)

Here we take a convolution layer and generate heatmap to understand what that layer is looking for. Computes gradient values w.r.t to pixels.

Image comes out better when we pass on only +ve values through reLU as shown below.

![1561824748903](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1561824748903.png)



## Occlusion Experiments

Mask part of images and feed to CNN to draw the heatmap with probability of the class. Then this process of changing the mask location goes on and we map the heatmap with probability.

![Image](https://github.com/amitkayal/akDeepLearningMaster/blob/master/Occlusion%20Experiment.JPG?raw=true)

Idea here is that if we block a part of Image **which drastically changes image class probability then probably this blocked part of the image is what CNN is looking for classification**. Red here  corresponding to low class probability whereas white color corresponding to high probability.

## Saliency Maps

![SP Image](https://github.com/amitkayal/akDeepLearningMaster/blob/master/Saliency-Maps-Details.JPG?raw=true)

# Optimisation Functions

## Gradient Descents

Following are the variants of GD and different of these algorithm is the amount of data.

### SGD

- Batch size of 1
- calculate gradient for each input data and change weights; so we learn a dog and then change weights. Now a cat comes and again we change the weights. So we will never be able to have our weights stable.
- Inefficient from computation perspective
- Takes lot of time to find out global minima

![1563383400684](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383400684.png)

![image](https://image.slidesharecdn.com/anoverviewofgradientdescentoptimizationalgorithms-170414055411/95/an-overview-of-gradient-descent-optimization-algorithms-13-638.jpg?cb=1492149859)

### Mini Batch GD

- Batch size is defined
- Calculate gradient for each batch and then change weights
- Optimal from performance aspect

![1563383800230](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383800230.png)

![1563383895112](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383895112.png)

### Batch GD

- Batch size is whole data set
- Calculate gradient for whole dataset and then change weights. Here we  do forward prop for every image, then store the loss value for each of them; calculate the average loss and then do backprop to change the weights.
- Worst from efficiency and performance aspect

![1563383214087](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383214087.png)

![1563383286027](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383286027.png)

![1563383719895](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563383719895.png)

### Challenges

- Setting and changing LR is very complicated in Mini Batch GD
- Data is sparse
  - Features have very different frequencies
  - we should not update all of them with same gradients
  - If we update with same LR then it will cause same update for rarely occurring data
- Very tough to come out from saddle points

![1563860887170](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563860887170.png)

### Solution of Issus from Gradient Descent

#### Momentum based Gradient

![Momentum](https://image.slidesharecdn.com/anoverviewofgradientdescentoptimizationalgorithms-170414055411/95/an-overview-of-gradient-descent-optimization-algorithms-28-638.jpg?cb=1492149859)

![Moment](https://image.slidesharecdn.com/anoverviewofgradientdescentoptimizationalgorithms-170414055411/95/an-overview-of-gradient-descent-optimization-algorithms-31-638.jpg?cb=1492149859)

**Saddle point has very less gradient and hence change in weight due to delta caused by derivative will be very less. So with standard GD, it will be extremely difficult to come out from flat plateaus. So in momentum concept we always refer the history of earlier movements (movement in direction of history) apart of current derivative as shared in solution because we try to always refer the past opinion also.**

![1563555106881](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563555106881.png)

```
Here v(t-1) is the earlier velocity and that is multiplied by a hyper-parameter gamma. So at any point current velocity is influenced by earlier velocity multiplied by a hyper-parameter and derivative of loss w.r.t weights multiplied by another hyper-parameter.
```

![1563555548980](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563555548980.png)

![1563555849461](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563555849461.png)

```
We monitor the slope of slope (curvature) as shared below and if the curvature is getting steeper then we assume that minima(bottom) is far from current point and we should take big jump. So we can take  big jump (we can use here momentum or learning rate of higher values)  to go more.
```

![1563451875466](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563451875466.png)

similarly we take very less jump when slope is getting shallower and we interpret that our current position may be near to bottom.

![1563452097167](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563452097167.png)

**Curvature is slope of slope or hessian**. It helps us to reduce no of steps in reaching bottom/minima but lot complex to compute. So we have to balance complexity and speed.

##### Why momentum works

- With Stochastic Gradient Descent we don’t compute the exact derivate of our loss function. Instead, we’re estimating it on a small batch. Which means we’re not always going in the optimal direction, because our derivatives are ‘noisy’. 

- Just like in my graphs above. So, exponentially weighed averages can provide us a better estimate which is closer to the actual derivate than our noisy calculations. This is one reason why momentum might work better than classic SGD.

- SGD will tend to oscillate across the narrow ravine since the negative gradient will point down one of the steep sides rather than along the ravine towards the optimum. Momentum helps accelerate gradients in the right direction.

  ![image](https://miro.medium.com/max/513/1*uTiP1uRl2CaHaA-dFu3NKw.gif)

  ![img](https://miro.medium.com/max/513/1*uTiP1uRl2CaHaA-dFu3NKw.gif)

  Left — SGD without momentum, right— SGD with momentum.

##### What are issues with momentum?

![1563557109627](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563557109627.png)

![1563557173423](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563557173423.png)

#### Nesterov accelerated Gradient descent

Here first we move by history of movements then calculate the derivative to again move by derivative. Intuition here is that since we need to move a factor of past velocity(movement in direction of history) always so why we should not first move and then decide how much further we should move which is given by gradient and hopefully it will reduce number of u-turn. **So rule here is that first move by history and then look at that point to calculate the derivative to decide further movement.**

![1563557547552](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563557547552.png)

#### Adaptive Update of LR

- Adapt our updates(learning rate 𝜼 for all parameters 𝜽) to each individual parameter to perform larger or smaller updates depending on their importance.
- We want to vary LR depending on update history. Initially we want to have higher learning rate and as we reach to near to mina when gradient is low and that means our features are there more and hence we need to learn more and so learning rate has to be reduced. All the following optimizer following this principle of varying LR. Aim is "**Decay the LR for parameters in proportion to their update history (fewer updates, lesser history)**"

## AdaGrad

Adagrad adapts the learning rate to the parameters

- Performing larger updates for infrequent
- Performing smaller updates for frequent parameters.
- It uses a different learning rate for every parameter 𝜃𝑖 at every time step 𝑡
- It is well-suited for dealing with sparse data.
- It greatly improved the robustness of SGD.
- It eliminates the need to manually tune the learning rate.
- **Main weakness is its accumulation of the squared gradients in the denominator**

Ex.

- Training large-scale neural nets at Google that learned to recognize cats in Youtube videos.

![1563864161296](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563864161296.png)

**Observations**: 

- Here in 2nd equation, we are trying to do something to LR and if we remove the denominator then 2nd equation become vanilla GD. Aim of this 2nd equation is "Features/Weights which are receiving lot of updates(in past) should have denominator high so that LR is less and hence effective update is less which will enable us to learn more. Similarly features/weights which are receiving less update(in past) their denominator will be low and hence effective LR will be more." 
- 1st equation calculate the velocity and here for features/weights which are receiving lot of updates will have less gradient but since we are updating lot of times, so we have gained momentum which will increase the velocity/momentum. So this will help in 2nd equation to reduce LR.

![Ada](https://image.slidesharecdn.com/anoverviewofgradientdescentoptimizationalgorithms-170414055411/95/an-overview-of-gradient-descent-optimization-algorithms-46-638.jpg?cb=1492149859)

![Image](https://image.slidesharecdn.com/gradientdescentoptimizer-180202151844/95/gradient-descent-optimizer-38-638.jpg?cb=1517584982)

### Advantages and Disadvantages

- Parameters corresponding to sparse features get better updates
- LR decays aggressively and become very low and we get difficulty in reaching minima



## RMS Prop

![1563866865460](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563866865460.png)![1563866902699](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563866902699.png)

Here we have added a decay factor into velocity or the manner in which we are collecting the history. This factor beta causes exponentially decay of velocity and hence prevent rapid growth of LR.

**Velocity in Adagrad**

![1563867919394](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563867919394.png)

**Velocity in RMS Prop**

![1563867960102](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563867960102.png)

**Comparing Adagrad and RMSProp**

- Adagrad was using history to change the weights while RMSProp was using history to manipulate learning rate. While both of them were looking "How to reach minima quickly" but their approach was different.

![1563868330244](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563868330244.png)

## Adam

- Taking momentum and RMS Prop together
- Storing an exponentially decaying average of past squared gradients 𝑣𝑡 like Adadelta and RMSprop
- Keeping an exponentially decaying average of past gradients 𝑚𝑡, similar to momentum.

![1563871697029](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563871697029.png)

## Assumptions vs Performance

![1563452642174](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1563452642174.png)

















