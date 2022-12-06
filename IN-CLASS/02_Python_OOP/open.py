# import os
# os.system('cls' if os.name=="nt" else 'clear')
#Terminalde yazilar alt alta gelecek. Her sefeferinde terminalin temizlenmesi icin bunu yazdik.
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP
# ---------------------------------------------
# Object Oriented Programming
# Classes -> BluePrint: Mimarların kullandığı mavi şablon kağıdıdır. Obje orada tanımlanmıştır.
# DRY: Don't Repeat Yourself
# ---------------------------------------------
# ---------------------------------------------

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
        