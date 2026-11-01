import json
import time
def student_management_system():
    while True:
        width = 50
        print("\033[0m")

        print("\033[36m")
        print("=" * width)
        print("STUDENT MANAGEMENT SYSTEM".center(width))
        print("=" * width)
        print("\033[0m")

        print("\033[32m")
        print("Welcome to Student Portal".center(width))
        print("\033[0m")

        print("Manage student records efficiently".center(width))
        print()
        

        for i in range(1, 11):
            bar = "#" * i + "-" * (10 - i)
            print(f"\rLoading: [{bar}] {i * 10}%", end="")
            time.sleep(0.2)

        print("\n")

        print("\033[36m")
        print("-" * width)
        print("MAIN MENU".center(width))
        print("-" * width)
        print("\033[0m")

        print(" [1] Add New Student")
        print(" [2] View Student Result")
        print(" [3] View All Students")
        print(" [4] Search Student")
        print(" [5] Exit")

        print("-" * width)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please try again!")
            continue
        def user_info():
            while True:
                try:
                    student_id = int(input("Enter student id: (if you want to quit! Please enter '0')"))
                except ValueError:
                    print("Invalid input. Please try again!")
                    continue
                if student_id == 0:
                    print("Thanks to use my Student Management System!")
                    break
                try:
                    with open("student.json", 'r') as file:
                        students = json.load(file)
                except FileNotFoundError:
                        students = []
                except json.JSONDecodeError:
                    print("Student file contains invalid JSON!")
                    return
                for student in students:
                    if student["Student_Id"] == student_id:
                        print(f"The student id {student_id} is already exists!")
                        break
                else:
                    while True:
                        try:
                            name = input("Enter student name: ")
                            if name.strip():
                               break
                            else:
                               print("Name cannot be empty. Please try again.")
                        except ValueError:
                            print("Invalid input. Please try again.")
                            continue
                    print("Here enter your marks!")
                    while True:
                        try:
                            HND = int(input("Enter the marks of hindi: "))
                            if HND >= 1 and HND <= 100:
                                break
                            else:
                                print("Please enter marks between 1 to 100!")
                        except ValueError:
                            print("Invalid input. Please try again: ")
                            continue
                    while True:
                        try:
                            ENG = int(input("Enter the marks of english: "))
                            if ENG >= 1 and ENG <= 100:
                                break
                            else:
                                print("Please enter marks between 1 to 100!")
                        except ValueError:
                            print("Invalid input. Please try again: ")
                            continue
                    while True:
                        try:
                            MATH = int(input("Enter the marks of mathematics: "))
                            if MATH >= 1 and MATH <= 100:
                                break
                            else:
                                print("Please enter marks between 1 to 100!")
                        except ValueError:
                            print("Invalid input. Please try again: ")
                            continue
                    while True:
                        try:
                            SCI = int(input("Enter the marks of science: "))
                            if SCI >= 1 and SCI <= 100:
                                break
                            else:
                                print("Please enter marks between 1 to 100!")
                        except ValueError:
                            print("Invalid input. Please try again: ")
                            continue
                    while True:
                        try:
                            SST = int(input("Enter the marks of social science: "))
                            if SST >= 1 and SST <= 100:
                                break
                            else:
                                print("Please enter marks between 1 to 100!")
                        except ValueError:
                            print("Invalid input. Please try again: ")
                            continue
                    marks = HND + ENG + MATH + SCI + SST
                    percentage = (marks/500)*100
                    Grade = ""
                    if percentage >= 90:
                        Grade = "A+"
                    elif percentage < 90 and percentage >=70:
                        Grade = "A"
                    elif percentage < 70 and percentage >= 60:
                        Grade = "B"
                    elif percentage < 60 and percentage >=33:
                        Grade = "C"
                    else:
                        Grade = "D"
                    info = {
                        "Student_Id" : student_id,
                        "details" : {
                                "Name" : name,
                                "Marks" : {
                                        "Hindi" : HND,
                                        "English" : ENG,
                                        "Mathematics" : MATH,
                                        "Science" : SCI,
                                        "Social_Science" : SST,
                                        "Total Marks" : marks,
                                        "Percentage" : percentage,
                                        "Grade" : Grade
                                    }
                                }
                            }
                            
                    # Load existing student records
                    try:
                        with open("student.json", "r") as file:
                            students = json.load(file)
                    except FileNotFoundError:
                        students = []
                    except json.JSONDecodeError:
                        print("Student file contains invalid JSON!")
                        return
                                                                                    
                    # Add new student to the list
                    students.append(info)
                                                                                    
                    # Save all student records
                    with open("student.json", "w") as file:
                        json.dump(students, file, indent=4)
                        print("Student added successfully!")
                        break
                    
                                                    
                        
                    
                                        
        def View_Result():
            try:
                with open("student.json", 'r') as file:
                    students = json.load(file)
            except FileNotFoundError:
                students = []
            except json.JSONDecodeError:
                print("Student file contains invalid JSON!")
                return
            try:
                student_id = int(input("Enter student Id: "))
            except ValueError:
                print("Invalid input. Plase try again:")
                return
            for student in students:
                if student_id == student["Student_Id"]:
                    name = student["details"]["Name"]
                    m1 = student["details"]["Marks"]["Hindi"]
                    m2 = student["details"]["Marks"]["English"]
                    m3 = student["details"]["Marks"]["Mathematics"]
                    m4 = student["details"]["Marks"]["Science"]
                    m5 = student["details"]["Marks"]["Social_Science"]
                    full_marks = student["details"]["Marks"]["Total Marks"]
                    average = student["details"]["Marks"]["Percentage"]
                    Grade = student["details"]["Marks"]["Grade"]
                    if average >= 33:
                        status = "Pass"
                    else:
                        status = "Fail"
                    width = 50
                    print("\033[32m")
                    print(f"{'=' * width}")
                    print("REPORT CARD".center(width))
                    print(f"{'=' * width}")
                    print("\033[35m")
                    print(f"{'-'*width}")
                    print("\033[33m")
                    print(f"Name : {name}")
                    print(f"\nStudent_Id : {student_id}")
                    print("\033[35m")
                    print(f"{'-'*width}")
                    print("\033[33m")
                    print("MARKS".rjust(20))
                    print(f"{'-'*width}")
                    print("\033[34m")
                    print(f"Hindi : {m1}")
                    print(f"English : {m2}")
                    print(f"Mathematics : {m3}")
                    print(f"Science : {m4}")
                    print(f"Social_Science : {m5}", end="")
                    print("\033[31m")
                    print(f"Total_Marks : {full_marks}".rjust(24))
                    print(f"Percentage : {average:.2f}%".rjust(25))
                    print(f"Grade : {Grade}".rjust(17))
                    print(f"Status : {status}".rjust(20))
                    break
                    
            else:
                print("student Id not found!")
                return


        def All_Student():
            print("\033[32m")
            print("=" * 50)
            print("ALL STUDENT".center(50))
            print("=" * 50)
            print("\033[0m")
            try:
                with open("student.json", 'r') as file:
                    students = json.load(file)
            except FileNotFoundError:
                students = []
            except json.JSONDecodeError:
                print("Student file contains invalid JSON!")
                return
            else:
                for ch in students:
                    Student_id = ch["Student_Id"]
                    name = ch["details"]["Name"]
                    Hindi = ch["details"]["Marks"]["Hindi"]
                    English = ch["details"]["Marks"]["English"]
                    Mathematics = ch["details"]["Marks"]["Mathematics"]
                    Science = ch["details"]["Marks"]["Science"]
                    Social_Science = ch["details"]["Marks"]["Social_Science"]
                    Full_Marks = ch["details"]["Marks"]["Total Marks"]
                    average = ch["details"]["Marks"]["Percentage"]
                    Grade = ch["details"]["Marks"]["Grade"]
                    if average >= 33:
                        status = "Pass"
                    else:
                        status = "Fail"
                    print(f"Student Id : {Student_id}")
                    print(f"Name : {name}")
                    print(f"Hindi : {Hindi}")
                    print(f"English : {English}")
                    print(f"Mathematics : {Mathematics}")
                    print(f"Science : {Science}")
                    print(f"Social Science : {Social_Science}")
                    print(f"Total Marks : {Full_Marks}")
                    print(f"Percentage : {average:.2f}%")
                    print(f"Grade : {Grade}")
                    print(f"Status : {status}")
                    print(f"{'-'*width}")  


        
        def Search_Student():
            try:
                with open("student.json", 'r') as file:
                    students = json.load(file)
            except FileNotFoundError:
                students = []
            except json.JSONDecodeError:
                print("Student file contains invalid JSON!")
                return
            else:
                try:
                    student_id = int(input("enter the student Id: "))
                except ValueError:
                    print("Invalid input. Please try again: ")
                    return
                for ch in students:
                    if student_id == ch["Student_Id"]:
                        print("Student is found! Here is the student details:")
                        break
                else:
                    print("Student is not found!")
                    return

        if choice == 1:
            user_info()
        elif choice == 2:
            View_Result()
        elif choice == 3:
            All_Student()
        elif choice == 4:
            Search_Student()
        elif choice == 5:
            print("Thanks to use my Student Management System!")
            break
        else:
            print("Invalid Input! Please try again!")
student_management_system()