
#Класс Student:
class Student:
    def __init__(self, id, surname, name, patronymic, dob, address, phone, faculty, course, group):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.dob = dob
        self.address = address
        self.phone = phone
        self.faculty = faculty
        self.course = course
        self.group = group

    def setTun(self, new_tun):
        self.tun = new_tun

    def getTun(self):
        
        return self.tun

    def __str__(self):
        return f"№{self.id}, {self.surname} {self.name} {self.patronymic}, {self.dob}, {self.address}, {self.phone}, " \
               f"{self.faculty}, {self.course} курс, гр. {self.group}"

    def __hash__(self):
        return hash((self.id, self.surname, self.name, self.patronymic))

    def getId(self):
        return self.id

    def getSurname(self):
        return self.surname

    def getName(self):
        return self.name

    def getPatronymic(self):
        return self.patronymic

    def getDob(self):
        return self.dob

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getFaculty(self):
        return self.faculty

    def getCourse(self):
        return self.course

    def getGroup(self):
        return self.group


#Создаем массив объектов:
students = [
    Student(1, "Иванов", "Иван", "Иванович", "02.12.1998", "ул. Пушкина 1", "88005553535", "ИКНТ", 2, "ИКНТ-21"),
    Student(2, "Петров", "Петр", "Петрович", "05.05.1999", "ул. Ильфа и Петрова 11", "88009009090", "ИКНТ", 2,
            "ИКНТ-21"),
    Student(3, "Сидоров", "Сидор", "Сидорович", "12.08.2000", "ул. Лермонтова 5", "88005553535", "ИКНТ", 1, "ИКНТ-22"),
    Student(4, "Смирнов", "Дмитрий", "Иванович", "23.02.1998", "ул. Пушкина 1", "88003334444", "ФИТИС", 2,
            "ФИТИС-21"),
    Student(5, "Кузнецов", "Илья", "Петрович", "17.10.1999", "ул. Ильфа и Петрова 11", "88004445555", "ФИТИС", 1,
            "ФИТИС-22"),
    Student(6, "Михайлов", "Александр", "Владимирович", "22.06.2000", "ул. Лермонтова 5", "88006667777", "ФИТИС", 1,
            "ФИТИС-22")
]


#a) Вывод списка студентов заданного факультета:
faculty = input("Введите название факультета: ")
faculty_students = list(filter(lambda s: s.getFaculty() == faculty, students))
print(f"Список студентов факультета {faculty}:")
for student in faculty_students:
    print(student)


#b) Вывод списков студентов для каждого факультета и курса:
faculty_course_students = {}
for student in students:
    if student.getFaculty() not in faculty_course_students:
        faculty_course_students[student.getFaculty()] = {}
    if student.getCourse() not in faculty_course_students[student.getFaculty()]:
        faculty_course_students[student.getFaculty()][student.getCourse()] = []
    faculty_course_students[student.getFaculty()][student.getCourse()].append(student)

print("Списки студентов для каждого факультета и курса:")
for faculty, course_students in faculty_course_students.items():
    print(f"Факультет {faculty}:")
    for course, students in course_students.items():
        print(f"\t{course} курс:")
        for student in students:
            print(f"\t\t{student}")


#c) Вывод списка студентов, родившихся после заданного года:
year = int(input("Введите год: "))
year_students = list(filter(lambda s: int(s.getDob().split(".")[2]) > year, students))
print(f"Список студентов, родившихся после {year} года:")
for student in year_students:
    print(student)


#d) Вывод списка учебной группы:
group = input("Введите название группы: ")
group_students = list(filter(lambda s: s.getGroup() == group, students))
print(f"Список студентов группы {group}:")
for student in group_students:
    print(student)
