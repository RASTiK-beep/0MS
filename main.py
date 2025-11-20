import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import numpy as np


class window(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Buttons.TButton', font=('Arial', 13),bordercolor="#006dda", background="#006dda", foreground="#d5d9dd", borderwidth=0)
        style.map('Buttons.TButton', background=[('active', "#508ecc")])
        style.configure('TFrame', background="#0c1218", foreground="#d5d9dd")
        style.configure('TLabelframe',bordercolor="#0c1218", background="#0c1218", foreground="#d5d9dd")
        style.layout('TLabelframe', [
        ('Labelframe.border', {'sticky': 'nswe'})])
        style.configure('TLabelframe.Label',bordercolor="#0c1218", background="#0c1218", foreground="#d5d9dd")
        style.configure('TEntry', background="#1c2631", foreground="#1c2631")
        style.configure('TLabel', background="#0c1218", foreground="#d5d9dd")


        self.configure(bg="#0c1218")

        self.title("Integral Calculator")
        self.geometry("1500x1000")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=8)

        middleSep = tk.Canvas(self, width=2, bg="#d5d9dd", highlightthickness=0)
        middleSep.grid(row=0, column=1, sticky="ns", padx=5, pady=20)

        self.rowconfigure(0, weight=1)

        leftFrame = ttk.Frame(self)
        leftFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        leftFrame.columnconfigure(0, weight=1)
        leftFrame.rowconfigure(0, weight=1)
        leftFrame.rowconfigure(1, weight=0)
        
        leftTopSep = tk.Canvas(leftFrame, height=2, bg="#d5d9dd", highlightthickness=0)
        leftTopSep.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        leftFrame.rowconfigure(2, weight=1)
        leftFrame.rowconfigure(3, weight=0)

        leftBotSep = tk.Canvas(leftFrame, height=2, bg="#d5d9dd", highlightthickness=0)
        leftBotSep.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        
        leftFrame.rowconfigure(4, weight=1)


        rightFrame = ttk.Frame(self)
        rightFrame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        singleIntFr = singleInt(leftFrame)
        singleIntFr.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)


        doubleIntFr = doubleInt(leftFrame)
        doubleIntFr.grid(row=2, column=0, sticky="nsew", padx=3, pady=3)

        tripleIntFr = tripleInt(leftFrame)
        tripleIntFr.grid(row=4, column=0, sticky="nsew", padx=3, pady=3)

class singleInt(ttk.LabelFrame):
    def __init__(self, parent): #treba poskusat relief : sunken flat raised groove
        super().__init__(parent, borderwidth=2, labelanchor="n",  padding=3, relief="solid", text="Integrál")
        self.columnconfigure(0, weight=1)

        self.createWidgets()
        style = ttk.Style()


    """
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
    """
        
    def createWidgets(self):
        ttk.Label(self, text="Funkcia f(x)", font=('Arial', 20, 'bold')).grid(column=0, row=0)

        self.fText = ttk.Entry(self, font=('Arial', 20))
        self.fText.grid(column=0, row=1, columnspan=1, sticky="ew", pady=5)
        
        self.calcButton = ctk.CTkButton(self, text="Vypočítaj",  corner_radius=10, #command=self.calculate, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        
        
        self.calcButton.grid(column=0, row=2, pady=5)
        self.drawButton = ctk.CTkButton(self, text="Vyykresli Graf",  corner_radius=10, #command=self.calculate, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)

        self.drawButton.grid(column=0, row=3, pady=5)

        self.result = tk.Text()


class doubleInt(ttk.LabelFrame):
    def __init__(self, parent): #treba poskusat relief : sunken flat raised groove
        super().__init__(parent, borderwidth=2, labelanchor="n",  padding=3, relief="solid", text="Dvojný Integrál")
        self.columnconfigure(0, weight=1)

        self.createWidgets()
        style = ttk.Style()
        style.configure('Buttons.TButton', font=('Arial', 13))


    """
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
    """
        
    def createWidgets(self):
        ttk.Label(self, text="Funkcia f(x, y)", font=('Arial', 20, 'bold')).grid(column=0, row=0)

        self.fText = ttk.Entry(self, font=('Arial', 20))
        self.fText.grid(column=0, row=1, columnspan=1, sticky="ew", pady=5)

        self.calcButton = ctk.CTkButton(self, text="Vypočítaj",  corner_radius=10, #command=self.calculate, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        self.calcButton.grid(column=0, row=2, pady=5)


        self.drawButton = ctk.CTkButton(self, text="Vyykresli Graf",  corner_radius=10, #command=self.calculate, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        self.drawButton.grid(column=0, row=3, pady=5)


        self.result = tk.Text()

class tripleInt(ttk.LabelFrame):
    def __init__(self, parent): #treba poskusat relief : sunken flat raised groove
        super().__init__(parent, borderwidth=2, labelanchor="n",  padding=3, relief="solid", text="Trojný Integrál")
        self.columnconfigure(0, weight=1)
        self.createWidgets()
        
    def createWidgets(self):
        ttk.Label(self, text="Funkcia f(x, y, z)", font=('Arial', 20, 'bold')).grid(column=0, row=0)

        self.fText = ttk.Entry(self, font=('Arial', 20))
        self.fText.grid(column=0, row=1, sticky="ew", columnspan=1, pady=5)

        self.calcButton = ctk.CTkButton(self, text="Vypočítaj",  corner_radius=10, #command=self.calculate, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        self.calcButton.grid(column=0, row=2, pady=5)


        self.result = tk.Text()

    



if __name__ == "__main__":
    app = window()
    tk.mainloop()
    
