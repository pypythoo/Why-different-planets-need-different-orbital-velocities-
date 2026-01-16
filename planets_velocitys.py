import math
# constants
G = 6.67430e-11 
M = 1.989e30    #mass ps the sun

#fuction to calculate orbital velocity
def orbital_v(radius):
    return math.sqrt(G * M / radius)

#taking inputs of planet
planet1 = input("enter planet1 name:")
r1= float(input("enter the radius of planet1:"))

planet2 = input("enter planet2 name:")
r2 = float(input("enter radius of planet2:"))

#calculate the velocities
v1= orbital_v(r1)
v2= orbital_v(r2)

#display result
print(f"{planet1} orbital velocity:{v1: .2f} m/s")
print(f"{planet2} orbital velocity:{v2: .2f} m/s")

#comapring values
if v1>v2:
    print(f"{planet} moves faster as it is near to the sun.")
elif v2>v1:
    print(f"{planet2} moves faster as it is near to the sun.")
else:
    print("both planet have same orbital velocity")


