import tkinter as tk
from tkinter import font

class MainApplication:
    def __init__(self, master):
        # App configuration
        # Setup the color theme of the application
        self.color_theme = {
            "app_background_color" : "#333333",
            "box_background_color" : "#404040",
            "btn_background_color" : "#404040",
            "highlight_background" : "#000000",
            "active_background" : "#595959",
            "text_color" : "#ffffff",

            # Setup the fonts
            "font_style_label" : font.Font(family = 'Times', size = 17),
            "font_style_entry" : font.Font(family = 'Times', size = 15)
        }

        self.master = master
        self.master.title("Compound Interest Calculator")
        self.master.geometry("500x370")
        self.master.resizable(False, False)
        self.master.configure(bg = self.color_theme["app_background_color"])

        # Create the main calculator frame
        self.ci_calculator_frame = tk.Frame(self.master, bg = self.color_theme["app_background_color"])
        self.create_cic_frame(self.ci_calculator_frame, self.color_theme)

    # Frames - functions
    def create_cic_frame(self, frame, color_theme):
        # Text box
        display_result = tk.Text(frame, state = "disabled", height = 3, font = color_theme["font_style_label"], bg = color_theme["box_background_color"], fg = color_theme["text_color"], borderwidth = 0, highlightbackground = color_theme["highlight_background"])
        display_result.grid(row = 0, columnspan = 5)

        # Principal
        principal_label = tk.Label(frame, text = "Principal: ", font = color_theme["font_style_label"], bg = color_theme["app_background_color"], fg = color_theme["text_color"])
        principal_label.grid(row = 1, pady = (40, 15))

        principal = tk.Entry(frame, justify = "center", font = color_theme["font_style_entry"], bg = color_theme["box_background_color"], fg = color_theme["text_color"], borderwidth = 0, highlightbackground = color_theme["highlight_background"])
        principal.grid(row = 1, column = 1, pady = (40, 15))

        # Period
        period_label = tk.Label(frame, text = "Years: ", font = color_theme["font_style_label"], bg = color_theme["app_background_color"], fg = color_theme["text_color"])
        period_label.grid(row = 2, pady = 15)

        period = tk.Entry(frame, justify = "center", font = color_theme["font_style_entry"], bg = color_theme["box_background_color"], fg = color_theme["text_color"], borderwidth = 0, highlightbackground = color_theme["highlight_background"])
        period.grid(row = 2, column = 1, pady = 15)

        # Interest
        interest_label = tk.Label(frame, text = "Interest: ", font = color_theme["font_style_label"], bg = color_theme["app_background_color"], fg = color_theme["text_color"])
        interest_label.grid(row = 3, pady = 15)

        interest = tk.Entry(frame, justify = "center", font = color_theme["font_style_entry"], bg = color_theme["box_background_color"], fg = color_theme["text_color"], borderwidth = 0, highlightbackground = color_theme["highlight_background"])
        interest.grid(row = 3, column = 1, pady = 15)

        # "Calculate" button
        calculate_button = tk.Button(frame, text = "Calculate", font = color_theme["font_style_entry"], bg = color_theme["btn_background_color"], fg = color_theme["text_color"], borderwidth = 0, highlightbackground = color_theme["highlight_background"], activebackground = color_theme["active_background"])
        calculate_button.grid(row = 4, columnspan = 2, pady = (30, 0))

        frame.pack(expand = False)

    # Other functions
    def calculate_ci(p, n, i):
        print("TO DO")

if __name__ == "__main__":
    app = tk.Tk()
    MainApplication(app)
    app.mainloop()
