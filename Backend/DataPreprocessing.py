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
            target=self.data.pop(self.data.columns[0])
            self.y_data=target.values
        self.x_data=self.data.values
        shape=[self.x_data.shape[1],]
        return self.x_data,self.y_data,shape
    
    def smart_preprocess(self,factor=3):
        # *** Experimental ***
        #this fn will replace missing values and convert non-numeric values to numeric
        #Dropping unnecessary cols and non numeric -> numeric
        non_numeric_cols=self.data.select_dtypes(include="object")
        for col in non_numeric_cols:
            if len(self.data[col].unique())>self.data.shape[0]//factor or (self.data.shape[0]-self.data[col].count()) > self.data.shape[0]//factor:
                self.data.drop([col],inplace=True,axis=1)
            else:
                self.data[col]=pd.Categorical(self.data[col]).codes
        #Filling Missing values
        self.data.fillna(value=self.data.median(),inplace=True)
        return self.data.shape[1]
        
class DataSplitter:
    def __init__(self,name,path=".",train_r=0.9,test_r=0.1,val_r=0.0):
        self.file_path=os.path.join(path,name)
        self.data=pd.read_csv(self.file_path)
    
    def get_xy(self,label_cnt=1,label_last=True):
        pass
    
    def smart_preprocess(self):
        pass