hiddenmap1=[['o','o','o','o','x'],
            ['o','x','x','o','x'],
            ['o','o','o','o','x']]
hiddenmap2=[['o','o','o'],
            ['o','x','o'],
            ['o','o','x']]

#Ορισμός κλάσης TreasureMap
class TreasureMap:
    def __init__(self,hiddenmap1):
        self.map = hiddenmap1
        #Βρίσκουμε τις σειρές και τις στήλες με την len()
        self.rows = len(self.map)
        self.columns = len(self.map[0])

    def create_hunter_map(self):
        #Με 2 εμφωλευμένες for δημιουργούμε έναν κενό χάρτη για τον hunter για κάθε σειρά και στήλη
        hunter_map=[["-" for _ in range(self.columns)] for _ in range(self.rows)]
        return hunter_map

    def update_hunter_map(self,hunter_map,position):
        #Ορίζουμε την θέση του hunter
        rows, columns = position
        thisavros = self.map[rows][columns]
        #Αν πέσει πάνω σε θησαυρό τότε ο χάρτης του hunter παίρνει x και ο γενικός χάρτης παίρνει o ώστε ο επόμενος να μην βρει τίποτα
        if thisavros == "x":
            hunter_map[rows][columns] = "x"
            self.map[rows][columns] = "o"
            return 1
        else:
            hunter_map[rows][columns] = thisavros
            return 0       

#Ορισμός κλάσης TreasureHunter
class TreasureHunter:
    def __init__(self,hunter_name, hiddenmap1):
        self.hunter_name = hunter_name
        #Εισαγωγή αρχικού χάρτη hiddenmap1
        self.map = hiddenmap1
        #Εισάγουμε τον κενό χάρτη που έχει παραχθεί από την create_hunter_map() ώστε να κάνουμε συγκρίσεις
        self.hunter_map = self.map.create_hunter_map()

    def move_on_map(self,position):
        #Αφού εισάγουμε σειρά και στήλη ορίζουμε την θέση στον χάρτη ως αυτές τις δύο παραμέτρους
        rows, columns = position
        #Ελέγχουμε αν γύρισε 0 ή 1 ώστε να ξέρουμε αν βρέθηκε θησαυρός
        ethisavrisamen = self.map.update_hunter_map(self.hunter_map, position)
        if ethisavrisamen:
            print(f"{self.hunter_name} found a treasure on island {position}!")
        else:
            print(f"{self.hunter_name} found coal on island {position}!")

    def check_status(self):
        treasure_count = 0
        #Ελέγχουμε με δυο for κάθε στοιχείο του πίνακα του κυνηγού
        for row in self.hunter_map:
            for value in row:
                if value == "x":
                    treasure_count = treasure_count + 1
        #Εκτύπωση αποτελεσμάτων όπως στο παράδειγμα
        print(f"** {self.hunter_name} status **\nMap")
        for row in self.hunter_map:
            print(' '.join(row))
        print(f"Aquired {treasure_count} treasure(s) so far!\n")

t_map = TreasureMap(hiddenmap1)

hunter_Mits = TreasureHunter("Mitsos", t_map)
hunter_Mits.move_on_map([2, 1])
hunter_Mits.check_status()
hunter_Mits.move_on_map([0, 4])
hunter_Mits.check_status()
hunter_Mits.move_on_map([0, 0])
hunter_Mits.check_status()

hunter_Lakis = TreasureHunter("Lakis", t_map)
hunter_Lakis.move_on_map([0, 4])
hunter_Lakis.check_status()