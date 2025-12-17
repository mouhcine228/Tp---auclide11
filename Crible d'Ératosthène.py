
def crible_eratosthene(n):
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False

    p = 2
    while p * p <= n:
        if est_premier[p]:
            for multiple in range(p * p, n + 1, p):
                est_premier[multiple] = False
        p += 1

    return [i for i in range(2, n + 1) if est_premier[i]]


def afficher_tableau(nombres, colonnes=10):
    print("\n=== Tableau des nombres premiers ===\n")
    for i in range(0, len(nombres), colonnes):
        ligne = nombres[i:i+colonnes]
        print("  ".join(f"{x:4}" for x in ligne))


# -------------------------------------------------------
# Programme principal
# -------------------------------------------------------

print("=== Crible d'Ératosthène ===")
n = int(input("Entrez un nombre (ex : 100) : "))

premiers = crible_eratosthene(n)

afficher_tableau(premiers)