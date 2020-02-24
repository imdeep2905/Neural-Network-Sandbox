from Frontend.MainApp import NNSandboxApp,ExceptionHandler #Importing mainapp and exception handler
import traceback #For tracing error's source

if __name__ == "__main__":
    try:
        #Running App
        NNSandboxApp().run()
    except Exception as e:
        #In case any exception occurs it is displayed to user
        text=str(str(type(e))+"\n"+str(e.args)+"\n"+"You can report this using report bug button")
        print(text)
        print(traceback.print_tb(e.__traceback__)) #For debugging
        ExceptionHandler(text=text+"\n Close the App and try again").run()
        