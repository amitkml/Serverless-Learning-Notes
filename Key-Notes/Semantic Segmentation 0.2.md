[TOC]

# Semantic Segmentation

This is another classic case study of NN other than classification. Architecture and loss function gets changed when we change the business problem from classification to other ones.

- Fully Convolution Network for Semantic Segmentation
- Simultaneous localization and recognition using CNN
- Siamese Network for Metric Learning

## What is semantic segmentation

Semantic image segmentation is the task of classifying each pixel in an image from a predefined set of classes. In the following example, different entities are classified.

![img](https://divamgupta.com/assets/images/posts/imgseg/image15.png?style=centerme)*Semantic segmentation of a bedroom image*

In the above example, the pixels belonging to the bed are classified in the class “bed”, the pixels corresponding to the walls are labeled as “wall”, etc.

In particular, our goal is to take an image of size W x H x 3 and generate a W x H matrix containing the predicted class ID’s corresponding to all the pixels.

![img](https://divamgupta.com/assets/images/posts/imgseg/image14.png?style=centerme)*Image source: jeremyjordan.me*

Usually, in an image with various entities, we want to know which pixel belongs to which entity, For example in an outdoor image, we can segment the sky, ground, trees, people, etc.

Semantic segmentation is different from object detection as it does not predict any bounding boxes around the objects. We do not distinguish between different instances of the same object. For example, there could be multiple cars in the scene and all of them would have the same label.

![img](https://divamgupta.com/assets/images/posts/imgseg/image7.png?style=centerme)*An example where there are multiple instances of the same object class*

In order to perform semantic segmentation, a higher level understanding of the image is required. The algorithm should figure out the objects present and also the pixels which correspond to the object. Semantic segmentation is one of the essential tasks for complete scene understanding.

## What is Image Segmentation?

Image segmentation is a critical process in computer vision. It involves dividing a visual input into segments to simplify image analysis. Segments represent objects or parts of objects, and comprise sets of pixels, or “super-pixels”. Image segmentation sorts pixels into larger components, eliminating the need to consider individual pixels as units of observation. There are three levels of image analysis:

- **Classification** – categorizing the entire image into a class such as “people”, “animals”, “outdoors”
- **Object detection** – detecting objects within an image and drawing a rectangle around them, for example, a person or a sheep.
- **Segmentation** – identifying parts of the image and understanding what object they belong to. Segmentation lays the basis for performing object detection and classification.

![Analysis](https://missinglink.ai/wp-content/uploads/2019/03/what-is-image-segmentation-e1553795451244.png)

### Semantic Segmentation vs. Instance Segmentation

Within the segmentation process itself, there are two levels of granularity:

- **Semantic segmentation**—classifies all the pixels of an image into meaningful classes of objects. These classes are “semantically interpretable” and correspond to real-world categories. For instance, you could isolate all the pixels associated with a cat and color them green. This is also known as dense prediction because it predicts the meaning of each pixel.

![semantic segmentation](https://missinglink.ai/wp-content/uploads/2019/03/Semantic-segmentation-original-1.png)

- **Instance segmentation**—identifies each instance of each object in an image. It differs from semantic segmentation in that it doesn’t categorize every pixel. If there are three cars in an image, semantic segmentation classifies all the cars as one instance, while instance segmentation identifies each individual car.

## What is?

It is labelling Pixels according to their class. It is also called pixel wise classification or pixel level segmentation. We answer the question **What is in this image and Where the image is located?**

- Algorithm used for this include "Fully Convolutional Network", "Segnet", "U-net". 
- These algorithm uses Encode- Decoder  architecture,  up-sampling, transpose convolution
- Spatial context is important for such segmentation
- This is supervised learning and this means in the ground truth dataset someone has to draw boundary to map everything within the box and its corresponding class. This labelling is quite manual and is important to train the network.

![Image](https://www.mathworks.com/help/vision/ug/semanticsegmentation_transferlearning.png)

![Image](https://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/opencv-semantic-segmentation/opencv_semantic_segmentation_animation.gif)

![Image](https://miro.medium.com/max/875/1*hf6J8vsX7gmHhZnbPa4y9g.png)

In the above image you can see that all cars are labelled with the same color. Each object class has been segmented separately. Introduced in the paper  [Fully Convolutional Networks for Semantic Segmentation](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf). 

Sample results for the pre-trained models provided below...

**Input Image:**

![Image](https://github.com/divamgupta/image-segmentation-keras/raw/master/sample_images/1_input.jpg)

**Output Image**

![Image](https://github.com/divamgupta/image-segmentation-keras/raw/master/sample_images/1_output.png)



## Input Data 

**Output of Semantic Segmentation**

![1597347457799](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597347457799.png)

**Whereas the output of object classification**

![1597347491030](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597347491030.png)



## Base type of Architecture

**Many architecture of semantic segmentation falls into architecture like following which is called Auto Encoder.** Here common technique in Decoder networks are **Up-sampling**,**Un-pooling** and **Transposed-Convolution**.

![1597347573203](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597347573203.png)





## How Deep Learning Powers Image Segmentation Methods

Like most of the other applications, using a CNN for semantic segmentation is the obvious choice. When using a CNN for semantic segmentation, the output is also an image rather than a fixed length vector.

### Convolutional neural networks for segmentation

Usually, the architecture of the model contains several convolutional layers, non-linear activations, batch normalization, and pooling layers. **The initial layers learn the low-level concepts such as edges and colors and the later level layers learn the higher level concepts such as different objects.**

At a lower level, the neurons contain information for a small region of the image, whereas at a higher level the neurons contain information for a large region of the image. Thus, as we add more layers, the size of the image keeps on decreasing and the number of channels keeps on increasing. The downsampling is done by the pooling layers.

**For the case of image classification, we need to map the spatial tensor from the convolution layers to a fixed length vector. To do that, fully connected layers are used, which destroy all the spatial information.**

![img](https://divamgupta.com/assets/images/posts/imgseg/image1.png?style=centerme)

​                                  ***Spatial tensor is downsampled and converted to a vector Image source***

**For the task of semantic segmentation, we need to retain the spatial information, hence no fully connected layers are used**. That’s why they are called **fully convolutional networks**. The convolutional layers coupled with downsampling layers produce a low-resolution tensor containing the high-level information.

Taking the low-resolution spatial tensor, which contains high-level information, we have to produce high-resolution segmentation outputs. To do that we add more convolution layers coupled with upsampling layers which increase the size of the spatial tensor. As we increase the resolution, we decrease the number of channels as we are getting back to the low-level information.

This is called an **encoder-decoder** structure. Where the layers which downsample the input are the part of the encoder and the layers which upsample are part of the decoder.

![img](https://divamgupta.com/assets/images/posts/imgseg/image5.png?style=centerme)*Encoder-Decoder architecture Image source*

When the model is trained for the task of semantic segmentation, the encoder outputs a tensor containing information about the objects, and its shape and size. The decoder takes this information and produces the segmentation maps

**SegNet neural network** An architecture based on deep encoders and decoders, also known as semantic pixel-wise segmentation. It involves encoding the input image into low dimensions and then recovering it with orientation invariance capabilities in the decoder. This generates a segmented image at the decoder end. ![convolutional encoder-decoder](https://missinglink.ai/wp-content/uploads/2019/03/SegNet-neural-network_2x.png)

## Some information on Context

### Converting FC to CONV layers

Our scenario is 

![Image](https://miro.medium.com/max/875/1*4khobU2QrwUKlMopA2w9sA.png)

- A convolutional layers which outputs a volume of size *7×7×512* and this is followed by a FC layer with 4096 neurons i.e. the output of the FC layers is 1x4096 for a single image input.
- We can replace FC layer with a convolutional layer with filter size *7x7*, padding of zero, stride of *1* and output depth of **4906**
- Output will simply be *1x1x4096,* equivalent to the output of the FC layer.

## Sliding Convolution window approach

- We have a convolution window and we try to predict here the center pixel value of the window. So class label belong to entire window will be labelled as the class of the central pixel one. Window here provides contextual information so that class of the center pixel can be predicted.
- Convolution window will have slide of 1
- Our desired output here is to have a feature map of same input image size where each of the value will be class value. So the map will have class label and this label is derived from the highest probability one.
- Major disadvantage here is that  double sliding happening. So same information is getting through convolution multiple times.

![1564763701693](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564763701693.png)

## Fully Convolutional Network-based 

FCN network pipeline is an extension of the classical CNN. The restriction of CNNs to accept and produce labels only for specific sized inputs comes from the fully-connected layers which are fixed. Contrary to them, FCNs only have convolutional and pooling layers which give them the ability to make predictions on arbitrary-sized inputs.

![image](https://miro.medium.com/max/781/1*Aa2fKFN2PEKmMQoy8ps-lw.png)

One issue in this specific **FCN is that by propagating through several alternated convolutional and pooling layers, the resolution of the output feature maps is down sampled**. Therefore, the direct predictions of FCN are typically in low resolution.

More advanced FCN-based approaches have been proposed to address this issue, including [SegNet](https://arxiv.org/pdf/1511.00561.pdf), [DeepLab-CRF](https://arxiv.org/pdf/1412.7062.pdf), and [Dilated Convolutions](https://arxiv.org/pdf/1511.07122.pdf).



## Transposed Convolution

### Why Up-Sampling?

When we use neural networks to generate images, it usually involves up-sampling from low resolution to high resolution.![Image](https://miro.medium.com/max/1057/1*u5hMSBG7fZ7uo85ckmLiUw.png)

There are various methods to conduct up-sampling operation:

- Nearest neighbor interpolation
- Bi-linear interpolation
- Bi-cubic interpolation

All these methods involve some interpolation method which we need to chose when deciding a network architecture. It is like a manual feature engineering and there is nothing that the network can learn about.

### Why Transposed Convolution?

If we want our network to learn how to up-sample optimally, we can use [the transposed convolution](https://arxiv.org/abs/1603.07285). It does not use a predefined interpolation method. It has learnable parameters.

It is useful to understand the transposed convolution concept as it is used in important papers and projects such as:

- the generator in [DCGAN](https://arxiv.org/pdf/1511.06434v2.pdf) takes randomly sampled values to produce a full-size image.
- the [semantic segmentation](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf) uses convolutional layers to extract features in the encoder and then restores the original image size in the decoder so that it can classify every pixel in the original image.

We can use it to conduct up-sampling. Moreover, the weights in the transposed convolution are learnable. So we do not need a predefined interpolation method.

### Reacap of Convolution

The convolution operation calculates the sum of the element-wise multiplication between the input matrix and kernel matrix. Since we have no padding and the stride of 1, we can do this only 4 times. Hence, the output matrix is 2x2.![Image](https://miro.medium.com/max/1030/1*M33WSDDeOSx6nbUZ0sbkxQ.png)

**One important point of such convolution operation is that the positional connectivity exists between the input values and the output values**.

For example, the top left values in the input matrix affect the top left value of the output matrix.

More concretely, the 3x3 kernel is used to connect the 9 values in the input matrix to 1 value in the output matrix. **A convolution operation forms a many-to-one relationship.** **Let’s keep this in mind as we need it later on.**

### Going Backward

Now, Lets associate 1 value in a matrix to 9 values in another matrix. **It’s a one-to-many relationship.** This is like going backward of convolution operation, and it is the core idea of **transposed convolution**.

In image of 5x5 is fed into a convolutional layer. The stride is set to 2, the padding is deactivated and the kernel is 3x3. This results in a 2x2 image.

If we wanted to reverse this process, we’d need the inverse mathematical operation so that 9 values are generated from each pixel we input. Afterward, we traverse the output image with a stride of 2. This would be a deconvolution.

#### Convolution Matrix

We can express a convolution operation using a matrix. It is nothing but a kernel matrix rearranged so that we can use a matrix multiplication to conduct convolution operations.

![img](https://miro.medium.com/max/267/1*0wFFJUNHLRPd3r8R6WT8ng.png)



We rearrange the 3x3 kernel into a 4x16 matrix as below:

![img](https://miro.medium.com/max/1239/1*LKnTr_0k409vOjgj2h4-vg.png)



This is the convolution matrix. Each row defines one convolution operation. If you do not see it, the below diagram may help. Each row of the convolution matrix is just a rearranged kernel matrix with zero padding in different places.

![img](https://miro.medium.com/max/1870/1*yLMY-HCEGg2r7IHevR48oA.png)



To use it, we flatten the input matrix (4x4) into a column vector (16x1).

![img](https://miro.medium.com/max/550/1*0_oqO0AFZBigpBxPcJ7c_A.png)



​									Flattened Input Matrix

We can matrix-multiply the 4x16 convolution matrix with the 16x1 input matrix (16 dimensional column vector).

![img](https://miro.medium.com/max/1650/1*ql2ZxrS_h8D7KHNCrGndug.png)



The output 4x1 matrix can be reshaped into a 2x2 matrix which gives us the same result as before.

![img](https://miro.medium.com/max/191/1*YZwIXPPyb_AsKmxn_em42Q.png)



In short, a convolution matrix is nothing but an rearranged kernel weights, and a convolution operation can be expressed using the convolution matrix.

#### Transposed Convolution Matrix

We want to go from **4 (2x2) to 16 (4x4)**. So, we use a 16x4 matrix. But there is one more thing here. We want to maintain the 1 to 9 relationship.

Suppose we transpose the convolution matrix C (4x16) to C.T (16x4). We can matrix-multiply C.T (16x4) with a column vector (4x1) to generate an output matrix (16x1). 

![img](https://miro.medium.com/max/1331/1*JDAuBt3aS9mz3aQQ7JKYKA.png)



Convolution By Matrix Multiplication

The output can be reshaped into 4x4.

![img](https://miro.medium.com/max/341/1*STkqLI87Q8qlO1gxpG6sJA.png)



**We have just up-sampled a smaller matrix (2x2) into a larger one (4x4).** The transposed convolution maintains the 1 to 9 relationship because of the way it lays out the weights.

NB: the actual weight values in the matrix does not have to come from the original convolution matrix. What’s important is that the weight layout is transposed from that of the convolution matrix

## U-Net

Any image segmentation architecture can be said to have an encoder part followed by a decoder part. The encoder part is usually a pre-trained classifier network like ResNet/VGG which has the job of classifying each pixel into a certain category. The decoder part on the other hand takes those low-resolution classified pixels and projects the features onto a plane so as to get a high-resolution segmented image.

U-Net was designed for the purpose of Biomedical Image Processing. This field relies on high level of data augmentation as much data isn’t available. U-Net overcomes all the drawbacks of the previous state-of-the-art sliding window CNN architecture 

[UNet](https://arxiv.org/abs/1505.04597)[2] is **Convolutional Neural Network (CNN)** which builds on the well known [FCN](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf)[3]. Compared to the [traditional sliding window approach](http://people.idsia.ch/~juergen/nips2012.pdf), which won the Electron Microscopy Segmentation challenge at [ISBI 2012](http://brainiac2.mit.edu/isbi_challenge/home), the FCN pose a more elegant architecture which reduces redundant overlapping patches its predecessor had.

The **Unet consists of 23 convolutional layers with one contraction and one, more or less symmetric, expansion path.** A concatenation of high resolution features from the contracting path to the unsampled features from the expanding path allows for localization

### How?

The UNet architecture can be seen below.

![1597347857845](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597347857845.png)

**Here skip connections are there and then depthwise concatenation happening in decoder network.** *Why skip connection*

- Easier Training
  - Vanishing gradient
- Intuition
  - Coarse feature fill in gaps
- 

![Image](https://github.com/amitkayal/UNet/blob/master/pictures/u-net-architecture.png?raw=true)



Let's first rearrange the above conceptual network as shown below. Here whenever there is down-sampling then we have moved down the layer, otherwise moved it up.

![1564849437449](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564849437449.png)

We now can tweak the above network to connect as shared below to ensure concatenation of feature maps. This will help to get more information which were partially lost due to down-sampling. So here we take the previous sampling resolution and concat with downsample output.

![1564849529307](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564849529307.png)

Implementation wise it is very simple, just couple of convolution layers paired with Max Pooling and ReLu() activation.

### Advantage of U-Net

- As Biomedical Imaging has very less number of images, the network should be highly invariant. That means it should focus more on **what the features are rather than where the features are**. U-Net is able to achieve this due to its *u-shape*, where in the features are merged together to give high resolution results.

- Works efficiently on small datasets through heavy data augmentation as in some cases the number of annotated samples will be less.

- Works for binary as well as multiple classes.

- It is scale-invariant.

- Can be used in a multitude of applications like Object Detection/Segmentation, GANs, etc.

- The features extracted at different levels in the contracting path are then combined with the feature maps in the expansion path giving rise to more number of features which is necessary for an accurate segmentation map.

### Architecture Details

 The architecture contains two paths. 

- First path is the contraction path (also called as the **encoder**) which is used to capture the context in the image. The encoder is just a traditional stack of convolutional and max pooling layers. 
- The second path is the symmetric expanding path (also called as the **decoder**) which is used to enable precise localization using transposed convolutions. 

Thus it is an **end-to-end fully convolutional network** (FCN), i.e. it only contains Convolutional layers and does not contain any Dense layer because of which it can accept image of any size. In the original paper, the UNET is described as follows:![im](https://miro.medium.com/max/1400/1*lvXoKMHoPJMKpKK7keZMEA.png)

- Final activation into final layer is softmax because we need to find out probability value for each of the pixel to draw the segmentation.
- Original u-net architecture proposes that a sub portion of input is concatenated. This is what shows as dotted one.

Essentially the network has following functional aspect. **The difference between the contraction and the expansion layers is that the pooling operations in the contraction network are replaced by up sampling operation in the expansion network**. Also the expansion network has more number of filters which result in high resolution layers.![im](https://miro.medium.com/max/1270/1*dYbiGpoojsAkVYeUMyiLsA.jpeg). 

![1564851695037](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564851695037.png)

In a CNN, an encoder-decoder network typically looks like this (a CNN encoder and a CNN decoder) and further details can be found in [paper](https://arxiv.org/pdf/1511.00561.pdf). 

This is a network to perform semantic segmentation of an image. **The left half of the network maps raw image pixels to a rich representation of a collection of feature vectors. The right half of the network takes these features, produces an output and maps the output back into the “raw” format (in this case, image pixels).**

Here we are first doing down sampling and then doing up sampling. Here pooling gives us **translation invariance** as it is not related to exact location of features. In semantic segmentation pooling helps us to increase receptive field and allows each of output pixel of the MP to see more. This is required because 3x3 or 5x5 or 7X7 kernel will not be enough for us to tell whether central pixel belong to a class. we need more RF to decide on this.

![1564766296514](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564766296514.png)

### Upsampling

Aim here is to increase the output size w.r.t input size. Ex: We have 2x2 after MP and after up sampling we want to have output of 4x4. It generally follows a hour glass structure as shown below.

![1564847770455](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564847770455.png)

Max pooling operation is non-invertible, however, we can obtain an approximate inverse by recording the locations of the maxima within each pooling region in a set of *switch* variables. In the deconvnet, the unpooling operation uses these switches to place the reconstructions from the layer above into appropriate locations, preserving the structure of the stimulus. 

- Replicate

  - Here each of the value in 2x2 gets replicated into 2x2 of the output

- Use once and put others to zero

  - Here we take values from input and put to any random position of 2x2 in the output while setting others to zero

- Retain exact position of max pooling element values and place there

  - To perform unpooling, we need to remember the position of each maximum activation value when doing the max pooling. Then, the remembered position is used for unpooling

  ![1564846950636](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564846950636.png)

- Up sampling through filters

  up sampling can also be learnt through filters as shown below. Here the filter which is doing convolution on upsampled data will learn its weights through back propagation. 

![1564847326341](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564847326341.png)

#### Upsampling layers

we can add multiple upsampling layers like a standard convolution network to have finer segmentation.

![1564848206850](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1564848206850.png)

### UNET Architecture and Training



The [*UNET* ](https://arxiv.org/abs/1505.04597)was developed by Olaf Ronneberger et al. for Bio Medical Image Segmentation. The architecture contains two paths. First path is the contraction path (also called as the encoder) which is used to capture the context in the image. The encoder is just a traditional stack of convolutional and max pooling layers. The second path is the symmetric expanding path (also called as the decoder) which is used to enable precise localization using transposed convolutions. Thus it is an end-to-end fully convolutional network (FCN), i.e. it only contains Convolutional layers and does not contain any Dense layer because of which it can accept image of any size.

In the original paper, the UNET is described as follows:

![Image](https://miro.medium.com/max/1500/1*OkUrpDD6I0FpugA_bbYBJQ.png)



Lets try to describe this architecture much more intuitively. Note that in the original paper, the size of the input image is 572x572x3, however, we will use input image of size 128x128x3. Hence the size at various locations will differ from that in the original paper but the core components remain the same.

Below is the detailed explanation of the architecture:

![Image](https://miro.medium.com/max/1952/1*yzbjioOqZDYbO6yHMVpXVQ.jpeg)



Detailed UNET Architecture

## Points to note:

- 2@Conv layers means that two consecutive Convolution Layers are applied
- c1, c2, …. c9 are the output tensors of Convolutional Layers
- p1, p2, p3 and p4 are the output tensors of Max Pooling Layers
- u6, u7, u8 and u9 are the output tensors of up-sampling (transposed convolutional) layers
- The left hand side is the contraction path (Encoder) where we apply regular convolutions and max pooling layers.
- In the Encoder, the size of the image gradually reduces while the depth gradually increases. Starting from 128x128x3 to 8x8x256
- This basically means the network learns the “WHAT” information in the image, however it has lost the “WHERE” information
- The right hand side is the expansion path (Decoder) where we apply transposed convolutions along with regular convolutions
- In the decoder, the size of the image gradually increases and the depth gradually decreases. Starting from 8x8x256 to 128x128x1
- Intuitively, the Decoder recovers the “WHERE” information (precise localization) by gradually applying up-sampling
- To get better precise locations, at every step of the decoder we use skip connections by concatenating the output of the transposed convolution layers with the feature maps from the Encoder at the same level:
  u6 = u6 + c4
  u7 = u7 + c3
  u8 = u8 + c2
  u9 = u9 + c1
  After every concatenation we again apply two consecutive regular convolutions so that the model can learn to assemble a more precise output
- This is what gives the architecture a symmetric U-shape, hence the name UNET
- On a high level, we have the following relationship:
  Input (128x128x1) => Encoder =>(8x8x256) => Decoder =>Ouput (128x128x1)







## Training

Model is compiled with Adam optimizer and we use binary cross entropy loss function since there are only two classes (salt and no salt).

We use Keras callbacks to implement:

- Learning rate decay if the validation loss does not improve for 5 continues epochs.
- Early stopping if the validation loss does not improve for 10 continues epochs.
- Save the weights only if there is improvement in validation loss.

We use a batch size of 32.

Note that there could be a lot of scope to tune these hyper parameters and further improve the model performance.

# Practical Issues

## Computationally Expensive

![1597348575689](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597348575689.png)

## Class Imbalance

Here taking a crop of input image is a problem because majority of time the cropped image will have background class only or negative class. Also sometime such cropped input image might capture edges of our foreground class class and such few edge pixels(very few which are ex: 3 or 4 pixels) are not enough for network to understand about foreground class and hence ne**twork may predict them as background clas**s. and network will sill penalize them. So such cropping is creating a situation where cropped input does not have enough pixels(or *local information*) of our class (foreground one) and we expect network to predict. **So solution to avoid this is not random/blindly cropping rather than we should do cropping from positive window.** 

![1597348786111](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597348786111.png)

**How we do positive window cropping**

![1597349250986](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597349250986.png)



# Loss Function of Semantic Segmentaion

**Image classification has categorical loss function which is called cross entropy.**

![1597348242448](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597348242448.png)

Now for semantic segmentation, every pixel is a classification problem and they have a class. So one potential loss function for semantic segmentation can be cross-entropy and then just take average loss for all pixel loss. Otherwise we can use Dice Coefficient.

## Metrics to Evaluate Semantic Segmentation Model

How do you know your segmentation model performs well.?

![Image](https://miro.medium.com/max/1607/1*YZudFQ0ChAUV1TycWc3C-A.png)

## Pixel Accuracy

It is perhaps the easiest to understand conceptually. *It is the percent of pixels in your image that are classified correctly.*

Let’s say you ran the following image(*Left*)through your segmentation model. The image on the right is the ground truth, or annotation (what the model is supposed to segment). In this case, our model is trying to segment ships in a satellite image.

![Image](https://miro.medium.com/max/2625/0*AmruarcqPbBG4jUx.png)

You see that your segmentation accuracy is **95%**

. That’s awesome! Let’s see how your segmentation looks like! ![Image](https://miro.medium.com/max/656/1*yO-dem7wHFv0zNN1LM0saA.png)

It’s just that one class was 95% of the original image. So if the model classifies all pixels as that class, 95% of pixels are classified accurately while the other 5% are not. As a result, although your accuracy is a whopping 95%, your model is returning a completely useless prediction. This is meant to illustrate that high pixel accuracy doesn’t always imply superior segmentation ability.

This issue is called **class imbalance**. When our classes are extremely imbalanced, it means that a class or some classes dominate the image, while some other classes make up only a small portion of the image.

## Intersection-Over-Union (IoU, Jaccard Index)

The Intersection-Over-Union (IoU), also known as the Jaccard Index, is one of the most commonly used metrics in semantic segmentation… and for good reason. The IoU is a very straightforward metric that’s extremely effective.

 ![image](https://miro.medium.com/max/563/0*kraYHnYpoJOhaMzq.png)

**IoU is the area of overlap between the predicted segmentation and the ground truth divided by the area of union between the predicted segmentation and the ground truth**, as shown on the image to the left. This metric ranges from 0–1 (0–100%) with 0 signifying no overlap (garbage) and 1 signifying perfectly overlapping segmentation (fat dub).

For **binary** (two classes) or **multi-class segmentation**, the mean IoU of the image is calculated by **taking the IoU of each class and averaging them**.

 ![Image](https://miro.medium.com/max/668/1*FcuTtRWwHi1zGycFHRdEHg.png) ![Image](https://miro.medium.com/max/656/1*yO-dem7wHFv0zNN1LM0saA.png)

Union consists of all of the pixels classified as ships from **both** images, minus the overlap/intersection. In this case, there are 5 pixels (this is an arbitrary number choice) that are classified as ships total. Subtract the overlap/intersection which is 0 to get 5 as the area of union. After doing the calculations, we learn that the IoU is merely **47.5%!** 

## Dice Coefficient (F1 Score)

Simply put, the **Dice Coefficient is 2 \* the Area of Overlap divided by the total number of pixels in both images.** (See explanation of area of union in section 2).

![Image](https://miro.medium.com/max/804/1*yUd5ckecHjWZf6hGrdlwzA.png)

![1597348385041](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1597348385041.png)

- Total Number of Pixels for both images combined = 200
- Ships: Area of Overlap = 0  *(2 \* Area of Overlap)/(total pixels combined) = 0/200 = 0*

- Background: 

  Area of Overlap = 95

  *(2 \* Area of Overlap)/(total pixels combined) = 95\*2/200 = 0.95*

- Dice 

  *(Ships + Background)/2 = (0%+95%)/2 =* **47.5%**

The Dice coefficient is very similar to the IoU. They are positively correlated, meaning if one says model A is better than model B at segmenting an image, then the other will say the same. Like the IoU, they both range from 0 to 1, with 1 signifying the greatest similarity between predicted and truth.





# One by One [ 1 x 1 ] Convolution

## What is that?

![Image](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/conv_arithmetic/full_padding_no_strides_transposed.gif) ![Image](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/conv_arithmetic/full_padding_no_strides_transposed_small.gif)

​		left : **Convolution with kernel of size 3x3** right : **Convolution with kernel of size 1x1**



**Andrew Ng’s video link below explains this visually. A summary of his explanation**

When we do a standard convolution of say a 6x6 image with three color channels(*depth -3*) , Fig 1. below, with a single filter of dimension 3x3x3 (*depth of filter has to match input volume depth*) we get as output 4x4x1 (*assuming stride 1 and no padding*). The key point to note here is the output is collapsed from depth 3 to depth 1 *(granted width and height changed too but we could have kept that same as input by proper choice of padding of input)*.

![img](https://qphs.fs.quoracdn.net/main-qimg-543980c1c593016c48331ba0b399ea34)

Fig 1.

Now instead of using a 3 x 3 x 3 filter, if we use a 1 x 1 x 3 *(often called 1x1 since the depth is a variable and forced to match input volume depth - which is perhaps why it is so confusing), fig 2.* the output again has depth 1 as in previous case (fig 1), except since we convolved with a 1x1 filter, the width and height of the input remains unchanged.

![img](https://qphs.fs.quoracdn.net/main-qimg-3d412cacb0435a8e56eda709ae26795f)

Fig 2.

However, if we increase the number of filters we can control the depth of the output. For instance, using two filters *(each of depth 3)* in the figure below , fig 3, the output depth is 2.

![img](https://qphs.fs.quoracdn.net/main-qimg-0b3c4bbc86cc5c73efb8dbf2c699265a)

Fig 3.

Finally in the case of Fig 4 below, where we use the 3 filters, the input and output volumes are exactly the same dimension. So the filters serve as a means to add a nonlinearity to the input volume *(though I don’t know/think if it is ever used this way)*

![img](https://qphs.fs.quoracdn.net/main-qimg-80ebcfc916a3016013b14e258c82daaa)

Fig 4.

In summary, 1x1 convolutions serve as a means to

- control the depth of the input volume as it is passed to the next layer, either decrease it, or increase it, or just add a non-linearity when it doesn’t alter the depth. This control is achieved by the choosing the appropriate number of filters. We can control the other two dimensions - width and height by the filter sizes and padding parameters, or use pooling to reduce width and height.
- In the case when it is reduces the dimensions, it is a means to reduce computations - can be an order of magnitude less as shown in the example from Andrew’s lectures fig. 5 (without 1x1) and fig 6 (with 1x1).

![img](https://qphs.fs.quoracdn.net/main-qimg-7df9c28f92d879d9f9e6d25f6f991a1e)

Fig 5. without 1x1 - 120 million computations

![img](https://qphs.fs.quoracdn.net/main-qimg-93361dde6ee02fb428e5df5416718c0c)

## Simple Answer

Most simplistic explanation would be that 1x1 convolution leads to dimension reductionality. For example, an image of 200 x 200 with 50 features on convolution with 20 filters of 1x1 would result in size of 200 x 200 x 20. But then again, is this is the best way to do dimensionality reduction in the convoluational neural network? What about the efficacy vs efficiency?

## Complex Answer

### Feature transformation

Although 1x1 convolution is a ‘feature pooling’ technique, there is more to it than just sum pooling of features across various channels/feature-maps of a given layer. 1x1 convolution acts like coordinate-dependent transformation in the filter space[[1](https://plus.google.com/118431607943208545663/posts/2y7nmBuh2ar)]. It is important to note here that this transformation is strictly linear, but in most of application of 1x1 convolution, it is succeeded by a non-linear activation layer like ReLU. This transformation is learned through the (stochastic) gradient descent. But an important distinction is that it suffers with less over-fitting due to smaller kernel size (1x1).

### Non Linearity

Add more nonlinearity to the representation learned by the previous layer so that supposedly enhance the representation of the network.

1x1 filter does not consider spatial information but takes channels into account.  

## More Uses

- 1x1 Convolution can be combined with Max pooling

![Pooling with 1x1 convolution](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/conv_arithmetic/numerical_max_pooling.gif) **Pooling with 1x1 convolution**

- 1x1 Convolution with higher strides leads to even more redution in data by decreasing resolution, while losing very little non-spatially correlated information.

![1x1 convolution with strides](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/conv_arithmetic/no_padding_strides.gif) **1x1 convolution with strides**

- Replace fully connected layers with 1x1 convolutions as Yann LeCun believes they are the same 

  > In Convolutional Nets, there is no such thing as “fully-connected layers”. There are only convolution layers with 1x1 convolution kernels and a full connection table. – [Yann LeCun](https://www.facebook.com/yann.lecun/posts/10152820758292143)

  They are used in such way: we have image with size 32x32x100, where 100 means features, and after applying 20 1x1 convolutions filters we will get images with 32x32x20 dimensions.

  ![/images/ML_notes/convolutions/02_1x1_convs.png](https://ikhlestov.github.io/images/ML_notes/convolutions/02_1x1_convs.png)

  # Label Smoothing

  ## Intuition

  The answer is that we don’t want our model to become **too confident** in its predictions.

  By applying label smoothing we can lessen the confidence of the model and prevent it from descending into deep crevices of the loss landscape where overfitting occurs.

  ## Solution

  When performing image classification tasks we typically think of labels as **hard, binary assignments.** 

  ![Image](https://www.pyimagesearch.com/wp-content/uploads/2019/12/keras_label_smoothing_mnist_digit.png)

  This digit is clearly a *“7”*, and if we were to write out the one-hot encoded label vector for this data point it would look like the following:

  ```
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
  ```

  What will happen when we say??

  *“Well, I’m sure that’s a 7. But even though I’m 100% certain that it’s a 7, I’m going to put 90% of that 7 in the ‘7’ box and then divide the remaining 10% into all boxes just so my brain doesn’t overfit to what a ‘7’ looks like.”*

  If we were to apply soft label assignment to our one-hot encoded vector above it would now look like this:

  ```
  [0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.91 0.01 0.01]
  - Notice how summing the list of values equals 1, just like in the original one-hot encoded vector.
  ```

  Unlike hard label assignments where class labels are binary (i.e., positive for one class and a negative example for all other classes), soft label assignment allows:

  - The positive class to have the largest probability
  - While all other classes have a very small probability

# Depthwise Separable Convolutions

The depthwise separable convolution is so named because it deals not just with the spatial dimensions, but with the depth dimension — the number of channels — as well. 

A depthwise separable convolution splits a kernel into 2 separate kernels that do two convolutions: **the depthwise convolution and the pointwise convolution**. But first of all, let’s see how a normal convolution works.

## Depthwise Convolution

we give the input image a convolution without changing the depth. We do so by using 3 kernels of shape 5x5x1. ![Image](https://miro.medium.com/max/2453/1*yG6z6ESzsRW-9q5F_neOsg.png)

Each 5x5x1 kernel iterates 1 channel of the image (note: **1 channel**, not all channels), getting the scalar products of every 25 pixel group, giving out a 8x8x1 image. Stacking these images together creates a 8x8x3 image.

## Pointwise Convolution

The pointwise convolution is so named because it uses a 1x1 kernel, or a kernel that iterates through every single point. This kernel has a depth of however many channels the input image has; in our case, 3. Therefore, we iterate a 1x1x3 kernel through our 8x8x3 image, to get a 8x8x1 image.![image](https://miro.medium.com/max/2291/1*37sVdBZZ9VK50pcAklh8AQ.png)

## Summary

**We’ve separated the convolution into 2: a depthwise convolution and a pointwise convolution. In a more abstract way, if the original convolution function is 12x12x3 — (5x5x3x256) →12x12x256, we can illustrate this new convolution as 12x12x3 — (5x5x1x1) — > (1x1x3x256) — >12x12x256.**

- 256 5x5x3 kernels that move 8x8 times. That’s 256x3x5x5x8x8=1,228,800 multiplications
- Depthwise separable Convolution
  - In the depthwise convolution, we have 3 5x5x1 kernels that move 8x8 times. That’s 3x5x5x8x8 = 4,800 multiplications. 
  - In the pointwise convolution, we have 256 1x1x3 kernels that move 8x8 times. That’s 256x1x1x3x8x8=49,152 multiplications. Adding them up together, that’s 53,952 multiplications.
- Main difference is this: in the normal convolution, we are **transforming the image 256 times**. And every transformation uses up 5x5x3x8x8=4800 multiplications. In the separable convolution, we only really **transform the image once** — in the depthwise convolution. Then, we take the transformed image and **simply elongate it to 256 channels**. Without having to transform the image over and over again, we can save up on computational power.

# Group Convolution

Usually, convolution filters are applied on an image layer by layer to get the final output feature maps. We increase the no of kernels per layer to learn more no of intermediate features, therefore increasing the no of channels in the next layer. But to learn more no. of features, we could also create two or more models that train and backpropagate in parallel. This process of using different set of convolution filter groups on same image is called as grouped convolution.

Grouped convolutions were initial mentioned in AlexNet, and later reused in [ResNeXt](https://arxiv.org/abs/1611.05431). Main motivation of such convolutions is to reduce computational complexity while dividing features on groups. ![Image](https://ikhlestov.github.io/images/ML_notes/convolutions/05_2_group_convolutions.png)

- With grouped convolutions, we can build networks as wide as we want. Take one modular block of filter group and replicate them.
- Now, each filter convolves only on some of the feature maps obtained from kernel filters in its filter group, we are drastically reducing the no of computations to get output feature maps. If we were to take all kernel filters in grouped convolutions and not use the concept of grouped convolutions, the number of computations will grow exponentially.

Grouped convolutions seem to be learning better representations of the data. Essentially, the correlation between kernel filters of different filter groups is usually quite less, which implies that, each filter group is learning a unique representation of the data. This is something which might not be easily possible in traditional neural networks as the kernels will usually correlate with each other.![1580576753350](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1580576753350.png)

# Inception Network

## Intuition?

- **Salient parts** in the image can have extremely **large variation** in size. For instance, an image with a dog can be either of the following, as shown below. The area occupied by the dog is different in each image.

![img](https://miro.medium.com/max/2955/1*aBdPBGAeta-_AM4aEyqeTQ.jpeg)

From left: A dog occupying most of the image, a dog occupying a part of it, and a dog occupying very little space

- Because of this huge variation in the location of the information, choosing the **right kernel size** for the convolution operation becomes tough. A **larger kernel** is preferred for information that is distributed more **globally**, and a **smaller kernel** is preferred for information that is distributed more **locally.**
- **Very deep networks** are prone to **overfitting**. It also hard to pass gradient updates through the entire network.
- Naively stacking large convolution operations is **computationally expensive**.

## The Solution:

Why not have filters with **multiple sizes** operate on the **same level**? The network essentially would get a bit “**wider**” rather than “deeper”. The authors designed the inception module to reflect the same.

The below image is the “naive” inception module. It performs **convolution** on an input, with **3 different sizes of filters** (1x1, 3x3, 5x5). Additionally, **max pooling** is also performed. The outputs are **concatenated** and sent to the next inception module. ![Image](https://miro.medium.com/max/1571/1*DKjGRDd_lJeUfVlY50ojOA.png)

## Further Inception Layers

- Authors **limit** the number of **input channels** by adding an **extra 1x1 convolution** before the 3x3 and 5x5 convolutions
- Adding an extra operation may seem counterintuitive, 1x1 convolutions are far more cheaper than 5x5 convolutions, and the reduced number of input channels also helpful.
- 1x1 convolution is introduced after the max pooling layer, rather than before.

![Image](https://miro.medium.com/max/1543/1*U_McJnp7Fnif-lw9iIC5Bw.png)

## GoogLeNet 

![image](https://miro.medium.com/max/1553/1*uW81y16b-ptBDV8SIT1beQ.png)

- GoogLeNet. The orange box is the **stem**, which has some preliminary convolutions. The purple boxes are **auxiliary classifiers**. The wide parts are the inception modules.

- GoogLeNet has 9 such inception modules stacked linearly. It is 22 layers deep (27, including the pooling layers). It uses global average pooling at the end of the last inception module.

- In order to prevent **Vanishing Gradients** problems  and **middle part** of the network from “**dying out**”, the authors introduced **two auxiliary classifiers** (The purple boxes in the image). They essentially applied softmax to the outputs of two of the inception modules, and computed an **auxiliary loss** over the same labels. The **total loss function** is a **weighted sum** of the **auxiliary loss** and the **real loss**. Weight value used in the paper was 0.3 for each auxiliary loss.

  ```
  # The total loss used by the inception net during training.
  total_loss = real_loss + 0.3 * aux_loss_1 + 0.3 * aux_loss_2
  ```

- Auxiliary loss is purely used for training purposes, and is ignored during inference.

## Inception v2

### Intution

- The intuition was that, neural networks perform better when convolutions didn’t alter the dimensions of the input drastically. Reducing the dimensions too much may cause loss of information, known as a “representational bottleneck”
- Smart Convolution(**Factorize** convolutions of filter size **nxn** to a **combination** of **1xn and nx1** convolutions)

### Solution

- **Factorize 5x5** convolution **to two 3x3** convolution operations to improve computational speed. So stacking two 3x3 convolutions infact leads to a boost in performance. ![image](https://miro.medium.com/max/1044/1*RzvmmEQH_87qKWYBFIG_DA.png)



- A 3x3 convolution is equivalent to first performing a 1x3 convolution, and then performing a 3x1 convolution on its output. They found this method to be **33% more cheaper** than the single 3x3 convolution.

  ![Image](https://miro.medium.com/max/1121/1*hTwo-hy9BUZ1bYkzisL1KA.png)

  - The **filter banks** in the module were **expanded** (made wider instead of deeper) to remove the representational bottleneck. ![Image](https://miro.medium.com/max/1078/1*DVXTxBwe_KUvpEs3ZXXFbg.png)

## Inception v3

### Intution

- The authors noted that the **auxiliary classifiers** didn’t contribute much until near the end of the training process, when accuracies were nearing saturation. They argued that they function as **regularizes**, especially if they have BatchNorm or Dropout operations.
- Possibilities to improve on the Inception v2 without drastically changing the modules were to be investigated.

### The Solution

- **Inception Net v3** incorporated all of the above upgrades stated for Inception v2, and in addition used the following:
  - RMSProp Optimizer.
  - Factorized 7x7 convolutions.
  - BatchNorm in the Auxillary Classifiers.
  - Label Smoothing (A type of regularizing component added to the loss formula that prevents the network from becoming too confident about a class. Prevents over fitting).

# MiniGoogLeNet

### MiniGoogLeNet on CIFAR-10

The details about CIFAR-10 datasets can be found [here](https://www.cs.toronto.edu/~kriz/cifar.html). The MiniGoogLeNet on CAFAR-10 dataset is inspired by [Eric Jang](https://twitter.com/ericjang11) and [pluskid](https://twitter.com/pluskid).

There are three modules inside MiniGoogLeNet, including Conv module, inception module, downsample module. Figure 1 shows the MiniGoogLeNet architecture. ![Image](https://github.com/meng1994412/GoogLeNet_from_scratch/raw/master/output/minigooglenet_architecture.png)

 The input to the model includes dimensions of the image (height, width, depth, and number of classes). In this part, the input would be (width = 32, height = 32, depth = 3, classes = 10).

# DEEPLABV3-RESNET101

For the semantic segmentation model, GluonCV-Torch mainly supports pre-trained FCN, PSPNet and DeepLab-V3. DeepLab-V3 is a very common open source model, which has very good effect on semantic segmentation tasks. The pre-training effects of these three models in the Pascal VOC dataset are shown below, where Pascal VOC contains 20 categories of images:

## Dilated Convolution

**Standard Convolution (l=1) (Left) Dilated Convolution (l=2) (Right)**

![im](https://miro.medium.com/max/1185/1*btockft7dtKyzwXqfq70_w.gif)

- The above illustrate an example of dilated convolution when l=2. We can see that the receptive field is larger compared with the standard one.![im](https://miro.medium.com/proxy/1*tnDNIyPePgHvb8JIx8SbqA.png)

  **l=1 (left), l=2 (Middle), l=4 (Right)**    

## Understanding the DeepLab Model Architecture

DeepLab V3 uses ImageNet’s pretrained Resnet-101 with atrous convolutions as its main feature extractor. In the modified ResNet model, the last ResNet block uses atrous convolutions with different dilation rates. It uses Atrous Spatial Pyramid Pooling and bilinear upsampling for the decoder module on top of the modified ResNet block.

DeepLab V3+ uses Aligned Xception as its main feature extractor, with the following modifications:

1. All max pooling operations are replaced by depthwise separable convolution with striding
2. Extra batch normalization and ReLU activation are added after each 3 x 3 depthwise convolution
3. Depth of the model is increased without changing the entry flow network structure



![img](https://i0.wp.com/s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2019/01/semantic_8.png?resize=649%2C333&ssl=1)

## References

- https://www.kaggle.com/mobassir/deeplabv3-resnet101-for-severstal-sdd/notebook
- 

# Why Odd Filter Size?

The explanation for that is that though we may use even sized filters, odd filters are preferable because if we were to consider the final output pixel (of next layer) that was obtained by convolving on the previous layer pixels, all the previous layer pixels would be symmetrically around the output pixel. Without this symmetry, we will have to account for distortions across the layers. This will happen due to the usage of an even sized kernel. Therefore, even sized kernel filters aren’t preferred.

![Image](https://miro.medium.com/max/1208/0*zZDxNYnURBLdxnKn.jpg)

