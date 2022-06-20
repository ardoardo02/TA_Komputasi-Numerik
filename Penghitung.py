from tkinter import *
from numpy import *
from functools import partial
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

test = Tk()


#Mencari Nilai Y
def NilaiY(root):
    root.destroy()
    NilaiY = Tk()
    NilaiY.title('Mencari Nilai Y')
    NilaiY.geometry("310x275")
    NilaiY.configure(bg='white')

    text = Label(NilaiY,text=' Masukkan Data',padx=25,bg='white',fg='black',font=('Times',20,'bold'))
    text.grid(row=1,column=1,columnspan=4)

    X = Label(NilaiY,text='Nilai t   =',bg='white',fg='red',font=('Times',15,'bold'))
    X.grid(row=3,column=1)

    X1 = Label(NilaiY,text='(t1, y1) =',bg='white',fg='black',font=('Times',15,'bold'))
    X1.grid(row=4,column=1)

    X2 = Label(NilaiY,text='(t2, y2) =',bg='white',fg='black',font=('Times',15,'bold'))
    X2.grid(row=5,column=1)

    X3 = Label(NilaiY,text='(t3, y3) =',bg='white',fg='black',font=('Times',15,'bold'))
    X3.grid(row=6,column=1)

    Y1 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y1.grid(row=4,column=3)

    Y2 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y2.grid(row=5,column=3)

    Y3 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y3.grid(row=6,column=3)

    hasil = Label(NilaiY,text='Nilai y',bg='white',fg='black',font=('Times',15,'bold'))
    hasil.grid(row=8,column=1)

    blank1 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank1.grid(row=2,column=1)
    blank2 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank2.grid(row=7,column=1)

    X = Entry(NilaiY,width=15,borderwidth=5)
    X.grid(row=3,column=2)
    X.get()

    X1 = Entry(NilaiY,width=15,borderwidth=5)
    X1.grid(row=4,column=2)
    X1.get()

    X2 = Entry(NilaiY,width=15,borderwidth=5)
    X2.grid(row=5,column=2)
    X2.get()

    X3 = Entry(NilaiY,width=15,borderwidth=5)
    X3.grid(row=6,column=2)
    X3.get()

    Y1 = Entry(NilaiY,width=15,borderwidth=5)
    Y1.grid(row=4,column=4)
    Y1.get()

    Y2 = Entry(NilaiY,width=15,borderwidth=5)
    Y2.grid(row=5,column=4)
    Y2.get()

    Y3 = Entry(NilaiY,width=15,borderwidth=5)
    Y3.grid(row=6,column=4)
    Y3.get()

    hasil = Entry(NilaiY,width=25,borderwidth=5)
    hasil.grid(row=9,column=1,columnspan=2)

    exBtn = Button(NilaiY, text='Kembali',padx=15, bg='black', fg='white', command= partial(menu,1,NilaiY))
    exBtn.grid(row=9, column=4)
    button1 = Button(NilaiY,text='Hitung nilai y', bg='green', fg='white', command= partial(RumusY,X,X1,X2,X3,Y1,Y2,Y3,hasil))
    button1.grid(row=8, column=4)

def RumusY(X,X1,X2,X3,Y1,Y2,Y3,hasil):
    X = float(X.get())
    X1 = float(X1.get())
    X2 = float(X2.get())
    X3 = float(X3.get())
    Y1 = float(Y1.get())
    Y2 = float(Y2.get())
    Y3 = float(Y3.get())

    NilaiY = (Y1*(X-X2)*(X-X3)) / ((X1-X2)*(X1-X3)) + (Y2*(X-X1)*(X-X3)) / ((X2-X1)*(X2-X3)) + (Y3*(X-X1)*(X-X2)) / ((X3-X1)*(X3-X2))
    hasil.delete(0, END)
    hasil.insert(0, NilaiY)


#Mencari Nilai Y1
def NilaiY1(root):
    root.destroy()
    NilaiY = Tk()
    NilaiY.title('Mencari Nilai Y1')
    NilaiY.geometry("310x275")
    NilaiY.configure(bg='white')

    text = Label(NilaiY,text=' Masukkan Data',padx=25,bg='white',fg='black',font=('Times',20,'bold'))
    text.grid(row=1,column=1,columnspan=4)

    X = Label(NilaiY,text='(t, y)     =',bg='white',fg='black',font=('Times',15,'bold'))
    X.grid(row=3,column=1)

    X1 = Label(NilaiY,text='Nilai t1 =',bg='white',fg='red',font=('Times',15,'bold'))
    X1.grid(row=4,column=1)

    X2 = Label(NilaiY,text='(t2, y2) =',bg='white',fg='black',font=('Times',15,'bold'))
    X2.grid(row=5,column=1)

    X3 = Label(NilaiY,text='(t3, y3) =',bg='white',fg='black',font=('Times',15,'bold'))
    X3.grid(row=6,column=1)

    Y = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y.grid(row=3,column=3)

    Y2 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y2.grid(row=5,column=3)

    Y3 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y3.grid(row=6,column=3)

    hasil = Label(NilaiY,text='Nilai y1',bg='white',fg='black',font=('Times',15,'bold'))
    hasil.grid(row=8,column=1)

    blank1 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank1.grid(row=2,column=1)
    blank2 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank2.grid(row=7,column=1)
    
    X = Entry(NilaiY,width=15,borderwidth=5)
    X.grid(row=3,column=2)
    X.get()

    X1 = Entry(NilaiY,width=15,borderwidth=5)
    X1.grid(row=4,column=2)
    X1.get()

    X2 = Entry(NilaiY,width=15,borderwidth=5)
    X2.grid(row=5,column=2)
    X2.get()

    X3 = Entry(NilaiY,width=15,borderwidth=5)
    X3.grid(row=6,column=2)
    X3.get()

    Y = Entry(NilaiY,width=15,borderwidth=5)
    Y.grid(row=3,column=4)
    Y.get()

    Y2 = Entry(NilaiY,width=15,borderwidth=5)
    Y2.grid(row=5,column=4)
    Y2.get()

    Y3 = Entry(NilaiY,width=15,borderwidth=5)
    Y3.grid(row=6,column=4)
    Y3.get()

    hasil = Entry(NilaiY,width=25,borderwidth=5)
    hasil.grid(row=9,column=1,columnspan=2)

    exBtn = Button(NilaiY, text='Kembali',padx=18, bg='black', fg='white', command= partial(menu,1,NilaiY))
    exBtn.grid(row=9, column=4)
    button1 = Button(NilaiY,text='Hitung nilai y1', bg='green', fg='white', command= partial(RumusY1,X,X1,X2,X3,Y,Y2,Y3,hasil))
    button1.grid(row=8, column=4)

def RumusY1(A,A1,A2,A3,B,B2,B3,hasil):
    X = float(A.get())
    X1 = float(A3.get())
    X2 = float(A2.get())
    X3 = float(A1.get())
    Y = float(B.get())
    Y1 = float(B3.get())
    Y2 = float(B2.get())

    NilaiY = (Y*(X3-X1)*(X3-X2)) / ((X-X1)*(X-X2)) + (Y1*(X3-X)*(X3-X2)) / ((X1-X)*(X1-X2)) + (Y2*(X3-X)*(X3-X1)) / ((X2-X)*(X2-X1))
    hasil.delete(0, END)
    hasil.insert(0, NilaiY)


#Mencari Nilai Y2
def NilaiY2(root):
    root.destroy()
    NilaiY = Tk()
    NilaiY.title('Mencari Nilai Y2')
    NilaiY.geometry("310x275")
    NilaiY.configure(bg='white')

    text = Label(NilaiY,text=' Masukkan Data',padx=25,bg='white',fg='black',font=('Times',20,'bold'))
    text.grid(row=1,column=1,columnspan=4)

    X = Label(NilaiY,text='(t, y)     =',bg='white',fg='black',font=('Times',15,'bold'))
    X.grid(row=3,column=1)

    X1 = Label(NilaiY,text='(t1, y1) =',bg='white',fg='black',font=('Times',15,'bold'))
    X1.grid(row=4,column=1)

    X2 = Label(NilaiY,text='Nilai t2 =',bg='white',fg='red',font=('Times',15,'bold'))
    X2.grid(row=5,column=1)

    X3 = Label(NilaiY,text='(t2, y2) =',bg='white',fg='black',font=('Times',15,'bold'))
    X3.grid(row=6,column=1)

    Y = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y.grid(row=3,column=3)

    Y1 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y1.grid(row=4,column=3)

    Y3 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y3.grid(row=6,column=3)

    hasil = Label(NilaiY,text='Nilai y2',bg='white',fg='black',font=('Times',15,'bold'))
    hasil.grid(row=8,column=1)

    blank1 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank1.grid(row=2,column=1)
    blank2 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank2.grid(row=7,column=1)

    X = Entry(NilaiY,width=15,borderwidth=5)
    X.grid(row=3,column=2)
    X.get()

    X1 = Entry(NilaiY,width=15,borderwidth=5)
    X1.grid(row=4,column=2)
    X1.get()

    X2 = Entry(NilaiY,width=15,borderwidth=5)
    X2.grid(row=5,column=2)
    X2.get()

    X3 = Entry(NilaiY,width=15,borderwidth=5)
    X3.grid(row=6,column=2)
    X3.get()

    Y = Entry(NilaiY,width=15,borderwidth=5)
    Y.grid(row=3,column=4)
    Y.get()

    Y1 = Entry(NilaiY,width=15,borderwidth=5)
    Y1.grid(row=4,column=4)
    Y1.get()

    Y3 = Entry(NilaiY,width=15,borderwidth=5)
    Y3.grid(row=6,column=4)
    Y3.get()

    hasil = Entry(NilaiY,width=25,borderwidth=5)
    hasil.grid(row=9,column=1,columnspan=2)

    exBtn = Button(NilaiY, text='Kembali',padx=18, bg='black', fg='white', command= partial(menu,1,NilaiY))
    exBtn.grid(row=9, column=4)
    button1 = Button(NilaiY,text='Hitung nilai y2', bg='green', fg='white', command= partial(RumusY2,X,X1,X2,X3,Y,Y1,Y3,hasil))
    button1.grid(row=8, column=4)

def RumusY2(A,A1,A2,A3,B,B1,B3,hasil):
    X = float(A.get())
    X1 = float(A1.get())
    X2 = float(A3.get())
    X3 = float(A2.get())
    Y = float(B.get())
    Y1 = float(B1.get())
    Y2 = float(B3.get())

    NilaiY = (Y*(X3-X1)*(X3-X2)) / ((X-X1)*(X-X2)) + (Y1*(X3-X)*(X3-X2)) / ((X1-X)*(X1-X2)) + (Y2*(X3-X)*(X3-X1)) / ((X2-X)*(X2-X1))
    hasil.delete(0, END)
    hasil.insert(0, NilaiY)


#Mencari Nilai Y3
def NilaiY3(root):
    root.destroy()
    NilaiY = Tk()
    NilaiY.title('Mencari Nilai Y3')
    NilaiY.geometry("310x275")
    NilaiY.configure(bg='white')

    text = Label(NilaiY,text=' Masukkan Data',padx=25,bg='white',fg='black',font=('Times',20,'bold'))
    text.grid(row=1,column=1,columnspan=4)

    X = Label(NilaiY,text='(t, y)     =',bg='white',fg='black',font=('Times',15,'bold'))
    X.grid(row=3,column=1)

    X1 = Label(NilaiY,text='(t1, y1) =',bg='white',fg='black',font=('Times',15,'bold'))
    X1.grid(row=4,column=1)

    X2 = Label(NilaiY,text='(t2, y2) =',bg='white',fg='black',font=('Times',15,'bold'))
    X2.grid(row=5,column=1)

    X3 = Label(NilaiY,text='Nilai t3 =',bg='white',fg='red',font=('Times',15,'bold'))
    X3.grid(row=6,column=1)

    Y = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y.grid(row=3,column=3)

    Y1 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y1.grid(row=4,column=3)

    Y2 = Label(NilaiY,text=', ',bg='white',fg='black',font=('Times',15,'bold'))
    Y2.grid(row=5,column=3)

    hasil = Label(NilaiY,text='Nilai y3',bg='white',fg='black',font=('Times',15,'bold'))
    hasil.grid(row=8,column=1)

    blank1 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank1.grid(row=2,column=1)
    blank2 = Label(NilaiY,text='',bg='white',fg='black',font=('Times',15,'bold'))
    blank2.grid(row=7,column=1)
    
    X = Entry(NilaiY,width=15,borderwidth=5)
    X.grid(row=3,column=2)
    X.get()

    X1 = Entry(NilaiY,width=15,borderwidth=5)
    X1.grid(row=4,column=2)
    X1.get()

    X2 = Entry(NilaiY,width=15,borderwidth=5)
    X2.grid(row=5,column=2)
    X2.get()

    X3 = Entry(NilaiY,width=15,borderwidth=5)
    X3.grid(row=6,column=2)
    X3.get()

    Y = Entry(NilaiY,width=15,borderwidth=5)
    Y.grid(row=3,column=4)
    Y.get()

    Y1 = Entry(NilaiY,width=15,borderwidth=5)
    Y1.grid(row=4,column=4)
    Y1.get()

    Y2 = Entry(NilaiY,width=15,borderwidth=5)
    Y2.grid(row=5,column=4)
    Y2.get()

    hasil = Entry(NilaiY,width=25,borderwidth=5)
    hasil.grid(row=9,column=1,columnspan=2)

    exBtn = Button(NilaiY, text='Kembali',padx=18, bg='black', fg='white', command= partial(menu,1,NilaiY))
    exBtn.grid(row=9, column=4)
    button1 = Button(NilaiY,text='Hitung nilai y3', bg='green', fg='white', command= partial(RumusY3,X,X1,X2,X3,Y,Y1,Y2,hasil))
    button1.grid(row=8, column=4)

def RumusY3(X,X1,X2,X3,Y,Y1,Y2,hasil):
    X = float(X.get())
    X1 = float(X1.get())
    X2 = float(X2.get())
    X3 = float(X3.get())
    Y = float(Y.get())
    Y1 = float(Y1.get())
    Y2 = float(Y2.get())

    NilaiY = (Y*(X3-X1)*(X3-X2)) / ((X-X1)*(X-X2)) + (Y1*(X3-X)*(X3-X2)) / ((X1-X)*(X1-X2)) + (Y2*(X3-X)*(X3-X1)) / ((X2-X)*(X2-X1))
    hasil.delete(0, END)
    hasil.insert(0, NilaiY)

#menu
def menu(X,wndw):
    if X == 0:
        test.destroy()
    if X > 0:
        wndw.destroy()
    root = Tk()
    root.title('Penghitung Pergerakan Sebuah Benda Padat Berbentuk Parabola')
    root.geometry("600x400")
    root.configure(bg='black')
    text1 = Label(root,text='PENGHITUNG PERGERAKAN', bg='black',font=('Arial',20,'bold'), fg='white')
    text1.place(x=105, y=30)
    text1 = Label(root,text='SEBUAH BENDA PADAT', bg='black',font=('Arial',20,'bold'), fg='white')
    text1.place(x=135, y=70)
    text1 = Label(root,text='BERBENTUK PARABOLA', bg='black',font=('Arial',20,'bold'), fg='white')
    text1.place(x=130, y=110)
    var=IntVar()
    btn1 = Button(root, text="Mencari nilai y", padx="15", font=('Helvetica',16,'bold'), command= partial(NilaiY,root))
    btn1.place(x=205,y=170)
    btn2 = Button(root, text="Mencari nilai y1", padx="9", font=('Helvetica',16,'bold'), command= partial(NilaiY1,root))
    btn2.place(x=205,y=220)
    btn3 = Button(root, text="Mencari nilai y2", padx="9", font=('Helvetica',16,'bold'), command= partial(NilaiY2,root))
    btn3.place(x=205,y=270)
    btn3 = Button(root, text="Mencari nilai y3", padx="9", font=('Helvetica',16,'bold'), command= partial(NilaiY3,root))
    btn3.place(x=205,y=320)


menu(0,None)
test.mainloop()
