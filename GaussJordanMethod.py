from tkinter import *
import pandas as pd
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# Create the main window
window = ctk.CTk()
window.title("Gauss-Jordan Method")
window.resizable(0,0)

def gaussmethod(matrix):
    n = len(matrix)
    
    for col in range(n):
        # Find the pivot row
        pivot_row = None
        for i in range(col, n):
            if matrix[i][col] != 0:
                pivot_row = i
                break
        
        if pivot_row is None:
            return False  
        
        matrix[col], matrix[pivot_row] = matrix[pivot_row], matrix[col]
        
        # Make the diagonal element 1
        pivot_element = matrix[col][col]
        for j in range(col, n + 1):  
            matrix[col][j] /= pivot_element 
        
        # Eliminate other elements in the current column
        for i in range(col + 1, n):
            factor = matrix[i][col]
            for j in range(col, n + 1): 
                matrix[i][j] -= factor * matrix[col][j]
    
    # Back-substitution to find the solution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    return solution

def convert_to_upper_triangular(matrix):
    n = len(matrix)
    
    for col in range(n):
        # Find the pivot row
        pivot_row = None
        for i in range(col, n):
            if matrix[i][col] != 0:
                pivot_row = i
                break
        
        if pivot_row is None:
            return False, matrix  # Matrix cannot be converted to upper triangular form
        
        # Swap the current row with the pivot row
        matrix[col], matrix[pivot_row] = matrix[pivot_row], matrix[col]
        
        # Eliminate other elements in the current column
        pivot_element = matrix[col][col]
        for i in range(col + 1, n):
            factor = matrix[i][col] / pivot_element
            for j in range(col, n + 1): 
                matrix[i][j] -= factor * matrix[col][j]
    
    return True, matrix

def solve_equations():
    matrix = []
    for i in range(n):
        row = []
        for j in range(n + 1):
            entry = matrix_entries[i][j].get()
            if entry.strip() == "":
                entry = "0"
            row.append(round(float(entry), 2))  # Round input values to 2 decimal places
        matrix.append(row)

    success, result_matrix = convert_to_upper_triangular(matrix)
    if success:
        solution_label.configure(text="Matrix in upper triangular form:")
        result = gaussmethod(result_matrix)
        for i,val in enumerate(result):
            L=[
                    {'0': "1"  ,  '1': "0"  ,  '2': "0" ,'3': "x1"},
                    {'0': "0"  ,  '1': "1"  ,  '2': "0", '3': "x2"},
                    {'0': "0"  ,  '1': "0"  ,  '2': "1", '3': "x3"},
                    {'0': "-"  ,  '1': "-"  ,  '2': "-", '3': "-"}]
                
            L_df = pd.DataFrame(L,columns = ['0','1','2','3'], index = ['','','','']).rename(columns = {'0':'','1':'','2':'','3':''})

        d2 = Label(window,
            text=(L_df),
            bg="#343638",
            fg="white",
            font=('Montserrat', 16, 'bold')).grid(row=6, column=0, columnspan=n, padx=5, pady=5)
        
        result = gaussmethod(result_matrix)
        if result:
            solution_label.configure(text="Solution:")
            for i, val in enumerate(result):
                solution_labels[i + n].configure(text=f'X{i + 1} = {round(val,2)}')
    else:
        solution_label.configure(text="No unique solution or matrix is inconsistent.")
        for i in range(n):
            solution_labels[i].configure(text="")

frame1 = ctk.CTkFrame(master=window,
                      width= 50 ,
                      bg_color="transparent",
                      height= 50 )
frame1.grid(row= 0, column=0, padx='10', pady='10')

LabelTitle = ctk.CTkLabel(frame1,
                          text='Matrix:',
                          bg_color="transparent",
                          text_color="white",
                          font=('Montserrat', 18, 'bold'))
LabelTitle.grid(sticky='ne' , padx='5', pady='5')

# Create input fields for matrix and constants
n = 3  # You can change this to match the desired matrix size
matrix_entries = [[None] * (n + 1) for _ in range(n)]

for i in range(n):
    for j in range(n + 1):
        entry = ctk.CTkEntry(window)
        entry.grid(row=1 + i, column=j, padx=5, pady=5)
        matrix_entries[i][j] = entry

# Create a Solve button
solve_button = ctk.CTkButton(window, 
                             bg_color='#343638',
                             fg_color='white',
                             text='Calculate',
                             text_color='#343638',
                             font=('Montserrat', 20, 'bold'),command=solve_equations)
solve_button.grid(row=5, column=n // 2, columnspan=2, padx=5, pady=10)

# Create a label to display the solution
solution_label = ctk.CTkLabel(window, 
                              text="",
                              bg_color="transparent",
                              text_color="white",
                              font=('Montserrat', 16, 'bold'))
solution_label.grid(row=5 + 1, column=0, columnspan=n, padx=5, pady=5)

solution_labels = [ctk.CTkLabel(window, 
                                text="",
                                anchor = "center", 
                                bg_color="transparent",
                                text_color="white",
                                font=('Montserrat', 16, 'bold')) for _ in range(n + n)]
for i in range(n + n):
    solution_labels[i].grid(row=5 + 2 + i, column=0, columnspan=n, padx=5, pady=5)

window.mainloop()