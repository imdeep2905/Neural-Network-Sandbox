#Using tf,tf.keras as backend for NN
import tensorflow as tf
from tensorflow import keras

#class NN for Neural Network
class NN:
    def __init__(self,layers_n=1,layers=[1],activ_fns,loss_fn="sparse_categorical_crossentropy",opti_tech="SGD",lr=0.01,epochs=1,kernal_init="he_normal"):
        self.total_layers=layers_n          #Num of layers 
        self.neuron_layers=layers           #Num of neurons in each layer -list
        self.activation_layers=activ_fns    #Activation fn of each layer -list
        self.loss_fn=loss_fn                #Loss function 
        self.optimizer=opti_tech            #Optimizer 
        self.lr=lr                          #learning rate
        self.epochs=epochs                  #epochs
        self.kernal_init=kernal_init        #Weights Initializer
        self.model=keras.models.Sequential()#keras's Functional API for model
    def connect_network(self,normalize=False):
        #This fn connects and compiles model
        for i in range(self.total_layers):
            self.model.add(keras.layers.Dense(self.neuron_layers[i],activation=self.activation_layers[i],kernal_initializer=self.kernal_init))
            if normalize==True:
                self.model.add(keras.layers.BatchNormalization())
        #compiling model
        self.model.compile(loss=self.loss_fn,optimizer=self.op)
        