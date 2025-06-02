
def fib(x):
    if x==0 or x==1:
        return x
    else:
        return fib(x-1)+fib(x-2)
try:
    x=fib(int(input("which fib num: ")))
    print(x)
except ValueError:
    print("you tried...")
except RecursionError:
    print("i got this covered...")

