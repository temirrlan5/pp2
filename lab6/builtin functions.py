#ex1
l = [4, 8, 9, 7]
print(eval("*".join(map(str, l))))


# s = input()
# s = s.split()
# s = list(map(int, s))
# prod = 1
# for i in s:
#     prod*=i
# print(prod)

#ex2
s = input()
lower = 0
upper = 0
for i in range (0, len(s)):
    if s[i].islower():
        lower+=1
    elif s[i].isupper():
        upper+=1
print(f"This string has {lower} lower letters and {upper} upper letters")

#ex3
s = input()
reverse = "".join(reversed(s))
if s==reverse:
    print("it's a palindrome")
else:
    print("It is not a palindrome")
    
#ex4
import math
import time
num = float(input())
vremya = float(input())
t = vremya/1000
time.sleep(t)
print(f"Square root of {num} after {vremya} miliseconds is {math.sqrt(num)}")

#ex5
t = (4, "helo", [1, 8])
print(all(t))
