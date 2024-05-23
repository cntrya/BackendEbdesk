import math
def persegi(s):
    return s * s
def persegi_panjang(p, l):
    return p * l
def segitiga(a, t):
    return (a * t) / 2
def lingkaran(r):
    return math.pi * r * r
def trapesium(a, b, t):
    return 0.5 * (a + b) * t
def jajar_genjang(a, t):
    return a * t
def belah_ketupat(d1, d2):
    return d1 * d2

def LuasBangun():
    print("Pilih bangun yang ingin dihitung luasnya: ")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Trapesium")
    print("6. Jajar Genjang")
    print("7. Belah Ketupat")

    print()

    opsi = input("Masukkan pilihan (1-7): ")

    print()

    if opsi in ["1", "2", "3", "4", "5", "6", "7"]:

        if opsi == "1":
            s = float(input("Masukkan panjang sisi: "))
            bangun = "Persegi"
            hasil = persegi(s)

        elif opsi == "2":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))
            bangun = "Persegi Panjang"
            hasil = persegi_panjang(p, l)

        elif opsi == "3":
            a = float(input("Masukkan panjang alas: "))
            t = float(input("Masukkan tinggi: "))
            bangun = "Segitiga"
            hasil = segitiga(a, t)

        elif opsi == "4":
            r = float(input("Masukkan panjang jari-jari: "))
            bangun = "Lingkaran"
            hasil = lingkaran(r)

        elif opsi == "5":
            a = float(input("Masukkan panjang sisi atas: "))
            b = float(input("Masukkan panjang sisi bawah: "))
            t = float(input("Masukkan tinggi: "))

        elif opsi == "6":
            a = float(input("Masukkan panjang alas: "))
            t = float(input("Masukkan tinggi: "))
            bangun = "Jajar Genjang"
            hasil = jajar_genjang(a, t)

        elif opsi == "7":
            d1 = float(input("Masukkan panjang diagonal pertama: "))
            d2 = float(input("Masukkan panjang diagonal kedua: "))

        print()

        print(f"Hasil perhitungan luas {bangun} adalah {hasil} ")

    else:
        print("Maaf, pilihan yang Anda masukkan salah")
        print("Silahkan coba lagi...")

    print()

    def main():
        for i in range(1):
            ulangi = input("Apakah Anda ingin melakukan penghitungan lagi? (y/t) : ")
            print()
            if ulangi.lower() != "y":
                print("Baiklahh, Terimakasih yaa sudah mencoba program ini!")
                break
            else:
                LuasBangun()

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    LuasBangun()
