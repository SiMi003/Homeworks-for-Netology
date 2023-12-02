def averege_dict(dict_):
    values = list(dict_.values())
    values_list = [x for t in values for x in t]
    from statistics import mean
    average_value = round(mean(values_list), 2)
    return average_value


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def lecture_grading(self, mentor, course, grade):
        if (isinstance(mentor, Lecturer) and course in self.courses_in_progress
            and course in mentor.courses_attached):
            if course in mentor.lect_grades:
                mentor.lect_grades[course] += [grade]
            else:
                mentor.lect_grades[course] = [grade]
        else:
            return 'Error of the input data'              
    
    def __str__(self):
        stud_average_grade = averege_dict(self.grades)
        return (f'Name: {self.name}{'\n'}Surname: {self.surname}{'\n'}'
                f'Average grade per homeworks: {stud_average_grade}{'\n'}'
                f'Courses in a progress: {', '.join(self.courses_in_progress)}{'\n'}' 
                f'Complited courses: {', '.join(self.finished_courses)}')
        
    def __gt__(self, other):
        return (f'Student {self.name} {self.surname} '
                f'is cooler then student {other.name} {other.surname}: '
                f'{averege_dict(self.grades) < averege_dict(other.grades)}')
    
    def __lt__(self, other):
        return (f'Student {other.name} {other.surname} '
                f'is cooler then student {self.name} {self.surname}: '
                f'{averege_dict(self.grades) > averege_dict(other.grades)}') 
      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
  

class Lecturer(Mentor):
    lect_grades = {}
    
    def __gt__(self, other):
        return (f'Lectorer {self.name} {self.surname} ' 
                f'is cooler then lectorer {other.name} {other.surname}: '
                f'{averege_dict(self.lect_grades) < averege_dict(other.lect_grades)}')
    
    def __lt__(self, other):
        return (f'Lectorer {other.name} {other.surname} '
                f'is cooler then lectorer {self.name} {self.surname}: '
                f'{averege_dict(self.lect_grades) > averege_dict(other.lect_grades)}') 
    
    def __str__(self):
        lect_average_grade = averege_dict(self.lect_grades)
        return (f'Name: {self.name}{'\n'}Surname: {self.surname} '
                f'{'\n'}Average grade per lection: {lect_average_grade}')


class Reviewer(Mentor):
    def __str__(self):
        return f'Name: {self.name}{'\n'}Surname: {self.surname}'
    
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error in the input data'


student1 = Student('Albina', 'Ronina', 'female')
student1.courses_in_progress += ['Python', 'Java', 'BI', 'C++', 'Frontend developer']
student1.finished_courses += ['Fullstack developer', 'Machine learning']
student1.grades = {'Python': [5, 6, 6, 5], 'BI': [5, 6, 5], 'C++': [5, 4]}

student2 = Student('Mihail', 'Varnin', 'male')
student2.courses_in_progress += ['Python', 'HTML', 'SQL']
student2.finished_courses += ['Backend developer', 'Data visualithation', 'C++']
student2.grades = {'Python': [4, 5, 6], 'HTML': [5, 4], 'SQL': [5]}


mentor1 = Reviewer('Vadim', 'Petrov')
mentor1.courses_attached += ['Python', 'C++', 'Fullstack developer', 'Backend developer']

mentor2 = Reviewer('Alisa', 'Omneva')
mentor2.courses_attached += ['Java', 'Frontend developer', 'HTML', 'SQL']


mentor3 = Lecturer('Aleksandra', 'Panova')
mentor3.courses_attached += ['Python', 'Fullstack developer', 'Backend developer', 'Frontend developer']
mentor3.lect_grades = {'Python': [5, 6, 7], 'Backend developer': [4]}

mentor4 = Lecturer('Nikita', 'Semenov')
mentor4.courses_attached += ['BI', 'Data visualithation', 'HTML', 'SQL']
mentor4.lect_grades = {'BI': [3, 5], 'HTML': [4, 5, 3]}


print(f'STUDENTS:{'\n'}{student1}{'\n'}{student2}'
      f'{'\n'}REVIEWERS:{'\n'}{mentor1}{'\n'}{mentor2}'
      f'{'\n'}LECTURERS:{'\n'}{mentor3}{'\n'}{mentor4}'
      f'{'\n'}COMPARISON OF LECTURERS AND STUDENTS:{'\n'}'
      f'{student1 > student2}{'\n'}{mentor3 > mentor4}{'\n'}'   
      f'{student1 < student2}{'\n'}{mentor3 < mentor4}{'\n'}')


mentor2.rate_hw(student1, 'Java', 10)              # Creating a new key and writing a grade
mentor1.rate_hw(student1, 'Python', 1)             # Writing a grade to the existed key
mentor2.rate_hw(student2, 'Frontend developer', 6) # Error, courses not in progress for that student
mentor2.rate_hw(student2, 'HTML', 10)              # Writing a grade to the existed key

student1.lecture_grading(mentor3, 'Frontend developer', 1)  # Creating a new key and writing a grade
student1.lecture_grading(mentor3, 'Fullstack developer', 8) # Error, courses not in progress for that student
student2.lecture_grading(mentor3, 'Python', 10)             # Writing a grade to the existed key
student2.lecture_grading(mentor4, 'Java', 5)                # Error, courses not in a lecturer list 
student2.lecture_grading(mentor4, 'HTML', 10)               # Writing a grade to the existed key
student2.lecture_grading(mentor4, 'SQL', 10)                # Creating a new key and writing a grade

print('Rankings of students and lectorers after data update:')
print(f'STUDENTS:{'\n'}{student1}{'\n'}{student2}'
      f'{'\n'}LECTURERS:{'\n'}{mentor3}{'\n'}{mentor4}'
      f'{'\n'}COMPARISON OF LECTURERS AND STUDENTS:{'\n'}'
      f'{student1 > student2}{'\n'}{mentor3 > mentor4}{'\n'}'
      f'{student1 < student2}{'\n'}{mentor3 < mentor4}{'\n'}')