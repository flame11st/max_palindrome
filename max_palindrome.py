#check on the palindrome
def is_pal(pal):
    half_len = int(len(pal) / 2.0)
    if len(pal) % 2 == 0:
        if pal[:int(half_len):1] == pal[:int(half_len)-1:-1]: return True
    else:
        if pal[:int(half_len):1] == pal[:int(half_len):-1]: return True