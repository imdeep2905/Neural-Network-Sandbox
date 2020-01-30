#importing necessary libraries
import tensorflow as tf 
import pandas as pd 
import os
import numpy as np 

class DataProcessor:
    def __init__(self,name,path="."):
        self.file_path=os.path.join(path,name)
        self.data=pd.read_csv(self.file_path)
        self.x_data=0
        self.y_data=0
    
    def get_xy(self,label_last=True):
        # Currently only single label is supported
        #self.data=self.data.drop(["thal"],axis=1) #TESTING
        if label_last==True:
            target=self.data.pop(self.data.columns[len(self.data.columns)-1])
            self.y_data=target.values
        else:
            target=self.data.pop(data.columns[0])
            self.y_data=target.values
        self.x_data=self.data.values
        shape=[self.x_data.shape[1],]
        return self.x_data,self.y_data,shape
    
    def smart_preprocess(self,):
        #this fn will replace missing values and convert non-numeric values to numeric
    
class DataSplitter:
    def __init__(self,name,path=".",train_r=0.9,test_r=0.1,val_r=0.0):
        self.file_path=os.path.join(path,name)
        self.data=pd.read_csv(self.file_path)
    
    def get_xy(self,label_cnt=1,label_last=True):
        pass
    
    def smart_preprocess(self):
        pass