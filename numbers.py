

class Num:
    test = []
    def dddd(sdf):
        test = sdf
        return test


def trf(aaaa):
        _b = aaaa
        _b.reverse()
        return _b

numbers = list(map(int, input('input number : ').split()))

print("your numbers -> ", numbers)

numbers.reverse()

print("your numbers reverse -> ", numbers)

print("your numbers reverse -> ", trf(numbers))


b = trf(numbers)
print("your numbers reverse b -> ", b)
print("your numbers reverse numbers -> ", numbers)
b.reverse()

c = Num.dddd(numbers);
c.reverse()
c.reverse()

for i in zip(numbers, c):
    print(i)



print("\n")