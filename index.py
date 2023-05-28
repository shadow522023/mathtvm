import time
import os
import subprocess as sub
import math
import colorama
import corner_all as co



text_show_corol_renbow = ("""
  ____________________________
||                            ||
||                            ||
||      MATH COMUNITIONS      ||
||            v.0.1           ||
||            THAI            || 
||____________________________||
 """)

print(text_show_corol_renbow)
number_show = ("""
[0] อัปเดต (สคริป)

[1] หามุมรอบวงกลม(องศา,พิกัด,ตำแหน่ง,เรเดียน)        

[2] เปลี่ยน องศา เป็น เรีเดียน            

[3] เปลี่ยน เรเดี่ยน เป็น องศา


""")
print(number_show)
input_number = input("หมายเลขที่ต้องการ : ")
if input_number == "1":
    print("หามุมรอบวงกลม(องศา,พิกัด,ตำแหน่ง,เรเดียน)")
    co.corner()
    exit_1 = input("ออกหน้านี้พิมพ์ N : ")
    if exit_1 == "N":
        print("ออก")
    else :
        print("ออก")
elif (input_number) == "2":
    print("เปลี่ยน องศา เป็น เรีเดียน ")
elif (input_number) == "0":
    print("เริ่มการอัปเดต")
    os.system("cd $home")
    time.sleep(2)
    os.system("rm -rf mathtvm")
    time.sleep(2)
    os.system("git clone https://github.com/shadow522023/mathtvm.git")
    os.system("cd mathtvm")
    os.system("python3 index.py")
    print("อัปเดตเรียบร้อย")
   
    

