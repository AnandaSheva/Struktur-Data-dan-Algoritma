# Meminta input list bilangan dari pengguna
bilangan = list(map(int, input("Masukkan list bilangan (pisahkan dengan spasi): ").split()))

# Inisialisasi bilangan terbesar dan terkecil
terbesar = bilangan[0]
terkecil = bilangan[0]

# Looping untuk mencari bilangan terbesar dan terkecil
for num in bilangan:
    if num > terbesar:
        terbesar = num
    elif num < terkecil:
        terkecil = num

# Menampilkan hasil
print("Bilangan terbesar: ", terbesar)
print("Bilangan terkecil: ", terkecil)
