classmates = ["Ferdinand", "Lucas", "Regan", "Hunter", "Maddox"]
print("Original list:", classmates)
print("First classmate:", classmates[0])
print("Third classmate:", classmates[2])
print("Last classmate:", classmates[-1])
classmates.append("Clara")
print("After adding a name:", classmates)
classmates.remove("Regan")
print("After removing a name:", classmates)
classmates.sort()
print("Sorted list:", classmates)
classmates.reverse()
print("Reversed list:", classmates)
teacher = {
    "name": "Mrs. Ebner",
    "subject": "English",
    "experience": 22
}
print("Teacher profile:", teacher)
print("Teacher's name:", teacher["name"])
print("Teacher's subject:", teacher["subject"])
teacher["subject"] = "English"
print("Updated teacher profile:", teacher)
names = ["Ferdinand", "Lucas", "Hunter", "Clara"]
grades = [9, 9, 9, 9]
student_directory = dict(zip(names, grades))
print("Student directory:", student_directory)