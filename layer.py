import math
import torch.nn as nn
import torch
from torch.nn.parameter import Parameter
from torch.nn.modules.module import Module

class SGC(nn.Module):
    def __init__(self, k, nfeat, nclass):
        super(SGC, self).__init__()
        self.k = k
        self.W = nn.Linear(nfeat, nclass)


    def forward(self, x, adj):
        k = self.k
        for i in range(k):
            x = torch.spmm(adj, x)
        x = self.W(x)
        return x