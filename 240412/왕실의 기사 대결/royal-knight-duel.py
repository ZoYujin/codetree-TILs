l, n, q = map(int, input().split())
board = []
knights  = []
commands = []
for i in range(l):
    board.append(list(map(int, input().split())))
for j in range(n):
    knights.append(list(map(int, input().split())))
for k in range(q):
    commands.append(list(map(int, input().split())))
# print(board)#[[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 2, 0]]
# print("board[3][2]", board[3][2])
# print(knights)#[[1, 2, 2, 1, 5], [2, 1, 2, 1, 1], [3, 2, 1, 2, 3]]
# print(commands)#[[1, 2], [2, 1], [3, 3]]
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]
sum_damage = [0] * n

def move(command):
    dir = command[1]

    check = True
    for knight in knights:
        #벽/체스판 밖으로 있으면 못 감. 기사들 wXh 중 하나라도 벽때문에 못 움직이면 전부 이동X.
        #다 체크해서 전원 체스판 안에 있으면 nr, nc로 업데이트
        # (r,c)->(r+dr[dir], c+dc[dir]
        if knight[4] >0:
            # print("moving knight", knight)
            h = knight[2]
            w = knight[3]
            nr = knight[0] + dr[dir] # [nr, nr+h]
            nc = knight[1] + dc[dir] # [nc, nc+w]
            if not(1<=nr<=l and 1<=nc<=l and 1<=nr+h<=l+1 and 1<=nc+w<=l+1):
                check = False
                # print("out of board")
                break
            for i in range(nr, nr+h):
                for j in range(nc, nc+w):
                    # print("board[i-1][j-1]", i-1, j-1,board[i-1][j-1])
                    if board[i-1][j-1] == 2:
                        check = False
                        # print("barrier")
                        break
    if check == True:
        for knight in knights:
            knight[0] += dr[dir]
            knight[1] += dc[dir]
            # print("move", knight)
    return check

def damage(command):
    attacker = command[0]-1
    for idx, knight in enumerate(knights):
        if idx != attacker and knight[4] > 0:
            h = knight[2]
            w = knight[3]
            r = knight[0] # [nr, nr+h]
            c = knight[1] # [nc, nc+w]
            for i in range(r, r+h):
                for j in range(c, c+w):
                    if board[i-1][j-1] == 1:
                        knight[4] -= 1
                        sum_damage[idx] += 1
                    # print("after damage calcul:", knight)


##Main command excution##
for command in commands:
    check = move(command)
    if check:
        damage(command)
answer = 0
for idx, knight in enumerate(knights):
    if knight[4] > 0:
        # print(knight)
        # print(sum_damage[idx])
        answer += sum_damage[idx]
print(answer)