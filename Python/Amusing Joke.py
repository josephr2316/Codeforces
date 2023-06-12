#   141A - Amusing Joke
def remove_letters(str1, str2):
    for x in str1:
        if x in str2:
            str2.remove(x)
    return str2;
              
               
     
if __name__ == '__main__':
    guest_name = input()
    residence_host_name = input()
    letters = list(input())
    if len(letters) != len(guest_name) + len(residence_host_name) :
          print('NO')
    else :
        letters = remove_letters(guest_name,letters)
        letters = remove_letters(residence_host_name,letters)
        if len(letters) is 0 :
            print('YES')
        else:
            print('NO')
     
     