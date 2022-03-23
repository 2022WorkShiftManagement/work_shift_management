import random
import string


def randomstring(n):
    random_string = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(random_string)
