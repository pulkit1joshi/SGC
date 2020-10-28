import torch
import torch.nn as nn
from utils import load_data, accuracy
from layer import SGC

adj, features, labels, idx_train, idx_val, idx_test = load_data()

# Parameters currently hard coded 
epochs = 100
k = 2
lr = 0.2
wd = 0.000001




# Model and optmizer

model = SGC(k, features.size(1), labels.max().item()+1)
optimizer = torch.optim.Adam(model.parameters(), lr=lr,
                           weight_decay=wd)

# Training

for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(features, adj)
        loss_train = torch.nn.functional.cross_entropy(output[idx_train], labels[idx_train])
        loss_train.backward()
        optimizer.step()
with torch.no_grad():
            model.eval()
            output = model(features, adj)
            acc_val = accuracy(output[idx_val], labels[idx_val])
            print("Validation Loss",format(acc_val))

model.eval()
output = model(features, adj)
acc_val = accuracy(output[idx_test], labels[idx_test])
print("Test Error:", format(acc_val))

