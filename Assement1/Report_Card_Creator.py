"""
Creator:    Oscar Onyeke


Program:    Report Card Creator.py
Given four inputs in the order of courses.csv, students.csv, tests.csv, and marks.csv,
a report card is generated with the characteristics of the order of the students should
be based on the student id,The first line should contain the student id and the student’s name,
The second line is the average of all the courses the student is enrolled in,
Below that, a listing of all courses and the student’s grade in each course
and the courses are ordered by course id
"""

"""used to remove newlines from the inout"""""
import re


"""
Class: Courses
    A class used to used to contain information in regards to all courses received from the
    file courses.csv and test.csv. This includes: the names of each teacher, their course,
    and the test for each course
"""


class Courses:

    def __init__(self):
        self.names = {}
        self.teachers = {}
        self.tests = {}

    """
    :function - insert: places the class name and the teachers into individual hash maps
                        by using the course id as a key for each value
    :parameter - courses_id - the id of the course
                 name - the name of the course
                 teacher - the name of the teacher of the course
    """
    def insert(self, courses_id, name, teacher):
        self.names[courses_id] = name
        self.teachers[courses_id] = teacher

    """
    :function - insert_test: places the course_id and the weight of a test into an
                             individual hash map by using the course id as a key for each value
    :parameter - courses_id - the id of the course
                 test_id - the id of the test
                 weight - the weight of a test
    """
    def insert_test(self, courses_id, test_id, weight):
        self.tests[test_id] = (courses_id, weight)

    """
    :functions - get_name: returns the name of a course by retrieving if from
                           the names hash map
    :parameter - courses_id - the id of the course
    :return - name of a course
    """
    def get_name(self, courses_id):
        return self.names[courses_id]

    """
    :function - get_teacher: returns the name of a teacher by retrieving if from
                           the teachers hash map
    :parameter - courses_id - the id of the course
    :return - name of a teacher
    """
    def get_teacher(self, courses_id):
        return self.teachers[courses_id]

    """
    :function - get_test: returns the weight and course_id of a test
    :parameter - test_id - the id of a test
    :return - a tuple containing the weight and course_id of a test
    """
    def get_test(self, test_id):
        return self.tests[test_id]

"""
Class: Student
    A class used to used to contain information of a single student, the data is received from the
    files students.csv, marks.csv, and courses. This includes: the name of the student, their id,
    the test id for each test they have done, their mark on that test, and the id of the course
    where they took the test
"""


class Student:

    def __init__(self):
        self.name = ""
        self.id = 0
        self.tests = []

    """
    :function - insert: places the students' name and id into self.name and self.id
                         by using the course id as a key for each value
    :parameter - s_id - the id of the student
                 name - the name of the student
    """
    def insert(self, s_id, name):
        self.id = s_id
        self.name = name

    """
    :function - insert_test: places the test id, grade, and course_id of a test into a
                              list called tests
    :parameter - test_id - the id of the test
                 grade - the mark a student received on a test
                 courses_id - the id of the course where the test as taken
    """
    def insert_test(self, test_id, grade, course_id):
        self.tests.append((test_id, grade, int(course_id)))

    """
    :function - get_name: returns the name of a student
    :return - name of a student
    """
    def get_name(self):
        return self.name

    """
    :function - get_test: returns the weight and course_id of a test
    :parameter - test_id - the id of a test
    :return - a tuple containing the test id, grade, and course_id of a test
    """
    def get_tests(self):
        return self.tests

    """
    :function - sort_test: sorts the list of tests in accordance to their course ids'
    """
    def sort_test(self):
        self.tests.sort(key=take_third)

"""
Class: Students
    A class used to used to contain information of al students, the data is received from the
    files students.csv, and courses.csv. The information includes: the name of the all students,
    their ids.
"""


class Students:

    def __init__(self):
        self.student_ids = []
        self.students = {}

    """
    :function - insert: places a students' id in a list of student ids, from there a
                         a new Student class is created and placed into a hash map where
                         it is populated with the name of the student and their id
    :parameter - student_id - the id of a student
                 name - the name of a student
    """
    def insert(self, student_id, name):
        self.student_ids.append(int(student_id))
        self.students[student_id] = Student()
        self.students[student_id].insert(student_id, name)

    """
    :function - get_student_ids: returns the list student ids
    :return - the entire list of student ids
    """
    def get_student_ids(self):
        return self.student_ids

    """
    :function - get_student: returns a Student class from the student hash map
    :parameter - student_id - the id of a student
    :return - a Student class
    """
    def get_student(self, student_id):
        return self.students[student_id]

    """
    :function - sort_ids: sorts the list of students in accordance to their student ids'
    """
    def sort_ids(self):
        self.student_ids.sort(key=int)

"""
:function - take_first(elem):
            returns the first element of a tuple
:parameter - elem - the tuple
:returns - the first element
"""


def take_first(elem):
    return elem[0]

"""
:function - take_second(elem):
            returns the second element of a tuple
:parameter - elem - the tuple
:returns - the second element
"""


def take_second(elem):
    return elem[1]

"""
:function - take_third(elem):
            returns the third element of a tuple
:parameter - elem - the tuple
:returns - the third element
"""


def take_third(elem):
    return elem[2]

"""
:function - create_course(data):
            iterates through data to get the information of each course id,
            course name, and teacher. This information is then placed into a
            newly created Courses class
:parameters - data - a list of all information in the tests.csv file
:returns - courses - a populated courses class
"""


def create_courses(data):
    order = {}
    courses = Courses()

    ids = []
    names = []
    teachers = []
    i = 0
    for typ in range(0, 3, 1):
        if data[0] == "id":
            order["id"] = typ
        elif data[0] == "name":
            order["name"] = typ
        elif data[0] == "teacher":
            order["teacher"] = typ
        data.pop(0)

    for ind in range(order["id"], len(data), 3):
        ids.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["name"], len(data), 3):
        names.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["teacher"], len(data), 3):
        teachers.append(data[ind])
        i += 1

    for i in range(0, len(ids)):
        courses.insert(ids[i], names[i], teachers[i])
    return courses

"""
:function - create_tests(data, courses):
            iterates through data to get the information of each tests id,
            weight, and course id. This information is then placed into a
            previously populated Courses class
:parameters - data - a list of all information in the tests.csv file
            - courses - a populated courses class
:returns - courses - a fully populated courses class
"""


def create_tests(data, courses):
    order = {}

    test_ids = []
    course_id = []
    weight = []
    i = 0
    for typ in range(0, 3, 1):
        if data[0] == "id":
            order["id"] = typ
        elif data[0] == "course_id":
            order["course_id"] = typ
        elif data[0] == "weight":
            order["weight"] = typ
        data.pop(0)

    for ind in range(order["id"], len(data), 3):
        test_ids.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["course_id"], len(data), 3):
        course_id.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["weight"], len(data), 3):
        weight.append(data[ind])
        i += 1

    for i in range(0, len(test_ids)):
        courses.insert_test(course_id[i], test_ids[i], weight[i])
    return courses

"""
:function - create_students(data):
            iterates through data to get the information of each student's name
            and id, which is then placed in a newly crated Students class.
:parameters - data - a list of all information in the students.csv file
:returns - students - a populated Students class
"""


def create_students(data):
    order = {}
    students = Students()
    student_ids = []
    names = []
    i = 0
    for typ in range(0, 2, 1):
        if data[0] == "id":
            order["id"] = typ
        elif data[0] == "name":
            order["name"] = typ
        data.pop(0)

    for ind in range(order["id"], len(data), 2):
        student_ids.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["name"], len(data), 2):
        names.append(data[ind])
        i += 1

    for i in range(0, len(student_ids)):
        students.insert(student_ids[i], names[i])
    return students

"""
:function - create_marks(data, students, courses):
            iterates through the marks each student gets and places them
            in the appropriate student class.
:parameters - data - a list of all information in the marks.csv file
              students - a populated Students class
              courses -  a populated Courses class
"""


def create_marks(data, students, courses):
    order = {}

    test_ids = []
    student_id = []
    marks = []
    i = 0
    for typ in range(0, 3, 1):
        if data[0] == "test_id":
            order["test_id"] = typ
        elif data[0] == "student_id":
            order["student_id"] = typ
        elif data[0] == "mark":
            order["mark"] = typ
        data.pop(0)

    for ind in range(order["test_id"], len(data), 3):
        test_ids.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["student_id"], len(data), 3):
        student_id.append(data[ind])
        i += 1
    i = 0
    for ind in range(order["mark"], len(data), 3):
        marks.append(data[ind])
        i += 1

    for i in range(0, len(test_ids)):
        course = courses.get_test(test_ids[i])
        students.students[student_id[i]].insert_test(test_ids[i], marks[i], take_first(course))
    return students

"""
:function - create_report_card(student, courses, file):
            this function takes the information of a student and figures out the grade they
            achieve in each of their courses. Once this is done an average is calculated and
            the information is written to a file.
:parameters - courses - the courses class containing information of all of the courses
              students - the students class containing all information of all of the students
              file - the file where the information will be written to
"""


def create_report_card(student, courses, file):
    student.sort_test()

    student_name = student.get_name()
    student_id = student.id
    student_tests = student.get_tests()
    course_id = None
    teacher_name = None
    course_name = None
    classes = []
    teachers = []
    averages = []
    total_weight = 0
    total_average = 0
    average = 0

    for test in student_tests:
        if course_id is None:
            course_id = str(take_third(test))
            teacher_name = courses.get_teacher(course_id)
            course_name = courses.get_name(course_id)

        if course_id != str(take_third(test)):
            if total_weight != 100:
                raise Exception(' student {} has not completed: {}\n'.format(student_id, course_id))

            else:
                classes.append(course_name)
                teachers.append(teacher_name)
                averages.append(average)
                total_average += average

            course_id = str(take_third(test))
            teacher_name = courses.get_teacher(course_id)
            course_name = courses.get_name(course_id)
            average = 0
            total_weight = 0

        test_id = take_first(test)
        grade = take_second(test)
        weight = take_second(courses.get_test(test_id))
        mark = (int(grade) * int(weight))/100
        average += mark
        total_weight += int(weight)

    if student_tests is None:
        file.write("Student Id: "+student_id+", name: "+student_name+"\n")
        file.write("Total Average:\t"+str(format(total_average, '.2f'))+"%\n\n\n")
        return
    if total_weight != 100:
        raise Exception(' student {} has not completed: {}\n'.format(student_id, course_id))

    else:
        classes.append(course_name)
        teachers.append(teacher_name)
        averages.append(average)
        total_average += average

    total_average = total_average/len(averages)
    file.write("Student Id: "+student_id+", name: "+student_name+"\n")
    file.write("Total Average:\t"+str(format(total_average, '.2f'))+"%\n\n")
    for i in range(0, len(classes)):
        file.write("\tCourse: "+classes[i]+", Teacher: "+teachers[i]+"\n")
        file.write("\tFinal Grade:\t"+str(format(averages[i], '.2f'))+"%\n\n")
    file.write("\n")

"""
:function - generator(courses, students):
            opens a new file where the grades will be written, to do this
            a list of student ids are retrieved from students where they are iterated through.
:parameters - courses - the courses class containing information of all of the courses
              students - the students class containing all information of all of the students
"""


def generator(courses, students):
    students.sort_ids()
    file = open("output.txt", "w+")
    for student_id in students.get_student_ids():
        create_report_card(students.get_student(str(student_id)), courses, file)
    file.close()

"""
:function - main():
            main() begins the program  by asking the user for input where which
            is then interpreted, scanned and sent to their proper locations
"""


def main():

    courses = None
    students = None

    for i in range(0, 4, 1):
        Input = input("Please enter the file ")
        file = open(Input, "r")
        data = file.read()
        file.close()

        data = re.split(",|\n", data)
        while "" in data:
            data.remove("")
        if i == 0:
            courses = create_courses(data)
        elif i == 1:
            students = create_students(data)
        elif i == 2:
            courses = create_tests(data, courses)
        elif i == 3:
            students = create_marks(data, students, courses)
    generator(courses, students)


main()

"""
if __name__ == "__main__":
    courses = None
    students = None
    file1 = open("courses2.csv", "r")
    data = file1.read()
    data = re.split(",|\n", data)
    while "" in data:
        data.remove("")
    courses = create_courses(data)
    file1.close()

    file1 = open("students2.csv", "r")
    data = file1.read()
    data = re.split(",|\n", data)
    while "" in data:
        data.remove("")
    students = create_students(data)
    file1.close()

    file1 = open("tests2.csv", "r")
    data = file1.read()
    data = re.split(",|\n", data)
    while "" in data:
        data.remove("")
    courses = create_tests(data, courses)
    file1.close()

    file1 = open("marks2.csv", "r")
    data = file1.read()
    data = re.split(",|\n", data)
    while "" in data:
        data.remove("")
    students = create_marks(data, students, courses)
    file1.close()

    generator(courses, students)
"""
