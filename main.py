# libraries
import torch 
import torch.nn as nn 
import tkinter as tk

# functions/classes
import funs
from funs import linReg

# CONSTANTS
B = 'black'
W = 'white'

# HYPERPARAMETERS
b_height = 200
b_width = 1000

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
root.configure(bg=B)

text = tk.Text(root, 
               height=100, 
               width=100, 
               background='black', 
               foreground='white',
               font=('Comic Sans', 20))
text.insert(tk.END, torch.zeros(4,2))

#text.pack()

canvas = tk.Canvas(root,
                   height=b_height,
                   width=b_width,
                   bg=W)
canvas.pack()

entry1 = tk.Entry(root, bg=B, fg=W)
canvas.create_window(200,140, 
                     window= entry1)

canvas.create_window(200,140, window = text)



#input = entry1.get()







tk.mainloop()
