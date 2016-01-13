import string
import random


def passgen(length=8):
    """Generate a strong password with *length* characters"""
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(pool) for _ in range(length))


def main():
    for _ in range(10):
        print passgen()
