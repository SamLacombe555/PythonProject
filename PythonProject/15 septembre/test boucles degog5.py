def fete(n):
    forme = ""
    for i in range(1, n + 1):
        espaces = " " * (n - i)
        if i % 2 == 0:
            branches = "*" * (2 * i - 1)
        else:
            branches = "#" * (2 * i - 1)
        forme = forme + espaces + branches + "\n"

    forme = forme + " " * (n - 1) + "|\n"
    return forme

fete(5)
print(fete(5))