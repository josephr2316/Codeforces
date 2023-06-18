# 	282A - Bit++
if __name__ == '__main__' :
    cases = int(input())
    increment_numbers = 0;
    decrement_numbers = 0;
    for x in range(cases) :
        word = input()
        increment_numbers += word.count('++')
        decrement_numbers += word.count('--')
    print(increment_numbers-decrement_numbers)

