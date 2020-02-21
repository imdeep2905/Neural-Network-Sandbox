#Using tf,tf.keras as backend for NN
import tensorflow as tf
from tensorflow import keras
import time
from tensorflow.keras.callbacks import Callback
#other packages
import pandas as pd 
import matplotlib.pyplot as plt 
import os
import json
#Permit CPU usage
def set_device(GPU):
    if GPU==False:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1' #For CPU use

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

class MyLogger(Callback):
        
    def on_epoch_end(self, epoch,logs):
        with open('log.txt', 'w') as f:
            stats= "Epoch: "+ str(epoch+1)
            for key in logs:
                stats+=" - "+str(key).capitalize()+": "+str(round(logs[key],2))
            f.write(stats)
                
#class NN for Neural Network
class NN:
    def __init__(self,GPU=True,layers_n=1,layers=[1],activ_fns=["relu"],loss_fn="sparse_categorical_crossentropy",opti_tech="SGD",lr=0.01,epochs=1,kernal_init="he_normal",metrics=["accuracy"]):
        set_device(GPU=GPU)
        keras.backend.clear_session()
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
    
    def connect_network(self,shape=[28,28],normalize=False):
        #This fn connects and compiles model
        #Creating Model
        self.model.add(keras.layers.Flatten(input_shape=shape))     
        for i in range(1,self.total_layers):
            if normalize==True:
                self.model.add(keras.layers.BatchNormalization())
            self.model.add(keras.layers.Dense(self.neuron_layers[i],activation=self.activation_layers[i],kernel_initializer=self.kernal_init))
        #Compiling Model    
        self.model.compile(loss=self.loss_fn,optimizer=get_optimizer(self.optimizer,self.lr),metrics=self.metrics)
        print(self.model.summary()) #for debugging 
    
    def fit(self,x_train,y_train,val_split=0.0,shuffle=True):
        self.train_history=self.model.fit(x_train,y_train,epochs=self.epochs,validation_split=val_split,callbacks=[MyLogger()],shuffle=shuffle)
            
    def evaluate(self,x_test,y_test):
        self.test_history=self.model.evaluate(x_test,y_test,verbose=0)#Bug in tf (too many '='s in console)
    
    def train_visualize(self,size_x=8,size_y=5):
        pd.DataFrame(self.train_history.history).plot(figsize=(size_x,size_y)) 
        plt.grid(True)
        plt.xlabel('epochs')
        plt.ylabel('value')
        plt.savefig("train_history_img")
    
    def get_test_stats(self):
        #not working
        stats="Loss: " + str(self.test_history[0]) +"\nAccuracy: " +str(self.test_history[1]) + "\nMSE: " + str(self.test_history[2])
        return stats
            
    def save_model(self,name,path="."):
        self.model.save(os.path.join(path,name+".h5"))
    
    def load_model(self,path):
        self.model=keras.models.load_model(path)
        return self.model.to_json() #returns model config in json form