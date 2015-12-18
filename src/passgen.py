import string
import random


def generate():
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits

    return ''.join(random.SystemRandom().choice(pool) for _ in range(12))


def passgen():
    for _ in range(10):
        print generate()
