import math

print(" Nama    : Rakha Shidqi wirawan")
print(" NIM     : 20230801280")
print(" Prodi   : Teknik Informatika")
print("                                     ")


def luas_persegi(sisi):
    """Fungsi untuk menghitung luas persegi."""
    return sisi ** 2

def luas_persegi_panjang(panjang, lebar):
    """Fungsi untuk menghitung luas persegi panjang."""
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    """Fungsi untuk menghitung luas segitiga."""
    return 0.5 * alas * tinggi

def main():
    print("Pilih bangun datar:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")

    pilihan = input("Masukkan pilihan Anda (1/2/3): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print("Luas persegi:", luas_persegi(sisi))
    elif pilihan == '2':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        print("Luas persegi panjang:", luas_persegi_panjang(panjang, lebar))
    elif pilihan == '3':
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print("Luas segitiga:", luas_segitiga(alas, tinggi))
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
