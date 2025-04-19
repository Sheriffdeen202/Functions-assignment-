

def student_management_system():
    # 1. TUPLES for immutable student records (name, age, major)
    student1 = ("Alice Johnson", 20, "Computer Science")
    student2 = ("Bob Smith", 21, "Mathematics")
    student3 = ("Charlie Brown", 22, "Physics")
    
    # List of student tuples
    students = [student1, student2, student3]
    
    # 2. RANGE for generating student IDs
    student_ids = range(1000, 1000 + len(students))  # Generates 1000, 1001, 1002
    
    # 3. LISTS for mutable data (courses and grades)
    courses = ["Algorithms", "Calculus", "Quantum Mechanics"]
    grades = [[90, 85, 88], [78, 92, 85], [95, 89, 91]]  # List of lists
    
    # Display all student information
    print("\nSTUDENT RECORDS:")
    for id, student, grade_list in zip(student_ids, students, grades):
        print(f"\nID: {id}")
        print(f"Name: {student[0]}")
        print(f"Age: {student[1]}")
        print(f"Major: {student[2]}")
        
        # Display courses and grades
        print("\nCourses and Grades:")
        for course, grade in zip(courses, grade_list):
            print(f"- {course}: {grade}")
    
  
    
   