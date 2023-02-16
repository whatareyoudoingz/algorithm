import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1) # 노드 i의 대표노드를 저장 #parent[i] : 노드 i의 부모노드

def find(a): #a의 대표노드를 찾기
    if a == parent[a]: #같다면 탈출
        return a
    else: #다르다면 대표 노드와 부모 노드와 일치할때까지 반복
        parent[a]=find(parent[a])
        return parent[a]

def union(a, b): #a,b가 속한 그룹 합치기
    a_=find(a)
    b_=find(b)
    if a_!=b_:
        parent[b_]=a_ #b의 부모를 a의 대표값으로 교체

def checkSame(a, b): # a의 대표값과 g의 대표값이 같은지 확인 
    return find(a)==find(b)
    pass

for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")