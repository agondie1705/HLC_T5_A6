def numro(n):
    nr={
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    numro=''
    for i in sorted(nr.keys(),reverse=True):
        while n >= i:
            numro += nr[i]
            n -=i
    return numro
print(numro(9))