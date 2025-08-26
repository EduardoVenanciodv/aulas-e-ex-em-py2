
for c in range(0, 50+1):
    print(f'\033[35m{c}\033[m')
    if c > 1 and c%2 != 0 and c%3 != 0 and c%5 != 0 and c%7 != 0 and c%11 != 0 or c == 2 or c == 3 or c == 5 or c == 7 or c == 11 :
        print('\033[32mnumero primo\033[m') 
    else:
        print('\033[31mNao e um numero primo\033[m')    
    

