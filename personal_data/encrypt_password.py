#!/usr/bin/env python3
"""
Main file
"""
import bcrypt
from typing import Union

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password using bcrypt
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
