#Function คือ โปรแกรมย่อยที่อยู่ในโปรแกรมหลัก
'''
เช่น
Function max
Function min
และอื่นๆ

โปรแกรม เฟสบุ๊ค
Function ที่ 1 โพส
Function ที่ 2 ไลค์สด
Function ที่ 3 แชท
และอื่นๆ
'''

a=[0,1,2,3]
a2=[1,0,0,0]
n=0

def f1(c,b,e):
    c[0]+=e[0]
    c[1]+=1
    c[2]=5
    e=[1,2,3,4]
    b+=1

f1(a,n,a2)
print(a)
print(a2)
print(n)