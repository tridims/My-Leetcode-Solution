# Solution 1

Menggunakan dictionary / hashmap data type untuk menyimpan data angka yang telah ada. 
Program akan melakukan looping pada setiap angka yang ada dan melihat apakah angka tersebut ada di hashmap/dictionary.
jika iya maka return True. Jika sampai terakhir tidak ada yang double, maka return False.

# Solution 2

Memanfaatkan tipe data list dan sets di python. sets tidak bisa menyimpan data double. List yang merupakan masukan di buat salinannya berupa sets dan panjang/jumlah elemen di dalamnya akan dibandingkan dengan list awal. Jika sama maka tidak ada elemen yang dobel.

# time complexity : O(N)
