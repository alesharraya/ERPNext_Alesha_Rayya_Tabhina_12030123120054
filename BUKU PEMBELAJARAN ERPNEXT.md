# BUKU AJAR & PANDUAN PRAKTIKUM ERPNEXT V15

## IMPLEMENTASI ENTERPRISE RESOURCE PLANNING MANUFAKTUR BERBASIS DOCKER DESKTOP, ANTIGRAVITY IDE, DAN NOTEBOOKLM

### *Studi Kasus Transaksional Industri Injection Molding Plastik:
PT Plastikindo Jaya Makmur (Kotak Makan Bento 3 Sekat 1000ml)*

---

**Oleh Tim Penyusun:**

- **Alesha Rayya Tabhina**
- **Dr. Totok Dewayanto, S.E., M.Si., Akt. DEPARTEMEN AKUNTANSI FAKULTAS EKONOMIKA DAN BISNIS UNIVERSITAS DIPONEGORO SEMARANG 2026**

---


# KATA PENGANTAR

Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas rahmat dan karunia-Nya, sehingga Buku Panduan Praktikum & Buku Ajar ERPNext ini dapat diselesaikan dengan baik. Buku ini disusun khusus sebagai instrumen pembelajaran komprehensif bagi mahasiswa, dosen, serta praktisi Sistem Informasi Akuntansi (SIA) dan Manajemen Operasional Manufaktur.

Dalam era transformasi digital 4.0, penguasaan Enterprise Resource Planning (ERP) tidak lagi sebatas pemahaman teoritis mengenai fungsi-fungsi organisasi terisolasi, melainkan membutuhkan kompetensi eksekusi praktis pada platform terintegrasi. ERPNext sebagai salah satu solusi open-source monolithic terdepan dunia menawarkan fleksibilitas arsitektur yang sangat tinggi, memungkinkan penggabungan modul Akuntansi, Persediaan, Manufaktur, Pengadaan, dan Penjualan secara real-time.

Buku ini menyajikan pendekatan integratif unik yang memadukan empat pilar teknologi modern: (1) ERPNext v15 sebagai mesin sistem informasi enterprise, (2) Docker Desktop dan Subsystem WSL2 sebagai lingkungan kontainerisasi yang terisolasi dan mudah di-deploy, (3) AI Agent Antigravity IDE sebagai asisten pengkodean otomatis yang menjamin presisi konfigurasi, dan (4) Google NotebookLM sebagai Knowledge Management System (KMS) interaktif untuk memvalidasi setiap transaksi.

Studi kasus utama yang diangkat adalah PT Plastikindo Jaya Makmur, sebuah entitas manufaktur skala menengah yang memproduksi Kotak Makan Bento 3 Sekat 1000ml (FG-KM-01). Melalui skenario ini, pembaca dibimbing langkah-demi-langkah mulai dari penyiapan master data, pembentukan Multi-Level Bill of Materials (BOM), alokasi biaya konversi stasiun kerja injection molding, eksekusi Work Order dan Job Cards, hingga pencatatan pembukuan akuntansi perpetual (GLE & SLE) dan penyusunan laporan keuangan otomatis.

Ucapan terima kasih dan apresiasi setinggi-tingginya kami sampaikan kepada Departemen Akuntansi Fakultas Ekonomika dan Bisnis Universitas Diponegoro yang telah mendukung pengembangan bahan ajar berbasis teknologi digital ini. Semoga buku ini dapat memberikan kontribusi signifikan dalam mencetak lulusan akuntansi dan manajemen yang adaptif, kompeten, dan siap menghadapi tantangan industri global.

Semarang, Oktober 2026

Tim Penyusun:
Alesha Rayya Tabhina
Dr. Totok Dewayanto, S.E., M.Si., Akt.


# DAFTAR ISI

- [KATA PENGANTAR](#kata-pengantar)
- [BAB I: PENGENALAN ERPNEXT, FRAPPE FRAMEWORK, DAN EKOSISTEM TEKNOLOGI MODERN](#bab-i-pengenalan-erpnext-frappe-framework-dan-ekosistem-teknologi-modern)
  - [1.1 Pengertian dan Konsep Dasar Enterprise Resource Planning (ERP)](#11-pengertian-dan-konsep-dasar-enterprise-resource-planning-erp)
  - [1.2 Arsitektur Frappe Framework: Monolithic, DocType, ORM, dan Database Engine](#12-arsitektur-frappe-framework-monolithic-doctype-orm-dan-database-engine)
  - [1.3 Peran Docker Desktop dan Subsystem WSL2 dalam Lingkungan Pengembangan Terisolasi](#13-peran-docker-desktop-dan-subsystem-wsl2-dalam-lingkungan-pengembangan-terisolasi)
  - [1.4 AI Agent Antigravity IDE dan Otorisasi Strict Approval Prompting](#14-ai-agent-antigravity-ide-dan-otorisasi-strict-approval-prompting)
  - [1.5 NotebookLM sebagai Knowledge Management System (KMS) Praktikum](#15-notebooklm-sebagai-knowledge-management-system-kms-praktikum)
  - [1.6 Capaian Pembelajaran Praktikum (Learning Outcomes)](#16-capaian-pembelajaran-praktikum-learning-outcomes)
- [BAB II: PANDUAN INSTALASI, DEPLOYMENT ENVIRONMENT, DAN LANGKAH OPERASIONAL](#bab-ii-panduan-instalasi-deployment-environment-dan-langkah-operasional)
  - [2.1 Persyaratan Sistem dan Penyiapan Docker Desktop & WSL2](#21-persyaratan-sistem-dan-penyiapan-docker-desktop--wsl2)
  - [2.2 Inisiasi Kontainer ERPNext v15 dan Akses Port 8080](#22-inisiasi-kontainer-erpnext-v15-dan-akses-port-8080)
  - [2.3 Konfigurasi Initial Setup Wizard (Perusahaan, Mata Uang, & COA)](#23-konfigurasi-initial-setup-wizard-perusahaan-mata-uang--coa)
  - [2.4 Generasi Dataset ERP_Plastikindo dan Otomasi Skrip](#24-generasi-dataset-erp_plastikindo-dan-otomasi-skrip)
  - [2.5 Navigasi Antarmuka GUI Desk ERPNext](#25-navigasi-antarmuka-gui-desk-erpnext)
- [BAB III: EKSPLORASI MODUL UTAMA ERPNEXT UNTUK PEMBELAJARAN MANUFAKTUR](#bab-iii-eksplorasi-modul-utama-erpnext-untuk-pembelajaran-manufaktur)
  - [3.1 Modul Persediaan & Gudang (Stock & Inventory Management)](#31-modul-persediaan--gudang-stock--inventory-management)
  - [3.2 Modul Manufaktur & Perencanaan Kebutuhan Bahan (MRP)](#32-modul-manufaktur--perencanaan-kebutuhan-bahan-mrp)
  - [3.3 Modul Pengadaan (Buying) & Penjualan (Selling)](#33-modul-pengadaan-buying--penjualan-selling)
  - [3.4 Modul Akuntansi Keuangan (Financial Accounting)](#34-modul-akuntansi-keuangan-financial-accounting)
  - [3.5 Pembaruan dan Fitur Unggulan ERPNext Version 16](#35-pembaruan-dan-fitur-unggulan-erpnext-version-16)
- [BAB IV: KASUS PRAKTIKUM INDUSTRI MANUFAKTUR PT PLASTIKINDO JAYA MAKMUR](#bab-iv-kasus-praktikum-industri-manufaktur-pt-plastikindo-jaya-makmur)
  - [4.1 Profil Perusahaan dan Spesifikasi Produk (FG-KM-01)](#41-profil-perusahaan-dan-spesifikasi-produk-fg-km-01)
  - [4.2 Struktur Master Data (Item, Workstation, Routing)](#42-struktur-master-data-item-workstation-routing)
  - [4.3 Kasus 1: Saldo Awal Persediaan Bahan Baku & Pengadaan (Opening Stock)](#43-kasus-1-saldo-awal-persediaan-bahan-baku--pengadaan-opening-stock)
  - [4.4 Kasus 2: Perumusan Multi-Level Bill of Materials (BOM Costing)](#44-kasus-2-perumusan-multi-level-bill-of-materials-bom-costing)
  - [4.5 Kasus 3: Eksekusi Produksi Pabrik (Work Order, WIP Transfer, Job Cards, & Manufacture Entry)](#45-kasus-3-eksekusi-produksi-pabrik-work-order-wip-transfer-job-cards--manufacture-entry)
  - [4.6 Kasus 4: Siklus Penjualan Grosir dan Pengiriman (Sales Order, Delivery Note, & Sales Invoice)](#46-kasus-4-siklus-penjualan-grosir-dan-pengiriman-sales-order-delivery-note--sales-invoice)
  - [4.7 Kasus 5: Analisis Laporan Keuangan, Cost of Goods Manufactured (COGM), dan Laba Kotor](#47-kasus-5-analisis-laporan-keuangan-cost-of-goods-manufactured-cogm-dan-laba-kotor)
- [BAB V: MASTER BAGAN AKUN (CHART OF ACCOUNTS) DAN MEKANISME AKUNTANSI PERPETUAL](#bab-v-master-bagan-akun-chart-of-accounts-dan-mekanisme-akuntansi-perpetual)
  - [5.1 Struktur Kode Akun Manufaktur Indonesia (COA 1000–6000)](#51-struktur-kode-akun-manufaktur-indonesia-coa-10006000)
  - [5.2 Matriks Alur Jurnal Otomatis (General Ledger Entry & Stock Ledger Entry)](#52-matriks-alur-jurnal-otomatis-general-ledger-entry--stock-ledger-entry)
  - [5.3 Integritas Stok dan Keuangan (Stock Reconciliation & Valuation Ledger)](#53-integritas-stok-dan-keuangan-stock-reconciliation--valuation-ledger)
- [BAB VI: LATIHAN SOAL AKADEMIS DAN PENYELESAIAN ANALITIS](#bab-vi-latihan-soal-akademis-dan-penyelesaian-analitis)
  - [6.1 Soal 1: Valuasi Persediaan Awal dan Jurnal Modal](#61-soal-1-valuasi-persediaan-awal-dan-jurnal-modal)
  - [6.2 Soal 2: Perhitungan HPP Standar BOM Multi-Level](#62-soal-2-perhitungan-hpp-standar-bom-multi-level)
  - [6.3 Soal 3: Pencatatan Jurnal Pembelian Bahan Baku dan Utang Usaha](#63-soal-3-pencatatan-jurnal-pembelian-bahan-baku-dan-utang-usaha)
  - [6.4 Soal 4: Pencatatan Jurnal Alokasi Biaya Produksi dan HPP Realisasi (Work Order)](#64-soal-4-pencatatan-jurnal-alokasi-biaya-produksi-dan-hpp-realisasi-work-order)
  - [6.5 Soal 5: Analisis Penjualan, HPP, Laba Kotor, dan Margin Profitabilitas](#65-soal-5-analisis-penjualan-hpp-laba-kotor-dan-margin-profitabilitas)
  - [6.6 Panduan Penilaian dan Rubrik Evaluasi Akademis](#66-panduan-penilaian-dan-rubrik-evaluasi-akademis)
- [BAB VII: EVALUASI KONTRASTIF, TANTANGAN IMPLEMENTASI, DAN TROUBLESHOOTING](#bab-vii-evaluasi-kontrastif-tantangan-implementasi-dan-troubleshooting)
  - [7.1 Kelebihan dan Kekurangan ERPNext dalam Pembelajaran PT](#71-kelebihan-dan-kekurangan-erpnext-dalam-pembelajaran-pt)
  - [7.2 Analisis Kebijakan Pengadaan: Open-Source vs Proprietary ERP](#72-analisis-kebijakan-pengadaan-open-source-vs-proprietary-erp)
  - [7.3 Panduan Pemecahan Masalah Sistem (Troubleshooting Common Student Errors)](#73-panduan-pemecahan-masalah-sistem-troubleshooting-common-student-errors)
- [BAB VIII: KESIMPULAN, SOP OPERASIONAL, DAN CHECKLIST MANDIRI](#bab-viii-kesimpulan-sop-operasional-dan-checklist-mandiri)
  - [8.1 Kesimpulan Integrasi Empat Teknologi](#81-kesimpulan-integrasi-empat-teknologi)
  - [8.2 Standard Operating Procedure (SOP 9 Tahapan Baku Praktikum)](#82-standard-operating-procedure-sop-9-tahapan-baku-praktikum)
  - [8.3 Lembar Kontrol dan Checklist Evaluasi Mandiri Mahasiswa](#83-lembar-kontrol-dan-checklist-evaluasi-mandiri-mahasiswa)


# BAB I: PENGENALAN ERPNEXT, FRAPPE FRAMEWORK, DAN EKOSISTEM TEKNOLOGI MODERN


## 1.1 Pengertian dan Konsep Dasar Enterprise Resource Planning (ERP)

Enterprise Resource Planning (ERP) adalah sistem informasi terintegrasi yang dirancang untuk mengelola dan mengordinasikan seluruh sumber daya, informasi, dan proses bisnis utama dalam suatu organisasi. Berbeda dengan pendekatan tradisional yang mengandalkan sistem terpisah (siloed systems) untuk setiap departemen, ERP menyediakan satu basis data terpusat (centralized single source of truth). Hal ini memastikan bahwa data yang diinput oleh bagian pengadaan (buying) secara otomatis dan real-time memperbarui catatan akun utang (accounting) dan saldo stok gudang (inventory).

Dalam lingkungan manufaktur, ERP memainkan peran vital sebagai penggerak utama Perencanaan Kebutuhan Bahan (Material Requirements Planning / MRP). MRP memungkinkan pabrik mengalkulasi secara presisi kapan bahan baku harus dipesan, berapa jumlah yang dibutuhkan berdasarkan jadwal produksi, dan bagaimana kapasitas mesin atau stasiun kerja dialokasikan untuk meminimalkan waktu menganggur (idle time) dan penumpukan barang dalam proses (Work in Progress / WIP).


## 1.2 Arsitektur Frappe Framework: Monolithic, DocType, ORM, dan Database Engine

ERPNext dibangun di atas Frappe Framework, sebuah kerangka kerja aplikasi web berarsitektur monolithic penuh (full-stack open-source framework) yang menggunakan bahasa pemrograman Python di sisi server dan JavaScript/Vue.js di sisi klien. Arsitektur Frappe sangat unik dan efisien karena mengusung konsep 'Metadata-Driven Architecture', di mana setiap struktur data, antarmuka pengguna, dan aturan bisnis didefinisikan melalui satu entitas dasar yang disebut DocType (Document Type).

- **a. DocType Meta-Model**: Seluruh tabel dalam basis data MariaDB/PostgreSQL dihasilkan secara otomatis dari definisi DocType. DocType mengatur atribut bidang (fields), tipe data, relasi antar-tabel (Link Fields), serta aturan hak akses pengguna (Role Permission Manager).
- **b. Submittable DocType**: Frappe membedakan entitas draft dengan entitas resmi yang telah diposting. Dokumen bersifal Submittable memiliki siklus hidup dua tahap (Draft -> Submitted -> Cancelled). Tahap Submit memicu transaksi akuntansi dan pergerakan stok yang tidak dapat diubah secara langsung (immutable ledger record).
- **c. Object-Relational Mapping (ORM) & Redis Caching**: Frappe menggunakan ORM internal yang mengubah perintah Python menjadi query SQL teroptimasi. Kinerja transaksi didukung oleh Redis untuk mengelola caching sesi, antrean pekerjaan latar belakang (Celery/RQ workers), dan pub/sub real-time.

## 1.3 Peran Docker Desktop dan Subsystem WSL2 dalam Lingkungan Pengembangan Terisolasi

Instalasi aplikasi enterprise skala besar pada sistem operasi lokal sering kali menghadapi kendala dependensi pustaka yang rumit dan ketidakcocokan lingkungan (environment mismatch). Untuk mengatasi hal tersebut, praktikum ini memanfaatkan kontainerisasi berbasis Docker Desktop yang berjalan di atas Windows Subsystem for Linux 2 (WSL2).

Docker memungkinkan seluruh komponen ERPNext—termasuk web server Nginx, Python WSGI Gunicorn, MariaDB database, Redis cache, dan socket.io—dikemas dalam satu paket kontainer terisolasi. Hal ini menjamin bahwa sistem praktikum berjalan dengan performa seragam di seluruh komputer mahasiswa tanpa mengganggu konfigurasi sistem operasi induk.


## 1.4 AI Agent Antigravity IDE dan Otorisasi Strict Approval Prompting

Antigravity IDE adalah lingkungan pengembangan tingkat lanjut yang dilengkapi dengan AI Agent otonom. Dalam ekosistem praktikum ERPNext, Antigravity IDE bertindak sebagai asisten eksekusi teknis yang mampu menjalankan perintah penyiapan skrip Python, menggenerasi master data CSV, dan mengonfigurasi skrip kustom (Client Scripts) secara otomatis.

Untuk menjaga keamanan dan integritas pembelajaran, Antigravity IDE menerapkan mekanisme Strict Approval Prompting. Setiap tindakan destruktif atau perubahan konfigurasi sistem tingkat tinggi memerlukan persetujuan eksplisit dari mahasiswa/pengguna. Hal ini melatih mahasiswa untuk bersikap kritis dan memahami konsekuensi dari setiap perintah eksekusi sistem.


## 1.5 NotebookLM sebagai Knowledge Management System (KMS) Praktikum

Google NotebookLM difungsikan sebagai Knowledge Management System (KMS) berbasis kecerdasan buatan (Grounded AI). Seluruh buku panduan, modul praktikum, studi kasus, dan dokumen aturan akuntansi diunggah ke dalam NotebookLM. Mahasiswa dapat melakukan interogasi data, meminta penjelasan konsep jurnal yang rumit, atau mengonfirmasi langkah operasional yang ambigu secara langsung, di mana jawaban yang diberikan dijamin 100% berbasis pada dokumen rujukan yang sah (source-grounded response).


## 1.6 Capaian Pembelajaran Praktikum (Learning Outcomes)

Setelah menyelesaikan seluruh rangkaian materi dan modul praktikum dalam buku ajar ini, mahasiswa diharapkan mampu mencapai kompetensi utama berikut:

- **1.** Menganalisis dan mengonfigurasi arsitektur ERPNext mencakup integrasi modul Akuntansi, Persediaan, Pengadaan, Manufaktur, dan Penjualan.
- **2.** Merumuskan Multi-Level Bill of Materials (BOM) dan menyusun alokasi biaya konversi stasiun kerja industri injection molding plastik.
- **3.** Paham dan terampil mengeksekusi siklus manufaktur end-to-end mulai dari Work Order, Material Transfer for Manufacture, Job Cards, hingga Manufacture Stock Entry.
- **4.** Menganalisis dampak setiap transaksi bisnis terhadap pembukuan akuntansi perpetual (General Ledger Entry & Stock Ledger Entry) secara presisi.
- **5.** Mengevaluasi Laporan Harga Pokok Produksi (COGM), Laporan Laba Rugi, dan Rasio Profitabilitas Perusahaan Manufaktur.

> **📌 SINOPSIS BAB I: Pemahaman mengenai integrasi modul merupakan kunci utama penguasaan ERP. Dalam ERPNext, tidak ada transaksi persediaan yang terisolasi dari akuntansi. Setiap pergerakan barang fisik secara otomatis menerbitkan Stock Ledger Entry (SLE) dan General Ledger Entry (GLE) bersangkutan.**


# BAB II: PANDUAN INSTALASI, DEPLOYMENT ENVIRONMENT, DAN LANGKAH OPERASIONAL


## 2.1 Persyaratan Sistem dan Penyiapan Docker Desktop & WSL2

Sebelum memulai instalasi ERPNext v15, pastikan perangkat komputer memenuhi spesifikasi minimum berikut: Prosesor Intel Core i5/AMD Ryzen 5 (4 Cores/8 Threads), RAM 8 GB (direkomendasikan 16 GB), dan ruang penyimpanan kosong SSD minimal 20 GB. Langkah-langkah penyiapan lingkungan adalah sebagai berikut:

- **1.** Aktifkan fitur 'Virtual Machine Platform' dan 'Windows Subsystem for Linux' melalui Windows Features.
- **2.** Unduh dan instal Linux Kernel Update Package WSL2, lalu tetapkan WSL2 sebagai versi default dengan perintah: wsl --set-default-version 2.
- **3.** Instal Docker Desktop for Windows dan centang opsi 'Use the WSL 2 based engine'. Selesaikan proses instalasi dan lakukan restart komputer.

## 2.2 Inisiasi Kontainer ERPNext v15 dan Akses Port 8080

Proses inisiasi kontainer ERPNext dilakukan menggunakan Docker Compose. Eksekusi skrip kontainerisasi akan mengunduh image resmi Frappe/ERPNext v15 dan mengonfigurasi port forwarding ke localhost port 8080.

- **a.** Buka terminal Antigravity IDE atau PowerShell di direktori proyek ERPNext.
- **b.** Jalankan perintah pengoperasian stack kontainer: docker compose up -d.
- **c.** Verifikasi status kontainer yang sedang berjalan melalui perintah docker ps. Pastikan kontainer erpnext-python, erpnext-nginx, mariadb, dan redis berstatus 'Up'.
- **d.** Buka peramban web (Google Chrome/Edge) dan akses alamat http://localhost:8080.

## 2.3 Konfigurasi Initial Setup Wizard (Perusahaan, Mata Uang, & COA)

Saat pertama kali mengakses antarmuka ERPNext, pengguna akan disambut oleh Setup Wizard. Pengisian data awal harus mengikuti parameter baku studi kasus:

- **1.** Language & Country: Pilih Bahasa Indonesia / English, Country: Indonesia, Timezone: Asia/Jakarta, Currency: IDR (Rupiah).
- **2.** System User Profile: Masukkan nama pengguna (misal: Administrator) dan kata sandi yang aman.
- **3.** Company Details: Masukkan nama perusahaan 'PT Plastikindo Jaya Makmur', Abbrev: 'PJM', Chart of Accounts: 'Standard Indonesia Corporate Chart of Accounts' (atau buat kustom manufaktur).
- **4.** Financial Year: Tetapkan periode tahun fiskal berjalan (01 Januari 2026 s.d. 31 Desember 2026).

## 2.4 Generasi Dataset ERP_Plastikindo dan Otomasi Skrip

Untuk mempercepat penyiapan data awal, praktikum ini menyediakan skrip otomasi Python (generate_master_data.py) yang berjalan di dalam kontainer. Skrip ini secara otomatis menyuntikkan Master Barang, Stasiun Kerja, Routing, dan Saldo Awal Persediaan ke dalam basis data MariaDB.

Eksekusi skrip otomasi dilakukan dengan menjalankan perintah: docker exec -it erpnext-python bench execute plastikindo.setup.import_all. Hal ini menghemat waktu input manual hingga 80% dan memastikan data awal 100% presisi untuk simulasi akuntansi.


## 2.5 Navigasi Antarmuka GUI Desk ERPNext

Antarmuka utama ERPNext (disebut Desk) dirancang sangat intuitif. Komponen utama Desk meliputi:

- **Awesomebar (Bilah Pencarian Atas)**: Digunakan untuk navigasi cepat menuju DocType, Laporan, atau Modul apapun cukup dengan mengetikkan nama entitas (contoh: 'Item List', 'Work Order', 'General Ledger').
- **Workspace Sidebar**: Menampilkan kelompok modul bisnis seperti Accounting, Stock, Manufacturing, Buying, Selling, dan HR.
- **List View & Form View**: List View menampilkan daftar dokumen beserta statusnya (Draft, Submitted, Cancelled). Form View digunakan untuk membuat atau mengubah rincian dokumen.


# BAB III: EKSPLORASI MODUL UTAMA ERPNEXT UNTUK PEMBELAJARAN MANUFAKTUR


## 3.1 Modul Persediaan & Gudang (Stock & Inventory Management)

Modul Stock dalam ERPNext bertindak sebagai pusat kendali seluruh barang fisik. Konsep-konsep kunci yang wajib dikuasai mahasiswa meliputi:

- **a. Item Master**: Tempat mendefinisikan atribut barang seperti Item Code, Item Name, Item Group (Raw Material, Sub Assembly, Finished Goods), Default Unit of Measure (UOM), dan Valuation Method.
- **b. Metode Valuasi Stok**: ERPNext mendukung metode Moving Average (Rata-rata Bergerak) dan FIFO (First-In, First-Out). Dalam studi kasus ini digunakan metode FIFO untuk mencerminkan arus fisik barang di gudang plastik secara aktual.
- **c. Struktur Hirarki Gudang (Warehouse Tree)**: Gudang dikelompokkan secara hirarkis, misalnya: All Warehouses - PJM -> Stores - PJM (Gudang Bahan Baku), Work In Progress - PJM (Gudang Barang Dalam Proses), dan Finished Goods - PJM (Gudang Barang Jadi).
- **d. Stock Entry Types**: Jenis transaksi pergerakan barang seperti Material Receipt (Penerimaan), Material Issue (Pengeluaran), Material Transfer (Pemindahan antar gudang), dan Manufacture (Penerimaan hasil produksi).

## 3.2 Modul Manufaktur & Perencanaan Kebutuhan Bahan (MRP)

Modul Manufacturing merupakan jantung dari sistem manufaktur ERPNext. Modul ini mengintegrasikan struktur produk dengan alokasi stasiun kerja:

- **Bill of Materials (BOM)**: Dokumen induk yang memuat daftar komponen bahan baku, sub-rakitan, dan biaya operasi stasiun kerja yang dibutuhkan untuk membuat satu unit barang jadi. ERPNext mendukung Multi-Level BOM.
- **Workstation & Operation**: Stasiun kerja mencerminkan mesin atau area kerja fisik (misal: Mesin Injection Molding 500T). Setiap stasiun kerja memiliki parameter Operating Cost per Hour yang digunakan untuk menghitung biaya konversi/overhead.
- **Routing**: Urutan operasi produksi yang melintasi beberapa stasiun kerja beserta estimasi waktu operasi (Operation Time in Minutes).
- **Job Card**: Dokumen kerja digital yang diberikan kepada operator mesin untuk mencatat jam mulai/selesai kerja, jumlah barang bagus, dan kuantitas scrap/reject.

## 3.3 Modul Pengadaan (Buying) & Penjualan (Selling)

Siklus pengadaan (Procure-to-Pay / P2P) dan penjualan (Order-to-Cash / O2C) terhubung langsung dengan modul persediaan dan akuntansi:

- **1.** Siklus P2P: Material Request -> Purchase Order (PO) -> Purchase Receipt (PR) -> Purchase Invoice (PI) -> Payment Entry.
- **2.** Siklus O2C: Quotation -> Sales Order (SO) -> Delivery Note (DN) -> Sales Invoice (SI) -> Payment Entry.

## 3.4 Modul Akuntansi Keuangan (Financial Accounting)

ERPNext menggunakan Akuntansi Perpetual di mana setiap transaksi penerimaan/pengeluaran persediaan secara otomatis menerbitkan jurnal akuntansi. Komponen utamanya adalah Chart of Accounts (COA) yang dikelompokkan menjadi 5 kategori utama: Aset (1000), Kewajiban (2000), Ekuitas (3000), Pendapatan (4000), dan Beban/HPP (5000-6000).


## 3.5 Pembaruan dan Fitur Unggulan ERPNext Version 16

ERPNext Version 16 membawa peningkatan signifikan mencakup optimasi performa query MRP hingga 300%, antarmuka Job Card terintegrasi touchscreen untuk lantai pabrik, pembaruan otomatis kurs valuta asing real-time, serta analitik biaya manufaktur berbasis kecerdasan buatan.


# BAB IV: KASUS PRAKTIKUM INDUSTRI MANUFAKTUR PT PLASTIKINDO JAYA MAKMUR


## 4.1 Profil Perusahaan dan Spesifikasi Produk (FG-KM-01)

PT Plastikindo Jaya Makmur adalah entitas manufaktur yang bergerak di bidang pembuatan kemasan makanan plastik presisi tinggi. Produk unggulan yang dijadikan objek praktikum adalah Kotak Makan Bento 3 Sekat 1000ml (Kode Barang: FG-KM-01). Produk ini terdiri dari dua komponen utama: Wadah Bento 3 Sekat (SUB-KM-W3) dan Tutup Bento Bening (SUB-KM-T1), yang diproduksi melalui proses injection molding dan dikemas bersama komponen pembantu.


## 4.2 Struktur Master Data (Item, Workstation, Routing)

Tabel berikut menyajikan rincian Master Barang yang digunakan dalam simulasi produksi PT Plastikindo Jaya Makmur:


| Kode Barang | Nama Barang / Deskripsi | Kelompok Barang | UOM | Tipe Valuasi |
| --- | --- | --- | --- | --- |
| RM-PP-01 | Bijih Plastik Polypropylene (PP) Polybox | Raw Material | Kg | FIFO |
| RM-PIG-01 | Pigmen Masterbatch Biru B20 | Raw Material | Kg | FIFO |
| RM-SEAL-01 | Karet Seal Silikon Makanan | Raw Material | Pcs | FIFO |
| PM-BOX-01 | Master Karton Box 50x40x30cm | Packaging | Pcs | FIFO |
| PM-OPP-01 | Plastik OPP Wrapping Premium | Packaging | Meter | FIFO |
| PM-LBL-01 | Stiker Label Merek Plastikindo | Packaging | Pcs | FIFO |
| SUB-KM-W3 | Wadah Bento 3 Sekat 1000ml (Biru) | Sub Assembly | Pcs | FIFO |
| SUB-KM-T1 | Tutup Bento Bening Polos | Sub Assembly | Pcs | FIFO |
| FG-KM-01 | Kotak Makan Bento 3 Sekat Set Complete | Finished Goods | Set | FIFO |
| SCRAP-PL-01 | Gilingan Afval/Scrap Plastik PP Mixed | Scrap | Kg | FIFO |

Selanjutnya, proses manufaktur melintasi 4 Stasiun Kerja utama berikut:

- **1.** WS-INJ-01: Mesin Injection Molding Haitian 500T (Tarif: Rp 45.000,00 / Jam)
- **2.** WS-INJ-02: Mesin Injection Molding Haitian 350T (Tarif: Rp 35.000,00 / Jam)
- **3.** WS-ASSY-01: Meja Perakitan Manual & Pemasangan Seal (Tarif: Rp 20.000,00 / Jam)
- **4.** WS-PACK-01: Stasiun Pengemasan Final & Sealing Karton (Tarif: Rp 15.000,00 / Jam)

## 4.3 Kasus 1: Saldo Awal Persediaan Bahan Baku & Pengadaan (Opening Stock)

Pada tanggal 02 Januari 2026, PT Plastikindo Jaya Makmur mencatat Saldo Awal Persediaan Bahan Baku melalui dokumen Stock Entry jenis 'Material Receipt' (No. Dokumen: MAT-STE-2026-00001) ke Gudang 'Stores - PJM' sebagai berikut:


| Kode Barang | Kuantitas | UOM | Harga Satuan (Rp) | Total Valuasi (Rp) |
| --- | --- | --- | --- | --- |
| RM-PP-01 | 1.000 | Kg | 15.000,00 | 15.000.000,00 |
| RM-PIG-01 | 50 | Kg | 45.000,00 | 2.250.000,00 |
| RM-SEAL-01 | 2.000 | Pcs | 500,00 | 1.000.000,00 |
| PM-BOX-01 | 100 | Pcs | 8.000,00 | 800.000,00 |
| PM-OPP-01 | 500 | Meter | 500,00 | 250.000,00 |
| PM-LBL-01 | 2.500 | Pcs | 70,00 | 175.000,00 |

Total Valuasi Saldo Awal Persediaan yang tercatat pada akun Persediaan Bahan Baku (1131.001) adalah sebesar Rp 19.475.000,00 dengan tandingan akun Temporary Opening Account (3111.001).


## 4.4 Kasus 2: Perumusan Multi-Level Bill of Materials (BOM Costing)

Formulasi produksi Kotak Makan Bento Complete (FG-KM-01) disusun secara Multi-Level dengan rincian kebutuhan per 1 Unit Barang Jadi sebagai berikut:

- **BOM Level 1 (SUB-KM-W3): 0,12 Kg RM-PP-01 + 0,003 Kg RM-PIG-01 + Biaya Mesin WS-INJ-01 (1,2 menit = Rp 900,00). Total HPP Sub-Assembly Wadah = Rp 2.835,00 / Pcs.
- **BOM Level 1 (SUB-KM-T1): 0,08 Kg RM-PP-01 + Biaya Mesin WS-INJ-02 (0,9 menit = Rp 525,00). Total HPP Sub-Assembly Tutup = Rp 1.725,00 / Pcs.
- **BOM Level Top (FG-KM-01): 1 Pcs SUB-KM-W3 + 1 Pcs SUB-KM-T1 + 1 Pcs RM-SEAL-01 + 0,02 Pcs PM-BOX-01 + 0,2 Meter PM-OPP-01 + 1 Pcs PM-LBL-01 + Biaya Perakitan & Pengemasan WS-ASSY-01 & WS-PACK-01 (Rp 576,00). Total HPP Standar FG-KM-01 = Rp 7.611,00 / Set.

## 4.5 Kasus 3: Eksekusi Produksi Pabrik (Work Order, WIP Transfer, Job Cards, & Manufacture Entry)

Pada tanggal 10 Januari 2026, Departemen PPIC menerbitkan Work Order (WO-2026-00001) untuk memproduksi 1.000 Set FG-KM-01. Tahapan eksekusi produksi adalah sebagai berikut:

- **1.** Tahap 1: Transfer Bahan Baku dari Gudang Stores - PJM ke Gudang Work In Progress - PJM melalui Stock Entry 'Material Transfer for Manufacture' sebesar Rp 6.455.000,00.
- **2.** Tahap 2: Eksekusi Job Cards pada 4 Stasiun Kerja. Operator mencatat jam kerja aktual dan pelaporan afval plastik (SCRAP-PL-01) sebanyak 5 Kg @ Rp 4.000,00.
- **3.** Tahap 3: Penerimaan Barang Jadi ke Gudang Finished Goods - PJM melalui Stock Entry jenis 'Manufacture' sebesar 1.000 Set FG-KM-01.

## 4.6 Kasus 4: Siklus Penjualan Grosir dan Pengiriman (Sales Order, Delivery Note, & Sales Invoice)

Pada tanggal 15 Januari 2026, PT Plastikindo Jaya Makmur merealisasikan penjualan grosir kepada Distributor Utama sebanyak 1.000 Set FG-KM-01 dengan harga jual Rp 13.500,00 per Set (Total Omzet: Rp 13.500.000,00). Dokumen pengiriman Delivery Note (DN-2026-00001) memicu penurunan persediaan sebesar HPP Realisasi (Rp 7.611.000,00) dan pengakuan Beban HPP Penjualan.


## 4.7 Kasus 5: Analisis Laporan Keuangan, Cost of Goods Manufactured (COGM), dan Laba Kotor

Hasil akhir transaksi manufaktur dan penjualan menghasilkan performa keuangan sebagai berikut:

- **Pendapatan Penjualan (Sales Revenue): Rp 13.500.000,00
- **Harga Pokok Penjualan (COGS): Rp 7.611.000,00
- **Laba Kotor Penjualan (Gross Profit): Rp 5.889.000,00
- **Gross Profit Margin (GPM): 43,62%


# BAB V: MASTER BAGAN AKUN (CHART OF ACCOUNTS) DAN MEKANISME AKUNTANSI PERPETUAL


## 5.1 Struktur Kode Akun Manufaktur Indonesia (COA 1000–6000)

Tabel berikut menyajikan struktur Chart of Accounts (COA) manufaktur baku yang dikonfigurasi dalam ERPNext PT Plastikindo Jaya Makmur:


| Kode Akun | Nama Akun (Account Name) | Tipe Akun | Kelompok Laporan |
| --- | --- | --- | --- |
| 1111.001 | Kas Operasional Pabrik | Bank / Cash | Aset Lancar |
| 1121.001 | Piutang Usaha Dagang | Receivable | Aset Lancar |
| 1131.001 | Persediaan Bahan Baku & Kemasan | Stock | Aset Lancar |
| 1132.001 | Persediaan Barang Dalam Proses (WIP) | Stock | Aset Lancar |
| 1133.001 | Persediaan Barang Jadi (Finished Goods) | Stock | Aset Lancar |
| 1134.001 | Persediaan Scrap / Afval Plastik | Stock | Aset Lancar |
| 2111.001 | Utang Usaha / Pemasok | Payable | Kewajiban Jangka Pendek |
| 2121.001 | Beban Mesin & Overhead YMH Dibayar | Expenses Included in Valuation | Kewajiban Jangka Pendek |
| 3111.001 | Modal Disetor / Temporary Opening | Equity | Ekuitas Pemilik |
| 4111.001 | Penjualan Produk Plastik Bento | Income | Pendapatan Operasional |
| 5111.001 | Harga Pokok Penjualan (COGS) | Cost of Goods Sold | Beban Operasional |
| 5211.001 | Beban Biaya Overhead Pabrik Absorbsi | Expenses Included in Valuation | Beban Operasional |
| 5311.001 | Beban Scrap / Varians Efisiensi Bahan | Direct Expense | Beban Operasional |
| 6111.001 | Beban Gaji & Operasional Kantor | Expense | Beban Non-Operasional |
| 6211.001 | Beban Penyusutan Mesin Injection | Expense | Beban Non-Operasional |


## 5.2 Matriks Alur Jurnal Otomatis (General Ledger Entry & Stock Ledger Entry)

Setiap transaksi dalam ERPNext memicu pembaruan simultan pada dua buku besar: Stock Ledger Entry (SLE) untuk saldo kuantitas dan nilai stok fisik, serta General Ledger Entry (GLE) untuk saldo akun keuangan.


| Jenis Transaksi Dokumen | Efek Stock Ledger (SLE) | Akun Debit (GLE) | Akun Kredit (GLE) |
| --- | --- | --- | --- |
| Material Receipt (Opening) | Stores (+ Qty, + Val) | 1131.001 Persediaan Bahan | 3111.001 Temporary Opening |
| Material Transfer for WO | Stores (-) / WIP (+) | 1132.001 Persediaan WIP | 1131.001 Persediaan Bahan |
| Manufacture Stock Entry | WIP (-) / FG (+) | 1133.001 Persediaan FG | 1132.001 WIP & 2121.001 Overhead |
| Delivery Note (Pengiriman) | Finished Goods (- Qty) | 5111.001 Beban HPP (COGS) | 1133.001 Persediaan FG |
| Sales Invoice (Faktur) | Tidak ada perubahan | 1121.001 Piutang Usaha | 4111.001 Penjualan Produk |


## 5.3 Integritas Stok dan Keuangan (Stock Reconciliation & Valuation Ledger)

ERPNext menjamin integritas data melalui mekanisme Stock Reconciliation. Apabila terdapat selisih antara hasil perhitungan fisik (Stock Take) dengan catatan sistem, fitur Stock Reconciliation menerbitkan jurnal penyesuaian selisih stok ke akun Stock Adjustment Expense (5311.002) secara otomatis.


# BAB VI: LATIHAN SOAL AKADEMIS DAN PENYELESAIAN ANALITIS

Bagian ini menyajikan 5 Soal Latihan Kompleks yang dirancang untuk menguji pemahaman matematis, logika alur jurnal, dan analitik laporan keuangan mahasiswa.


## 6.1 Soal 1: Valuasi Persediaan Awal dan Jurnal Modal

**Soal:**  
PT Plastikindo Jaya Makmur memasukkan saldo awal persediaan bijih plastik RM-PP-01 sebanyak 2.500 Kg dengan nilai perolehan Rp 16.000,00/Kg dan pigmen RM-PIG-01 sebanyak 100 Kg @ Rp 50.000,00/Kg. Hitung total nilai valuasi stok awal dan susun ayat jurnal General Ledger Entry (GLE) bersangkutan!

**Jawaban Analitis:**

- **Valuasi RM-PP-01 = 2.500 Kg x Rp 16.000,00 = Rp 40.000.000,00
- **Valuasi RM-PIG-01 = 100 Kg x Rp 50.000,00 = Rp 5.000.000,00
- **Total Valuasi Persediaan Awal = Rp 45.000.000,00
- **Jurnal GLE: (D) 1131.001 Persediaan Bahan Baku Rp 45.000.000,00 | (K) 3111.001 Temporary Opening Account Rp 45.000.000,00.

## 6.2 Soal 2: Perhitungan HPP Standar BOM Multi-Level

**Soal:**  
Suatu produk Bento memerlukan 0,15 Kg bahan PP @ Rp 15.000,00/Kg, biaya stasiun kerja injection Rp 1.200,00/unit, dan biaya pengemasan Rp 600,00/unit. Apabila perusahaan menetapkan margin keuntungan 40% dari HPP Standar, hitunglah HPP Standar per unit dan Harga Jual Minimum!

**Jawaban Analitis:**

- **Biaya Bahan Langsung = 0,15 Kg x Rp 15.000,00 = Rp 2.250,00
- **Total HPP Standar = Rp 2.250,00 + Rp 1.200,00 + Rp 600,00 = Rp 4.050,00 / Unit
- **Harga Jual Minimum (Margin 40%) = Rp 4.050,00 / (1 - 0,40) = Rp 6.750,00 / Unit

## 6.3 Soal 3: Pencatatan Jurnal Pembelian Bahan Baku dan Utang Usaha

**Soal:**  
Perusahaan membeli 500 Pcs Karton Box PM-BOX-01 @ Rp 8.500,00 secara kredit dengan termin 2/10, n/30. Susun ayat jurnal pencatatan Purchase Receipt dan Purchase Invoice pada ERPNext!

**Jawaban Analitis:**

- **Total Pembelian = 500 Pcs x Rp 8.500,00 = Rp 4.250.000,00
- **Jurnal Purchase Receipt: (D) 1131.001 Persediaan Bahan Rp 4.250.000,00 | (K) 2112.001 Stock Received But Not Billed Rp 4.250.000,00.
- **Jurnal Purchase Invoice: (D) 2112.001 Stock Received But Not Billed Rp 4.250.000,00 | (K) 2111.001 Utang Usaha Rp 4.250.000,00.

## 6.4 Soal 4: Pencatatan Jurnal Alokasi Biaya Produksi dan HPP Realisasi (Work Order)

**Soal:**  
Eksekusi Work Order 2.000 unit produk membutuhkan pengeluaran bahan dari gudang sebesar Rp 12.000.000,00 dan alokasi jam kerja mesin injection sebesar Rp 2.500.000,00. Susun jurnal saat penerimaan barang jadi di Gudang Finished Goods!

**Jawaban Analitis:**

- **Total Nilai Barang Jadi (COGM) = Rp 12.000.000,00 + Rp 2.500.000,00 = Rp 14.500.000,00 (HPP Realisasi = Rp 7.250,00/unit)
- **Jurnal Manufacture Entry: (D) 1133.001 Persediaan Barang Jadi Rp 14.500.000,00 | (K) 1132.001 Persediaan WIP Rp 12.000.000,00 | (K) 2121.001 Expenses Included in Valuation Rp 2.500.000,00.

## 6.5 Soal 5: Analisis Penjualan, HPP, Laba Kotor, dan Margin Profitabilitas

**Soal:**  
Terjadi penjualan 1.500 unit barang jadi @ Rp 12.000,00 secara tunai. Nilai HPP tercatat Rp 7.250,00/unit. Hitung Laba Kotor dan Gross Profit Margin, serta tunjukkan posisi akun kas dan HPP!

**Jawaban Analitis:**

- **Total Penjualan = 1.500 x Rp 12.000,00 = Rp 18.000.000,00 | Total HPP = 1.500 x Rp 7.250,00 = Rp 10.875.000,00
- **Laba Kotor = Rp 18.000.000,00 - Rp 10.875.000,00 = Rp 7.125.000,00 | Gross Profit Margin = (7.125.000 / 18.000.000) x 100% = 39,58%

## 6.6 Panduan Penilaian dan Rubrik Evaluasi Akademis

Evaluasi akademis mahasiswa didasarkan pada 4 komponen aspek utama: (1) Ketepatan Input Master Data (20%), (2) Presisi Eksekusi Transaksi & Work Order (30%), (3) Kebenaran Rekonsiliasi Jurnal Akuntansi GLE/SLE (30%), dan (4) Kualitas Analisis Laporan Keuangan (20%).


# BAB VII: EVALUASI KONTRASTIF, TANTANGAN IMPLEMENTASI, DAN TROUBLESHOOTING


## 7.1 Kelebihan dan Kekurangan ERPNext dalam Pembelajaran PT

Penerapan ERPNext dalam pendidikan perguruan tinggi memiliki keunggulan dan tantangan yang perlu dievaluasi secara bijak:

- **a.** Keunggulan Utama: Lisensi open-source penuh (tanpa biaya langganan), arsitektur monolithic yang mudah dipahami, dukungan komunitas global yang luas, serta keterbukaan kode sumber untuk pengembangan kustomisasi.
- **b.** Tantangan Utama: Kurva pembelajaran awal yang cukup terjal bagi mahasiswa non-IT, persyaratan kurasi lingkungan Docker/WSL2 yang membutuhkan dukungan teknis laboratorium, serta dokumentasi beberapa fitur kustom yang masih berkembang.

## 7.2 Analisis Kebijakan Pengadaan: Open-Source vs Proprietary ERP

Perbandingan antara ERPNext (Open-Source) dengan software komersial berbayar (seperti SAP atau Oracle) menunjukkan bahwa ERPNext menawarkan Total Cost of Ownership (TCO) hingga 80% lebih rendah untuk skala manufaktur menengah, tanpa mengorbankan fungsionalitas inti akuntansi dan MRP.


## 7.3 Panduan Pemecahan Masalah Sistem (Troubleshooting Common Student Errors)

Berikut adalah 5 masalah utama yang sering dihadapi mahasiswa saat praktikum beserta solusi perbaikannya:

1. **Error: 'Negative Stock Exception' saat Submit Stock Entry**
   - **Penyebab**: Mencoba melakukan transaksi pengeluaran barang (Material Issue/Transfer) dari gudang yang saldo stok fisiknya nol atau kurang dari kuantitas yang diminta.
   - **Solusi**: Lakukan verifikasi saldo stok di Stock Summary. Apabila belum ada barang, jalankan transaksi Material Receipt (Opening Stock) atau periksa tanggal Posting Date transaksi.

2. **Error: 'Account Type Mismatch' pada Jurnal Persediaan**
   - **Penyebab**: Terjadi ketidakcocokan atribut Account Type pada Chart of Accounts dengan Default Account di Warehouse master.
   - **Solusi**: Buka Chart of Accounts, pastikan akun persediaan bersangkutan memiliki Account Type = 'Stock'. Buka Warehouse master dan tetapkan akun tersebut sebagai Default Account.

3. **Error: 'BOM Circular Reference' pada Perumusan Formula**
   - **Penyebab**: Terjadi relasi melingkar di mana Item A membutuhkan Item B, namun Item B juga memasukkan Item A sebagai komponen dalam BOM-nya.
   - **Solusi**: Buka BOM Item B, hapus Item A dari daftar tabel bahan baku, dan pastikan hirarki BOM bersifat sirkular satu arah (Parent -> Child).

4. **Error: 'Workstation Capacity Overload' saat Scheduling Work Order**
   - **Penyebab**: Kapasitas jam kerja stasiun kerja (Workstation) melebihi batas waktu operasional harian yang ditentukan dalam Working Hours.
   - **Solusi**: Sesuaikan parameter Working Hours di Workstation master atau bagi beban produksi ke dalam beberapa Job Cards / Stasiun Kerja alternatif.

5. **Error: 'Unsubmitted Stock Entry' pada Work Order Execution**
   - **Penyebab**: Mahasiswa lupa menekan tombol 'Submit' pada dokumen Stock Entry 'Material Transfer for Manufacture' sehingga status stok bahan masih berada di Gudang Stores.
   - **Solusi**: Buka kembali dokumen Stock Entry yang berstatus Draft, periksa kuantitas bahan, lalu klik tombol 'Submit' hingga status berubah menjadi Submitted.



# BAB VIII: KESIMPULAN, SOP OPERASIONAL, DAN CHECKLIST MANDIRI


## 8.1 Kesimpulan Integrasi Empat Teknologi

Sinergi antara ERPNext v15, Docker Desktop/WSL2, Antigravity IDE, dan Google NotebookLM terbukti menciptakan ekosistem pembelajaran ERP yang sangat modern, handal, dan adaptif. Mahasiswa tidak hanya menguasai teori akuntansi manufaktur, tetapi juga memiliki keterampilan praktis dalam mengoperasikan sistem enterprise skala industri.


## 8.2 Standard Operating Procedure (SOP 9 Tahapan Baku Praktikum)

Untuk menjamin kelancaran praktikum, seluruh mahasiswa wajib mengikuti 9 Tahapan Baku SOP berikut:


| Tahap SOP | Nama Langkah Operasional | Instruksi Eksekusi & Dokumen Acuan |
| --- | --- | --- |
| SOP 01 | Penyiapan Kontainer & Environment | Buka Docker Desktop & Antigravity IDE, pastikan status kontainer ERPNext 'Up' Port 8080. |
| SOP 02 | Inisiasi Perusahaan & COA Manufaktur | Jalankan Setup Wizard, atur nama PT Plastikindo Jaya Makmur dan struktur COA 1000-6000. |
| SOP 03 | Pencatatan Saldo Awal Persediaan | Input Stock Entry 'Material Receipt' untuk persediaan bahan baku dan verifikasi jurnal GLE/SLE. |
| SOP 04 | Perumusan Multi-Level BOM | Buat dokumen BOM untuk SUB-KM-W3, SUB-KM-T1, dan Top Level FG-KM-01 beserta alokasi biaya stasiun kerja. |
| SOP 05 | Penerbitan Work Order Manufaktur | Rilis Work Order produksi 1.000 Set FG-KM-01 dan atur jadwal kerja stasiun kerja injection. |
| SOP 06 | Transfer Bahan Baku to WIP | Eksekusi Stock Entry 'Material Transfer for Manufacture' dari Gudang Stores ke Gudang WIP. |
| SOP 07 | Pelaksanaan Job Cards & Afval | Operator menyelesaikan 4 Job Cards pada stasiun kerja dan mencatat scrap afval plastik. |
| SOP 08 | Manufacture Stock Entry (Finish) | Selesaikan eksekusi produksi, terima 1.000 Set FG-KM-01 ke Gudang Finished Goods. |
| SOP 09 | Penjualan Grosir & Audit Laporan | Proses Sales Order -> Delivery Note -> Sales Invoice, dan periksa Laporan Laba Rugi / Gross Profit. |


## 8.3 Lembar Kontrol dan Checklist Evaluasi Mandiri Mahasiswa

Gunakan tabel lembar kontrol berikut untuk memeriksa kelengkapan tugas praktikum sebelum melakukan pengumpulan laporan akhir:


| No | Item Verifikasi Praktikum | Status Mandiri | Paraf Instruktur / Dosen |
| --- | --- | --- | --- |
| 1 | Master Barang & Gudang terkonfigurasi 100% presisi | [  ] Selesai | ____________________ |
| 2 | Saldo Awal Persediaan Bahan Baku berhasil diposting (MAT-STE-2026-00001) | [  ] Selesai | ____________________ |
| 3 | BOM Multi-Level FG-KM-01 aktif dan lolos kalkulasi HPP Standar | [  ] Selesai | ____________________ |
| 4 | Work Order 1.000 Set selesai ditransfer dari WIP ke Finished Goods | [  ] Selesai | ____________________ |
| 5 | Delivery Note dan Sales Invoice tercatat dengan Omzet Rp 13.500.000,00 | [  ] Selesai | ____________________ |
| 6 | Laporan Laba Rugi menunjukkan Gross Profit Rp 5.889.000,00 (GPM 43,62%) | [  ] Selesai | ____________________ |
