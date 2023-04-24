



a = 1
print("a -> ", a)
print(id(a))

b = 1
print("b -> ", b)
print(id(b))

c = a
print("c -> ", c)
print(id(c))

a = 2
print("a -> ", a)
print(id(a))

print("c -> ", c)
print(id(c))


abc = [1, 2, 3]
print("abc -> ", id(abc))

print("abc'[0]' id -> ", id(abc[0]))
print("abc'[1]' id -> ", id(abc[1]))
print("abc'[2]' id -> ", id(abc[2]))


aa = 1
bb = aa

print("aa id -> ", id(aa))
print("bb id -> ", id(bb))
print("aa == bb-> ", id(aa) == id(bb))
print("aa is bb-> ", id(aa) is id(bb))


aa = 2
bb = 2

print("aa id -> ", id(aa))
print("bb id -> ", id(bb))
print("aa == bb-> ", id(aa) == id(bb))
print("aa is bb-> ", id(aa) is id(bb))

