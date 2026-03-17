import torch
import typing as tp

def get_silu() -> tp.Callable[[torch.Tensor], torch.Tensor]:
    def fn(x):
        return x * x.sigmoid()

    return torch.compile(fn)
