# 	112A - Petya and Strings
if __name__ == '__main__' :
    string_a = input().lower()
    string_b = input().lower()
    if  string_a == string_b :
        print(0)
    elif string_a < string_b :
        print(-1)
    else :
        print(1)
