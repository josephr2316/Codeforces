# 	1811A - Insert Digit
if __name__ == '__main__' :
    cases = int(input())
    for x in range(cases):
        lst = list(map(int,input().split()))
        word = input()
        for m in range(lst[0]):
            if int(word[m]) < lst[1] and m == 0:
                new_lst = list(word)
                new_lst.insert(m,lst[1])
                break;
            elif m < lst[0] -1 and int(word[m]) >= lst[1] and int(word[m + 1]) < lst[1] :
                new_lst = list(word)
                new_lst.insert(m + 1,lst[1])
                break;
            elif m == lst[0] -1 :
                new_lst = list(word)
                new_lst.append(str(lst[1]))
                break;
        print(''.join([str(x) for x in new_lst]))

