from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

#Inisialisasi fungsi
def cetak(i):
    if (i+1)%2==0:
      print(i+1, "Genap - ID proses", getpid())
    else:
      print(i+1,"Ganjil - ID proses", getpid())
    sleep(1)

a=int(input("Masukkan batas perulangan: "))

#Pemrosesan sekuensial
print("Sekuensial")
# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
sekuensial_awal = time()
# PROSES BERLANGSUNG
for i in range(a):
    cetak(i)
# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
sekuensial_akhir = time()

#Multiprocessing dengan kelas Process
print("multiprocessing.Process")
# UNTUK MENAMPUNG PROSES-PROSES
kumpulan_proses = []
# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
process_awal = time()
# PROSES BERLANGSUNG
for i in range(a):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
# UNTUK MENGGABUNGKAN PROSES-PROSES AGAR TIDAK LONCAT KE PROSES SEBELUM'NYA
for i in kumpulan_proses:
    p.join()
# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
process_akhir = time()

#Multiprocessing dengan kelas Pool
print("multiprocessing.Pool")
# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_awal = time()
# PROSES BERLANGSUNG
pool = Pool()
pool.map(cetak, range(0,a))
pool.close()
# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_akhir = time()

#Bandingkan Waktu Eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
