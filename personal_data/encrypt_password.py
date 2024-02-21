#!/usr/bin/env python3
"""
Main file
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes
    """
    pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates
    """
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        valid = True
    return valid
