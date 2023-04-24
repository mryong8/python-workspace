

even_num = []

for i in range(10):
    if i % 2 == 0:
        even_num.append(i)
        print("for -> ", even_num)
    
print(even_num)
my_num = even_num
even_num.reverse()
print("even_num -> ", even_num)
print("my_num -> ", my_num)




a = 3
b = a
print("b -> ", b)
a = 4
print("b -> ", b)
import sys
aa = sys.getrefcount(a)

print("aa -> ", aa)


class Test:
    name = "yong8"
    score = 100

print(f"{Test.name}의 점수는 {Test.score}")


a = 3
mystr = f"{a:02d}"
print(mystr)




even_num = [i for i in range(10) if i % 2 == 0]
print("num list -> ", even_num)


even_num = [i for i in range(10) if i % 2 == 1]
print("num list -> ", even_num)


even_num = [i*i for i in range(10)]
print("num list -> ", even_num)


a = 1, 2, 3

print("a -> ", a)
print("a type -> ", type(a))

n1, n2, n3 = a
print("n1, n2, n3 -> ", n1, n2, n3)


scores = 1, 2, 3, 4, 5, 6, 7
low, *tt, high = scores
print("scores low -> ", low)
print("scores tt -> ", tt)
print("scores high -> ", high)

s, *ttt, d = scores
print("scores s -> ", s)
print("scores ttt -> ", ttt)
print("scores d -> ", d)

def ft(n1, n2, n3):
    return n1+n2+n3

scores = 1, 2, 3
result = ft(*scores)
print("result -> ", result)



name = 'yong', 'min', 'seo'
price = 500, 1000, 1500

z = zip(name, price)
print("z -> ", list(z))
print("z -> ", list(z))
print("z -> ", list(z))

print("z -> ", list(z))
print("z -> ", list(z))

print("z -> ", list(z))
print("z -> ", list(z))

print("z -> ", list(z))
print("z -> ", list(z))

print("z -> ", list(z))
print("z -> ", list(z))

