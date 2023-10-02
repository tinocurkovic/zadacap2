def parni_neparni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i, "paran"
        else:
            yield i, "neparan"

n = 10
numbers = parni_neparni(n)

for number, parity in numbers:
    print(number, "je", parity)
