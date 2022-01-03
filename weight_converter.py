# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:10:25 2021

@author: user
"""
# complete weight conversion from kilograms, grams to pounds
#and vice versa
# when iterating through functions 
# make it possible for users to enter wrong values
#and program shouldn't knock(crash) !!

import sys
from utility import (kilo_to_pounds, pounds_to_kilo, gram_to_kilo, 
                     kilo_to_gram, pounds_to_gram, grams_to_pounds
                     )
#import unittest

#class WeightTestCase(unittest.TestCase):
#    """ TEST FUNCTIONS UNDER [UTILITY.PY] """
    
#    pass
    

while True:
    unit = input("enter (L)bs or (G)ram or (K)g:  ")
    while True:
        if unit.lower() == "l" or unit.lower() =="g" or unit.lower() == "k" or unit.lower() == "":
            break
            
        else:
            print("\n We Dont understand...\n--PLEASE ENTER L,G or K... ")
            break
        
    if unit.isspace():
        sys.exit(0)
        
    elif unit.lower() == "l":
        grams_to_pounds()
        kilo_to_pounds()
    
    
    elif unit.lower() == "g":
        kilo_to_gram()
        pounds_to_gram()
        
    
    elif unit.lower() == "k":
        gram_to_kilo()
        pounds_to_kilo()
        
         
    

    
        
        
        