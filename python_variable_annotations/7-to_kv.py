#!/usr/bin/env python3
"""
function to_kv take string and Union as argument.
:v Union: float, int
:return: Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv take string and Union as argument.
    :v Union: float, int
    :return: Tuple
    """
    return (k, v**2)
