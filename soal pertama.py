import math

#masukkan data
l1 = float(input("masukkan L1: "))
l2 = float(input("masukkan L2: "))
b1 = float(input("masukkan B1: "))
b2 = float(input("masukkan B2: "))
h1 = float(input("masukkan h1(m): "))
h2 = float(input("masukkan h2(m): "))
s23 = float(input("masukkan jarak(m): "))
a123 = float(input("masukkan sudut: "))
z21 = float(input("masukkan zenit_21: "))
z23 = float(input("masukkan zenit_23: "))
R = 6371000

#menghitung azimuth 21 dan azimuth 23
az21 = math.atan2(math.sin(math.radians(l2) - math.radians(l1)), 
                        (math.cos(math.radians(b1)) * math.tan(math.radians(b2)) - 
                         math.sin(math.radians(b1)) * math.cos(math.radians(l2) - math.radians(l1))))
az23 = az21 + math.radians(a123)
print("azimuth 21= ", az21)
print("azimuth 23= ", az23)

#menghitung koordinat titik 3
dh = h2 - h1
s21 = s23 * math.sin(math.radians(a123)) / math.sin(math.radians(180) - z21 - z23)
print("delta H= ", dh)
print("jarak 21= ",s21)

#koordinat titik 3
b3 = math.asin(math.sin(math.radians(b1)) * math.cos(s21 / R) + 
               math.cos(math.radians(b1)) * math.sin(s21 / R) * 
               math.cos(az21))
l3 = math.radians(l1) + math.atan2(math.sin(az21) * math.sin(s21 / R) 
                                   * math.cos(math.radians(b1)), math.cos(s21 / R) - 
                                   math.sin(math.radians(b1)) * math.sin(math.radians(b3)))
h3 = h1 + dh * s21 / s23

#konversi Ke degress
b3_deg = math.degrees(b3)
l3_deg = math.degrees(l3)

#Tampilkan hasil
print("Latitude koordinat titik 3  = " , l3_deg)
print("Longitude koordinat titik 3 = " , b3_deg)
print("Altitude koordinat titik 3  = " , h3)


