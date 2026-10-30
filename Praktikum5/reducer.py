import sys
kunci_sekarang, total = None, 0
for baris in sys.stdin:
    kunci, nilai = baris.rstrip("\n").split("\t")
    if kunci != kunci_sekarang:
        if kunci_sekarang is not None:
            print(f"{kunci_sekarang}\t{total}")
        kunci_sekarang, total = kunci, 0
    total += int(nilai)
if kunci_sekarang is not None:
    print(f"{kunci_sekarang}\t{total}")
