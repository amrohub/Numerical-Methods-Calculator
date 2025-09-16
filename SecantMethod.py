from math import *
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# Create the main window
window = ctk.CTk()
window.title("Secant Method")
window.resizable(0,0)

def get_Xi():
    xi = float(xi_Input.get())
    return xi

def get_XMin():
    xMin = float(xMin_Input.get())
    return xMin

def get_Epsilon():
    eps = float(epsilon_Input.get())
    return eps

def get_Function(x):
    function = str(eval(func_Input.get()))
    return function

def secant_Method():
    error = 0.0 
    xi_PlusOne = 0.0
    
    xi = get_Xi() 
    xi_MinusOne = get_XMin() 
    epsilon = get_Epsilon() 
    
    for i in range(100):
        f_of_xi = get_Function(xi)
        f_of_xi_float = float(f_of_xi)
        f_of_xMin_ = get_Function(xi_MinusOne)
        f_of_xMin_float = float(f_of_xMin_)
        xi_PlusOne = xi - (f_of_xi_float * (xi_MinusOne - xi)) / (f_of_xMin_float - f_of_xi_float)
            
        if i == 1:
            table.insert(parent='', 
                         index='end', 
                         iid=i, 
                         text='',
                         values=(i, 
                                 round(xi_MinusOne,3), 
                                 round(f_of_xMin_float,3), 
                                 round(xi,3), 
                                 round(f_of_xi_float,3), " " ) )
        else:
            table.insert(parent='', 
                         index='end', 
                         iid=i, 
                         text='',
                         values=(i, 
                                 round(xi_MinusOne,3), 
                                 round(f_of_xMin_float,3), 
                                 round(xi,3), 
                                 round(f_of_xi_float,3), 
                                 f"{round(error,3)} %"))
            
        if error > epsilon or i==0:
            error   = abs((xi_PlusOne - xi) / xi_PlusOne) * 100
            xi_MinusOne = xi
            xi = xi_PlusOne
        else:
            break
    result_Label['text']=f"The Value of Required Root is : {round(xi,3)} "
    return xi

frame1 = ctk.CTkFrame(master=window,
                      width= 300 ,
                      bg_color="transparent",
                      height= 200 )
frame1.pack(side=TOP, padx='20', pady='20')

LabelTitle = ctk.CTkLabel(frame1,
                          text='Secant Method',
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 24, 'bold'))
LabelTitle.pack(padx='5', pady='5')

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

xi_Label = ctk.CTkLabel(window,
                            text='𝒳𝒊',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 15, 'bold')).pack(padx='10')
xi_Input = ctk.CTkEntry(window,
                            border_width=2,
                            width=200)
xi_Input.pack(padx='10',pady='10')

xMin_Label = ctk.CTkLabel(window,
                            text='𝒳𝒊−𝟏',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 15, 'bold')).pack(padx='10')
xMin_Input = ctk.CTkEntry(window,
                            border_width=2,
                            width=200)
xMin_Input.pack(padx='10',pady='10')

epsilon_label = ctk.CTkLabel(window,
                             text='ε',
                             bg_color="transparent",
                             text_color="white",
                             font=('Montserrat', 20, 'bold')).pack(padx='10')
epsilon_Input = ctk.CTkEntry(window,
                             border_width=1,
                             width=200)
epsilon_Input.pack(padx='10',pady='10')

# Create a table to display roots of polynomials
table = ttk.Treeview(window,
                     columns=(1,2,3,4,5,6),
                     show='headings',
                     height=8)
table.pack(fill='both', expand= True)

table.column("1",
                anchor=CENTER, 
                stretch=YES, 
                width=50)			
table.heading(1, text='𝒊')

table.column("2",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(2, text='𝒳𝒊−𝟏')

table.column("3",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(3, text='𝒇(𝒳𝒊−𝟏)')

table.column("4",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(4, text='𝒳𝒊')

table.column("5",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(5, text='𝒇(𝒳𝒊)')

table.column("6",
                anchor=CENTER, 
                stretch=YES, 
                width=100)
table.heading(6, text='𝞮')

# Define a function to select values from tables
def item_select(_):
	print(table.selection())
	for i in table.selection():
		print(table.item(i)['values'])
table.bind('<<TreeviewSelect>>', item_select)

# Create a Solve button
result_Button = ctk.CTkButton(window,
                              text='Get Root',
                              bg_color="transparent",
                              text_color="white",
                              font=('Montserrat', 20, 'bold'),
                              command=secant_Method)
result_Button.pack(padx='5',pady='5')

# Create a label to display the solution
result_Label= Label(window,
                          text=" ",                 
                          bg="#2a2d2e",
                          fg="white",
                          font=('Montserrat', 20, 'bold'))
result_Label.pack()
 
# Create a style
style = ttk.Style()

# Set the theme with the theme_use method  
style.theme_use("default")

style.configure("Treeview",
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

style.configure("Treeview.Heading",
                background="#565b5e",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",
            background=[('active', '#3484F0')])

window.mainloop()

