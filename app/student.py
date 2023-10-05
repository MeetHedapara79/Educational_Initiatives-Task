# Class to represent a student

class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def __str__(self):
        return str(self.student_id)
    