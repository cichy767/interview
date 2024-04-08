# METHOD RESOLUTION ORDER
class A(object):
    def save(self):
        print("A")


class B(A):
    def save(self):
        print("B")


class C(A):
    def save(self):
        print("C")
    pass


class D(C, B):
    def save(self):
        print("D")
    pass


d = D()
d.save()
print(D.mro())
