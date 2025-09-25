#Name: Kavya Malav Mehta
#UID: 43001957
#Function to check if 3 given sides make a triangle
def triangle_validator(sideA,sideB,sideC):#Using sideA,sideB and sideC as parameters
    """
    Function to check if sum of 2 sides are greater than the third
    If yes, triangle is formed.
    """
    if sideA+sideB>sideC and sideB+sideC>sideA and sideC+sideA>sideB:
        return True #Returns True if sum of 2 sides are greater than third
    else:
        return False #Returns False if sum of 2 sides are less than the third
def main():
    """
    User inputs length of three sides
    """
    sideA=  int(input('Enter length of side A: '))
    sideB = int(input('Enter length of side B: '))
    sideC = int(input('Enter length of side C: '))
    print(triangle_validator(sideA, sideB, sideC)) #Calling the function
main() # Calling the main function
