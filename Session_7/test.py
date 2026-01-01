class person :
    def __init__(self,name , age , gander):
        self.name = name
        self.age = age
        self.gander = gander
    def display(self):
        print (f"my name is {self.name},my age is {self.age},my gander is {self.gander}")
    def number_of_days_in_My_age(self):
        days = self.age * 365
        print (f"my age is {days} days")
class student(person) :
    def __init__(self,name,age,gander,student_id,grade):
        person.__init__(self,name,age,gander)
        self.student_id = student_id
        self.grade = grade
    def display(self):
        person.display(self)
        print(f"{self.student_id} is {self.grade}")

std1 = student("Abdo",21,"Male",227253,"four")
std1.display()