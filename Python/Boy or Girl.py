# 	236A - Boy or Girl
if __name__ == '__main__':
    user_name = input()
    set_name = set(user_name)
    if len(set_name) % 2 is 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')