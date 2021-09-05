class Student(object):
    def __init__(self,name,age,grade,gender,marks,course):
        self.name=name
        self.age=age
        self.grade=grade
        self.gender=gender
        self.marks=marks
        self.course=course

    def get_nameGradeMarks(self):
        print(self.name,self.grade,self.marks)

    def checkCourseEligiblity(self):
        if self.age >=10:
            print('you are eligible to attend the course')
        else:
            print('try after ',(10-self.age),'years')

    def findPercentages(self):
        total =0
        for marks in self.marks:
            total=total+marks
        print ('percentage = ',(total/4))
S1=Student('Cheshta',15,10,'Female',[97,89,90,100],'Maths')
S1.get_nameGradeMarks()
S1.checkCourseEligiblity()
S1.findPercentages()