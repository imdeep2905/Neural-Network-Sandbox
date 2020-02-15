from kivy.uix.popup import Popup
from Frontend.MainApp import NNSandboxApp
from kivy.uix.label import Label
       
if __name__ == "__main__":
    try:
        NNSandboxApp().run()
    except Exception as inst:
        text=str(str(type(inst))+"\n"+str(inst.args)+"\n"+"You can report this using report bug button")
        popup = Popup(title='Exception Occured', size_hint=(0.5, 0.5),auto_dismiss=True)
        popup.open()
        popup.add_widget((Label(text=text)))