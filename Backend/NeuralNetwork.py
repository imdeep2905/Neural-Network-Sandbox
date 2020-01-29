#Using tf,tf.keras as backend for NN
import tensorflow as tf
from tensorflow import keras
#other packages
import pandas as pd 
import matplotlib.pyplot as plt 

#choosing optimizer according to user's choice
def get_optimizer(optimizer,lr):
    if optimizer=="SGD":
        return keras.optimizers.SGD(learning_rate=lr)
    elif optimizer=="RMSprop":
        return keras.optimizers.RMSprop(learning_rate=lr)
    elif optimizer=="Adagrad":
        return keras.optimizers.Adagrad(learning_rate=lr)
    elif optimizer=="Adam":
        return keras.optimizers.Adam(learning_rate=lr)
    elif optimizer=="Adamax":
        return keras.optimizers.Adamax(learning_rate=lr)
    elif optimizer=="Nadam":
        return keras.optimizers.Nadam(learning_rate=lr)
    elif optimizer=="Adadelta":
        return keras.optimizers.Adadelta(learning_rate=lr)

#class NN for Neural Network
class NN:
    def __init__(self,layers_n=1,layers=[1],activ_fns=["relu"],loss_fn="sparse_categorical_crossentropy",opti_tech="SGD",lr=0.01,epochs=1,kernal_init="he_normal",metrics=["accuracy"]):
        self.total_layers=layers_n          #Num of layers 
        self.neuron_layers=layers           #Num of neurons in each layer -list
        self.activation_layers=activ_fns    #Activation fn of each layer -list
        self.loss_fn=loss_fn                #Loss function 
        self.optimizer=opti_tech            #Optimizer 
        self.lr=lr                          #learning rate
        self.epochs=epochs                  #epochs
        self.kernal_init=kernal_init        #Weights Initializer
        self.model=keras.models.Sequential()#keras's Functional API for model
        self.metrics=metrics                #Metrics which we want to see
        self.train_history=0                #Reserved for future use
        self.test_history=0                 #           " 
    
    def connect_network(self,normalize=False):
        #This fn connects and compiles model
        #Creating Model
        self.model.add(keras.layers.Flatten(input_shape=[28,28])) #Testing with MNIST    
        for i in range(1,self.total_layers):
            if normalize==True:
                self.model.add(keras.layers.BatchNormalization())
            self.model.add(keras.layers.Dense(self.neuron_layers[i],activation=self.activation_layers[i],kernel_initializer=self.kernal_init))
        #Compiling Model 
        self.model.compile(loss=self.loss_fn,optimizer=get_optimizer(self.optimizer,self.lr),metrics=self.metrics)
        print(self.model.summary()) #for debugging
    
    def fit(self,x_train,y_train,x_val=0,y_val=0):
        if x_val==0:
            self.train_history=self.model.fit(x_train,y_train,epochs=self.epochs)
        else:
            self.train_history=self.model.fit(x_train,y_train,epochs=self.epochs,validation_data=(x_val,y_val))
    
    def evaluate(x_test,y_test):
        self.test_history=self.model.evaluate(x_test,y_test)
    
    def train_visualize(self):
        pd.DataFrame(self.train_history.history).plot(figsize=(16,10)) #will change here for other devices
        plt.grid(True)
        #plt.gca().set_ylim(0,1)
        plt.savefig("train_v")
    
    def test_visualize(self):
        pd.DataFrame(self.test_history.history).plot(figsize=(8,5)) #will change here for other devices
        plt.grid(True)
        #plt.gca().set_ylim(0,1)
        plt.show()
        
    def save_model(self,path):
        pass
    
    def load_model(self,path):
        pass