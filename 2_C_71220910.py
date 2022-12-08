daftar_angka = input ("masukkan angka: ")
angka = input ("masukkan angka yang dihitung: ")
jumlah = 0
for i in range(len(daftar_angka)):
    if daftar_angka[i] == angka:
        jumlah += 1
print ("angka {} muncul sebanyak {} kali". format (angka, jumlah))