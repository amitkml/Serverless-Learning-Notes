# Understanding n-grams and bag-of-words

Word n-grams are group of N "or fewer" consecutive words that you can  extract from a sentence. The same concept may also be applied to  characters instead of words

Here's a simple example. Consider the sentence "The cat sat on the mat." It may be decomposed into the follow set of **2-grams**:

```
{
"The", "The cat", "cat", "cat sat", "sat on", "on", "on the", "the", "the mat", "mat"
}
```

It may also be decomposed into the following set of **3-grams**:

```
{
"The", "The cat", "cat", "cat sat", "The cat sat", "sat", "sat on", "on", "cat sat on", "on the", "the", "sat on the", "the mat", "mat", "on the mat"
}
```

Such a set is called a **bag-of-2-grams or bag-of-3-grams**, respectively. The term **bag** here refers to the fact that you're dealing with a set of  tokens rather than a list of sequence: the tokens have no specific order. This family of tokenization methods is called bag-of-words.

# Using Word Embeddings

Another popular and powerful way to associate a vector with a word is the use of dense word vectors, also called word embeddings. Whereas the vectors obtained through one-hot encoding are binary, sparse (mostly made of zeros), and very high-dimensional (same dimensionality as the number of words in the vocabulary), word embeddings are low-dimensional floating-point vectors (that is, dense vectors, as opposed to sparse vectors)

![1583491844033](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583491844033.png)

Unlike the word vectors obtained via one-hot encoding, word  embeddings are learned from data. It's common to see word embedding that  are 256, 512 or 1024 dimensional when dealing with very large  vocabularies. On the other hand, one-hot encoding leads to vectors that  are 20,000 dimensional or greater (capturing a vocabulary of 20000  tokens, in this case). So, word embeddings pack more information into  far fewer dimensions.

 There are two ways to obtain word embeddings:

- Learn word embeddings jointly with the main task you care about  (such as document classification or sentiment prediction). In this  setup, you start with random word vectors and then learn word vectors in  the same way way you learn the weights of a neural network
- Load into your model word embeddings that were pre-computed using a  different machine-learning task than the one you're trying to solve.  These are called pre-trained word embeddings.

## Learning word embeddings with the embedding layer 

- The simplest way to associate a dense vector with a word is to choose the vector at random. The problem with this approach is that the resulting embedding space has no structure; for instance, the words accurate and exact may end up with completely different embeddings, even though they're interchangeable in most sentences. 
- Is there some ideal word-embedding space that would perfectly map human language and could be used for any natural-language-processing task? The word-embedding space for an English-language movie-review sentiment-analysis model may look different from the embedding space for an English-language legal-document-classification model, because the importance of certain semantic relationships varies from task to task.

## Keras Word Embedding

It is thus reasonable to learn a new embedding space with every new task. Fortunately, back-propagation makes that easy, and Keras makes it even easier. It is about learning the weights of a layer: the Embedding 
Layer.

```
from keras.layers import Embedding

#the embedding layer take at least two arguments: the number of possible tokens (here, 1000: 1 + max word index) and the dimensionality of the embeddings (here, 64).
embedding_layer = Embedding(1000, 64)
```

 ![1583517626830](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1583517626830.png)

# Overview of Word2Vec

Word2vec  is a combination of models used to represent distributed  representations of words in a corpus C. Word2Vec (W2V) is an algorithm  that accepts text corpus as an input and outputs a vector representation  for each word, as shown in the diagram below

![Image](https://miro.medium.com/max/724/1*aaMLVYSbAe086KowQQl6zw.png)

## Neural Word Embeddings

The vectors we use to represent words are called *neural word embeddings*,  and representations are strange. One thing describes another, even  though those two things are radically different. As Elvis Costello said:  “Writing about music is like dancing about architecture.” Word2vec  “vectorizes” about words, and by doing so it makes natural language  computer-readable – we can start to perform powerful mathematical  operations on words to detect their similarities.

So a neural word embedding represents a word with numbers. It’s a simple, yet unlikely, translation.

Word2vec is similar to an autoencoder, encoding each word in a  vector, but rather than training against the input words through  reconstruction, as a [restricted Boltzmann machine](https://pathmind.com/wiki/restricted-boltzmann-machine) does, word2vec trains words against other words that neighbor them in the input corpus.

It does so in one of two ways, either using context to predict a  target word (a method known as continuous bag of words, or CBOW), or  using a word to predict a target context, which is called skip-gram. We  use the latter method because it produces more accurate results on large  datasets.

![diagrams](https://pathmind.com/images/wiki/word2vec_diagrams.png)

There are two flavors of this algorithm namely: **CBOW** and **Skip-Gram**. Given a set of sentences (also called corpus) the model loops on the words of each sentence and either tries to use the current word *w* in
order to predict its neighbors (i.e., its context), this approach is called “Skip-Gram”, or it uses each of these contexts to predict the current word *w*, in that case the method is called “Continuous Bag Of Words” (CBOW). To limit the number of words in each context, a parameter called “window size” is used.

![Image](https://miro.medium.com/max/670/1*vZhxrBkCz-yN_rzZBqSKiA.png)

**The  vectors we use to represent words are called neural word embeddings**,  and representations are strange. One thing describes another, even  though those two things are radically different. As Elvis Costello said:  “Writing about music is like dancing about architecture.” Word2vec  “vectorizes” about words, and by doing so it makes natural language  computer-readable — we can start to perform powerful mathematical  operations on words to detect their similarities.

So,  **a neural word embedding represents a word with numbers**. It’s a simple,  yet unlikely, translation. Word2vec is similar to an autoencoder,  encoding each word in a vector, but rather than training against the  input words through reconstruction, as a restricted Boltzmann machine  does, word2vec trains words against other words that neighbor them in  the input corpus.

It  does so in one of two ways, either using context to predict a target  word (a method known as continuous bag of words, or CBOW), or using a  word to predict a target context, which is called skip-gram. We use the  latter method because it produces more accurate results on large  datasets.

![Image](https://miro.medium.com/max/696/1*99ewFdV861rqY_K14bc69w.png)

When the feature vector assigned to a word cannot be used to accurately predict that word’s context, the components of the vector are adjusted. Each word’s context in the corpus is the teacher sending error signals back to adjust the feature vector. The vectors of words judged similar by their context are nudged closer together by adjusting the numbers in the vector. 

**we are going to focus on Skip-Gram model which in contrast to CBOW consider center word as input as depicted in figur**e above and predict context words.

## Model overview

We  understood that we have to feed some strange neural network with some  pairs of words but we can’t just do that using as inputs the actual  characters, we have to find some way to represent these words  mathematically so that the network can process them. One way to do this  is to create a vocabulary of all the words in our text and then to  encode our word as a vector of the same dimensions of our vocabulary.  Each dimension can be thought as a word in our vocabulary. So we will  have a vector with all zeros and a 1 which represents the corresponding  word in the vocabulary. This encoding technique is called one-hot  encoding. Considering our example, if we have a vocabulary made out of  the words “the”, “quick”, “brown”, “fox”, “jumps”, “over”, “the” “lazy”,  “dog”, the word “brown” is represented by this vector: [ 0, 0, 1, 0, 0,  0 ,0 ,0 ,0 ].

![Image](https://miro.medium.com/max/705/1*-XuyVQRaeD7gCKjNZqURHg.png)

The Skip-gram model takes in a corpus of text and creates a hot-vector for each word. A hot vector is a vector representation of a word where the vector is the size of the vocabulary (total unique words). All 
dimensions are set to 0 except the dimension representing the word that is used as an input at that point in time. Here is an example of a hot vector:

![Img](https://miro.medium.com/max/511/1*Gz4zpYpBh9gUqED5rcIXHA.png)

**The above input is given to a neural network with a single hidden layer.**

We’re  going to represent an input word like “ants” as a one-hot vector. This  vector will have 10,000 components (one for every word in our  vocabulary) and we’ll place a “1” in the position corresponding to the  word “ants”, and 0s in all of the other positions. The output of the  network is a single vector (also with 10,000 components) containing, for  every word in our vocabulary, the probability that a randomly selected  nearby word is that vocabulary word.

In word2vec, a distributed representation of a word is used. Take a vector with several hundred dimensions (say 1000). Each word is represented by a distribution of weights across those elements. So 
instead of a one-to-one mapping between an element in the vector and a word, the representation of a word is spread across all the elements in the vector, and each element in the vector contributes to the definition of many words.

If I label the dimensions in a hypothetical word vector (there are no such pre-assigned labels in the algorithm of course), it might look a bit like this:

![img](https://miro.medium.com/max/704/1*VE6e-n7Ot2cy3N6PVnibAw.png)

Such a vector comes to represent in some abstract way the ‘meaning’ of a word. And as we’ll see next, simply by examining a large corpus it’s possible to learn word vectors that are able to capture the 
relationships between words in a surprisingly expressive way. We can also use the vectors as inputs to a neural network. Since our input vectors are one-hot, multiplying an input vector by the weight matrix **W1** amounts to simply selecting a row from **W1**.

![im](https://miro.medium.com/max/539/1*UhWLrIy-0tVkPuCmDz35Wg.png)

From the hidden layer to the output layer, the second weight matrix W2 
can be used to compute a score for each word in the vocabulary, and softmax can be used to obtain the posterior distribution of words.

The skip-gram model is the opposite of the CBOW model. It is **constructed with the focus word as the single input vector, and the target context words are now at the output layer**. The activation function for the hidden layer simply amounts to copying the corresponding row from the weights matrix W1 (linear) as we saw before. At the output layer, we now output C multinomial distributions instead of just one. The training objective is to mimimize the summed prediction error across all context words in the output layer. In our example, the input would be “learning”, and we hope to see (“an”, “efficient”, “method”, “for”, “high”, “quality”, “distributed”, “vector”) at the output layer.

![im](https://miro.medium.com/max/753/1*2QrR-94OCmTsuO6sKCMqYw.png)

For  our example, we’re going to say that we’re learning word vectors with  300 features. So the hidden layer is going to be re**presented by a weight  matrix with 10,000 rows (one for every word in our vocabulary) and 300  columns (one for every hidden neuron). 300 features is what Google used  in their published model trained on the Google news dataset (you can  download it from here). The number of features is a “hyper parameter”  that you would** just have to tune to your application (that is, try  different values and see what yields the best results).

If you look at the rows of this weight matrix, these are what will be our word vectors!

![im](https://miro.medium.com/max/515/1*QTap8L-wBXleN6QPoQ1RKw.png)

**So the end goal of all of this is really just to learn this hidden layer weight matrix — the output layer we’ll just toss when we’re done! The 1x 300 word vector for “ants” then gets fed to the output layer. The** 
**output layer is a softmax regression classifier. Specifically, each output neuron has a weight vector which it multiplies against the word vector from the hidden layer, then it applies the function exp(x) to the result. Finally, in order to get the outputs to sum up to 1, we divide this result by the sum of the results from all 10,000 output nodes**. Here’s an illustration of calculating the output of the output neuron for the word “car”.

![imk](https://miro.medium.com/max/753/1*shL52PGejlFANL0jy9ud_w.png)

*If two different words have very similar “contexts” (that is, what words are likely to appear around them), then our model needs to output very similar results for these two words. And one way for the network to output similar context predictions for these two words is if the word vectors are similar. So, if two words have similar contexts, 
then our network is motivated to learn similar word vectors for these two words! Ta da!*

Each  dimension of the input passes through each node of the hidden layer.  The dimension is multiplied by the weight leading it to the hidden  layer. Because the input is a hot vector, only one of the input nodes  will have a non-zero value (namely the value of 1). This means that for a  word only the weights associated with the input node with value 1 will  be activated, as shown in the image above.

As  the input in this case is a hot vector, only one of the input nodes  will have a non-zero value. This means that only the weights connected  to that input node will be activated in the hidden nodes. An example of  the weights that will be considered is depicted below for the second  word in the vocabulary:

*The  vector representation of the second word in the vocabulary (shown in  the neural network above) will look as follows, once activated in the  hidden layer:*

![k](https://miro.medium.com/max/658/1*EfxciQT_WOoyxLvak-I_RA.png)

*Those weights start off as random values. The network is then trained in order to adjust the weights to represent the input words. This is where the output layer becomes important. Now that we are in the hidden layer with a vector representation of the word we need a way to determine how well we have predicted that a word will fit in a 
particular context. The context of the word is a set of words within a window around it, as shown below:*

![k](https://miro.medium.com/max/554/1*uqBRSVGzYBZ6xDhBy6FlZw.png)

*The above image shows that the context for Friday includes words like “cat” and “is”. The aim of the neural network is to predict that “Friday” falls within this context.*

*We activate the output layer by multiplying the vector that we passed through the hidden layer (which was the input hot vector \*weights entering hidden node) with a vector representation of the context word (which is the hot vector for the context word \* weights entering the output node). The state of the output layer for the first 
context word can be visualised below:*

![kk](https://miro.medium.com/max/753/1*C1lTrQKeZT2NEX2LdJnpEQ.png)

- The above multiplication is done for each word to context word pair. We then calculate the probability that a word belongs with a set of context words using the values resulting from the hidden and output layers. Lastly, we apply stochastic gradient descent to change the values of the weights in order to get a more desirable value for the probability calculated.



### Summary

**In a nutshell, Skip-gram model reverses the use of target and context words**. In this case, the target word is fed at the input, the hidden layer remains the same, and the output layer of the neural network is 
replicated multiple times to accommodate the chosen number of context words. Taking the example of “cat” and “tree” as context words and “climbed” as the target word, the input vector in the skim-gram model 
would be [0 0 0 1 0 0 0 0 ]t, while the two output layers would have [0 10 0 0 0 0 0] t and [0 0 0 0 0 0 0 1 ]t as target vectors respectively.

# Word2Vec Tutorial - The Skip-Gram Model

This tutorial covers the skip gram neural network architecture for  Word2Vec. My intention with this tutorial was to skip over the usual  introductory and abstract insights about Word2Vec, and get into more of  the details. Specifically here I’m diving into the skip gram neural  network model.

## The Model

The skip-gram neural network model is actually surprisingly simple in  its most basic form; I think it’s all of the little tweaks and  enhancements that start to clutter the explanation.

Let’s start with a high-level insight about where we’re going.  Word2Vec uses a trick you may have seen elsewhere in machine learning.  We’re going to train a simple neural network with a single hidden layer  to perform a certain task, but then we’re not actually going to use that  neural network for the task we trained it on! Instead, the goal is  actually just to learn the weights of the hidden layer–we’ll see that  these weights are actually the “word vectors” that we’re trying to  learn.

 Another place you may have seen this trick is in unsupervised feature  learning, where you train an auto-encoder to compress an input vector in  the hidden layer, and decompress it back to the original in the output  layer. After training it, you strip off the output layer (the  decompression step) and just use the hidden layer--it's a trick for  learning good image features without having labeled training data. 

## The Fake Task

So now we need to talk about this “fake” task that we’re going to  build the neural network to perform, and then we’ll come back later to  how this indirectly gives us those word vectors that we are really  after.

We’re going to train the neural network to do the following. Given a  specific word in the middle of a sentence (the input word), look at the  words nearby and pick one at random. The network is going to tell us the  probability for every word in our vocabulary of being the “nearby word”  that we chose.

 When I say "nearby", there is actually a "window  size" parameter to the algorithm. A typical window size might be 5,  meaning 5 words behind and 5 words ahead (10 in total).

The output probabilities are going to relate to how likely it is find  each vocabulary word nearby our input word. For example, if you gave  the trained network the input word “Soviet”, the output probabilities  are going to be much higher for words like “Union” and “Russia” than for  unrelated words like “watermelon” and “kangaroo”.

We’ll train the neural network to do this by feeding it word pairs  found in our training documents. The below example shows some of the  training samples (word pairs) we would take from the sentence “The quick  brown fox jumps over the lazy dog.” I’ve used a small window size of 2  just for the example. The word highlighted in blue is the input word.

[![Training Data](http://mccormickml.com/assets/word2vec/training_data.png)](http://mccormickml.com/assets/word2vec/training_data.png)

The network is going to learn the statistics from the number of times  each pairing shows up. So, for example, the network is probably going  to get many more training samples of (“Soviet”, “Union”) than it is of  (“Soviet”, “Sasquatch”). When the training is finished, if you give it  the word “Soviet” as input, then it will output a much higher  probability for “Union” or “Russia” than it will for “Sasquatch”.

## Model Details

So how is this all represented?

First of all, you know you can’t feed a word just as a text string to  a neural network, so we need a way to represent the words to the  network. To do this, we first build a vocabulary of words from our  training documents–let’s say we have a vocabulary of 10,000 unique  words.

We’re going to represent an input word like “ants” as a one-hot  vector. This vector will have 10,000 components (one for every word in  our vocabulary) and we’ll place a “1” in the position corresponding to  the word “ants”, and 0s in all of the other positions.

The output of the network is a single vector (also with 10,000  components) containing, for every word in our vocabulary, the  probability that a randomly selected nearby word is that vocabulary  word.

Here’s the architecture of our neural network.

[![Skip-gram Neural Network Architecture](http://mccormickml.com/assets/word2vec/skip_gram_net_arch.png)](http://mccormickml.com/assets/word2vec/skip_gram_net_arch.png)

There is no activation function on the hidden layer neurons, but the output neurons use softmax. We’ll come back to this later.

When *training* this network on word pairs, the input is a one-hot vector representing the input word and the training output *is also a one-hot vector*  representing the output word. But when you evaluate the trained network  on an input word, the output vector will actually be a probability  distribution (i.e., a bunch of floating point values, *not* a one-hot vector).

## The Hidden Layer

For our example, we’re going to say that we’re learning word vectors  with 300 features. So the hidden layer is going to be represented by a  weight matrix with 10,000 rows (one for every word in our vocabulary)  and 300 columns (one for every hidden neuron).

 300 features is what Google used in their published model trained on the Google news dataset (you can download it from [here](https://code.google.com/archive/p/word2vec/)).  The number of features is a "hyper parameter" that you would just have  to tune to your application (that is, try different values and see what  yields the best results). 

If you look at the *rows* of this weight matrix, these are actually what will be our word vectors!

[![Hidden Layer Weight Matrix](http://mccormickml.com/assets/word2vec/word2vec_weight_matrix_lookup_table.png)](http://mccormickml.com/assets/word2vec/word2vec_weight_matrix_lookup_table.png)

So the end goal of all of this is really just to learn this hidden  layer weight matrix – the output layer we’ll just toss when we’re done!

Let’s get back, though, to working through the definition of this model that we’re going to train.

Now, you might be asking yourself–“That one-hot vector is almost all  zeros… what’s the effect of that?” If you multiply a 1 x 10,000 one-hot  vector by a 10,000 x 300 matrix, it will effectively just *select* the matrix row corresponding to the “1”. Here’s a small example to give you a visual.

[![Effect of matrix multiplication with a one-hot vector](http://mccormickml.com/assets/word2vec/matrix_mult_w_one_hot.png)](http://mccormickml.com/assets/word2vec/matrix_mult_w_one_hot.png)

This means that the hidden layer of this model is really just  operating as a lookup table. The output of the hidden layer is just the  “word vector” for the input word.

## The Output Layer

The `1 x 300`  word vector for “ants” then gets fed to the output layer. The output  layer is a softmax regression classifier. There’s an in-depth tutorial  on Softmax Regression [here](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/),  but the gist of it is that each output neuron (one per word in our  vocabulary!) will produce an output between 0 and 1, and the sum of all  these output values will add up to 1.

Specifically, each output neuron has a weight vector which it  multiplies against the word vector from the hidden layer, then it  applies the function `exp(x)` to the result. Finally, in order to get the outputs to sum up to 1, we divide this result by the sum of the results from *all* 10,000 output nodes.

Here’s an illustration of calculating the output of the output neuron for the word “car”.

[![Behavior of the output neuron](http://mccormickml.com/assets/word2vec/output_weights_function.png)](http://mccormickml.com/assets/word2vec/output_weights_function.png)

 Note that neural network does not know anything about the offset of the output word relative to the input word. It *does not* learn a different set of probabilities for the word before the input versus the word after.   To understand the implication, let's say that in our training corpus, *every single occurrence*  of the word 'York' is preceded by the word 'New'. That is, at least  according to the training data, there is a 100% probability that 'New'  will be in the vicinity of 'York'. However, if we take the 10 words in  the vicinity of 'York' and randomly pick one of them, the probability of  it being 'New' *is not* 100%; you may have picked one of the other words in the vicinity. 

## Intuition

If two different words have very similar “contexts” (that is, what  words are likely to appear around them), then our model needs to output  very similar results for these two words. And one way for the network to  output similar context predictions for these two words is if *the word vectors are similar*.  So, if two words have similar contexts, then our network is motivated  to learn similar word vectors for these two words! Ta da!

And what does it mean for two words to have similar contexts? I think  you could expect that synonyms like “intelligent” and “smart” would  have very similar contexts. Or that words that are related, like  “engine” and “transmission”, would probably have similar contexts as  well.

# GloVe

- The Global vectors for word representation (GloVe) embeddings an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word
  co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.
- GloVe differs from Word2Vec in that Word2Vec is a predictive model while GloVe is a count-based model. The first step is to construct a large matrix of (word, context) pairs that co-occur in the training corpus. 
  - Rows correspond to words and columns correspond to contexts, usually a sequence of one or more words. Each element of the matrix represents how often the word co-occurs in the context.

## Creating your own embedding using gensim

Lets create an embedding using a small text corpus, called text8. The text8 consists of the first 109 bytes of English Wikipedia.

To download the text8 corpus, create a Word2Vec model from it, and save it for later use..

**gensim is an open source Python library designed to extract semantic meaning from text documents. One of its features is an excellent implementation of the Word2Vec algorithm, with an easy to use API that allows you to train and query your own Word2Vec model.**



```
import gensim.downloader as api
from gensim.models import Word2Vec
dataset = api.load("text8")
model = Word2Vec(dataset)
model.save("data/text8-word2vec.bin")
```

- This will train a Word2Vec model on the text8 dataset and save it as a binary file.
- will just use the defaults. In this case it trains a CBOW model (sg=0) with window size 5 (window=5) and
  will produce 100 dimensional embeddings (size=100). The full set of parameters are described in the Word2Vec documentation.

Refer to [notebook](https://colab.research.google.com/drive/1alqfgALMk17lCLn3MYAY_4-tbqWliUTo#scrollTo=7pvnIi83RfKU) for details and how we can bring nearest word..![1587297142575](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1587297142575.png)

# Using word embeddings for spam detection

- Various robust embeddings already been generated from large corpora
- Text is treated as a sequence of tokens.
- The embedding provides a dense fixed dimension vector for each token.
- Each token is **replaced with its vector**, and this converts the sequence of text into a matrix of examples, each of which has a **fixed number of features** corresponding to the d**dimensionality of the embedding**.
- Our example is a spam detector that will classify Short Message Service (SMS) or text messages as either "ham" or "spam."

## Objective

- Will see how the program learns an embedding from scratch that is customized to the spam detection task.

- Will see how to use an external third-party embedding which is similar to transfer learning in computer vision
- how to combine the two approaches, starting with a third party embedding and letting the network
  use that as a starting point for its custom embedding, a process similar to fine tuning in computer vision

# IMDB movie-review sentiment-prediction task

First, you'll quickly prepare the data. You'll restrict the movie  reviews to the top 10,000 most common words and cut off the reviews  after only 20 words. The network will learn 8-dimensional embeddings for  each of the 10000 words, turn the input integer sequences (2D integer  tensor) into embedding sequences (3D float tensor), flatten the tensor  to 2D, and train a single Dense layer on top for classification.

 

**Loading the IMDB data for use with an Embedding layer**

```
from keras.datasets import imdb
from keras import preprocessing

# number of words to consider as features
max_features = 10000

# cuts off the text after 20 number of words
maxlen = 20

# loads the data as lists of integer
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequences(x_text, maxlen=maxlen)
```

 


**Using an Embedding layer and classifier on the IMDB data**

 

```
from keras.models import Sequential
from keras.layers import Flatten, Dense

model = Sequential()
# specifies the max input length to the Embedding layer so you can later flatten the embedded inputs. After the Embedding layer, the activations have shape (samples, maxlen, 8)
model.add(Embedding(10000, 8, input_length=maxlen))

# flattens the 3D tensor of embeddings into a 2D tensor of shape (Samples, maxlen*8)
model.add(Flatten())

# adds the classifier on top
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metric=['acc'])
model.summary()

history = model.fit(x_train, y_train
epochs=10,
batch_size=32,
validation_split=0.2)
```

 You get to a validation accuracy of ~76%, which is pretty good  considering that you're only looking at the first 20 words in every  review.

**Downloading the IMDB data as raw text**


First, head to http://mng.nz/0tIo and download the raw IMDB  dataset. Uncompress it. Now, let's collect the individual training  reviews into a list of strings, one string per review. You'll also  collect the review labels (positive/negative) into a labels list.

 

**Processing the labels of the raw IMDB data**

```
import os

imdb_dir = '/aclImdb'
train_dir = os.path.join(imdb_dir, 'train')

labels = []
texts = []

for label_type in ['neg', 'pos']:
dir_name = os.path.join(train_dir, label_type)
for fname in os.listdir(dir_name):
if fname[-4] == '.txt'
f = open(os.path.join(dir_name, fname))
texts.append(f.read())
f.close()
if label_type == 'neg':
labels.append(0)
else:
labels.append(1)
```

 

 

**Tokenizing the data**

```
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

maxlen = 100 # cuts off reviews after 100 words
training_samples = 200 # train only on 200 samples
validation_samples = 10000
max_words = 10000

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=maxlen)

labels = np.asarray(labels)
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# Splits the data into a training set and a validation set, but first shuffles the data because you're starting with data in which samples are ordered, all negatives first, then all positives
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

x_train = data[:training_samples]
y_train = data[:training_samples]

x_val = data[training_samples: training_samples + valiation_samples]
y_val = labels[training_samples: training_samples + valiation_samples]
```

 

 

**Download the Glove word embeddings**

```
glove_dir = '/glove.6B'

embeddings_index = {}
f = open(os.path.join(glove_dir, 'glove.6B.100d.txt'))
for line in f:
values = line.split()
word = values[0]
coefs = np.assarray(values[1:], dtype='float32')
embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' %len(embeddings_index))

embedding_dim = 100

embedding_matrix = np.zeros((max_words, embedding_dim))

for word, i in word_index.items():
if i < max_words:
embedding_vector = embedding_index.get(word)
if embedding_vector is not None:
embedding_matrix[i] = embedding_vector
# words not found in the embedding index will all be zeros

# model definition
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# load Glove model
model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False

model.compile(optimizer='rmsprop',
loss='binary_crossentropy',
metrics=['acc'])
history = model.fit(x_train, y_train, 
epochs = 10,
batch_size=32,
validation_data=(x_val, y_val))
model.save_weights('pre_trained_glove_model.h5')
```

# Contextual word embeddings with ELMo

## Issue with Static Word Embedding

Take a look at these sentences below as an example.

```
The plane took off at exactly nine o’clock.
The plane surface is a must for any cricket pitch.
Plane geometry is fun to study.
```

**How meaning of the word *plane* changes based on context. This made it essential to find a way that captures the word meaning in changing contexts, as well as retain the contextual information.**

Suppose we have a couple of sentences:

1. I ***read*** the book yesterday.
2. Can you ***read*** the letter now?

Take a moment to ponder the difference between these two. The verb “read” in the first sentence is in the past tense. And the same verb transforms into present tense in the second sentence. This is a case of **Polysemy** wherein a word could have multiple meanings or senses.

## ELMo: Deep contextualized word representation

Instead of using a fixed embedding for each word, like models like GloVe do , ELMo looks at the entire sentence before assigning each word in it its embedding.

![img](https://miro.medium.com/max/1400/1*ko2Ut74J_oMxF4jSo1VnCg.png)

## How does it do it? Using Long Short-Term Memory (LSTM)

- Uses a bi-directional LSTM trained on a specific task, to be able to create contextual word embedding.

  ![img](https://miro.medium.com/max/1000/1*uYRapcRjy3rrgmpChF8jcA.gif)

- ELMo stands for Embeddings from Language Models, and hence it also has the ability to predict the next word in a sentence, which is, essentially, what Language Models do. When trained on a large dataset, the model also starts to pick up on language patterns.
- Such models allow us to determine that, we will see the phrase like “*I am going to write with a”*, the word *pencil* seems to be a more reasonable next word than “*frog”*.

## Deep Dive of ELMo

- Uses bi-directional LSTM in training, so that its language model not only understands the next word, but also the previous word in the sentence.
- Contains a 2-layer bidirectional LSTM backbone.
- Residual connections are used to allow gradients to flow through a network directly, without passing through the non-linear activation functions. The high-level intuition is that residual connections help deep models train more successfully.
- Unlike other word embeddings, it generates word vectors on run time.

![im](https://miro.medium.com/max/1400/1*HfOihLdIgotgOuwAuQfhdQ.png)



**Have a look at the notebook** <https://colab.research.google.com/drive/1IbRfwa_55-6WL64GIZcLI1xV4T2jEAuw#scrollTo=9hH7pGxJQR_l>

- The architecture above uses a character-level convolutional neural network (CNN) to represent words of a text string into raw word vectors

- These raw word vectors act as inputs to the first layer of biLM

- The forward pass contains information about a certain word and the context (other words) before that word

- The backward pass contains information about the word and the context after it

- This pair of information, from the forward and backward pass, forms the intermediate word vectors

- These intermediate word vectors are fed into the next layer of biLM

- The final representation (ELMo) is the weighted sum of the raw word vectors and the 2 intermediate word vectors.

As the input to the biLM is computed from characters rather than words, it captures the inner structure of the word. For example, the biLM will be able to figure out that terms like *beauty* and *beautiful* are related at some level without even looking at the context they often appear in. ![im](https://cdn.analyticsvidhya.com/wp-content/uploads/2019/03/output_YyJc8E.gif)

## **What else we can do with ELMo?**

We [saw](<https://colab.research.google.com/drive/1IbRfwa_55-6WL64GIZcLI1xV4T2jEAuw#scrollTo=IxNaRcTC2qJG>)  how effective ELMo can be for text  classification. If coupled with a more sophisticated model, it would  surely give an even better performance. The application of ELMo is not  limited just to the task of text classification. You can use it whenever  you have to vectorize text data.

Below are a few more NLP tasks where we can utilize ELMo:

- Machine Translation
- Language Modeling
- Text Summarization
- Named Entity Recognition
- Question-Answering Systems



# References

- https://medium.com/@zafaralibagh6/a-simple-word2vec-tutorial-61e64e38a6a1
- http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
- https://www.tensorflow.org/tutorials/text/word_embeddings
- <https://medium.com/saarthi-ai/elmo-for-contextual-word-embedding-for-text-classification-24c9693b0045>
- <https://sujayskumar.com/2018/10/02/elmo-embeddings-in-keras/>
- <https://towardsdatascience.com/elmo-embeddings-in-keras-with-tensorflow-hub-7eb6f0145440>
- <https://www.analyticsvidhya.com/blog/2019/03/learn-to-use-elmo-to-extract-features-from-text/>