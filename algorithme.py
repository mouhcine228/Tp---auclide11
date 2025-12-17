

def euclide_etendu(a, b):
    """
    Calcule le PGCD(a, b) et les coefficients (u, v)
    tels que : a*u + b*v = PGCD(a, b)
    """
    print(f"\nCalcul du PGCD étendu de {a} et {b} :")
    
    # Étape 1 : Initialisation
    u1, v1, u2, v2 = 1, 0, 0, 1  # coefficients initiaux

    while b != 0:
        q = a // b      # quotient
        r = a % b       # reste
        print(f"{a} = {b} * ({q}) + {r}")

        # Mise à jour des variables
        a, b = b, r
        u1, u2 = u2, u1 - q * u2
        v1, v2 = v2, v1 - q * v2

    print(f"\n➡️ PGCD = {a}")
    print(f"➡️ Coefficients : u = {u1}, v = {v1}")
    print(f"Vérification : ({u1})*X + ({v1})*Y = {a}")
    
    # Vérifier si les deux nombres sont premiers entre eux
    if a == 1:
        print("✅ Les deux nombres sont premiers entre eux.")
    else:
        print("ℹ️ Les deux nombres ne sont pas premiers entre eux.")

    return a, u1, v1


# --- Programme principal ---
x = int(input("Entrez le premier nombre (X) : "))
y = int(input("Entrez le deuxième nombre (Y) : "))

pgcd, u, v = euclide_etendu(x, y)
print(f"\nRésultat final : PGCD({x}, {y}) = {pgcd}")
print(f"→ Solution de l'équation : {x}*({u}) + {y}*({v}) = {pgcd}")

