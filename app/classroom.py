# Class to represent a classroom

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []  # for store enrolled students
        self.assignments = []  # for store assignments
        self.assignment_counter = 1  

    def __str__(self):
        return self.name

    # Method to enroll a student in the classroom
    def enroll_student(self, student_id, class_name):
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"Student '{student_id}' has been enrolled in '{class_name}' class.")
        else:
            print(f"Student '{student_id}' already exists in '{class_name}' classroom.")

    # Method to remove a student from the classroom
    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    # Method to schedule an assignment
    def schedule_assignment(self, teacher_id, assignment_details):
        assignment_id = f"A{self.assignment_counter}"
        self.assignment_counter += 1
        self.assignments.append({"assignment_id": assignment_id, "teacher_id": teacher_id, "details": assignment_details, "submitted": []})
        return assignment_id

    # Method to get a list of submitted assignments
    def submitted_assignments(self):
        return [assignment for assignment in self.assignments if assignment['submitted']]

    # Method for submit an assignment
    def submit_assignment(self, student_id, assignment_id):
        for assignment in self.assignments:
            if assignment['assignment_id'] == assignment_id:
                assignment['submitted'].append(student_id)
                return True
        return False
    