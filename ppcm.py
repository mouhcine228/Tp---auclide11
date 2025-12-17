def pgcd_etapes(a, b):
    print("\n=== Calcul du PGCD (Algorithme d’Euclide) ===")
    A, B = a, b
    while b != 0:
        q = a // b
        r = a % b
        print(f"{a} = {b} × {q} + {r}")
        a, b = b, r
    print(f"\n➡️ PGCD({A}, {B}) = {a}")
    return a

def ppcm(a, b):
    d = pgcd_etapes(a, b)
    lcm = abs(a * b) // d
    print(f"\n➡️ PPCM({a}, {b}) = |{a} × {b}| / {d} = {lcm}")
    return lcm

print("=== Calcul du PPCM ===")
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

ppcm(a, b)