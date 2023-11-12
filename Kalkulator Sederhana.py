def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y

while True:
    print("Pilih operasi.")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        
        break

    bilangan1 = float(input("Masukkan bilangan pertama: "))
    bilangan2 = float(input("Masukkan bilangan kedua: "))

    if pilihan == '1':
        print(bilangan1, "+", bilangan2, "=", tambah(bilangan1, bilangan2))

    elif pilihan == '2':
        print(bilangan1, "-", bilangan2, "=", kurang(bilangan1, bilangan2))

    elif pilihan == '3':
        print(bilangan1, "*", bilangan2, "=", kali(bilangan1, bilangan2))

    elif pilihan == '4':
        print(bilangan1, "/", bilangan2, "=", bagi(bilangan1, bilangan2))

    else:
        print("Input salah. Mohon masukkan pilihan yang valid.")
    
    input("\nAnada ingin menghitung lagi ? (Y/T)")
