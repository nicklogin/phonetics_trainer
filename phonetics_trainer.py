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

def get_last_coincide(a,b):
    coincide_nmb = -1
    for sym_nmb in range(len(a)):
        if sym_nmb == len(b):
            break
        
        if a[sym_nmb] == b[sym_nmb]:
            coincide_nmb += 1
        else:
            break
    return coincide_nmb

def debug_snd_characteristic_check(snd):
    snds = preparesnds('consonants')
    snds.update(preparesnds('vowels'))
    print(snds)
    chr = debarize(input())
    s = debarize(snds[snd])
    print(chr)
    print(s)
    if chr == s:
        print('ok')
    else:
        print('something wrong!')
        divergence = get_last_coincide(chr,s) + 1
        print('divergence at ' + str(divergence))
        print(s[divergence])
        print(chr[divergence])

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
    s = 0
    a = 0
    ks = [i for i in snds.keys()]
    l = len(ks)-1
    print('зациклить выдачу?')
    order = input()
    if debarize(order) == 'да':
        answer = ''
        while answer != 'стоп':
            n = random.randint(2,10)
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
    else:
        for r in range(len(ks)):
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
        print(str(s)+'/'+str(a))

        
if __name__ == '__main__':
    main()

            
        
