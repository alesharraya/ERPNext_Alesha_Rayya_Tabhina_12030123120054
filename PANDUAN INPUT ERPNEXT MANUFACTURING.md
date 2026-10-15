# Panduan Komprehensif Input & Pengoperasian Modul Manufaktur ERPNext v15

## Studi Kasus: Produksi Kotak Makan Plastik Bento 3 Sekat 1000ml (PT Plastikindo Jaya Makmur)

---

## 1. Pendahuluan & Gambaran Umum Sistem

Panduan ini disusun sebagai pedoman operasional lengkap dan komprehensif dalam mengonfigurasi master data, merancang struktur produk (*Bill of Materials*), hingga mengeksekusi proses manufaktur pada sistem ERPNext versi 15. Studi kasus yang digunakan merepresentasikan alur nyata industri manufaktur wadah plastik (*plastic houseware injection molding*) pada **PT Plastikindo Jaya Makmur**.

### 1.1 Profil Studi Kasus
- **Perusahaan**: PT Plastikindo Jaya Makmur (PJM)
- **Bidang Usaha**: Manufaktur Plastik Rumah Tangga (*Plastic Injection Molding*)
- **Produk Unggulan**: Kotak Makan Bento 3 Sekat 1000ml (*Complete Food Container Set*)
- **Kode Produk Jadi**: `FG-KM-01`
- **Metode Manufaktur**: *Make to Stock* (MTS) & *Make to Order* (MTO)
- **Akses Sistem ERP**: `http://localhost:8080/app/manufacturing`

### 1.2 Tujuan Dokumen
Setelah mengikuti panduan ini, pengguna diharapkan mampu:
1. Mengonfigurasi fondasi sistem manufaktur: Perusahaan, Periode Fiskal, Gudang, dan Akuntansi Persediaan Perpetual.
2. Memasukkan seluruh master data manufaktur: *Item Group*, *Item Master*, *Workstation*, *Operation*, dan *Routing*.
3. Menyusun formula produksi multi-komponen (*Bill of Materials / BOM*) dengan perhitungan biaya bahan baku (*raw material cost*) dan biaya operasional mesin/tenaga kerja (*operating cost*).
4. Melakukan import data secara massal menggunakan file CSV maupun penginputan manual via formulir antarmuka web ERPNext.
5. Menjalankan siklus eksekusi produksi secara end-to-end: *Work Order*, *Material Transfer for Manufacture*, *Job Card Execution*, hingga *Manufacture Stock Entry*.
6. Melakukan inspeksi kualitas (*Quality Inspection*) dan menganalisis laporan akuntansi persediaan serta Harga Pokok Produksi (HPP/COGS).

---

## 2. Prasyarat & Konfigurasi Fondasi Sistem

Sebelum memasukkan data manufaktur, pastikan konfigurasi dasar organisasi pada ERPNext telah siap. Jika menggunakan instalasi baru, periksa elemen-elemen berikut:

### 2.1 Konfigurasi Perusahaan (*Company*)
- **Company Name**: `PT Plastikindo Jaya Makmur`
- **Abbreviation**: `PJM`
- **Default Currency**: `IDR (Indonesian Rupiah)`
- **Country**: `Indonesia`
- **Chart of Accounts**: `Standard`
- **Domain**: `Manufacturing`

### 2.2 Struktur Gudang (*Warehouse Hierarchy*)
ERPNext menggunakan model hirarki gudang bertingkat (*tree structure*). Pastikan struktur gudang di bawah `All Warehouses - PJM` telah terbentuk:

| Nama Gudang | Tipe Gudang | Fungsi Operasional | Akun Persediaan Terkait |
|---|---|---|---|
| `Stores - PJM` | Stores | Penyimpanan bahan baku biji plastik, pewarna, seal, dan bahan kemasan | `Stock In Hand - PJM` |
| `Work In Progress - PJM` | Work In Progress | Penampungan bahan yang sedang diproses di lantai kerja mesin/operator | `Stock In Hand / WIP - PJM` |
| `Finished Goods - PJM` | Finished Goods | Penyimpanan produk jadi kotak makan yang siap dijual/didistribusikan | `Stock In Hand - PJM` |

> **Catatan Akuntansi**: Pada sistem persediaan perpetual (*Perpetual Inventory*), setiap perpindahan material antar-gudang dan penyelesaian produksi akan menghasilkan jurnal akuntansi otomatis (*General Ledger Entries*) tanpa perlu penjurnalan manual di akhir bulan.

---

## 3. Arsitektur Master Data Manufaktur

Struktur data manufaktur kotak makan bento dirancang dengan spesifikasi presisi agar perhitungan kebutuhan bahan dan kalkulasi biaya operasional akurat.

### 3.1 Struktur Produk (Bill of Materials Tree)

```
[FG-KM-01] Kotak Makan Bento 3 Sekat 1000ml (1 Set)
├── [SFG-KM-BODY] Body Kotak Makan Bento Biru (1 Pcs)
│   ├── [RM-PP-NAT] Biji Plastik PP Homopolymer Food Grade (0.095 Kg / 95 gram)
│   └── [RM-MB-BLU] Pewarna Biji Plastik Biru Food Grade (0.005 Kg / 5 gram)
├── [SFG-KM-LID] Tutup Kotak Makan Transparan (1 Pcs)
│   ├── [RM-PP-NAT] Biji Plastik PP Random Copolymer (0.058 Kg / 58 gram)
│   └── [RM-MB-CLR] Aditif Clarifier Transparan (0.002 Kg / 2 gram)
├── [RM-SIL-SEAL] Karet Seal Silikon Anti-Bocor (1 Pcs)
├── [RM-PLST-OPP] Plastik Pembungkus OPP 25x20cm (1 Pcs)
└── [RM-LBL-BTO] Paper Sleeve / Label Branding (1 Pcs)

* Kemasan Sekunder: 1 Karton Master Box [RM-BOX-CTN] memuat 24 Set Kotak Makan.
```

### 3.2 Master Item & Nilai Standar Biaya

Seluruh item yang terlibat dalam proses manufaktur harus terdaftar pada modul **Stock > Item**:

| Kode Item | Nama Item | Grup Item | UOM | Biaya Standar | Maintain Stock | Tipe Item |
|---|---|---|---|---|---|---|
| `RM-PP-NAT` | Biji Plastik PP Food Grade Natural | Raw Material | Kg | Rp 22.000 / Kg | Ya | Pembelian / Raw Material |
| `RM-MB-BLU` | Masterbatch Pewarna Biru Food Grade | Raw Material | Kg | Rp 65.000 / Kg | Ya | Pembelian / Raw Material |
| `RM-MB-CLR` | Clarifier Additive Transparan | Raw Material | Kg | Rp 85.000 / Kg | Ya | Pembelian / Raw Material |
| `RM-SIL-SEAL`| Karet Seal Silikon 1000ml | Raw Material | Nos | Rp 1.500 / Pcs | Ya | Pembelian / Raw Material |
| `RM-PLST-OPP`| Plastik Pembungkus OPP 25x20cm | Consumables | Nos | Rp 200 / Pcs | Ya | Pembelian / Consumable |
| `RM-LBL-BTO` | Paper Sleeve Label Bento | Consumables | Nos | Rp 500 / Pcs | Ya | Pembelian / Consumable |
| `RM-BOX-CTN` | Karton Box Master (Isi 24 Set) | Packaging Material | Nos | Rp 6.000 / Pcs | Ya | Pembelian / Packaging |
| `SFG-KM-BODY`| Body Kotak Makan Bento Biru | Sub Assemblies | Nos | Rp 3.500 / Pcs | Ya | Manufaktur / Semi-Finished |
| `SFG-KM-LID` | Tutup Kotak Makan Transparan | Sub Assemblies | Nos | Rp 2.200 / Pcs | Ya | Manufaktur / Semi-Finished |
| `FG-KM-01`   | Kotak Makan Bento 3 Sekat 1000ml | Plastic Products | Nos | Rp 7.611 / Set | Ya | Manufaktur / Finished Good |

### 3.3 Master Workstation (Stasiun Kerja)

Stasiun kerja merepresentasikan mesin atau meja perakitan tempat operasi produksi berlangsung. Tarif biaya per jam dihitung berdasarkan tarif konsumsi daya listrik dan upah operator:

| Kode WS | Nama Stasiun Kerja | Kapasitas | Tarif Listrik / Jam | Tarif Upah / Jam | Total Tarif / Jam |
|---|---|---|---|---|---|
| `WS-INJ-01` | Mesin Injection Molding 250 Ton (Body) | 1 Unit (4 Cavity) | Rp 45.000 | Rp 25.000 | Rp 70.000 |
| `WS-INJ-02` | Mesin Injection Molding 180 Ton (Tutup) | 1 Unit (4 Cavity) | Rp 35.000 | Rp 25.000 | Rp 60.000 |
| `WS-ASSY-01`| Meja Perakitan Seal & QC Visual | 4 Operator | Rp 5.000 | Rp 40.000 | Rp 45.000 |
| `WS-PACK-01`| Meja Finishing & Packing Master Box | 2 Operator | Rp 3.000 | Rp 30.000 | Rp 33.000 |

### 3.4 Master Operation & Alur Routing (`ROUT-BENTO-01`)

Operasi produksi disusun berurutan dalam dokumen Routing untuk menentukan waktu siklus (*cycle time*) dan biaya per unit barang:

| No Urut | Kode Operasi | Deskripsi Operasi | Workstation | Waktu per Unit (Menit) | Biaya Operasi per Unit (IDR) |
|---|---|---|---|---|---|
| 1 | `OP-INJ-BODY` | Molding Body Kotak Makan (Cycle Time: 25 dtk/shot) | `WS-INJ-01` | 0.416 Menit (25 detik) | Rp 486,11 |
| 2 | `OP-INJ-LID` | Molding Tutup Transparan (Cycle Time: 20 dtk/shot) | `WS-INJ-02` | 0.333 Menit (20 detik) | Rp 333,33 |
| 3 | `OP-TRIM-QC` | Pembersihan Flash/Runner & Inspeksi Visual Cacat | `WS-ASSY-01` | 0.250 Menit (15 detik) | Rp 187,50 |
| 4 | `OP-ASSY-SEAL`| Pemasangan Karet Seal Silikon ke Alur Tutup | `WS-ASSY-01` | 0.200 Menit (12 detik) | Rp 150,00 |
| 5 | `OP-PACKING` | Pemasangan Label Sleeve, Plastik OPP & Masuk Dus | `WS-PACK-01` | 0.250 Menit (15 detik) | Rp 137,50 |
| **Total** | | **Total Waktu Operasi per Set** | | **1.449 Menit** | **Rp 1.294,44** |

---

## 4. Opsi 1: Import Data Cepat Menggunakan File CSV (Batch Import)

Fitur **Data Import** pada ERPNext memungkinkan migrasi dan penyusunan ratusan baris master data secara instan dan bebas kesalahan pengetikan manual.

### 4.1 Hierarki dan Urutan Pengunggahan File CSV
Pengunggahan harus dilakukan secara berurutan sesuai relasi ketergantungan data (*data dependency*):

```
1. Item Group ──> 2. Workstation ──> 3. Operation ──> 4. Routing
                                                          │
5. Item Master <──────────────────────────────────────────┘
       │
       ▼
6. Bill of Materials (BOM)
       │
       ▼
7. Stock Entry (Saldo Awal Gudang Stores)
```

### 4.2 Prosedur Langkah demi Langkah Melakukan Data Import di ERPNext

1. **Akses Menu Data Import**:
   - Ketik `Data Import` pada Awesome Bar (kotak pencarian atas) atau navigasikan ke **Settings > Data Import**.
   - Klik tombol biru **Add Data Import** di pojok kanan atas.

2. **Memilih DocType Target**:
   - Pada kolom **Document Type**, pilih dokumen target sesuai urutan (misalnya `Item Group`).
   - Pada kolom **Import Type**, pilih `Insert New Records`.

3. **Mengunggah File CSV**:
   - Klik tombol **Attach** pada bagian Data Import File.
   - Pilih file CSV yang sesuai dari folder `docs/csv/`.
   - ERPNext akan memetakan kolom CSV ke field DocType secara otomatis.

4. **Validasi & Eksekusi Import**:
   - Klik tombol **Save** di pojok kanan atas formulir Data Import.
   - Klik tombol **Start Import**.
   - Monitor bilah progres (*progress bar*). Jika status berubah menjadi **Success**, data telah berhasil masuk. Jika muncul pesan **Failed**, buka tabel log error untuk memeriksa field yang tidak valid.

### 4.3 Daftar Lengkap File CSV Pendukung

| No | Target DocType | Nama File CSV | Lokasi File | Deskripsi Isi Data |
|---|---|---|---|---|
| 1 | `Item Group` | `01_item_group.csv` | `docs/csv/01_item_group.csv` | 5 Grup: Raw Material, Sub Assemblies, Packaging, Consumables, Plastic Products |
| 2 | `Workstation` | `02_workstation.csv` | `docs/csv/02_workstation.csv` | 4 Stasiun kerja beserta tarif listrik, upah, dan kapasitas |
| 3 | `Operation` | `03_operation.csv` | `docs/csv/03_operation.csv` | 6 Operasi produksi dari mixing, molding, trimming, seal assy, hingga packing |
| 4 | `Routing` | `04_routing.csv` | `docs/csv/04_routing.csv` | Alur sekuensial operasi produksi beserta alokasi waktu dan biaya |
| 5 | `Item` | `05_items.csv` | `docs/csv/05_items.csv` | 10 Master item bahan baku, komponen, kemasan, dan produk jadi |
| 6 | `BOM` | `06_bom_kotak_makan.csv`| `docs/csv/06_bom_kotak_makan.csv` | Struktur formula material dan operasi untuk 1 unit FG-KM-01 |
| 7 | `Stock Entry` | `07_stock_entry_raw_material.csv` | `docs/csv/07_stock_entry_raw_material.csv` | Saldo awal persediaan bahan baku di gudang Stores - PJM |

---

## 5. Opsi 2: Panduan Manual Input Data Melalui Antarmuka ERPNext (GUI)

Bagi pengguna yang ingin mempelajari alur sistem dari awal atau menguji formulir satu per satu, berikut adalah langkah detail penginputan manual via antarmuka web.

---

### Langkah 1: Penginputan Master Item Group (`/app/item-group`)

1. Buka URL: `http://localhost:8080/app/item-group/new`
2. Masukkan data grup:
   - **Item Group Name**: `Raw Material`
   - **Parent Item Group**: `All Item Groups`
   - **Is Group**: Jangan dicentang (karena menjadi leaf node)
   - Klik **Save**.
3. Ulangi langkah di atas untuk grup lainnya:
   - `Sub Assemblies` (Parent: `All Item Groups`)
   - `Packaging Material` (Parent: `All Item Groups`)
   - `Consumables` (Parent: `All Item Groups`)
   - `Plastic Products` (Parent: `All Item Groups`)

---

### Langkah 2: Penginputan Master Item (`/app/item`)

Buka URL: `http://localhost:8080/app/item/new`

#### A. Input Produk Jadi (Finished Good: `FG-KM-01`)
1. **Item Code**: `FG-KM-01`
2. **Item Name**: `Kotak Makan Bento 3 Sekat 1000ml`
3. **Item Group**: `Plastic Products`
4. **Default Unit of Measure (UOM)**: `Nos`
5. Pada bagian **Inventory & Manufacturing**:
   - Centang `Maintain Stock`.
   - Centang `Include in Manufacturing`.
   - Centang `Allow Alternative Item` (opsional jika ada alternatif warna).
   - **Valuation Method**: `FIFO` atau `Moving Average`.
   - **Default Warehouse**: `Finished Goods - PJM`.
6. Pada bagian **Sales, Purchase & Accounting**:
   - Centang `Is Sales Item`.
   - Hapus centang `Is Purchase Item`.
   - **Standard Selling Rate**: `13500`.
7. Klik **Save**.

#### B. Input Bahan Baku Resin & Pewarna
Ulangi pembuatan untuk item bahan baku dengan rincian berikut:
- **`RM-PP-NAT`**:
  - Name: `Biji Plastik PP Food Grade Natural`
  - Group: `Raw Material` | UOM: `Kg`
  - Centang: `Maintain Stock`, `Include in Manufacturing`, `Is Purchase Item`
  - Hapus centang: `Is Sales Item`
  - Standard / Valuation Rate: `22000` | Default Warehouse: `Stores - PJM`
- **`RM-MB-BLU`**:
  - Name: `Masterbatch Pewarna Biru Food Grade`
  - Group: `Raw Material` | UOM: `Kg` | Standard Rate: `65000`
- **`RM-MB-CLR`**:
  - Name: `Clarifier Additive Transparan`
  - Group: `Raw Material` | UOM: `Kg` | Standard Rate: `85000`
- **`RM-SIL-SEAL`**:
  - Name: `Karet Seal Silikon 1000ml`
  - Group: `Raw Material` | UOM: `Nos` | Standard Rate: `1500`
- **`RM-PLST-OPP`**:
  - Name: `Plastik Pembungkus OPP 25x20cm`
  - Group: `Consumables` | UOM: `Nos` | Standard Rate: `200`
- **`RM-LBL-BTO`**:
  - Name: `Paper Sleeve Label Bento`
  - Group: `Consumables` | UOM: `Nos` | Standard Rate: `500`
- **`RM-BOX-CTN`**:
  - Name: `Karton Box Master (Isi 24 Set)`
  - Group: `Packaging Material` | UOM: `Nos` | Standard Rate: `6000`

---

### Langkah 3: Penginputan Stasiun Kerja / Workstation (`/app/workstation`)

Buka URL: `http://localhost:8080/app/workstation/new`

#### A. Stasiun Kerja Mesin Injection Body (`WS-INJ-01`)
1. **Workstation Name**: `WS-INJ-01`
2. Pada tabel **Operating Costs**:
   - **Hour Rate (Electricity)**: `45000`
   - **Hour Rate (Labour / Wages)**: `25000`
   - **Hour Rate (Rent)**: `0`
   - **Hour Rate (Consumables)**: `0`
3. Kolom **Total Operating Cost per Hour** akan terkalkulasi otomatis menjadi `Rp 70.000`.
4. **Production Capacity**: Masukkan `1`.
5. Klik **Save**.

#### B. Input Stasiun Kerja Lainnya
- **`WS-INJ-02`** (Mesin Tutup):
  - Listrik: `35000` | Upah: `25000` | Total/Jam: `Rp 60.000` | Kapasitas: `1`
- **`WS-ASSY-01`** (Meja Seal & QC):
  - Listrik: `5000` | Upah: `40000` | Total/Jam: `Rp 45.000` | Kapasitas: `4`
- **`WS-PACK-01`** (Meja Packing Dus):
  - Listrik: `3000` | Upah: `30000` | Total/Jam: `Rp 33.000` | Kapasitas: `2`

---

### Langkah 4: Penginputan Operasi Produksi / Operation (`/app/operation`)

Buka URL: `http://localhost:8080/app/operation/new`

1. Buat Operasi **`OP-INJ-BODY`**:
   - **Operation Name**: `OP-INJ-BODY`
   - **Workstation**: `WS-INJ-01`
   - **Description**: `Proses Injection Molding Wadah Body Kotak Makan Bento 3 Sekat`
   - Klik **Save**.
2. Ulangi untuk operasi lainnya:
   - `OP-INJ-LID` (Workstation: `WS-INJ-02`)
   - `OP-TRIM-QC` (Workstation: `WS-ASSY-01`)
   - `OP-ASSY-SEAL` (Workstation: `WS-ASSY-01`)
   - `OP-PACKING` (Workstation: `WS-PACK-01`)

---

### Langkah 5: Pembuatan Routing Produksi (`/app/routing`)

Routing berfungsi menghubungkan urutan operasi dengan alokasi waktu siklus per unit.
1. Buka URL: `http://localhost:8080/app/routing/new`
2. **Routing Name**: `ROUT-BENTO-01`
3. Pada tabel **Operations**, tambahkan 5 baris:
   - Baris 1: Operation `OP-INJ-BODY` | Workstation `WS-INJ-01` | Time in Mins `0.416`
   - Baris 2: Operation `OP-INJ-LID` | Workstation `WS-INJ-02` | Time in Mins `0.333`
   - Baris 3: Operation `OP-TRIM-QC` | Workstation `WS-ASSY-01` | Time in Mins `0.250`
   - Baris 4: Operation `OP-ASSY-SEAL` | Workstation `WS-ASSY-01` | Time in Mins `0.200`
   - Baris 5: Operation `OP-PACKING` | Workstation `WS-PACK-01` | Time in Mins `0.250`
4. ERPNext akan mengalikan waktu dengan tarif workstation per menit untuk mendapatkan **Operating Cost**.
5. Klik **Save**.

---

### Langkah 6: Pembuatan Bill of Materials / BOM (`/app/bom`)

BOM adalah formula inti yang merinci material, operasi, dan akumulasi estimasi biaya produksi.

1. Buka URL: `http://localhost:8080/app/bom/new`
2. Pada bagian **General Details**:
   - **Item**: Pilih `FG-KM-01` (Kotak Makan Bento 3 Sekat 1000ml)
   - **Quantity**: `1`
   - **Currency**: `IDR`
   - Centang: `With Operations`
   - Centang: `Is Active` dan `Is Default`
   - **Routing**: Pilih `ROUT-BENTO-01` (Tabel operasi akan terisi otomatis).
3. Pada tabel **Materials (Raw Materials Needed)**, masukkan baris bahan:
   - `RM-PP-NAT`: Qty `0.153` Kg | Rate `22000` | Amount `Rp 3.366`
   - `RM-MB-BLU`: Qty `0.005` Kg | Rate `65000` | Amount `Rp 325`
   - `RM-MB-CLR`: Qty `0.002` Kg | Rate `85000` | Amount `Rp 170`
   - `RM-SIL-SEAL`: Qty `1.000` Nos | Rate `1500` | Amount `Rp 1.500`
   - `RM-PLST-OPP`: Qty `1.000` Nos | Rate `200` | Amount `Rp 200`
   - `RM-LBL-BTO`: Qty `1.000` Nos | Rate `500` | Amount `Rp 500`
4. Periksa **Costing Summary**:
   - **Total Material Cost**: `Rp 6.061`
   - **Total Operating Cost**: `Rp 1.294,44`
   - **Total Cost per Unit**: `Rp 7.355,44` (~Rp 7.611 dengan alokasi dus proporsional)
5. Klik **Save**, kemudian klik **Submit**. Status dokumen berubah menjadi **Submitted**.

---

### Langkah 7: Pengisian Saldo Awal Gudang Bahan Baku (`/app/stock-entry`)

Sebelum perintah produksi dapat dijalankan, bahan baku harus tersedia di gudang `Stores - PJM`.

1. Buka URL: `http://localhost:8080/app/stock-entry/new`
2. **Stock Entry Type**: Pilih `Material Receipt`
3. **Company**: `PT Plastikindo Jaya Makmur`
4. **Default Target Warehouse**: `Stores - PJM`
5. Pada tabel **Items**, masukkan stok awal:
   - `RM-PP-NAT`: Qty `500` Kg | Rate `22000`
   - `RM-MB-BLU`: Qty `25` Kg | Rate `65000`
   - `RM-MB-CLR`: Qty `10` Kg | Rate `85000`
   - `RM-SIL-SEAL`: Qty `2000` Nos | Rate `1500`
   - `RM-PLST-OPP`: Qty `3000` Nos | Rate `200`
   - `RM-LBL-BTO`: Qty `3000` Nos | Rate `500`
   - `RM-BOX-CTN`: Qty `150` Nos | Rate `6000`
6. Klik **Save**, kemudian klik **Submit**.
7. Verifikasi stok dengan membuka **Stock > Stock Balance**. Seluruh kuantitas bahan kini tercatat di `Stores - PJM`.

---

## 6. Siklus Operasional Eksekusi Produksi (Shop Floor Execution)

Berikut adalah tahapan lengkap dalam mengeksekusi proses produksi 1.000 Set Kotak Makan Bento di lantai pabrik.

```
+-------------------------------------------------------------+
| 1. Work Order Dibuat & Disubmit                             |
|    - Target: 1.000 Set FG-KM-01                             |
|    - Sistem menghitung kebutuhan 153 Kg PP, 5 Kg Pewarna, dll.|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 2. Material Transfer for Manufacture                        |
|    - Transfer bahan dari Stores - PJM ke WIP - PJM          |
|    - Jurnal: Debit Persediaan WIP, Kredit Persediaan Stores  |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 3. Eksekusi Job Card di Masing-Masing Workstation           |
|    - WS-INJ-01: OP-INJ-BODY (Start -> Complete)             |
|    - WS-INJ-02: OP-INJ-LID (Start -> Complete)              |
|    - WS-ASSY-01: OP-TRIM-QC & OP-ASSY-SEAL                  |
|    - WS-PACK-01: OP-PACKING                                 |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 4. Penyelesaian Produksi (Stock Entry: Manufacture)         |
|    - Konsumsi aktual bahan di WIP dipotong                  |
|    - Produk Jadi FG-KM-01 masuk ke Finished Goods - PJM     |
|    - HPP Aktual terkalkulasi presisi                        |
+-------------------------------------------------------------+
```

---

### Tahap 1: Pembuatan Work Order (`/app/work-order`)

1. Buka URL: `http://localhost:8080/app/work-order/new`
2. Masukkan data:
   - **Item to Manufacture**: `FG-KM-01`
   - **BOM No**: Terpilih otomatis versi default yang aktif
   - **Quantity to Manufacture**: `1000`
   - **Source Warehouse (WIP)**: `Work In Progress - PJM`
   - **Target Warehouse (FG)**: `Finished Goods - PJM`
   - **Planned Start Date**: Masukkan tanggal hari ini
3. Periksa tabel **Required Items**. Sistem otomatis mengalikan formula BOM dengan kuantitas 1.000:
   - Biji Plastik Natural: `153 Kg`
   - Pewarna Biru: `5 Kg`
   - Clarifier: `2 Kg`
   - Seal Silikon: `1.000 Pcs`
   - Plastik OPP & Label: Masing-masing `1.000 Pcs`
4. Klik **Save**, kemudian klik **Submit**. Dokumen Work Order kini berstatus **Not Started**.

---

### Tahap 2: Pengeluaran Bahan Baku ke Lantai Produksi (Material Transfer)

1. Pada halaman dokumen Work Order yang telah disubmit, klik tombol **Create** di kanan atas, lalu pilih **Material Transfer**.
2. Halaman formulir **Stock Entry (Material Transfer for Manufacture)** akan terbuka otomatis dengan seluruh daftar item dan kuantitas yang dibutuhkan.
3. Pastikan:
   - **Source Warehouse**: `Stores - PJM`
   - **Target Warehouse**: `Work In Progress - PJM`
4. Klik **Save**, lalu klik **Submit**.
5. Bahan baku secara fisik dan sistem berpindah dari gudang penyimpanan bahan baku ke lantai produksi (WIP). Status Work Order kini berubah menjadi **In Process**.

---

### Tahap 3: Pelaksanaan & Pencatatan Job Card (`/app/job-card`)

ERPNext secara otomatis membuat **Job Card** untuk setiap operasi yang tercantum dalam Routing Work Order.

1. Buka daftar Job Card melalui link pada Work Order atau URL `http://localhost:8080/app/job-card`.
2. Untuk setiap Job Card (dimulai dari `OP-INJ-BODY` pada `WS-INJ-01`):
   - Klik dokumen Job Card.
   - Klik tombol **Start Job** saat operator mulai menyalakan mesin/bekerja.
   - Sistem mencatat waktu mulai (*Timer*).
   - Jika ada jeda istirahat, klik **Pause Job**.
   - Saat produksi selesai, klik **Complete Job**.
   - Masukkan kuantitas produk selesai (**Completed Qty**: `1000`).
   - Jika terdapat produk cacat/reject, masukkan angka pada kolom **Scrap Qty**.
   - Klik **Save** lalu **Submit**.
3. Ulangi proses ini untuk seluruh Job Card:
   - `OP-INJ-LID` pada `WS-INJ-02`
   - `OP-TRIM-QC` pada `WS-ASSY-01`
   - `OP-ASSY-SEAL` pada `WS-ASSY-01`
   - `OP-PACKING` pada `WS-PACK-01`
4. Setelah seluruh Job Card disubmit, status operasional produksi telah selesai 100%.

---

### Tahap 4: Penyelesaian Produksi & Penerimaan Produk Jadi (Manufacture Entry)

1. Kembali ke halaman dokumen Work Order utama.
2. Klik tombol **Create** di kanan atas, lalu pilih **Manufacture**.
3. Formulir **Stock Entry (Manufacture)** akan muncul:
   - Sistem akan mengkonsumsi bahan baku dari `Work In Progress - PJM`.
   - Sistem akan menambahkan kuantitas barang jadi `FG-KM-01` sebanyak `1.000 Nos` ke `Finished Goods - PJM`.
   - Biaya operasional aktual dari akumulasi waktu kerja Job Card ditambahkan ke nilai barang jadi.
4. Periksa tabel **Additional Costs** (jika ada biaya tambahan seperti lembur atau listrik ekstra).
5. Klik **Save**, lalu klik **Submit**.
6. Status Work Order otomatis berubah menjadi **Completed**!

---

## 7. Analisis Laporan, Akuntansi Persediaan & Costing

Setelah siklus manufaktur selesai, manajemen dapat memverifikasi catatan melalui laporan analitis:

### 7.1 Laporan Saldo Stok (*Stock Balance*)
- Buka **Stock > Stock Balance**.
- Filter berdasarkan Company `PT Plastikindo Jaya Makmur`.
- **Hasil**:
  - Saldo di `Stores - PJM`: Berkurang tepat sebesar bahan yang digunakan (misal: sisa PP Natural = 500 - 153 = 347 Kg).
  - Saldo di `Work In Progress - PJM`: Kembali menjadi `0` (karena seluruh bahan mentah telah dikonversi menjadi produk jadi).
  - Saldo di `Finished Goods - PJM`: Bertambah `1.000 Nos` kotak makan bento dengan nilai aset sesuai HPP.

### 7.2 Laporan Buku Besar Persediaan (*Stock Ledger*)
- Buka **Stock > Stock Ledger**.
- Laporan ini menampilkan histori kronologis setiap transaksi keluar-masuk barang lengkap dengan nomor dokumen referensi, kuantitas, nilai perolehan, dan sisa saldo.

### 7.3 Jurnal Akuntansi Otomatis (*General Ledger Entries*)
Modul Manufaktur ERPNext secara otomatis membuat entri jurnal akuntansi berikut:

1. **Saat Material Transfer**:
   - `Debit`: Persediaan Barang Dalam Proses (WIP)
   - `Kredit`: Persediaan Bahan Baku (Stores)
2. **Saat Manufacture Entry**:
   - `Debit`: Persediaan Barang Jadi (Finished Goods)
   - `Kredit`: Persediaan Barang Dalam Proses (WIP)
   - `Kredit`: Biaya Operasional / Biaya Tenaga Kerja yang Dibebankan (*Expenses Included In Valuation*)

---

## 8. Panduan Pemecahan Masalah (Troubleshooting & FAQs)

Berikut adalah panduan mengatasi kendala yang kerap terjadi pada implementasi modul manufaktur ERPNext:

| Kendala / Pesan Error | Penyebab Utama | Solusi Penanganan |
|---|---|---|
| `Insufficient Stock for Item RM-PP-NAT in Stores - PJM` | Stok bahan baku di gudang Stores kosong atau kurang dari kuantitas yang diminta. | Buat dokumen **Stock Entry (Material Receipt)** atau lakukan **Purchase Receipt** untuk menambah stok bahan sebelum transfer. |
| `Cannot Submit: No Active BOM found for Item FG-KM-01` | BOM belum dibuat, belum di-submit, atau opsi *Is Active* belum dicentang. | Buka dokumen BOM yang bersangkutan, pastikan statusnya **Submitted**, centang kotak **Is Active** dan **Is Default**, lalu simpan. |
| `Negative Stock Error during Manufacture` | Pengaturan sistem melarang stok minus, sementara bahan di gudang WIP belum ditransfer penuh. | Pastikan dokumen **Material Transfer for Manufacture** telah dibuat dan disubmit sebelum membuat dokumen **Manufacture**. |
| `Job Card cannot be submitted: Time overlaps` | Waktu kerja operator atau mesin tumpang tindih dengan pekerjaan lain. | Sesuaikan jam mulai (*From Time*) dan selesai (*To Time*) pada tabel Time Logs Job Card agar tidak bentrok. |
| `Difference Account is required for Company` | Akun selisih pembulatan/penyesuaian persediaan belum dipilih pada master Company. | Buka **Company > PT Plastikindo Jaya Makmur**, pilih akun default pada field **Stock Adjustment Account** dan **Round Off Account**. |
| *Ingin mengubah formula bahan baku pada BOM yang sudah disubmit* | BOM yang sudah berstatus Submitted tidak dapat diedit secara langsung. | Klik tombol **Cancel** pada BOM, lalu klik **Amend**, lakukan penyesuaian formula/operasi, simpan dan submit ulang sebagai revisi baru. |

---

## 9. Glosarium Istilah Manufaktur ERPNext

- **BOM (Bill of Materials)**: Daftar resep material baku, komponen, sub-assembly, serta tahapan operasi yang dibutuhkan untuk membuat satu unit produk jadi.
- **Workstation**: Lokasi fisik stasiun kerja (mesin injection, meja perakitan, line packing) yang memiliki kapasitas kerja dan tarif biaya operasional per jam tertentu.
- **Operation**: Jenis aktivitas kerja atau proses fisik yang dilakukan pada suatu workstation (contoh: mixing, molding, trimming, assembly, packaging).
- **Routing**: Rangkaian urutan sekuensial dari beberapa operasi produksi untuk menghasilkan suatu item.
- **Work Order**: Perintah kerja resmi dari manajemen produksi ke lantai pabrik untuk memproduksi sejumlah produk dalam jangka waktu tertentu.
- **Job Card**: Lembar kerja digital per stasiun kerja yang digunakan operator untuk mencatat waktu kerja aktual, jumlah output selesai, serta jumlah scrap/reject.
- **Material Transfer for Manufacture**: Dokumen pergerakan pemindahan bahan mentah dari gudang utama (*Stores*) ke area lantai kerja (*Work In Progress*).
- **Backflush**: Metode otomatisasi sistem dalam memotong stok bahan baku dan mencatat biaya produksi secara bersamaan pada saat produk jadi dilaporkan selesai.
- **HPP (Harga Pokok Produksi / COGS)**: Total akumulasi biaya bahan baku langsung, upah tenaga kerja langsung, dan overhead mesin yang melekat pada produk jadi.

---

*Dokumen ini disusun untuk modul praktikum dan referensi implementasi ERPNext Manufaktur PT Plastikindo Jaya Makmur.*
