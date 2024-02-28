list = []
n = int(input("Enter a number:"))
for i in range(0,n):
    a = int(input())
    list.append(a)
print(list)

even = 0
for j in list:
    if(j%2==0):
        print(j,end=" ")
        even = even + 1
print("\ncount of even number:",even)
