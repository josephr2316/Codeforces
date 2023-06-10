# 271A - Beautiful Year
if __name__ == '__main__':
    year = int(input())
    while True:
        year +=1
        str_year = str(year)
        if len(set(str_year)) == 4:
            print(year)
            break
