import time

def sum_for(n):
    sumf = 0
    for i in range(1, n+1):
        sumf += i
    return sumf

def sum_while(n):
    sum2 = 0
    i = 1
    while i <= n:
        sum2 += i
        i += 1
    return sum2

n = int(input("Enter Number: "))

sum_for(n)
time_start = time.time()
sum1 = sum_for(n)
time_end = time.time()
time_total = time_end - time_start

print(f"Using for loop: Sum is {sum1}. It took {time_total} seconds.")

sum_while(n)
time_start = time.time()
sum2 = sum_while(n)
time_end = time.time()
time_total = time_end - time_start

print(f"Using while loop: Sum is {sum2}. It took {time_total} seconds.")