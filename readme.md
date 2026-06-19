# 🎓 Student Grade Management System

A command-line application for managing student records, academic performance, and class statistics.

---

## 📌 Overview

The Student Grade Management System is a Python-based CLI application that allows users to store, manage, and analyze student academic records.

The system supports creating, updating, viewing, and deleting student records while automatically calculating percentages and generating class-level statistics such as toppers and averages.

Student data can be saved to and loaded from JSON files for persistence.

---

## 🚀 Features

### Student Management

* Add Student
* Update Student Marks
* View Student Details
* Show All Students
* Delete Student

### Academic Statistics

* Calculate Student Percentage
* Find Class Topper
* Calculate Class Average
* Display Student Performance

### Data Persistence

* Save Data to JSON
* Load Data from JSON

---

## 🛠 Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Match Case
* JSON
* File Handling

---

## 📂 Project Structure

```text
student_grade_management/
├── main.py
├── students.json
└── README.md
```

---

## 📊 Data Structure

```python
STUDENTS = {
    "Student Name": {
        "Maths": 95,
        "Physics": 90,
        "Chemistry": 85,
        "Percentage": 90.0
    }
}
```

---

## 📖 Menu Options

```text
1. Add Student
2. Update Student
3. View Student
4. Show All Students
5. Delete Student
6. Find Topper
7. Class Average
8. Save Data
9. Load Data
0. Exit
```

---

## 🧠 Concepts Practiced

This project was built to strengthen understanding of:

* Dictionaries
* CRUD Operations
* Modular Programming
* Functions
* Data Validation
* File Handling
* JSON Serialization
* Menu Driven Applications

---

## 🏆 Milestones

### Version 0.1 – Core System

* Student database created
* Menu system implemented
* Student template created
* Student display system completed

### Version 0.2 – Student Management

* Add student
* View student
* Show all students
* Delete student

### Version 0.3 – Academic Statistics

* Percentage calculation
* Class topper calculation
* Class average calculation

### Version 0.4 – Data Persistence

* Save data to JSON
* Load data from JSON

### Version 1.0 – Stable Release

* Fixed update student functionality
* Recalculation of percentage after updates

---

## 🔧 Current Improvements (v1.1)

### Planned

* Input validation
* Exception handling
* Cross-platform console clearing
* Improved CLI formatting

### Todo

* Prevent duplicate student names
* Validate marks range (0–100)
* Handle invalid file paths
* Handle missing JSON files
* Student search feature
* Subject-wise averages

---

## 🐞 Known Issues

### Open Bugs

* Console clearing currently works only on Windows systems.

### Fixed Bugs

* Fixed `updateStudent()` logic.
* Fixed percentage recalculation after updates.
* Fixed student deletion errors.
* Fixed invalid file path crashes while loading data.

---

## 💡 Future Features

### Version 2.0

* Student Ranking System
* Grade Assignment (A/B/C/D)
* Student Search
* Export Report Cards
* Student IDs
* Multiple Classes and Sections

### Advanced Upgrades

* SQLite Database Integration
* GUI using Tkinter
* Login System
* Teacher Dashboard
* Attendance Management
* PDF Report Cards

---

## 📅 Development Timeline

| Date       | Progress                           |
| ---------- | ---------------------------------- |
| 17-06-2026 | Project Started                    |
| 18-06-2026 | Core Functionality Completed (50%) |
| 19-06-2026 | Version 1.0 Completed              |

---

## 🎯 Learning Outcome

This project served as a practical revision and application of fundamental Python concepts including data structures, file handling, modular programming, and CRUD-based application development.

---

## 📜 License

This project is intended for educational and learning purposes.