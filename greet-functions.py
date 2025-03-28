def greet():
    print("Hello, World!")
    print("End of the greet function")

greet()

name1 = "Thor"
name2 = "Joel"
list_of_names = ["Katja", "Olga", "Tim"]

for name in list_of_names:
    print("Hello", name)

#name = parameter
def greet_person(name):
    print("Hello, ", name)
    print("End of the greet_person function.")


greet_person(name1)
#name1 = Variable
greet_person(name2)

for name in list_of_names:
    greet_person(name)

