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
    def add_w(self):
        self.add_widget(Layer())
    def remove_w(self):
        if len(self.children) > 2:
            self.remove_widget(self.children[0])
                        
class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.epochs=1
    def open_tutorial(self):
        webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/README.md")
    def open_help(self):
        webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/HELP.md")
    def report_bug(self):
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
            self.ids.epochs.text=str(val+1)
        if Decr:
            self.ids.epochs.text=str(max(1,val-1))
    def temp(self,text):
        print(text)
        
class NNSandboxApp(App):
    def build(self):
        return MainScreen()
