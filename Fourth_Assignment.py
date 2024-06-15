def euro_to_yen(euro):
    #Απλή μετατροπή σε yen με πολλαπλασιαμό
    yen = float(euro * 164.80)
    return yen

def total_cost():
    print("Δώσε σύνολο εξόδων σε €")
    expenses = 0
    #Απλή if Loop για τις 7 μέρες στο ταξίδι
    for i in range(7):
        #Βοηθητική print για την κάθε μέρα
        print("Δώσε τα έξοδα για την", i+1, "μέρα σε ¥")
        #Προσαύξηση κάθε μέρας στα τελικά έξοδα
        expenses = float(input()) + expenses
    return expenses

def yen_to_euro(yen, expenses):
    remaining_yen = yen - expenses
    #Βοηθητική print για το αποτέλεσμα
    print("Εναπομείναντα yen:", remaining_yen, "¥")
    remain_euro = remaining_yen/164.80
    #Επιστρογή μόνο το υπόλοιπο των ευρώ
    return remain_euro

#Έναρξη "main"
print("Δώσε το budget των ευρώ")
avail_euros = float(input())
conv_yen = euro_to_yen(avail_euros)
#Βρήκα  το f-string διότι το αποτέλεσμα μου έβγαζε μόνο ένα δεκαδικό ψηφίο αντί για 2
print(f"Το συνάλλαγμα σε yen είναι:  {conv_yen:.2f} yen(¥)")
tot_expenses = total_cost()
print(f"Τα έξοδα του ταξιδιού ανέρχονται σε: {tot_expenses: .2f} yen(¥)")
remain_euro = yen_to_euro(conv_yen,tot_expenses)
print(f"Τα εναπομείναντα ευρώ είναι {remain_euro:.2f} €")