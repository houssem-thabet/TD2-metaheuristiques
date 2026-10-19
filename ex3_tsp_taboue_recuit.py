import math, random

d = {(1,2):14,(1,3):15,(1,8):17,(2,3):13,(2,4):14,(2,5):20,(2,8):21,
     (3,4):11,(3,5):21,(3,6):17,(3,7):9,(3,8):9,(4,5):11,(4,6):10,
     (4,7):8,(4,8):20,(5,6):15,(5,7):18,(6,7):9,(7,8):13}

def cout(t):
    total = 0
    for a, b in zip(t, t[1:]):
        k = (min(a, b), max(a, b))
        total += d.get(k, 1000)
    return total

def voisin(t, i, j):
    return t[:i] + t[i:j+1][::-1] + t[j+1:]

depart = [1, 2, 3, 4, 5, 6, 7, 8, 1]
print("Solution initiale :", depart, "cout =", cout(depart))

print("\n--- Recherche taboue ---")
t = depart
meilleur = t
tabou = []
for it in range(1, 11):
    cands = []
    for i in range(1, 8):
        for j in range(i + 1, 8):
            v = voisin(t, i, j)
            if (i, j) not in tabou or cout(v) < cout(meilleur):
                cands.append((cout(v), i, j, v))
    c, i, j, t = min(cands)
    tabou = (tabou + [(i, j)])[-3:]
    if c < cout(meilleur):
        meilleur = t
    print("Iter", it, t, "cout =", c)
print("Meilleure tournee (taboue) :", meilleur, "cout =", cout(meilleur))

print("\n--- Recuit simule ---")
random.seed(1)
t = depart
meilleur = t
T = 20
for it in range(1, 6):
    while True:
        i, j = sorted(random.sample(range(1, 8), 2))
        v = t[:]
        v[i], v[j] = v[j], v[i]
        if cout(v) < 1000:
            break
    delta = cout(v) - cout(t)
    if delta <= 0 or random.random() < math.exp(-delta / T):
        t = v
        if cout(t) < cout(meilleur):
            meilleur = t
    print("Iter", it, "T =", T, "tournee", t, "cout =", cout(t))
    T = T * 0.5
print("Meilleure tournee (recuit) :", meilleur, "cout =", cout(meilleur))
