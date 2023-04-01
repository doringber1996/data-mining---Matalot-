# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:54:52 2023

@author: dor ingber 316080159
"""

def my_func(x1,x2,x3):
    try:
        numerator= (x1+x2+x3)*(x2+x3)*x3
        denominator =  (x1+x2+x3)
        result=numerator/denominator
        if ((type(x1) is int or type(x2) is int or type(x3) is int) and denominator != 0):
            raise ValueError
    except ValueError:
        return print("Error: parameters should be float")
    except ZeroDivisionError:
        return print("Not a number – denominator equals zero")
    except TypeError:
        return print(None)
    else:
        return print(result)
        
        
x1='s'
x2=0.0
x3=0.0
my_func(x1, x2, x3)
