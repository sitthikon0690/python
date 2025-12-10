#Exeption
#สร้าง Exeption ด้วย raise raise เกิดขึ้นภายในบล็อก try โค้ดบรรทัดถัดไปใน try จะไม่ทำต่อ
# while True:
#     try:
#         c=input("ป้อนชื่อ : ")
#         if c in ("ก", "a"):
#             raise Exception("มีชื่อนี้ในระบบแล้ว")
#         a=int(input(":"))
#         b=int(input(":"))
#         if a == 0 and b == 0:
#             break
#         if a<0 or b>0:
#             raise Exception("มีชื่อนี้ในระบบแล้ว")
#         c=a/b
#         print(c)
#         print("โอนเงิน")
#     except Exception as e:
#         print(e)
#     finally:
#         print("ทำงานต่อไป")

try:
    print("A")
    raise ValueError("oops")
    print("B")         # <— ไม่รัน
except Exception as e:
    print("C:", e)     # <— มาที่นี่
else:
    print("D")         # <— ไม่รัน เพราะมีข้อยกเว้น
finally:
    print("E")         # <— รันเสมอ
    
# A
# C: oops
# E