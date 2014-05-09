# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Filippos Lymperopoulos

This porject involved the use of recursion to create cool images of computational art.

"""

from __future__ import division
from random import randint
import Image
from math import *

def build_random_function(min_depth, max_depth):

    """The function has as inputs min_depth and max_depth. The variable min_depth 
    specifies the minimum amount of nesting for the function, while max_depth 
    specifies the maximum amount of nesting that happens for the function. In
    the end, it returns random functions. based on the ones we input"""

    functions=["sin_pi","cos_pi","square","prod","avg","x(a,b)","y(a,b)"]    
    l=["x","y"]
    depth = randint(min_depth,max_depth)
    if depth==1:
        return l[randint(0,1)]
    elif depth>1:
        rand_func=functions[randint(0,6)]
        if rand_func in functions[0:3]:
            return [rand_func, build_random_function(depth-1,depth-1)]
        elif rand_func in functions[3:]:
            return [rand_func,build_random_function(depth-1,depth-1),build_random_function(depth-1,depth-1)]
f=build_random_function(7, 8)
def evaluate_random_function(f, x, y):

    """Inputs a random function along with two random variables x,y, which 
    are within the domain of [-1,1] and outputs a value for the function."""
    
    if f[0]=="x":
        return x
    elif f[0]=="y":
        return y
    elif f[0]=="sin_pi":
        return sin(pi*evaluate_random_function(f[1],x,y))
    elif f[0]=="cos_pi":
        return cos(pi*evaluate_random_function(f[1],x,y))
    elif f[0]=="prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0]=="square":
        return evaluate_random_function(f[1],x,y)**2
    elif f[0]=="avg":
        return (evaluate_random_function(f[1],x,y)+evaluate_random_function(f[2],x,y))/2.0
    elif f[0]=="x(a,b)":
        return evaluate_random_function(f[1],x,y)
    elif f[0]=="y(a,b)":
        return evaluate_random_function(f[2],x,y)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).Then it returns the 
        output value in the given resulting range.
    """
    ratio=(val-input_interval_start)/(input_interval_end-input_interval_start)
    return (ratio*(output_interval_end-output_interval_start)+output_interval_start)
    
im = Image.new("RGB",(350,350))
red_function = build_random_function(5,14)
green_function = build_random_function(7,20)
blue_function = build_random_function(6,15)
pixels=im.load()

for i in range(350):
    for j in range(350):
        x=remap_interval(i,0,350,-1,1)
        y=remap_interval(j,0,350,-1,1)
        r1=evaluate_random_function(red_function,x,y)
        g1=evaluate_random_function(green_function,x,y)        
        b1=evaluate_random_function(blue_function,x,y)
        r=remap_interval(r1,-1,1,0,255)
        g=remap_interval(g1,-1,1,0,255)
        b=remap_interval(b1,-1,1,0,255)
        pixels[i,j]=(int(r), int(g), int(b))

im.save("example1.JPEG")
    
if __name__=="__main__":
    print f
    print evaluate_random_function(f, .4, .7)