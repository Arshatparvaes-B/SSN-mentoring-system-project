from tkinter import *       
from tkinter import messagebox
m=Tk()
m.title("SSN Mentoring system")
m.iconbitmap()
m.geometry('1920x1080')
#
img=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssnpro1.png')  #importing image of SSN
lab=Label(m,image=img)
lab.place(x=0,y=0,relheight=1,relwidth=1)

myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
myframe.pack(padx=250,pady=250)

def personalinfo(myframe):
    return
def academicdetails(myframe):
    return
def mentorship(myframe):
    return
def login(myframe):            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='arun' and passw=='123'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.pack(padx=250,pady=250)
        mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe))
        mb.grid(row=1,column=1,padx=10,pady=10)
        mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
        mb1.grid(row=1,column=2,padx=10,pady=10)
        mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
        mb2.grid(row=1,column=3,padx=10,pady=10)
    else:
        messagebox.showinfo("","incorrect")

def login1(myframe):            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='mentor' and passw=='345'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.pack(padx=50,pady=50)
        messagebox,messagebox.showinfo("","lgin sucessful")
    else:
        messagebox.showinfo("","incorrect")



def back(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    mybutton1=Button(myframe,text="Manager",borderwidth=0,font=('Helvetica',14),command=lambda:open(myframe))        # creating buttons for manager, mentor , mentee
    mybutton1.grid(row=1,column=0,padx=10,pady=10)
    mybutton2=Button(myframe,text="Mentor",borderwidth=0,font=('Helvetica',14),command=lambda :open(myframe))
    mybutton2.grid(row=1,column=1,padx=10,pady=10)
    mybutton3=Button(myframe,text="Mentee",borderwidth=0,font=('Helvetica',14),command=lambda :open(myframe))    
    mybutton3.grid(row=1,column=2,padx=10,pady=10)
def open(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)

   
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login(myframe)).place(relx=0.7,rely=1)
def open1(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)

   
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login1(myframe)).place(relx=0.7,rely=1)
        

mybutton1=Button(myframe,text="Manager",font=('Helvetica',14),command=lambda :open(myframe))        # creating buttons for manager, mentor , mentee
mybutton1.grid(row=4,column=0,padx=10,pady=10)
mybutton2=Button(myframe,text="Mentor",font=('Helvetica',14),command=lambda :open1(myframe))
mybutton2.grid(row=4,column=1,padx=10,pady=10)
mybutton3=Button(myframe,text="Mentee",font=('Helvetica',14),command=lambda :open(myframe))    
mybutton3.grid(row=4,column=2,padx=10,pady=10)

m.mainloop()


