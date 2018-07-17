def addTwoDigits(n):
    if n < 10:
        return n
    return (n // 10) + (n % 10)
