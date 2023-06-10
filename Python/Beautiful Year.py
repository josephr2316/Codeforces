# 271A - Beautiful Year
if __name__ == '__main__':
    year = int(input())
    while True:
        year +=1
        str_year = str(year)
        a = str_year.count(str_year[0])
        b = str_year.count(str_year[1])
        c = str_year.count(str_year[2])
        d = str_year.count(str_year[3])
        if a == 1 and b == 1 and c == 1 and d == 1:
            print(year)
            break
