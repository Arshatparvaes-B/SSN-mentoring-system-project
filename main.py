import csv
import AVLTree
import LinkedList

f1=open(r"C:\Users\User\Desktop\NF2\2nd sem\for project 3\first20.txt","r")
f2=open(r"C:\Users\User\Desktop\NF2\2nd sem\for project 3\second20.txt","r")
f3=open(r"C:\Users\User\Desktop\NF2\2nd sem\for project 3\third20.txt","r")

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

T1=AVLTree.AVL1()
T2=AVLTree.AVL1()
T3=AVLTree.AVL1()

root=None
for i in l1:
    root=T1.insert(root,int(i[0]),i)
l1=T1.inorder(root)


root=None
for i in l2:
    root=T2.insert(root,int(i[0]),i)
l2=T2.inorder(root,l=[])


root=None
for i in l3:
    root=T3.insert(root,int(i[0]),i)
l3=T3.inorder(root,l=[])

menteementor=LinkedList.LinkedList()
a="chandru"
b="raji"
c="divya"
menteementor.append(a)
menteementor.append(T1)
menteementor.append(b)
menteementor.append(T2)
menteementor.append(c)
menteementor.append(T3)





