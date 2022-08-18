from ast import Lambda
from re import T
from tkinter import *       
from tkinter import messagebox
import math
from samplecode import *
import logincred
import csv
import avl
import linkedlist
import main
#from tkcalendar import Calendar
snoe,dide,ree,ssne,gene,dte,se,sne=None,None,None,None,None,None,None,None
ae,be,ce=None,None,None
marks_tree=None
class BST:

	"""This constructor takes 3 arguments: self, key and number. Key-record, number - serial number"""
	def __init__(self,key,number):
		self.key=key
		self.lchild=None
		self.rchild=None
		self.position=number
    
	# This method inserts the records in the binary search tree. It compares the number 
	# passed as an argument, compares the number with the numbers of previously inserted nodes,
	#  and places the record in the tree accordingly.

	def insert(self,data,number):
		if self.position is None:
			self.key=data
			return
		elif self.position>number:
			if self.lchild is None:
				self.lchild= BST(data,number)
			else:
				self.lchild.insert(data,number)
		else:
			if self.rchild:
				self.rchild.insert(data,number)
			else:
				self.rchild= BST(data,number)

	"""This method traverses and prints the records in the ascending order of serial number of records."""

	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key,end= "\n")
		if self.rchild:
			self.rchild.inorder()
"""Piece of code which reads the records in the csv file containing mentee details""" 

f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\IT-A details.txt","r")
n=next(csv.reader(f))
l=[]
for i in csv.reader(f):
	l.append(i)
f.close()

"""Insertion of records into the binary search tree start here."""

obj=BST(l[31],32)
n=16
p=n
i=1
q=n
c=0
while c<5:
    
    for j in range(2**i):
        obj.insert(l[int(p-1)],p)
        p= p + 2**((math.log(q,2))+1)
    i+=1
    o = n/(2**(i-1))
    p=o
    q=o
    c+=1

"""Calling .inorder() method to print the records."""
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

f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\credentials1.txt","r")

lis=[]
x=[]
y=[]
no=next(csv.reader(f))
for i in csv.reader(f):
    x.append(i[0])
f.seek(1)
no=next(csv.reader(f))
for j in csv.reader(f):
    y.append(j[1])
lis.append(x)
lis.append(y)
#f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\credentials1.txt","r")
aru=[]
f.seek(0)
a=next(csv.reader(f))
for z in csv.reader(f):
    aru.append(z)
#f.close()
f.close()
s=None
#one_mentee_details=None
def personalinfo(myframe,fno):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.6)
    global aru
    T=main.T4
    root=main.root4
    T.retrieve(root,fno)
    record=T.record
    l1=[("digital Id",record[1]),("roll No",record[2]),
        ("Name",record[3]),("Section",record[4]),("dept",record[5]),
        ("Email-Id",record[6]),("Gender",record[7])]
        
        
    for i in range(len(l1)):
        for j in range(2):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l1[i][j])               #mentee personal info
    '''def search(tree,data):

        global s
        if tree.key==data:
            s="found"
        elif data<tree.key:
            if tree.lchild:
                search(tree.lchild,data)
            else:
                return False
        elif data>tree.key:
            if tree.rchild:
                search(tree.rchild,data)
            else:
                return False'''


    '''def createBST(l,a=0):
        
        """This function creates BST """
        obj=BST(l[31][a:],32)
        n=16
        p=n
        i=1
        q=n
        c=0
        while c<5:
            
            for j in range(2**i):
                obj.insert(l[int(p-1)][a:],p)
                p= p + 2**((math.log(q,2))+1)
            i+=1
            o = n/(2**(i-1))
            p=o
            q=o
            c+=1
        return obj'''

    '''def retrieve(tree,um):
        global one_mentee_details
        if tree.key[-2]==um:
            one_mentee_details=tree.key
        elif um<tree.key[-2]:
            if tree.lchild:
                retrieve(tree.lchild,um)
            else:
                return False
        elif um>tree.key[-2]:
            if tree.rchild:
                retrieve(tree.rchild,um)
            else:
                return False   
    credtree=createBST(aru)
   

    l1=[]
    def check(tree,un,pd):
        
        
        search(tree,[un,pd])

        
    
        retrieve(mentee_details_tree,user4)
        l1=[("digital Id",one_mentee_details[1]),("roll No",one_mentee_details[2]),
        ("Name",one_mentee_details[3]),("Section",one_mentee_details[4]),("dept",one_mentee_details[5]),
        ("Email-Id",one_mentee_details[6]),("Gender",one_mentee_details[7])]
        
        
        for i in range(len(l1)):
            for j in range(2):
                e=Entry(m,width=20,fg='blue')
                e.grid(row=i,column=j)
                e.insert(0,l1[i][j])  
            
        
    b=check(credtree,user4,passw4)'''
    
def marks(myframe):
    global one_mentee_details
    global marks_tree
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.5)
    if a=="SELECT EXAM":

    
        f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\CAT-1results.txt","r")
        #c=csv.reader(f)
        no=next(csv.reader(f))
        l=[]
        for i in csv.reader(f):
            l.append(i)
        f.close()
        #print(l)

        marks_tree=createBST(l)

    elif a=="CAT-2":
        f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\CAT-2 results.txt","r")
        c=csv.reader(f)
        no=next(c)
        l=[]
        for i in c:
            l.append(i)
        f.close()

        marks_tree=createBST(l)
    
    elif a=="SAT":
        f=open()  #inside the parenthesis put the filename containing SAT Marks
        c=csv.reader(f)
        no=next(c)
        l=[]
        for i in c:
            l.append(i)
        f.close()

        marks_tree=createBST(l)
    #marks_tree.inorder()

    one_mentee_details=retrievex(marks_tree,user4,1)

    marks_details=one_mentee_details[3:]
    marks_details=[("Maths",marks_details[0]),("BEEE",marks_details[1]),("Physics",marks_details[2]),("PDS",marks_details[3]),
    ("HSE",marks_details[4]),("EVS",marks_details[5])]

    total_rows=len(marks_details)
    
    for i in range(total_rows):
        for j in range(2):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,marks_details[i][j])  
        

def academicdetails(myframe):
    global a
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.5)
    #myframe.config(text=clicked.get())
    #label=Label(myframe,text)
    options = [
	"CAT-1",
	"CAT-2",
	"SAT"]

# datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("SELECT EXAM")

    # Create Dropdown menu
    drop = OptionMenu( myframe, clicked , *options )
    drop.pack()
    a=clicked.get()
    #print(a)
    # Create button, it will change label text
    button = Button( myframe, text = "SELECT",command=lambda: marks(myframe) ).pack()

def mentorship(myframe):
    return
def login(myframe):   
    global user4
    global passw4
    
    # entering details of the user
    user4=entry1.get()
    passw4=entry2.get()
    d=logincred.give(user4,passw4,logincred.t)    
    if d=='Invalid username or password':
        messagebox.showinfo("","blank invalid")
    elif isinstance(d,str):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.pack(padx=250,pady=250)
        mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe,int(d)))
        mb.grid(row=1,column=1,padx=10,pady=10)
        mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
        mb1.grid(row=1,column=2,padx=10,pady=10)
        mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
        mb2.grid(row=1,column=3,padx=10,pady=10)
    else:
        messagebox.showinfo("","incorrect")
#d#]ef next(myframe):          #for creating to add update delete
    #myframe.destroy() a page
    #myframe=LabelFrame(m,bg="white")   #importing the frame colour
    #myframe.pack(padx=250,pady=250)
    #mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe))
    #mb.grid(row=1,column=1,padx=10,pady=10)
    #mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
    #mb1.grid(row=1,column=2,padx=10,pady=10)
    #mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
    #mb2.grid(row=1,column=3,padx=10,pady=10)
def add(myframe,username):
    global snoe,dide,ree,ssne,gene,dte,se,sne,un
    un=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    sno=Label(myframe,text='Serial No.').grid(row=1,column=1)
    snoe=Entry(myframe,bd=5)
    snoe.grid(row=1,column=2)
    did=Label(myframe,text='Digital ID').grid(row=2,column=1)
    dide=Entry(myframe,bd=5)
    dide.grid(row=2,column=2)
    re=Label(myframe,text='Register No.').grid(row=3,column=1)
    ree=Entry(myframe,bd=5)
    ree.grid(row=3,column=2)
    sn=Label(myframe,text='Student Name').grid(row=4,column=1)
    sne=Entry(myframe,bd=5)
    sne.grid(row=4,column=2)
    s=Label(myframe,text='Section').grid(row=5,column=1)
    se=Entry(myframe,bd=5)
    se.grid(row=5,column=2)
    dt=Label(myframe,text='Department').grid(row=6,column=1)
    dte=Entry(myframe,bd=5)
    dte.grid(row=6,column=2)
    ssn=Label(myframe,text='SSN Mail ID').grid(row=7,column=1)
    ssne=Entry(myframe,bd=5)
    ssne.grid(row=7,column=2)
    gen=Label(myframe,text='Gender').grid(row=8,column=1)
    gene=Entry(myframe,bd=5)
    gene.grid(row=8,column=2)
    sdj=Button(myframe,text='INSERT',command=lambda: add1(myframe)).grid(row=10,column=1)
def add1(myframe):

    a=snoe.get()
    b=dide.get()
    c=sne.get()
    d=se.get()
    e=ree.get()
    f=dte.get()
    g=ssne.get()
    h=gene.get()
    details=[a,b,e,c,d,f,g,h]
    if un=='divyajohn@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    elif un=='chandrasekar@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    elif un=='rajalakshmi@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()

    f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","w",newline="")
    w=csv.writer(f)
    w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
    w.writerows(l)
    f.close()
    # root=None
    # Tnew=avl.AVL1()
    # for i in l:
    #     root=Tnew.insert(root,int(i[0]),i)
    # l1=Tnew.inorder(root)
    # print(l1)
    # root=main.root3
    # mentees=main.T3
    # print(details[0],type(details[0]))
    # root=mentees.insert(root,int(details[0]),details)
    
def update(myframe,username):
    global ae,be,ce,unam
    unam=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    a=Label(myframe,text='Enter SNO. of the record to be updated').grid(row=2,column=2)
    b=Label(myframe,text='Enter type of data to be updated').grid(row=3,column=2)
    c=Label(myframe,text='Enter the new data to be replaced').grid(row=4,column=2)
    ae=Entry(myframe,bd=5)
    ae.grid(row=2,column=3)
    be=Entry(myframe,bd=5)
    be.grid(row=3,column=3)
    ce=Entry(myframe,bd=5)
    ce.grid(row=4,column=3)
    d=Button(myframe,text='UPDATE THE DETAILS',command=lambda :update1(myframe)).grid(row=5,column=2)
def update1(myframe):
    x=ae.get()
    x=int(x)
    y=be.get()
    z=ce.get()
    if unam=='divyajohn@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unam=='chandrasekar@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unam=='rajalakshmi@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()

def delete(myframe,username):
    global unh
    unh=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    dele=Label(myframe,text='Do You Want An Entire Record To Be Deleted?').grid(row=2,column=2)
    yese=Button(myframe,text='YES',command=lambda :yes(myframe)).grid(row=2,column=4)
    noe=Button(myframe,text='NO',command=lambda :nono(myframe)).grid(row=2,column=6)
def nono(myframe):
    global xee,yee
    xe=Label(myframe,text='Enter SNO. of the record').grid(row=4,column=2)
    ye=Label(myframe,text='Enter type of data to be deleted').grid(row=5,column=2)
    xee=Entry(myframe,bd=5)
    xee.grid(row=4,column=3)
    yee=Entry(myframe,bd=5)
    yee.grid(row=5,column=3)
    xc=Button(myframe,text='DELETE',command=lambda :nono1(myframe)).grid(row=7,column=2)
def nono1(myframe):
    xec=xee.get()
    xec=int(xec)
    yec=yee.get()
    if unh=='divyajohn@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unh=='chandrasekar@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unh=='rajalakshmi@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()

def yes(myframe):
    global zee
    ze=Label(myframe,text='Enter the SNO. of the record to be deleted').grid(row=4,column=2)
    zee=Entry(myframe,bd=5)
    zee.grid(row=4,column=3)
    cv=Button(myframe,text='DELETE RECORD',command=lambda :yes1(myframe)).grid(row=5,column=2)
def yes1(myframe):
    nb=zee.get()
    if unh=='divyajohn@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    if unh=='rajalakshmi@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    if unh=='chandrasekar@ssn.edu.in':
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()


def login1(myframe):            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='chandrasekar@ssn.edu.in' and passw=='chandru'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
#cal=Calendar(myframe, selectmode = 'day',
         #              year = 2020, month = 5,
         #      day = 22)
        #cal.pack()
        column=len(l[1])
        mentees=main.T1
        records=mentees.inorder(main.root1,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'chandrasekar@ssn.edu.in'))
        f.place(relx=0,rely=0.1)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'chandrasekar@ssn.edu.in'))
        g.place(relx=0,rely=0.3)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'chandrasekar@ssn.edu.in'))
        h.place(relx=0,rely=0.5)
        
        
    elif (user=='rajalakshmi@ssn.edu.in' and passw=='raji'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
        column=len(l[1])
        mentees=main.T2
        records=mentees.inorder(main.root2,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'rajalakshmi@ssn.edu.in'))
        f.place(relx=0,rely=0.1)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'rajalakshmi@ssn.edu.in'))
        g.place(relx=0,rely=0.3)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'rajalakshmi@ssn.edu.in'))
        h.place(relx=0,rely=0.5)
        
      
    elif (user=='divyajohn@ssn.edu.in' and passw=='dj'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
        column=len(l[1])
        mentees=main.T3
        records=mentees.inorder(main.root3,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'divyajohn@ssn.edu.in'))
        f.place(relx=0,rely=0.1)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'divyajohn@ssn.edu.in'))
        g.place(relx=0,rely=0.3)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'divyajohn@ssn.edu.in'))
        h.place(relx=0,rely=0.5)
    else:
        messagebox.showinfo("","incorrect")
def raja(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    for i in range(0,21):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
def chandra(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    for i in range(21,42):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
def dj(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    
    column=len(l[1])
    for i in range(42,63):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
    
def login2(myframe):
    
    user2=entry1.get()
    passw2=entry2.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    
    if user2=='' and passw2=='':
        messagebox.showinfo("","blank invalid")
    elif user2=='manager' and passw2=='123':
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0)
        
        b1=Button(myframe,text='ACADEMIC REPORT',width=0)
        
        b1.grid(row=0,column=1,padx=10,pady=10)
        b2=Button(myframe,text='Chandrasekar',width=0,command=lambda:chandra(myframe))
        b2.grid(row=0,column=2,padx=10,pady=10)
        b=Button(myframe,text='Rajalakshmi',width=0,command=lambda:raja(myframe))
        b.grid(row=0,column=3,padx=10,pady=10)
        b3=Button(myframe,text='Divya John',width=0,command=lambda:dj(myframe))
        b3.grid(row=0,column=4,padx=10,pady=10)

def back(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda:open2(myframe))        # creating buttons for manager, mentor , mentee
    mybutton1.grid(row=1,column=0,padx=10,pady=10)
    mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
    mybutton2.grid(row=1,column=1,padx=10,pady=10)
    mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open(myframe))    
    mybutton3.grid(row=1,column=2,padx=10,pady=10)
def openx(myframe):
    
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
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda: login(myframe)).place(relx=0.7,rely=1)
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
        
def open2(myframe):
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
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login2(myframe)).place(relx=0.7,rely=1)


mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open2(myframe))        # creating buttons for manager, mentor , mentee
mybutton1.grid(row=4,column=0,padx=10,pady=10)
mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
mybutton2.grid(row=4,column=1,padx=10,pady=10)
mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :openx(myframe))    
mybutton3.grid(row=4,column=2,padx=10,pady=10)

m.mainloop()
