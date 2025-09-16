from math import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# Create the main window
window = ctk.CTk()
window.title("Bisection Method")
window.resizable(0,0)

def get_XLower():
    x_Lower = float(xLower_Input.get())
    return x_Lower

def get_Xupper():
    x_Upper = float(xUpper_Input.get())
    return x_Upper

def get_Epsilon():
    eps = float(epsilon_Input.get())
    return eps

def get_Function(x):
    function = str(eval(func_Input.get()))
    return function

def bisection_Method():
    xLower = get_XLower()
    xUpper = get_Xupper()
    epsilon = get_Epsilon()

    xr = 0.0
    xr_old = 0.0
    error = 0.0
    iteration = 0

    while  True:
        xr_old = xr
        xr = (xLower+xUpper)/2
        f_of_xLower = get_Function(xLower)
        f_of_xUpper = get_Function(xUpper)
        f_of_xLower_iteration = float(f_of_xLower)
        f_of_xUpper_iteration = float(f_of_xUpper)
        
        polynomial_Check = f_of_xLower_iteration * f_of_xUpper_iteration
        if polynomial_Check >= 0:
            messagebox.showwarning("Warning!","Polynomial Has No Solution.")
            exit()

        f_of_xr = get_Function(xr)
        f_of_xr_iteration = float(f_of_xr)
        error = abs((xr-xr_old)/xr)*100
        iteration = iteration + 1
        
        if iteration == 1:
            table.insert(parent='', 
                         index='end', 
                         iid=iteration, 
                         text='',
                         values=(iteration, 
                                 round(xLower,3), 
                                 round(f_of_xLower_iteration,3), 
                                 round(xUpper,3), 
                                 round(f_of_xUpper_iteration,3), 
                                 round(xr,3), 
                                 round(f_of_xr_iteration,3), ' '))
        else:
          table.insert(parent='', 
                       index='end', 
                       iid=iteration, 
                       text='',
                       values=(  iteration, 
                                 round(xLower,3), 
                                 round(f_of_xLower_iteration,3), 
                                 round(xUpper,3), 
                                 round(f_of_xUpper_iteration,3), 
                                 round(xr,3), 
                                 round(f_of_xr_iteration,3), 
                                 f"{round(error,3)} %"))                             
          
        sign_Check = f_of_xLower_iteration * f_of_xr_iteration
        if sign_Check > 0:
            xLower = xr
        elif sign_Check < 0:
            xUpper = xr
        else:
            result_Label['text'] = f"The Value of Required Root is : {round(xr,3)} "
            return xr
            break

        if error <= epsilon :
            break
     
    result_Label['text'] = f"The Value of Required Root is : {round(xr,3)} "
    return xr 

frame1 = ctk.CTkFrame(master=window,
                      width= 300 ,
                      bg_color="transparent",
                      height= 200 )
frame1.pack(side=TOP, padx='15', pady='15')

LabelTitle = ctk.CTkLabel(frame1,
                          text='Bisection Method',
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

xLower_Label = ctk.CTkLabel(window,
                            text='𝒳𝒍',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 20, 'bold')).pack(padx='10')
xLower_Input = ctk.CTkEntry(window,
                            border_width=2,
                            width=200)
xLower_Input.pack(padx='10',pady='10')

xUpper_Label = ctk.CTkLabel(window,
                            text='𝒳𝒖',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 20, 'bold')).pack(padx='10')
xUpper_Input = ctk.CTkEntry(window,
                            border_width=1,
                            width=200)
xUpper_Input.pack(padx='10',pady='10')

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
                     columns=(1,2,3,4,5,6,7,8),
                     show='headings',
                     height=9)
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
table.heading(2, text='𝒳𝒍')

table.column("3",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(3, text='𝒇(𝒳𝒍)')

table.column("4",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(4, text='𝒳𝒖')

table.column("5",
                anchor=CENTER, 
                stretch=YES, 
                width=100)			
table.heading(5, text='𝒇(𝒳𝒖)')

table.column("6",
                anchor=CENTER, 
                stretch=YES, 
                width=100)				
table.heading(6, text='𝒳𝒓')

table.column("7",
                anchor=CENTER, 
                stretch=YES, 
                width=100)
table.heading(7, text='𝒇(𝒳𝒓)')

table.column("8",
                anchor=CENTER, 
                stretch=YES, 
                width=100)
table.heading(8, text='𝞮')

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
                              command=bisection_Method)
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