from Frontend.MainApp import NNSandboxApp,ExceptionHandler
import traceback

if __name__ == "__main__":
    try:
        app=NNSandboxApp()
        app.run()
    except Exception as inst:
        text=str(str(type(inst))+"\n"+str(inst.args)+"\n"+"You can report this using report bug button")
        print(text)
        print(traceback.print_tb(inst.__traceback__)) #For debugging
        ExceptionHandler(text=text+"\n Close the App and try again").run()
        