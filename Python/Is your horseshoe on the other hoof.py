# 	228A - Is your horseshoe on the other hoof?
if __name__ == '__main__' :
    colors = {int(x) for x in input().split()}
    print(4-len(colors))