from tkinter import *

window=Tk()
window.title("Calculator")
#Functions

def button_click(number):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))

def clear():
    e1.delete(0,END)


def add():
    first_number=e1.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e1.delete(0,END)

def substract():
    first_number = e1.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e1.delete(0, END)


def multiply():
    first_number = e1.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e1.delete(0, END)


def divide():
    first_number = e1.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e1.delete(0, END)




def equal():
    second_number=e1.get()
    e1.delete(0,END)
    if math=="addition":
        e1.insert(0,int(f_num)+int(second_number))
    elif math=="substraction":
        e1.insert(0,int(f_num)-int(second_number))
    elif math == "multiply":
        e1.insert(0, int(f_num) * int(second_number))
    else:
        e1.insert(0, int(f_num) / int(second_number))
#Buttons
e1=Entry(window,borderwidth=4,font=("Times New Roman",24))
e1.grid(row=0,column=0,padx=10,pady=10,columnspan=3)



b_ac=Button(window,text="AC",padx=45,pady=20,bg="red",fg="white",command=clear)
b_ac.grid(row=5,column=0)

b1=Button(window,text="1",padx=50,pady=20,bg="grey",command=lambda :button_click(1))
b1.grid(row=4,column=0)

b2=Button(window,text="2",padx=50,pady=20,bg="grey",command=lambda :button_click(2))
b2.grid(row=4,column=1)

b3=Button(window,text="3",padx=50,pady=20,bg="grey",command=lambda :button_click(3))
b3.grid(row=4,column=2)

b4=Button(window,text="4",padx=50,pady=20,bg="grey",command=lambda :button_click(4))
b4.grid(row=3,column=0)

b5=Button(window,text="5",padx=50,pady=20,bg="grey",command=lambda :button_click(5))
b5.grid(row=3,column=1)

b6=Button(window,text="6",padx=50,pady=20,bg="grey",command=lambda :button_click(6))
b6.grid(row=3,column=2)

b7=Button(window,text="7",padx=50,pady=20,bg="grey",command=lambda :button_click(7))
b7.grid(row=2,column=0)

b8=Button(window,text="8",padx=50,pady=20,bg="grey",command=lambda :button_click(8))
b8.grid(row=2,column=1)

b9=Button(window,text="9",padx=50,pady=20,bg="grey",command=lambda :button_click(9))
b9.grid(row=2,column=2)

b0=Button(window,text="0",padx=50,pady=20,bg="grey",command=lambda :button_click(0))
b0.grid(row=5,column=1)



b_equals=Button(window,text="=",padx=50,pady=20,bg="bisque",command=equal)
b_equals.grid(row=5,column=2)


b_plus=Button(window,text="+",padx=25,pady=20,bg="silver",command=add)
b_plus.grid(row=2,column=3)

b_minus=Button(window,text="-",padx=27,pady=20,bg="silver",command=substract)
b_minus.grid(row=3,column=3)

b_mul=Button(window,text="X",padx=26,pady=20,bg="silver",command=multiply)
b_mul.grid(row=4,column=3)

b_div=Button(window,text="/",padx=27,pady=20,bg="silver",command=divide)
b_div.grid(row=5,column=3)

window.mainloop()


