def fatorial(n,show=False):
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
        if show:
            if i > 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')
    return fat

print(fatorial(4,))
print(fatorial(5,True))




fatorial(3)