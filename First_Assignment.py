#Εκτύπωση εισαγωγικού κειμένου
print("Please give me the number of seconds")
#Εισαγωγή από τον χρήστη, με το int ορίζουμε πως το user_input θα είναι ακέραιος
user_input = int(input())
#Για ώρες, λεπτά και δευτερόλεπτα κάνουμε διαιρέσεις για να πάρουμε το υπόλοιπο και το αποτέλεσμα ορίζοντας πως όλες οι μεταβλητές είναι ακέραιοι
hours = int(user_input//3600)
remaining_secs = int(user_input%3600)
mins = int(remaining_secs//60)
secs = int(remaining_secs%60)
#Εκτυπώνουμε το αποτέλεσμα
print ("Τα δευτερόλεπτα είναι",hours,":",mins,":",secs)