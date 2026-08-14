n = 5

def Fact_N_numbers(n):
    if n==1:
        return 1
    return n * Fact_N_numbers(n-1)

print(Fact_N_numbers(n))