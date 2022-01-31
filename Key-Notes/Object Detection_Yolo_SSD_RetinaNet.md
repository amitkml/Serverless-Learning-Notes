[TOC]

# Object Detection

## What is object detection?

As the name goes, it involves detecting the objects in an image along with their location, typically using a bounded box. 

![1568988748301](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1568988748301.png)

## Object Detection as Regression?

![1581187729419](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187729419.png)

We use same Convolution network which was used for image classification into Object localization

![image](https://miro.medium.com/max/1094/1*4Eac89VWR8tBzrf-HTVAMA.png)

**Predicting the location of the object along with the class is called object Detection.** In place of predicting the class of object from an image, we now have to predict the class as well as a rectangle(called bounding box) containing that object. It takes 4 variables to uniquely identify a rectangle. So, for each instance of the object in the image, we shall predict following variables:

- *class_name,* 

- *bounding_box_top_left_x_coordinate,*

- *bounding_box_top_left_y_coordinate,*

- *bounding_box_width,*

- *bounding_box_height*

We can have multi-class object detection problem where we detect multiple kinds of objects in a single image as similar to  multi-label image classification problems.

![img](https://cv-tricks.com/wp-content/uploads/2017/12/Multi-class-object-detection.png)

## Classification based Object detector

All the methods discussed handled d**etection as a classification problem by building a pipeline where first object proposals are generated and then these proposals are send to classification/regression heads.** 

### Sliding Window Approach

The **Sliding Window algorithm** is one way of achieving the first step where a rectangular window is slid through the original image and each of the grid box is used as a smaller piece, like the white box shown in the image below.![Image](https://miro.medium.com/max/1094/1*fUfX60od5YMFseccIxyFjw.gif)

![Image](https://cv-tricks.com/wp-content/uploads/2017/12/Sliding-window.gif)



![1581187786574](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187786574.png)

![1581187819162](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187819162.png)

Task involves:

- generating grids or windows of multiple images taking into consideration various aspect ratios (sizes), angles, shapes. Windows formed the bounding boxes
- inputting grids into a Conv net for the classification part.
- Computationally quite costly as window need to be moved through whole images

Object can have varying shape and hence it can be of problem. To solve this problem an image pyramid is created by scaling the image.**Idea is that we resize the image at multiple scales and we count on the fact that our chosen window size will completely contain the object in one of these resized images**. 

Image is downsampled(size is reduced) until certain condition typically a minimum size is reached. On each of these images, a fixed size window detector is run. It’s common to have as many as 64 levels on such pyramids. Now, all these windows are fed to a classifier to detect the object of interest. This will help us solve the problem of size and location.

![img](https://cv-tricks.com/wp-content/uploads/2017/12/pyramid-269x300.png) 

### Region Proposal principle

Here regression network is trained to give bounding box co-ordinates. Generally x,y co-ordinates here belong to center of bounding box. Here  we have same input going to two "FC Layers" which are going to two FC layers and their corresponding activation functions (Softmax and Linear). **Softmax activation function will have "Cross Entropy function" and Linear activation will have "RMSE" loss function.** Total loss = (Lambda**RMSE) + (Beta*Cross*EntropyLoss). These two are hyper parameter and we can penalize the network depending on where we want network to concentrate (Classification or BBox Coordinates).

![1581187965918](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187965918.png)

  ![1566050640735](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566050640735.png)

So here our output are : **Class Probability and BBOx Coordinates**

![1566045599111](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566045599111.png)

### Region-based Convolutional Neural Networks(R-CNN)

 R-CNN solves this(*CNNs were too slow and computationally very expensive*) problem by using an object proposal algorithm called **Selective Search** which reduces the number of bounding boxes that are fed to the classifier to close to 2000 region proposals. 

**Hence, there are 3 important parts of R-CNN:**

1. Run Selective Search to generate probable objects.
2. Feed these patches to CNN, followed by SVM to predict the class of each patch.
3. Optimize patches by training bounding box regression separately.

![img](https://cv-tricks.com/wp-content/uploads/2017/12/RCNN-e1514378306435.jpg)

#### Loss Function

Here the loss function has two component and they are classification loss and bounding box loss. So it will be as shown below.
$$
\begin{align}
\dot{TotalLoss} & = \beta BoundingBoxLoss + ClassificationLoss
\end{align}
$$


Classification loss will be cross entropy one and Bounding box related loss can be MSE.  Here factor  **Beta** determines the emphasis factor which determines when we will put more weightage on ClassificationLoss. **So initially we keep Beta low to allow have more importance on classification and once classification is stable then we will put more weightage in boundingbox loss**.

### Faster RCNN Algorithm and the Region Proposal Network (RPN)

The authors of Faster RCNN proposed a unified approach for both the tasks in hand — which meant that both the region proposal and classifier shared the same convolutional features. Slowest part in Fast RCNN was **Selective Search** or **Edge boxes**. Faster RCNN replaces selective search with a very small convolutional network called **R**egion **P**roposal **N**etwork to generate regions of Interests. 

This architecture has two network and they are

- RPN (Region Proposal Network)
- Object Detection Network using RPN

In simple words, the RPN works in the following way -

1. The feature map generated by the last conv layer in the shared conv network is taken and a small network is slid over the feature map.
2. The output of this fed into two fully connected networks (as shown below)
   1. classification layer
   2. Regression layer 

3. The red box in the above figure is called an **Anchor.** Every anchor is associated with a scale and aspect ratio. In the original paper every anchor was associated with 3 aspect ratios and 3 scales, having 9 anchors at every sliding window location.

4. The *reg* layer outputs the coordinates for each of maximum ‘k’ boxes (4k outputs) whereas the *cls* layer outputs the probability that each of the ‘k’ boxes contains an object or not (2k outputs)

![1566049957685](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566049957685.png)

![image](https://cv-tricks.com/wp-content/uploads/2017/12/Faster-RCNN-CV-Tricks-1.jpg)

Network takes the image as input and from there it generates lot of region proposals where image can be located. Then classifier takes these region proposals and identifies if objects are there or not and also refine the co-ordinates of the BBox. Here initially, we start with fixed size of K anchor boxes which generally covers all aspect ratios.![1566050398720](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566050398720.png)

Summary:

- To handle the variations in aspect ratio and scale of objects, Faster R-CNN introduces the idea of **anchor boxes**. At each location, the original paper uses 3 kinds of anchor boxes for scale **128x 128, 256×256 and 512×512**. 
- Similarly, for aspect ratio, **it uses three aspect ratios 1:1, 2:1 and 1:2**. So, In total at each location, we have 9 boxes on which RPN predicts the probability of it being background or foreground. 
- Bounding box regression is applied to improve the anchor boxes at each location.

 **Here is a quick comparison between various versions of RCNN.**

![img](https://cv-tricks.com/wp-content/uploads/2017/12/RCNN-speed-comparison.jpg)

## Regression-based object detectors

Here we pose detection as a regression problem. Two of the most popular ones are YOLO and SSD. These detectors are also called single shot detectors.

## YOLO

There are three main variations of the approach and they are **YOLOv1, YOLOv2, and YOLOv3. The first version proposed the general architecture, whereas the second version refined the design and made use of predefined anchor boxes to improve bounding box proposal, and version three further refined the model architecture and training process**.

From the paper:

> We reframe the object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities.

So, to put it simple, you take an image as input, pass it through a neural network that looks similar to a normal CNN, and you get a vector of bounding boxes and class predictions in the output

### A Fully Convolutional Neural Network

YOLO makes use of only convolutional layers, making it a fully convolutional network (FCN). It has 75 convolutional layers, with skip connections and upsampling layers. No form of pooling is used, and a convolutional layer with stride 2 is used to downsample the feature maps. This helps in preventing loss of low-level features often attributed to pooling.

Being a FCN, YOLO is invariant to the size of the input image. However, in practice, we might want to stick to a constant input size due to various problems that only show their heads when we are implementing the algorithm.

A big one amongst these problems is that if we want to process our images in batches (images in batches can be processed in parallel by the GPU, leading to speed boosts), we need to have all images of fixed height and width. This is needed to concatenate multiple images into a large batch (concatenating many PyTorch tensors into one)

The network downsamples the image by a factor called the **stride** of the network. For example, if the stride of the network is 32, then an input image of size 416 x 416 will yield an output of size 13 x 13. Generally, **stride of any layer in the network is equal to the factor by which the output of the layer is smaller than the input image to the network.**

### What is that?

The approach involves a single deep convolutional neural network (originally a version of GoogLeNet, later updated and called DarkNet based on VGG) that splits the input into a grid of cells and each cell directly predicts a bounding box and object classification. The result is a large number of candidate bounding boxes that are consolidated into a final prediction by a post-processing step.

For YOLO, detection is a simple regression problem which takes an input image and learns the class probabilities and bounding box coordinates.

![1566053019577](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566053019577.png)

![YOLO](https://static.wixstatic.com/media/4b2724_261a3ab8cd7b451bbcc474cf62df9cc8~mv2.gif)



![YOLO2](https://static.wixstatic.com/media/4b2724_3ffe1c10891641a48d6ae58e8de57c32~mv2.gif)

### How Prediction works?

- Input images divided into multiple  equal size grids. It divides each image into a grid of S x S. This Grid size can be 7x7 OR 13X13. 
- Then it tries to predict bounding boxes and confidence for each of the classes as shown here. Here C indicate "Prob" of having any object of our interest in the Grid. Then (w,h,x,y) indicates if there is out object of interest how our bounding box size will be.![1569076814891](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1569076814891.png)
- We try to predict class of the object for each of the grid and that generates "Class Probability map"
- We calculate confidence whether object is there in each of the grid in the input image. So we get anchor of the box and it means we have some confidence of our object into the grid.  The confidence reflects the accuracy of the bounding box and whether the bounding box actually contains an object(regardless of class). 
- YOLO also predicts the classification score for each box for every class in training. 

So, total SxSxN boxes are predicted. However, most of these boxes have low confidence scores and if we set a threshold say 30% confidence, we can remove most of them as shown in the example below.

![img](https://cv-tricks.com/wp-content/uploads/2017/12/model2-1024x280.jpg)

Notice that at runtime, we have run our image on CNN only once. Hence, YOLO is super fast and can be run real time. Another key difference is that YOLO sees the complete image at once as opposed to looking at only a generated region proposals in the previous methods. 

However, one limitation for YOLO is that it only predicts 1 type of class in one grid hence, it struggles with very small objects.

**So here is the summary...**

- YOLO first takes an input image:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-17-43-42.png)

- The framework then divides the input image into grids (say a 3 X 3 grid):

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-17-46-32.png)

- Image classification and localization are applied on each grid. YOLO then predicts the bounding boxes and their corresponding class probabilities for objects (if any are found, of course).

### Understanding Of Input to Yolo

**layer in the network is equal to the factor by which the output of the layer is smaller than the input image to the network.**

Typically, (as is the case for all object detectors) the features learned by the convolutional layers are passed onto a classifier/regressor which makes the detection prediction (coordinates of the bounding boxes, the class label.. etc).

In YOLO, the prediction is done by using a convolutional layer which uses 1 x 1 convolutions.

Now, the first thing to notice is our **output is a feature map**. Since we have used 1 x 1 convolutions, the size of the prediction map is exactly the size of the feature map before it. In YOLO v3 (and it's descendants), the way you interpret this prediction map is that each cell can predict a fixed number of bounding boxes.

> Though the technically correct term to describe a unit in the feature map would be a *neuron*, calling it a cell makes it more intuitive in our context.

**Depth-wise, we have (B x (5 + C)) entries in the feature map.** B represents the number of bounding boxes each cell can predict. According to the paper, each of these B bounding boxes may specialize in detecting a certain kind of object. Each of the bounding boxes have *5 + C* attributes, which describe the center coordinates, the dimensions, the objectness score and *C* class confidences for each bounding box. YOLO v3 predicts 3 bounding boxes for every cell.

**You expect each cell of the feature map to predict an object through one of it's bounding boxes if the center of the object falls in the receptive field of that cell.** (Receptive field is the region of the input image visible to the cell. Refer to the link on convolutional neural networks for further clarification).

This has to do with how YOLO is trained, where only one bounding box is responsible for detecting any given object. First, we must ascertain which of the cells this bounding box belongs to.

To do that, we divide the **input** image into a grid of dimensions equal to that of the final feature map.

Let us consider an example below, where the input image is 416 x 416, and stride of the network is 32. As pointed earlier, the dimensions of the feature map will be 13 x 13. We then divide the input image into 13 x 13 cells.

![yolo-5](https://blog.paperspace.com/content/images/2018/04/yolo-5.png)
Then, the cell (*on the input image*) containing the center of the ground truth box of an object is chosen to be the one responsible for predicting the object. In the image, it is the cell which marked red, which contains the center of the ground truth box (marked yellow).

Now, the red cell is the 7th cell in the 7th row on the grid. We now assign the 7th cell in the 7th row **on the feature map** (corresponding cell on the feature map) as the one responsible for detecting the dog.

Now, this cell can predict three bounding boxes. Which one will be assigned to the dog's ground truth label? In order to understand that, we must wrap out head around the concept of anchors.

> *Note that the cell we're talking about here is a cell on the prediction feature map. We divide the **input image** into a grid just to determine which cell of the **prediction feature map** is responsible for prediction*

- Lets look at the following image where Dog, Cycle, Car and Tree have been marked with their True Bounding box. Such images will be fed to model as Input.

- [VGG Image Annotator (VIA)](http://www.robots.ox.ac.uk/~vgg/software/via/) is a simple and standalone manual annotation software for image, audio and video and is one of Tool used to generate Input for YOLO.

![1569077540252](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1569077540252.png)

### Ways of Working

- We are going to get some image and some ground truth. 

![1581247161074](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581247161074.png)

- Here we then look into the center point of the bounding box and then whichever grid cell contain that centre is responding for predicting that BB. So first thing that we do is to adjust the class prediction of the grid cell.![1581248304674](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581248304674.png)

- We then adjust the bounding box which is most closest to ground truth and then also reduce the confidence of other bounding boxes which have lower IOU with ground truth. 

  ![1581248579055](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581248579055.png)

  ![1581248631203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581248631203.png)

  - Lot of Cells will  not have ground truth detection and we need to reduce confidence BB predicted by those cells. **DONT ADJUST THEIR CLASS PROBABILITY OR CO-ORDINDATES OF PREDICTED BB for those cells.**

  

  ![1581249185887](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581249185887.png)

  ![1581249860259](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581249860259.png)

  





### Understanding of Output

##### Output format

 The input image is divided into an *S x S* grid of cells. For each object that is present on the image, one grid cell is said to be “responsible” for predicting it. That is the cell where the center of the object falls into.

![1581246210391](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581246210391.png)

Each grid cell predicts *B* bounding boxes as well as *C* class probabilities. The bounding box prediction has 5 components: *(x, y, w, h, confidence)*. T**he *(x, y)*coordinates represent the center of the box, relative to the grid cell location (remember that, if the center of the box *does not* fall inside the grid cell, than this cell is not responsible for it). These coordinates are normalized to fall between 0 and 1. The *(w, h)* box dimensions are also normalized to [0, 1], relative to the image size. Let’s look at an example:**

![img](https://hackernoon.com/hn-images/1*oXSVP0HPVIaZqPpSinxsRQ.png)



There is still one more component in the bounding box prediction, which is the confidence score. From the paper:

> Formally we define confidence as *Pr(Object) \* IOU(pred, truth)* . If no object exists in that cell, the confidence score should be zero. Otherwise we want the confidence score to equal the intersection over union (IOU) between the predicted box and the ground truth.

Note that the confidence reflects the presence or absence of an object of *any class*.

We need to pass the labelled data to the model in order to train it. Suppose we have divided the image into a grid of size 3 X 3 and there are a total of 3 classes which we want the objects to be classified into. Let’s say the classes are Pedestrian, Car, and Motorcycle respectively. So, for each grid cell, the label y will be an eight dimensional vector:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-01-24.png)

Here,

- pc defines whether an object is present in the grid or not (it is the probability)
- bx, by, bh, bw specify the bounding box if there is an object
- c1, c2, c3 represent the classes. So, if the object is a car, c2 will be 1 and c1 & c3 will be 0, and so on

##### Sample Output and Understanding

Let’s say we select the first grid from the above example:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-08-47.png)

Since there is no object in this grid, pc will be zero and the y label for this grid will be:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-11-15.png)

Here, ‘?’ means that it doesn’t matter what bx, by, bh, bw, c1, c2, and c3 contain as there is no object in the grid. Let’s take another grid in which we have a car (c2 = 1):

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-15-50.png)

Before we write the y label for this grid, it’s important to first understand how YOLO decides whether there actually is an object in the grid. In the above image, there are two objects (two cars), so Y**OLO will take the mid-point of these two objects and these objects will be assigned to the grid which contains the mid-point of these objects**. The y label for the centre left grid with the car will be:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-27-25.png)

Since there is an object in this grid, pc will be equal to 1. bx, by, bh, bw will be calculated relative to the particular grid cell we are dealing with. Since car is the second class, c2 = 1 and c1 and c3 = 0. So, for each of the 9 grids, we will have an eight dimensional output vector. This output will have a shape of 3 X 3 X 8.

###### Objectness Score

Object score represents the probability that an object is contained inside a bounding box. It should be nearly 1 for the red and the neighboring grids, whereas almost 0 for, say, the grid at the corners.

The objectness score is also passed through a sigmoid, as it is to be interpreted as a probability.

###### Class Confidences

Class confidences represent the probabilities of the detected object belonging to a particular class (Dog, cat, banana, car etc). Before v3, YOLO used to softmax the class scores.

However, that design choice has been dropped in v3, and authors have opted for using sigmoid instead. The reason is that Softmaxing class scores assume that the classes are mutually exclusive. In simple words, if an object belongs to one class, then it's guaranteed it cannot belong to another class. This is true for COCO database on which we will base our detector.

However, this assumptions may not hold when we have classes like *Women* and *Person*. This is the reason that authors have steered clear of using a Softmax activation.

### Anchor Boxes

It might make sense to predict the width and the height of the bounding box, *but in practice, that leads to unstable gradients during training. Instead, most of the modern object detectors predict log-space transforms*, or simply offsets to pre-defined default bounding boxes called **anchors**.

Then, these transforms are applied to the anchor boxes to obtain the prediction. YOLO v3 has three anchors, which result in prediction of three bounding boxes per cell.

Coming back to our earlier question, the bounding box responsible for detecting the dog will be the one whose anchor has the highest IoU with the ground truth box.

Generally each grid can identify only one object. But what if there are multiple objects in a single grid? That can so often be the case in reality.  This is why Anchor Box concept has been evolved.

![ik](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-13-18-38.png)

- Above image is being divided into 3x3 grid

- We take midpoint of the object and based on its location, assigned the object to the corresponding grid.

- midpoint of both the objects lies in the same grid.

  ![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-13-20-41.png)

We will only be getting one of the two boxes, either for the car or for the person. But if we use anchor boxes, we might be able to output both boxes! First, we pre-define two different shapes called anchor boxes or anchor box shapes. Now, for each grid, instead of having one output, we will have two outputs. We can always increase the number of anchor boxes as well. Have taken two here to make the concept easy to understand:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-13-36-28.png)

*This is how the y label for YOLO without anchor boxes looks like:*

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-01-24.png)

**How y label will be if we have 2 anchor boxes**? The y label will be:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-13-33-31.png)

**The first 8 rows belong to anchor box 1 and the remaining 8 belongs to anchor box 2**. The objects are assigned to the anchor boxes based on the similarity of the bounding boxes and the anchor box shape. Since the shape of anchor box 1 is similar to the bounding box for the person, the latter will be assigned to anchor box 1 and the car will be assigned to anchor box 2. The output in this case, instead of 3 X 3 X 8 (using a 3 X 3 grid and 3 classes), will be 3 X 3 X 16 (since we are using 2 anchors).

So, for each grid, we can detect two or more objects based on the number of anchors. 

### More on Bounding Boxes

bx, by, bh, and bw are calculated relative to the grid cell we are dealing with. 

Consider the center-right grid which contains a car:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-19-23-07.png)

So, **bx, by, bh, and bw will be calculated relative to this grid only**. The y label for this grid will be:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-18-27-25.png)

pc = 1 since there is an object in this grid and since it is a car, c2 = 1. Now, let’s see how to decide bx, by, bh, and bw. In YOLO, the coordinates assigned to all the grids are:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-19-35-31.png)

bx, by are the x and y coordinates of the midpoint of the object with respect to this grid. In this case, it will be (around) bx = 0.4 and by = 0.3:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-15-19-39-51.png)

bh is the ratio of the height of the bounding box (red box in the above example) to the height of the corresponding grid cell, which in our case is around 0.9. So,  bh = 0.9. bw is the ratio of the width of the bounding box to the width of the grid cell. So, bw = 0.5 (approximately). The y label for this grid will be:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-16-12-44-34.png)

Notice here that bx and by will always range between 0 and 1 as the midpoint will always lie within the grid. Whereas bh and bw can be more than 1 in case the dimensions of the bounding box are more than the dimension of the grid.

### Making Predictions

The following formulae describe how the network output is transformed to obtain bounding box predictions.

![YOLO Equations](https://blog.paperspace.com/content/images/2018/04/Screen-Shot-2018-04-10-at-3.18.08-PM.png)
*bx, by, bw, bh* are the x,y center co-ordinates, width and height of our prediction. *tx, ty, tw, th* is what the network outputs. *cx* and *cy* are the top-left co-ordinates of the grid. *pw* and *ph* are anchors dimensions for the box.

#### Center Coordinates

Notice we are running our center coordinates prediction through a sigmoid function. This forces the value of the output to be between 0 and 1. Why should this be the case? Bear with me.

Normally, YOLO doesn't predict the absolute coordinates of the bounding box's center. It predicts offsets which are:

- Relative to the top left corner of the grid cell which is predicting the object.
- Normalised by the dimensions of the cell from the feature map, which is, 1.

For example, consider the case of our dog image. If the prediction for center is (0.4, 0.7), then this means that the center lies at (6.4, 6.7) on the 13 x 13 feature map. (Since the top-left co-ordinates of the red cell are (6,6)).

But wait, what happens if the predicted x,y co-ordinates are greater than one, say (1.2, 0.7). This means center lies at (7.2, 6.7). Notice the center now lies in cell just right to our red cell, or the 8th cell in the 7th row. **This breaks theory behind YOLO** because if we postulate that the red box is responsible for predicting the dog, the center of the dog must lie in the red cell, and not in the one beside it.

Therefore, to remedy this problem, the output is passed through a sigmoid function, which squashes the output in a range from 0 to 1, effectively keeping the center in the grid which is predicting.

#### Dimensions of the Bounding Box

The dimensions of the bounding box are predicted by applying a log-space transform to the output and then multiplying with an anchor.

![img](https://blog.paperspace.com/content/images/2018/04/yolo-regression-1.png)

How the detector output is transformed to give the final prediction. Image Credits. http://christopher5106.github.io/*             

The resultant predictions, *bw* and *bh*, are normalised by the height and width of the image. (Training labels are chosen this way). So, if the predictions *bx* and *by* for the box containing the dog are (0.3, 0.8), then the actual width and height on 13 x 13 feature map is (13 x 0.3, 13 x 0.8).



his is the reason that authors have steered clear of using a Softmax activation.

### Prediction across different scales.

YOLO v3 makes prediction across 3 different scales. The detection layer is used make detection at feature maps of three different sizes, having **strides 32, 16, 8** respectively. This means, with an input of 416 x 416, we make detections on scales 13 x 13, 26 x 26 and 52 x 52.

The network downsamples the input image until the first detection layer, where a detection is made using feature maps of a layer with stride 32. Further, layers are upsampled by a factor of 2 and concatenated with feature maps of a previous layers having identical feature map sizes. Another detection is now made at layer with stride 16. The same upsampling procedure is repeated, and a final detection is made at the layer of stride 8.

At each scale, each cell predicts 3 bounding boxes using 3 anchors, making the total number of anchors used 9. (The anchors are different for different scales)

![img](https://blog.paperspace.com/content/images/2018/04/yolo_Scales-1.png)

The authors report that this helps YOLO v3 get better at detecting small objects, a frequent complaint with the earlier versions of YOLO. Upsampling can help the network learn fine-grained features which are instrumental for detecting small objects.

### Intersection over Union

Intersection over Union calculates the intersection over union of the actual bounding box and the predicted bonding box. Consider the actual and predicted bounding boxes for a car as shown below:![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-16-13-07-50.png)

- red box is the actual bounding box and the blue box is the predicted one

- IoU, or Intersection over Union, will calculate the area of the intersection over union of these two boxes.

  - IoU = Area of the intersection / Area of the union, i.e.

    IoU = Area of yellow box / Area of green box

![ik](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-16-13-12-02.png)

If IoU is greater than 0.5, we can say that the prediction is good enough. Intuitively, the more you increase the threshold, the better the predictions become.

### Non-Max Suppression

One of the most common problems with object detection algorithms is that rather than detecting an object just once, they might detect it multiple times. Consider the below image:

![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-16-13-32-40.png)

Here, the cars are identified more than once. The Non-Max Suppression technique cleans up this up so that we get only a single detection per object. So here is what it does.

-  It first looks at the probabilities associated with each detection and takes the largest one. In the above image, 0.9 is the highest probability, **so the box with 0.9 probability will be selected first**.

  ![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-12-08-14.png)

- Then it looks at all the other boxes in the image. The boxes which have high IoU with the current box are suppressed. So, the boxes with 0.6 and 0.7 probabilities will be suppressed in our example:

  ![img](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-12-09-17.png)

- After the boxes have been suppressed, it selects the next box from all the boxes with the highest probability, which is 0.8 in our case:

  ![ik](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-12-10-38.png)

- Again it will look at the IoU of this box with the remaining boxes and suppress the boxes with a high IoU:

  ![ik](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-12-11-35.png)

  

- We repeat these steps until all the boxes have either been selected or suppressed and we get the final bounding boxes

  ![ik](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-17-12-21-31.png)

We are taking the **boxes with maximum probability and suppressing the close-by boxes with non-max probabilities**.

**Summary**

1. Discard all the boxes having probabilities less than or equal to a pre-defined threshold (say, 0.5)
2. For the remaining boxes:
   1. Pick the box with the highest probability and take that as the output prediction
   2. Discard any other box which has IoU greater than the threshold with the output box from the above step
3. Repeat step 2 until all the boxes are either taken as the output prediction or discarded



### Network

The network structure looks like a normal CNN, with convolutional and max pooling layers, followed by 2 fully connected layers in the end:

![1566107420277](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566107420277.png)

Some comments about the architecture:

- Note that the architecture was crafted for use in the Pascal VOC dataset, where the authors used S=7, B=2 and C=20. This explains why the final feature maps are 7x7, and also explains the size of the output (7x7x(2*5+20)). Use of this network with a different grid size or different number of classes might require tuning of the layer dimensions.
- The authors mention that there is a fast version of YOLO, with fewer convolutional layers. The table above, however, display the full version.
- The sequences of 1x1 reduction layers and 3x3 convolutional layers were inspired by the GoogLeNet (Inception) model
- The final layer uses a linear activation function. All other layers use a leaky RELU (Φ*(x) = x, if x>0; 0.1x otherwise*)

### Keras Yolo Object Detection

It is a challenging model to implement from scratch, especially for beginners as it requires the development of many customized model elements for training and for prediction. For example, even using a pre-trained model directly requires sophisticated code to distill and interpret the predicted bounding boxes output by the model.

The [keras-yolo3](https://github.com/experiencor/keras-yolo3) project provides a lot of capability for using YOLOv3 models, including object detection, transfer learning, and training new models from scratch.

### Loss Function

**YOLO output has following components and so loss function need to address all these ones.**

- Confidence probability

  - Loss (Confidance)

- Bounding Box coordinates

  - Loss (Width of BB)
  - Loss (Height of BB)
  - Loss (x of BB)
  - Loss (Y of BB)

- Class Probabilities

  - Cross Entropy

   

There is a lot to say about the loss function, so let's do it by parts. It starts like this:

![1566107643534](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566107643534.png)



This equation computes the loss related to the predicted bounding box position **(x,y)**. Don’t worry about **λ** for now, just consider it a given constant. The function computes a sum over each bounding box predictor **(j = 0.. B)** of each grid cell **(i = 0 .. S^2)**. **𝟙 obj** is defined as follows:

- 1, If an object is present in grid cell *i* and the *j*th bounding box predictor is “responsible” for that prediction
- 0, otherwise

But how do we know which predictor is responsible for the object? Quoting the original paper:

> *YOLO predicts multiple bounding boxes per grid cell. At training time we only want one bounding box predictor to be responsible for each object. We assign one predictor to be “responsible” for predicting an object based on which prediction has the highest current IOU with the ground truth.*

The other terms in the equation should be easy to understand: **(x, y)** are the predicted bounding box position and **(x̂, ŷ)** hatare the actual position from the training data.

**Let’s move on to the second part:**

![1566107692569](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566107692569.png)

This is the loss related to the predicted box width / height. The equation looks similar to the first one, except for the square root. What’s up with that? Quoting the paper again:

> *Our error metric should reflect that small deviations in large boxes matter less than in small boxes. To partially address this we predict the square root of the bounding box width and height instead of the width and height directly.*

**Moving on to the third part:**

![1566107754874](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566107754874.png)

Here we compute the loss associated with the confidence score for each bounding box predictor. **C** is the confidence score and **Ĉ** is the intersection over union of the predicted bounding box with the ground truth.**𝟙 obj** is equal to one when there is an object in the cell, and 0 otherwise. **𝟙 noobj** is the opposite.

The **λ** parameters that appear here and also in the first part are used to differently weight parts of the loss functions. This is necessary to increase model stability. The highest penalty is for coordinate predictions (**λ coord** *= 5)* and the lowest for confidence predictions when no object is present (**λ noobj***= 0.5)*.

The last part of the loss function is the classification loss:

![1566107774397](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1566107774397.png)



It looks similar to a normal sum-squared error for classification, except for the **𝟙 obj** term. This term is used because so we don’t penalize classification error when no object is present on the cell (hence the conditional class probability discussed earlier).

### Training

The authors describe the training in the following way

- First, pre-train the first 20 convolutional layers using the ImageNet 1000-class competition dataset, using a input size of 224x224
- Then, increase the input resolution to 448x448
- Train the full network for about 135 epochs using a batch size of 64, momentum of 0.9 and decay of 0.0005
- Learning rate schedule: for the first epochs, the learning rate was slowly raised from 0.001 to 0.01. Train for about 75 epochs and then start decreasing it.
- Use data augmentation with random scaling and translations, and randomly adjusting exposure and saturation.

### YOLO V2 Deeper Analysis

**All these are also valid for YOLO V3 also**

- YOLOv2 is a combined classification-bounding box prediction framework where we directly predict the objects in each cell and the corrections on anchor boxes.
- YOLOv2 divides the entire image into 13X13 grid cells, next places 5  anchor boxes at each location and finally predicts corrections on these anchor boxes.
- YOLOv2 makes 5 predictions corresponding to corrections on location of  center (x and y), height and width, and finally the intersection over union (IOU) between predicted bounding boxes and ground truth boxes. 
- A unique feature of YOLOv2 is that the anchor boxes are designed specifically for the given dataset using K-means clustering. Unlike other anchor boxes (or prior) based methods, like Single Shot Detection, YOLOv2 does not assume the aspect ratios or shapes of the boxes. As a 
  result, the YOLOv2 in general has lower localization loss and has higher intersection over union (IOU) between the target and network prediction.

### YOLO V3 Deeper Analysis

- 

![1569139682266](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1569139682266.png)

Here YOLOV3 predict 3D tensors (which is the last feature map) corresponding to 3 scales

The three scales are designed for detecting objects with various sizes. Here we take the scale 13x13 as an example. For this scale, the input image is divided into 13x13 grid cells, each grid cell corresponds to a 1x1x255 voxel inside a 3D tensor. Here, 255 comes from (3x(4+1+80)). Values in a 3D tensor such as bounding box coordinate, objectness score and class confidence are shown on the right of the diagram.

![YOLOV3](https://static.wixstatic.com/media/4b2724_732d986690524e5ca22e211ee85a4cbe~mv2.png/v1/fill/w_925,h_759,al_c,q_90,usm_0.66_1.00_0.01/4b2724_732d986690524e5ca22e211ee85a4cbe~mv2.webp)

![1581184041208](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581184041208.png)

#### Output Processing

For an image of size 416 x 416, YOLO predicts ((52 x 52) + (26 x 26) + 13 x 13)) x 3 = **10647 bounding boxes**. However, in case of our image, there's only one object, a dog. How do we reduce the detections from 10647 to 1?

###### Thresholding by Object Confidence

First, we filter boxes based on their objectness score. Generally, boxes having scores below a threshold are ignored.

###### Non-maximum Suppression

NMS intends to cure the problem of multiple detections of the same image. For example, all the 3 bounding boxes of the red grid cell may detect a box or the adjacent cells may detect the same object.

![img](https://blog.paperspace.com/content/images/2018/04/NMS-1.png)

```markdown

```

## SSD

### Introduction and Why?

SSD only need to take one single shot to detect multiple objects within the image, while regional proposal network (RPN) based approaches such as R-CNN series that need two shots, one for generating region proposals, one for detecting the object of each proposal. Thus, SSD is much faster compared with two-shot RPN-based approaches.

Refer the Video: [SSD Mobilenet Object detection FullHD S8#001](https://www.youtube.com/watch?time_continue=15&v=7p2XL8wApfo&feature=emb_logo)

In RCNN, When we tried to predict where object are, first we get probable area of of where image can be through "Selective Search" and then each of these areas pass through convolution network to predict where is the object location.![1581170815589](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581170815589.png)

Suppose, the selective search area gives me 100 area, so for each of 100 area , will pass through network to get prediction of class and location of class. Off course, this is slow as for each area, i am running through  100 times. So in order to make faster here is what "**Fast RCNN did?"**

- Parse the image through conv layer only once. This means Forward pass happens only happens which males Fast RCNN quick. 
- Run Selective search on Feature Maps instead of on Input feature. But still this selective search makes the process slow.

![1581171740183](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581171740183.png)

Then came **Faster RCNN** which did further improvement on Fast RCNN.

- Selective search algorithm has been replaced by RPN Network. This network gives us probable bounding box location and whether object will be there or not.
- RPN is class agonistic logic and hence it only tells whether there is object or not only.

![1581181164788](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581181164788.png)

But still we see RPN is a limitation as why RPN can't be class specific one? This is what has been done in **YOLO**.

![1581183117605](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581183117605.png)

**Let's look at the accuracy of all these models and what we see that although speed of YOLO is far better than all others but its accuracy is as similar to RCNN. But then see SSD which is quite faster than all others and better in accuracy.**

![1581183455714](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581183455714.png)

### Architecture

- Base Network of VGG16
- Auxiliary structure for detection at multiple stages. This helps for detection of small objects in the images
- YOLO Fails when object is small  
- Multi scale network and classifier at each stage
- Convolution layers in auxilary network are 1x1 convolution with stride 2. They create feature map with decreasing size. These varying size feature maps are used for scale variance of objects.
- Detector and classifier applied on each feature map
- SSD’s architecture builds on the venerable VGG-16 architecture, but discards the fully connected layers. The reason VGG-16 was used as the *base network* is because of its strong performance in high quality image classification tasks and its popularity for problems where *transfer learning* helps in improving results. Instead of the original VGG fully connected layers, a set of *auxiliary* convolutional layers (from *conv6* onwards) were added, thus enabling to extract features at multiple scales and progressively decrease the size of the input to each subsequent layer.

![1581184752084](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581184752084.png)

Now let us understand Object detection auxiliary connection. The following one has a limitation that it can detect only one object.![1581185794837](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581185794837.png)

Now, we can slightly change the above detector to detect multiple objects and its BB. But this network can only predict 3 objects and not more/less than 3 objects. Even with 1 object, it will still give me 3 output.

![1581185835794](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581185835794.png)

And here is how we can make generic. **Key here is that we have Object Score which indicate whether that prediction has any object or not. So, if this value is not set then we ignore that prediction.**

![1581186043515](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581186043515.png)



### MultiBox

The bounding box regression technique of SSD is inspired by Szegedy’s work on [MultiBox](https://arxiv.org/abs/1412.1441), a method for fast *class-agnostic* bounding box coordinate proposals. Interestingly, in the work done on MultiBox an [Inception](https://arxiv.org/abs/1409.4842)-style  convolutional network is used. The 1x1 convolutions that you see below  help in dimensionality reduction since the number of dimensions will go  down (but “width” and “height” will remain the same).

![img](https://miro.medium.com/max/1836/1*WbNf0ngkmCJYT_jXX6IaOw.png)



Architecture of multi-scale convolutional prediction of the location and confidences of multibox

MultiBox’s loss function also combined two critical components that made their way into SSD:

- **Confidence Loss**: this measures how confident the network is of the *objectness* of the computed bounding box. Categorical [cross-entropy](https://rdipietro.github.io/friendly-intro-to-cross-entropy-loss/#cross-entropy) is used to compute this loss.
- **Location Loss:** this measures how *far away* the network’s predicted bounding boxes are from the ground truth ones from the training set. [L2-Norm](https://rorasa.wordpress.com/2012/05/13/l0-norm-l1-norm-l2-norm-l-infinity-norm/) is used here.

Without  delving too deep into the math (read the paper if you are curious and  want a more rigorous notation), the expression for the loss, which  measures how far off our prediction “landed”, is thus:

**multibox_loss = confidence_loss + alpha \* location_loss**

The *alpha* term  helps us in balancing the contribution of the location loss. As usual  in deep learning, the goal is to find the parameter values that most  optimally reduce the loss function, thereby bringing our predictions  closer to the ground truth.

## Upsampling a bit more

### In-Network upsampling

![1581186742576](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581186742576.png)

### In-Network Upsampling - Max Pooling

![1581186897794](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581186897794.png)

### Learnable Upsampling

![1581187455866](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187455866.png)

![1581187481042](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187481042.png)

Lets understand more easily...

![1581187533779](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1581187533779.png)



# Retina Net

## Focal Loss

Snippet from paper ***In contrast, one-stage detectors that are applied over a regular, dense sampling of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far. In this paper, we investigate why this is the case. We discover that the extreme foreground-background class imbalance encountered during training of dense detectors is the central cause. We propose to address this class imbalance by reshaping the standard cross entropy loss such that it down-weights the loss assigned to well-classified examples***.



## Reference

- [Focal Loss Paper](https://arxiv.org/pdf/1708.02002.pdf)

# Self Notebook Reference

- [Custom Data Training - Gun](<https://colab.research.google.com/drive/1TEoXFL9c8uIdqyy8GoMhek-voo7nfiXa>)
- [Yolo DarkNet Class Detection](<https://colab.research.google.com/drive/1TEoXFL9c8uIdqyy8GoMhek-voo7nfiXa>)
- [SELF_LEARNING_Yolo_Darknet_Video_Without_Display](<https://colab.research.google.com/drive/1o6oXfFUKHWbgoWCHl1PFyeAUw0n0H8Zk#scrollTo=1k2IRK41YK_8>)
- [Yolo V3 in pytorch](<https://github.com/AyushExel/Detectx-Yolo-V3>)
- [Yolo from Custom Data](<https://colab.research.google.com/drive/1289IS8NPDUi3FtOr8Pp0DJEOlC_JrU-X>)
- <https://github.com/AyushExel/Detectx-Yolo-V3>

# Youtube Channel

- <https://www.youtube.com/channel/UCyn1QFyonOr-NKVtX3gw0vw/videos>
- <https://www.youtube.com/watch?v=PyjBd7IDYZs>





# An Introduction to Evaluation Metrics for Object Detection



## Introduction

The purpose of this post was to summarize some common metrics for object detection adopted by various popular competetions. This post mainly focuses on the definitions of the metrics; I’ll write another post to discuss the interpretaions and intuitions.

## Popular competetions and metrics

The following competetions and metrics are included by this post[1](https://blog.zenggyu.com/en/post/2018-12-16/an-introduction-to-evaluation-metrics-for-object-detection/#fn1):

- [The PASCAL VOC Challenge](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/devkit_doc.html) (Everingham et al. 2010)
- [The COCO Object Detection Challenge](http://cocodataset.org/#detection-eval) (Lin et al. 2014)
- [The Open Images Challenge](https://storage.googleapis.com/openimages/web/object_detection_metric.html) (Kuznetsova 2018).

The links above points to the websites that describe the evaluation metrics. In brief:

- All three challenges use mean average precision as a principal metric to evaluate object detectors; however, there are some variations in definitions and implementations.
- The COCO Object Detection challenge[2](https://blog.zenggyu.com/en/post/2018-12-16/an-introduction-to-evaluation-metrics-for-object-detection/#fn2) also includes mean average recall as a detection metric.

## Some concepts

Before diving into the competetion metrics, let’s first review some foundational concepts.

**Confidence score** is the probability that an anchor box contains an object. It is usually predicted by a classifier.

**Intersection over Union (IoU)** is defined as the area of the intersection divided by the area of the union of a predicted bounding box (BpBp) and a ground-truth box (BgtBgt):

IoU=area(Bp∩Bgt)area(Bp∪Bgt)(1)IoU=area(Bp∩Bgt)area(Bp∪Bgt)(1)

Both confidence score and IoU are used as the criteria that determine whether a detection is a true positive or a false positive. The pseudocode below shows how:

```
for each detection that has a confidence score > threshold:

  among the ground-truths, choose one that belongs to the same class and has the highest IoU with the detection
  
  if no ground-truth can be chosen or IoU < threshold (e.g., 0.5):
    the detection is a false positive
  else:
    the detection is a true positive
```

As the pseudocode indicates, a detection is considered a **true positive (TP)** only if it satisties three conditions: confidence score > threshold; the predicted class matches the class of a ground truth; the predicted bounding box has an IoU greater than a threshold (e.g., 0.5) with the ground-truth. Violation of either of the latter two conditions makes a **false positive (FP)**. It is worth mentioning that the PASCAL VOC Challenge includes some additional rules to define true/false positives. In case multiple predictions correspond to the same ground-truth, only the one with the highest confidence score counts as a true positive, while the remainings are considered false positives.

When the confidence score of a detection that is supposed to detect a ground-truth is lower than the threshold, the detection counts as a **false negative (FN)**. You may wonder how the number of false positives are counted so as to calculate the following metrics. However, as will be shown, we don’t really need to count it to get the result.

When the confidence score of a detection that is not supposed to detect anything is lower than the threshold, the detection counts as a **true negative (TN)**. However, in object detection we usually don’t care about these kind of detections.

**Precision** is defined as the number of true positives divided by the sum of true positives and false positives:

precision=TPTP+FP(2)precision=TPTP+FP(2)

**Recall** is defined as the number of true positives divided by the sum of true positives and false negatives (note that the sum is just the number of ground-truths, so there’s no need to count the number of false negatives):

recall=TPTP+FN(3)recall=TPTP+FN(3)

By setting the threshold for confidence score at different levels, we get different pairs of precision and recall. With recall on the x-axis and precison on the y-axis, we can draw a **precision-recall curve**, which indicates the association between the two metrics. Fig. 1 shows a simulated plot.

![img](https://gitlab.com/zenggyu/static/raw/master/post/2018-12-16/fig_1.gif)Figure 1

Note that as the threshold for confidence score decreases, recall increases monotonically; precision can go up and down, but the general tendency is to decrease.

In addition to precision-recall curve, there is another kind of curve called **recall-IoU curve**. Traditionally, this curve is used to evaluate the effectiveness of detection proposals (Hosang et al. 2016), but it is also the foundation of a metric called average recall, which will be introduced in the next section.

By setting the threshold for IoU at different levels, the detector would achieve different recall levels accordingly. With these values, we can draw the **recall-IoU curve** by mapping IoU∈[0.5,1.0]IoU∈[0.5,1.0] on the x-axis and recall on the y-axis (Fig. 2 shows a simulated plot).

![img](https://gitlab.com/zenggyu/static/raw/master/post/2018-12-16/fig_2.gif)Figure 2

The curve shows that recall decreases as IoU increases.

## Definitions of various metrics

This section introduces the following metrics: average precision (AP), mean average precision (mAP), average recall (AR) and mean average recall (mAR).

### Average precision

Although the precision-recall curve can be used to evaluate the performance of a detector, it is not easy to compare among different detectors when the curves intersect with each other. It would be better if we have a numerical metric that can be used directly for the comparison. This is where **average precision (AP)**, which is based on the precision-recall curve, comes into play. In essence, AP is the precision averaged across all unique recall levels.

Note that in order to reduce the impact of the wiggles in the curve, we first interpolate the precision at multiple recall levels before actually calculating AP. The interpolated precision pinterppinterp at a certain recall level rr is defined as the highest precision found for any recall level r′≥rr′≥r:

pinterp(r)=maxr′≥rp(r′)(4)pinterp(r)=maxr′≥rp(r′)(4)

Note that there are two ways to choose the levels of recall (denoted as rr above) at which the precision should be interpolated. The traditional way is to choose 11 equally spaced recall levels (i.e., 0.0, 0.1, 0.2, … 1.0); while a new standard adopted by the PASCAL VOC challenge chooses all unique recall levels presented by the data. The new standard is said to be more capable of improving precision and measuring differences between methods with low AP. Fig. 3 shows how the interpolated precision-recall curve is obtained over the original curve, using the new standard.

![img](https://gitlab.com/zenggyu/static/raw/master/post/2018-12-16/fig_3.gif)Figure 3

AP can then be defined as the area under the interpolated precision-recall curve, which can be calculated using the following formula:

AP=n−1∑i=1(ri+1−ri)pinterp(ri+1)(5)AP=∑i=1n−1(ri+1−ri)pinterp(ri+1)(5)

where r1,r2,...,rnr1,r2,...,rn is the recall levels (in an ascending order) at which the precision is first interpolated.

### Mean average precision

The calculation of AP only involves one class. However, in object detection, there are usually K>1K>1 classes. **Mean average precision (mAP)** is defined as the mean of AP across all KK classes:

mAP=∑Ki=1APiK(6)mAP=∑i=1KAPiK(6)

### Average recall

Like AP, **average recall (AR)** is also a numerical metric that can be used to compare detector performance. In essence, AR is the recall averaged over all IoU∈[0.5,1.0]IoU∈[0.5,1.0] and can be computed as two times the area under the recall-IoU curve:

AR=2∫10.5recall(o)do(7)AR=2∫0.51recall(o)do(7)

where oo is IoU and recall(o)recall(o) is the corresponding recall.

It should be noted that for its original purpose (Hosang et al. 2016), the recall-IoU curve does not distinguish among different classes[3](https://blog.zenggyu.com/en/post/2018-12-16/an-introduction-to-evaluation-metrics-for-object-detection/#fn3). However, the COCO challenge makes such distinctions and its AR metric is calculated on a per-class basis, just like AP.

### Mean average recall

**Mean average recall** is defined as the mean of AR across all KK classes:

mAR=∑Ki=1ARiK(8)mAR=∑i=1KARiK(8)

## Variations among the metrics

The Pascal VOC challenge’s mAP metric can be seen as a standard metric to evaluate the performance of object detectors; the major metrics adopted by the other two competetions can be seen as variants of the aforementioned metric.

### COCO Evaluation Metrices

```
Evaluate annotation type *bbox*
COCOeval_opt.evaluate() finished in 0.09 seconds.
Accumulating evaluation results...
COCOeval_opt.accumulate() finished in 0.03 seconds.
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.543
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.821
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.625
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.197
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.638
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.653
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.512
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.651
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.668
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.416
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.742
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.753
[07/17 10:19:24 d2.evaluation.coco_evaluation]: Evaluation results for bbox: 
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 54.320 | 82.143 | 62.473 | 19.711 | 63.843 | 65.263 |
OrderedDict([('bbox',
              {'AP': 54.31978768104956,
               'AP50': 82.14261911101626,
               'AP75': 62.47290365771423,
               'APl': 65.26308034807144,
               'APm': 63.84319489108482,
               'APs': 19.71092344586819})])
```

- The first metric states: AP at IoU = 0.5 : 0.05: 0.95. So, we have APs at 10 thresholds (0.5, 0.55, ...). So, how do we calculate the final AP. Should we take the mean of the APs taken?
  - Yes, you are right.
- The AP across scales specifies APs for various objects based on area. What 'area' does it refer to? Does it refer to area of the predicted B-Boxes?
  - Area refers to the G-truth bounding boxes. Have a look to the link <http://cocodataset.org/#detection-eval>
- How to calculate Average Recall (AR)? It also defines metrics for AR at different no. of detections per image . What if the image does not have those many number of detections?
  - Less than max detection is fine. But more than that it will give the wrong evaluation. Have a look at the discussion <https://stackoverflow.com/questions/52839368/understanding-coco-evaluation-maximum-detections>

### COCO challenge’s variants

Recall that the Pascal VOC challenge defines the mAP metric using a single IoU threshold of 0.5. However, the COCO challenge defines several mAP metrics using different thresholds, including:

- mAPIoU=.50:.05:.95mAPIoU=.50:.05:.95 which is mAP averaged over 10 IoU thresholds (i.e., 0.50, 0.55, 0.60, …, 0.95) and is the primary challenge metric;
- mAPIoU=.50mAPIoU=.50, which is identical to the Pascal VOC metric;
- mAPIoU=.75mAPIoU=.75, which is a strict metric.

In addition to different IoU thresholds, there are also mAP calculated across different object scales; these variants of mAP are all averaged over 10 IoU thresholds (i.e., 0.50, 0.55, 0.60, …, 0.95):

- mAPsmallmAPsmall, which is mAP for small objects that covers area less than 322322;
- mAPmediummAPmedium, which is mAP for medium objects that covers area greater than 322322 but less than 962962;
- mAPlargemAPlarge, which is mAP for large objects that covers area greater than 962962.

Like mAP, the mAR metric also has many variations. One set of mAR variants vary across different numbers of detections per image:

- mARmax=1mARmax=1, which is mAR given 1 detection per image;
- mARmax=10mARmax=10, which is mAR given 10 detections per image;
- mARmax=100mARmax=100, which is mAR given 100 detections per image.

The other set of mAR variants vary across the size of detected objects:

- mARsmallmARsmall, which is mAR for small objects that covers area less than 322322;
- mARmediummARmedium, which is mAR for medium objects that covers area greater than 322322 but less than 962962;
- mARlargemARlarge, which is mAR for large objects that covers area greater than 962962.

## The Open Images challenge’s variants

The Open Images challenge’s object detection metric is a variant of the PASCAL VOC challenge’s mAP metric, which accomodates to three key features of the dataset that affect how true positives and false positives are accounted:

- non-exhaustive image-level labeling;
- semantic hierarchy of classes;
- some ground-truth boxes may contain groups of objects and the exact location of a single object inside the group is unknown.

The [official site](https://storage.googleapis.com/openimages/web/object_detection_metric.html) provides more detailed description on how to deal with these cases.

## Implementations

The [Tensorflow Object Detection API](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/evaluation_protocols.md) provides implementations of various metrics.

There is also another opensource [project](https://github.com/rafaelpadilla/Object-Detection-Metrics) that implements various metrics that respect the competition’s specifications, with an advantage in unifying the input format.

# Web References

- **[EVA YOLO Repo](<https://github.com/theschoolofai/YoloV3>)**
- [**A series of notebooks describing how to use YOLO (darkflow) in python**](<https://github.com/amitkayal/YOLO-series>)
- [Everything you need to know to train your custom object detector model using YOLOv3](<https://medium.com/analytics-vidhya/everything-you-need-to-know-to-train-your-custom-object-detector-model-using-yolov3-1bf0640b0905>)
- [Start YOLO with Own Data](<http://guanghan.info/blog/en/my-works/train-yolo/>)
- [Darknet Yolo](<https://pjreddie.com/darknet/yolo/>)
- [Mask RCNN](<https://github.com/markjay4k/Mask-RCNN-series>)
- [Training YOLO](https://blog.paperspace.com/tag/series-yolo/)
- [YOLO E2E](https://docs.google.com/presentation/d/1aeRvtKG21KHdD5lg6Hgyhx5rPq_ZOsGjG5rJ1HP7BbA/pub?start=false&loop=false&delayms=3000&slide=id.p)
- [A Closer Look at YOLO v3](https://www.cyberailab.com/home/a-closer-look-at-yolov3)
- [A Closer Look at SSD](https://www.cyberailab.com/home/ssd-fpga)
- [What's new in YOLO v3](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)
- [Object Detection YOLO v1 , v2, v3](https://medium.com/@venkatakrishna.jonnalagadda/object-detection-yolo-v1-v2-v3-c3d5eca2312a)
- [Object Detection](https://github.com/amusi/awesome-object-detection)
- [Generating Anchor Box Size for YOLO](https://medium.com/@vivek.yadav/part-1-generating-anchor-boxes-for-yolo-like-network-for-vehicle-detection-using-kitti-dataset-b2fe033e5807)
- [K means Clustering for Anchor Boxes](https://lars76.github.io/object-detection/k-means-anchor-boxes/)
- [Fast RCNN and SSD](https://www.youtube.com/watch?v=5rY7CevPkKM)
- [YOLOv2 to detect your own objects using Darkflow](https://towardsdatascience.com/yolov2-to-detect-your-own-objects-soccer-ball-using-darkflow-a4f98d5ce5bf)
- [Image Annotation Tool](https://github.com/Ericsson/eva)
- [VGG Image Annotator](http://www.robots.ox.ac.uk/~vgg/software/via/)
- [How to Train Yolo on Custom Dataset](https://blog.goodaudience.com/part-1-preparing-data-before-training-yolo-v2-and-v3-deepfashion-dataset-3122cd7dd884)
- [Yolo-v3 and Yolo-v2 for Windows and Linux](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)
- [Powerful and efficient Computer Vision Annotation Tool (CVAT) ](https://github.com/opencv/cvat)
- [Computer Vision Annotation Tool: A Universal Approach to Data Annotation](https://software.intel.com/en-us/articles/computer-vision-annotation-tool-a-universal-approach-to-data-annotation)

