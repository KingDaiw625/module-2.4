numbers = list(range(1, 16))
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
