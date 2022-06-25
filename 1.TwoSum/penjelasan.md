# Brute Force

Dilakukan dengan melakukan iterasi pada setiap pasangan elemen yang mungkin pada array masukan.

Time Complexity : O(N^2)

# One Pass (menggunakan hashmap)

Hanya melakukan satu kali iterasi di array yang ada. Hashmap akan menyimpan pasangan elemen yaitu angka (key), dan index angka tersebut (value).

Setiap elemen akan dicek angka yang kurang berapa, misalkan angka tujuan 10, dan elemen yang sedang di cek adalah 6, berarti angka yang kurang adalah 4 (10 - 6). Angka yang kurang akan di cek apakah ada di hashmap, jika tidak maka masukkan elemen tersebut ke hasmap, lakukan untuk semua elemen.
