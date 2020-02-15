import tkinter as tk
from tkinter import filedialog
import os
import kivy
kivy.require('1.11.1') 
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
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
        print(Train,Test,filedialog.askopenfilename(filetypes=[('CSV File','*.csv')]) )        
    
    def get_h5_file(self):
        root = tk.Tk()
        root.withdraw()
        print(filedialog.askopenfilename(filetypes=[('HDF5 File','*.h5')]) )
    
    def show_img(self,Train=False,Test=False):
        if Train:
            im = Image.open('train_history_img.jpg')
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
    
    def start(self):
        self.running=True
        
        self.running=False
    
    def pause(self):
        pass
        
class NNSandboxApp(App):
    def build(self):
        return MainScreen()
