# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:51:09 2019

@author: STEM
"""

def cadbury(a):
    cadbury= a + 10 + 5
    print(cadbury)
    
cadbury(5)

cadbury1 = " milk chocolate"
cadbury2 = " dark chocolate"
cadbury3 = " white chocolate"
print("The chocolate bar contains",cadbury1,",",cadbury2,", and",cadbury3)

def cadburybox(a,b,c):
    print("The chocolate bar contains",a,b,"and",c)
    
cadburybox("milk chocolate","dark chocolate","white chocolate")

name = input("What is your name?")
print("Hello",name)

age = input("please enter your age")
print("Your age is",age)

ageint = int(age)
ageint=float(age)


import math

dir(math)

math.pi
math.factorial(0)
math.pow(6,15)


def cuberoot(a):
    print("The cubic root of",a,"is",math.pow(a,(1/3)))

cuberoot(8)

a=int(input("What number do you want to take the cubic root of?"))
def cuberootInteract(a):
    print("The cubic root of",a,"is",math.pow(a,(1/3)))

cuberoot(a)
