# 469A - I Wanna Be the Guy
if __name__ == '__main__':
    level = int(input())
    p1 = [int(x) for x in input().split()]
    p1 = p1[1:]
    p2 = [int(x) for x in input().split()]
    p2 = p2[1:]
    set_result = p1 + p2
    count = 0;
    for lev in range(level + 1):
        if lev in set_result:
            count += 1;
    if count is level:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
