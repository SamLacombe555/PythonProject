def qlqchose_for(n):
    qlqchose = ""
    for i in range(1, n + 1):
        if i % 2 == 0:
            qlqchose += "*"
        else:
            qlqchose += "-"
    return qlqchose

qlqchose_for(10)