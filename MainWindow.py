from tkinter import *
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")
mode = "dark"

# Create main window
main = ctk.CTk()  
main.geometry("1200x700")
main.resizable(0,0)
main.title('Calculator')

# Create a button to change theme
def change():
    global mode
    if mode == "dark":
        ctk.set_appearance_mode("light")
        mode = "light"

    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"
appearance_button = ctk.CTkButton(main, text="Change Light/Dark", font=('montserrat', 16), command=change)
appearance_button.pack(pady=20,side='bottom')

# Define a background image
background_Image = PhotoImage(file="./Assets/BackGround.png")
bg_Canvas = Canvas(main, width= 1200, height=700)
bg_Canvas.pack(fill="both", expand=True)
bg_Canvas.create_image(0, 0, image = background_Image, anchor= "nw")
bg_Canvas.create_text(80, 20, text="Methods:", font=('Montserrat', 20, 'bold') , fill= "#343638")
bg_Canvas.create_text(600, 350, text="Math is fun.", font=('Montserrat', 40, 'bold') , fill= "black")

# Create buttons to navigate through calculators
def bisect():  
    import BisectionMethod
bisectButt= ctk.CTkButton(main,
                          text='Bisection Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),
                          command=bisect)

def false():  
    import FalsePositionMethod
falseButt= ctk.CTkButton(main,
                          text='False Position Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),                      
                          command=false)

def newton():  
    import NewtonMethod
newtonButt= ctk.CTkButton(main,
                          text='Newton Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),                              
                          command=newton)

def simple():  
    import SimpleFixedPointMethod
simpleButt= ctk.CTkButton(main,
                          text='Simple Fixed Point Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=simple)

def secant():  
    import SecantMethod
secantButt= ctk.CTkButton(main,
                          text='Secant Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=secant)

def gauss():  
    import GaussMethod
gaussButt= ctk.CTkButton(main,
                          text='Gauss Elimination Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=gauss)

def jordan():  
    import GaussJordanMethod
jordanButt= ctk.CTkButton(main,
                          text='Gauss Jordan Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=jordan)


def luDecomp():  
    import LUDecompositionMethod
luDecompButt= ctk.CTkButton(main,
                          text='LU Decomposition Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=luDecomp)

def cramer():  
    import CramerMethod
cramerButt= ctk.CTkButton(main,
                          text='Cramer Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=cramer)

def golden():  
    import GoldenSectionMethod
goldenButt= ctk.CTkButton(main,
                          text='Golden Section Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=golden)

def gradient():  
    import GradientMethod
gradientButt= ctk.CTkButton(main,
                          text='Conjugate Gradient Method',
                          bg_color='#343638',
                          fg_color='white',
                          text_color='#343638',
                          font=('Montserrat', 20, 'bold'),    
                          command=gradient)

butt1_window = bg_Canvas.create_window(10, 50, anchor="nw", window=bisectButt)
butt2_window = bg_Canvas.create_window(10, 90, anchor="nw", window=falseButt)
butt3_window = bg_Canvas.create_window(10, 130, anchor="nw", window=newtonButt)
butt4_window = bg_Canvas.create_window(10, 170, anchor="nw", window=simpleButt)
butt5_window = bg_Canvas.create_window(10, 210, anchor="nw", window=secantButt)
butt6_window = bg_Canvas.create_window(10, 250, anchor="nw", window=gaussButt)
butt7_window = bg_Canvas.create_window(10, 290, anchor="nw", window=jordanButt)
butt8_window = bg_Canvas.create_window(10, 330, anchor="nw", window=luDecompButt)
butt9_window = bg_Canvas.create_window(10, 370, anchor="nw", window=cramerButt)
butt10_window = bg_Canvas.create_window(10, 410, anchor="nw", window=goldenButt)
butt11_window = bg_Canvas.create_window(10, 450, anchor="nw", window=gradientButt)
main.mainloop()
 
