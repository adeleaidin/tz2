def _max(a):
    x = a[0]
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            x = a[i+1]
    return x

def _min(a):
    x=1000000
    for i in range(len(a)):
        if x > int(a[i]):
            x = int(a[i])
    return x

def _sum(a):
    summ = 0
    for i in range(len(a)):
        summ += a[i]
    return summ

def _mult(a):
    mult = 1
    for i in a:
        mult *= i
    return mult

def _razmah(a):
    raz= _max(a) - _min(a)
    return raz
