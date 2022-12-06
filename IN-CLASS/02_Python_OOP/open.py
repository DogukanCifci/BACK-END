# # import os
# # os.system('cls' if os.name=="nt" else 'clear')
# #Terminalde yazilar alt alta gelecek. Her sefeferinde terminalin temizlenmesi icin bunu yazdik.
# # ---------------------------------------------
# # ---------------------------------------------
# # Python - OOP
# # ---------------------------------------------
# # Object Oriented Programming
# # Classes -> BluePrint: Mimarların kullandığı mavi şablon kağıdıdır. Obje orada tanımlanmıştır.
# # DRY: Don't Repeat Yourself
# # ---------------------------------------------
# # ---------------------------------------------

'''
def print_type(data) : 
    for per in data : 
        print(per, type(per))


print_type(["Dogukan", 27, [1,2,3], True, "Furkan", lambda x :x, (1,2,3)])

class ClassName : # PEP8 --> CamelCase yapida isimlendirilir.
    # Attribute
    variable = 'value'

    # Methods(arguments) :
    def example_function() : #PEP8 -->snake_case yapida isimlendirilir. Bütün kelimeler kücük harfle baslar. Aralarina _ koyulur.
        # Parameters :
        variable_for_function = 'value' 
'''

'''
class Person :
    name = 'Dogukan'
    surname = "Cifci"


print(Person)
print(Person.name)
print(Person.surname)
#Set Object from Class 
personal_1 = Person() # ->Instance

print(personal_1)
print(personal_1.name)
print(personal_1.surname)

print("--------------")

personal_1.name = "Mevlüt"
personal_1.surname = "Catal"
print(personal_1)
print(personal_1.name)
print(personal_1.surname)

personal_1.path = "Full-Stack"
print(personal_1.path) #Kendi olusturdugum classa etki eder ama genel class olan Person'a etki etmez.
'''

# #Bir instance ile olusturulan attribute baska bir instance ile olusturulan attribute etkilemez.

'''
class Person:
    name = "Dogukan"
    surname = "Cifci"

    def test(self) :
        print(self.name) 

person3 = Person()
#Call Method
person3.test()

'''
#-----------#-----------#-----------#-----------#-----------
'''
#Getter-Setter Methods : 
#underscore(_) ile baslayan degiskenlerin instance tarafinda degistirilmemesi ve cagrilmamasi beklenir. Ama zorunlu degil.
class Person : 
    _name = "Kadir"
    _surname = "Adamson"
    # Python, Double-Underscore(__) ile baslayan degiskenlerin disardan cagirilmasini engeller.
    __location = "Germany"
    # Getter Method
    def get_name(self) : 
        #...
        return self._name + " " + self._surname + " "+ self.__location

    # Setter method
    def set_name(self,new_name,new_surname, new_location) :
        #...
        self._name = new_name
        self._surname = new_surname
        self.__location = new_location

person4 = Person()

print(person4._name) # Kadir
# Ama bunun kullanilmasi tavsiye edilmez. Bunun yerine ; 

print(person4.get_name()) # Kadir Adamson Germany
#Bu sekilde cagirabiliriz.

#Eger yeni isim vermek istersek ; 

person4.set_name("Henry", "Cavil", "London")
print(person4.get_name()) # Henry Cavil London

# print(person4.__location) # --> Bunun sonucunda böyle bir degisken yok diye hata verir.

print(person4.set_name)

'''


#-----------#-----------#-----------#-----------#-----------
'''
class Person : 
    name = "Marie"
    surname = "Curie"

    # Method :
    # this --> self
    def test(self) :
        print(self.name)
    
    #Bazen calss icindeki argumanlarin fonksiyon icinde kullanilmasina gerek olmaz. O zaman tüm veriyi bosuna cagirmamiza gerek yoktur. Bunu icin staticmethod kullanilir.
    @staticmethod
    def static_method() :
        print("Merhaba verileri cagirmadan burda staticmethod kullandik.")

'''

#-----------#-----------#-----------#-----------#-----------
# Constructor Methods : 
'''
class Person : 
    name = "Marie"
    surname = "Curie"

    # Constructor Method 
    def __init__(self):
        print("Class cagirildi!")
    # Varsayilan yazilacak veri ___str__ ile belirlenir. __str__ isminin yerine baska bir isim kullanamam.
    def __str__(self):
        return self.name + " " + self.surname
    #Person classindan olusturulmus bir object direk cagirildiginda normalde <__main class ...> gibi bi sey yaziyor. Ben onun yerine cagirildiginda direk ne yzamasini istiyorsam __str__ fonksiyonunun icine yazabilirim.

person6 = Person() #__init__ bu asamada direk geldi
print(person6) # __str__ 'de bu asamada geldi.


'''

#-----------#-----------#-----------#-----------#-----------
#Encapsulation and Abstraction

#-----------#-----------#-----------#-----------#-----------
# Inheritance and Polymorphism

class Person : 
    name = "Marie"
    surname = "Curie"

    def get_name(self) : 
        return self.name + " " + self.surname
    
    def set_name(self, new_name,new_surname) :
        self.name = new_name
        self.surname = new_surname

class Employee(Person) : # Inheritance --> # Baska bir classin özelliklerini miras alarak yeni bir class olusturmak istersem Parantezin icine miras alacagimiz olan class'in ismini yazariz.
    salary = "5000"

    """ def set_name(self,salary) :
        self.salary = salary """ # Böyle bir sey yaparsam bir önceki  set_name  ezmisolurum.
    #Onun icin su sekilde yazmaliyim
    def set_name(self, new_name, new_surname,salary):
        super().set_name(new_name, new_surname)
        self.salary = salary

    def get_name(self):
        return f"{self.name} {self.surname} {self.salary}"

employee1 = Employee()
print(employee1.name + " " + employee1.surname + " " + employee1.salary)
print(employee1.get_name())

employee1.set_name("Dogukan", "Cifci", "10000")
print(employee1.get_name())
