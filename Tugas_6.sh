#!/bin/bash

#Membuat input jumlah semester yang telah diselesaikan
echo -n "Sudah berapa semester yang anda selesaikan? "
read sem

declare -a Nilai_IPS

i=0
let banyak=$sem-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  printf "Nilai Semester %.1i: " $angka;
  read nilai_sem;
  Nilai_IPS[$i]=$nilai_sem;
  let jumlah=jumlah+$nilai_sem;
  let i=$i+1;
done

let Nilai_IPK=$jumlah/$sem
echo "Nilai IPS: " $jumlah "/" $sem
echo "Nilai IPK: " $Nilai_IPK




