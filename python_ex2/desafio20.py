
for c in range(1, 5+1):
    peso = float(input('Digite seu peso corporal: '))
    if c == 1:
        p1 = peso + 0
    elif c == 2:
        p2 = peso + 0
    elif c == 3:
        p3 = peso + 0
    elif c == 4:
        p4 = peso + 0 
    elif c == 5:
        p5 = peso + 0
        if p1 > p2 and p1 > p3 and p1 > p4 and p1 > p5 :
            print('\033[34mMaior peso lido:{}\033[m'.format(p1))     
        if p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5 :
            print('\033[34mMaior peso lido:{}\033[m'.format(p2)) 
        if p3 > p1 and p3 > p2 and p3 > p4 and p3 > p5 :
            print('\033[34mMaior peso lido:{}\033[m'.format(p3)) 
        if p4 > p2 and p4 > p3 and p4 > p1 and p4 > p5 :
            print('\033[34mMaior peso lido:{}\033[m'.format(p4)) 
        if p5 > p2 and p5 > p3 and p5 > p4 and p5 > p1 :
            print('\033[34mMaior peso lido:{}\033[m'.format(p5)) 
        
        if p1 < p2 and p1 < p3 and p1 < p4 and p1 < p5 :
            print('\033[35mMenor peso lido:{}\033[m'.format(p1))     
        if p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5 :
            print('\033[35mMenor peso lido:{}\033[m'.format(p2)) 
        if p3 < p1 and p3 < p2 and p3 < p4 and p3 < p5 :
            print('\033[35mMenor peso lido:{}\033[m'.format(p3)) 
        if p4 < p2 and p4 < p3 and p4 < p1 and p4 < p5 :
            print('\033[35mMenor peso lido:{}\033[m'.format(p4)) 
        if p5 < p2 and p5 < p3 and p5 < p4 and p5 < p1 :
            print('\033[35mMenor peso lido:{}\033[m'.format(p5))
