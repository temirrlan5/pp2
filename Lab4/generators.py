#ex1
n = int(input())
a = (i ** 2 for i in range(1, n + 1))
for square in a:
    print(square, end=" ")

#ex2
def print_evens(N):
    for i in range(0, N+1, 2):
        yield i
n=int(input())
for i in print_evens(n):
    print(i,",", end=" ")   

#ex3
def div_3_4(N):
    for i in range(N+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for num in div_3_4(n):
    print(num)   
    
#ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)
    
#ex5
def to_zero(N):
    for i in range (n, -1, -1):
        yield i
n=int(input())
for num in to_zero(n):
    print(num, end=" ")