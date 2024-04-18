from student import Student

stu1 = Student("Brian", "Nordlinger", 12345)

print(stu1)
print(stu1.get_energy_level())
stu1.take_exam()
print(stu1.get_energy_level())
print(stu1.greeting())