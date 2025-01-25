# %% [markdown]
# # PHYS 3266/6260: Homework 2, Krish Kakadiya

# %% [markdown]
# ## Problem 1
# 
# For this I defined each constant seperately, and then also defined fractions seperately so the final call for the result is cleaner.

# %% [markdown]
# ###
#  The first three lines defined the three constants we need, and then our input T is turned into a float.
#  It computes the height h using the values provided and prints it.
#  The following after that calculates heights for periods of one day, 90 minutes, and for 45 minutes.

# %%
import numpy
import math
G = 6.67*10**(-11)
M = 5.97*10**(24)
R = 6371*10**(3)
def calculateheight(T):
    h1 = (G*M*T**2)
    h2 = (4*(math.pi)**2)
    h = (h1/h2)**(1/3) - R
    return(h)
twentyfourhouraltitude = calculateheight(24*60*60)
print("Height for a period of one day:",twentyfourhouraltitude)
print("Height for a period of 90 minutes:",calculateheight(90*60))
print("Height for a period of 45 minutes:",calculateheight(45*60))

# %% [markdown]
# The height for one day is 35855910.176 m, for 90 minutes it is 279321.625 m, for 45 minutes it is -2181559.8978 m

# %% [markdown]
# b) The period cannot be 45 minutes (or less than that) as it implies the satellite is at a negative altitude, also telling us that an object cannot physically and circularly orbit the Earth at any altitude with a period of 45 minutes (or less).
# 

# %% [markdown]
# c) The difference of the orbit between a 24 hour and a sideral day is the following:

# %%
geosynchrousorbitaltitude = calculateheight(23.93*60*60)
print("The difference between a 24 hour and a geosynchronous orbit is:", twentyfourhouraltitude - geosynchrousorbitaltitude)


# %% [markdown]
# ## Problem 2

# %% [markdown]
# The first line takes x in light years and converts it to meters, the second takes in v as a fraction of c, such as 0.1, 0.5, up to 1.
# 

# %% [markdown]
# The lines after that define the function and use the equation to calculate delta t for the moving frame, and converts it from seconds to years.

# %%
x = float(input("Enter distance travelled x in light years"))*(9.461*10**15)
v = float(input("Enter v as a fraction of c"))
c = 299792458
def calculatedeltat(x,v):
    deltat = x/(v*c)
    gamma = v
    deltatmovingframe = deltat*(1-(gamma)**2)**(1/2) / (60*60*24*365)
    return(deltatmovingframe)
print("Time it takes in seconds for the moving frame for",x/(9.461*10**15),"light years","(",x,"meters) with a speed of",v,"c:",calculatedeltat(x,v),"years")
print("Time it takes for the rest frame/stationary observer:",x/(v*c)/(60*60*24*365),"years")

# %% [markdown]
# For 10 light years with a speed of 0.99c, it returns 1.42 years for the moving frame and for the rest frame it returns 10.1 years

# %% [markdown]
# ## Problem 3
# The first few lines define the constants, and the last three store the values for a5 for different conditions.
# The if and elif functions check if A and Z are even or odd using modulo, and use the corresponding value for $a_5$ in the equation.

# %%
a1=15.67
a2=17.23
a3=0.75
a4=93.2
a5Aodd=0
a5AZeven=12
a5AevenZodd=-12
A = float(input("Enter the value of A"))
Z = float(input("Enter the value of Z"))

def B(a5):
    B = a1*A - a2*A**(2/3) - a3*(Z**2)/(A**(1/3)) - a4*((A-2*Z)**2)/A + a5/(A**(1/2))
    return(B)

def B(a5):
    B = a1*A - a2*A**(2/3) - a3*(Z**2)/(A**(1/3)) - a4*((A-2*Z)**2)/A + a5/(A**(1/2))
    return(B)

if A % 2 != 0:
    print("The binding energy is:",B(a5Aodd),"MeV")
    print("The binding energy per nucleon B/A is:",B(a5Aodd)/A,"MeV")
    
elif A % 2 == 0 and Z % 2 == 0:
    print("The binding energy is:",B(a5AZeven),"MeV")
    print("The binding energy per nucleon B/A is:",B(a5AZeven)/A,"MeV")
    
elif A % 2 == 0 and Z % 2 != 0:
    print("The binding energy is:",B(a5AevenZodd),"MeV")
    print("The binding energy per nucleon B/A is:",B(a5AevenZodd)/A,"MeV")



# %% [markdown]
# for A = 58, Z = 28, the function returns 493 eV


