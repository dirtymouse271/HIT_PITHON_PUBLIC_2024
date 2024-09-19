'''
OOP python
class ClassName:
# khai bao thuoc tinh
    sound = "voice"
# dinh nghia phuong thuc khoi tao
    def __init__(self, name, age):
    self.name = name
    self.age = age
'''
# class person:
#     sound = "yo"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sleep(self):
#         print(self.name, "is sleeping")
# # student1 = person('Thanh',19)
# # print(student1.age, student1.name, student1.sound)
# # student = person('Dirty Mouse', 20)
# # student.sleep()
# class Teacher:
#     basicSalary = 4160000
#     def __init__(self, name, age, oeffSalary):
#         self.name = name
#         self.age = age
#         self.oeffSalary = oeffSalary
#     def getSalary(self):
#         return self.oeffSalary * Teacher.basicSalary
 
# t1 = Teacher('Thanh', 19, 4.)
# t2 = Teacher('Dirty Mouse', 20, 2.)
# print(t1.basicSalary, t2.basicSalary)
# t1.getSalary()
# print(t1.getSalary())

class person:
    def __init__(self,name,age,hometown):
        self._name = name
        self._age = age
        self._hometown = hometown

class KYSU(person):
    def __init__(self, name, age, hometown, major, year):
        super().__init__(name, age, hometown)
        self._major = major
        self._year = year
    def printt(self):
        print(self._name, self._age, self._hometown, self._major, self._year)

kySu1= KYSU('Thanh', 19, 'Phu Tho', 'CNTT', 2026)
kySu1.printt()
