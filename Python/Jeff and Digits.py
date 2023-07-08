# 352A - Jeff and Digits
if __name__ == '__main__' :
    size,numbers = int(input()), input()
    zero_numbers = numbers.count('0')
    five_numbers = numbers.count('5')
    five_numbers -= five_numbers % 9
    if zero_numbers == 0 : print(-1)
    elif five_numbers < 9 : print(0)
    else :
        print(f"{'5'*five_numbers}{'0'*zero_numbers}")

    