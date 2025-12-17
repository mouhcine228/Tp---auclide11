def euclide_etendu(a, b):
    """
    Calcule le PGCD(a, b) et les coefficients (u, v)
    tels que : a*u + b*v = PGCD(a, b)
    Affiche toutes les étapes de l’algorithme.
    """

    print("\n=== Algorithme d’Euclide Étendu ===")
    print(f"Objectif : Trouver PGCD({a}, {b}) et (u, v) tels que {a}u + {b}v = PGCD({a}, {b})\n")

    # Étape 1 : Algorithme d’Euclide classique
    etapes = []
    A, B = a, b
    while b != 0:
        q = a // b
        r = a % b
        etapes.append((a, b, q, r))
        print(f"{a} = {b} × {q} + {r}")
        a, b = b, r

    d = a  # PGCD
    print(f"\n➡️ PGCD({A}, {B}) = {d}\n")

    # Étape 2 : Remontée (calcul de u et v)
    print("=== Étapes de la remontée (calcul de u et v) ===\n")

    u1, v1 = 1, 0
    u2, v2 = 0, 1

    for i, (a_i, b_i, q_i, r_i) in enumerate(etapes):
        u1, u2 = u2, u1 - q_i * u2
        v1, v2 = v2, v1 - q_i * v2
        print(f"Étape {i+1}: q = {q_i} → u = {u1}, v = {v1}")

    u, v = u1, v1
    print(f"\n➡️ Coefficients de Bézout : u = {u}, v = {v}")
    print(f"➡️ Vérification : {A}*({u}) + {B}*({v}) = {A*u + B*v}")

    # Vérification de la relation de Bézout
    if A * u + B * v == d:
        print("✅ Relation vérifiée : a*u + b*v = PGCD(a,b)\n")
    else:
        print("❌ Relation non vérifiée.\n")

    return d, u, v


def resoudre_diophantienne(a, b, c):
    """
    Résout l’équation diophantienne ax + by = c.
    Utilise l’algorithme d’Euclide étendu pour trouver les solutions.
    """

    print("\n=== Résolution de l’équation diophantienne ===")
    print(f"Équation : {a}x + {b}y = {c}")

    # Étape 1 : Calcul du PGCD et des coefficients
    d, u, v = euclide_etendu(a, b)

    # Étape 2 : Vérifier si d divise c
    if c % d != 0:
        print(f"❌ Pas de solution entière car {d} ne divise pas {c}.")
        return
    else:
        print(f"✅ Il existe des solutions entières car {d} divise {c}.\n")

    # Étape 3 : Calcul d'une solution particulière
    k = c // d
    x_p = u * k
    y_p = v * k

    print(f"➡️ Solution particulière : (xₚ, yₚ) = ({x_p}, {y_p})")
    print(f"Vérification : {a}*({x_p}) + {b}*({y_p}) = {a*x_p + b*y_p} = {c}")

    # Étape 4 : Solution générale
    alpha = b // d
    beta = -a // d
    print("\n=== Solution générale ===")
    print(f"(x, y) = ({x_p} + {alpha}k, {y_p} + {beta}k), k ∈ ℤ")

    print("\n✅ Résolution complète terminée.")


# -------------------------------------------------------
# Programme principal
# -------------------------------------------------------
print("=== TP : Équations diophantiennes linéaires ===")

# --- Mode interactif ---
a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))
c = int(input("Entrez la valeur de c : "))

resoudre_diophantienne(a, b, c)