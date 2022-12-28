#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime, timedelta

def program():
    kota_awal = []
    kota_akhir = []
    geolocator = Nominatim(user_agent="cari jarak")
    #kota berangkat
    print('\033[93m')
    kota1 = str(input("Dari kota mana Anda berangkat? "))
    location1 = geolocator.geocode(kota1)
    print('\033[96m'+ "Lokasi yang terdeteksi: ", location1.address + '\033[93m')
    print(" ")
    letak1 = location1.latitude, location1.longitude
    kota_awal.append(letak1)
    #kota tujuan
    kota2 = str(input("Kota mana yang akan Anda tuju? "))
    location2 = geolocator.geocode(kota2)
    print('\033[96m'+ "Lokasi yang terdeteksi: ",location2.address)
    letak2 = location2.latitude, location2.longitude
    kota_akhir.append(letak2)
    print(" ")
    #jarak
    jarak = geodesic(kota_awal, kota_akhir).miles
    print('\033[93m'+"Jarak perjalanan Anda ", jarak, "kilometer.")
    print(" ")
    #kecepatan
    cepat = int(input("Berapa kecepatan rata-rata (km/jam) menyetir Anda? "))
    print(" ")  
    print(" ")  

    waktu_tempuh = (jarak/cepat)*3600
    #konversi waktu dari detik
    jam = int(waktu_tempuh//3600)
    menit = int(waktu_tempuh%3600//60)
    detik = int(waktu_tempuh%60)
    waktu_saat_ini = datetime.now().strftime("%I:%M:%S %p")
    estimasi = datetime.now() + timedelta(seconds=waktu_tempuh)
    estimasi = estimasi.strftime("%I:%M:%S %p")

    print('\033[0m'+("="*80))
    print((" "*30),'\033[92m'+ "Hasil Perhitungan"+'\033[0m')
    print("="*80)
    print(" ")
    print(f"Anda akan membutuhkan waktu {jam:02}:{menit:02}:{detik:02} untuk tiba di tujuan.")
    print(f"Saat ini pukul {waktu_saat_ini}.") 
    print(f"Jika Anda berangkat sekarang, Anda akan tiba di sana sekitar pukul {estimasi}")

#header
print("="*80)
print((" "*25),'\033[1m'+ '\033[92m' + "Estimasi Waktu Perjalanan")
print((" "*28),'\033[92m' + "by: Ellexia Leonie"+'\033[0m')
print("="*80)
print(" ")

print((" "*12),'\033[95m'+"Selamat datang di program Estimasi Waktu Perjalanan!")
print(" ")
print((" "*28), "Tentang program ini: "+'\033[0m')
print('\033[91m'+"Program ini dapat menentukan secara otomatis jarak perjalanan yang akan Anda tuju.")
print("Anda cukup memasukkan nama kota Anda akan berangkat, dan nama kota tujuan Anda.")
print("Kemudian, masukkan kecepatan rata-rata (km/jam) menyetir Anda.")
print("Maka program akan secara otomatis menghitung perkiraan waktu perjalanan Anda.")
print('\033[1m'+"Notes: Lokasi terdekat merupakan deteksi lokasi terdekat dari nama kota yang Anda masukkan."+'\033[95m')
print(" ")

start = str(input("Apakah Anda ingin mencoba program ini? (Ya/Tidak) "))
if start == "Ya":
    print(" ")
    print(" ")
    print('\033[0m'+("="*80))
    print((" "*35),'\033[1m'+ '\033[92m' + "MULAI"+'\033[0m')
    print("="*80)
    print(" ")
    print('\033[95m'+"Silahkan masukkan:")
    print("nama kota anda berangkat, nama kota tujuan, dan kecepatan Anda menyetir.")
    print(" ")
    program()
else:
    start = "Tidak"
    print("Saya tunggu percobaan Anda pada program ini!")

