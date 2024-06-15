print("Δώσε βαθμούς μαθητών")
#Ορισμός μεταβλητών μετρήσεων για υπολογισμούς
dnf = 0
sum = 0
count = 0
max = 0
#Επανάληψη επ' αορίστου μέχρι να εκληρωθεί η συνθήκη για Break
while(1):
    grade = int(input())
    if grade < 0 or grade > 100:
        break
    elif grade == 0:
        print("Δεν έγραψε")
        dnf = dnf + 1 
    elif grade < 50:
        print("Δεν πέρασες")
    elif grade < 75:
        sum = sum + grade
        count= count + 1
        print("Πέρασες")
    elif grade <90:
        sum = sum + grade
        count= count + 1
        print("Μπράβο")
    elif grade <= 100:
        sum = sum + grade
        count= count + 1
        print("Άριστα")
    if grade > max:
        max = grade   
    print("Ο Βαθμός είναι:", grade)
    print("Δώσε βαθμούς μαθητών")
#Έλεγχος αν δεν υπάρχουν μαθητές γιατί δεν μπορεί να γίνει διαίρεση με 0 στον υπολογισμό του αποτελέσματος    
if count == 0:
    print("Λάνθασμένοι Παράμετροι, τερματισμός...")
else:
    print("Max:", max, "και MO:", sum/count )
    print("Δεν έγραψαν", dnf, "άτομα διαγώνισμα")
