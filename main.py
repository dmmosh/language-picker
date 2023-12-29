import funs
import torch 
import torch.nn as nn 
import tkinter as tk


root = tk.Tk()

root.geometry('250x170')

text = tk.Text(root, height=20, width=30)


text.pack()

text.insert(tk.END, 'hello world !')

tk.mainloop()
