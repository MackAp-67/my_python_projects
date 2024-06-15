#Με την εναλλαγή του αριθμού για την εκάστοτε λίστα δοκιμάζουμε διαφορετικές τιμές και έχουμε διαφορετικά αποτελέσματα
sokolates1 = [155, 77, 141, 73, 90, 192, 181, 149, 148, 77, 168, 143,
100, 72, 149, 195, 124, 193, 102, 186, 165, 141, 135, 189,
81, 130, 183, 99, 108, 139, 143, 138, 169, 160, 156, 72, 93,
156, 124, 166, 76, 122, 104, 174, 173, 91, 177, 143, 104, 183,
97, 125, 177, 155, 152, 175, 192, 155, 80, 109, 82, 174, 176, 76,
165, 96, 87, 115, 72, 112, 169, 184, 172, 95, 104, 137, 183, 160,
131, 188, 98, 113, 88, 91, 127, 123, 95, 183, 137, 75, 72, 113, 75,
127, 128, 142, 196, 115, 131, 70]

sokolotes2 = [134, 160, 178, 97, 86, 79, 88, 176, 107, 146, 179, 115, 149, 139, 192, 188, 100, 167,
191, 184, 194, 95, 120, 107, 85, 118, 84, 181, 120, 159, 81,131, 136, 189, 117, 153, 121, 
155, 123, 165, 199, 98, 198, 143, 177, 110, 76, 94, 147, 126, 82, 72, 112, 138, 121, 147,
151, 185, 87, 134, 146, 75,180, 200, 160, 146, 142, 94, 178, 134, 164, 146, 162, 143, 104,
121, 102, 164, 143, 123, 102, 112, 129, 71, 142, 187, 195, 198, 164, 132, 137, 164,138, 96, 
138, 101, 177, 189, 123, 166]

sokolotes3 = [147, 161, 156, 100, 103, 196, 76, 150, 122, 183, 116, 193, 162, 107, 177, 157, 177, 116, 181, 89, 96, 134, 98,
159, 155, 150, 92, 106, 108, 172, 183, 160, 78, 102, 89, 107, 157, 198, 82, 109, 77, 164, 97, 190, 112, 103, 76,
164, 178, 152, 128, 123, 143, 145, 195, 77, 177, 83, 85, 75, 117, 126, 85, 76, 185, 116, 173, 137, 197, 142, 74,
138, 134, 153, 173, 177, 78, 131, 115, 168, 78, 161, 109, 150, 97, 109, 107, 181, 196, 153, 104, 178, 113, 76,
135, 174, 166, 106, 108, 166]

#Για κάθε συνάρτηση δημιουργούμε μια κενή λίστα, κάνουμε parse τις εκάστοτε λίστες και με μια if ορίζουμε ποια στοιχεία από την αρχική λίστα θέλουμε να κρατήσουμε
#και τα προσθέτουμε (append) σε μια καινουρια λιστα
def find_faulty(sokolates1):
    faulty_sokolates = []
    for item in sokolates1:
        if item <= 90 or item >= 170:
            faulty_sokolates.append(item)   
    print("Το μέγεθος της λίστας των προβληματικών σοκολατών είναι:", len(faulty_sokolates)) 
    print("Και είναι η παρακάτω λίστα:\n", faulty_sokolates)   
    return(faulty_sokolates)

def find_ticket(sokolates1):
    ticket_sokolates = []
    for item in sokolates1:
        if item >= 150 and item <= 170:
            ticket_sokolates.append(item)
    #Ταξινόμηση κατά φθίνουσα σειρά
    ticket_sokolates.sort(reverse=True)
    return ticket_sokolates

def find_good(sokolates1):
    good_sokolates = []
    for item in sokolates1:
        if item >= 90 and item <= 150:
            good_sokolates.append(item)
    #παίρνουμε το σύνολο των σοκολατών και το πολ/ζουμε με 1.5 για να βρούμε το κέρδος
    kerdos = len(good_sokolates)*1.5
    print("Το κέρδος από τις πωλήσεις είναι:", kerdos)
    return good_sokolates 

def organize(faulty_sokolates, ticket_sokolates, good_sokolates):
    organized = {
        "faulty": faulty_sokolates,
        "ticket": ticket_sokolates,
        "good": good_sokolates
    }
    return organized

#Κλήση συναρτήσεων
faulty_sokolates = find_faulty(sokolates1)
#print(faulty_sokolates)
ticket_sokolates = find_ticket(sokolates1)
print("Η λίστα με τις σοκολάτες που μπορεί να περιέχουν το χρυσό εισιτήριο είναι, ταξινομημένη κατά φθίνουσα σειρά:\n", ticket_sokolates)
#print(ticket_sokolates)
good_sokolates = find_good(sokolates1)
#print(good_sokolates)
organized = organize(faulty_sokolates,ticket_sokolates,good_sokolates)
#Εμφανίζουμε τις λίστες με βάση τα κλειδιά
print("Οι λίστες εμφανιζόμενες ανάλογα τα κλειδιά είναι:")
print("Λίστα με τα προβληματικά:\n", organized["faulty"])
print("Λίστα με τα πιθανά εισιτήρια\n", organized["ticket"])
print("Λίστα με τις καλές σοκολάτες\n", organized["good"])