# restful_api
RFC Cookiecutter V1 RestFUL API

Scale to Infinity (Track API Web)
Tujuan Kursus:
Berpikirlah seperti insinyur perangkat lunak, bukan monyet kode. Pengembangan perangkat lunak adalah semua tentang mengambil masalah tingkat tinggi, dan kemudian mengubahnya menjadi scoping out, masalah ilmu komputer yang jelas yang dapat kita gunakan untuk memecahkan masalah. Bukan hanya mengetahui sintaks terbaru atau kerangka kerja mengkilap yang akan digunakan.

Pelajari semua seluk-beluk pengembangan API web menggunakan Flask sebagai contoh cemerlang, yang menyediakan kerangka kerja minimal untuk memaparkan Anda ke semua internal di balik aplikasi web modern apa pun.

Kembangkan pengalaman berkolaborasi dengan tim pada arsitektur skala besar & organisasi kode menggunakan pelat ketel populer yang membuat proyek Flask scalable di tim yang lebih besar. Berkolaborasi dengan pengembang lain menggunakan Github, ulasan kode standar, penyebaran Heroku, dll.

Jadikan portofolio Anda menonjol dengan pengalaman menciptakan produk nyata dalam produksi - Kohort bersama-sama akan bertanggung jawab untuk memberikan API web menyelesaikan masalah pemenuhan multi-saluran di akhir lintasan, yang akan dikonsumsi oleh aplikasi frontend dan melayani nyata pelanggan.
Kurikulum:
Persiapan Pra-Kursus: Minggu 1 - 3:
Format: Bagian ini tentu saja akan belajar sendiri dengan kolaborasi kelompok untuk mengajukan pertanyaan melalui saluran Slack.

Kami akan melakukan grup diskusi mingguan melalui Google Hangouts yang mencakup ~ 8 bab per minggu di tutorial utama serta beberapa sumber persiapan tambahan tambahan.

Tutorial induk labu
Sasaran 1: Membiasakan diri Anda dengan sistem backend server web sederhana. Kami memilih labu karena sistemnya sangat sederhana, sehingga Anda dapat memahami internal jika nanti Anda pindah ke kerangka kerja yang lebih lengkap seperti Django atau Ruby on Rails.
Sasaran 2: Memahami cara mengambil masalah bisnis tingkat tinggi dan mengonversinya menjadi model basis data yang mendasarinya.
Sasaran 3: Memahami cara kerja sistem migrasi basis data standar dan mengapa kita membutuhkannya.
Sasaran 4: Memahami cara menyebarkan pada Heroku dan mendapatkan aplikasi kerja ujung ke ujung yang dapat diakses oleh siapa saja.
Sasaran 5: Memahami batas waktu HTTP 30 detik pada Heroku, dan tahu kapan harus menggunakan pekerjaan latar belakang.

Model JWT (json web token)
Sasaran: Mengenal model JWT karena ini adalah model "klien-agnostik" yang paling umum untuk mengaktifkan akses API.

Pengaturan proyek Flask-RESTful + setup cookiecutter (walkthrough 60 menit)
Sasaran: Mempelajari cara mengatur kode untuk proyek yang lebih besar sehingga Anda tidak menembak diri sendiri dengan menulis banyak kode dalam pola yang buruk yang akan sulit untuk diperbaiki nanti.

Berpikir seperti insinyur perangkat lunak
Sasaran: Memahami perbedaan antara mempelajari sintaksis dan mengatasi masalah.

Penilaian Jangka Menengah: Minggu 4-5
Proyek: Spesifikasi lengkap ada di sini. Proyek penilaian jangka menengah adalah melakukan sebagian kecil dari spesifikasi ini:
Siapkan API RESTful-JWT otentikasi yang memungkinkan kami membuat pengguna, mengesahkan kredensial eBay, menambahkan daftar di eBay untuk pengguna itu, mengeditnya, dan juga mengakhiri daftar lebih awal.
Siapkan UI untuk melakukan pembaruan tersebut menggunakan API.
Munculkan hubungan model yang tepat dan titik akhir API sehingga kami dapat dengan mudah menanyakan operasi historis apa yang telah dilakukan pengguna pada platform eBay.
Menyebarkan proyek di Github & Heroku (dengan integrasi berkelanjutan) dan mengatur semua alat yang diperlukan untuk dengan mudah mengkonfigurasi / memantau aplikasi.
Muat aplikasi pengujian dan identifikasi kemacetan di aplikasi Anda, dan tentukan SLA yang mampu dipenuhi oleh layanan Anda.
Buat diagram arsitektur yang menggambarkan aliran data, dan jelaskan berbagai titik kegagalan sistem Anda dan bagaimana Anda berencana untuk menanggapi situasi tersebut.
Pada tingkat tinggi, tujuan kami adalah membantu pelanggan kami membuat daftar inventaris Amazon (mis. 500+ SKU) ke eBay dengan mengklik tombol. Bagaimana kami merancang titik akhir API untuk mendukung aliran ini, jika kami memiliki lebih dari 100 QPS di titik akhir ini?

Berhasil menyelesaikan penilaian ini diperlukan untuk pindah ke bagian selanjutnya.

Pada titik ini, semua orang yang lulus penilaian akan diminta untuk bergabung dengan kohort pertama kami untuk jalur Scale to Infinity!

Mulai Track to Infinity: Minggu 1-10:

Selama minggu-minggu lintasan ini, Anda akan menerapkan spesifikasi lengkap untuk masalah pemenuhan multi-saluran sebagai sebuah kelompok. Setiap minggu kami akan melakukan check-in dua mingguan untuk semua orang sehingga kami dapat dengan mudah melepaskan diri dari masalah.

Bersamaan dengan proyek, kami juga akan memiliki kelompok diskusi mingguan yang menyoroti hal-hal penting yang dipikirkan oleh insinyur perangkat lunak saat mereka membangun aplikasi tingkat produksi.

Minggu 1: Membangun sistem yang dapat diandalkan seperti air yang mengalir (pembicaraan 60 menit)
Uber mengandalkan lonjakan harga untuk menyeimbangkan penawaran dan permintaan di pasar pengendara / pengemudi. Pada NYE 2016, malam tersibuk tahun ini di mana semua orang di seluruh dunia bergantung pada Uber untuk transportasi, harga yang naik turun untuk malam itu. Harga yang ditetapkan terlalu rendah, menyebabkan mobil langsung terjual habis.

Orang-orang terdampar, tidak dapat menemukan transportasi selama berjam-jam dalam cuaca yang sangat dingin. Uber kehilangan kepercayaan sebagai perusahaan transportasi