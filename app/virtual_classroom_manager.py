from app.classroom import Classroom
from app.teacher import Teacher
from app.student import Student

# Class to manage the virtual classroom

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}  # for store classrooms
        self.teachers = {}  # for store teachers
        self.admin_password = "Meet7"  # Admin password

    # Method to add classroom
    def add_classroom(self, class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name] = Classroom(class_name)
            print(f"Classroom '{class_name}' has been created.")
        else:
            print(f"Classroom '{class_name}' already exists.")

    # Method to add student in classroom
    def add_student(self, student_id, class_name):
        if class_name in self.classrooms:
            classroom = self.classrooms[class_name]
            classroom.enroll_student(student_id, class_name)
        else:
            print(f"Classroom '{class_name}' does not exist.")

    # Method to schedule an assignment
    def schedule_assignment(self, teacher_id, class_name, assignment_details):
        if class_name in self.classrooms and teacher_id in self.teachers:
            classroom = self.classrooms[class_name]
            assignment_id = classroom.schedule_assignment(teacher_id, assignment_details)
            print(f"Assignment '{assignment_id}' has been scheduled by Teacher '{teacher_id}' in '{class_name}' classroom.")
        else:
            print("Classroom does not exist.")

    # Method to get a list of students who submitted assignments
    def submitted_assignments(self, teacher_id, class_name):
        if class_name in self.classrooms and teacher_id in self.teachers:
            classroom = self.classrooms[class_name]
            submitted = classroom.submitted_assignments()
            if submitted:
                print("Submitted Assignments:")
                for assignment in submitted:
                    num_submitted = len(assignment['submitted'])
                    submitted_students = ', '.join(assignment['submitted'])
                    print(f"Assignment ID: {assignment['assignment_id']}, Assignment: {assignment['details']}, "
                          f"Submitted by {num_submitted} students: {submitted_students}")
            else:
                print("Not any assignment submitted yet.")
        else:
            print("Classroom does not exist.")

    # Method to get list of students in a classroom
    def list_students(self, teacher_id, class_name):
            if class_name in self.classrooms:
                classroom = self.classrooms[class_name]
                if class_name.startswith(teacher_id):
                    if classroom.students:
                        print(f"Students in '{class_name}': {', '.join(map(str, classroom.students))}")
                    else:
                        print(f"No students in '{class_name}'.")
                else:
                    print("You can only list students in your classrooms.")
            else:
                print(f"Classroom '{class_name}' does not exist.")

    # Method to get list of classrooms for a teacher
    def list_classrooms(self, teacher_id):
        teacher_classrooms = [class_name for class_name in self.classrooms if class_name.startswith(teacher_id)]
        if teacher_classrooms:
            print("Your Classrooms:")
            for class_name in teacher_classrooms:
                num_students = len(self.classrooms[class_name].students)
                print(f"Classroom: {class_name}, Number of Students: {num_students}")
        else:
            print("You have no classrooms.")

    # Method to get list of teachers
    def list_teachers(self):
        if self.teachers:
            print("List of Teachers:")
            for teacher_id in self.teachers:
                print(teacher_id)
        else:
            print("No teachers available.")

    # Method to show all classrooms
    def show_classrooms(self):
        if self.classrooms:
            print("Classrooms:")
            for class_name, classroom in self.classrooms.items():
                teacher_id = class_name.split('_')[0]
                num_students = len(classroom.students)
                print(f"Classroom: {class_name}, Teacher ID: {teacher_id}, Number of Students: {num_students}")
        else:
            print("No classrooms available.")

    # Method to add teacher
    def add_teacher(self, teacher_id):
        if teacher_id not in self.teachers:
            self.teachers[teacher_id] = Teacher(teacher_id)
            print(f"Teacher '{teacher_id}' has been added.")
        else:
            print(f"Teacher '{teacher_id}' already exists.")

    # Method to remove classroom
    def remove_classroom(self, teacher_id, class_name):
        if class_name in self.classrooms and class_name.startswith(teacher_id):
            del self.classrooms[class_name]
            print(f"Classroom '{class_name}' has been removed.")
        else:
            print("Classroom does not exist.")

    # Method to remove a student from classroom
    def remove_student(self, teacher_id, class_name, student_id):
        if class_name in self.classrooms and teacher_id in self.teachers and class_name.startswith(teacher_id):
            classroom = self.classrooms[class_name]
            if student_id in classroom.students:
                classroom.remove_student(student_id)
                print(f"Student '{student_id}' has been removed from '{class_name}' class.")
            else:
                print(f"Student '{student_id}' is not enrolled in '{class_name}' class.")
        else:
            print("Classroom or student does not exist.")

    # Method to remove teacher
    def remove_teacher(self, admin_password, teacher_id):
        if admin_password == self.admin_password:
            if teacher_id in self.teachers:
                teacher_classrooms = [class_name for class_name in self.classrooms if class_name.startswith(teacher_id)]

                for class_name in teacher_classrooms:
                    del self.classrooms[class_name]

                del self.teachers[teacher_id]

                print(f"Teacher '{teacher_id}' has been removed along with associated classrooms, students, and assignments.")
            else:
                print(f"Teacher '{teacher_id}' does not exist.")
        else:
            print("Admin password is incorrect.")

    # Method for admin login
    def admin_login(self):
        password = input("Enter the admin password [pwd-> Meet7](for testing purpose): ")
        if password == self.admin_password:
            while True:
                print("\nAdmin Controls")
                print("1. Add Teacher")
                print("2. Show Classrooms")
                print("3. List of Teachers")
                print("4. Remove Teacher")
                print("5. Sign Out")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    teacher_id = input("Enter the teacher ID: ")
                    self.add_teacher(teacher_id)
                elif admin_choice == '2':
                    self.show_classrooms()
                elif admin_choice == '3':
                    self.list_teachers()
                elif admin_choice == '4':
                    teacher_id = input("Enter the teacher ID to remove: ")
                    self.remove_teacher(password, teacher_id)
                elif admin_choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Admin password is incorrect.")

    # Method for teacher login
    def teacher_login(self, teacher_id):
        while True:
            print(f"\nTeacher Controls (Teacher ID: {teacher_id})")
            print("1. Add Classroom")
            print("2. Add Student")
            print("3. Schedule Assignment")
            print("4. Submitted Assignments")
            print("5. List of Students")
            print("6. List of Classrooms")
            print("7. Remove Classroom")
            print("8. Remove Student")
            print("9. Sign Out")

            teacher_choice = input("Enter your choice: ")

            if teacher_choice == '1':
                class_name = input("Enter the name of the classroom: ")
                self.add_classroom(f"{teacher_id}_{class_name}")
            elif teacher_choice == '2':
                student_id = input("Enter the student ID: ")
                class_name = input("Enter the classroom name: ")
                self.add_student(student_id, f"{teacher_id}_{class_name}")
            elif teacher_choice == '3':
                class_name = input("Enter the classroom name: ")
                assignment_details = input("Enter assignment details: ")
                self.schedule_assignment(teacher_id, f"{teacher_id}_{class_name}", assignment_details)
            elif teacher_choice == '4':
                class_name = input("Enter the classroom name: ")
                self.submitted_assignments(teacher_id, f"{teacher_id}_{class_name}")
            elif teacher_choice == '5':
                class_name = input("Enter the classroom name: ")
                self.list_students(teacher_id, f"{teacher_id}_{class_name}")
            elif teacher_choice == '6':
                self.list_classrooms(teacher_id)
            elif teacher_choice == '7':
                class_name = input("Enter the classroom name to remove: ")
                self.remove_classroom(teacher_id, f"{teacher_id}_{class_name}")
            elif teacher_choice == '8':
                class_name = input("Enter the classroom name: ")
                student_id = input("Enter the student ID to remove: ")
                self.remove_student(teacher_id, f"{teacher_id}_{class_name}", student_id)
            elif teacher_choice == '9':
                break
            else:
                print("Invalid choice. Please try again.")

    # Method for student login
    def student_login(self, class_name, student_id):
        if class_name in self.classrooms:
            classroom = self.classrooms[class_name]
            if student_id in classroom.students:
                while True:
                    print(f"\nStudent Controls (Classroom: {class_name}, Student ID: {student_id})")
                    print("1. Scheduled Assignments")
                    print("2. Submit Assignment")
                    print("3. Sign Out")

                    student_choice = input("Enter your choice: ")

                    if student_choice == '1':
                        print("Scheduled Assignments:")
                        if classroom.assignments:  
                            for assignment in classroom.assignments:
                                print(f"Assignment ID: {assignment['assignment_id']}, Assignment: {assignment['details']}")
                        else:
                            print("No assignments scheduled yet.")
                    elif student_choice == '2':
                        assignment_id = input("Enter assignment ID: ")
                        if classroom.submit_assignment(student_id, assignment_id):
                            print(f"Assignment '{assignment_id}' submitted by Student '{student_id}' in '{class_name}' class.")
                        else:
                            print(f"Assignment '{assignment_id}' not found in '{class_name}' or already submitted.")
                    elif student_choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print(f"Student '{student_id}' is not enrolled in '{class_name}'.")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    # Method for run the virtual classroom manager
    def run(self):
        print("\nWelcome to Virtual Classroom!!")
        print("\nAdmin can add Teachers.\nTeachers can add classrooms and Students.\nSo, for run this program you have to 1st login as Admin then Teacher and then Student.")
        while True:
            print("\nVirtual Classroom Manager")
            print("1. Admin")
            print("2. Teacher")
            print("3. Student")
            print("4. Quit")

            user_type = input("Enter your user type: ")

            if user_type == '1':
                self.admin_login()
            elif user_type == '2':
                teacher_id = input("Enter your teacher ID: ")
                if teacher_id in self.teachers:
                    self.teacher_login(teacher_id)
                else:
                    print("Teacher ID not recognized.")
            elif user_type == '3':
                class_name = input("Enter your classroom name(Format->TeacherID_ClassroomName): ")
                student_id = input("Enter your student ID: ")
                self.student_login(class_name, student_id)
            elif user_type == '4':
                break
            else:
                print("Invalid choice. Please try again.")
                