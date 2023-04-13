from tkinter import *

window=Tk()
window.geometry("400x500")
window.title("Simple Calculator")

lab1=Label(window,text="Enter 1st Number:")
lab1.place(x=30,y=50)
lab2=Label(window,text="Enter 2nd Number:")
lab2.place(x=30,y=100)
lab3=Label(window,text="Result:")
lab3.place(x=120,y=150)
t1=Entry()
t1.place(x=150,y=50)
t2=Entry()
t2.place(x=150,y=100)
t3=Entry()
t3.place(x=180,y=150)
def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1+num2
  t3.insert(END, str(sum))
b1=Button(window,text="Add",command=add)
b1.place(x=50,y=200)


  