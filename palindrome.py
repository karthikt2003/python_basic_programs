n = int(input("enter a number"))
a = str(n)
t = a[::-1]
d = int(t)
print(d)
if(n == d):
    print("palindrome")
else:
    print("not a palindrome")
