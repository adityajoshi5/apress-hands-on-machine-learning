#!/usr/bin/env python
"""Chapter 12: Tensor creation, autograd, and a tiny linear layer."""

import torch


def main() -> None:
    features = torch.tensor([[1.0, 2.0], [3.0, 4.0], [2.5, 1.0]])
    targets = torch.tensor([[1.0], [2.0], [1.2]])

    layer = torch.nn.Linear(2, 1)
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(layer.parameters(), lr=0.05)

    for _ in range(100):
        optimizer.zero_grad()
        preds = layer(features)
        loss = criterion(preds, targets)
        loss.backward()
        optimizer.step()

    print("Final loss:", round(float(loss.item()), 6))
    print("Learned weights:", layer.weight.data)


if __name__ == "__main__":
    main()
