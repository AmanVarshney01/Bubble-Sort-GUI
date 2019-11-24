from tkinter import *

root = Tk()

input1 = Label(root, text="Enter Numbers :").pack()

def Bubble_Sort(mylist):
    while True:
        corrected = False
        for i in range(0, len(mylist) - 1):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1] , mylist[i]
                corrected = True
        if not corrected:
            return mylist

mylist = []

def appendlist():
    value = int(numinput.get())
    mylist.append(value)
    numinput.delete(0, END)
    label = Label(root, text=str(Bubble_Sort(mylist))).pack()

numinput = Entry(root)

numinput.pack()

button = Button(root, text='Submit', command=appendlist).pack()

root.mainloop()


print(Bubble_Sort(mylist))