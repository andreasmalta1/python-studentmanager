from studentmanager import Student, StudentTeacher


def show_menu():
    while True:
        print("Student Manager")
        print("_______________")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Exit")
        response = input("Choice: ")

        if response == "1":
            add_student()
        elif response == "2":
            show_students()
        elif response == "3":
            break
        else:
            print("Invalid Choice")


def add_student():
    print()
    name = input("Name: ")
    surname = input("Surname: ")
    student_type = input("[S]tudent or Student [T]eacher: ")

    if student_type == "T":
        teaching_area = input("Teaching Area: ")
        StudentTeacher(name, surname, teaching_area)
    else:
        Student(name, surname)
    print()


def show_students():
    name_pad = 10
    sur_pad = 10
    for s in Student.STUDENT_LIST:
        if len(s.name) > name_pad:
            name_pad = len(s.name)
        if len(s.surname) > sur_pad:
            sur_pad = len(s.surname)

    print("{0:3}\t{1:{5}}\t{2:{6}}\t{3:<5}\t{4:17}".format("ID", "Name", "Surname", "GPA", "Teaching Status", name_pad, sur_pad))

    for s in Student.STUDENT_LIST:
        teaching_area = "N/A"
        if type(s) == StudentTeacher:
            teaching_area = s.teaching_area + (" ✅" if s.is_allowed_teaching() else " ❌")
        print("{0:03d}\t{1:{5}}\t{2:{6}}\t{3:<5.1f}\t{4:17}".format(s.id, s.name, s.surname, s.gpa, teaching_area, name_pad, sur_pad))

    student_id = input("Type a student id show grades, any other key to return: ")
    if student_id.isdigit():
        show_marks(int(student_id))
        response = input("Type [a] to add grades, any other key to return: ")
        if response == "a":
            assign_marks(int(student_id))


def show_marks(student_id: int) -> None:
    s = Student.get_by_id(student_id)
    print()
    print("Marks for {0:03d} ({1} {2})".format(s.id, s.name, s.surname))
    print("{0:10}\t{1:5}".format("Subject", "Mark"))
    for subject, mark in s.gradebook.items():
        print("{0:10}\t{1:5}".format(subject, mark))


def assign_marks(student_id) -> None:
    s = Student.get_by_id(student_id)
    print()
    print("Adding marks for {0:03d} ({1} {2})".format(s.id, s.name, s.surname))

    while True:
        subject = input("Subject: ")
        mark = float(input("Mark "))
        s.add_grade(subject, mark)
        response = input("Type [a] to add more grades, any other key to return: ")
        if response != "a":
            break


show_menu()
