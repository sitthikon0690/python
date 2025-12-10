# + การรวมข้อมูล , extend
#a+=b,c,d a+=[b,c,d] ถ้าเป็น Listได้ เอาListไปยัดใส่  / a+= b + c + d extend
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a+b
print(c)
a.extend(b)
print(a)
a2=[1,2,3,4,5]
a2+=b
print(a2)

a2=[1,2,3]
b2=1
a2=a2+[b2]
print(a2)