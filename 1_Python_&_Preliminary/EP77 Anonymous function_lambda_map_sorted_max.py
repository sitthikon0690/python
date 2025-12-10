#lambda function คือ ฟังชั่นที่เรายังไม่คืดชื่อ
'''
lambda arguments : expession
'''
a=lambda a:a
b=lambda a,b:a+b
print(a(1))
print(a([1,2,3]))
print(b(1,2))
print('')
def c(c):
    print(c)
    #c=ตัวเลข
    #x=เลขคูณ
    return lambda s:c*s #รีเทิร์น lambda กลับไปที่ x
x=c(2)
y=x(3) #กำหนดค่าให้ s ใน lambda
print(y)

z=[1,2,3]
print("-"*20)
print("z",list(map(lambda a:a, z)))

print("-"*20)
items = [("a", 3), ("b", 1), ("c", 2)]
a = sorted(items, key=lambda x: x[1])  # เรียงตามคอลัมน์ที่ 2
print(type(a),a)

print("-"*20)
students = [{"name":"Ann","score":78}, {"name":"Bee","score":92}]
top = max(students, key=lambda s: s["score"])
print(top)

print("-"*20)
words = ["cat", "dog", "bird"]
print(list(map(lambda s: s.upper(), words)))