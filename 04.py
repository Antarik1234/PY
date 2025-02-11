class Student:
    'This class defines a Student for Mechatronics Department'
    department="Mechatronics"
    offSubjects=['Mech', 'LA', 'ES', 'CP-II', 'MOM', 'Proj']

    def __init__(self, fName, lName, reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.courses=['Proj']

    def registerSubject(self, *sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'(s) is not offered!')
            if s in Student.offSubjects and s not in self.courses:
                self.courses.append(s)

## Main Program ##

std1=Student('Anwar', 'Ali', 'MCT-UET-01')
std2=Student('Akbar', 'Khan', 'MCT-UET-02')
std3=Student('Hamza', 'Akhtar', 'MCT-UET-03')
std1.registerSubject('CP-II', 'MOM', 'MOM')
std1.department='Electrical'

print(std1.department,std2.department)

for i in std1.__dict__.items():
    print(i)
print('*****************')
for i in std2.__dict__.items():
    print(i)
print('******************')
for i in Student.__dict__.items():
    print(i)