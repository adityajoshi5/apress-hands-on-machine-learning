#!/usr/bin/env python
"""Chapter 15: Recurrent neural network for sequence classification."""

import torch


def build_sequence_data(samples: int = 300, timesteps: int = 12):
    """Return inputs of shape (samples, timesteps, 1) and labels based on positive sequence sum."""
    x = torch.randn(samples, timesteps, 1)
    y = (x.sum(dim=1).squeeze(-1) > 0).long()
    return x, y


def main() -> None:
    x, y = build_sequence_data()

    rnn = torch.nn.RNN(input_size=1, hidden_size=16, batch_first=True)
    classifier = torch.nn.Linear(16, 2)
    criterion = torch.nn.CrossEntropyLoss()

    params = list(rnn.parameters()) + list(classifier.parameters())
    optimizer = torch.optim.Adam(params, lr=0.01)

    for _ in range(120):
        outputs, hidden = rnn(x)
        logits = classifier(hidden[-1])
        loss = criterion(logits, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    preds = classifier(rnn(x)[1][-1]).argmax(dim=1)
    acc = (preds == y).float().mean().item()

    print("Final loss:", round(float(loss.item()), 6))
    print("Training accuracy:", round(acc, 4))


if __name__ == "__main__":
    main()
