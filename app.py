from tkinter import *

class NLPApp:

    def __init__(self):

        #login gui
        self.root=Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#3377FF')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        heading=Label(self.root,text="NLPApp",bg='#3377FF',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn=Button(self.root,text='Login',width=25,height=2)
        login_btn.pack(pady=(10,10))

        label1=Label(self.root,text='Not a member?')
        label1.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(20,10))

nlp = NLPApp()