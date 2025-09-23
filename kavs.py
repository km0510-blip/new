def evenodd(num):
    if num%2==0:#check if number is even
        print('number is even')
    elif num==0:
        print('the number is neither even nor odd')
    else:
        print('the number odd')
def square_cube(num):
    square=num**2#square of a number
    cube=num**3#cube of a number
    print('square of',num,'is', square)
    print('cube of',num,'is', cube)
def main():
    num=int(input('enter a number: '))#asking user to input a number
    '''
    calling the two functions
    '''
    evenodd(num)
    square_cube(num)
main()