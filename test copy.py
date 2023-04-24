
        
        
class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Exception {} arguments'.format(len(self._fields)))
        
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            print("222222222222222222")
            
            

class Point(Structure):
    _fields = ["xx", "y", "z", "u"]
    print("1111111111111111")
    
p = Point(1, 2, 3, 4)
print("객체 속성 확인", p.__dict__)


y_list = ['A', 'B', 'C']
pp = {string : i for i,string in enumerate(y_list)}
print("객체 속성 확인", pp)