# 
if __name__ == '__main__' :
    cases = int(input())
    for x in range(cases):
        tsondu_monsters, tenzing_monster = input().split()
        tsondu_list = [int(x) for x in input().split()]
        tenzing_list = list(map(int,input().split()))
        while len(tsondu_list) is not 0 and len(tenzing_list) is not 0 :
            if tsondu_list[0] - tenzing_list[0] == 0:
                tenzing_list.remove(tenzing_list[0])
                tsondu_list.remove(tsondu_list[0])
                
            elif tenzing_list[0] - tsondu_list[0] < 0 :
                tsondu_list[0] -=tenzing_list[0]
                tenzing_list.remove(tenzing_list[0])
            else :
                tenzing_list[0] -= tsondu_list[0]
                tsondu_list.remove(tsondu_list[0])
        if len(tenzing_list) == len(tsondu_list)  :
            print("Draw")
        elif len(tenzing_list) == 0 :
            print('Tsondu')
        else :
            print('Tenzing')





