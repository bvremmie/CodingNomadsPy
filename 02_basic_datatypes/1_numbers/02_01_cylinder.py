'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math
pi = math.pi
r = 3.14
h = 5

volume = pi*r**2*h
surface_area = (2*pi*r*h) + (2*pi*r**2)

print(round(volume, 2))
print(round(surface_area, 2))