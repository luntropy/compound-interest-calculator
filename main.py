# import tkinter as tk
# from tkinter import font
import tkinter.messagebox as tkmsg
import math

def CalculateCompoundInterest(n, p, i):
    ci = p * (math.pow((1 + i / 100), n) - 1)
    tkmsg.showinfo('Compound Interest', round(ci, 2))

# app = tk.Tk()
# app.title('Compound Interest Calculator')
# app.geometry('450x300')

# calculator = tk.Frame(app)
# font_style_label = font.Font(family = 'Times', size = 15)
# font_style_entry = font.Font(family = 'Times', size = 13)

# n_label = tk.Label(calculator, text = 'Years: ', font = font_style_label)
# n_label.grid(row = 0, pady = 10)

# n = tk.Entry(calculator, justify = 'center', font = font_style_entry)
# n.grid(row = 0, column = 1, pady = 10)

# principal_label = tk.Label(calculator, text = 'Principal: ', font = font_style_label)
# principal_label.grid(row = 1, pady = 10)

# principal = tk.Entry(calculator, justify = 'center', font = font_style_entry)
# principal.grid(row = 1, column = 1, pady = 10)

# interest_label = tk.Label(calculator, text = 'Interest: % ', font = font_style_label)
# interest_label.grid(row = 2, pady = 10)

# interest = tk.Entry(calculator, justify = 'center', font = font_style_entry)
# interest.grid(row = 2, column = 1, pady = 10)

# calculator.place(anchor = 'c', relx = 0.5, rely = 0.4)

calculate_button = tk.Button(app, text = 'Calculate', command = lambda: CalculateCompoundInterest(int(n.get()), int(principal.get()), int(interest.get())))
# calculate_button.place(anchor = 'c', relx = 0.5, rely = 0.7)

# app.mainloop()

# print("Calculate Compound Interest \n")
#
# n = int(input("Years (n): "))
#
# p = int(input("Principal (P): "))
#
# i = int(input("Interest in furute, percentage (i): "))
#
# ci = p * (math.pow((1 + i / 100), n) - 1)
#
# print("Compound interest: {0}".format(round(ci, 2)))
