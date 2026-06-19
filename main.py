# Project 2: Student Grade Management System

import json
import os

STUDENTS = {}

def clearConsole():
    os.system("cls")

def studentTemplate(marks):
    return {
        "Maths": marks[0],
        "Physics": marks[1],
        "Chemistry": marks[2],
        "Percentage": marks[3],
    }

def printStudent(studentName, marks):
    print("\nName: ", studentName, "\n")
    print("-----Marks-----\n")
    print("Maths: ", marks["Maths"])
    print("Physics: ", marks["Physics"])
    print("Chemistry: ", marks["Chemistry"], "\n")
    print("Percentage: ", marks["Percentage"], "\n")
    print("-" * 15, "\n")

def menu():

    while True:
        clearConsole()
        print("Student Grade Management System \n")

        print("==================================================\n")

        print("""1. Add Student
2. Update Marks
3. View Student
4. Show All Students
5. Show Topper
6. Show Class Average
7. Delete Student
8. Save Data
9. Load Data
10. Exit \n""")

        print("==================================================\n")

        userChoice = input("Enter your choice:\n> ")

        match userChoice:
            case "1":
                clearConsole()
                addStudent()
                input("\nPress Enter...")

            case "2":
                clearConsole()
                updateStudent()
                input("\nPress Enter...")

            case "3":
                clearConsole()
                showStudent()
                input("\nPress Enter...")

            case "4":
                clearConsole()
                showAllStudents()
                input("\nPress Enter...")

            case "5":
                clearConsole()
                topper()
                input("\nPress Enter...")

            case "6":
                clearConsole()
                classAverage()
                input("\nPress Enter...")

            case "7":
                clearConsole()
                deleteStudent()
                input("\nPress Enter...")

            case "8":
                clearConsole()

                saveData()
                input("\nPress Enter...")

            case "9":
                clearConsole()

                loadData()
                input("\nPress Enter...")

            case "10":
                print("Thank You!")
                break

            case _:
                clearConsole()
                print("Invalid choice!")
                input("\nPress Enter...")

def addStudent():

    name = input("Enter the name of the student: ")

    maths = float(input("Enter the marks on Maths: "))
    physics = float(input("Enter the marks in Physics: "))
    chemistry = float(input("Enter the marks in Chemistry: "))

    percentage = ((maths + physics + chemistry) * 100) / 300

    STUDENTS[name] = studentTemplate([maths, physics, chemistry, percentage])

    print("Student added successfully !!!")

def updateStudent():
    name = input("Enter the name of the student: ")

    for student, marks in STUDENTS.items():
        if name == student:
            marks["Maths"] = float(input("Enter the marks on Maths: "))
            marks["Physics"] = float(input("Enter the marks in Physics: "))
            marks["Chemistry"] = float(input("Enter the marks in Chemistry: "))
            marks["Percentage"] = ((marks["Maths"] + marks["Physics"] + marks["Chemistry"]) * 100) / 300
            print("\nStudent marks updated !!!")
            return
    print("\nNo student found !!!")
    return

def showStudent():

    name = input("Enter the name of the student: ")

    for studentName, marks in STUDENTS.items():
        if studentName == name:
            print("\n")
            printStudent(studentName, marks)
            return
    print("\nStudent not found !!!")
    return

def showAllStudents():

    if not STUDENTS:
        print("No students found!")
        return

    i = 1

    for studentName, marks in STUDENTS.items():
        print(f"===== Student {i} =====\n")

        printStudent(studentName, marks)
        i += 1

    return

def topper():

    if not STUDENTS:
        print("No students found!")
        print("Unable to calculate the topper of the class !!!")
        return

    topStudent = ""
    topPercentage = 0

    for studentName, marks in STUDENTS.items():
        if marks["Percentage"] >= topPercentage:
            topStudent = studentName
            topPercentage = marks["Percentage"]
    print(f"Topper: {topStudent}, % : {topPercentage}")
    return

def classAverage():
    if not STUDENTS:
        print("No students found!")
        print("Unable to calculate the class average !!!")
        return

    classAverage = 0

    for studentName, marks in STUDENTS.items():
        classAverage += marks["Percentage"]
    classAverage = classAverage / len(STUDENTS)

    print(f"\nClass Average: {classAverage} %")
    return

def deleteStudent():

    studentName = input("Enter the student name: ")
    exists = False
    for student, marks in STUDENTS.items():
        if studentName == student:
            printStudent(student, marks)
            prompt = input(
                f"Are u sure that u want to delete {studentName} (y/n): "
            ).lower()
            if prompt == "y" or prompt == "yes":
                exists = True
                break
            elif prompt == "n" or prompt == "no":
                print("Operation cancelled !!!")
                return
    if exists:
        del STUDENTS[studentName]
        print("Student deleted successfully !!!")
        return
    print("Student not found !!!")
    return

def saveData():
    fileName = input("Enter the file name: ")
    filePath = os.path.join(os.getcwd(), f"{fileName}.json")
    with open(filePath, "w+") as f:
        json.dump(STUDENTS, f, indent=4)
    print(f"file path: {filePath}")
    return

def loadData():

    global STUDENTS
    filePath = input("Enter the file path: ")

    if not os.path.exists(filePath):
        print("Invalid file path !!!")
        return

    with open(filePath, "r+") as f:
        STUDENTS = json.load(f)
    print(f"file loaded successfully !!!")
    return

menu()