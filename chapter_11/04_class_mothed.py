# class Employe:
#     a = 1
#     def show(self):
#         print("The class value of a is ",self.a)


# o = Employe()
# o.a = 2
# o.show() # The class value of a is  2


class Employe:
    a = 1
    @classmethod
    def show(cls):
        print("The class value of a is ",cls.a)


o = Employe()
o.a = 2
o.show() # The class value of a is  1