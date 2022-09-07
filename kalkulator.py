def tambah (x,y): 
    a = x+y
    return a #mengembalikan hasil a
def kurang (x,y): #buat fungsi untuk pengurangan
    a = x-y #buat rumusnya
    return a #mengembalikan hasil a
def kali (x,y): #buat fungsi untuk perkalian
    a = x*y #buat rumusnya
    return a #mengembalikan hasil a
def bagi (x,y): #buat fungsi untuk pembagian
    a = x/y #buat rumusnya
    return a #mengembalikan hasil a

angka1 = int(input("masukkan angka pertama: "))
angka2 = int(input("masukkan angka kedua: "))

print("hasil",angka1,"+",angka2,"adalah", tambah(angka1,angka2))
print("hasil",angka1,"-",angka2,"adalah", kurang(angka1,angka2))
print("hasil",angka1,"x",angka2,"adalah", kali(angka1,angka2))  
print("hasil",angka1,":",angka2,"adalah", bagi(angka1,angka2))