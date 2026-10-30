import sys, re
for baris in sys.stdin:
    kategori, judul = baris.rstrip("\n").split("\t", 1)
    for kata in re.findall(r"[a-z]+", judul.lower()):
        print(f"{kata}\t1")
