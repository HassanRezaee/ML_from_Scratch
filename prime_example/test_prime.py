# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:20:05 2021

@author: Koala
"""
from primes import is_prime

def test_five_is_prime():
    assert is_prime(5)==True

def test_four_is_prime():
    assert is_prime(4) == False