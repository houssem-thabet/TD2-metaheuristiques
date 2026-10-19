cout = [[5, 3, 4],
        [6, 7, 2]]

def total(x):
    return sum(cout[i][j] * x[i][j] for i in range(2) for j in range(3))

x = [[4, 4, 0],
     [0, 1, 8]]
meilleur, c_meilleur = [l[:] for l in x], total(x)
tabou = []

for it in range(1, 11):
    candidats = []
    for j1 in range(3):
        for j2 in range(3):
            for i1, i2 in [(0, 1), (1, 0)]:

                if j1 != j2 and x[i1][j2] > 0 and x[i2][j1] > 0:
                    y = [l[:] for l in x]
                    y[i1][j1] += 1; y[i2][j2] += 1
                    y[i1][j2] -= 1; y[i2][j1] -= 1
                    mv = (i1, j1, j2)
                    if mv not in tabou or total(y) < c_meilleur:
                        candidats.append((total(y), mv, y))
    if not candidats:
        break
    c, mv, x = min(candidats)
    tabou.append((mv[0], mv[2], mv[1]))
    tabou = tabou[-3:]
    if c < c_meilleur:
        meilleur, c_meilleur = [l[:] for l in x], c
    print("Iteration", it, ": cout =", c, " meilleur =", c_meilleur)

print("Meilleure solution :", meilleur, "cout =", c_meilleur)
