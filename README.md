# Simple Graph Convolution
Pytorch implementation of **Simple Graph Convolution*** as presented in [***"Simplifying Graph Convolutional Networks"***](https://arxiv.org/abs/1902.07153)

## Abstract 

## Resources

Graph Convolutional Networks (GCNs) and their variants have experienced significant attention and have become the de facto methods for learning graph representations. GCNs derive inspiration primarily from recent deep learning approaches, and as a result, may inherit unnecessary complexity and redundant computation. In this paper, we reduce this excess complexity through successively removing nonlinearities and collapsing weight matrices between consecutive layers. We theoretically analyze the resulting linear model and show that it corresponds to a fixed low-pass filter followed by a linear classifier. Notably, our experimental evaluation demonstrates that these simplifications do not negatively impact accuracy in many downstream applications. Moreover, the resulting model scales to larger datasets, is naturally interpretable, and yields up to two orders of magnitude speedup over FastGCN.

## Resources
[Paper](https://arxiv.org/abs/1902.07153) <br>
[Medium](https://medium.com/me/stats/post/dd78d4682ea1) <br>
[Authors Implementation](https://github.com/Tiiiger/SGC) <br>

## Results
This implementation of SGC on Cora Dataset gives:

Test Accuracy: 81% 

