import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# S clam témou
style = ttk.Style()
style.theme_use('clam')

frame2 = ttk.Frame(root)
frame2.pack(side='left', padx=20, pady=20)

ttk.Label(frame2, text="Clam téma").pack()
ttk.Button(frame2, text="Tlačidlo").pack(pady=5)
ttk.Entry(frame2).pack(pady=5)


root.mainloop()