# PinkNotes-AI
## Nama: Novellysna Nurziska
## Nim: 312410131
## Kelas: I241A
## Link ClickUp: https://app.clickup.com/90181887809/v/l/6-901817836509-1


## 🚀 Alur Antarmuka (UI)
### Aplikasi PinkNotes dirancang dengan alur yang intuitif, mulai dari penyambutan pengguna hingga penggunaan kecerdasan buatan untuk efisiensi mencatat.

## Splash Screen & Loading
<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 13 48 03" src="https://github.com/user-attachments/assets/bd012884-efdf-4058-86ed-a6830c3171f6" />

### Saat pertama kali dijalankan, aplikasi akan menampilkan Splash Screen dengan logo PinkNotes. Pada tahap ini, sistem melakukan inisialisasi awal dan memuat data yang diperlukan.  Tampilan: Logo utama dengan progres bar di bagian bawah. 

## Onboarding Screen
<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 13 48 04" src="https://github.com/user-attachments/assets/3a391bb4-dac3-4b9d-9fa5-21676b9b54b8" />

### Setelah memuat, pengguna akan disambut oleh halaman Onboarding. Halaman ini memberikan deskripsi singkat bahwa PinkNotes adalah aplikasi catatan pribadi untuk mengorganisir ide dengan mudah dan menyenangkan

## Deteksi Lokasi Otomatis
<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 15 21 50" src="https://github.com/user-attachments/assets/8e40796b-b153-42b1-b799-6d9ea66c1144" />

### Sebelum masuk ke halaman utama, aplikasi meminta izin akses lokasi. Setelah diberikan, aplikasi akan mendeteksi posisi pengguna secara real-time.  Contoh: Jika pengguna berada di wilayah tersebut, akan muncul notifikasi "Lokasi Anda: Kecamatan Batujaya" dan sapaan khusus "Halo!!! Selamat datang warga Kecamatan Batujaya!" pada header aplikasi.  

## Halaman Utama (Empty State)
<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 15 21 54" src="https://github.com/user-attachments/assets/aa0b7311-b175-4158-a833-18d349a9aa14" />

### Jika pengguna belum memiliki catatan, halaman utama akan menampilkan status "No Notes Available". Di sini terdapat tombol "+" (plus) untuk mulai menambah catatan baru.


## Proses Tambah Catatan & Generate Judul AI
<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 13 48 04 (2)" src="https://github.com/user-attachments/assets/3aced3e5-f933-41e0-8eda-5f6394f99170" />

### Input Konten: Pengguna menulis isi catatan yang panjang (misalnya tentang analisis faktor manusia dalam aplikasi).

<img width="717" height="1600" alt="WhatsApp Image 2026-05-03 at 13 48 05 (1)" src="https://github.com/user-attachments/assets/691712f7-ea90-45ef-8c00-138745bd5d56" />

### Setelah menekan "Buat Judul Otomatis" Hasil AI Backend Flask yang terintegrasi dengan Google Gemini AI akan memproses konten tersebut dan memberikan saran judul yang relevan, seperti "Analisis Faktor Manusia dalam Aplikasi", yang langsung mengisi kolom judul secara otomatis, Setelah judul terisi, pengguna dapat menekan tombol "Simpan". Catatan tersebut akan tersimpan ke dalam database lokal (SQLite) dan muncul di daftar catatan pada halaman utama.

## 🛠️ Ringkasan Teknologi yang Digunakan
### Frontend: Java (Android Studio).  
### Backend: Python (Flask) sebagai jembatan ke Google Gemini API.  
### API Lokasi: Fused Location Provider untuk deteksi wilayah.  
### Jaringan: Koneksi antara Android dan Backend menggunakan protokol HTTP (dengan konfigurasi network_security_config khusus untuk IP lokal).






