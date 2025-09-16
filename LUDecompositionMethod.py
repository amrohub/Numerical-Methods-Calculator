import tkinter as tk
import pandas as pd
import customtkinter as ctk

# Create the main window
calc = tk.Tk()
calc.title("LU Decomposition Method")
calc.resizable(0,0)

# Main Function
def solve_Equations():
    a11=float(n1.get())
    a12=float(n2.get())
    a13=float(n3.get())
    a21=float(n4.get())
    a22=float(n5.get())
    a23=float(n6.get())
    a31=float(n7.get())
    a32=float(n8.get())
    a33=float(n9.get())
    b1=float(n10.get())
    b2=float(n11.get())
    b3=float(n12.get())

    a =[
        [a11,a12,a13],
        [a21,a22,a23],
        [a31,a32,a33]]

    k21 =a21/a11
    k31 =a31/a11

    m0=[
        [a11  ,  a12          ,  a13],
        [0.0  ,  -k21*a12+a22  ,  -k21*a13+a23],
        [0.0  ,  -k31*a12+a32  ,  -k31*a13+a33]]

    k32=m0[2][1]/m0[1][1]

    U=[
        {'0':a11  ,  '1':a12          ,  '2':a13},
        {'0':"0"  ,  '1':-k21*a12+a22  ,  '2':-k21*a13+a23},
        {'0':"0"  ,  '1':"0"          ,  '2':-k32*m0[1][2]+m0[2][2]}]

    U_df = pd.DataFrame(U,columns = ['0','1','2'], index = ['','','']).rename(columns = {'0':'','1':'','2':'' })

    L=[
        {'0': "1"  ,  '1': "0"  ,  '2': "0"},
        {'0': k21  ,  '1': "1"  ,  '2': "0"},
        {'0': k31  ,  '1': k32  ,  '2': "1"}]

    L_df = pd.DataFrame(L,columns = ['0','1','2'], index = ['','','']).rename(columns = {'0':'','1':'','2':'' })

    c1 = b1 
    c2 = b2 - (k21*c1)
    c3 = b3 - (k31*c1) - (k32*c2)

    x3 = c3 / (-k32*m0[1][2]+m0[2][2])
    x2 = (c2 - (-k21*a13+a23)*x3) / (-k21*a12+a22)
    x1 = (c1 - (a13*x3)-(x2*a12) ) / a11

    d1 = tk.Label(calc,
                  bg="#343638",
                  fg="white",
                  text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=4,column=1,padx=7,pady=7,columnspan=6)
   
    d1 = tk.Label(calc,
                  text=(U_df),
                  bg="#343638",
                  fg="white",
                  font=('Montserrat', 12, 'bold')).grid(row=4,column=1,padx=7,pady=7,columnspan=6)
   
    d2 = tk.Label(calc,
                  bg="#343638",
                  fg="white",
                  text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=5,column=1,padx=7,pady=7,columnspan=6)
   
    d2 = tk.Label(calc,
                  text=(L_df),
                  bg="#343638",
                  fg="white",
                  font=('Montserrat', 12, 'bold')).grid(row=5,column=1,padx=7,pady=7,columnspan=6)
    
    d3 = tk.Label(calc,
                  bg="#343638",
                  fg="white",
                  text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=6,column=1,padx=7,pady=7,columnspan=6)
   
    d3 = tk.Label(calc,
                  text=(f"c1 = {b1}, c1 = {c1} \n{k21}c1 + c2 = {b1}, c2 = {c2}\n{k31}c1 + ({k32})c2 + c3 = {b3}, c3 = {c3}"),
                  bg="#343638",
                  fg="white",
                  font=('Montserrat', 12, 'bold')).grid(row=6,column=1,padx=7,pady=7,columnspan=6)
    
    d4 = tk.Label(calc,
                  bg="#343638",
                  fg="white",
                  text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=7,column=1,padx=7,pady=7,columnspan=6)
   
    d4 = tk.Label(calc,
                  text=(f"{a11}x1 + ({a12})x2 + ({a13})x3 = {c1}, x1 = {x1} \n{-k21*a12+a22}x2 + ({-k21*a13+a23})x3 = {c2}, x2 = {x2}\n{-k32*m0[1][2]+m0[2][2]}x3 = {c3}, x3 = {x3}"),
                  bg="#343638",
                  fg="white",
                  font=('Montserrat', 12, 'bold')).grid(row=7,column=1,padx=7,pady=7,columnspan=6)

# Main Labels
txt0 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='    Matrix Formula:    ', 
                     borderwidth=5 ,
                     font=('Montserrat', 20, 'bold'),padx=20 ,pady=10).grid(row=0,column=0)

txt1 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='[ a11     a12     a13 ]     [b1]',
                     font=('Montserrat', 15, 'bold'), 
                     borderwidth=5 ,padx=20 ,pady=10).grid(row=1,column=0)

txt2 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text=' [ a21     a22     a23 ]     [b2]',
                     font=('Montserrat', 15, 'bold'), 
                     borderwidth=5 ,padx=20 ,pady=10).grid(row=2,column=0)

txt3 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text=' [ a31     a32     a33 ]     [b3]',
                     font=('Montserrat', 15, 'bold'), 
                     borderwidth=5 ,padx=20 ,pady=10).grid(row=3,column=0)

lbl1 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      a11', 
                     font=('Montserrat', 10, 'bold')).grid(row=1,column=1)

lbl2 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      a12', 
                     font=('Montserrat', 10, 'bold')).grid(row=1,column=3)

lbl3 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      a13', 
                     font=('Montserrat', 10, 'bold')).grid(row=1,column=5)

lbl20 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      b1', 
                     font=('Montserrat', 10, 'bold')).grid(row=1,column=7)

lbl4 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a21',font=('Montserrat', 10, 'bold')).grid(row=2,column=1)

lbl5 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a22',
                     font=('Montserrat', 10, 'bold')).grid(row=2,column=3)

lbl6 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a23', 
                     font=('Montserrat', 10, 'bold')).grid(row=2,column=5)

lbl21 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      b2', 
                     font=('Montserrat', 10, 'bold')).grid(row=2,column=7)

lbl7 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a31', 
                     font=('Montserrat', 10, 'bold')).grid(row=3,column=1)

lbl8 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a32', 
                     font=('Montserrat', 10, 'bold')).grid(row=3,column=3)

lbl9 = tk.Label(calc, 
                     bg="#343638", 
                     fg="white", 
                     text='      a33', 
                     font=('Montserrat', 10, 'bold')).grid(row=3,column=5)

lbl22 = tk.Label(calc,
                     bg="#343638",
                     fg="white", 
                     text='      b3', 
                     font=('Montserrat', 10, 'bold')).grid(row=3,column=7)

lbl10 = tk.Label(calc,
                      bg="#343638", 
                      fg="white", 
                      text='                                             \n                                            \n             U (Upper Matrix)               \n                                                   \n                                          ', 
                      font=('Montserrat', 15, 'bold')).grid(row=4,column=0)

lbl11 = tk.Label(calc, 
                      bg="#343638",
                      fg="white", 
                      text='                                             \n                                            \n             L (Lower Matrix)               \n                                                   \n                                          ', 
                      font=('Montserrat', 15, 'bold')).grid(row=5,column=0)

lbl12 = tk.Label(calc, 
                      bg="#343638",
                      fg="white", 
                      text='                                             \n                                            \n             Lc = b              \n                                                   \n                                          ', 
                      font=('Montserrat', 15, 'bold')).grid(row=6,column=0)

lbl13 = tk.Label(calc, 
                      bg="#343638",
                      fg="white", 
                      text='                                             \n                                            \n             Ux = c              \n                                                   \n                                          ', 
                      font=('Montserrat', 15, 'bold')).grid(row=7,column=0)

# Create a Solve button
solve_button= ctk.CTkButton(  calc, 
                              bg_color='#343638',
                              fg_color='white',
                              text='Calculate',
                              text_color='#343638',
                              font=('Montserrat', 20, 'bold'),command=solve_Equations).grid(row=0,column=1,padx=7,pady=7,columnspan=6)

# Create input fields for variables
e1= tk.Entry(calc,borderwidth=1 , width= 5)
e1.grid(row=1,column=2,padx=10 ,pady=5)
n1=tk.DoubleVar()
n1.set(2)
e1["textvariable"] = n1

e2= tk.Entry(calc,borderwidth=1 , width= 5)
e2.grid(row=1,column=4,padx=10 ,pady=5)
n2=tk.DoubleVar()
n2.set(0)
e2["textvariable"] = n2

e3= tk.Entry(calc,borderwidth=1 , width= 5)
e3.grid(row=1,column=6,padx=10 ,pady=5)
n3=tk.DoubleVar()
n3.set(1)
e3["textvariable"] = n3

e10= tk.Entry(calc,borderwidth=1 , width= 5)
e10.grid(row=1,column=8,padx=10 ,pady=5)
n10=tk.DoubleVar()
n10.set(4)
e10["textvariable"] = n10

e4= tk.Entry(calc,borderwidth=1 , width= 5)
e4.grid(row=2,column=2,padx=10 ,pady=5)
n4=tk.DoubleVar()
n4.set(2)
e4["textvariable"] = n4

e5= tk.Entry(calc,borderwidth=1 , width= 5)
e5.grid(row=2,column=4,padx=10 ,pady=5)
n5=tk.DoubleVar()
n5.set(5)
e5["textvariable"] = n5

e6= tk.Entry(calc,borderwidth=1 , width= 5)
e6.grid(row=2,column=6,padx=10 ,pady=5)
n6=tk.DoubleVar()
n6.set(-9)
e6["textvariable"] = n6

e11= tk.Entry(calc,borderwidth=1 , width= 5)
e11.grid(row=2,column=8,padx=10 ,pady=5)
n11=tk.DoubleVar()
n11.set(4)
e11["textvariable"] = n11

e7= tk.Entry(calc,borderwidth=1 , width= 5)
e7.grid(row=3,column=2,padx=10 ,pady=5)
n7=tk.DoubleVar()
n7.set(-5)
e7["textvariable"] = n7

e8= tk.Entry(calc,borderwidth=1 , width= 5)
e8.grid(row=3,column=4,padx=10 ,pady=5)
n8=tk.DoubleVar()
n8.set(7)
e8["textvariable"] = n8

e9= tk.Entry(calc,borderwidth=1 , width= 5)
e9.grid(row=3,column=6,padx=10 ,pady=5)
n9=tk.DoubleVar()
n9.set(4)
e9["textvariable"] = n9

e12= tk.Entry(calc,borderwidth=1 , width= 5)
e12.grid(row=3,column=8,padx=10 ,pady=5)
n12=tk.DoubleVar()
n12.set(4)
e12["textvariable"] = n12

calc.config(bg="#343638") 
calc.mainloop()