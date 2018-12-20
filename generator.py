import random, math
from constants import chars, chars_len

"""
This code will be the overall generator for primitive data types in racket:
    Numbers
    Decimal Numbers (lol)
    Booleans
    Strings
    Characters
    Lists
"""


def generate_bool():
    return [True, False][random.randint(0, 1)]


def generate_num(min_val=-999999999, max_val=99999999):
    return random.randint(min_val, max_val)


def generate_float(min_val=-999999999, max_val=99999999):
    decimal = random.random()
    return random.randrange(min_val, math.floor(max_val-decimal))+decimal


def generate_char():
    """
    For the sake of readability and convenience, generate_char will only do alphanumeric and whitespace
    characters in racket
    """
    return random.choice(chars)


def generate_string(length=1):
    return "".join(generate_char() for i in range(length))


funcs = {'Bool': generate_bool, 'Num': generate_num, 'Float':generate_float,
         'Char':generate_char, 'Str':generate_string, 'Nat':lambda : generate_num(0, 99999999)}

any = ('Bool', 'Num', 'Float', 'Char', 'Str', 'Nat')


def generate_primitive(types=any):
    return funcs[random.choice(types)]()

"""
The next portion will handle the recursive structs of racket
it will handle it using the format (listof primitives) (listof structs)
"""

def generate_list(types=any, size=5):
    """
    sample generator for a struct, specifically list
    :param types: types of parameters allowed
    :param size: the length of the list
    :return: a randomized list
    """
    cval = funcs[random.choice(types)]()
    if size == 0:
        return None
    elif size == 1:
        return [cval]
    else:
        subcase = generate_list(types, size-1)
        subcase.append(cval)
        return subcase


