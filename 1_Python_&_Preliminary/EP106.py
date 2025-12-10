a3=2.11112
print("dfgfd {:.2f}".format(a3))
print(f"{"fvdfvdf":15}{a3:>15}".format(a3))
#BMI=float("%.1f"%(BMI)) #แปลงเป็น 1 ตำแหน่ง
#BMI=float("{:.1f}".format(BMI)) #แปลงเป็น 1 ตำแหน่งprint(BMI)


member = str.upper(input("T/F: "))
#if member == "T" or member == "t": #if member in "T","ts"

num1 , num2 = eval ( input ( ' Please enter number 1,number 2 : ' ) )
print ( num1 , ' + ' , num2 , ' = ' , num1 + num2 )
a=[]
for i in range(3):
     a.append(input ( " >>> " )) #ใส่ตัวเลขเลยเลื่อยๆ
print(a)

code = "print('Hello World!')"
exec(code)