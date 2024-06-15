class Army:
    def __init__(self,nation,mil_count,origin):
        #Αποθήκευση μεταβλητών σε self.
        self.nation = nation
        self.soldiers = mil_count
        self.origin = origin

    def title(self):
        return "Army"
    
    def status(self):
        #Εμφάνιση αποτελσμάτων κατάσταση στρατού
        print(f"{self.nation}'s {self.title()} status:")
        print(f"The military count is {self.soldiers} and their homeland is {self.origin}")
        
    def __add__(self,second):
        if isinstance(second,Army) and second.nation == self.nation:
            #Προσθήκη νέων πόλεων
            self.origin = list(set(self.origin + second.origin))
            #Προσθήκη του 20%
            self.soldiers += int(second.soldiers * 0.2)
            if self.soldiers >= 3000:
                return Legion(self.nation, self.soldiers, self.origin)
        return self


    def __sub__(self,second):
        if isinstance(second, Army):
            #Αφαίρεση 80%
            self.soldiers -= int(second.soldiers * 0.8)
            if self.soldiers <= 0:
                return None
        return self

class Legion(Army):
    #Κληρονόμηση από την Army
    def __init__(self,nation,mil_count,origin):
        super().__init__(nation,mil_count,origin)

    def title(self):
        return "Legion"
    
    def _add__(self,second):
        if isinstance(second,Army) and second.nation == self.nation:
            #Προσθήκη νέων πόλεων και +40% στρατιωτών
            self.origin = list(set(self.origin + second.origin))
            self.soldiers += int(second.soldiers * 0.4)
        return self
    
    def __sub__(self,second):
        if isinstance(second,Army):
            #Αφαίρεση 60% και έλεγχος στρατιωτών
            self.soldiers -= int(second.soldiers * 0.6)
            if self.soldiers <= 0:
                return None
            elif self.soldiers < 3000:
                return Army(self.nation, self.soldiers, self.origin)
        return self


greeks=Army("Greece",2800,["Athens"])
#Στρατεύματα στην πορεία που ακολουθούν οι Έλληνες
world_map=[
    Army("Greece",500,["Athens"]),
    Army("Persia",100,["Persepolis"]),
    Army("Greece",1000,["Athens","Sparta"]),
    Army("Greece",100,["Thebes"]),
    Army("Persia",500,["Susa"]),]

#Πέρασμα από όλα τα στρατεύματα του χάρτη
for army in world_map:
    print()
    if army.nation == greeks.nation:
        print("More soldiers added to the ranks!")
        greeks += army
    else:
        print("Battle initiated! Some didn't arrive...")
        greeks -= army
    greeks.status()

#Δοκιμή εξολόθρευσης στρατεύματος
greeks -= Army("Unknown", 100000, [])
print("The apocalypse is upon us...")
print("Your army was defeated...")