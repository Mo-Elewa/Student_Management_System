from student import Student
from data import students

def add_student(name, age, grade):
    for student in students:
        if student.name == name:
            print("Student alredy exists")
            return         
    student = Student(name, age, grade)
    students.append(student)
    print(f"{name} has been added successfully")
    
def show_students():
        if len (students) == 0:
            print("No students found")
            return
        students.sort(key=lambda student: student.name)
        for student in students:
            student.display()
            print("-------------")

def search_student(name):
    for student in students:
        if student.name.lower() == name.lower():              
            student.display()
            return
    print("student not found")            

def update_student(name, new_age, new_grade):
        for student in students:
            if student.name.lower() == name .lower():
                student.age = new_age 
                student.grade = new_grade
                print("Student updated successfully")
                return
            print("Student not found")

def delete_student(name):
         for student in students:
             if student.name.lower() == name.lower():
                 confirm = input(f"Are you sure you want to delete {name}?(y/n): ")
                 if confirm. lower() == "y":
                    students.remove(student)
                    print("Student deleted succesfully") 
                 else:
                     print("Deleted cancelled")
                     return
         print("Student not found")  








