from Backend.NeuralNetwork import NN
from Backend.DataPreprocessing import DataProcessor,DataSplitter
import tkinter as tk
from tkinter import filedialog
import os
import time
import kivy
kivy.require('1.11.1') 
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics.instructions import Canvas
from kivy.graphics import *
from kivy.uix.filechooser import FileChooser
from kivy.uix.checkbox import CheckBox
import webbrowser
from PIL import Image

class Layer(BoxLayout):
    pass

class Middle(BoxLayout):
    def add_layer(self):
        self.add_widget(Layer())
    
    def remove_layer(self):
        if len(self.children) > 2:
            self.remove_widget(self.children[0])
                        
class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.epochs=1
        self.lr=0.01
        self.kernal_init="he_normal"
        self.loss_fn="sparse_categorical_crossentropy"
        self.optimizer="SGD"
        self.running=False
        self.validation_split=0
        self.smart_preprocess=True
        self.label_at_start=True
        self.train_path=""
        self.test_path=""
        self.batch_normalization=True
        self.metrics=["accuracy"]
        self.model=NN()
        
    def open_browser(self,tutorial=False,help=False,bug=False):
        if tutorial:
            webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/README.md")
        if help:
            webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/HELP.md")
        if bug:
            webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/issues/newa")
    
    def get_csv_file(self,Train=False,Test=False):
        root = tk.Tk()
        root.withdraw()        
        if Train:
            self.train_path=filedialog.askopenfilename(filetypes=[('CSV File','*.csv')])
        if Test:
            self.test_path=filedialog.askopenfilename(filetypes=[('CSV File','*.csv')])
    
    def get_h5_file(self):
        root = tk.Tk()
        root.withdraw()
        loaded_model_path=filedialog.askopenfilename(filetypes=[('HDF5 File','*.h5')])
        self.load_model(loaded_model_path)
    
    def show_img(self,Train=False,Test=False):
        if Train:
            im = Image.open('train_history_img.png')
            im.show()    
        if Test:
            im = Image.open('test_history_img.jpg')
            im.show()    
    def change_epoch(self,Incr=False,Decr=False):
        val=int(self.ids.epochs.text)
        if Incr:
            self.epochs=str(val+1)
            self.ids.epochs.text=self.epochs
        if Decr:
            self.epochs=str(max(1,val-1))
            self.ids.epochs.text=self.epochs
            
    def reset(self):
        if not self.running:
            self.ids.epochs.text=str(1)
            self.ids.lr.text=str(0.01)
            self.ids.optimizer.text=str("SGD")
            self.ids.loss_fn.text=str("sparse_categorical_crossentropy")
            self.ids.kernal_init.text=str("he_normal")
            self.ids.validation_split.value=0
            self.ids.label_start.active=True
            self.ids.smart_preprocess.active=True
            self.train_path=""
            self.test_path=""
            while(len(self.ids.mid.children)>2):
                self.ids.mid.remove_layer()
            for children in self.ids.mid.children:
                children.ids.neurons.text=str(1)
                children.ids.activation_fn.text=str("None")
            
    def start(self):
        self.running=True
        layers_n,layers,active_fns=self.setup()
        self.model=NN(
            GPU=True,
            layers_n=layers_n,
            layers=layers,
            activ_fns=active_fns,
            loss_fn=self.loss_fn,
            opti_tech=self.optimizer,
            lr=self.lr,
            epochs=int(self.epochs),
            kernal_init=self.kernal_init,
            metrics=self.metrics
        )
        shape,x_train,y_train,x_test,y_test,x_val,y_val=None,[None],[None],[None],[None],[None],[None]
        if self.validation_split!=0 and self.test_path=="":
            d=DataSplitter(self.train_path,smart_preprocess=self.smart_preprocess)
            shape,x_train,x_test,x_val,y_val,x_test,y_test=d.get_splitted_xy(test_r=0.1,val_r=self.validation_split/100)
            #self.ids.mid.children[layers_n-1].neurons.text=str(d.cols)
        
        if self.validation_split==0 and self.test_path=="":
            d=DataProcessor(self.train_path)
            shape,x_train,y_train=d.get_xy(label_last= not self.label_at_start,smart_preprocess=self.smart_preprocess)
            #self.ids.mid.children[layers_n-1].neurons.text=str(d.cols)
        
        if self.validation_split==0 and self.test_path!="":
            d=DataProcessor(self.train_path)
            shape,x_train,y_train=d.get_xy(label_last= not self.label_at_start,smart_preprocess=False)
            d=DataProcessor(self.test_path)
            shape,x_test,y_test=d.get_xy(label_last= not self.label_at_start,smart_preprocess=False)
        
        if self.validation_split!=0 and self.test_path!="":
            d=DataProcessor(self.train_path)
            shape,x_train,y_train=d.get_xy(label_last=not self.label_at_start,smart_preprocess=False)
            d=DataSplitter(self.test_path)
            shape,x_test,y_test,x_val,y_val=d.get_splitted_xy(test_r=self.validation_split/100)
        self.running=False
        #Actual Training and Testing 
        self.model.connect_network(shape=shape,normalize=self.batch_normalization)
        if x_val==None:
            self.model.fit(x_train,y_train)
            if not isinstance(x_test,list):
                self.model.evaluate(x_test,y_test)
        else:
            self.model.fit(x_train,y_train,x_val=x_val,y_val=y_val)
            if not isinstance(x_test,list):
                self.model.evaluate(x_test,y_test)
        #Saving history
        self.model.train_visualize()
        #self.model.test_visualize()
                
    def setup(self):
        self.running=True
        #Checking errors
        try:
            self.lr=float(self.lr)
        except ValueError:
            popup = Popup(title='Learning Rate Error', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text='Learning rate must be a number.(Genrally between 0 and 1)')))
            self.ids.start_btn.state="normal"
            self.running=False
            return
        if self.train_path=="":
            popup = Popup(title='Training Data Error', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text='Make sure training data is selected')))
            self.ids.start_btn.state="normal"
            self.running=False
            return 
        layers_n=len(self.ids.mid.children)
        layers=[]
        active_fns=[]
        i=layers_n
        for children in self.ids.mid.children: 
            try:
                layers.append(int(children.ids.neurons.text))
                active_fns.append(children.ids.activation_fn.text)
            except ValueError:
                popup = Popup(title='Neurons Error', size_hint=(0.5, 0.5),auto_dismiss=True)
                popup.open()
                popup.add_widget((Label(text=f'Number of neurons in layer {i} is not a number')))
                self.ids.start_btn.state="normal"
                self.running=False
                return                 
            i-=1
        self.running=False
        layers.reverse()
        active_fns.reverse()
        print(layers,active_fns)
        return layers_n,layers,active_fns
    
    def pause(self):
        if self.running==False:
            pass#Do something here
    
    def save_model(self):
        try:
            file_name="MyModel"+time.strftime("%Y-%m-%d-%H-%M-%S")
            self.model.save_model(file_name)
            popup = Popup(title='Current model saved successfully !!', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text='Model Saved in current directory with name {file_name}')))
        except ValueError:
            popup = Popup(title='Cannot Save Model', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text='First Train the model before saving it !!!')))
                            
    def load_model(self,path):
        pass
                        
class NNSandboxApp(App):
    def build(self):
        return MainScreen()
