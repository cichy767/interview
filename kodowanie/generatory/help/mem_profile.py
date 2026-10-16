"""Pomiar pamięci procesu w MiB."""

import os
import sys

import psutil


def memory_usage_psutil():
    """Bieżący RSS; działa również na Windows."""
    return psutil.Process(os.getpid()).memory_info().rss / (2 ** 20)


def memory_usage_resource():
    """Maksymalny RSS na Unix; moduł resource nie jest dostępny na Windows."""
    if sys.platform == "win32":
        raise NotImplementedError("Na Windows użyj memory_usage_psutil().")
    import resource

    denominator = 2 ** 20 if sys.platform == "darwin" else 1024
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / denominator
