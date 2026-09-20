class Student:
    grade = 9
    name = "Hasan"
    
    def introduction(self):
        print("Hi I am a student")
        
    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

cat = Student()
cat.introduction()
cat.details()