from operations import(
    add_student,
    show_students,
    search_student,
    update_student,
    delete_student 
)

while True:
    print("=====Student Management System=====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exite")

    choice = input("Enter your choice:")
   
    if choice == "1":
         name = input("Enter name:")
         try:
             age = int(input("Enter age:"))
             if age <= 0:
                 print("Age nust be greater than 0")
                 continue            
         except ValueError:
             print("Age must be a number")
             continue                
         grade = input("Enter grad:")
         add_student(name, age, grade)

    elif choice == "2":
        show_students() 

    elif choice == "3":
       name = input("Enter student name:")
       search_student(name) 
               
    elif choice == "4":
        name = input("Enter student name:")
        try:
           age = int(input("Enter new age:"))
           if age <= 0:
               print("Age must be greater than 0")
               continue
        except ValueError:
            print("Age must be a number")
            continue       
        grade = input("Enter new grade:") 
        update_student(name, age, grade) 

    elif choice == "5":
        name = input("Enter student name:")
        delete_student (name)

    elif choice == "6":
         print("Thank you for using Student Management System")
         break
    else:
        print("Invalid choice.Please try again.")                                





    
    


    
