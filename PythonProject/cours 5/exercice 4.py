montant = float(input("Quelle est le montant avant taxe?"))
TPS = 0.05*montant
TVQ = 0.09975*montant
TOTAL = montant + (TPS) + (TVQ)

print(f"Montant Facture: {montant:.2f}$")
print(f"Montant TPS: {TPS}$")
print(f"Montant TVQ: {TVQ}$")
print(f"Montant total: {TOTAL:.2f}$")

