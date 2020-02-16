#importing necessary libraries
import tensorflow as tf 
import pandas as pd 
import os
import numpy as np 
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self,path,smart_preprocess=False):
        self.data=pd.read_csv(path)
        self.x_data=0
        self.y_data=0
        self.cols=0
        self.smart_preprocess=smart_preprocess
    
    def get_xy(self,label_last=True):
        if self.smart_preprocess:
            self.cols=self.smart_preprocess_()
        # Currently only single label is supported
        #self.data=self.data.drop(["thal"],axis=1) #TESTING
        if label_last:
            target=self.data.pop(self.data.columns[len(self.data.columns)-1])
            self.y_data=target.values
        else:
            target=self.data.pop(self.data.columns[0])
            self.y_data=target.values
        self.x_data=self.data.values
        shape=[self.x_data.shape[1],]
        return shape,self.x_data,self.y_data
    
    def smart_preprocess_(self,factor=3):
        # *** Experimental ***
        #this fn will replace missing values and convert non-numeric values to numeric
        #Dropping unnecessary cols and non numeric -> numeric
        #                   ****
        #Need to impliment the drops of ID like columns
        #                   ****
        non_numeric_cols=self.data.select_dtypes(include="object")
        for col in non_numeric_cols:
            if len(self.data[col].unique())>self.data.shape[0]//factor or (self.data.shape[0]-self.data[col].count()) > self.data.shape[0]//factor:
                self.data.drop([col],inplace=True,axis=1)
            else:
                self.data[col]=pd.Categorical(self.data[col]).codes
        #Filling Missing values
        self.data.fillna(value=self.data.median(),inplace=True)
        return self.data.shape[1]
        
class DataSplitter(DataProcessor):
    #this class is inherited because all basic funcs are same except this will split data
    def __init__(self,path,smart_preprocess):
        super().__init__(path=path,smart_preprocess=smart_preprocess)
        
    def get_splitted_xy(self,test_r=0.1,val_r=None,label_last=True,seed=42):
        shape,x_data,y_data=super().get_xy(label_last=label_last)
        x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=test_r, random_state=seed)
        if val_r!=None:
            x_test,x_val,y_test,y_val=train_test_split(x_test, y_test, test_size=val_r,random_state=seed)
            return shape,x_train,y_train,x_val,y_val,x_test,y_test
        else:
            return shape,x_train,y_train,x_test,y_test

#class ImageToData: #if time permits this will be implimented