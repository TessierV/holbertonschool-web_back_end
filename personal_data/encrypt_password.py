#!/usr/bin/env python3
"""
Main file
"""
import bcrypt


def hash_password(password):
    """
    Hashes
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def is_valid(hashed_password, password):
    """
    Validates a password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
