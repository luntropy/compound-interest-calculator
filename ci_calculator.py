import tkinter as tk
from tkinter import font

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title('Compound Interest Calculator')
        self.master.geometry('450x350')
        self.master.resizable(False, False)

        # Setup the color of the application
        self.app_background_color = '#204060'
        self.btn_background_color = '#ffffff'
        self.master.configure(bg = self.app_background_color)

        # Setup the color of the text
        self.text_color = '#ffffff'

        # Setup fonts
        self.font_style_label = font.Font(family = 'Times', size = 15)
        self.font_style_entry = font.Font(family = 'Times', size = 13)

        self.ci_calculator_frame = tk.Frame(self.master, bg = self.app_background_color)
        self.create_cic_frame(self.ci_calculator_frame, self.font_style_label, self.font_style_entry)

    # Frames - functions
    def create_cic_frame(self, frame, font_label, font_entry):
        principal_label = tk.Label(frame, text = 'Principal: ', font = font_label, bg = self.app_background_color, fg = self.text_color)
        principal_label.grid(row = 0, pady = 10)

        principal = tk.Entry(frame, justify = 'center', font = font_entry)
        principal.grid(row = 0, column = 1, pady = 10)

        period_label = tk.Label(frame, text = 'Years: ', font = font_label, bg = self.app_background_color, fg = self.text_color)
        period_label.grid(row = 1, pady = 10)

        period = tk.Entry(frame, justify = 'center', font = font_entry)
        period.grid(row = 1, column = 1, pady = 10)

        interest_label = tk.Label(frame, text = 'Interest: ', font = font_label, bg = self.app_background_color, fg = self.text_color)
        interest_label.grid(row = 2, pady = 10)

        interest = tk.Entry(frame, justify = 'center', font = font_entry)
        interest.grid(row = 2, column = 1, pady = 10)

        # Text box
        display_result = tk.Text(frame, height = 2, font = font_entry)
        display_result.grid(row = 3, columnspan = 5, pady = 10)

        calculate_button = tk.Button(frame, text = 'Calculate', bg = self.btn_background_color)
        calculate_button.grid(row = 4, columnspan = 2, pady = 10)

        frame.pack(expand = True)

    # Other functions
    def calculate_ci(p, n, i):
        print('TO DO')

if __name__ == '__main__':
    app = tk.Tk()
    MainApplication(app)
    app.mainloop()
