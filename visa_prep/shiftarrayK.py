n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
rotated_array=arr[-k:]+arr[:-k]
print(" ".join(map(str,rotated_array)))
