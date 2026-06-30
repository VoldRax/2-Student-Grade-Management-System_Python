# Project 2: Student Grade Management System

import json
import os

STUDENTS = {}

def clearConsole():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def studentTemplate(marks):
    return {
        "Maths": marks[0],
        "Physics": marks[1],
        "Chemistry": marks[2]
    }

def printStudent(studentName, marks):
    print("\nName: ", studentName.capitalize(), "\n")
    print("-----Marks-----\n")
    print("Maths: ", marks["Maths"])
    print("Physics: ", marks["Physics"])
    print("Chemistry: ", marks["Chemistry"], "\n")
    print(f"Percentage: {calculatePercentage(marks):.2f}\n")
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

def calculatePercentage(marks):
    return (marks["Maths"] + marks["Physics"] + marks["Chemistry"])/3

def checkDuplicates(name):
    if name in STUDENTS:
        print("Name already exists !!!")
        return True
    return False

def getMarks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.\n")

        except ValueError:
            print("Please enter a valid number.\n")


def addStudent():

    name = input("Enter the name of the student: ").lower()

    if checkDuplicates(name):
        return

    maths = getMarks("Maths")
    physics = getMarks("Physics")
    chemistry = getMarks("Chemistry")

    STUDENTS[name] = studentTemplate([maths, physics, chemistry])

    print("Student added successfully !!!")


def updateStudent():
    name = input("Enter the name of the student: ").lower()

    if name not in STUDENTS:
       print("\nNo student found !!!")
       return

    marks = STUDENTS[name]

    marks["Maths"] = getMarks("Maths")
    marks["Physics"] = getMarks("Physics")
    marks["Chemistry"] = getMarks("Chemistry")

    print("\nStudent marks updated !!!")
    return


def showStudent():

    name = input("Enter the name of the student: ").lower()

    if name in STUDENTS:
        print("\n")
        printStudent(name, STUDENTS[name])
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
        studentPercentage = calculatePercentage(marks)
        if studentPercentage >= topPercentage:
            topStudent = studentName
            topPercentage = studentPercentage
    print(f"Topper: {topStudent.capitalize()}, % : {topPercentage:.2f}")
    return


def classAverage():
    if not STUDENTS:
        print("No students found!")
        print("Unable to calculate the class average !!!")
        return

    classAverage = 0

    for studentName, marks in STUDENTS.items():
        classAverage += calculatePercentage(marks)
    classAverage = classAverage / len(STUDENTS)

    print(f"\nClass Average: {classAverage:.2f} %")
    return


def deleteStudent():

    studentName = input("Enter the student name: ").lower()

    if studentName not in STUDENTS:
        print("Student not found !!!")
        return

    printStudent(studentName, STUDENTS[studentName])

    prompt = input(
        f"Are you sure you want to delete {studentName.capitalize()} (y/n): "
    ).lower()

    if prompt in ("y", "yes"):
        del STUDENTS[studentName]
        print("Student deleted successfully !!!")

    elif prompt in ("n", "no"):
        print("Operation cancelled !!!")

    else:
        print("Invalid choice !!!")


def saveData():
    fileName = input("Enter the file name: ")
    filePath = os.path.join(os.getcwd(), f"{fileName}.json")
    with open(filePath, "w") as f:
        json.dump(STUDENTS, f, indent=4)
    print(f"file path: {filePath}")
    return


def loadData():
    try:
        global STUDENTS
        filePath = input("Enter the file path: ")

        with open(filePath, "r") as f:
            STUDENTS = json.load(f)
        print("file loaded successfully !!!")
        return
    except FileNotFoundError:
            print("Invalid file path !!!")
            return
    except json.JSONDecodeError:
        print("Invalid JSON file !!!")
        return

menu()