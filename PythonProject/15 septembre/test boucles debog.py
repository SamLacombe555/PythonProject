def mystere_for(n):
    val = 0
    for i in range(1, n + 1):
        val = val + i**2
    return val

mystere_for(10)
