#!/bin/bash

echo -n "Masukkan angka ganjil: ";
read angka

while [ $angka -gt 0 ]
do
  echo $angka
  angka=$((angka - 2))
done
