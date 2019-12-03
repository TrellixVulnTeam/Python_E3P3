# PROGRAM DZIEKANAT
# -> KLASA MODELU STUDENT: INDEX, NAME, LASTNAME, GRADES[]

# -> KLASA LOGIKI BIZNESOWEJ -> addStudent(), getStudents(), deleteStudentbyIndex()
# metoda uruchomieniowa -> GUI ->CLI




# GUI UŻYTKOWNIKA
from cwiczenia_day5.P67.controller.studentcontroller import StudentController


def commandLineInterface():
    sc = StudentController()
    while(True):
        try:

            print("APLIKACJA DZIEKANAT")
            choice = input("(I) - dodaj studenta \n(S) - wypisz studentów \n(G) - dodaj ocenę \n(D) - usuń studenta \n(Q) - wyjscie")
            if (choice.upper() == "I"):
                data = input("Podaj numer indeksu, imię i nazwisko (po spacji)").split(" ") # lista 3 elementów
                sc.addStudent(data[0], data[1], data[2])
            elif(choice.upper() == "S"):
                sc.getStudents()
            elif(choice.upper() == "G"):
                data = input("Podaj numer indeksu studenta i ocenę którą chcesz przypisać (po spacji)").split(" ")
                sc.addGradeToStudent(data[0],float(data[1]))
            elif(choice.upper() == "D"):
                data = input("Podaj numer indeksu studenta, którego chcesz usunąć")
                sc.deleteStudentByIndex(data)
            elif(choice.upper() == "Q"):
                print("Wyjście")
                break
            else:
                print("Błędny wybór")
        except:
            print("Ups! Coś poszło nie tak")

commandLineInterface()
















