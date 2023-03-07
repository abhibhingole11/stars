n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        print(i,j)
