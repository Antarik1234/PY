class Student:
    def initial(obj,f,l,r):
        obj.fName=f
        obj.lName=l
        obj.reg=r
        
    
std1=Student()
std2=Student()

Student.initial(std1,'Amar','Ali','MCT-UET-01')
std2.initial('Akbar','Khan','MCT-UET-02')

print(std1.fName)
print(std2.reg)