fw=open('1_Python_&_Preliminary/EP93.1.txt',"w",encoding="utf-8")# W เป็นการสร้างไฟล์เพื่อเขียน  และถ้ามีอยู่แล้วจะเขียนทับอันเก่า
#ทดสอบความยาว
fw.writelines("jmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeori")
fw.writelines("qqqqq")
fw.writelines("1")
fw.writelines("\n555")
fw.close

fw=open('1_Python_&_Preliminary/EP93.1.txt',"r")
print(fw.read())
fw.close

# fw=open("EP93.2.txt","r")
# print(fw.read())
# fw.close


'''
    f.write("hello")
    f.writelines(["a\n", "b\n", "c\n"])  # ต้องใส่ \n ในแต่ละสตริงเอง
    .writelines(f"{n}\n" for n in nums) / f.write("\n".join(map(str, nums)) + "\n(บรรทัดถัดไปต้องขึ้นใหม่)")
'''