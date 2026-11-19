# ShootingRangeV2

Aplikasi desktop yang dikembangkan menggunakan **Python, PySide6, dan OpenCV** dengan arsitektur modular untuk mendukung pengembangan antarmuka, integrasi kamera, dan pengelolaan aplikasi.

## Tentang Proyek

ShootingRangeV2 merupakan pengembangan lanjutan dari prototype awal aplikasi simulasi shooting range real-time.

Proyek ini berfokus pada pengembangan aplikasi desktop yang terstruktur, mudah dipelihara, dan dapat dikembangkan lebih lanjut melalui pemisahan komponen antarmuka, logika aplikasi, serta layanan pendukung.

## Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python 3.11 | Bahasa pemrograman utama |
| PySide6 | Framework antarmuka desktop |
| OpenCV | Integrasi kamera dan pemrosesan video |
| NumPy | Pengolahan gambar dan frame kamera |
| Pytest | Pengujian otomatis aplikasi |

## Fitur Aplikasi

### Fitur yang Sudah Tersedia

- Halaman awal aplikasi (Start Screen).
- Halaman persetujuan pengguna (Agreement Screen).
- Jendela utama aplikasi.
- Tiga bagian navigasi utama:
  - **Quick Start** – Pengaturan koneksi kamera dan tampilan preview.
  - **Programs** – Antarmuka informasi program.
  - **Timed Drills** – Antarmuka konfigurasi latihan.
- Mock Camera untuk pengujian tanpa perangkat kamera fisik.
- Layanan integrasi kamera fisik menggunakan OpenCV.
- Fitur Connect dan Disconnect kamera.
- Tampilan preview kamera secara langsung.
- Konfigurasi aplikasi terpusat.
- Struktur aplikasi modular.
- Pengujian otomatis untuk layanan kamera.
- Fondasi sistem logging aplikasi.

### Rencana Pengembangan

- Penyelesaian tampilan halaman Programs berdasarkan prototype awal.
- Penyempurnaan halaman Timed Drills.
- Pengembangan lebih lanjut layanan kamera.
- Pengelolaan data aplikasi.
- Penambahan pengujian otomatis.
- Persiapan packaging dan deployment aplikasi.

*Fitur yang direncanakan dapat disesuaikan dengan kebutuhan dan hasil pengembangan selanjutnya.*

## Struktur Proyek

```text
ShootingRangeV2/
├── assets/
│   └── images/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHANGELOG.md
│   ├── DEVELOPMENT.md
│   └── TESTING.md
├── src/
│   └── shooting_range/
│       ├── config/
│       │   └── settings.py
│       ├── core/
│       │   ├── app.py
│       │   └── navigation.py
│       ├── services/
│       │   ├── camera_service.py
│       │   └── mock_camera_service.py
│       ├── ui/
│       │   ├── screens/
│       │   ├── pages/
│       │   ├── styles/
│       │   ├── camera_page.py
│       │   └── main_window.py
│       ├── utils/
│       │   └── logger.py
│       └── main.py
├── tests/
│   └── test_camera_service.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Persiapan dan Instalasi

### Persyaratan

- Python 3.11
- Git
- Sistem operasi Windows, Linux, atau macOS

### Langkah Instalasi

**1. Clone repository**

```bash
git clone https://github.com/RakanDhiya/ShootingRangeV2.git
cd ShootingRangeV2
```

**2. Membuat virtual environment**

```bash
python -m venv .venv
```

**3. Mengaktifkan virtual environment**

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

**4. Menginstal dependencies**

```bash
pip install -r requirements.txt
```

## Menjalankan Aplikasi

Dari direktori utama proyek, jalankan perintah berikut melalui Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m shooting_range.main
```

## Menjalankan Pengujian

Untuk menjalankan seluruh pengujian otomatis:

```bash
python -m pytest -v
```

## Pedoman Pengembangan

- Mengikuti arsitektur aplikasi modular.
- Memisahkan komponen antarmuka dengan layanan aplikasi.
- Menghindari penempatan logika layanan secara langsung di dalam komponen UI.
- Menggunakan konfigurasi terpusat untuk pengaturan aplikasi.
- Menulis kode yang jelas dan mudah dipelihara.
- Menyertakan docstring dan dokumentasi yang sesuai.
- Menambahkan pengujian otomatis untuk fungsionalitas baru.
- Memperbarui dokumentasi apabila terdapat perubahan arsitektur atau perilaku aplikasi.

## Dokumentasi

Dokumentasi tambahan tersedia di dalam direktori `docs/`:

| Dokumen | Keterangan |
|---|---|
| `ARCHITECTURE.md` | Penjelasan arsitektur dan tanggung jawab komponen aplikasi |
| `DEVELOPMENT.md` | Panduan lingkungan dan proses pengembangan |
| `TESTING.md` | Strategi dan panduan pengujian |
| `CHANGELOG.md` | Riwayat perubahan dan pengembangan proyek |

## Status Proyek

**Sedang dalam tahap pengembangan aktif.**

Aplikasi saat ini telah memiliki antarmuka desktop awal, fondasi integrasi kamera, serta pengujian otomatis untuk layanan kamera. Pengembangan selanjutnya akan difokuskan pada penyelesaian antarmuka aplikasi dan penyempurnaan komponen modular.

## Lisensi

Belum ditentukan.