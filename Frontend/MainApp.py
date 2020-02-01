import kivy
kivy.require('1.11.1') 
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics.instructions import Canvas
from kivy.graphics import *
#main.kv
#rgba(44, 58, 71,1.0)
Builder.load_string('''
<MainScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1.0 #Will change color later
            Rectangle:
                pos: self.pos
                size: self.size
        canvas: 
            Color: 
                rgba: 1, 1, 1, 1
            Line: 
                width: 5
                rectangle: (self.x, self.y, self.width, 0.3)
        StackLayout:
            size_hint: 1,0.45
            pos_hint:{"left":0,"bottom":root.width}
            Button:
                text: "Save Current Model"
                size_hint: 1/3.,0.1
            Button:
                text: "Training Stats"
                size_hint: 1/3.,0.1
            Button:
                text: "Browse traindata (*.csv)"    
                size_hint: 1/3.,0.1
            Button:
                text: "Load Exsisting Model"
                size_hint: 1/3.,0.1
            Button:
                text: "Report a Bug"
                size_hint: 1/3.,0.1    
            Button:
                text: "Browse testdata (*.csv)"    
                size_hint: 1/3.,0.1
''')
class MainScreen(FloatLayout):
    pass

class NNSandboxApp(App):
    def build(self):
        return MainScreen()