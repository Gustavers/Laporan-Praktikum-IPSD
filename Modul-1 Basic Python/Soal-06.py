def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def deret_faktorial(n):
    if n == 0:
        return [1]
    else:
        return deret_faktorial(n - 1) + [faktorial(n)]

# Contoh penggunaan:
n = 4
hasil = deret_faktorial(n)
print(f"Input: n = {n}")
print(f"Output: {', '.join(map(str, hasil))}")
