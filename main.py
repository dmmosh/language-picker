# libraries
import torch 
import torch.nn as nn 
import tkinter as tk

# functions/classes
import funs
from funs import linReg

#HYPERPARAMS
#box height, width
b_height = 250
b_width = 170


model = linReg()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.L1Loss()

iter_num = 1


# yeah something here i guess
#TODO: train the actual regression
for i in range(iter_num):

    model.train()


# box romatting

root = tk.Tk()

root.geometry(str(b_height)+'x'+str(b_width))

text = tk.Text(root, 
               height=b_height, 
               width=b_height, 
               background='black', 
               foreground='white',
               font=('Courier', 44))
text.pack()

text.insert(tk.END, torch.zeros(4,2))

tk.mainloop()
