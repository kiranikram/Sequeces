"""Autoregressive models."""

import torch


class AutoregressiveLinear(torch.nn.Module):

  def __init__(self, seq_len: int, *, initialiser=torch.randn):
    super().__init__()
    self.W = torch.nn.Parameter(initialiser(size=(seq_len, seq_len)))
    self.b = torch.nn.Parameter(initialiser(size=(seq_len,)))
    self.mask = torch.tril(torch.ones((seq_len, seq_len)))

  def __call__(self, inputs: torch.Tensor):
    batch_size, seq_len, element_size = inputs.shape
    inputs = torch.squeeze(inputs, axis=-1)
    out = torch.matmul(inputs, (self.mask * self.W).T) + self.b
    return out.reshape(batch_size, seq_len, 1)
    #change


class AutoregressiveLSTM(torch.nn.Module):

  def __init__(self, *, hidden_size: int = 32, num_layers: int = 1):
    super().__init__()
    self.lstm = torch.nn.LSTM(1, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
    self.linear = torch.nn.Linear(in_features=hidden_size, out_features=1)

  def __call__(
      self, 
      inputs: torch.Tensor,  # [batch_size, sequence_length, element_size]
  ) -> torch.Tensor:  # [batch_size, sequence_length, element_size]

    batch_size, sequence_length, _ = inputs.shape

    # "Seq2Seq style" forward pass.  
    output, _ = self.lstm(inputs)  # Zeros initial state.
    output = self.linear(output)
    assert output.shape == (batch_size, sequence_length, 1)
    return output


class AutoregressiveTransformer(torch.nn.Module):

  def __init__(self, embedding_size: int = 32, *, ffw_fanout: int = 4):
    super().__init__()
    self.initial_linear = torch.nn.Linear(1, embedding_size)
    self.transformer = torch.nn.TransformerEncoderLayer(
        d_model=embedding_size, nhead=2, dim_feedforward=ffw_fanout * embedding_size, dropout=0, batch_first=True)
    self.final_linear = torch.nn.Linear(embedding_size, 1)

  def __call__(self, inputs):
    _, sequence_length, _ = inputs.shape

    mask = torch.tril(torch.ones(size=(sequence_length, sequence_length)))
    
    x = self.initial_linear(inputs)
    x = self.transformer(x, mask)
    
    return self.final_linear(x)