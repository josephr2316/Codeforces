#   266A - Stones on the Table
if __name__ == '__main__':
    size = int(input())
    colors_stones = input()
    count = 0
    for x in range(1,size):
        if colors_stones[x] is colors_stones [x-1]:
            count += 1
    print(count)

