#define an S-box in terms list with index corresponding to input bit
first = [3,5,2,1,6,7,4,0]
second = [10,12,11,8,9,15,13,14]
sbox = first + second
size = len(sbox)
dt = []

for i in range(size):
    dt.append([0]*size)
    #print('%X & %X \\\\\\hline' % (i, sbox[i]))

def s(x):
    return sbox[x]

def outputs():
    for i in range(size):
        print(get(i))

def diffs():
    print('   ', end='')
    for i in range(size):
        print(' %X ' % i, end=' ')
    print()
    for x in range(size):
        print('%X' % x,end='| ')
        for delx in range(size):
            dely = s(x) ^ s(x^delx)
            print('%X:%X' %(delx, dely) ,end=' ')
            dt[delx][dely] += 1
        print('')
    print()

def latex_diffs():
    for i in range(size):
        print('& %X' % i, end=' ')
    print('\\\\\\hline')
    for x in range(size):
        print('%X' % x,end=' ')
        for delx in range(size):
            dely = s(x) ^ s(x^delx)
            print('& %X' % dely, end=' ')
            dt[delx][dely] += 1
        print('\\\\\\hline')
    print()

def diff_table():
    print('   ', end='')
    for i in range(size):
        print(' %X' % i, end=' ')
    print()
    for i in range(size):
        print('%X' % i,end='| ')
        for j in range(size):
            print('%2d' % dt[i][j] ,end=' ')
        print('')

def latex_diff_table():
    for i in range(size):
        print('& %X' % i, end=' ')
    print('\\\\\\hline')
    for i in range(size):
        print('%X' % i,end=' ')
        for j in range(size):
            print('& %d' % dt[i][j] ,end=' ')
        print('\\\\\\hline')

diffs()
diff_table()
