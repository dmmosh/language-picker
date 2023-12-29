import torch



# FUNCTIONS AND CLASSES 
class linReg(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.weight = torch.nn.Parameter(torch.randn(1))
        self.bias = torch.nn.Parameter(torch.randn(1))
    
    def forward(self, x:torch.tensor)->torch.tensor:
        return self.weights*x + self.biases