#
if __name__ == '__main__' :
    cases = int(input())
    for x in range(cases) :
        size = int(input())
        word = input().strip()
        word_b = word
        delete_item = 0
        for z in range(size) :
            