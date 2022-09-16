#!/bin/bash

printf "Menu Makanan Sesuai Budgetmu\n"
printf "Berapa sisa uangmu saat ini? \n"
read uang

if [$uang <  5000]
then
  echo "Kamu belum bisa beli makan :("
elif [uang >= 5000 && uang <= 10000]
then
  echo "Kamu bisa beli nasi dan telur dadar."
elif [uang >=10000 && uang <= 20000]
then
  echo "Kamu bisa beli nasi, ayam, dan sayur di warung."
else
  echo "Kamu bisa makan sesuka hatimu di restaurant :D"
f
