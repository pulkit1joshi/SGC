# Simple Graph Convolution
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/simplifying-graph-convolutional-networks/text-classification-on-ohsumed)](https://paperswithcode.com/sota/text-classification-on-ohsumed?p=simplifying-graph-convolutional-networks) [![codebeat badge](https://codebeat.co/badges/0ec71c2f-c9b1-4a29-9df9-caf1bd09e186)](https://codebeat.co/projects/github-com-pulkit1joshi-sgc-main)

Pytorch implementation of **Simple Graph Convolution*** as presented in [***"Simplifying Graph Convolutional Networks"***](https://arxiv.org/abs/1902.07153)

## Abstract 

## Resources

Graph Convolutional Networks (GCNs) and their variants have experienced significant attention and have become the de facto methods for learning graph representations. GCNs derive inspiration primarily from recent deep learning approaches, and as a result, may inherit unnecessary complexity and redundant computation. In this paper, we reduce this excess complexity through successively removing nonlinearities and collapsing weight matrices between consecutive layers. We theoretically analyze the resulting linear model and show that it corresponds to a fixed low-pass filter followed by a linear classifier. Notably, our experimental evaluation demonstrates that these simplifications do not negatively impact accuracy in many downstream applications. Moreover, the resulting model scales to larger datasets, is naturally interpretable, and yields up to two orders of magnitude speedup over FastGCN.
![SGCOverview](https://user-images.githubusercontent.com/42002993/97458724-fbfabb00-1960-11eb-8fdd-e40234f42c33.png)


## Resources
[Paper](https://arxiv.org/abs/1902.07153) <br>
[Medium](https://medium.com/me/stats/post/dd78d4682ea1) <br>
[Authors Implementation](https://github.com/Tiiiger/SGC) <br>

## Results
This implementation of SGC on Cora Dataset gives:

Test Accuracy: 81% 

