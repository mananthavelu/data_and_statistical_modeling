# Reference: https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch


# Transformers code using PyTorch - for texts
# Questions to answer
# What are parameters in the context of Transformers
# What are Hyper - parameters in the context of Transformers
# How the parameters are learned in trasformers
# Type of Input data
# Type of expected output data


# Transformer - main components
# Word embedding - Words to numbers. Consideration: number of values for each token
# Positional embedding - helps keep track of word order
# Attention - Establishes relationships with words - Mechanism to correctly associate one word with other word
# Self-attention

import torch
import torch.nn as nn# NN Module
import torch.nn.functional as F#For Softmax function

sample = nn.Linear(in_features = 2, out_features = 2)
print(sample.weight)
class SelfAttention(nn.Module):
    """

    """
    def __init__(self, d_model = 2, row_dim = 0, col_dim = 1):
        # d_model = 2 enclded integers for each token
        # row_dim = 
        # col_dim = 
        # batch_size?
        self.row_dim = row_dim
        self.col_dim = col_dim
        self.d_model = d_model
        super().__init()
        # Object to calculate the weight values for Q, K, V
        self.W_q = nn.Linear(in_features = d_model, out_features = d_model, bias = False)
        self.W_k = nn.Linear(in_features = d_model, out_features = d_model, bias = False)
        self.W_v = nn.Linear(in_features = d_model, out_features = d_model, bias = False)

    def forward(self, token_encodings):
        q = self.W_q(token_embeddings)
        k = self.W_k(token_embeddings)
        v = self.W_v(token_embeddings)
        similarities = torch.matmul(q, k.transpose(dim0=self.row_dim, dim1=self.col_dim))
        scaled_sims = sims/torch.tensor(k.size(self.col_dim)**0.5)
        attention_percents = F.softmax(scaled_sims, dim = self.col_dim)
        attention_scores = torch.matmil(attention_percents, v)

        return attention_scores

#encoding_matrix = torch.tensor()


# Encoder - Representation of an input


# Decoder - Generation of a new input


# Query Q
# Key K
# Value V






# Perceptron as Logical Operators
# AND operator

# Import the necessary libraries
import pandas as pd

# Define the inputs, expected outputs from Perceptron
inputs = [(0,0), (1,0), (0,1), (1,1)]
expected_outputs = [False, False, False, True]


# Guess the weights
weight_1 = 1
weight_2 = 1
bias = 0

actual_outputs = []
for input, expected_outputs in zip(inputs, expected_outputs):
    linear_combination = input[0]*weight_1 + input[1]*weight_2 + bias
    if linear_combination < 0:
        result = False
    else:
        result = True
    actual_outputs.append(result)

print(actual_outputs)
