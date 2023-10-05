# Virtual Classroom Manager

Virtual Classroom Manager is a Python program that allows administrators, teachers, and students to manage virtual classrooms, enroll students, schedule assignments, and more. This README provides an overview of the program's features and how to use it.

## Features

- **Admin Controls:**
  - Add and remove teachers.
  - If Admin remove any particular teacher then classrooms, students and assignments which were created by that teacher were also removed.
  - View a list of teachers.
  - View a list of classrooms after creating classrooms by teacher.

- **Teacher Controls:**
  - Teachers can only access and manage their own classrooms and students, with no access to others'.
  - Add classrooms to manage.
  - Enroll students in their classrooms.
  - Schedule assignments for their classrooms.
  - View submitted assignments.
  - List of students in their classrooms.
  - Remove classrooms and students they manage.

- **Student Controls:**
  - View scheduled assignments for their classroom.
  - Submit assignments.

## Getting Started

Follow these steps to get started with the Virtual Classroom Manager:

1. Clone the repository to your local machine:
  git clone https://github.com/MeetHedapara79/Educational_Initiatives-Task.git

2. Navigate to the project directory:
  cd your_directory_name

3. Run the program:
  **python main.py**
 
## Usage

- **Admin:**
  - When you run the program, choose the "Admin" option.
  - Enter the admin password to access administrative controls.
  - Add teachers, view classrooms, and manage teachers.

- **Teacher:**
  - After admin approval, teachers can log in using their teacher ID.
  - Add classrooms, enroll students, schedule assignments, and manage classrooms and students.
  - Each teacher has exclusive access to their assigned classrooms and students, ensuring privacy and control over their educational environment. Teachers are unable to access or manage classrooms and students belonging to other teachers.

- **Student:**
  - Students need to specify their classroom name (in the format "TeacherID_ClassroomName") and their student ID.
  - View "Scheduled Assignments".
  - Submit assignments using Assignment ID which wass mentioned in "Scheduled Assignments".
 
- **So, basically to run this program you have to first login as "Admin" then "Teacher" and then "Student".**

## If you face any difficuly to run this program then kindly go through these Screen Shots:

- **First Login as Admin and add teachers:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/36d7dc6b-52c3-42d3-a861-85e812fba2fd)

- **Then Sign Out as Admin and Login as Teacher and then add Classrooms:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/f1948cc2-ad30-4faf-b495-13e78a4d4fbf)

- **Then add Students in that classroom and schedule the assignments:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/c4b8211d-6d25-4162-af5c-0f62dbbe4a74)

- **You can also see the list of classrooms and list of students in particular classrooms:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/3c4eb9c2-7b77-4eb5-b8c7-be7d14cb46dc)

- **Then Sign Out as Teacher and Login as Student and see the scheduled assignments and submit it:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/33e12dec-d02f-4232-973d-f688084f03d9)

- **Then Sign Out as Student and again Login as Teacher and see the Submission of Assignments:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/28fab20c-5e5a-4ef1-9d2d-3d3e50725f96)

- **Admin can see the all classrooms along with teacher and number of students:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/244d0422-f135-463e-a902-ade48f48829f)

- **Teacher can also remove any student and any classroom which were created by him/her:**
  ![image](https://github.com/MeetHedapara79/Educational_Initiatives-Task/assets/121930245/ed8003a5-6ec9-4ab8-9e7d-061c35936e74)


## Enjoy managing your virtual classrooms!



