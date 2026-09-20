class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Parrot("Bob", 10)
billy = Parrot("Billy", 15)

print(bob.species)
print(billy.species)
print(bob.name, bob.age)
print(billy.name, billy.age)