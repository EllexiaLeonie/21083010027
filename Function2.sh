#!/bin/bash
# Mendeklarasikan fungsi
function nama {
echo "Siapa namamu?"
read nama
}
function npm {
echo "Sebutkan NPM mu"
read npm
echo -e "Hai $nama dengan NPM $npm,
Selamat datang \n di praktikum Sistem Operasi yang seru ini ya!"
}
# Memanggil fungsi
nama
npm
