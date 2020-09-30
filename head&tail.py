from random import *
from tkinter import *
from collections import *

global s

def ht():
    count=0
    for m in range (0,5):
        
        i=input()
        
        color=['head','tails']
        value=choice(color)
        
        if i==value:
            print('won')
            count+=1
        else:
            print('loose')
            count-=1
    print('the points you have is ',count)        
        
    cont=input('yes/no')
    if cont=='yes':
        ht()
        
    else:
        exit()
ht()
        
