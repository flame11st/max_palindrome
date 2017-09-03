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
