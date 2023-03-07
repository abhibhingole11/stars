T = int(input("Enter your name"))
for i in range(T):
    l,r = map(int,input().split())
    n = 0
    for m in range(l,r+1):
        if m%10==2 or m%10==3 or m%10==9:
            n+=1
    print(n)