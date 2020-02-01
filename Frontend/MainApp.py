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
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics.instructions import Canvas
from kivy.graphics import *
from kivy.uix.filechooser import FileChooser
import webbrowser

class MainScreen(FloatLayout):
    def open_tutorial(self):
        webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/README.md")
    def open_help(self):
        webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/blob/master/HELP.md")
    def report_bug(self):
        webbrowser.open("https://github.com/imdeep2905/Neural-Network-Sandbox/issues/newa")
    def get_file(self,Train=False,Test=False):
        root = tk.Tk()
        root.withdraw()
        print(Train,Test,filedialog.askopenfilename(filetypes=[('CSV Files','*.csv')]) )        

class NNSandboxApp(App):
    def build(self):
        return MainScreen()
