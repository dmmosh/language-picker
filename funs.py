import torch
import tkinter as tk

# FUNCTIONS

# CLASSES 
class linReg(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.weight = torch.nn.Parameter(torch.randn(1))
        self.bias = torch.nn.Parameter(torch.randn(1))
    
    def forward(self, x:torch.tensor)->torch.tensor:
        return self.weights*x + self.biases

def btn_test(window: tk.Tk, entry_window:tk.Entry)->tk.Label:
    return tk.Label(window, text=entry_window.get())

