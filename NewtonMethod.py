from tkinter import *
from tkinter import ttk
from math import *
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# Create the main window
window = ctk.CTk()
window.title("Newton Method")
window.resizable(0,0)

def get_XNode():
    x_Node = float(xNode_Input.get())
    return x_Node

def get_Function(x):
    function = str(eval(func_Input.get()))
    return function

def get_Fdash(x):
    Func=str(eval(funcDash_Input.get()))
    return Func

def get_Epsilon():
    EPS=float(epsilon_Input.get())
    return EPS

def newton_Method():
    xNode = get_XNode() 
    epsilon = get_Epsilon() 
    xi_PlusOne = 0.0 
    xi = 0.0
    error = 0.0

    for i in range(100):
        xi = xNode 
        fDash_of_x = get_Fdash(xi) 
        fDash_of_xi = float(fDash_of_x)
        f_of_x = get_Function(xi)
        f_of_xi = float(f_of_x)
        xi_PlusOne = xi - f_of_xi/fDash_of_xi

        if i == 0:
            table.insert(parent='', 
                         index='end', 
                         iid=i, 
                         text='',
                         values=(i,
                                 round(xNode,3),
                                 round(f_of_xi,3),
                                 round(fDash_of_xi,3)," "))
        else:
            table.insert(parent='', 
                         index='end', 
                         iid=i, 
                         text='',
                         values=(i,
                                 round(xNode,3),
                                 round(f_of_xi,3),
                                 round(fDash_of_xi,3),
                                 f"{round(error,3)} %"))

        if error >= epsilon or i == 0:
            error = abs((xi_PlusOne-xi)/xi_PlusOne)*100
            xNode = xi_PlusOne
          
        else: 
            break
        result_Label['text']=f"The Value of Required Root is : {round(xNode,3)} "

    return xNode
    
frame1 = ctk.CTkFrame(master=window,
                      width= 300 ,
                      bg_color="transparent",
                      height= 200 )
frame1.pack(side=TOP, padx='15', pady='15')

LabelTitle = ctk.CTkLabel(frame1,
                          text='Newton-Raphson Method',
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 24, 'bold'))
LabelTitle.pack(padx='5', pady='5')

func_Label = ctk.CTkLabel(window, 
                          text="𝒇(𝒳)",
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 15, 'bold')).pack(padx='10')
func_Input = ctk.CTkEntry(window,
                          border_width=1,
                          width=200)
func_Input.pack(padx='10',pady='10')

funcDash_Label = ctk.CTkLabel(window, 
                              text="𝒇`(𝒳)",
                              bg_color="transparent",
                              text_color="white",
                              font=('Montserrat', 15, 'bold')).pack(padx='10')
funcDash_Input = ctk.CTkEntry(window,
                              border_width=1,
                              width=200)
funcDash_Input.pack(padx='10',pady='10')

xNode_Label = ctk.CTkLabel(window,
                            text='𝒳𝒐',
                            bg_color="transparent",
                            text_color="white",
                            font=('Montserrat', 20, 'bold')).pack(padx='10')
xNode_Input = ctk.CTkEntry(window,
                            border_width=2,
                            width=200)
xNode_Input.pack(padx='10',pady='10')

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
                     columns=(1,2,3,4,5),
                     show='headings',
                     height=8)
table.pack(fill='both', expand= True)

table.column("1",
             anchor=CENTER, 
             stretch=YES, 
             width=100)
table.heading(1, text='𝒊')

table.column("2",
             anchor=CENTER, 
             stretch=YES, 
             width=100)
table.heading(2, text='𝒳𝒊')

table.column("3",
             anchor=CENTER, 
             stretch=YES, 
             width=100)
table.heading(3, text='𝒇(𝒳𝒊)')

table.column("4",
             anchor=CENTER, 
             stretch=YES, 
             width=100)
table.heading(4, text='𝒇`(𝒳𝒊)')

table.column("5",
             anchor=CENTER, 
             stretch=YES, 
             width=100)
table.heading(5, text='𝞮')

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
                              command=newton_Method)
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