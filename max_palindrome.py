#check on the palindrome
def is_pal(pal):
    half_len = int(len(pal) / 2.0)
    if len(pal) % 2 == 0:
        if pal[:int(half_len):1] == pal[:int(half_len)-1:-1]: return True
    else:
        if pal[:int(half_len):1] == pal[:int(half_len):-1]: return True


#return list with Prime numbers in range x,y
def primes(x, y):
    arr = []
    if x % 2 == 0: x += 1
    for z in range(x, y, 2):
        i = 2
        while i < z:
            if z % i == 0: break
            if i == z-1: arr.append(z)
            i += 1
    return arr


#multiple prime numbers and return palindromes
def res_pal(primes):
    pal = {}
    pal_only = []
    for i in range(len(primes)-1):
        z = i
        while z < len(primes)-1:
            x = primes[i] * primes[z + 1]
            if is_pal(str(x)):
                pal[x] = [primes[i], primes[z + 1]]
                pal_only.append(x)
            z += 1
    return pal,pal_only


#print max palindrome and multipliers
def max_pal(x,y):
    pr = primes(x, y)
    pal = res_pal(pr)
    res = max(pal[1])
    mult1 = pal[0][res][0]
    mult2 = pal[0][res][1]
    print("Max palindrome is : %d" % res)
    print("Multipliers: %d , %d" % (mult1, mult2))


while True:
    try:
        max_pal(int(input("Take numbers from: ")),int(input("Take numbers to: ")))
    except:
        ValueError
        print("no one palindrome found")