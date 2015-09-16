# Function calling another function
def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2
    


# Function with control loop
def cube(number):
    ans = number**3
    return ans
    
def by_three(number):
    if (number%3)== 0:
        return cube(number)
    else:
        return False


# importing functions from another module
# in this case the sqrt() is imported from "math"
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)


