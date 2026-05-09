Note-Taking App Data Structure
Aplikasi sederhana berbasis Python untuk simulasi struktur data pada sistem note-taking.
Project ini dibuat untuk memenuhi kebutuhan:


Multiple tags per note (Multi Linked List)


Chronological & alphabetical views (Doubly Linked List)


Sync status tracking (Circular Buffer)



📌 Features
1. Multiple Tags per Note
Satu note dapat memiliki banyak tag, dan satu tag dapat dimiliki banyak note.
Contoh:


Note "Tugas AI" → tag: Tugas, Penting


Note "Struktur Data" → tag: Kuliah, Penting


Menggunakan:


Multi Linked List



2. Chronological View
Menampilkan note berdasarkan urutan waktu dibuat.
Menggunakan:


Doubly Linked List



3. Alphabetical View
Menampilkan note berdasarkan urutan alfabet judul note.
Menggunakan:


Doubly Linked List



4. Sync Status Tracking
Menyimpan aktivitas terbaru seperti:


tambah note


edit note


hapus note


Menggunakan:


Circular Buffer (deque)



🛠️ Struktur Data yang Digunakan
FiturStruktur DataMultiple TagsMulti Linked ListChronological ViewDoubly Linked ListAlphabetical ViewDoubly Linked ListSync LogsCircular Buffer

📂 Struktur Project
note-taking-app/│├── main.py├── README.md└── screenshots/

▶️ Cara Menjalankan
1. Clone Repository
git clone https://github.com/username/note-taking-app.git
2. Masuk ke Folder Project
cd note-taking-app
3. Jalankan Program
python main.py

💻 Contoh Output
=== CHRONOLOGICAL VIEW ===[1] Struktur Data[2] Basis Data[3] Tugas AI=== ALPHABETICAL VIEW ===[2] Basis Data[1] Struktur Data[3] Tugas AITag: Penting- Struktur Data- Tugas AI=== RECENT SYNC LOGS ===2026-05-09 22:00:00 -> Added note 'Struktur Data'2026-05-09 22:00:01 -> Added note 'Basis Data'2026-05-09 22:00:02 -> Added note 'Tugas AI'

🧠 Konsep Struktur Data
Multi Linked List
Digunakan untuk relasi:


banyak note ↔ banyak tag


Ilustrasi:
Tag Kuliah   ↓[Note A] → [Note B]Tag Penting   ↓[Note A] → [Note C]

Doubly Linked List
Digunakan untuk:


navigasi next/previous


sorting chronological


sorting alphabetical


Ilustrasi:
[Note A] ⇄ [Note B] ⇄ [Note C]

Circular Buffer
Digunakan untuk:


riwayat aktivitas terbaru


sinkronisasi data


log perubahan


Ilustrasi:
[Edit A] [Tambah B] [Hapus C]
Ketika penuh:


data lama akan tertimpa otomatis
