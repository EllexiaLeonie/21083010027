#!/bin/bash
printf "Menu Makanan Sesuai Budgetmu\n"
printf "Berapa sisa uangmu saat ini? \n"
read -p "Jumlah uangku:" x

if [[ $x -lt 5000 ]]
then
  echo "Kamu belum bisa beli makan :("
elif [[ $x -eq 10000 ]]
then
  echo "Kamu bisa beli nasi dan telur dadar."
elif [[ $x -le 20000 ]]
then
  echo "Kamu bisa beli nasi, ayam, dan sayur di warung."
elif [[ $x -ge 50000 ]]
then
  echo "Kamu bisa makan sesuka hatimu di restaurant :D"
else
  echo "Jumlah uang yang kamu miliki tidak terdeteksi oleh sistem."
fi
