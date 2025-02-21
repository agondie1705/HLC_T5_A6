def palindromo(pl):
    if len(pl) <= 1:
        return True
    if pl[0] == pl[-1]:
        return palindromo(pl[1:-1])
    return False

p = "reconocer"
print(palindromo(p))