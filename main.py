import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from mpl_toolkits.mplot3d import Axes3D


defaultRange = [-100, 100, -sp.oo, sp.oo]


class window(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style()
        style.theme_use("clam")

        style.configure('Buttons.TButton', font=('Arial', 13),bordercolor="#006dda", background="#006dda", foreground="#d5d9dd", borderwidth=0)
        style.configure('TFrame', background="#0c1218", foreground="#d5d9dd")
        style.configure('TLabelframe',bordercolor="#0c1218", background="#0c1218", foreground="#d5d9dd")
        style.layout('TLabelframe', [
        ('Labelframe.border', {'sticky': 'nswe'})])
        style.configure('TLabelframe.Label',bordercolor="#0c1218", background="#0c1218", foreground="#d5d9dd")
        style.configure('TLabel', background="#0c1218", foreground="#d5d9dd")


        self.configure(bg="#0c1218")

        self.title("Integral Calculator")
        self.geometry("1600x1000")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=8)

        middleSep = tk.Canvas(self, width=2, bg="#d5d9dd", highlightthickness=0)
        middleSep.grid(row=0, column=1, sticky="ns", padx=5, pady=20)

        self.rowconfigure(0, weight=1)

        self.leftFrame = ttk.Frame(self)
        self.leftFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.leftFrame.columnconfigure(0, weight=1)
        self.leftFrame.rowconfigure(0, weight=1)
        self.leftFrame.rowconfigure(1, weight=0)
        
        leftTopSep = tk.Canvas(self.leftFrame, height=2, bg="#d5d9dd", highlightthickness=0)
        leftTopSep.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        self.leftFrame.rowconfigure(2, weight=1)
        self.leftFrame.rowconfigure(3, weight=0)

        self.leftFrame.rowconfigure(4, weight=1)


        self.rightFrame = ttk.Frame(self)
        self.rightFrame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.singleIntFr = singleInt(self.leftFrame, self)
        self.singleIntFr.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)


        self.doubleIntFr = doubleInt(self.leftFrame, self)
        self.doubleIntFr.grid(row=2, column=0, sticky="nsew", padx=3, pady=3)

    def draw_function(self):
        global defaultRange
        rawFunction = self.singleIntFr.fText.get().strip()
        if not rawFunction:
            return
        

        expr, func = text_to_function_1d(rawFunction)

        start = self.singleIntFr.fromXentry.get().strip()
        end = self.singleIntFr.toXentry.get().strip()

        start = convert(start, 0)
        end = convert(end, 1)

        
        x = np.linspace(start, end, 1000)

        y = func(x)

        for widget in self.rightFrame.winfo_children():
            widget.destroy()


        fig, ax = plt.subplots(figsize=(8, 6), facecolor="#0c1218")  
        ax.set_facecolor("#0c1218")
        ax.tick_params(colors='#bedeff')
        ax.set_xlabel('x', color='#bedeff')
        ax.set_ylabel('f(x)', color='#bedeff')
        ax.set_title(expr, color="#bedeff")
        ax.plot(x, y, color='#9da6ee', linewidth=2)
        ax.grid(True, color='#006dda', alpha=0.2)

        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def draw_3d_function(self):
        global defaultRange
        rawFunction = self.doubleIntFr.fText.get().strip()

        if not rawFunction:
            return
        
        expr, func = text_to_function_2d(rawFunction)

        startX = self.doubleIntFr.fromXentry.get().strip()
        endX = self.doubleIntFr.toXentry.get().strip()

        startY = self.doubleIntFr.fromYentry.get().strip()
        endY = self.doubleIntFr.toYentry.get().strip()

        startX = convert(startX, 0)
        endX = convert(endX, 1)
        startY = convert(startY, 0)
        endY = convert(endY, 1)

        x = np.linspace(startX, endX, 500)
        y = np.linspace(startY, endY, 500)
        X, Y = np.meshgrid(x, y)

        Z = func(X, Y)

        
        for widget in self.rightFrame.winfo_children():
            widget.destroy()
        

        fig = plt.figure(figsize=(8, 6), facecolor="#0c1218")
        ax = fig.add_subplot(111, projection='3d')

        surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)


        ax.set_facecolor("#0c1218")
        ax.set_xlabel('x', color='#d5d9dd')
        ax.set_ylabel('y', color='#d5d9dd')
        ax.set_zlabel('f(x,y)', color='#d5d9dd')
        ax.tick_params(colors='#bedeff')
        colorbar = fig.colorbar(surface)
        colorbar.ax.tick_params(colors='#bedeff')
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def calculate_single_int(self):
        rawFunction = self.singleIntFr.fText.get().strip()

        if not rawFunction:
            return
        
        expr, func = text_to_function_1d(rawFunction)

        start = self.singleIntFr.fromXentry.get().strip()
        end = self.singleIntFr.toXentry.get().strip()

        start = convert(start, 2)
        end = convert(end, 3)

        x = sp.Symbol('x')

        integratedF = sp.integrate(expr, x)

        result = sp.integrate(expr, (x, start, end))

        if result == sp.oo:
            result = '∞'
        elif result == -sp.oo:
            result = '-∞'
        else:
            result = round(float(result), 3)

        pretty_integral = sp.pretty(integratedF, use_unicode=True)
        self.singleIntFr.integratedF.config(text=pretty_integral)
        self.singleIntFr.result.config(text=str(result))

    def calculate_double_int(self):
        rawFunction = self.doubleIntFr.fText.get().strip()

        if not rawFunction:
            return
        
        expr, func = text_to_function_2d(rawFunction)

        startX = self.doubleIntFr.fromXentry.get().strip()
        endX = self.doubleIntFr.toXentry.get().strip()
        startY = self.doubleIntFr.fromYentry.get().strip()
        endY = self.doubleIntFr.toYentry.get().strip()

        startX = convert(startX, 2)
        endX = convert(endX, 3)
        startY = convert(startY, 2)
        endY = convert(endY, 3)

        x, y = sp.symbols('x y')

        integratedF = sp.integrate(expr, y, x)

        result = sp.integrate(expr, (y, startY, endY), (x, startX, endX))

        if result == sp.oo:
            result = '∞'
        elif result == -sp.oo:
            result = '-∞'
        else:
            try:
                result = round(float(result), 3)
            except:
                result = str(result)

        pretty_integral = sp.pretty(integratedF, use_unicode=True)
        self.doubleIntFr.integratedF.config(text=pretty_integral)
        self.doubleIntFr.result.config(text=str(result))


class singleInt(ttk.LabelFrame):
    def __init__(self, parent, window): #treba poskusat relief : sunken flat raised groove
        super().__init__(parent, borderwidth=2, labelanchor="n",  padding=3, relief="solid", text="Integrál")
        self.columnconfigure(0, weight=1)
        self.window = window
        self.createWidgets()
        style = ttk.Style()

        
    def createWidgets(self):
        ttk.Label(self, text="Funkcia f(x)", font=('Arial', 20, 'bold')).grid(column=0, row=0, columnspan=6)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)


        self.fText = ctk.CTkEntry(self, font=('Arial', 15), fg_color="#9da6ee", border_width=0)
        self.fText.grid(column=0, row=1, columnspan=6, sticky="ew", pady=5)

        ttk.Label(self, text="X Od:", font=('Arial', 12)).grid(column=0, row=2, sticky="w", padx=(5,2))
        self.fromXentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100, height=30)
        self.fromXentry.grid(column=1, row=2, sticky="w", pady=5)

        ttk.Label(self, text="X Do:", font=('Arial', 12)).grid(column=0, row=3, sticky="w", padx=(5,2))
        self.toXentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100,height=30)
        self.toXentry.grid(column=1, row=3, sticky="w", pady=5)

        


        self.calcButton = ctk.CTkButton(self, text="Vypočítaj",  corner_radius=10, command=self.window.calculate_single_int, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        
        
        self.calcButton.grid(column=0,columnspan=6, row=5, pady=5)
        self.drawButton = ctk.CTkButton(self, text="Vykresli Graf Funkcie",  corner_radius=10, command=self.window.draw_function, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)

        self.drawButton.grid(column=0, row=6, pady=5,columnspan=6)

        ttk.Label(self, text="Integrovaná funkcia:", font=('Arial', 16, 'bold')).grid(column=0, row=7, pady=10, padx=10, sticky="e")
        self.integratedF = ttk.Label(self, text="", font=('Courier New', 14), justify='left')
        self.integratedF.grid(column=1, row=7, pady=10, padx=10, sticky="w", columnspan=5)

        ttk.Label(self, text="Výsledok integrácie:", font=('Arial', 16, 'bold')).grid(column=0, row=8, pady=10, padx=10, sticky="e")
        self.result = ttk.Label(self, text="", font=('Arial', 16))
        self.result.grid(column=1, row=8, pady=10, padx=10, sticky="w", columnspan=5)



class doubleInt(ttk.LabelFrame):
    def __init__(self, parent, window): #treba poskusat relief : sunken flat raised groove
        super().__init__(parent, borderwidth=2, labelanchor="n",  padding=3, relief="solid", text="Dvojný Integrál")
        self.columnconfigure(0, weight=1)

        self.window = window
        

        self.createWidgets()
        style = ttk.Style()

        
    def createWidgets(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=0)
        self.columnconfigure(5, weight=1)

        ttk.Label(self, text="Funkcia f(x, y)", font=('Arial', 20, 'bold')).grid(column=0, row=0, columnspan=6)

        self.fText = ctk.CTkEntry(self, font=('Arial', 15), fg_color="#9da6ee", border_width=0)
        self.fText.grid(column=0, row=1, columnspan=6, sticky="ew", pady=5)

        ttk.Label(self, text="X Od:", font=('Arial', 12)).grid(column=0, row=2, sticky="w", padx=(5,2))
        self.fromXentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100, height=30)
        self.fromXentry.grid(column=1, row=2, sticky="w", pady=5)

        ttk.Label(self, text="X Do:", font=('Arial', 12)).grid(column=0, row=3, sticky="w", padx=(5,2))
        self.toXentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100,height=30)
        self.toXentry.grid(column=1, row=3, sticky="w", pady=5)

        ttk.Label(self, text="Y Od:", font=('Arial', 12)).grid(column=2, row=2, sticky="w", padx=(5,2))
        self.fromYentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100, height=30)
        self.fromYentry.grid(column=3, row=2, sticky="w", pady=5)

        ttk.Label(self, text="Y Do:", font=('Arial', 12)).grid(column=2, row=3, sticky="w", padx=(5,2))
        self.toYentry = ctk.CTkEntry(self, font=('Arial', 12), fg_color="#9da6ee", border_width=0, width=100,height=30)
        self.toYentry.grid(column=3, row=3, sticky="w", pady=5)



        self.calcButton = ctk.CTkButton(self, text="Vypočítaj",  corner_radius=10, command=self.window.calculate_double_int,
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        self.calcButton.grid(column=0, row=4, pady=5, columnspan=6)


        self.drawButton = ctk.CTkButton(self, text="Vykresli Graf Funkcie",  corner_radius=10, command=self.window.draw_3d_function, 
                                        fg_color='#006dda', hover_color='#508ecc', font=('Arial', 18, 'bold'), width=200, height=35)
        self.drawButton.grid(column=0, row=5, pady=5, columnspan=6)

        ttk.Label(self, text="Integrovaná funkcia:", font=('Arial', 16, 'bold')).grid(column=0, row=6, pady=10, padx=10, sticky="e")
        self.integratedF = ttk.Label(self, text="", font=('Courier New', 14), justify='left')
        self.integratedF.grid(column=1, row=6, pady=10, padx=10, sticky="w", columnspan=5)

        ttk.Label(self, text="Výsledok integrácie:", font=('Arial', 16, 'bold')).grid(column=0, row=7, pady=10, padx=10, sticky="e")
        self.result = ttk.Label(self, text="", font=('Arial', 16))
        self.result.grid(column=1, row=7, pady=10, padx=10, sticky="w", columnspan=5)


def text_to_function_1d(text):
    x = sp.Symbol('x')
    text = text.replace('^', '**')
    expression = sp.sympify(text)
    f = sp.lambdify(x, expression, 'numpy')
    return expression, f
    
def text_to_function_2d(text):
    x, y = sp.symbols('x y')
    text = text.replace('^', '**')
    expression = sp.sympify(text)
    f = sp.lambdify((x, y), expression, 'numpy')
    return expression, f

def text_to_function_3d(text):
    x, y, z = sp.symbols('x y z')
    text = text.replace('^', '**')
    expression = sp.sympify(text)
    f = sp.lambdify((x, y, z), expression, 'numpy')
    return expression, f

def convert(input, index):
    global defaultRange

    if not input:
        return defaultRange[index]
    else:
        try:
            return float(input)
        except:
            return defaultRange[index]




if __name__ == "__main__":
    app = window()
    tk.mainloop()
    
