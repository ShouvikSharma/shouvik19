
### https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
li = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness=0
for i in li:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
        
print(happiness)