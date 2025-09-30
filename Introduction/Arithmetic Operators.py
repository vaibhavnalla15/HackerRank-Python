""" Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers. """

if __name__ == '__main__':
    a = int(input("Enter first num:- "))
    b = int(input("Enter second num:- "))
    
    add  = a + b
    diff = a - b
    multiply = a * b
    
    print(add)
    print(diff)
    print(multiply)
