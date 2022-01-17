# Solution 1

Dilakukan dengan cara melakukan dua kali iterasi di element tersebut. Iterasi pertama untuk mendapatkan total elemen pada array (elemen bernilai 0 tidak akan dihitung). Iterasi kedua untuk memasukkan jawaban ke array, yaitu dengan total / elemen pada index tersebut.

Bisa error jika ada 0, sehingga dipisahkan menjadi tiga kategori
- tidak ada 0 : seperti biasa
- ada 1 buah nilai 0 : index yang nilainya 0 diisi nilai total
- ada lebih dari 1 buah nilai 0 : semuanya 0.

hasil :
Runtime: 208 ms, faster than 82.63% of Python online submissions for Product of Array Except Self.
Memory Usage: 18.4 MB, less than 99.75% of Python online submissions for Product of Array Except Self.

# Solution 1_2

Rewrite di bagian looping kedua. Run time-nya jadi lebih lama.

# Solution 2

Menggunakan prefix, dan postfix. Jawaban didapatkan dengan mengalikan hasil kalia semua elemen di kiri (prefix) dan kanan (postfix) dari elemen yang dimaksud. Kita bisa menghitung prefix dan postfix tersebut dengan melakukan dua kali iterasi didalam array.