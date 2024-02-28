list = []
n = int(input("Enter a number:"))
for i in range(0,n):
    a = int(input())
    list.append(a)
list.sort(reverse = True)
print(list)
