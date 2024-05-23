def penjumlahan(a, b):
    return a + b
def pengurangan(a, b):
    return a - b
def perkalian(a, b):
    return a * b
def pembagian(a, b):
    if b == 0:
        print("Tidak terdefinisi")
    else:
        return a / b

def OperasiMTK():
    print("Pilih operasi matematika: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    print()

    opsi = input("Masukkan pilihan (1-4): ")

    print()

    if opsi in ["1", "2", "3", "4"]:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        print()

        if opsi == "1":
            operasi = "Penjumlahan"
            hasil = penjumlahan(a, b)
        elif opsi == "2":
            operasi = "Pengurangan"
            hasil = pengurangan(a, b)
        elif opsi == "3":
            operasi = "Perkalian"
            hasil = perkalian(a, b)
        elif opsi == "4":
            operasi = "Pembagian"
            hasil = pembagian(a, b)
        print(f"Hasil {operasi} dari {a} dan {b} adalah {hasil} ")
    else:
        print("Maaf, pilihan yang Anda masukkan salah")
        print("Silahkan coba lagi...")

    print()

    def main():
        for i in range(1):
            ulangi = input("Apakah Anda ingin melakukan penghitungan lagi? (y/t) : ")
            print()
            if ulangi.lower() == "y":
                OperasiMTK()
            else:
                print("Baiklahh, Terimakasih yaa sudah mencoba program ini!")
                break

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    OperasiMTK()
