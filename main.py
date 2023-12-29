import funs
import torch 
import torch.nn as nn 
import tkinter as tk

#HYPERPARAMS

#box height, width
b_height = 250
b_width = 170

class linReg(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.weight = torch.nn.Parameter(torch.randn(1))
        self.bias = torch.nn.Parameter(torch.randn(1))
    
    def forward(self, x:torch.tensor)->torch.tensor:
        return self.weights*x + self.biases


model = linReg()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.L1Loss()

iter_num = 1


# yeah something here i guess
for i in range(iter_num):

    model.train()


root = tk.Tk()

root.geometry(str(b_height)+'x'+str(b_width))

text = tk.Text(root, height=b_height, width=b_height, background='black', foreground='white')
text.pack()

text.insert(tk.END, torch.zeros(4,2))

tk.mainloop()
