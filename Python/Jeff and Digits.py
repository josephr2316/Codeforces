#
if __name__ == '__main__' :
    size = int(input())
    numbers = input()
    w = ''
    is_true = False
    for number in numbers.split() :
        w+=number
        print(w)
        if int(w) % 90 == 0 :
            print(w)
            is_true = True
            break

    if not(is_true):
        print(0)