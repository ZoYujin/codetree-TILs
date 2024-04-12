#방향 : 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, Q = map(int, input().split())
#벽으로 둘러싸서, 범위 체크 안 하고, 범위 밖으로 밀리지 않게 처리
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split())) + [2] for _ in range(N)] +[[2]*(N+2)]
# print(arr)
units = {}
init_k = [0]*(M+1)
for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = [si, sj, h, w, k]
    init_k[m] = k #ㅊ초기 체력 저장(ans 처리용)

def push_unit(start, dr): #BFS : s를 밀고 연쇄 처리
    q = [] #push 후보 저장
    pset = set() #visited 역할-이동시킬 기사 번호 저장
    damage = [0]*(M+1) #각 유닛별 데미지 누적
    #초기 데이터 추가
    q.append(start)
    pset.add(start)

    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = units[cur]
        #명령 받은 방향 진행, 벽이 아니면, 겹치는 다른 조각이면=> 큐에 삽입
        ni, nj = ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2: #벽이면 큐고 뭐고 취소
                    return
                if arr[i][j] == 1:
                    damage[cur]+=1
        #겹치는 다른 유닛 있는 경우 큐에 추가(모든 유닛 체크)
        for idx in units:
            if idx in pset: continue
            ti, tj, th, tw, tk = units[idx]
            #겹치는 경우
            if ni<=ti+th-1 and ni+h-1>=ti and nj<=tj+tw-1 and nj+w-1>=tj:
                q.append(idx)
                pset.add(idx)
    damage[start] = 0
    #이동, 데미지가 체력 이상이면 삭제 처리
    for idx in pset:
        si, sj, h, w, k = units[idx]
        if k<=damage[idx]:
            units.pop(idx)
        else:
            ni, nj = si+di[dr], sj+dj[dr]
            units[idx] = [ni, nj, h, w, k-damage[idx]]

for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)
ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)