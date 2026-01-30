def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
num = int(input("Enter how many fibonacci  number you want to generate: "))
print("fibanacci sequence:", fibonacci(num))
 