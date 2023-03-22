# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for ctr in range(3, int(n**0.5+1), 2):
        if n % ctr == 0:
            return False
    return True

T = int(input())
ns = []

for itr in range(T):
    ns.append(int(input()))

for n in ns:
    if is_prime(n):
        print("Prime")
        continue
    print("Not prime")
