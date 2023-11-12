# Meminta input dari pengguna
umur = int(input("Masukkan usia anda: "))
berat_badan = float(input("Masukkan berat badan anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan anda (cm): "))
durasi_latihan = int(input("Masukkan durasi latihan anda (dalam menit): "))

# Menghitung detak jantung maksimum
detak_jantung_maksimum = 220 - umur

# Menghitung zona target detak jantung
zona_target_rendah = detak_jantung_maksimum * 0.6
zona_target_tinggi = detak_jantung_maksimum * 0.7

# Menghitung kalori yang terbakar
kalori_terbakar_per_menit = 0.0175 * berat_badan
kalori_terbakar_total = kalori_terbakar_per_menit * durasi_latihan

# Menampilkan hasil
print("Detak jantung maksimum anda adalah:", detak_jantung_maksimum, "detak/menit")
print("Zona target detak jantung anda adalah antara", zona_target_rendah, "dan", zona_target_tinggi, "detak/menit")
print("Anda telah membakar", kalori_terbakar_total, "kalori selama latihan")
