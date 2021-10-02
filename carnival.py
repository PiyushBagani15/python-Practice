D = list(map(int,input("Enter distances: ").strip().split()))[:10]
n = int(input("N: "))
t = int(input("t: "))
total = 0
for x in range(0,n):
    total=total+D[x]

fi=(total*2 / 100) +t

print(f"The time is {fi} ")