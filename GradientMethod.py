import sympy as smp
from math import *
from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# Create the main window
window = ctk.CTk()
window.title("Gradient Method")
window.resizable(0,0)

def get_i():
    x_Lower = float(x_Input.get())
    return x_Lower

def get_j():
    x_Upper = float(y_Input.get())
    return x_Upper

def get_Function(x,y):
    function = str(eval(func_Input.get()))
    return function

def getpartial():
    x = smp.symbols('x')
    y = smp.symbols('y')
    ivalue = get_i()
    jvalue = get_j()
    function = get_Function(x,y)
    dfdx = smp.diff(function, x)
    dfdY = smp.diff(function, y)

    result_Label['text'] = f"df/dx: {dfdx}\ndf/dy: {dfdY}\n𝛁𝒇 = df/dx 𝒊 + df/dY 𝒋 = {ivalue} 𝒊 + {jvalue} 𝒋\n𝚹 = tan^-1({jvalue}/{ivalue}) = {round(atan(jvalue/ivalue),3)} rad\ng`(0) = {ivalue}cos({round(atan(jvalue/ivalue),3)}) + {jvalue}sin({round(atan(jvalue/ivalue),3)})= {round(ivalue*cos(round(atan(jvalue/ivalue),3)) + jvalue*sin(round(atan(jvalue/ivalue),3)),3)}"

frame1 = ctk.CTkFrame(master=window,
                      width= 300 ,
                      bg_color="transparent",
                      height= 200 )
frame1.pack(side=TOP, padx='15', pady='15')

LabelTitle = ctk.CTkLabel(frame1,
                          text='Gradient Method',
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 24, 'bold'))
LabelTitle.pack(padx='5', pady='5')

x_Label = ctk.CTkLabel(window,
                            text='𝒊',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 25, 'bold')).pack(padx='10')
x_Input = ctk.CTkEntry(window,
                            border_width=2,
                            width=200)
x_Input.pack(padx='10',pady='10')

y_Label = ctk.CTkLabel(window,
                            text='𝒋',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 25, 'bold')).pack(padx='10')
y_Input = ctk.CTkEntry(window,
                            border_width=1,
                            width=200)
y_Input.pack(padx='10',pady='10')

# Create input fields for variables
func_Label = ctk.CTkLabel(window, 
                          text="𝒇(𝒳)",
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 15, 'bold')).pack(padx='10')
func_Input = ctk.CTkEntry(window,
                          border_width=1,
                          width=200)
func_Input.pack(padx='10',pady='10')

# Create a Solve button
result_Button = ctk.CTkButton(window,
                              text='Differentiate',
                              bg_color="transparent",
                              text_color="white",
                              font=('Montserrat', 20, 'bold'),
                              command=getpartial)
result_Button.pack(padx='5',pady='5')

# Create a label to display the solution
result_Label= Label(window,
                          text=" ",                 
                          bg="#2a2d2e",
                          fg="white",
                          font=('Montserrat', 20, 'bold'))
result_Label.pack()
window.mainloop()