import random
import math

def preparesnds(filename):
    d=dict()
    with open (filename+'.txt','r',encoding='utf-8') as f:
        for line in f:
            k,v = line.strip('\n').split('\t')
            d[k] = v
    return d

def debarize(line):
    lin1 = ''
    for i in line:
        if i != ' ':
            lin1 += i
    return lin1

def main():
    print('consonants,vowels or all?')
    x = input()
    if (x == 'consonants') or (x == 'vowels'):
        snds = preparesnds(x)
    elif x == 'all':
        snds = preparesnds('consonants')
        snds.update(preparesnds('vowels'))
    else:
        print('error')
    n = int(input ('введите количество бросков: '))
    s = 0
    a = 0
    ks = [i for i in snds.keys()]
    l = len(ks)-1
    while True:
        dispersion = []
        r = random.randint(0,l)
        dispersion.append(r)
        for i in range(n-1):
            r1 = random.randint(0,l)
            r += r1
            dispersion.append(r1)
        r = int(r/n)
        print('ожидание',r)
        dispersion = [(i-r)**2 for i in dispersion]
        d = 0
        for i in dispersion:
            d += i
        d = math.sqrt(d/n)
        print('dispersion =', str(d))
        print(ks[r])
        answer = input()
        if answer == 'стоп':
            print(str(s)+'/'+str(a))
            input()
            break
        elif debarize(answer) == debarize(snds[ks[r]]):
            s += 1
            print('правильно')
        else:
            print('Неправильно')
            print('Правильный ответ - '+snds[ks[r]])
        a += 1

if __name__ == '__main__':
    main()

            
        
