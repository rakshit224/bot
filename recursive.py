def fact(n):
    if n ==0:
        return 1
    else :
        return n*fact(n-1)
num = 10
print(f"the factorial of {num} is {fact(num)}")