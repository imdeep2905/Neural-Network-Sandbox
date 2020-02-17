from Backend.NeuralNetwork import NN
from Backend.DataPreprocessing import DataProcessor,DataSplitter
import tkinter as tk
from tkinter import filedialog
import os
import traceback
import time
import kivy
kivy.require('1.11.1') 
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.graphics import Ellipse
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
    def draw_neurons(self):
        self.canvas.add(Color(0.33,0.6,0.3))
        for i in range (int(self.ids.neurons.text)):
            print(i)
            self.canvas.add(Ellipse(size=(100,100),pos_hint={"x":0.5,"y":0.5}))

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
        self.metrics=["accuracy","mse"]
        self.stats="loss: ,val_loss: ,acc: "
        self.model=0
        self.gpu_use=True
        
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
            self.model.train_visualize()
            im = Image.open('train_history_img.png')
            im.show()    
        if Test:
            if self.test_path=="":
                popup = Popup(title='Error', size_hint=(0.5, 0.5),auto_dismiss=True)
                popup.add_widget((Label(text='Make sure that model is tested before visualizing testing data')))
                popup.open()
            else:   
                self.model.test_visualize() 
                im = Image.open('test_history_img.png')
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
        with open('log.txt','w') as f:
            f.write("")
        self.running=True
        layers_n=2
        layers=[1,1]
        active_fns=[None,None]
        layers_n,layers,active_fns=self.setup()
        if layers==-1:
            return
        self.model=NN(
            GPU=self.gpu_use,
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
        shape,x_train,y_train,x_test,y_test=None,[None],[None],[None],[None]
        d=DataProcessor(self.train_path,smart_preprocess=self.smart_preprocess)
        shape,x_train,y_train=d.get_xy(label_last= not self.label_at_start)
        if self.test_path!="":
            d=DataProcessor(self.test_path,smart_preprocess=self.smart_preprocess)
            shape,x_test,y_test=d.get_xy(label_last=not self.label_at_start)
            self.model.connect_network(shape=shape,normalize=self.batch_normalization)
            self.model.fit(x_train,y_train,val_split=self.validation_split/100)
            self.model.evaluate(x_test,y_test)
        else:
            self.model.connect_network(shape=shape,normalize=self.batch_normalization)             
            self.model.fit(x_train,y_train,val_split=self.validation_split/100)         
        #Saving history
        self.update_stats()
        self.running=False
                
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
            return -1,-1,-1
        if self.train_path=="":
            popup = Popup(title='Training Data Error', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.add_widget((Label(text='Make sure that training data is selected')))
            popup.open()
            self.ids.start_btn.state="normal"
            self.running=False
            return -1,-1,-1
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
                return -1,-1,-1                
            i-=1
        layers.reverse()
        active_fns.reverse()
        print(layers,active_fns)
        return layers_n,layers,active_fns
    
    def save_model(self):
        try:
            file_name="MyModel"+time.strftime("%Y-%m-%d-%H-%M-%S")
            self.model.save_model(file_name)
            popup = Popup(title='Current model saved successfully !!', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text=f'Model Saved in current directory with name {file_name}')))
        except ValueError:
            popup = Popup(title='Cannot Save Model', size_hint=(0.5, 0.5),auto_dismiss=True)
            popup.open()
            popup.add_widget((Label(text='First Train the model before saving it !!!')))
                            
    def load_model(self,path):
        pass
    
    def update_stats(self,text=""):
        with open('log.txt', 'r') as f:
            data=f.read()
            #print(data)
        self.ids.stats.text=text+str(data)

                        
class NNSandboxApp(App):
    def build(self):
        return MainScreen()

class ExceptionHandler(App):
    def __init__(self, text="",**kwargs ):
        super().__init__(**kwargs)
        self.text=text

    def build(self):
        return Label(size=(700,700),text=self.text)
