from tkinter import *
from mydb import Database
from tkinter import messagebox
class NLPApp:

    def __init__(self):

        # create db object
        self.dbo=Database()

        #login gui load
        self.root=Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#3377FF')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()

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

    def register_gui(self):
        self.clear()

        heading=Label(self.root,text="NLPApp",bg='#3377FF',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0=Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn=Button(self.root,text='Register',width=25,height=2,
                            command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label1=Label(self.root,text='Already a member?')
        label1.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(20,10))
    def clear(self):
        #clear existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('error','Email already exists')

nlp = NLPApp()