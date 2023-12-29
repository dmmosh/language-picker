# libraries
import torch 
import torch.nn as nn 
import tkinter as tk

# functions/classes
import funs
from funs import linReg

#HYPERPARAMS
#box height, width
b_height = 1000
b_width = 300


'''
HEART OF CODE
'''
model = linReg()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.L1Loss()

iter_num = 1


# yeah something here i guess
#TODO: train the actual regression
for i in range(iter_num):

    model.train()


# box romatting


'''
GUI !!
'''

root = tk.Tk()

root.geometry(str(b_height)+'x'+str(b_width))

text = tk.Text(root, 
               height=b_height//2, 
               width=b_width, 
               background='black', 
               foreground='white',
               font=('Comic Sans', 20))

text.pack()
text.insert(tk.END, torch.zeros(4,2))

canvas = tk.Canvas(root,
                   height=b_height//2,
                   width=b_width)

canvas.pack()



tk.mainloop()
