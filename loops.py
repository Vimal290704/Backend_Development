arr = [47, 32, 56, 90, 21]
prefix = [0] * len(arr)

prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

# for num in prefix:
#     print(num)


def isPrime(n):
    prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime and n != 1:
        return "prime"
    else:
        return "not prime"


for i in range(1, 100):
    print(i, isPrime(i))
else: 
    print("Finished")
