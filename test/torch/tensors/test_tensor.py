import torch
import syft

from syft.frameworks.torch.tensors import TorchTensor, PointerTensor


def test_init(workers):
    pointer = PointerTensor(id=1000, location=workers["alice"], owner=workers["me"])
    pointer.__str__()


def test_create_pointer(workers):
    x = torch.Tensor([1, 2])
    x.create_pointer()
    x.create_pointer(location=workers["james"])
