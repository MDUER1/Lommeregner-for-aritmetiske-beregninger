"""Dette er en Lommeregner, som kan udfører normale aritmetiske beregninger"""
# variabler + spørgsmål til brugeren
operation = input("Hvilken regneoperation vil du benytte? (+,-,*,/):")
tal_1 = int(input("Indtast dit første tal:"))
tal_2 = int(input("indtast dit andet tal:"))

# Funktioner


def lommeregner(tal_1, tal_2, operation):
    svar = None

    if operation == "+":
        svar = tal_1 + tal_2
    elif operation == "-":
        svar = tal_1 - tal_2
    elif operation == "*":
        svar = tal_1 * tal_2
    elif operation == "/" and tal_2 != 0:
        svar = round(tal_1 / tal_2, 2)
    else:
        print("fejl")
        return None
    return svar


svar = lommeregner(tal_1, tal_2, operation)
print(f"Dit resultat er {svar}")
