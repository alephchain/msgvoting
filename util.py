from random import randint
from config import *


def generate_bit():
    return str(randint(0, 1))


def generate_boolean_function():
    bf = ""
    for i in range(function_size):
        bf += generate_bit()

    return bf


def generate_msg_properties():
    bf = ""
    for i in range(msg_property_size):
        bf += generate_bit()

    return bf

