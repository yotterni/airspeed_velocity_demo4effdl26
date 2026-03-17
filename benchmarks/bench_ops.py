import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import torch
from mypackage.silu import get_silu

def check_cuda_avail():
    if not torch.cuda.is_available():
        raise NotImplementedError(
            "Torch could not detect your GPU, so..."
        )


class TimeFusionCUDA:
    params = [1024, 4096]
    param_names = ["size"]

    def setup(self, size):
        check_cuda_avail()

        self.x = torch.randn(size, size, device="cuda")
        # compile if necessary
        self.silu = get_silu()
        # warmup (avoid measuring compile)
        self.silu(self.x)
        torch.cuda.synchronize()

    def time_unfused(self, size):
        self.silu(self.x)
        torch.cuda.synchronize()


class MemFusionCUDA:
    params = [1024, 4096]
    param_names = ["size"]

    def setup(self, size):
        check_cuda_avail()

        self.x = torch.randn(size, size, device="cuda")
        self.silu = get_silu()
        self.silu(self.x)
        torch.cuda.synchronize()

    def peakmem_unfused(self, size):
        self.silu(self.x)
        torch.cuda.synchronize()
