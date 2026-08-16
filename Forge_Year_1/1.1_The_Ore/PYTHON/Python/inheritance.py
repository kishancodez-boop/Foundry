class Engineering:
    def __init__(self,college_name,course):
        self.college_name=college_name
        self.course=course

class Student(Engineering):
    def __init__(self,college_name,course,name,usn):
        super().__init__(college_name,course)
        self.name=name
        self.usn=usn
    def details(self):
        print(f"Hi my name is - {self.name} , USN - {self.usn} , of course - {self.course} from {self.college_name} college.")
student = Student("AMC","CSE","kishan","123456789")
student.details()

###################################################



