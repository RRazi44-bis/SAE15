# Abdoul Hakim
def average(list_valeur):
    if list_valeur:
        return sum(list_valeur) / len(list_valeur)
    else:
        return 0
# Test
liste = [10, 5, 6, 2, 4]
print("Moyenne exacte :", average(liste))
