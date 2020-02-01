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
#main.kv
#rgba(44, 58, 71,1.0)
Builder.load_string('''
<MainScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.137, 0.149, 0.161, 1.0 #Will change color later
            Rectangle:
                pos: self.pos
                size: self.size
        #1/3 MainScreen
        FloatLayout:
            pos_hint: {"x":0,"y":.7}
            size_hint:1,0.3
            ToggleButton:
                pos_hint: {"x":0,"y":0}
                border: 0,0,0,0
                size_hint: 0.1,0.3
                background_color:(0.137, 0.149, 0.161, 1.0)
                background_normal:'play.png'
                background_down: 'pause.png'
            Button:
                pos_hint: {"x":0.1,"y":0}
                border: 0,0,0,0
                size_hint: 0.1,0.3
                background_normal:'reset.png'
        #2/3 MainScreen
        BoxLayout:
            pos_hint: {"x":0,"y":.15}
            size_hint:1,0.55
            Button:
                text:"Animation"
        #3/3 MainScreen
        GridLayout:
            size_hint: 1,0.15 
            cols: 3
            Button:
                text: "Save Current Model"
            Button:
                text: "Visualize Training"
            Button:
                text: "Browse training data(*.csv)"
            Button:
                text: "Load Existing Model"
            Button:
                text: "Visualize Testing"
            Button:
                text: "Browse testing data(*.csv)"
            Button:
                text: "About"
            Button:
                text: "Report a Bug"
            BoxLayout:
                Label:
                    size_hint: 0.4,1
                    text: "Validation Split: "
                Slider:
                    size_hint: 0.5,1
                    id: slider
                    min: 0
                    max: 90
                    step: 10
                    orientation: 'horizontal'
                Label:
                    size_hint: 0.1,1
                    text: str(slider.value)+str("%")
''')
class MainScreen(FloatLayout):
    pass

class NNSandboxApp(App):
    def build(self):
        return MainScreen()
