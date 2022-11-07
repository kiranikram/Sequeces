"""Sine waves dataset + helpers."""

from __future__ import annotations

import typing as tp

import numpy as np
import torch


def random_chunks(raw: np.ndarray, num_chunks: int, sequence_length: int) -> np.ndarray:
  data = []
  num_data = len(raw)
  for _ in range(num_chunks):
    start = np.random.randint(0, num_data - sequence_length - 1)
    end = start + sequence_length + 1
    data.append(raw[start:end])
  return np.array(data)


def shuffle(data: np.ndarray, seed: tp.Optional[int] = None) -> np.ndarray:
  np.random.seed(seed)
  shuffle_indices = np.random.permutation(len(data))
  return data[shuffle_indices]


def batched_autoregressive_iterator(
    data: np.ndarray, 
    *, 
    batch_size: int,
) -> tp.Iterator[Batch]:
  num_data = len(data)
  # Dropping remainder
  data = data[:(batch_size * num_data // batch_size)]
  for idx in range(0, num_data - batch_size, batch_size):
    sequences = data[idx:(idx + batch_size)]
    context = sequences[:, :-1, :]
    target = sequences[:, 1:, :]
    yield Batch(context, target)



class Batch(tp.NamedTuple):
  # Multivariate sequence prediction
  inputs: np.ndarray  # [B, T, D]
  outputs: np.ndarray  # [B, T, D]


def signal_only(batch: Batch, signal_idx: int = 1) -> Batch:
  return Batch(
      inputs=batch.inputs[..., signal_idx][..., None], 
      outputs=batch.outputs[..., signal_idx][..., None],
  )

def to_tensor(batch: Batch) -> Batch:
  return Batch(
      inputs=torch.tensor(batch.inputs, dtype=torch.float32),
      outputs=torch.tensor(batch.outputs, dtype=torch.float32),
  )


def train_test_split(
    data: np.ndarray,
    train_ratio: float = 0.8
) -> tp.Tuple[np.ndarray, np.ndarray]:
    num_train = int(len(data) * train_ratio)
    train_data = data[:num_train]
    test_data = data[num_train:]
    assert len(train_data) + len(test_data) == len(data)

    return train_data, test_data


def make_default_iterator(
    data: np.ndarray,
    batch_size: int,
    seed: tp.Optional[int] = None,
) -> tp.Iterator[Batch]:
    data = shuffle(data, seed)
    iterator = batched_autoregressive_iterator(data, batch_size=batch_size)
    iterator = map(signal_only, iterator)
    iterator = map(to_tensor, iterator)
    return iterator