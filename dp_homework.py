from collections import deque


def min_change(money, change):  # Эта функция не работает при отсутствии 1
    changes = [0]
    for el in range(1, money + 1):
        changes.append(min(changes[el - coin] if coin <= el else money for coin in change) + 1)
    return changes[-1]


def min_change2(money, change):  # Работает без 1, но страшная
    change.sort()
    changes = [0]
    for el in range(1, money + 1):
        min_change = money
        for coin in change:
            if coin <= el:
                if changes[el - coin] < min_change:
                    min_change = el - coin
        if min_change == money:
            changes.append(money)
        else:
            changes.append(changes[min_change] + 1)
    if changes[money] == money:
        print('Couldn\'t be changed')
        return None
    return changes[money]


def min_change3(money, change):
    change.sort()
    min_change = 0
    ind = 1
    mod = money
    while mod:
        mod, div = mod % change[-ind], mod // change[-ind]
        min_change += div
        ind += 1
        if ind > len(change):
            break
    if mod:
        print('Couldn\'t be changed')
        return None
    return min_change


def min_change_w_value(money, change):
    changes = {0:[]}
    for el in range(1, money + 1):
        min_change = money
        for coin in change:
            if coin <= el:
                if len(changes[el - coin]) < min_change:
                    min_change = el - coin
        if min_change == money:
            changes[el] = []
        else:
            changes[el] = changes[min_change] + [el - min_change]
    if sum(changes[money]) == money:
        return changes[money]
    print('Couldn\'t be changed')
    return None


def levenstein_dist_dif(x, y):
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


def levenstein_dist_com(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0] * (len(y) + 1))
    path = []
    max_ = 0
    max_ind = [0, 0]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j-1]
            distVer = D[i-1][j]
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1] + 1
            else:
                distDiag = D[i-1][j-1]
            D[i][j] = max(distHor, distDiag, distVer)
            if D[i][j] > max_:
                max_ = D[i][j]
                max_ind = [i, j]

    i, j = max_ind
    while i != 0 or j != 0:
        print(i, j)
        if i == 0:
            path.append('i')
            j -= 1
            continue
        elif j == 0:
            path.append('d')
            i -= 1
            continue

        if x[i-1] == y[j-1]:
            path.append('m')
            i -= 1
            j -= 1
        elif D[i-1][j] > D[i][j-1]:
            path.append('d')
            i -= 1
        else:
            j -= 1
            path.append('i')

    path.reverse()
    x_iter = iter(x)
    y_iter = iter(y)
    align = [[],[]]
    for el in path:
        if el == 'm':
            align[0].append(next(x_iter))
            align[1].append(next(y_iter))
        elif el == 'i':
            align[0].append('-')
            align[1].append(next(y_iter))
        elif el == 'd':
            align[0].append(next(x_iter))
            align[1].append('-')
    print(''.join(align[0]))
    print(''.join(align[1]))
    return D[-1][-1]


def horse_walk(m , n):
    board = [[0 for i in range(m)] for j in range(n)]
    board[0][0] = 1
    steps = [(1, 2), (2, 1)]
    places = deque()
    places.extend(steps)
    while places:
        i, j = places.popleft()
        if i >= n or j >= m:
            continue
        if board[i][j]:
            continue
        places.extend((i + step[0], j + step[1]) for step in steps)
        print(places)
        board[i][j] = sum(board[i-step[0]][j-step[1]] if (i - step[0]) >= 0 or (j - step[1]) >= 0
                                              else 0 for step in steps)
    print(board)
    return board[-1][-1]


def horse_walk_2(m, n):
    board = [[-1 for i in range(m)] for j in range(n)]
    board[0][0] = 1
    def good(i, j):
        return (0 <= i < n and 0 <= j < m)
    def solve(i, j):
        if good(i, j):
            if board[i][j] == -1:
                board[i][j] = solve(i - 2, j - 1) + solve(i - 2, j + 1) + solve(i - 1, j - 2) + solve(i + 1, j - 2)
            return board[i][j]
        else: return 0
    return solve(n-1, m-1)


def horse_walk_2_my(m , n):  # Не правильно
    board = [[0 for i in range(m)] for j in range(n)]
    board[0][0] = 1
    steps = [(-1, 2), (2, 1)]
    places = deque()
    places.extend(steps)
    while places:
        i, j = places.popleft()
        if not board[i][j]:
            for step in steps:
                # print(board[i][j])
                if (0 <= i - step[0] < n) and (0 <= j - step[1] < m):
                    board[i][j] += board[i-step[0]][j-step[1]]
                if (0 <= i + step[0] < n) and (0 <= j + step[1] < m):
                    places.append((i + step[0], j + step[1]))
        #print(places)
    # print(board)
    steps = [(1, 2), (2, -1)]
    places = deque()
    places.extend(steps)
    while places:
        i, j = places.popleft()
        if not board[i][j]:
            for step in steps:
                # print(board[i][j])
                if (0 <= i - step[0] < n) and (0 <= j - step[1] < m):
                    board[i][j] += board[i - step[0]][j - step[1]]
                if (0 <= i + step[0] < n) and (0 <= j + step[1] < m):
                    places.append((i + step[0], j + step[1]))
                    # print(places)
                    # print(board)

    return board[-1][-1]


def C_horse(m, n):
    board = [[0 for i in range(m + 2)] for j in range(n + 2)]
    for i in range(2, n + 2):
        for j in range(2, m +2):
            board[i][j] = board[i-2][j-1] + board[i-1][j-2]
            board[2][2] = 1
    return(board[-1][-1])
