class Animals:
    pass
class pets(Animals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("dog is barking")

a = dog()
a.bark()