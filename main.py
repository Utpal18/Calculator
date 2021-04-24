'''from tkinter import *

window=Tk()

#Functions

def button_click(number):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))

def clear():
    e1.delete(0,END)


#Buttons
e1=Entry(window,width=45,borderwidth=4,font=("Times New Roman",24))
e1.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

b_ac=Button(window,text="AC",padx=19,pady=10,bg="red",fg="white",command=clear())
b_ac.grid(row=1,column=3)

b1=Button(window,text="1",padx=30,pady=20,command=lambda :button_click(1))
b1.grid(row=4,column=0)

b2=Button(window,text="2",padx=30,pady=20,command=lambda :button_click(2))
b2.grid(row=4,column=1)

b3=Button(window,text="3",padx=30,pady=20,command=lambda :button_click(3))
b3.grid(row=4,column=2)

b4=Button(window,text="4",padx=30,pady=20,command=lambda :button_click(4))
b4.grid(row=3,column=0)

b5=Button(window,text="5",padx=30,pady=20,command=lambda :button_click(5))
b5.grid(row=3,column=1)

b6=Button(window,text="6",padx=30,pady=20,command=lambda :button_click(6))
b6.grid(row=3,column=2)

b7=Button(window,text="7",padx=30,pady=20,command=lambda :button_click(7))
b7.grid(row=2,column=0)

b8=Button(window,text="8",padx=30,pady=20,command=lambda :button_click(8))
b8.grid(row=2,column=1)

b9=Button(window,text="9",padx=30,pady=20,command=lambda :button_click(9))
b9.grid(row=2,column=2)

b0=Button(window,text="0",padx=30,pady=20,command=lambda :button_click(0))
b0.grid(row=5,column=1)

b_dec=Button(window,text=".",padx=31,pady=20)
b_dec.grid(row=5,column=0)

b_equals=Button(window,text="=",padx=29,pady=20)
b_equals.grid(row=5,column=2)


b_plus=Button(window,text="+",padx=23,pady=20)
b_plus.grid(row=2,column=3)

b_minus=Button(window,text="-",padx=25,pady=20)
b_minus.grid(row=3,column=3)

b_mul=Button(window,text="X",padx=24,pady=20)
b_mul.grid(row=4,column=3)

b_div=Button(window,text="/",padx=25,pady=20)
b_div.grid(row=5,column=3)
window.mainloop()
'''