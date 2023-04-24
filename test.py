person = {"name":"ricepotato", "email":"sukjun402@naver.com"}
new_person = {**person, "phone":"010-123-1234"}
print("** person :", person)
print("** new person :", new_person)



class Point():
    def __init__(self, x, y, z, u):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        
        
class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Exception {} arguments'.format(len(self._fields)))
        
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            print("** ================")