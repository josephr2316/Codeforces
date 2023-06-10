
def calculate_factorial(number):
    if number == 1 :
        return 1
    else:
        print("Before the execution")
        print(number)
        m = number * calculate_factorial (number-1)
        print(m)
        print("After execution")
        return m
    
if __name__ == '__main__':
    n = int(input('Insert a number: ', ))
    value = calculate_factorial(n)
    print(value)
