# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:15:04 2020

@author: gvkri
"""

def myName(name):
    print("My Name is {}".format(name))

myName('Venkat')
    
def varargsfunc(*args):
    return sum(args)*0.1

print(varargsfunc(100))
print(varargsfunc(100,100))
print(varargsfunc(100,100,100))

def kwarargsfunc(**kwargs):
    print(kwargs)
    if('fruit' in kwargs):
        print('Value is {}'.format(kwargs['fruit']))
    else:
        print('Did not find the key fruit')

kwarargsfunc(fruit='apple',animal='dog')

kwarargsfunc(animal='dog')

def varargsandkwargsfunc(*args,**kwargs):
    print(args)
    print(kwargs)
varargsandkwargsfunc(10,20,30,food='biscuit',animal='dog')


def lesser_of_two_evens(a,b):
    if(a%2==0 and b%2==0):
        result = min(a,b)
    else:
       result = max(a,b)
    return result
    
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))