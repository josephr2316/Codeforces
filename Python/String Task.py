# 	118A - String Task
import re
if __name__ == '__main__' : string = input() ;string = string.lower() ; 
string = re.sub('[AEIOUYaeiouy]','',string)
for i in string :
    print(f".{i}", end='')