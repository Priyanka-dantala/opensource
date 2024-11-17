N=int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
for i in range(N):
    matrix[i]=matrix[i][::-1]
for row in matrix:
    print(" ".join(map(str,row)))
