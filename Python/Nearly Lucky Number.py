#   110A - Nearly Lucky Number
if __name__ == '__main__':
    number = input()
    lucky = number.count("7") + number.count("4")

    if lucky == 7 or lucky == 4:
         print('YES')
    else:
        print('NO')