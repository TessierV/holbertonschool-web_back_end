#!/usr/bin/env python3
"""
Main file
"""
from typing import List
import re

def filter_datum(fields: List[str], redaction: str,
    message: str, separator: str) -> str:
    """
    Obfuscate log fields.
    """
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
        f'{item}={redaction}{separator}', message)
    return message
