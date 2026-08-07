n = 5

def SumOf_N_numbers(n):
    if n==1:
        return 1
    return n + SumOf_N_numbers(n-1)

print(SumOf_N_numbers(n))