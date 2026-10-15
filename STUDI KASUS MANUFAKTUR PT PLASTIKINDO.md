# Studi Kasus Manufaktur: Produksi Kotak Makan Plastik (Food Container Bento 3 Sekat 1000ml)

## PT Plastikindo Jaya Makmur — Implementasi ERPNext v15 Modul Manufacturing

---

## 1. Profil Perusahaan & Latar Belakang Industri

### 1.1 Profil Perusahaan
- **Nama Perusahaan**: PT Plastikindo Jaya Makmur
- **Bentuk Badan Usaha**: Perseroan Terbatas (Manufaktur Skala Menengah)
- **Lokasi Pabrik**: Kawasan Industri Jababeka, Cikarang, Jawa Barat
- **Bidang Usaha**: Manufaktur Produk Plastik Rumah Tangga (*Plastic Houseware Injection Molding*)
- **Kapasitas Terpasang**: 8 Unit Mesin Injection Molding (120 Ton s/d 380 Ton)
- **Produk Unggulan**: **Kotak Makan Bento 3 Sekat 1000ml (Set Lengkap)**
- **Kode Produk Jadi**: `FG-KM-01`
- **Metode Produksi**: Kombinasi *Make to Stock* (MTS) untuk katalog reguler dan *Make to Order* (MTO) untuk pesanan korporat/maklon.
- **Sistem ERP yang Digunakan**: ERPNext v15 (Modul Terintegrasi: Manufacturing, Stock, Buying, Quality, dan Accounts).

### 1.2 Karakteristik Industri Manufaktur Plastik (Injection Molding)
Industri manufaktur plastik dengan proses cetak injeksi (*injection molding*) memiliki dinamika operasional yang sangat khas:
1. **Kecepatan Siklus Produksi Tinggi (*High-Speed Cycle Time*)**: Produksi berlangsung dalam hitungan detik per cetakan (*shot*). Kehilangan waktu beberapa detik per siklus berdampak langsung pada kapasitas harian dan utilitas mesin.
2. **Sensitivitas Fluktuasi Harga Bahan Baku**: Resin polimer minyak bumi (seperti Polypropylene/PP) sangat dipengaruhi oleh harga minyak dunia dan kurs mata uang, sehingga penentuan nilai persediaan (*stock valuation*) harus presisi.
3. **Pengelolaan Limbah & Runner (*Scrap & Regrind Management*)**: Pemotongan sisa saluran lelehan plastik (*sprue* dan *runner*) menghasilkan material sisa yang harus dicatat, apakah akan digiling kembali (*regrind*) atau dialokasikan sebagai biaya pemborosan (*scrap loss*).
4. **Intensitas Konsumsi Energi Listrik**: Pemanasan barel silinder mesin (*heater band*) dan penggerak hidrolik/servo motor membutuhkan daya listrik yang besar. Biaya listrik menjadi salah satu komponen overhead utama di samping upah tenaga kerja.

### 1.3 Permasalahan Operasional Sebelum Menggunakan ERPNext
Sebelum mengadopsi ERPNext, PT Plastikindo Jaya Makmur menghadapi sejumlah kendala operasional:
- **Ketidakpastian Perhitungan HPP**: Perhitungan Biaya Pokok Produksi (HPP/COGS) dilakukan secara manual berbasis perkiraan bulanan, bukan per batch produksi riil, mengakibatkan margin laba yang meleset.
- **Kebocoran Stok Bahan Baku di Lantai Pabrik**: Perpindahan bahan baku dari gudang utama ke lantai mesin tidak tercatat secara sistematis, memicu selisih fisik yang signifikan saat *stock opname*.
- **Ketiadaan Pelacakan Jam Kerja Mesin & Operator**: Tidak ada visibilitas mengenai durasi aktual perbaikan cetakan (*downtime*), waktu siklus kerja per shift, dan efisiensi operator.
- **Kesulitan Menghubungkan Rencana Penjualan dengan Kebutuhan Material**: Pesanan penjualan sering tertunda karena kehabisan bahan penunjang kecil seperti karet seal silikon atau plastik kemasan luar.

---

## 2. Spesifikasi Teknis Produk & Desain Rekayasa

Produk yang menjadi fokus studi kasus adalah **Kotak Makan Bento 3 Sekat 1000ml (Set Lengkap)** dengan kode master item `FG-KM-01`. Produk ini dirancang untuk segmen perlengkapan bekal premium, katering, dan ritel rumah tangga yang menuntut kualitas tinggi, daya tahan panas, dan fitur anti-tumpah.

### 2.1 Rincian Dimensi & Komponen Produk

| Bagian Komponen | Kode Item ERP | Dimensi Fisik (P x L x T) | Berat Bersih | Material Utama | Spesifikasi Khusus |
|---|---|---|---|---|---|
| **Wadah Utama (Body)** | `SFG-KM-BODY` | 190 x 135 x 60 mm | 95 gram | PP Homopolymer Food Grade | 3 Kompartemen Sekat, Tahan Panas 120°C, Warna Biru Solid |
| **Tutup (Lid)** | `SFG-KM-LID` | 195 x 140 x 15 mm | 58 gram | PP Random Copolymer | Sangat Jernih (*Clarified*), Tahan Benturan, 4 Pengunci Klip |
| **Gasket Seal Silikon** | `RM-SIL-SEAL` | Keliling 620 mm, Tebal 3 mm | 8 gram | Silicone Food Grade Elastomer | Anti-Bocor (*Leak-Proof*), Removable & Washable |
| **Kemasan Primer OPP** | `RM-PLST-OPP` | 250 x 200 mm | 3 gram | Plastik OPP Adhesive Seal | Ketebalan 30 Mikron, Melindungi dari Debu & Goresan |
| **Label Branding / Sleeve** | `RM-LBL-BTO` | 500 x 70 mm | 5 gram | Art Paper 150 GSM Full-Color | Berisi Barcode EAN-13, Sertifikasi Halal, & Instruksi Pakai |
| **Karton Master Box** | `RM-BOX-CTN` | 420 x 400 x 320 mm | 650 gram | Corrugated Single Wall K125/M125/K125 | Menampung 24 Set Kotak Makan Lengkap |

### 2.2 Kepatuhan Standar Kualitas & Regulasi Makanan
Seluruh bahan baku yang digunakan dalam produk ini memenuhi standar regulasi internasional dan nasional:
- **Bebas BPA (*BPA Free*)**: Aman untuk wadah makanan bayi dan dewasa.
- **Tahan Suhu Ekstrem**: Aman untuk *Microwave Reheating* (hingga +120°C) dan penyimpanan di *Freezer* (hingga -20°C).
- **Standar BPOM & FDA 21 CFR 177.1520**: Lolos uji migrasi zat kimia berbahaya (*Overall Migration Limit* < 10 mg/dm²).
- **Uji Kedap Udara & Air (*Hermetic Seal Test*)**: Tidak mengalami kebocoran saat dibalik dengan beban air 1.000 ml selama 30 menit.

---

## 3. Struktur Produk & Formula Manufaktur (Bill of Materials)

Struktur produk dirancang dengan arsitektur **Multi-Level Bill of Materials (BOM Tree)**, yang memisahkan pembentukan sub-assembly wadah dan tutup sebelum disatukan di jalur perakitan akhir.

### 3.1 Pohon Struktur Produk (BOM Tree)

```
[FG-KM-01] Kotak Makan Bento 3 Sekat 1000ml (1 Set Lengkap)
│
├── [SFG-KM-BODY] Body Kotak Makan Bento Biru (1 Pcs)
│   ├── [RM-PP-NAT] Biji Plastik PP Homopolymer Food Grade (0.095 Kg / 95 gram)
│   └── [RM-MB-BLU] Pewarna Masterbatch Biru Food Grade (0.005 Kg / 5 gram)
│
├── [SFG-KM-LID] Tutup Kotak Makan Transparan (1 Pcs)
│   ├── [RM-PP-NAT] Biji Plastik PP Random Copolymer (0.058 Kg / 58 gram)
│   └── [RM-MB-CLR] Aditif Clarifier Transparan (0.002 Kg / 2 gram)
│
├── [RM-SIL-SEAL] Karet Seal Silikon Anti-Bocor (1 Pcs)
├── [RM-PLST-OPP] Plastik Pembungkus OPP 25x20cm (1 Pcs)
└── [RM-LBL-BTO] Paper Sleeve / Label Branding (1 Pcs)

* Kemasan Sekunder: 1 Karton Master Box [RM-BOX-CTN] menampung 24 Set Kotak Makan (0.0417 Box / Set).
```

### 3.2 Analisis Toleransi Bahan & Scrap Factor
Dalam proses injection molding, terdapat material lelehan pada saluran cetakan (*runner* dan *sprue*) serta pembersihan awal barel (*purging*). 
- **Toleransi Scrap Biji Plastik Natural (`RM-PP-NAT`)**: Ditetapkan toleransi susut / scrap sebesar 2% pada BOM.
- **Toleransi Pewarna (`RM-MB-BLU`)**: Ditetapkan 1% kelebihan dosis untuk kompensasi adhesi pada dinding hopper mesin mixing.
- **Limbah Runner**: Saluran runner dipotong di stasiun kerja `WS-ASSY-01`. Runner bersih dikumpulkan dalam kontainer terpisah untuk digiling ulang (*regrind*) menjadi produk non-food grade (misalnya pot tanaman atau hanger plastik), sehingga nilai susut material dapat diminimalkan.

---

## 4. Master Data Manufaktur pada ERPNext

### 4.1 Master Item (Bahan Baku, Komponen, dan Produk Jadi)

Tabel berikut menyajikan seluruh master data item yang telah terkonfigurasi dalam sistem ERPNext:

| Kode Item | Nama Item | Grup Item | UOM | Valuasi Satuan (IDR) | Harga Jual Standar | Default Warehouse |
|---|---|---|---|---|---|---|
| `RM-PP-NAT` | Biji Plastik PP Food Grade Natural | Raw Material | Kg | Rp 22.000 / Kg | - | `Stores - PJM` |
| `RM-MB-BLU` | Masterbatch Pewarna Biru Food Grade | Raw Material | Kg | Rp 65.000 / Kg | - | `Stores - PJM` |
| `RM-MB-CLR` | Clarifier Additive Transparan | Raw Material | Kg | Rp 85.000 / Kg | - | `Stores - PJM` |
| `RM-SIL-SEAL`| Karet Seal Silikon 1000ml | Raw Material | Nos | Rp 1.500 / Pcs | - | `Stores - PJM` |
| `RM-PLST-OPP`| Plastik Pembungkus OPP 25x20cm | Consumables | Nos | Rp 200 / Pcs | - | `Stores - PJM` |
| `RM-LBL-BTO` | Paper Sleeve Label Bento | Consumables | Nos | Rp 500 / Pcs | - | `Stores - PJM` |
| `RM-BOX-CTN` | Karton Box Master (Isi 24 Set) | Packaging Material | Nos | Rp 6.000 / Pcs | - | `Stores - PJM` |
| `SFG-KM-BODY`| Body Kotak Makan Bento Biru | Sub Assemblies | Nos | Rp 3.500 / Pcs | - | `Work In Progress - PJM`|
| `SFG-KM-LID` | Tutup Kotak Makan Transparan | Sub Assemblies | Nos | Rp 2.200 / Pcs | - | `Work In Progress - PJM`|
| `FG-KM-01`   | Kotak Makan Bento 3 Sekat 1000ml | Plastic Products | Nos | Rp 7.611 / Set | Rp 13.500 / Set | `Finished Goods - PJM` |

---

### 4.2 Stasiun Kerja (Workstation) & Analisis Biaya Operasional per Jam

Setiap mesin dan meja perakitan dihitung tarif biaya operasional per jam (*Hourly Operating Cost*) berdasarkan beban daya listrik riil, upah operator langsung, dan biaya pemeliharaan:

| Kode WS | Nama Stasiun Kerja | Kapasitas Kerja | Beban Listrik (kW) | Tarif Listrik / Jam | Upah Operator / Jam | Biaya Total / Jam |
|---|---|---|---|---|---|---|
| `WS-INJ-01` | Mesin Injection Molding 250 Ton (Body) | 1 Unit (Cetakan 4-Cavity) | 30.0 kWh | Rp 45.000 | Rp 25.000 (1 Operator) | Rp 70.000 |
| `WS-INJ-02` | Mesin Injection Molding 180 Ton (Tutup) | 1 Unit (Cetakan 4-Cavity) | 23.3 kWh | Rp 35.000 | Rp 25.000 (1 Operator) | Rp 60.000 |
| `WS-ASSY-01`| Meja Perakitan Seal Silikon & QC | 4 Operator Perakitan | 3.3 kWh | Rp 5.000 | Rp 40.000 (4 Operator) | Rp 45.000 |
| `WS-PACK-01`| Meja Finishing & Packing Master Box | 2 Operator Pengemasan | 2.0 kWh | Rp 3.000 | Rp 30.000 (2 Operator) | Rp 33.000 |

#### Catatan Perhitungan Beban Listrik:
- Tarif listrik industri PLN Golongan I-3/TM diasumsikan rata-rata Rp 1.500 per kWh.
- Mesin `WS-INJ-01` menggunakan motor servo 32 kW dan heater band 13 kW, dengan faktor daya (*duty cycle*) 65%, menghasilkan konsumsi rerata 30 kWh x Rp 1.500 = Rp 45.000 per jam.

---

### 4.3 Operasi Produksi & Alur Kerja (*Routing*: `ROUT-BENTO-01`)

Alur produksi disusun berurutan dari penyiapan bahan baku hingga barang siap masuk ke gudang produk jadi:

```
+-------------------------------------------------------------+
| Operasi 1: OP-INJ-BODY di WS-INJ-01 (Molding Wadah Body)   |
| Waktu Siklus: 25 detik/shot (4 cavity) = 0.416 menit/unit   |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Operasi 2: OP-INJ-LID di WS-INJ-02 (Molding Tutup Bening)   |
| Waktu Siklus: 20 detik/shot (4 cavity) = 0.333 menit/unit   |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Operasi 3: OP-TRIM-QC di WS-ASSY-01 (Trimming & QC Visual)  |
| Waktu Kerja: 15 detik/unit = 0.250 menit/unit               |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Operasi 4: OP-ASSY-SEAL di WS-ASSY-01 (Pasang Seal Silikon) |
| Waktu Kerja: 12 detik/unit = 0.200 menit/unit               |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Operasi 5: OP-PACKING di WS-PACK-01 (Packing OPP & Master)  |
| Waktu Kerja: 15 detik/unit = 0.250 menit/unit               |
+-------------------------------------------------------------+
```

Tabel Parameter Waktu dan Biaya per Unit pada Dokumen Routing:

| No Urut | Kode Operasi | Stasiun Kerja Terkait | Waktu per Unit (Menit) | Biaya per Menit | Biaya Operasi per Unit (IDR) |
|---|---|---|---|---|---|
| 1 | `OP-INJ-BODY` | `WS-INJ-01` | 0.416 Menit (25 detik) | Rp 1.166,67 | Rp 486,11 |
| 2 | `OP-INJ-LID` | `WS-INJ-02` | 0.333 Menit (20 detik) | Rp 1.000,00 | Rp 333,33 |
| 3 | `OP-TRIM-QC` | `WS-ASSY-01` | 0.250 Menit (15 detik) | Rp 750,00 | Rp 187,50 |
| 4 | `OP-ASSY-SEAL`| `WS-ASSY-01` | 0.200 Menit (12 detik) | Rp 750,00 | Rp 150,00 |
| 5 | `OP-PACKING` | `WS-PACK-01` | 0.250 Menit (15 detik) | Rp 550,00 | Rp 137,50 |
| **Total** | | | **1.449 Menit** | | **Rp 1.294,44** |

---

## 5. Simulasi Perhitungan Biaya Pokok Produksi (HPP / COGS Analysis)

Perhitungan Harga Pokok Produksi (*Cost of Goods Manufactured / COGM*) pada ERPNext menggabungkan nilai konsumsi bahan baku langsung (*Direct Materials*) dan biaya operasional langsung (*Direct Operational & Labor Costs*).

### 5.1 Rincian Biaya per Satuan (1 Set Kotak Makan Bento)

| Komponen Biaya | Rincian Material / Operasi | Kebutuhan per Set | Harga Satuan (IDR) | Subtotal Biaya (IDR) |
|---|---|---|---|---|
| **Bahan Baku Wadah (Body)** | Biji Plastik PP Natural (`RM-PP-NAT`) | 0.095 Kg | Rp 22.000 / Kg | Rp 2.090,00 |
| | Masterbatch Biru (`RM-MB-BLU`) | 0.005 Kg | Rp 65.000 / Kg | Rp 325,00 |
| **Bahan Baku Tutup (Lid)** | Biji Plastik PP Natural (`RM-PP-NAT`) | 0.058 Kg | Rp 22.000 / Kg | Rp 1.276,00 |
| | Clarifier Additive (`RM-MB-CLR`) | 0.002 Kg | Rp 85.000 / Kg | Rp 170,00 |
| **Bahan Penunjang & Kemasan** | Karet Seal Silikon 1000ml (`RM-SIL-SEAL`) | 1.000 Pcs | Rp 1.500 / Pcs | Rp 1.500,00 |
| | Plastik Pembungkus OPP (`RM-PLST-OPP`) | 1.000 Pcs | Rp 200 / Pcs | Rp 200,00 |
| | Paper Sleeve Label (`RM-LBL-BTO`) | 1.000 Pcs | Rp 500 / Pcs | Rp 500,00 |
| | Master Box Proporsional (`RM-BOX-CTN`) | 0.0417 Box (1/24) | Rp 6.000 / Box | Rp 250,00 |
| **Total Biaya Material Langsung** | | | | **Rp 6.311,00** |
| **Biaya Mesin & Listrik** | Injection Body (`WS-INJ-01`) | 0.416 Menit | Rp 45.000 / Jam | Rp 312,50 |
| | Injection Tutup (`WS-INJ-02`) | 0.333 Menit | Rp 35.000 / Jam | Rp 194,44 |
| **Biaya Tenaga Kerja (Labor)** | Operator Mesin Injection (Body & Tutup) | 0.749 Menit | Rp 25.000 / Jam | Rp 312,50 |
| | Operator Trimming & QC (`WS-ASSY-01`) | 0.250 Menit | Rp 40.000 / Jam | Rp 166,67 |
| | Operator Pasang Seal Silikon (`WS-ASSY-01`) | 0.200 Menit | Rp 40.000 / Jam | Rp 133,33 |
| | Operator Packing & Dus (`WS-PACK-01`) | 0.250 Menit | Rp 30.000 / Jam | Rp 125,00 |
| **Biaya Overhead Pabrik Lainnya** | Depresiasi Mold & Pemeliharaan | Estimasi per set | - | Rp 155,56 |
| **Total Biaya Konversi (Labor + Overhead)**| | | | **Rp 1.300,00** |
| **TOTAL HARGA POKOK PRODUKSI (HPP / COGM)** | **Material Langsung + Biaya Konversi** | **1 Set Lengkap** | | **Rp 7.611,00** |

---

### 5.2 Analisis Penetapan Harga Jual (*Pricing Strategy*) & Profitabilitas

Berdasarkan HPP sebesar **Rp 7.611 per set**, manajemen menetapkan struktur harga jual bertingkat untuk saluran distribusi yang berbeda:

| Saluran Distribusi | Volume Pesanan Minimal | Target Harga Jual (IDR) | Margin Laba Kotor (Gross Profit) | Persentase Margin |
|---|---|---|---|---|
| **Distributor Besar (Grosir B2B)** | Min. 5.000 Set | **Rp 11.500 / Set** | Rp 3.889 / Set | 33,8 % |
| **Agen Wilayah & Toko Grosir** | Min. 1.000 Set | **Rp 13.500 / Set** | Rp 5.889 / Set | 43,6 % |
| **Toko Ritel & E-Commerce Resmi** | Eceran (1 - 24 Set) | **Rp 18.900 / Set** | Rp 11.289 / Set | 59,7 % |

---

## 6. Skenario Eksekusi Produksi Nyata: Batch 1.000 Set

Untuk memvalidasi integrasi modul manufaktur di ERPNext v15, disimulasikan eksekusi perintah kerja (*Work Order*) riil sebanyak **1.000 Set Kotak Makan Bento 3 Sekat** untuk memenuhi pesanan distributor.

### 6.1 Tahap 1: Pengadaan & Saldo Awal Bahan Baku di Gudang
Sebelum perintah kerja dimulai, gudang bahan baku (`Stores - PJM`) harus memiliki stok bahan baku yang cukup. Transaksi penerimaan barang dicatat melalui dokumen **Stock Entry (Material Receipt)**:

| Item Code | Kuantitas Saldo Awal | Nilai Perolehan Satuan | Total Nilai Stok Awal |
|---|---|---|---|
| `RM-PP-NAT` | 500 Kg | Rp 22.000 | Rp 11.000.000 |
| `RM-MB-BLU` | 25 Kg | Rp 65.000 | Rp 1.625.000 |
| `RM-MB-CLR` | 10 Kg | Rp 85.000 | Rp 850.000 |
| `RM-SIL-SEAL`| 2.000 Nos | Rp 1.500 | Rp 3.000.000 |
| `RM-PLST-OPP`| 3.000 Nos | Rp 200 | Rp 600.000 |
| `RM-LBL-BTO` | 3.000 Nos | Rp 500 | Rp 1.500.000 |
| `RM-BOX-CTN` | 150 Nos | Rp 6.000 | Rp 900.000 |
| **Total Nilai Persediaan Bahan Baku** | | | **Rp 19.475.000** |

---

### 6.2 Tahap 2: Penerbitan Perintah Kerja (Work Order: `WO-2026-00001`)
1. Bagian PPIC (*Production Planning and Inventory Control*) membuat dokumen Work Order baru:
   - **Production Item**: `FG-KM-01`
   - **Quantity**: `1.000`
   - **BOM No**: `BOM-FG-KM-01-001`
   - **WIP Warehouse**: `Work In Progress - PJM`
   - **Target Warehouse**: `Finished Goods - PJM`
2. Sistem ERPNext secara otomatis mengalokasikan kebutuhan bahan baku:
   - `153 Kg` Biji Plastik PP Natural (95 Kg untuk Body + 58 Kg untuk Tutup)
   - `5 Kg` Pewarna Masterbatch Biru
   - `2 Kg` Clarifier Additive
   - `1.000 Pcs` Karet Seal Silikon
   - `1.000 Pcs` Plastik OPP
   - `1.000 Pcs` Label Branding
   - `42 Pcs` Karton Master Box (1.000 / 24 = 41,67 dibulatkan ke atas menjadi 42 box)
3. Work Order disetujui (*Submit*) dan berstatus **Not Started**.

---

### 6.3 Tahap 3: Pemindahan Bahan Baku (Stock Entry: Material Transfer)
1. Supervisor Gudang mengklik tombol **Create > Material Transfer** pada Work Order.
2. Seluruh bahan baku di atas dipindahkan dari gudang penyimpanan bahan mentah ke lantai produksi:
   - **Source Warehouse**: `Stores - PJM`
   - **Target Warehouse**: `Work In Progress - PJM`
3. Dokumen Stock Entry disubmit. Nilai persediaan bahan berpindah ke akun *Work In Progress* di buku besar akuntansi.

---

### 6.4 Tahap 4: Pelaksanaan Pekerjaan Lantai Pabrik (Job Cards Execution)
ERPNext menerbitkan 5 dokumen Job Card digital untuk memantau waktu kerja aktual dan efisiensi mesin:

1. **Job Card 1 (`OP-INJ-BODY` di `WS-INJ-01`)**:
   - Operator menyalakan mesin injeksi 250 Ton.
   - Timer Job Card dimulai (*Start Timer*).
   - Mesin mencetak 250 shot (cetakan 4 cavity = 1.000 wadah body).
   - Waktu siklus aktual: 25 detik per shot (Total waktu: 416 menit = ~6,9 jam kerja mesin).
   - Hasil selesai: 1.000 wadah body diterima dalam kondisi baik.
2. **Job Card 2 (`OP-INJ-LID` di `WS-INJ-02`)**:
   - Operator menyalakan mesin injeksi 180 Ton.
   - Mesin mencetak 250 shot (cetakan 4 cavity = 1.000 tutup bening).
   - Waktu siklus aktual: 20 detik per shot (Total waktu: 333 menit = ~5,5 jam kerja mesin).
   - Hasil selesai: 1.000 tutup bening siap diproses.
3. **Job Card 3 & 4 (`OP-TRIM-QC` & `OP-ASSY-SEAL` di `WS-ASSY-01`)**:
   - Operator memotong sisa sprue runner dan melakukan pemeriksaan visual.
   - Operator memasang gasket seal silikon ke dalam celah alur tutup.
   - Waktu kerja perakitan selesai tepat waktu dalam 225 menit.
4. **Job Card 5 (`OP-PACKING` di `WS-PACK-01`)**:
   - Setiap set dimasukkan ke dalam plastik OPP, dipasangi label sleeve, dan ditata rapi ke dalam 42 Master Karton Box (masing-masing 24 set, box terakhir berisi 16 set).
   - Seluruh Job Card disubmit.

---

### 6.5 Tahap 5: Penyelesaian Produksi & Penerimaan Produk Jadi (Manufacture Entry)
1. Supervisor Produksi mengklik **Create > Manufacture** pada dokumen Work Order.
2. Dokumen **Stock Entry (Manufacture)** terbit secara otomatis:
   - Memotong seluruh bahan baku di `Work In Progress - PJM`.
   - Mengakui penambahan stok sebanyak **1.000 Set `FG-KM-01`** ke dalam `Finished Goods - PJM`.
   - Mengalokasikan biaya operasional mesin dan tenaga kerja dari Job Card ke dalam nilai perolehan produk jadi.
3. Dokumen disubmit. Work Order berubah status menjadi **Completed**.

---

## 7. Integrasi Akuntansi Persediaan Perpetual & Jurnal Finansial

Salah satu keunggulan terbesar implementasi ERPNext adalah integrasi otomatis antara pergerakan fisik material di lantai pabrik dengan modul akuntansi (*General Ledger*).

### 7.1 Alur Transaksi Jurnal Akuntansi Manufaktur

```
+-------------------------------------------------------------+
| Transaksi 1: Penerimaan Bahan Baku di Gudang (Stores)       |
| Debit  : Persediaan Bahan Baku (Stock In Hand - Stores)     |
| Kredit : Utang Usaha / Kas Bank                             |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Transaksi 2: Material Transfer for Manufacture              |
| Debit  : Barang Dalam Proses (Stock In Hand - WIP)          |
| Kredit : Persediaan Bahan Baku (Stock In Hand - Stores)     |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Transaksi 3: Manufacture Entry (Produk Selesai)             |
| Debit  : Persediaan Barang Jadi (Stock In Hand - FG)        |
| Kredit : Barang Dalam Proses (Stock In Hand - WIP)          |
| Kredit : Biaya Operasi Dibebankan (Expenses in Valuation)   |
+------------------------------+------------------------------+
                               |
+------------------------------v------------------------------+
| Transaksi 4: Penjualan & Pengiriman ke Pelanggan (Delivery) |
| Debit  : Harga Pokok Penjualan (Cost of Goods Sold / COGS)  |
| Kredit : Persediaan Barang Jadi (Stock In Hand - FG)        |
| Debit  : Piutang Usaha / Kas                                |
| Kredit : Pendapatan Penjualan (Sales Revenue)               |
+-------------------------------------------------------------+
```

### 7.2 Simulasi Jurnal Finansial untuk Batch 1.000 Set Kotak Makan

| No Transaksi | Keterangan Jurnal Akuntansi | Akun Debit | Akun Kredit | Nilai (IDR) |
|---|---|---|---|---|
| **1. Transfer Bahan** | Pemindahan 153 Kg PP, Pewarna, Seal, & Kemasan ke Lantai Kerja | `Stock In Hand - WIP` | `Stock In Hand - Stores` | Rp 6.311.000 |
| **2. Alokasi Biaya Operasi** | Pengakuan Biaya Listrik Mesin & Upah Operator Lantai Kerja | `Stock In Hand - WIP` | `Expenses Included In Valuation` | Rp 1.300.000 |
| **3. Penerimaan Produk Jadi** | Penerimaan 1.000 Set FG-KM-01 ke Gudang Barang Jadi | `Stock In Hand - FG` | `Stock In Hand - WIP` | Rp 7.611.000 |
| **4. Penjualan ke Grosir** | Pengiriman 1.000 Set FG-KM-01 dengan Harga Grosir Rp 13.500 | `Cost of Goods Sold (COGS)` | `Stock In Hand - FG` | Rp 7.611.000 |
| | Pencatatan Piutang & Pendapatan Penjualan | `Accounts Receivable (Piutang)` | `Sales Revenue (Penjualan)` | Rp 13.500.000 |
| **Laba Kotor (Gross Profit)** | **Selisih Penjualan dan HPP pada Laporan Laba Rugi** | | | **Rp 5.889.000** |

---

## 8. Pengendalian Kualitas (Quality Control & Inspection)

Untuk menjaga reputasi produk di pasar, diterapkan sistem inspeksi kualitas terintegrasi di ERPNext pada tiga titik kendali kritis:

### 8.1 Titik Kendali Kualitas (Quality Inspection Gates)

```
[Bahan Baku Masuk] ──> [Gate 1: Inspeksi Resin & Seal] ──> Masuk Gudang Stores
                              │
[Proses Molding]   ──> [Gate 2: Inspeksi First-Piece & Runner] ──> Lanjut Perakitan
                              │
[Produk Jadi]      ──> [Gate 3: Inspeksi Akhir & Leak Test] ──> Masuk Finished Goods
```

### 8.2 Parameter Uji pada Quality Inspection Template (`QIT-KM-01`)

| Parameter Uji | Metode Pengujian | Standar Penerimaan (Acceptance Criteria) | Tindakan Korektif Jika Reject |
|---|---|---|---|
| **Keseragaman Berat Wadah** | Timbangan Digital Presisi 0.1g | 95.0 gram (+/- 1.5 gram) | Setel ulang holding pressure & dosing stroke pada mesin injeksi. |
| **Kejernihan Tutup Transparan** | Uji Transmisi Cahaya & Cacat Visual | Tidak ada noda gelembung (*void*), bintik hitam, atau silver streak | Tingkatkan suhu lelehan dan bersihkan hopper resin. |
| **Bebas Flash / Burrs** | Inspeksi Visual & Rabaan Tangan | Tepi wadah dan tutup halus tanpa sisa plastik tipis menonjol | Kurangi injection pressure atau periksa clamping unit mold. |
| **Uji Kedap Air (*Leakage Test*)** | Diisi 1.000 ml air, dibalik dengan beban 2 kg selama 15 menit | 100% Tidak boleh ada tetesan air merembes keluar | Periksa kelenturan dan dudukan gasket karet seal silikon. |
| **Uji Banting (*Drop Impact Test*)** | Dijatuhkan dari ketinggian 1,2 meter pada lantai beton | Wadah dan pengunci klip tidak retak/pecah | Evaluasi konsentrasi clarifier dan temperatur lelehan polimer. |

---

## 9. Indikator Kinerja Utama Manufaktur (Manufacturing KPIs)

Implementasi ERPNext memungkinkan pemantauan metrik kinerja operasional pabrik secara *real-time*:

### 9.1 Overall Equipment Effectiveness (OEE) pada Stasiun Injeksi
- **Availability Rate**: 92% (Tercapai waktu operasional 6,9 jam dari jadwal terencana 7,5 jam; 0,6 jam untuk pemanasan barel dan pergantian material).
- **Performance Rate**: 96% (Kecepatan siklus mesin mencapai rerata 26 detik dibanding target desain 25 detik).
- **Quality Rate**: 98,5% (Dari 1.000 unit cetakan, hanya terdapat 15 unit reject pada uji coba awal).
- **Skor OEE Keseluruhan**: **87,0%** (Melampaui standar manufaktur kelas dunia / *World Class Manufacturing* yang berada di ambang 85%).

### 9.2 Efisiensi Biaya Bahan Baku (*Material Yield*)
- Target Konsumsi Bahan: 153 Kg Biji Plastik.
- Konsumsi Aktual: 155 Kg (Selisih 2 Kg digunakan untuk pembersihan saluran runner dan purging awal).
- *Yield Rate*: **98,7%**. Sisa 2 Kg material runner bersih disimpan untuk proses regrind.

---

## 10. Kesimpulan & Rekomendasi Pengembangan Sistem

### 10.1 Manfaat Nyata Implementasi ERPNext bagi Perusahaan
1. **Ketepatan Kalkulasi HPP**: Perusahaan kini mengetahui secara pasti bahwa biaya produksi 1 set kotak makan bento adalah **Rp 7.611**, memberikan kepastian dalam negosiasi harga kontrak dengan distributor skala besar.
2. **Eliminasi Kehilangan Stok (*Zero Material Leakage*)**: Mekanisme *Material Transfer for Manufacture* memastikan bahwa tidak ada satu kilogram bahan baku pun yang keluar dari gudang tanpa dokumen perintah kerja yang sah.
3. **Peningkatan Produktivitas Operator**: Penerapan Job Card digital menciptakan akuntabilitas waktu kerja dan memangkas waktu tunggu (*idle time*) antar-stasiun sebesar 24%.
4. **Otomatisasi Akuntansi Finansial**: Laporan neraca dan laba-rugi persediaan terbarui secara otomatis setiap kali produk selesai dicetak dan disubmit ke gudang produk jadi.

### 10.2 Rencana Pengembangan Lanjutan (Future Enhancements)
- **Integrasi Sensor IoT pada Mesin Injeksi**: Menghubungkan PLC mesin injection langsung ke Frappe REST API untuk pencatatan otomatis jumlah shot cetakan dan alarm downtime tanpa perlu input manual operator.
- **Penerapan Barcode / QR Code Scanner**: Menempelkan label barcode pada setiap kontainer WIP untuk mempercepat proses hand-over antar stasiun kerja dengan scanner genggam.
- **Modul Pemeliharaan Cetakan (*Mold Maintenance Module*)**: Memanfaatkan fitur *Asset Maintenance* di ERPNext untuk melacak jumlah shot cetakan dan menjadwalkan pelumasan pin ejektor serta pembersihan kerak ventilasi udara secara preventif setiap 50.000 shot.

---

*Studi kasus ini disusun sebagai referensi operasional resmi modul Manufaktur ERPNext v15 untuk program akademik dan praktikum industri.*
