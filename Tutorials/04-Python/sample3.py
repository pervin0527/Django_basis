class Student():
    school_name = "MIT" ## class attributes, 모든 인스턴스가 동일하게 가지고 있는 속성.

    def __init__(self, name, age):
        ## instance attributes, 인스턴스마다 가지는 값이 서로 다름.
        self.name = name
        self.age = age


student1 = Student(name="Maria", age="20")
student2 = Student(name="Jake", age="21")
print(student1.name, student1.age)
print(student1.school_name, student2.school_name)

Student.school_name = "Seoul Univ"
print(Student.school_name)
print(student1.school_name, student2.school_name)

class Circle():
    pi = 3.141592
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * self.pi ## class attributes에 접근할 때도 self를 사용함.
    
circle1 = Circle(radius=10)
print(circle1.area())