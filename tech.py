"""
Index yang tersusun rapih

ada array yang berisi ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B'].
guru meminta agar tulisan C saja yang ditampilkan ke dalam layar.
penuhi permintaan guru tersebut.

Contoh
Input:
['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

Output:
C C
"""

tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# Menggunakan list comprehension untuk mendapatkan semua elemen 'C'
hasil = [x for x in tech if x == 'C']

# Mencetak elemen 'C' yang ditemukan
print(' '.join(hasil))
