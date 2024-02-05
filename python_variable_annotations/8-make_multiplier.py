#!/usr/bin/env python3
"""
function make_multiplier take float.
:multiplier: float
:return: float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier take float.
    :multiplier: float
    :return: float
    """
    def multiplies(m: float):
        return m * multiplier
    return multiplies
