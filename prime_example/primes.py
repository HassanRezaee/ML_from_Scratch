# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:16:24 2021

@author: Koala
"""

def is_prime(number):
    """return True if the number is prime """
    for element in range(2,number):
        if number % element == 0:
            return False
        return True
        
    
