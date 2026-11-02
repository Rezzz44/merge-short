"""
Project Merge Sort (Python)

Cara pakai:
    python merge_sort.py                 # mode interaktif
    python merge_sort.py 5 2 9 1 7       # urutkan angka dari argumen
    python merge_sort.py --test          # jalankan unit test
"""

import random
import sys
import unittest


def merge(kiri, kanan):
    """Gabungkan dua list yang sudah terurut menjadi satu list terurut."""
    hasil = []
    i = j = 0

    while i < len(kiri) and j < len(kanan):
        # <= menjaga stabilitas (elemen sama tetap urut aslinya)
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil


def merge_sort(data):
    """Urutkan list secara ascending dengan algoritma merge sort.

    Kompleksitas waktu : O(n log n)
    Kompleksitas ruang : O(n)
    """
    if len(data) <= 1:
        return list(data)

    tengah = len(data) // 2
    kiri = merge_sort(data[:tengah])
    kanan = merge_sort(data[tengah:])
    return merge(kiri, kanan)


# ---------------------------------------------------------------- Unit test
class TestMergeSort(unittest.TestCase):
    def test_kosong(self):
        self.assertEqual(merge_sort([]), [])

    def test_satu_elemen(self):
        self.assertEqual(merge_sort([42]), [42])

    def test_sudah_terurut(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_terbalik(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplikat(self):
        self.assertEqual(merge_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_negatif(self):
        self.assertEqual(merge_sort([0, -5, 3, -1]), [-5, -1, 0, 3])

    def test_acak_sama_dengan_sorted(self):
        for _ in range(100):
            data = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            self.assertEqual(merge_sort(data), sorted(data))

    def test_input_tidak_berubah(self):
        asli = [3, 1, 2]
        merge_sort(asli)
        self.assertEqual(asli, [3, 1, 2])


# --------------------------------------------------------------------- Main
def main():
    args = sys.argv[1:]

    if args and args[0] == "--test":
        unittest.main(argv=[sys.argv[0]], verbosity=2)
        return

    if args:
        data = [float(x) if "." in x else int(x) for x in args]
    else:
        teks = input("Masukkan angka (pisahkan dengan spasi): ")
        data = [float(x) if "." in x else int(x) for x in teks.split()]

    print("Sebelum :", data)
    print("Sesudah :", merge_sort(data))


if __name__ == "__main__":
    main()
