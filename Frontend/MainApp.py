import kivy
kivy.require('1.11.1') 
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text="Hello from Frontend !!!")