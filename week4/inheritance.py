class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age
  
	def sleep(self):
		print(f"{self.name} is sleeping People..")
  
class Student(People):
    def __init__(self, name, age, student_id):
        #People.__init__(self, name, age)
        super().__init__(name, age)
        self.student_id = student_id
    def sleep(self):
        print(f"{self.name} is sleeping Student..")
        
student_1 = Student("Gino", 20, 99)
student_1.sleep()