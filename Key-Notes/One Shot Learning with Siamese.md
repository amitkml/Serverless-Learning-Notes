[TOC]

# Introduction

Deep Convolutional Neural Networks have become the state of the art methods for image classification tasks. However, one of the biggest limitations is they require a lots of labelled data. In many applications, collecting this much data is sometimes not feasible. One Shot Learning aims to solve this problem.

# Classification vs One Shot Learning

In case of **standard classification**, the input image is fed into a series of layers, and finally at the output we generate a probability distribution over all the classes (typically using a Softmax). For example, if we are trying to classify an image as cat or dog or horse or elephant, then for every input image, we generate 4 probabilities, indicating the probability of the image belonging to each of the 4 classes. 

Two important points must be noticed here. **First**, during the training process, we require a **large** number of images for each of the class (cats, dogs, horses and elephants). **Second**, if the network is trained only on the above 4 classes of images, then we cannot expect to test it on any other class, example “zebra”. If we want our model to classify the images of zebra as well, then we need to first get a lot of zebra images and then we must **re-train** the model again. There are applications wherein we neither have enough data for each class and the total number classes is huge as well as dynamically changing. Thus, the cost of data collection and periodical re-training is too high.

On the other hand, in a **one shot classification**, we require only one training example for each class. Yes you got that right, just one. Hence the name **One Shot**. Let’s try to understand with a real world practical example.

Assume that we want to build face recognition system for a small organization with only 10 employees (small numbers keep things simple). Using a traditional classification approach, we might come up with a system that looks as below:

![img](https://miro.medium.com/max/1800/1*A49puFRGzvHjRJJBHTxryg.jpeg)



Standard classification using CNN

**Problems:**

a) To train such a system, we first require a lot of **different** images of each of the 10 persons in the organization which might not be feasible. (Imagine if you are doing this for an organization with thousands of employees).

b) What if a new person joins or leaves the organization? You need to take the pain of collecting data again and re-train the entire model again. This is practically not possible specially for large organizations where recruitment and attrition is happening almost every week.

Now let’s understand how do we approach this problem using one shot classification which helps to solve both of the above issues:

![img](https://miro.medium.com/max/1800/1*g-561DsAfbU6gcVEk9AC4g.jpeg)

​							One Shot Classification

![Image](https://miro.medium.com/max/3101/1*jQcJ7ik58aeTV0As2d9Jcw.png)

Instead of directly classifying an input(test) image to one of the 10 people in the organization, this network instead takes an extra reference image of the person as input and will produce a similarity score denoting the chances that the two input images belong to the same person. Typically the similarity score is squished between 0 and 1 using a sigmoid function; wherein 0 denotes no similarity and 1 denotes full similarity. Any number between 0 and 1 is interpreted accordingly.

Notice that this network is not learning to classify an image directly to any of the output classes. Rather, it is learning a **similarity function**, which takes two images as input and expresses how similar they are.

How does this solve the two problems we discussed above?

a) In a short while we will see that to train this network, you do not require too many instances of a class and only few are enough to build a good model.

b) But the biggest advantage is that , let’s say in case of face recognition, we have a new employee who has joined the organization. Now in order for the network to detect his face, we only require a **single** image of his face which will be stored in the database. Using this as the reference image, the network will calculate the similarity for any new instance presented to it. Thus we say that network predicts the score in **one shot**.

# Siamese-Networks-for-One-Shot-Learning

The code uses Keras library and the Omniglot dataset. This repository tries to implement the code for Siamese Neural Networks for One-shot Image Recognition by Koch *et al.*

**Siamese neural network** *is an* [artificial neural network](https://en.wikipedia.org/wiki/Artificial_neural_network) *that use the same weights while working in tandem on two different input vectors to compute comparable output vectors. Often one of the output vectors is precomputed, thus forming a baseline against which the other output vector is compared. This is similar to comparing* [fingerprints](https://en.wikipedia.org/wiki/Fingerprint) *or more technical as a distance function for* [Locality-sensitive hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)*.*

## One-Shot Learning

Currently most deep learning models need generally thousands of  labeled samples per class. Data acquisition for most tasks is very  expensive. The possibility to have models that could learn from one or a  few samples is a lot more interesting than having the need of acquiring  and labeling thousands of samples. One could argue that a young child  can learn a lot of concepts without needing a large number of examples.   This is where one-shot learning appears: the task of classifying with  only having access of one example of each possible class in each test  task. This ability of learning from little data is very interesting and  could be used in many machine learning problems.

Despite this paper is focused on images, this concept can be applied  to many fields. To fully understand the problem we should describe what  is considered an example of an one-shot task. Given a test sample, X, an  one-shot task would aim to classify this test image into one of C  categories. For this support set of samples with a representing N unique  categories (N-way one shot task) is given to the model in order to  decide what is the class of the test images. Notice that none of the  samples used in this one-shot task have been seen by the model (the  categories are different in training and testing).

Frequently for one-shot learning tasks, the Omniglot dataset is used  for evaluating the performance of the models. Let’s take a deeper look  to this database, since it was the dataset used in the paper (MNIST was  also tested but we will stick with Omniglot).

## Omniglot Dataset

   [![Omniglot Dataset](https://user-images.githubusercontent.com/10371630/36079867-c94b19fe-0f7f-11e8-9ef8-6f017d214d43.png)](https://user-images.githubusercontent.com/10371630/36079867-c94b19fe-0f7f-11e8-9ef8-6f017d214d43.png) 

The Omniglot dataset consists in 50 different alphabets, 30 used in a  background set and 20 used in a evaluation set. Each alphabet has a  number of characters from 14 to 55 different characters drawn by 20  different subjects, resulting in 20 105x105 images for each character.  The background set should be used in training for hyper parameter tuning  and feature learning, leaving the final results to the remaining 20  alphabets, never seen before by the models trained in the background  set. Despite that this paper uses 40 background alphabets and 10  evaluation alphabets.

This dataset is considered as sort of a MNIST transpose, where the  number of possible classes is considerably higher than the number of  training samples, making it suitable to one-shot tasks.

The authors use 20-way one-shot task for evaluating the performance  in the evaluation set. For each alphabet it is performed 40 different  one-shot tasks, completing a total of 400 tasks for the 10 evaluation  alphabets. An example of one one-shot task in this dataset can be seen  in the following figure:

   [![One-Shot Task](https://user-images.githubusercontent.com/10371630/36079892-1df60568-0f80-11e8-8297-a7c6beec4491.png)](https://user-images.githubusercontent.com/10371630/36079892-1df60568-0f80-11e8-8297-a7c6beec4491.png) 

Let's dive into the methodology proposed by Koch_et al._ to solve this one-shot task problem.

## Methodology

To solve this methodology, the authors propose the use of a Deep  Convolutional Siamese Networks.  S**iamese Nets were introduced by Bromley  and Yan LeCun in the 90s for a verification problem. Siamese nets  are two twin networks that accept distinct inputs but are  joined in by a energy function that calculates a distance metric between  the outputs of the two nets**. The weights of both networks are tied, allowing them to compute the same  function. In this paper the weighed L1 distance between twin feature vectors is  used as energy function, combined with a sigmoid activations.

![1582819906219](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582819906219.png)

This architecture seems to be designed for verification tasks, and this is exactly how the authors approach the problem.

In the paper a convolutional neural net was used. 3 Blocks of  Cov-RELU-Max Pooling are used followed by a Conv-RELU connected to a  fully-connected layer with a sigmoid function. This layer produces the  feature vectors that will be fused by the L1 weighed distance layer. The  output is fed to a final layer that outputs a value between 1 and 0  (same class or different class).  To assess the best architecture,  Bayesian hyper-parameter tuning was performed. The best architecture is  depicted in the following image:

   [![best_architecture](https://user-images.githubusercontent.com/10371630/36121224-71403aa0-103d-11e8-81c6-6caae24a835c.png)](https://user-images.githubusercontent.com/10371630/36121224-71403aa0-103d-11e8-81c6-6caae24a835c.png) 

L2-Regularization is used in each layer, and as an optimizer it is  used Stochastic Gradient Descent with momentum. As previously mentioned,  Bayesian hyperparameter optimization was used to find the best  parameters for the following topics:

- Layer-wise Learning Rates (search from 0.0001 to 0.1)
- Layer-wise Momentum (search from 0 to 1)
- Layer-wise L2-regularization penalty (from 0 to 0.1)
- Filter Size from 3x3 to 20x20
- Filter numbers from 16 to 256 (using multipliers of 16)
- Number of units in the fully connected layer from 128 to 4096 (using multipliers of 16)

For training some details were used:

- The learning rate is defined layer-wise and it is decayed by 1% each epoch.
- In every layer the momentum is fixed at 0.5 and it is increased linearly each epoch until reaching a value mu.
- 40 alphabets were used in training and validation and 10 for evaluation
- The problem is considered a verification task since the train  consists in classifying pairs in same or different character. - After  that in evaluation phase, the test image is paired with each one of the  support set characters. The pair with higher probability output is  considered the class for the test image.
- Data Augmentation was used with affine distortions (rotations, translations, shear and zoom)

**Network**

[![img](https://github.com/rohanrao619/Face_Recognition_using_Siamese_Network/raw/master/Images/Siamese_Network.png)](https://github.com/rohanrao619/Face_Recognition_using_Siamese_Network/blob/master/Images/Siamese_Network.png)

As shown, two faces are compared to find if they belong to the same person or not. A given input face is checked against all the faces present in the Face_database (faces of known persons). The person having minimum distance to the input face is identified as the target (if distance < threshold). Threshold value needs to be tuned according to the application.



# Input Dataset

![1582829224554](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582829224554.png)

# Basic Working

In the case of finding similarity between images we can first get the images in numpy array format and feed them through any architecture(should be same for both images) and get an n-dimensional representation at the end of the common network. These n-dimensional representations can then be used as input to some loss function or a similarity metric or a simple neural network architecture would work as well. One simple example of Siamese network is: ![Image](https://miro.medium.com/max/1096/1*TjIZ52znavYCghYs0WBgLA.png)

- left_input and right_input shown in the above image represents the vectorized form of the two input images we wish to compare similarity.
- These image representation are then fed to a common network (a CNN in the above example)
- Same operations are performed on both the image vectors and the finally the distance between both of them is calculated by subtracted the vectors.
- The output of the difference of both the vectors is connected to a simple sigmoid output layer. Note that the input to this network is a list of two inputs — left_input and right_input.

# Siamese network for image similarity

Siamese networks work very well for image similarity tasks.

[![img](https://github.com/rohanrao619/Face_Recognition_using_Siamese_Network/raw/master/Images/Siamese_Network.png)](https://github.com/rohanrao619/Face_Recognition_using_Siamese_Network/blob/master/Images/Siamese_Network.png)

As shown, two faces are compared to find if they belong to the same person or not. A given input face is checked against all the faces present in the Face_database (faces of known persons). The person having minimum distance to the input face is identified as the target (if distance < threshold). Threshold value needs to be tuned according to the application.

The base model or the common network in the Siamese network(as discussed above) used in this case study is VGGFACE pre-trained model (you can use any architecture of your choice here)in which trainable parameter for all the layers except the last three layers. The significance of doing this is that the top layers are just being used for feature engineering and the later layers responsible for decision making can be fine-tuned.

![Image](https://miro.medium.com/max/1178/1*Mc3KoB1lMBlJQikl-w57Xw.png)

- x1 and x2 shown in the code are the features representing the two images. 

- These two vectors are then sent through Global Max Pool and Global Avg Pool. 
- x3 vector is the difference of of the vectors which then squared. 
- Similarly x4 vector is the difference of the sqaure of x1 and x2 vectors. 
- Further, x5 vector is the cosine similarity between x1 and x2 vectors. 
- Finally, the x3, x4, x5 are concatenated and fed to a dense layer followed by a Dropout layer and then output sigmoid layer.

**In simple words, the two images are featurized using a common network, then these two feature vectors can be directly used or sent through some decision making network to check for similarity between images.**

# Siamese in conjunction with triplet loss

Siamese network is often used in conjunction with triplet loss. Triplet loss synergies quite well with Siamese network because it accepts three different images or any input which is fed through a common Siamese network for getting features which can be used to later predict/classify accordingly.

According to Wikipedia:

> **Triplet loss** is a [loss function](https://en.wikipedia.org/wiki/Loss_function) for [artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network) where a baseline (anchor) input is compared to a positive (truthy) input and a negative (falsy) input. The distance from the baseline (anchor) input to the positive (truthy) input is minimized, and the distance from the baseline (anchor) input to the negative (falsy) input is maximized.
>
> It is often used for [learning similarity](https://en.wikipedia.org/wiki/Similarity_learning) of for the purpose of learning embeddings, like [word embeddings](https://en.wikipedia.org/wiki/Word_embedding) and even [thought vectors](https://en.wikipedia.org/wiki/Thought_vector), and [metric learning](https://en.wikipedia.org/wiki/Metric_learning).

In triplet loss basically, 

- we have three inputs- anchor, positive and negative. 

- Anchor can be any image of the person, positive is some other image of the same person and negative is an image of different person. 

- The loss function can be described as: L=max(d(a,p)−d(a,n)+margin,0) where d(a,p) is the distance between anchor image and positive image. Similarly, d(a,n) is the distance between anchor and negative image.

  ![Image](https://miro.medium.com/max/586/1*ESSKGKp-wKMaxU74lMCs1Q.png)

  *As it can be seen in the above image the triplet loss function tries to maximize the distance between anchor image and negative image while minimizing the distance between anchor image and positive image thereby learning to differentiate similar images to non similar ones.* 

**This one presents the manner of training the network to differentiate between intra-class and inter-class cases. By pairing the images into triplet pairs of *Anchor-Positive* and *Anchor-Negative*, the network learns the distribution of images from each class with respect to all other classes**

In practical scenarios the datasets we generally work with will have image pairs and output labels. So, we will have to first generate inputs such that instead of image pairs we have triplets of anchor, positive and negative image. We won’t require an output label so any dummy value will work as our triplet loss will try to work on the distances of the images rather than any labels.

## Learning Objective

Our aim is to have similar set of encoding given following two pictures from our Neural Network as we want them to predict as similar ones.

![1582820370407](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582820370407.png)

But for the following pairs, we want our Neural Network to have different set of encoding as these are not similar images.

![1582820592455](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582820592455.png)

So basically in Triplet loss, we are comparing Anchor, Positive and Negative Image and train the network.

![1582820691242](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582820691242.png)

So basically **our model loss function wants the distance between Anchor and Positive Image to be always less or equal to distance between Anchor and Negative Image**.

![1582820908606](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582820908606.png) and so loss function will be: ![1582821042402](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582821042402.png)

But the above loss function has one issue whereby the NN can make both component **as 0 and hence 0-0 will become equal to 0**. So this situation will force Neural network force Encoding of Anchor Image, Positive Image and Negative image as perfectly identical which will be completely wrong. So in order to avoid this situation, **we generally say it should be less than -x where this value of x is called a margin which is a hyperparameter**.

![1582821272873](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582821272873.png)

So our final loss function will be:

![1582821826057](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582821826057.png)

whereby

- If the first component is less than zero then max value will return 0 and hence loss will become 0
- If the first component is more than zero then loss will be positive and hence Backpropagation will try to reduce the loss.

So our final cost function will be sum of all the Loss over M No of images. So here if we have 10K images for 1k persons, then we need to generate these kind of Anchor, Positive and Negative image for each person and form the training for triplet loss for one run. **What will happen if we have 10K images and no of persons there are 10K**?

![1582822049127](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582822049127.png)

## How to Choose dataset for Triplet Loss?

**Aim here is**: ![1582822610080](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582822610080.png)

Options are for Dataset Selection:

- Choose A(Anchor), P(Positive) and N(Negative) randomly and so above aim is very likely to meet as pictures are being selected randomly but then GD will not be able to learn much. **Why???**
- Recommended to choose dataset such a way that they are hard to train on which means we will try to choose such a way that distance between Anchor and Positive Images are are close to distance between Anchor and Negative Image. **This will force network to minimize the distance between A and N while trying to maximize the distance between A and N**.

![1582822913976](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582822913976.png)

**Conclusion**:

 By pairing the images into triplet pairs of *Anchor-Positive* and *Anchor-Negative*, the network learns the distribution of images from each class with respect to all other classes.

The **loss function** is defined as:

[![alt text](https://github.com/AdrianUng/keras-triplet-loss-mnist/raw/master/images/triplet_loss_function_2.png)](https://github.com/AdrianUng/keras-triplet-loss-mnist/blob/master/images/triplet_loss_function_2.png)

Where *d(A,P)* and *d(A,N)* represent the Euclidean distances between the Anchor and the Positive and Negative pairs. *margin* is a parameter helping the network learning a specific distance between positive and negative samples (using the anchor).

Positive and Negative pairs are important to training the network correctly. Ideally the Anchor-Positive templates should have large(r) distance between them whereas the Anchor-Negative templates should have small(er) distance. These represent **HARD examples**

```
## Computes the triplet loss with semi-hard negative mining.

tf.contrib.losses.metric_learning.triplet_semihard_loss(
    labels,
    embeddings,
    margin=1.0
)

The loss encourages the positive distances (between a pair of embeddings with the same labels) to be smaller than the minimum negative distance among which are at least greater than the positive distance plus the margin constant (called semi-hard negative) in the mini-batch. If no such negative exists, uses the largest negative distance instead. See: https://arxiv.org/abs/1503.03832.

Args:
labels: 1-D tf.int32 Tensor with shape [batch_size] of multiclass integer labels.
embeddings: 2-D float Tensor of embedding vectors. Embeddings should be l2 normalized.
margin: Float, margin term in the loss definition.
```

## Triplet Mining

There are 3 kind of Triplets :

- Easy Triplet : **distance(anchor,positive) + alpha < distance(anchor,negative)**
- Semi-hard Triplet : **distance(anchor,positive) < distance(anchor,negative) < distance(anchor,positive) + alpha**
- Hard Triplet : **distance(anchor,negative) < distance(anchor,positive)**

It can be seen that Easy triplets have loss=0, making them useless for training the Encoder network. So mostly Hard and Semi-hard Triplets are desired for training the Encoder network. Triplet Mining is therefore required to find triplets having maximum impact on the training process.

## Applications

Before we proceed, I would like to mention a few applications of one shot learning in order to motivate you so that you develop more keen interest in understanding this technology.

a. As I have already mentioned about face recognition above, just go to this [*link*](https://www.youtube.com/watch?v=wr4rx0Spihs) wherein the AI Guru Andrew Ng demonstrates how Baidu (the Chinese Search Giant) has developed a face recognition system for the employees in their organization.

b. Read this [*blog*](https://www.microway.com/hpc-tech-tips/one-shot-learning-methods-applied-drug-discovery-deepchem/) to understand how one shot learning is applied to drug discovery where data is very scarce.

c. In this [*paper*](https://arxiv.org/abs/1707.02131), the authors have used one shot learning to build an offline signature verification system which is very useful for Banks and other Government and also private institutions.

# Siamese in conjunction with Face Verification as Binary Classification



## Network

Here output embedding of two images are being compared through logistic activation function to understand whether they are similar or not.

![1582828777151](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582828777151.png)

## Binary Classification

Here we are comparing absolute values of two embedding and have assumed them as 128 dimension and then passing through logistic regression sigmoid function.

![1582828912767](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1582828912767.png)

# Omniglot Dataset and its Siamese Network

For the purpose of this blog, we will use the Omniglot dataset which is a collection of 1623 hand drawn characters from 50 different alphabets. For every character there are just 20 examples, each drawn by a different person. Each image is a gray scale image of resolution 105x105.

Let’s look at some images of characters from different alphabets to get a better feel of the dataset.

![img](https://miro.medium.com/max/1798/1*GoAVSgNTIXeVbM4nA916HQ.jpeg)

Thus we have 1623 different classes(each character can be treated as a separate class) and for each class we have only 20 images. Clearly, if we try to solve this problem using the traditional image classification method then definitely we won’t be able to build a good generalized model. And with such less number of images available for each class, the model will easily overfit.

You can download the dataset by cloning this [*GitHub repository*](https://github.com/brendenlake/omniglot). The folder named “Python” contains two zip files: images_background.zip and images_evaluation.zip. Just unzip these two files.

images_background folder contains characters from 30 alphabets and will be used to train the model, while images_evaluation folder contains characters from the other 20 alphabets which we will use to test our system.

Once you unzip the files, you will see below folders (alphabets) in the images_background folder(used for training purpose):

![img](https://miro.medium.com/max/521/1*RlaIu4FZ6uczRGFhEx50_A.jpeg)



​					Contents of images_background directory

And you will see below folders (alphabets) in the images_evaluation folder (used for testing purpose):

![img](https://miro.medium.com/max/392/1*cASkYmQo2id1MLx6V4pECg.jpeg)



Contents of images_evaluation directory

Notice that we will train the system on one set of characters and then test it on a completely different set of characters which were never used during the training. This is not possible in a traditional classification cycle.

## Loading the dataset

First we need to load the images into tensors and later use these tensors to provide data in batches to the model.

We use below function to load images into tensors:

```
def loadimgs(path,n = 0):
    '''
    path => Path of train directory or test directory
    '''
    X=[]
    y = []
    cat_dict = {}
    lang_dict = {}
    curr_y = n
    
    # we load every alphabet seperately so we can isolate them later
    for alphabet in os.listdir(path):
        print("loading alphabet: " + alphabet)
        lang_dict[alphabet] = [curr_y,None]
        alphabet_path = os.path.join(path,alphabet)
        
        # every letter/category has it's own column in the array, so  load seperately
        for letter in os.listdir(alphabet_path):
            cat_dict[curr_y] = (alphabet, letter)
            category_images=[]
            letter_path = os.path.join(alphabet_path, letter)
            
            # read all the images in the current category
            for filename in os.listdir(letter_path):
                image_path = os.path.join(letter_path, filename)
                image = imread(image_path)
                category_images.append(image)
                y.append(curr_y)
            try:
                X.append(np.stack(category_images))
            # edge case  - last one
            except ValueError as e:
                print(e)
                print("error - category_images:", category_images)
            curr_y += 1
            lang_dict[alphabet][1] = curr_y - 1
    y = np.vstack(y)
    X = np.stack(X)
    return X,y,lang_dict
```

​				                       Code to load images from disk

To call this function as follows, pass the path of the train directory as the parameter as follows:

```
X,y,c = loadimgs(train_folder)
```

The function returns a tuple of 3 variables. I won’t go through each line of the code, but I will provide you some intuition what exactly the function is doing by understanding the values it returns. Given this explanation you should be in a good position to understand the above function, once you go through it.

Let’s understand what is present in ‘X’:

```
X.shape
(964, 20, 105, 105)
```

This means we have **964** characters (or letters or categories) spanning across 30 different alphabets. For each of this character, we have **20** images, and each image is a gray scale image of resolution **105x105.** Hence the shape (964, 20, 105, 105).

Let’s now understand how the labels ‘y’ are populated:

```
y.shape
(19280, 1)
```

Total number of images = 964 * 20 = 19280. All the images for one letter have the same label., i.e. The first 20 images have the label 0, the next 20 have the label 1, and so on, … the last 20 images have the label 963.

Finally the last variable ‘c’ stands for categories and it is a dictionary as follows:

```
c.keys() # 'c' for categoriesdict_keys(['Alphabet_of_the_Magi', 'Anglo-Saxon_Futhorc', 'Arcadian', 'Armenian', 'Asomtavruli_(Georgian)', 'Balinese', 'Bengali', 'Blackfoot_(Canadian_Aboriginal_Syllabics)', 'Braille', 'Burmese_(Myanmar)', 'Cyrillic', 'Early_Aramaic', 'Futurama', 'Grantha', 'Greek', 'Gujarati', 'Hebrew', 'Inuktitut_(Canadian_Aboriginal_Syllabics)', 'Japanese_(hiragana)', 'Japanese_(katakana)', 'Korean', 'Latin', 'Malay_(Jawi_-_Arabic)', 'Mkhedruli_(Georgian)', 'N_Ko', 'Ojibwe_(Canadian_Aboriginal_Syllabics)', 'Sanskrit', 'Syriac_(Estrangelo)', 'Tagalog', 'Tifinagh'])c['Alphabet_of_the_Magi']
[0, 19]c['Anglo-Saxon_Futhorc']
[20, 48]
```

Since there are 30 different alphabets, this dictionary ‘c’ contains 30 items. The key for each item is the name of the alphabet. The value for each item is a list of two numbers: [low, high], where ‘low’ is the label of the first character in that alphabet and ‘high’ is the label of the last character in that alphabet.

Once we load the train and test images, we save the tensors on the disk in a pickle file, so that we can utilize them later directly without having to load the images again.

## Mapping the problem to binary classification task

Let’s understand how can we map this problem into a supervised learning task where our dataset contains pairs of (Xi, Yi) where ‘Xi’ is the input and ‘Yi’ is the output.

Recall that the input to our system will be a pair of images and the output will be a similarity score between 0 and 1.

Xi = Pair of images

Yi = 1 ; if both images contain the same character

Yi = 0; if both images contain different characters

Let’s have a better understanding by visualizing the dataset below:

![img](https://miro.medium.com/max/1950/1*4kfqL7aEvVMU0iALyxvG0g.png)



Sample of 6 data points

Thus we need to create pairs of images along with the target variable, as shown above, to be fed as input to the Siamese Network. Note that even though characters from Sanskrit alphabet are shown above, but in practice we will generate pairs **randomly** from all the alphabets in the training data.

The code to generate these pairs and targets is shown below:

```
def get_batch(batch_size,s="train"):
    """
    Create batch of n pairs, half same class, half different class
    """
    if s == 'train':
        X = Xtrain
        categories = train_classes
    else:
        X = Xval
        categories = val_classes
    n_classes, n_examples, w, h = X.shape
    
    # randomly sample several classes to use in the batch
    categories = rng.choice(n_classes,size=(batch_size,),replace=False)
    
    # initialize 2 empty arrays for the input image batch
    pairs=[np.zeros((batch_size, h, w,1)) for i in range(2)]
    
    # initialize vector for the targets
    targets=np.zeros((batch_size,))
    
    # make one half of it '1's, so 2nd half of batch has same class
    targets[batch_size//2:] = 1
    for i in range(batch_size):
        category = categories[i]
        idx_1 = rng.randint(0, n_examples)
        pairs[0][i,:,:,:] = X[category, idx_1].reshape(w, h, 1)
        idx_2 = rng.randint(0, n_examples)
        
        # pick images of same class for 1st half, different for 2nd
        if i >= batch_size // 2:
            category_2 = category  
        else: 
            # add a random number to the category modulo n classes to ensure 2nd image has a different category
            category_2 = (category + rng.randint(1,n_classes)) % n_classes
        
        pairs[1][i,:,:,:] = X[category_2,idx_2].reshape(w, h,1)
    
    return pairs, targets
```

​					Code to load data in batches

We need to call the above function by passing the batch_size and it will return “batch_size” number of image pairs along with their target variables.

We will use the below generator function to generate data in batches during the training of the network.

```
def generate(batch_size, s="train"):
    """
    a generator for batches, so model.fit_generator can be used.
    """
    while True:
        pairs, targets = get_batch(batch_size,s)
        yield (pairs, targets)
```

## Model Architecture and Training

This code is an implementation of the methodology described in this [*research paper*](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) by Gregory Koch et al*.* Model architecture and hyper-parameters that I have used are all as described in the paper.

Let’s first understand the architecture on a high level before diving into the details. Below I present an intuition of the architecture.

![img](https://miro.medium.com/max/2297/1*dFY5gx-Vze3micJ0AMVp0A.jpeg)

​						A high level architecture

**Intuition**: The term Siamese means twins. The two Convolutional Neural Networks shown above are not different networks but are two copies of the same network, hence the name Siamese Networks. Basically they share the same parameters. The two input images (x1 and x2) are passed through the ConvNet to generate a fixed length feature vector for each (h(x1) and h(x2)). Assuming the neural network model is trained properly, we can make the following hypothesis: If the two input images belong to the same character, then their feature vectors must also be similar, while if the two input images belong to the different characters, then their feature vectors will also be different. Thus the element-wise absolute difference between the two feature vectors must be very different in both the above cases. And hence the similarity score generated by the output sigmoid layer must also be different in these two cases. This is the central idea behind the Siamese Networks.

Given the above intuition let’s look at the picture of the architecture with more finer details taken from the research paper itself:

![img](https://miro.medium.com/max/4802/1*v40QXakPBOmiq4lCKbPu8w.png)



Image Source: <https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf>

The below function is used to create the model architecture:

```
def get_siamese_model(input_shape):
    """
        Model architecture
    """
    
    # Define the tensors for the two input images
    left_input = Input(input_shape)
    right_input = Input(input_shape)
    
    # Convolutional Neural Network
    model = Sequential()
    model.add(Conv2D(64, (10,10), activation='relu', input_shape=input_shape,
                   kernel_initializer=initialize_weights, kernel_regularizer=l2(2e-4)))
    model.add(MaxPooling2D())
    model.add(Conv2D(128, (7,7), activation='relu',
                     kernel_initializer=initialize_weights,
                     bias_initializer=initialize_bias, kernel_regularizer=l2(2e-4)))
    model.add(MaxPooling2D())
    model.add(Conv2D(128, (4,4), activation='relu', kernel_initializer=initialize_weights,
                     bias_initializer=initialize_bias, kernel_regularizer=l2(2e-4)))
    model.add(MaxPooling2D())
    model.add(Conv2D(256, (4,4), activation='relu', kernel_initializer=initialize_weights,
                     bias_initializer=initialize_bias, kernel_regularizer=l2(2e-4)))
    model.add(Flatten())
    model.add(Dense(4096, activation='sigmoid',
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer=initialize_weights,bias_initializer=initialize_bias))
    
    # Generate the encodings (feature vectors) for the two images
    encoded_l = model(left_input)
    encoded_r = model(right_input)
    
    # Add a customized layer to compute the absolute difference between the encodings
    L1_layer = Lambda(lambda tensors:K.abs(tensors[0] - tensors[1]))
    L1_distance = L1_layer([encoded_l, encoded_r])
    
    # Add a dense layer with a sigmoid unit to generate the similarity score
    prediction = Dense(1,activation='sigmoid',bias_initializer=initialize_bias)(L1_distance)
    
    # Connect the inputs with the outputs
    siamese_net = Model(inputs=[left_input,right_input],outputs=prediction)
    
    # return the model
    return siamese_net
```

​							Siamese Model Architecture

Notice that there is no predefined layer in Keras to compute the absolute difference between two tensors. We do this using the Lambda layer in Keras which is used to add customized layers in Keras.

To understand the shape of the tensors passed at different layers, refer the below image generated using the plot_model utility of Keras.

![img](https://miro.medium.com/max/1680/1*RvqlZBlfOT9TcnEYhe_IQw.png)



​									Tensor shapes at every level

The model was compiled using the adam optimizer and binary cross entropy loss function as shown below. Learning rate was kept low as it was found that with high learning rate, the model took a lot of time to converge. However these parameters can well be tuned further to improve the present settings.

```
optimizer = Adam(lr = 0.00006)
model.compile(loss="binary_crossentropy",optimizer=optimizer)
```

The model was trained for 20000 iterations with batch size of 32.

After every 200 iterations, model validation was done using 20-way one shot learning and the accuracy was calculated over 250 trials. This concept is explained in the next section.

## Validating the Model

Now that we have understood how to prepare the data for training, model architecture and training; it’s time we must think about a strategy to validate and test our model.

Note that, for every pair of input images, our model generates a similarity score between 0 and 1. But just looking at the score its difficult to ascertain whether the model is really able to recognize similar characters and distinguish dissimilar ones.

A nice way to judge the model is **N-way one shot learning**. Don’t worry, it’s much easier than what it sounds to be.

An example of 4-way one shot learning:

We create a dataset of 4 pairs of images as follows:

![img](https://miro.medium.com/max/1481/1*2VWymNAhUWX4h9sxmwzwSQ.jpeg)



​					Example of a 4-way one shot learning

Basically the same character is compared to 4 different characters out of which only one of them matches the original character. Let’s say by doing the above 4 comparisons we get 4 similarity scores S1, S2, S3 and S4 as shown. Now if the model is trained properly, we expect that S1 is the maximum of all the 4 similarity scores because the first pair of images is the only one where we have two same characters.

Thus if S1 happens to be the maximum score, we treat this as a correct prediction otherwise we consider this as an incorrect prediction. Repeating this procedure ‘k’ times, we can calculate the percentage of correct predictions as follows:

- percent_correct = (100 * n_correct) / k

- where k => total no. of trials and n_correct => no. of correct predictions out of k trials.

Similarly a 9-way one shot learning will look as follows:

![img](https://miro.medium.com/max/2141/1*89ve6btnbfFTJxQqe51M9g.jpeg)

​					Example of a 9-way one shot learning

A 16-way one shot leaning will be as shown below:

![img](https://miro.medium.com/max/1446/1*zJ0EOMguRIoj8ZDHeOcVLA.jpeg)

​						Example of a 16-way one shot learning

Below is how a 25-way one shot learning would look like:

![img](https://miro.medium.com/max/1446/1*5OgTjZzF-6w5fdsQp1L3GA.jpeg)

​					Example of a 25-way one shot learning

Note that the value of ’N’ in N-way one shot learning need not necessarily be a perfect square. The reason for me taking values 4, 9, 16 and 25 was because it just looks good for presentation when the square is filled completely.

It’s quite obvious that smaller values of ’N’ will lead to more correct predictions and larger values of ’N’ will lead to relatively less correct predictions when repeated multiple times.

Just a reminder again: All the examples shown above are from the Sanskrit Alphabet but in practice we will generate the test image and the support set randomly from all the alphabets of the test/validation dataset images.

The code to generate the test image along with the support set is as follows:

```
def make_oneshot_task(N, s="val", language=None):
    """Create pairs of test image, support set for testing N way one-shot learning. """
    if s == 'train':
        X = Xtrain
        categories = train_classes
    else:
        X = Xval
        categories = val_classes
    n_classes, n_examples, w, h = X.shape
    
    indices = rng.randint(0, n_examples,size=(N,))
    if language is not None: # if language is specified, select characters for that language
        low, high = categories[language]
        if N > high - low:
            raise ValueError("This language ({}) has less than {} letters".format(language, N))
        categories = rng.choice(range(low,high),size=(N,),replace=False)
        else: # if no language specified just pick a bunch of random letters
        categories = rng.choice(range(n_classes),size=(N,),replace=False)            
    
    true_category = categories[0]
    ex1, ex2 = rng.choice(n_examples,replace=False,size=(2,))
    test_image = np.asarray([X[true_category,ex1,:,:]]*N).reshape(N, w, h,1)
    support_set = X[categories,indices,:,:]
    support_set[0,:,:] = X[true_category,ex2]
    support_set = support_set.reshape(N, w, h,1)
    targets = np.zeros((N,))
    targets[0] = 1
    targets, test_image, support_set = shuffle(targets, test_image, support_set)
    pairs = [test_image,support_set]
    return pairs, targets

  
  def test_oneshot(model, N, k, s = "val", verbose = 0):
    """Test average N way oneshot learning accuracy of a siamese neural net over k one-shot tasks"""
    n_correct = 0
    if verbose:
        print("Evaluating model on {} random {} way one-shot learning tasks ... \n".format(k,N))
    for i in range(k):
        inputs, targets = make_oneshot_task(N,s)
        probs = model.predict(inputs)
        if np.argmax(probs) == np.argmax(targets):
            n_correct+=1
    percent_correct = (100.0 * n_correct / k)
    if verbose:
        print("Got an average of {}% {} way one-shot learning accuracy \n".format(percent_correct,N))
    return percent_correct
```



Code to generate a test image along with the support set

## Base Line 1 — Nearest Neighbor Model

It is always a good practice to create simple baseline models and compare their results with complex model you are trying to build.

Our first baseline model is the Nearest Neighbor approach. If you are familiar with K-Nearest Neighbor algorithm, then this is just the same thing.

As discussed above, in an N-way one shot learning, we compare a test image with N different images and select that image which has highest similarity with the test image as the prediction.

This is intuitively similar to the KNN with K=1. Let’s understand in detail how this approach works.

You might have studied how we can compute the L2 distance (also called as the Euclidean distance) between two vectors. If you do not recall, below is how it is done:

![img](https://miro.medium.com/max/1560/1*HHCG84Re2avw6_rDYGFtrg.jpeg)

​						L2 distance between two vectors

Let’s say we compare L2 distance of a vector X with 3 other vectors say A, B and C. Then one way to compute the most similar vector to X is check which vector has the least L2 distance with X. Because distance is inversely proportional to similarity. Thus for example if the L2 distance between X and B is minimum, we say that the similarity between X and B is maximum.

However, in our case we do not have vectors but gray scale images, which can be represented as matrices and not vectors. Then how do we compute L2 distance between matrices?

That’s simple, just flatten the matrices into vectors and then compute the L2 distance between these vectors. For example:

![img](https://miro.medium.com/max/2008/1*ibo02Yz9oTfOHeAG34faTg.jpeg)

​				Computing L2 distance between images

Thus in N-way One Shot learning, we compare the L2 distance of the test image with all the images in the Support Set. Then we check the character for which we got the minimum L2 distance. If this character is the same as the character in the test image, then the prediction is correct, else the prediction is incorrect. For example:

![img](https://miro.medium.com/max/1446/1*Z0yD3o1cVc1a7S3GgK_x6Q.jpeg)

​					N way Nearest Neighbor Approach

Similar to N way one shot learning, we repeat this for multiple trials and compute the average prediction score over all the trials. The code for nearest neighbor approach is below:

```
def nearest_neighbour_correct(pairs,targets):
    """returns 1 if nearest neighbour gets the correct answer for a one-shot task
        given by (pairs, targets)"""
    L2_distances = np.zeros_like(targets)
    for i in range(len(targets)):
        L2_distances[i] = np.sum(np.sqrt(pairs[0][i]**2 - pairs[1][i]**2))
    if np.argmin(L2_distances) == np.argmax(targets):
        return 1
    return 0

  
  def test_nn_accuracy(N_ways,n_trials):
    """Returns accuracy of NN approach """
    print("Evaluating nearest neighbour on {} unique {} way one-shot learning tasks ...".format(n_trials,N_ways))
    n_right = 0
    
    for i in range(n_trials):
        pairs,targets = make_oneshot_task(N_ways,"val")
        correct = nearest_neighbour_correct(pairs,targets)
        n_right += correct
    return 100.0 * n_right / n_trials
```

​					Code to compute Nearest Neighbors

# MNIST Dataset with Triplet Loss

## Preparing the network

First, the network architecture was defined, with an *Input* layer of the same shape as the input image (28x28) and an *Output* layer of size (64), representing the embedding.

```
def create_base_network(image_input_shape, embedding_size):
    """
    Base network to be shared (eq. to feature extraction).
    """
    input_image = Input(shape=image_input_shape)

    x = Flatten()(input_image)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(embedding_size)(x)

    base_network = Model(inputs=input_image, outputs=x)
    plot_model(base_network, to_file='base_network.png', show_shapes=True, show_layer_names=True)
    return base_network
```

[![alt text](https://github.com/AdrianUng/keras-triplet-loss-mnist/raw/master/images/base_network.png)](https://github.com/AdrianUng/keras-triplet-loss-mnist/blob/master/images/base_network.png)

We then define the Model such that the Triplet Loss function receives all the embeddings from each batch, as well as their corresponding labels (used for determining the best triplet-pairs). This is done by defining an input layer for the labels and then concatenating it to the embeddings.

```
  base_network = create_base_network(input_image_shape, embedding_size)

  input_images = Input(shape=input_image_shape, name='input_image') # input layer for images
  input_labels = Input(shape=(1,), name='input_label')    # input layer for labels
  embeddings = base_network([input_images])               # output of network -> embeddings
  labels_plus_embeddings = concatenate([input_labels, embeddings])  # concatenating the labels + embeddings

  # Defining a model with inputs (images, labels) and outputs (labels_plus_embeddings)
  model = Model(inputs=[input_images, input_labels],
                outputs=labels_plus_embeddings)
```

[![alt text](https://github.com/AdrianUng/keras-triplet-loss-mnist/raw/master/images/model.png)](https://github.com/AdrianUng/keras-triplet-loss-mnist/blob/master/images/model.png)

## Training

In order to train, we need to define some 'dummy' embeddings to pass as **ground truth (y)** values

```
opt = Adam(lr=0.0001)  # choose optimiser. RMS is good too!
model.compile(loss=triplet_loss_lol, 
              optimizer=opt)

filepath = "semiH_trip_MNIST_v13_test_ep{epoch:02d}_BS%d.hdf5" % batch_size
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=False, period=25)
callbacks_list = [checkpoint]

# Uses 'dummy' embeddings + dummy gt labels; removed as soon as they enter the loss function...
dummy_gt_train = np.zeros((len(x_train), embedding_size + 1))
dummy_gt_val = np.zeros((len(x_val), embedding_size + 1))

x_train = np.reshape(x_train, (len(x_train), x_train.shape[1], x_train.shape[1], 1))
x_val = np.reshape(x_val, (len(x_val), x_train.shape[1], x_train.shape[1], 1))
H = model.fit(x=[x_train,y_train],
            y=dummy_gt_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=([x_val, y_val], dummy_gt_val),
            callbacks=callbacks_list)
```

## Visualizing separation of classes

We need to:

1. Make an empty network

```
# creating an empty network
testing_embeddings = create_base_network(input_image_shape,
                                         embedding_size=embedding_size)
# embeddings before training...
x_embeddings_before_train = testing_embeddings.predict(np.reshape(x_test, (len(x_test), 28, 28, 1)))
```

2. Loop over the trained model and copy weights

```
# Grabbing the weights from the trained network
for layer_target, layer_source in zip(testing_embeddings.layers, model.layers[2].layers):
  weights = layer_source.get_weights()
  layer_target.set_weights(weights)
  del weights
```

3. Obtain predictions (embeddings) for test set

```
x_embeddings = testing_embeddings.predict(np.reshape(x_test, (len(x_test), 28, 28, 1)))
```

4. Obtain PCA decomposition

```
dict_embeddings = {}
dict_gray = {}
test_class_labels = np.unique(np.array(y_test))

pca = PCA(n_components=no_of_components)
decomposed_embeddings = pca.fit_transform(x_embeddings)
decomposed_gray = pca.fit_transform(x_embeddings_before_train)
```

5. Visualize the separation... 

   ![alt text](https://github.com/AdrianUng/keras-triplet-loss-mnist/raw/master/images/pca_decomposition_before_after.png)](https://github.com/AdrianUng/keras-triplet-loss-mnist/blob/master/images/pca_decomposition_before_after.png

