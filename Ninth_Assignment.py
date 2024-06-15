class Pokemon:
    def __init__(self,name,max_hp):
        #Ορισμός
        self.name = name
        self.max_hp = max_hp
        self.__current_hp = max_hp
        self.level = 1
        self.type = "normal"

    def hp_status(self):
        #Εμφανίζουμε τo current_hp των πόκεμον
        message1 = f"{self.name} : {self.__current_hp} / {self.max_hp}"
        print(message1)

    def level_up(self):
        #Ανεβαίνουν επίπεδο τα πόκεμον και αυξάνονται οι πόντοι ζωής
        self.level = self.level + 1
        self.max_hp = self.max_hp + int(self.max_hp* 0.1)
        self.__current_hp = self.__current_hp + int(self.max_hp* 0.1)
        message2 = f"{self.name} : has leveled up to level {self.level}!"
        print(message2)

    def take_damage(self,dmg):
        #Αφαίρεση ζωής μετά από επίθεση και έλεγχος να είναι 0 το current_hp
        dmg = int(dmg)
        message3 = f"{self.name} lost {dmg} hp..."
        message4 = f"{self.name} has fainted..."
        if dmg > self.__current_hp:
            self.__current_hp = 0
            print(message3)
            print(message4)
        else:
            self.__current_hp = self.__current_hp - dmg
            print(message3)
    
    def restore_hp(self,heal):
        #Μετατρέπουμε το heal σε ακέραιο και προσθέτουμε το heal στην ζωή του πόκεμον
        message5 = f"{self.name} has restored {heal} hp!"
        heal = int(heal)
        if (heal+self.__current_hp > self.max_hp):
            self.__current_hp = self.max_hp
        else:
            self.__current_hp = self.__current_hp + heal
        print(message5)

    def attack(self,defender,dmg):
        #Απλή επίθεση και καλόύμε την take_damage για να αφεραιθεί από το Hp των πόκεμον
        message6 = f"{self.name} used a normal attack against {defender.name}!"
        print(message6)
        defender.take_damage(dmg)

class FirePokemon(Pokemon):
    def __init__(self,name,max_hp):
        #Inheritance του fire pokemon από την Κλάση pokemon
        super().__init__(name,max_hp)
        self.type = "fire"
    
    def fire_attack(self,defender,dmg):
        #Υπολογίζουμε ανάλογα το είδος του αμυνόμενου το damage που θα έχει 
        message7 = f"{self.name}, used a fire attack against {defender.name}!"
        print(message7)
        if defender.type == "grass":
            dmg = dmg*1.5
        elif defender.type == "water":
            dmg = dmg*0.5
        defender.take_damage(dmg)

    def burn(self,defender):
        #Αφαιρούμε το Burn damage από την ζωή του άλλου πόκεμον
        message8 = f"{self.name} used burn against {defender.name}!"
        print(message8)
        burn_dmg = defender.max_hp - int(defender.max_hp-0.1)
        defender.take_damage(burn_dmg)


class GrassPokemon(Pokemon):
    def __init__(self, name, max_hp):
        #Inheritance του grass pokemon από την Κλάση pokemon
        super().__init__(name, max_hp)
        self.type = "grass"

    def grass_attack(self, defender,dmg):
        #Υπολογισμός επίθεσης ανάλογα τον τύπο του αμυνόμενου και κλήση της take_damage
        message9 = f"{self.name}, used a grass attack against {defender.name}!"
        print(message9)
        if defender.type == "water":
            dmg = dmg*1.5
        elif defender.type == "fire":
            dmg = dmg*0.5
        defender.take_damage(dmg)

    def absorb(self,defender):
        #Υπολογισμός ταυτόχρονα του damage Και του heal που θα έχει με αυτήν την επίθεση
        message10 = f"{self.name} used absorb against {defender.name}!"
        print(message10)
        absorb_dmg = (defender.max_hp * 0.05)
        defender.take_damage(absorb_dmg)
        healing = self.max_hp * 0.05         
        self.restore_hp(healing)
        
class WaterPokemon(Pokemon):
    def __init__(self, name, max_hp):
        #Inheritance του water pokemon από την Κλάση pokemon
        super().__init__(name, max_hp)
        self.type = "water"

    def water_attack(self,defender,dmg):
        #Υπολογισμός επίθεσης και κλίση της take damage για να αφεραιθούν οι πόντοι ζωής
        message11 = f"{self.name}, used a water attack against {defender.name}!"
        print(message11)
        if defender.type == "fire":
            dmg = dmg*1.5
        elif defender.type == "grass":
            dmg = dmg*0.5
        defender.take_damage(dmg)

    def aqua_ring(self):
        #Κλήση της restore_hp για να γίνει heal στο water pokemon
        message12 = f"{self.name} used aqua ring!"
        print(message12)
        restored = self.max_hp * 0.1
        self.restore_hp(restored)


#Ορισμός των Pokemon
char = FirePokemon("Charmander", 50)
bulba = GrassPokemon("Bulbasaur", 50)
squi = WaterPokemon("Squirtle", 50)
rat = Pokemon("Rattata", 20)

#Ανέβασμα Επιπέδων Σε Μερικά
print()
char.level_up()
char.level_up()
rat.level_up()

#HP Πριν Τις Μάχες
char.hp_status()
bulba.hp_status()
squi.hp_status()
rat.hp_status()

#Μάχη 1
print()
char.attack(bulba,10)
char.fire_attack(bulba,10)
char.burn(bulba)
bulba.grass_attack(char,10)
print()

#Μάχη 2
print()
bulba.grass_attack(squi,10)
bulba.absorb(squi)
squi.water_attack(bulba,10)
print()

#Μάχη 3
print()
squi.water_attack(char,10)
squi.aqua_ring()
char.fire_attack(squi,10)
print()

#Μάχη 4
print()
rat.attack(bulba,10)
bulba.grass_attack(rat,25)
print()

#HP Μετά Μαχών
char.hp_status()
bulba.hp_status()
squi.hp_status()
rat.hp_status()