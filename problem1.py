#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""

def hypotenuse(a, b, boolean):
    input = [a, b]
    input.sort()
    if boolean == True:
        x = ((input[0]**2)+(input[1]**2))**0.5
    elif boolean == False:
        x = ((input[1]**2)-(input[0]**2))**0.5
    return (x)

if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5
    
    