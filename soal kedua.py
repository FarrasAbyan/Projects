import math

slant = float(input("masukkan jarak miring(m): "))
azAB = float(input("masukkan azimut(°): "))
lA = float(input("masukkan lintang A(°): "))
hA = float(input("tinggi geodetic(m): "))

def haversine(lat1, lon1, lat2, lon2):
    # Mengonversi derajat ke radian
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Menghitung delta lintang dan bujur
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Rumus Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Jarak di elipsoida
    R = 6371000 # dalam meter
    d = R * c
    return d

# Menghitung koordinat titik B berdasarkan azimut dan jarak miring
azABrad = math.radians(azAB)
dlatB = slant * math.cos(azABrad) / 6371000 

# konversi jarak ke derajat lintang
dlonB = slant * math.sin(azABrad) / (6371000 * math.cos(math.radians(lA)))
latA = lA
lonA = 0 # Misalkan titik A berada di meridian nol
latB = latA + math.degrees(dlatB)
lonB = lonA + math.degrees(dlonB)

# Menghitung jarak menggunakan rumus Haversine
delips = haversine(latA, lonA, latB, lonB)

# Menambahkan tinggi geodetik A ke jarak
delipsh= math.sqrt(slant**2 + hA**2)

# Menampilkan hasil
print("Jarak di elipsoida (Haversine) dalam meter: ", delips)
print("Jarak miring dengan tinggi geodetik (Pythagoras) dalam meter: ", delipsh)