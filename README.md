# Neural-Network-Sandbox
**Current Version: V1.0**

# Contents

1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [How to run](#How-to-run) 
4. [Features](#Features)
   * [Readme](#Readme) 
   * [Help](#Help)
   * [Optimization Technique](#Optimization-Technique)
   * [Loss Function](#Loss-Function)
   * [Add Layer](#Add-Layer)
   * [Remove Layer](#Remove-Layer)
   * [Weights Intialization](#Weights-Intialization)
   * [Learning rate](#Learning-rate)
   * [Epochs](#Epochs)
   * [Start](#Start)
   * [Reset](#Reset)
   * [Batch Normalization](#Batch-Normalization)
   * [Use GPU](#Use-GPU)
   * [Shuffle Data](#Shuffle-Data)
   * [Training Stats](#Training-Stats)
   * [Layer Control](#Layer-Control)
   * [Network Drawings](#Network-Drawing)
   * [Save Current Model](#Save-Current-Model)
   * [Visualize Training](#Visualize-Training)
   * [Browse training Data](#Browse-Training-Data)
   * [Load Exsisting Model](#Load-Exsisting-Model)
   * [Testing Stats](#Testing-Stats)
   * [Browse testining Data](#Browse-Testing-Data)
   * [Report a Bug](#Report-a-Bug)
   * [Label at Start](#Label-at-Start)
   * [Smart PreProcess Data](#Label-at-Start)
   * [Validation Split](#Validation-Split)
5. [Known Issues](#Known-Issues)
6. [Credits](#Credits)

# Introduction
Neural Network Sandbox is a GUI based application which makes making and training basic feed forward neural networks easy.

Before starting: **Assume default value of parameters which are not listed here.(For Ex: batch_size=32)**

# Installation

Currently we are working on one **executable file** and **pip package** for this application.

**Updates about package and executable will be posted here**

# How to run
While there is no executable available you can try Neural Network Sandbox with source code.

  1. Clone this repo.
  2. Fulfill ```requirements.txt``` (```pip install requirements.txt```).
  3. Run with command ```python main.py```.

# Features

![Main Screen](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/mainscreen.PNG)

Above is the screenshot of Application.We will see each section one by one

### Readme
This button will simply redirect you to ```README.md``` (Which contains documentation)of Github repo.

### Help
This button will simply redirect you to ```HELP.md```(Which is useful for new users) of Github repo.
You can read ```HELP.md``` if you are beginner in Neural networks.All the buzzwords are explained there.

### Optimization Technique

This option gives user number of choices for optimizer for their network.Click on ```SGD``` to see options and select one of them.

Options are:

  * SGD
  * RMSprop
  * Adagrad
  * Adam
  * Adamax
  * Nadam
  * Adadelta 

### Loss Function

This option gives user number of choices for loss function for their network.Click on ```sparse_categorical_crossentropy``` to see options and select one of them.

Options are:

  * sparse_categorical_crossentropy
  * binary_crossentropy 
  * categorical_crossentropy 
  * mean_squared_error 
  * mean_absolute_error 
  * huber_loss
  * cosine_proximity
  * poisson

### Add Layer

Clicking on this button will add new Layer in Layer Control.

Before Adding Layer:
![lc before](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/before_add_layer.PNG)

After Adding Layer:
![lc after](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/after_add_layer.PNG)

### Remove Layer

Clicking on this button will add remove Layer from Layer Control.Note that minimum of 2 Layer is required so it can only remove layer  when number of layers are >=3.

Before Removing Layer:
![lc before](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/after_add_layer.PNG)

After Removing Layer:
![lc after](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/before_add_layer.PNG)

### Weights Intialization

This option gives user number of choices for weights intialization (kernal intialization) for their network.Click on ```he_normal``` to see options and select one of them.

Note that picked intializer will be used for the whole network.

Options are:

  * he_normal
  * he_uniform
  * lecun_normal
  * lecun_uniform
  * glorot_normal
  * glorot_uniform
  * RandomNormal
  * RandomUniform
  * Orthogonal

### Learning rate

Input your choice of learning rate here.Generally it is between ```0``` and```1```.Here,default value is ```0.01```.
### Epochs

Buttons ```+``` and  ```-``` can be used for increasing or decreasing number of epochs.Note that minimum value is 1 however there is no limit on maximum value.

### Start

![start](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/play.png)

Clicking this button will first check for errors (Error will be reported as popup if any) in selected options and than it will start training.

### Reset

![reset](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/reset.png)

Clicking this button will reset app to it's initial state(i.e. mainscreen shown in Features).

### Batch Normalization

Checking this will add **BatchNormalize** layer after each layer in your network except ouput layer.

### Use GPU

If you check this app will try it's best to utilize GPU for training.

Tensorflow Version | Effects of this option
------------ | -------------
Tensorflow <2.1.0 (CPU) | Checking or Unchecking will not make any difference
Tensorflow-gpu <=2.0.0 | Checking will use GPU (won't work if  CUDA is not configured) unchecking will use CPU.
Tensorflow == 2.1.0 (Which supports both CPU and GPU)  | Checking will use GPU (will work on CPU if CUDA is not configured) unchecking will use CPU.

### Shuffle Data

Checking this will shuffle training data before training.

### Training Stats

After training if finished all stats (like accuracy,loss etc..) will be shown here.

Note that it only shows following metrics:

  * Loss 
  * accuracy
  * mse
  * val_loss (if validation split >0)
  * val_accuracy (if validation split >0)
  * val_mse (if validation split >0)

### Layer Control

![lc before](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/after_add_layer.PNG)

You can give number of neurons and activation for each layer in layer control.Minimum number of neurons is ```1``` however there is no limit on maximum value.

Click on ```sigmoid``` to select other options for activation.

Options are:

  * sigmoid
  * relu
  * elu
  * selu
  * tanh
  * softmax
  * linear       

Note that You can't select activation for first layer.

### Network Drawing

Network Drawing will be shown in middle of application.Default Drawing is ``` Input -> Ouput ``` as shown in main screen.Drawing will be updated after training (given training is successful).

Note that it is not practical to include all neurons in drawing so for performance reasons number of neurons in drawing are limited to 13.

### Save Current Model

After Training you can save your model by clicking this.It will give dynamic name to your file and save it with ```.h5``` extension.Popup is shown upon successful saving.

### Visualize Training

After training you can see graphical history of training by clicking this.It will open new window containing image.

![vis_train](https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/Frontend/imgs/vis_train.PNG)

### Browse Training Data 

You can select any training file with ```.csv``` extension.Before selecting note that app only supports single label in training data.

### Load Exsisting Model

You can load any file (Even model which is trained outside this application) with  ```.h5``` extension.Layer control and Network Drawing will be set according to loaded model.

Note that as app only supports simple feed forward networks, loading file of other networks may not give appropiate output.

### Testing Stats

After training and testing (if testing data is selected) you can click this button to view testing statistics.Popup will be shown with this statistics.

This Contains:
  * loss
  * accuracy
  * mse
  
### Browse Testing Data 

You can select any testing file with ```.csv``` extension.Before selecting note that app only supports single label in testing data.

### Report a Bug

Clicking this button will simply redirect you to issues page of github repo.You can raise new issue and we'll try our best to fix it.

### Label at Start

Checking it tells app that label is in first column of training/testing file.
UnChecking it tells app that label is in last column of training/testing file.

### Smart Preprocess Data

**This is an experimental feature**.

Checking this will preprocess selected training/testing before starting.It does mainly following:

  * Remove Unnecessary columns(Based on number of unique values).
  * Fill Missing data with median.
  * Replace text data with number representation.

### Validation Split

Slide it to select percentage of validation data from training data.```0%``` means no validation.

# Known Issues
Issue | Solved
------------ | -------------
Sometimes Visualize training doesn't work | No

# Credits

Contributors:compuer:: 
   * [Deep Raval](https://github.com/imdeep2905)

Without these excellant libraries :heart: this would not have been possible.
   * tensorflow
   * matplotlib
   * pandas
   * pydot
   * pygame
   * kivy
   * kivy-deps.angle
   * kivy-deps.glew
   * kivy-deps.gstreamer
   * Kivy-Garden
   * kivy.deps.sdl2
   * kiwisolver
   * pydotplus
   * graphviz
   * pillow
   * scikit-learn
   * scipy
   * setuptools
   * docutils 
   * pygments 
   * pypiwin32
   * pip
