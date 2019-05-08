n=int(input())

arr=[int(n) for _ in input().split()]
sum=0

for i in arr:
    sum+=i
print(sum)