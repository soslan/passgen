import string
import random


def passgen():
    """Generate a strong password"""
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(pool) for _ in range(12))


def main():
    for _ in range(10):
        print passgen()
