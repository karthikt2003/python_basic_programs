list = []
n = int(input("Enter a number:"))
for i in range(0,n):
    a = int(input())
    list.append(a)
print(list)

odd = 0
for j in list:
    if(j%2==1):
        print(j,end=" ")
        odd = odd + 1
print("\ncount of odd number:",odd)
    
