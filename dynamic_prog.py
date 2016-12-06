change_var = {}
def dynamic_change(money, change):
    global change_var
    #print(money, change)
    if money <= 0:
        return 1
    if money not in change_var:
        change_var[money] = sum(dynamic_change(money - i, change) for i in change if (money - i) >= 0)
    return change_var[money]

print(dynamic_change(20, [1,5,10]))


import collections
change_var_2 = collections.defaultdict(int)


def dynamic_change_2(money, change):
    global change_var_2
    change_var_2[0] = 1
    for n in range(1, money+1):
        for i in change:
            if n - i >= 0:
                change_var_2[n] += change_var_2[n-i]
    return change_var_2[money]

print(dynamic_change_2(20, [1, 5, 10]))
print(change_var)
print(change_var_2)


def levenstein_dist(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0] * (len(y) + 1))

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distDiag, distVer)
    print(D)
    return D[-1][-1]



#print(levenstein_dist('ACGTGT', 'ACGTC'))
print(levenstein_dist('ACGTC', 'ACCGTC'))
