# Two Pointer

Dilakukan dengan membuat dua pointer (left dan right untuk menandakan bahwa perbandingan hanya berjalan ke kanan/ tidak bisa menjual ke sebelumnya).

- left / kiri yaitu yang dibeli.
- right / kanan adalah yang dijual.

ketika iterasi dan bagian kanannya lebih rendah dari kiri, maka pointer kiri akan di pindah di tempat si kanan. Iterasi dilakukan sampai si pointer kanan sampai di elemen terakhir.

Time complexity O(N)
space complexity O(1)