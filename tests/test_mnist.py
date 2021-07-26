import torch
from torchvision.datasets.mnist import MNIST


def test_mnist_for_tests():
    mnist = MNIST("/tmp", download=True)
    assert mnist.data.size() == torch.Size([60000, 28, 28])


def test_mnist_for_examples():
    mnist = MNIST(".", download=True)
    assert mnist.data.size() == torch.Size([60000, 28, 28])
