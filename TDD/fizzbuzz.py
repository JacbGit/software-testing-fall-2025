# -*- coding: utf-8 -*-
"""Funcion FizzBuzz"""


def fizzbuzz(num):
    """Revisa si es divisible entre 3 y 5 y regresa FIZZ o BUZZ o ambos respectivamente"""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)
