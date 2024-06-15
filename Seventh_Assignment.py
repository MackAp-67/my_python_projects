import random

class Robot:
    def __init__(self,name):
        #Ορίζουμε τα κομμάτια του ρομποτ και καλούμε 3 φορές την connect_body_part για να δούμε σε ποια κομμάτια έχει θέμα το ρομπότ
        self.name = name
        check = self.connect_body_part()
        self.head = check
        check = self.connect_body_part()
        self.legs = check
        check = self.connect_body_part()
        self.arms = check

    def connect_body_part(self):
        #Χρησιμοποιούμε την random για να βρούμε έναν τυχαίο αριθμό σε 1 και 0
        x = random.random()
        if x > 0.5:
            return True
        else:
            return False

    def start(self):
        #Ελέγχουμε αν έχουν συνδεθεί τα κομμάτια και βάζουμε Exceptions όπως ζητάει η άσκηση
        if self.head == False:
            raise Exception ("Head not connected")
        if self.arms == False:
            raise Exception ("Arms not connected")
        if self.legs == False:
            raise Exception ("Legs not connected")
        #Αν δεν υπάρξει κάποιο exception σημαίνει ότι το ρομπότ δεν έχει πρόβλημα
        #print("Robot initiated without errors")
        #print(f"{self.name} started successfully.")

class RepairShop:
    def __init__(self,owner):
        #Ορίζουμε το όνομα και την λίστα των repairs
        self.owner = owner
        self.repairs = []
    
    def repair_logging(self):
        #Εμφανίζουμε το όνομα και κάνουμε parse την λίστα repairs για να εμφανίσουμε τα fixed κομμάτια
        print(f"Repair Shop Owner: {self.owner}")
        for repair in self.repairs:
            print(f"Robot Name: {repair['robot name']}, Fixed Part: {repair['fixed part']}")

    def new_repair_log(self,robot_name,part_name):
        #Λίστα για τα repairs και κάνουμε append όποιο repair γίνει
        repair = {
            'robot name': robot_name,
            'fixed part' : part_name
        }
        self.repairs.append(repair)
    
    def fix_robot(self,robot):
        #Δημιουργία λίστας για να γίνει η αναζήτηση
        parts_to_fix = ["head","arms","legs"]
        #Loop για κάθε τι στην λίστα
        for part in parts_to_fix:
            while True:
                #Προσπάθεια να ξεκινήσει το ρομπότ με την μέθοδο start() αν ξεκινήσει τότε δίνουμε break για να τελειώσει η loop
                try:
                    robot.start()
                    break
                except Exception as e:
                    #Αν υπάρχει σφάλμα αποθηκεύεται στην e και μετατρέπεται σε string 
                    error_message = str(e)
                    #3 if για τα άκρα του ρομπότ που ελέγχει αν υπάρχουν τα σφάλματα και τα προσθέτει στην λίστα με τα repairs που πρέπει να γίνουν και break ώστε να σταματήσει η loop
                    if error_message == "Head not connected":
                        robot.head = True
                        self.new_repair_log(robot.name, 'head')
                        break
                    elif error_message == "Arms not connected":
                        robot.arms = True
                        self.new_repair_log(robot.name, 'arms')
                        break
                    elif error_message == "Legs not connected":
                        robot.legs = True
                        self.new_repair_log(robot.name, 'legs')
                        break

#Παράδειγμα χρήσης ομοίως με αυτό που έχει δοθεί για λόγους ευκρίνιας
shop = RepairShop("Smith")
robot1 = Robot("Wall-E")
robot2 = Robot("R2-D2")

#Επισκευή των ρομπότ
shop.fix_robot(robot1)
shop.fix_robot(robot2)

#εμφάνιση repairs
print("The robots are up and running!")
shop.repair_logging()