# Neural-Network-Sandbox Help Section

# Contents

1. [I'm absoulte beginner](#I-m-absoulte-beginner)
2. [Buzzwords](#Buzzwords)
   * [Optimization Technique](#Optimization-Technique)
   * [Loss Function](#Loss-Function)
   * [Learning rate](#Learning-rate)
   * [Weights Intialization](#Weights-Intialization)
   * [Epochs](#Epochs)
   * [Validation](#Validation)
3. [Help me select parameters](#Help-me-select-parameters)
4. [Demo Tutorial](#Demo-Tutorial)

# I'm absoulte beginner
Don't Worry Deep learning isn't that Hard !!!
Follow these **Resources** in order and you'll be good to go !
  * [Introduction to Neural Network](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
  * [Make your Own Neural network](https://kupdf.net/download/make-your-own-neural-network-tariq-rashid-chb-books_598f6fe5dc0d60e932300d19_pdf)
  * [Your First Network in Tensorflow](https://www.tensorflow.org/tutorials/keras/classification)
  

# Buzzwords

Don't be sacred by this hard words.Let's see them one by one:

### Optimization Technique

Optimization Technique dictates Technique through which loss function is optimized.In informal words basically how your network get tweaked.See [Pros and Cons of diffrent Techniques](#Choose-Optimization-Technique).

### Loss Function

Loss function basically is one function which measures error in whole network.Goal of Optimization Technique is to minimize value of this Loss Function.See [See Usage of different Losss Functions](#Choose-Loss-Function).

### Learning rate

This is the number which controls the speed of learning.For ex. ```0``` means no learning and ```1``` means Full paced learning.See [See Choosing right learning rate](#Choose-Learning-rate).

### Weights Intialization

As you know before training weights of network must be intialized.And Weights Intialization dictates Technique through which weights get intialized.See [Pros and Cons of diffrent Techniques](#Choose-Weights-Intialization).

### Epochs

Epoch is number which dictates how many times training should be done on training data.
For Ex:
3 : Do training on training data 3 times.

See [Pros and Cons of diffrent Epochs](#Choose-Epochs)

### Validation

Validation Data is basically testing data derived from training/testing data.It can be used to see if model is overfitting/underfitting.

# Help me select parameters

### Choose Optimization Technique

| Optimizer | Convergence Speed |Convergence Quality|
| --- | --- | --- |
| SGD | # |###|
| Adagrad | ### |#|
| RMSprop | ### |## or ###|
| Adam | ### |## or ###|
| Nadam | ### |## or ###|
| AdaMax | ### |## or ###|

You should always choose optimizer according do available data and time.

### Choose Loss function


### Choose Learning rate

![choose_loss](https://github.com/imdeep2905/Neural-Network-Sandbox/tree/master/Frontend/imgs/choose_loss.png)
Actually it's little hactic to select just right learning rate for your project.Feel free to experiment with different learning rates and see which gives best accuracy/mse.

Our Advice is to start with smaller learning rate and gradually increase it untill you find best one.

### Choose Weights Intialization

### Choose Epochs
Start with low number of epochs and increase it untill you find best one.
# Demo Tutorial

### Will be Updated Soon !
