print("Δώσε χρόνια παραμονής στην εταιρία")
years_in_company = int(input())
print("Δώσε μηνιαία χρέωση")
monthly_subscrition = float(input())
if years_in_company == 1:
    discount = monthly_subscrition*0.05
    print("check in 1")
elif years_in_company == 2 or years_in_company == 3 :
    discount = monthly_subscrition*0.1
    print("check in 2")
elif years_in_company >= 4:
    discount = monthly_subscrition*0.2
    print("check in 3")
else:
    discount = monthly_subscrition*0.5
    print("check in 4")
if years_in_company == 0:
    cost = (monthly_subscrition-discount)*6 + monthly_subscrition*6
    print("Check in second 1st")
else:
    cost = (monthly_subscrition-discount)*12
    print("check in second 2nd")
print("Η ετήσια συνδρομή σου είναι", round(cost, 1), "€")