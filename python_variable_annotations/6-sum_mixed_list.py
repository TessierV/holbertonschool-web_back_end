#!/usr/bin/env python3
"""
function sum_mixed_list take list as argument.
:mxd_lst List: float
:return: sum list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    function sum_mixed_list take list as argument.
    :mxd_lst List: float
    :return: sum list
    """
    return sum(mxd_lst)
