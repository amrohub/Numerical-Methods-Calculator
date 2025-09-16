from math import *
import tkinter as tk
from decimal import *
from sympy import symbols, Matrix
import customtkinter as ctk

# Create the main window
window = tk.Tk()
window.title("Cramer Method")
window.resizable(0,0)

# Define the variables
x1, x2, x3 = symbols('x1 x2 x3')

# Main Labels
txt0 = tk.Label(window,bg="#343638",fg="white", text='    Matrix Formula:    ', borderwidth=5 ,font=('Montserrat', 20, 'bold'),padx=20 ,pady=10).grid(row=0,column=0)
txt1 = tk.Label(window,bg="#343638",fg="white", text='[ a11     a12     a13     |     b11]',font=('Montserrat', 15, 'bold'), borderwidth=5 ,padx=20 ,pady=10).grid(row=1,column=0)
txt2 = tk.Label(window,bg="#343638",fg="white", text='[ a21     a22     a23     |     b12]',font=('Montserrat', 15, 'bold'), borderwidth=5 ,padx=20 ,pady=10).grid(row=2,column=0)
txt3 = tk.Label(window,bg="#343638",fg="white", text='[ a31     a32     a33     |     b13]',font=('Montserrat', 15, 'bold'), borderwidth=5 ,padx=20 ,pady=10).grid(row=3,column=0)
lbl1 = tk.Label(window,bg="#343638",fg="white", text='      a11',font=('Montserrat', 10, 'bold')).grid(row=1,column=1)
lbl2 = tk.Label(window,bg="#343638",fg="white", text='      a12',font=('Montserrat', 10, 'bold')).grid(row=1,column=3)
lbl3 = tk.Label(window,bg="#343638",fg="white", text='      a13',font=('Montserrat', 10, 'bold')).grid(row=1,column=5)
lbl10 = tk.Label(window,bg="#343638",fg="white", text='      b11',font=('Montserrat', 10, 'bold')).grid(row=1,column=7)
lbl4 = tk.Label(window,bg="#343638",fg="white", text='      a21',font=('Montserrat', 10, 'bold')).grid(row=2,column=1)
lbl5 = tk.Label(window,bg="#343638",fg="white", text='      a22',font=('Montserrat', 10, 'bold')).grid(row=2,column=3)
lbl6 = tk.Label(window,bg="#343638",fg="white", text='      a23',font=('Montserrat', 10, 'bold')).grid(row=2,column=5)
lbl11 = tk.Label(window,bg="#343638",fg="white", text='      b12',font=('Montserrat', 10, 'bold')).grid(row=2,column=7)
lbl7 = tk.Label(window,bg="#343638",fg="white", text='      a31',font=('Montserrat', 10, 'bold')).grid(row=3,column=1)
lbl8 = tk.Label(window,bg="#343638",fg="white", text='      a32',font=('Montserrat', 10, 'bold')).grid(row=3,column=3)
lbl9 = tk.Label(window,bg="#343638",fg="white", text='      a33',font=('Montserrat', 10, 'bold')).grid(row=3,column=5)
lbl12 = tk.Label(window,bg="#343638",fg="white", text='      b13',font=('Montserrat', 10, 'bold')).grid(row=3,column=7)
lbl13 = tk.Label(window,bg="#343638",fg="white", text='                                             \n                                            \n             Cramer Rule Solution:               \n                                                   \n                                          ',font=('Montserrat', 15, 'bold')).grid(row=4,column=0)

# Main input Widgets
e1= tk.Entry(window,borderwidth=1 , width= 5)
e1.grid(row=1,column=2,padx=10 ,pady=5)
n1=tk.DoubleVar()
n1.set(2)
e1["textvariable"] = n1

e2= tk.Entry(window,borderwidth=1 , width= 5)
e2.grid(row=1,column=4,padx=10 ,pady=5)
n2=tk.DoubleVar()
n2.set(0)
e2["textvariable"] = n2

e3= tk.Entry(window,borderwidth=1 , width= 5)
e3.grid(row=1,column=6,padx=10 ,pady=5)
n3=tk.DoubleVar()
n3.set(1)
e3["textvariable"] = n3

e10= tk.Entry(window,borderwidth=1 , width= 5)
e10.grid(row=1,column=8,padx=10 ,pady=5)
n10=tk.DoubleVar()
n10.set(4)
e10["textvariable"] = n10

e4= tk.Entry(window,borderwidth=1 , width= 5)
e4.grid(row=2,column=2,padx=10 ,pady=5)
n4=tk.DoubleVar()
n4.set(2)
e4["textvariable"] = n4

e5= tk.Entry(window,borderwidth=1 , width= 5)
e5.grid(row=2,column=4,padx=10 ,pady=5)
n5=tk.DoubleVar()
n5.set(5)
e5["textvariable"] = n5

e6= tk.Entry(window,borderwidth=1 , width= 5)
e6.grid(row=2,column=6,padx=10 ,pady=5)
n6=tk.DoubleVar()
n6.set(-9)
e6["textvariable"] = n6

e11= tk.Entry(window,borderwidth=1 , width= 5)
e11.grid(row=2,column=8,padx=10 ,pady=5)
n11=tk.DoubleVar()
n11.set(4)
e11["textvariable"] = n11

e7= tk.Entry(window,borderwidth=1 , width= 5)
e7.grid(row=3,column=2,padx=10 ,pady=5)
n7=tk.DoubleVar()
n7.set(-5)
e7["textvariable"] = n7

e8= tk.Entry(window,borderwidth=1 , width= 5)
e8.grid(row=3,column=4,padx=10 ,pady=5)
n8=tk.DoubleVar()
n8.set(7)
e8["textvariable"] = n8

e9= tk.Entry(window,borderwidth=1 , width= 5)
e9.grid(row=3,column=6,padx=10 ,pady=5)
n9=tk.DoubleVar()
n9.set(4)
e9["textvariable"] = n9

e12= tk.Entry(window,borderwidth=1 , width= 5)
e12.grid(row=3,column=8,padx=10 ,pady=5)
n12=tk.DoubleVar()
n12.set(4)
e12["textvariable"] = n12

def round_val(x, r):
    getcontext().prec = 56
    factor = Decimal(1) / 10 ** r
    num1 = Decimal(x).quantize(factor, rounding=ROUND_HALF_EVEN)
    return num1

def solve():
    a11=float(n1.get())
    a12=float(n2.get())
    a13=float(n3.get())
    a21=float(n4.get())
    a22=float(n5.get())
    a23=float(n6.get())
    a31=float(n7.get())
    a32=float(n8.get())
    a33=float(n9.get())
    b11=float(n10.get())
    b12=float(n11.get())
    b13=float(n12.get())

    A = Matrix([
        [a11,a12,a13],
        [a21,a22,a23],
        [a31,a32,a33]])

    B = Matrix(
        [b11,b12,b13])

    det_A = A.det()

    A1 = A.copy()
    A1[:, 0] = B
    A2 = A.copy()
    A2[:, 1] = B
    A3 = A.copy()
    A3[:, 2] = B

    # Calculate determinants of matrices A1, A2, A3
    det_A1 = A1.det()
    det_A2 = A2.det()
    det_A3 = A3.det()

    # Use Cramer's Rule to find the solutions
    x1_solution = det_A1 / det_A
    x2_solution = det_A2 / det_A
    x3_solution = det_A3 / det_A
    result_Label['text'] = f"x1 = A1/A = {int(x1_solution)}\nx2 = A2/A = {int(x2_solution)}\nx3 = A3/A = {int(x3_solution)}"

result_Label= tk.Label(window,
                          text=" ",                 
                          bg="#2a2d2e",
                          fg="white",
                          font=('Montserrat', 20, 'bold'))
result_Label.grid(row=4,column=1,padx=7,pady=7,columnspan=6)
# Create a Solve button
solve_button= ctk.CTkButton(window, 
                  bg_color='#343638',
                  fg_color='white',
                  text='Calculate',
                  text_color='#343638',
                  font=('Montserrat', 20, 'bold'),command=solve).grid(row=0,column=1,padx=7,pady=7,columnspan=6)

window.config(bg="#343638")
window.mainloop()