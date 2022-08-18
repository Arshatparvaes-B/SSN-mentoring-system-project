import csv
import avl
import linkedlist

f1=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\first20.txt","r")
f2=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\second20.txt","r")
f3=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\third20.txt","r")

r1=csv.reader(f1)
no=next(csv.reader(f1))
l1=[]
for i in csv.reader(f1):
    l1.append(i)
f1.close()

r2=csv.reader(f2)
no=next(csv.reader(f2))
l2=[]
for i in csv.reader(f2):
    l2.append(i)
f2.close()

r3=csv.reader(f3)
no=next(csv.reader(f3))
l3=[]
for i in csv.reader(f3):
    l3.append(i)
f3.close()

T1=avl.AVL1()
T2=avl.AVL1()
T3=avl.AVL1()

root=None
for i in l1:
    root=T1.insert(root,int(i[0]),i)
root1=root
root=None
for i in l2:
    root=T2.insert(root,int(i[0]),i)
root2=root
root=None
for i in l3:
    root=T3.insert(root,int(i[0]),i)
root3=root
menteementor=linkedlist.LinkedList()
a="chandrasekar@ssn.edu.in"
b="rajalakshmi@ssn.edu.in"
c="divyajohn@ssn.edu.in"
menteementor.append(a)
menteementor.append(T1)
menteementor.append(b)
menteementor.append(T2)
menteementor.append(c)
menteementor.append(T3)

f4=open(r'C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\IT-A details.txt','r')
r4=csv.reader(f4)
no=next(csv.reader(f4))
l4=[]
for i in csv.reader(f4):
    l4.append(i)
f4.close()

T4=avl.AVL1()

root=None
for i in l4:
    root=T4.insert(root,int(i[0]),i)
root4=root
