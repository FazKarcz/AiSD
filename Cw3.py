#ZAD1
def numbers(n :int)->None:
    if n < 0:
        return
    print(f'i: {n}')
    numbers(n-1)
#numbers(5)
#ZAD2
def fib(n: int) ->int:
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
#print(fib(10))
#ZAD3
def power(number: int,n:int)->int:
    if n == 0:
        return number == 1
    if n == 1:
        return number
    else:
        return number * power(number,n-1)
#print(power(3,2))
#ZAD4
def reverse(txt:str)->str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]
#print(reverse("dupa"))
#ZAD5
def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)
#print(factorial(0))
#ZAD6
def prime(n: int) -> bool:
    if n == 1:
        return True