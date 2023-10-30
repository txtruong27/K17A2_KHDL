#1.1
print("** ** ******    **      **     ** ****" )
print("** ** **        **      **     **   **")
print("***** ******    **      **     **   **")
print("** ** **        **      **     **   **")
print("** ** ** ****   ******  ******  ******")
#1.3
ten_hang = "Sua hop Vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Ten hang:", ten_hang)
print("So luong:", so_luong)
print("Tien phai tra:", tien_phai_tra)
#1.4
import math
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Dien tich cua tam giac:", s)