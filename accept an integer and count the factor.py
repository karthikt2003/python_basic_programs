n = int(input("Enter a number:"))
count = 0
for i in range(1,n+1):
    if(n % i == 0):
        count = count + 1
        print(i)
print("count factor is:",count)
    
