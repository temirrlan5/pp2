#ex1
import math
def deg_to_rad(deg):
    rad=deg * math.pi/180
    return rad
n = int(input())
print(deg_to_rad(n))

#ex2
def area_trapezoid(h,fba,sba):
    area=((fba + sba)*h)/2
    return area
height=int(input())
a=int(input())
b=int(input())
print(area_trapezoid(height,a,b))

#ex3
import math
def area_polygon(n,length):
    return(n * length ** 2) / (4 * math.tan(math.pi / n))
n = int(input())
length = int(input())
print(area_polygon(n,length))

#ex4
def area_parallelogram(l,h):
    return l * h
length=int(input())
height=int(input())
print(area_parallelogram(length,height))

