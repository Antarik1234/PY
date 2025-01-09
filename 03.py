class Student:
    def __init__(self,f,l,r):
        self.fName=f
        self.lName=l
        self.reg=r
        self.email=f'{self.reg}@gamil.com'

std1 = Student('Amar','Ali','MCT-UET-01')
std2 = Student('Akbar','Khan','MCT-UET-02')

print(std1.fName)
print(std2.email)