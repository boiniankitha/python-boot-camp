class Animal:
    def speak():
        return "speaking..."
class dog (animal):
    def speak():
    return "dog..."
class puppy(dog):
    def speak():
        return "puppy is speaking"
obj3=puppy
print(obj3.speak())
               