from tkinter import *

class NLPApp:

    def __init__(self):

        #login gui
        self.root=Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#FFE933')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        heading=Label(self.root,text="NLPApp")



nlp = NLPApp()