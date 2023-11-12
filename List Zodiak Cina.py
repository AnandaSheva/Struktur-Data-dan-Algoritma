# Membuat list zodiak cina
zodiak_cina = ['Tikus', 'Kerbau', 'Macan', 'Kelinci', 'Naga', 'Ular', 'Kuda', 'Kambing', 'Monyet', 'Ayam', 'Anjing', 'Babi']

# Menentukan tahun kelahiran
tahun = int(input("Masukkan tahun kelahiran anda: "))

# Menentukan zodiak berdasarkan tahun kelahiran
zodiak_tahun = zodiak_cina[(tahun - 4) % 12]

# Menampilkan zodiak berdasarkan tahun kelahiran
print("Zodiak Cina anda berdasarkan tahun kelahiran adalah:", zodiak_tahun)

# Menentukan bulan kelahiran
bulan = int(input("Masukkan bulan kelahiran anda (1-12): "))

# Menentukan zodiak berdasarkan bulan kelahiran
if bulan == 1:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 2:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 3:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 4:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 5:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 6:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 7:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 8:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 9:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 10:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 11:
  zodiak_bulan = zodiak_cina[(tahun - 4) % 12]
elif bulan == 12:
  zodiak_bulan = zodiak_cina[(tahun - 3) % 12]
else:
  print("Bulan yang anda masukkan salah")

# Menampilkan zodiak berdasarkan bulan kelahiran
if bulan in range(1, 13):
  print("Zodiak Cina anda berdasarkan bulan kelahiran adalah:", zodiak_bulan)
