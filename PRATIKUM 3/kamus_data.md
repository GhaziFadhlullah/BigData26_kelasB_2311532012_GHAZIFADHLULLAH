# Kamus Data — Trips Bersih NYC TLC (Januari 2023)

| Kolom | Tipe | Satuan | Sumber | Aturan Validitas | Penanganan Nilai Hilang |
|-------|------|--------|--------|-----------------|------------------------|
| tpep_pickup_datetime | datetime64[ns] | UTC | TLC Parquet | Jan 2023 | Buang baris |
| tpep_dropoff_datetime | datetime64[ns] | UTC | TLC Parquet | > pickup | Buang baris |
| passenger_count | float64 | Orang | TLC Parquet | 1–9 | Isi median per jam |
| passenger_count_hilang | int8 | 0/1 | Turunan | - | - |
| trip_distance | float64 | Mil | TLC Parquet | 0.01–100 | Buang baris |
| trip_distance_capped | float64 | Mil | Turunan (winsorize p99.5) | ≤ p99.5 | - |
| PULocationID | int64 | ID zona | TLC Parquet | 1–263 | Buang baris |
| DOLocationID | int64 | ID zona | TLC Parquet | 1–263 | Buang baris |
| payment_type | int64 | Kode | TLC Parquet | 1–6 | Biarkan |
| fare_amount | float64 | USD | TLC Parquet | ≥ 0 | Biarkan |
| tip_amount | float64 | USD | TLC Parquet | ≥ 0 | Biarkan |
| total_amount | float64 | USD | TLC Parquet | > 0 | Buang baris |
| durasi_menit | float64 | Menit | Turunan (dropoff - pickup) | 1–180 | Buang baris |
| jam | int32 | 0–23 | Turunan | - | - |
| jam_mulai | datetime64[ns] | UTC dibulatkan per jam | Turunan | - | - |
| borough_naik | object | Nama | Zona CSV (join PULocationID) | Diketahui TLC | Left join (NaN = zona tak dikenal) |
| zona_naik | object | Nama | Zona CSV | - | Left join |
| nama_pembayaran | object | Label | SQLite tarif_referensi | - | Left join |
| suhu_c | float64 | °C | Open-Meteo API | - | Left join per jam |
| hujan_mm | float64 | mm | Open-Meteo API | ≥ 0 | Left join per jam |
| tarif_ekstrem | int8 | 0/1 | Turunan (IQR total_amount) | - | - |
| hari_minggu | int32 | 0=Sen, 6=Min | Turunan | - | - |
| akhir_pekan | int8 | 0/1 | Turunan | - | - |
| kecepatan_mph | float64 | Mil/jam | Turunan | - | Biarkan (inf kalau durasi=0, tapi sudah dibuang) |
| tarif_per_mil | float64 | USD/mil | Turunan | - | Biarkan |
| hujan | int8 | 0/1 | Turunan (hujan_mm > 0.1) | - | Isi 0 bila NaN |
| tanggal | datetime64[ns] | Hari | Turunan | - | - |
| adalah_libur | int8 | 0/1 | Nager.Date API (Tugas 3) | - | 0 bila tidak libur |
