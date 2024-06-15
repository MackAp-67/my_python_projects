class Workplace:
    def __init__(self,budget, positions):
        #Αρχικοποίηση σε __budget, __position και αρχικοποίηση λίστας
        self.__budget = budget
        self.__positions = positions
        self.__employees = []

    def get_positions(self):
        #Δημιουργία λίστας και αλλαγή με το append για κάθε διαθέσιμη θέση 
#        available_positions = []
#        for position in self.__positions: 
#            available_positions.append(position)
#        return available_positions
        available_positions = list(self.__positions.keys())
        return available_positions
        
    def set_position(self,pos_name,salary):
        #Αποθήκευση νέας τιμής αλλιώς throw exception
        if salary > 0:
            self.__positions[pos_name] = salary
        else:
            raise Exception(f"Δεν θα δουλεύει κανείς για να σε πληρώνει...{salary}")
        
    def get_employees(self,position=None):
        #Αρχικοποίηση λίστας, για κάθε εργαζόμενο στην λίστα αν η θέση είναι None ή υπάρχει ήδη θέση τότε προσθήκη στην λίστα των εργαζομένων και επιστροφή λίστας
        employee_list = []
        for employee in self.__employees:
            if position is None or employee.get_position() == position:
                employee_list.append(employee)
        return employee_list
    
    def __proipologismos_mina(self):
        #Αρχικοποίηση μιας μεταβλητής και προσθήκη όλων των μισθών των υπαλλήλων ???
        general_salary = 0
        for employee in self.__employees:
            general_salary += self.__positions[employee.get_position()]
        if general_salary < self.__budget:
            return True
        else:
            return False
        
    def assign_employee(self,employee,position):
        #Αν υπάρχει διαθέσιμο budget από τον προϋπολογισμό προστίθεται νέος εργαζόμενος, αλλιώς throw exception
        if position not in self.__positions:
            raise Exception(f"Η θέση {position} δεν υπάρχει.")
        x = self.__proipologismos_mina()
        if x == True:
            employee.set_position(position)
            self.__employees.append(employee)
        else:
            raise Exception("Η εταιρία χρεοκόπησε, δεν θα δεχτεί νέα μέλη μέχρι να ανακάμψει...")

class Employee:
    def __init__(self,name):
        self.__name = name
        self.__position = "Unemployed"

    def get_name(self):
        return self.__name
    
    def get_position(self):
        return self.__position
    
    def set_position(self,new_position):
       if self.__position == "Unemployed" or new_position == "Unemployeed":
           self.__position = new_position
       else:
           raise Exception(f"Ένας εργάτης πρέπει να φύγει από την τωρινή του θέση για να πάρει άλλη...{new_position}")
        
            

positions={
    "μηχανικός":500
    }

#key= "βοηθός"
#value = 200
#positions[key] = value
work = Workplace(1200,positions)
work.set_position("τεχνικός", 300)

print("Διαθέσιμες θέσεις:")
for position in work.get_positions():
    print("-",position)

e1= Employee("Nikos")
e2 = Employee("Eleni")
e3 = Employee("Giannis")
e4 = Employee("Monica")


work.assign_employee(e1,"μηχανικός")
print("O/H",e1.get_name(),"έπιασε δουλειά ως",e1.get_position())
#O/H Nikos έπιασε δουλειά ως μηχανικός

work.assign_employee(e2,"τεχνικός")
print("O/H",e1.get_name(),"έπιασε δουλειά ως",e2.get_position())
#Ο/Η Eleni έπιασε δουλειά ως τεχνικός

work.assign_employee(e3, "τεχνικός")
print("O/H", e3.get_name(), "έπιασε δουλειά ως", e3.get_position())

engineers = work.get_employees("μηχανικός")
print("Μηχανικοί της εταιρίας:")
for engineers in engineers:
    print("-", engineers)

work.assign_employee(e4, "τεχνικός")
print("Ο/Η", e4.get_name(), "έπιασε δουλειά ως", e4.get_position())
