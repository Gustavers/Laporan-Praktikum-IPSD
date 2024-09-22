def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_pattern(rows):
    count = 0
    for i in range(1, rows + 1):
        primes = generate_primes(count + i)

        print(" ".join(map(str, primes[count:count + i])))
        count += i

# contoh
num_rows = 4
generate_pattern(num_rows)
