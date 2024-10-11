define s = Character("Serina")

define p = Character("[playername]")

label start:

    $ playername = renpy.input("Siapa Namamu?", length=32)
    $ playername = playername.strip()

    if not playername:
        $ playername = "Audric"

    p "Namamu adalah [playername]"

label intro:

    scene bg gku:
        zoom 0.25

    "{cps=40}[playername] adalah seorang calon mahasiswa yang mengikuti Campus Tour di Telkom University. Bersama rombongannya{/cps}"

    "{cps=40}[playername] mendengar penjelasan kakak Marketing Crew tentang berbagai fasilitas dan fakultas yang ada di Telkom University{/cps}"

    "{cps=40}Namun, saat tiba di Gedung GKU, tiba-tiba pandangan [playername] teralihkan oleh sekelompok angsa yang ada di penangkaran{/cps}"

    "{cps=40}[playername] malah mendekat ke kandang angsa{/cps}"

    scene bg kandang:
        zoom 0.25

    p "{cps=40}Lucu juga ya, ada angsa di kampus{/cps}"

    "{cps=40}[playername] memandang dengan kagum{/cps}"

    "{cps=40}Saking asyiknya memperhatikan, [playername] tidak sadar kalau rombongannya sudah berjalan jauh meninggalkan [playername]{/cps}"

    "{cps=40}[playername] panik dan berlari untuk mengejar, tetapi ketika melihat sekeliling, mereka sudah tidak terlihat{/cps}"

    "{cps=40}Namun, sebelum benar-benar putus asa, seseorang menepuk bahu [playername] dengan pelan{/cps}"

    "?" "{cps=40}Hey, kamu nyasar ya?{/cps}"

    "{cps=40}Suara lembut seorang gadis mengagetkan [playername]{/cps}"

    "{cps=40}[playername] menoleh dan melihat seorang gadis dengan senyum wajah ramah di wajahnya{/cps}"

    "{cps=40}Gadis itu mengenakan jaket bertuliskan “Official Campus Guide” dengan name tag Serina di dadanya{/cps}"

    s "{cps=40}Aku Serina, guide di sini. Kamu dari rombongan mana?{/cps}"

    p "{cps=40}“Uh, rombongan yang tadi lewat situ…{/cps}"

    "{cps=40}jawab [playername] sambil menunjuk arah depan GKU. Tempat terakhir ia melihat rombongan tour nya{/cps}"

    "{cps=40}Serina tertawa kecil{/cps}"

    s "{cps=40}Tenang saja, aku bisa bantu kamu. Karena kamu nyasar, gimana kalau aku kasih private tour yang lebih seru?{/cps}"

    s "{cps=40}Aku bisa nunjukin tempat-tempat yang mungkin rombongan kamu nggak sempat kunjungi{/cps}"

    "{cps=40}[playername] berbinar serta mengangguk mantap{/cps}"

label fit:

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Ilmu Terapan (FIT).{/cps}"

    s "{cps=40}FIT ini adalah salah satu dari tujuh fakultas di Telkom University{/cps}"

    s "{cps=40} Di fakultas ini, kamu akan lebih banyak mempelajari praktik ketimbang teori{/cps}"

    s "{cps=40}jadi cocok buat kamu yang mau langsung terjun ke dunia kerja setelah lulus{/cps}"

label fks:

    "{cps=40}Serina mengajak [playername] menuju Fakultas Komunikasi dan Ilmu Sosial (FKS){/cps}"

    "{cps=40}Saat mereka tiba, Serina memberikan senyum misterius{/cps}"

    "{cps=40}FKS merupakan tempat yang tepat buat kamu yang ingin mendalami atau mempelajari dinamika sosial{/cps}"

    "{cps=40}Fakultas Komunikasi dan Ilmu Sosial (FKS) memiliki lima program studi yang telah terakreditasi nasional{/cps}"

    "{cps=40}beberapa program studi diantaranya telah terakreditasi Unggul dan A{/cps}"

    "{cps=40}Selain itu terdapat program studi yang telah terakreditasi internasional dari IABEE{/cps}"

label feb:

    "{cps=40}Serina mengajak [playername] menuju Fakultas Ekonomi dan Bisnis (FEB){/cps}"

    "{cps=40}Saat mereka tiba, Serina memberikan senyum misterius{/cps}"

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Ekonomi dan Bisnis (FEB){/cps}"

    s "{cps=40}Fakultas Ekonomi dan Bisnis (FEB) merupakan satu dari tujuh fakultas yang ada di dalam Universitas Telkom{/cps}"

    s "{cps=40}Fakultas Ekonomi dan Bisnis Telkom University hadir untuk menjawab segenap tantangan yang muncul dari perkembangan teknologi digital{/cps}"

    s "{cps=40}dengan merumuskan konsep education 4.0 yang akan menjawab tuntutan dari industry 4.0{/cps}"

    s "{cps=40}mengeksploitasi teknologi digital dan mendukung terciptanya collaborative learning{/cps}"

    s "{cps=40} serta lifelong learning dengan tagline “Preparing The Digital Business Leader”{/cps}"

    "{cps=40}{/cps}"

label fik:

    "{cps=40}Serina mengajak Player berlari menuju Fakultas Industri Kreatif (FIK){/cps}"

    s "{cps=40}Fakultas Industri Kreatif (FIK) Telkom University memiliki 7 Program Studi unggulan dan terlengkap di bidang kreatif{/cps}"

    s "{cps=40}FIK telah menghasilkan banyak lulusan yang kiprahnya telah banyak memberikan warna pada perkembangan industri kreatif di Indonesia dan mancanegara{/cps}"

    "{cps=40}{/cps}"

label fri:

    "{cps=40}Serina mengajak Player berlari menuju Fakultas Rekayasa Industri (FRI){/cps}"

    s "{cps=40}Kali ini kamu sedang ada di Gedung Kuliah 20 lantai Telkom University! Asik banget deh kalau dapat kelas di sini{/cps}"

    s "{cps=40}Soalnya bisa sambil lihat pemandangan Bandung dari atas{/cps}"

    s "{cps=40}Kalau kamu beruntung, bisa juga sambil melihat KCIC Whoosh sedang melaju cepat{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label fte:

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Teknik Elektro (FTE){/cps}"

    s "{cps=40}Masih di gedung kuliah TULT{/cps}"

    s "{cps=40}mahasiswa Fakultas Teknik Elektro juga kuliah di sini lho! {/cps}"

    s "{cps=40}Mahasiswa di fakultas ini suka banget bikin robot atau benda-benda keren lainnya. Yuk kita lihat!”{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label fif:

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Informatika (FIF){/cps}"

    s "{cps=40}Program studi yang ada di Fakultas Informatika terkenal dengan coding dan data{/cps}"

    s "{cps=40}Mereka juga belajar banyak hal tentang software dan cybersecurity{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label situ_techno:

    s "{cps=40}Selamat datang di Situ Techno!{/cps}"

    s "{cps=40}Situ Techno sering dijuluki sebagai Danau Galau{/cps}"

    s "{cps=40}Pssstttt, konon katanya disebut sebagai Danau Galau karena ada mahasiswa teknik yang duduk-duduk di pinggiran situ sambil menggalaukan tugas akhirnya{/cps}"

    s "{cps=40}Situ Techno terletak tepat di depan Gedung Kuliah Umum (GKU){/cps}"

    s "{cps=40}Situ ini, sering digunakan untuk bersantai , kerja kelompok, dan acara berkumpul lainnya.{/cps}"

    s "{cps=40}Di pinggiran Situi, disediakan banyak tempat duduk yang cocok digunakan oleh mahasiswa sebagai sarana bersantai maupun berkumpul{/cps}"

    s "{cps=40}Setelah sekilas mengetahui tentang Situ Techno, yuk bantu aku temukan teman untuk nongkrong cantik di Situ Techno!{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label asrama:

    "{cps=40}Serina Mengajak [playername] untuk bersepeda menggunakan beam menuju Asrama{/cps}"

    "{cps=40}Ketika sampai, Serina tersenyum lebar penuh antusias{/cps}"

    s "{cps=40}Gedung Asrama merupakan 'rumah' bagi setiap mahasiswa baru!{/cps}"

    s "{cps=40}Gedung ini juga bisa secepatnya jadi rumah untuk Kamu!{/cps}"

    s "{cps=40}Di gedung ini, akan ada hadiah tersembunyi khusus untuk Kamu setelah menyelesaikan teka-teki{/cps}"

    s "{cps=40}Apakah kamu siap memecahkannya?{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label rektorat:

    "{cps=40}Serina mengajak Player berlari menuju Gedung Rektorat. Ketika sampai, Serina tersenyum penuh antusias{/cps}"

    s "{cps=40}Kamu adalah salah satu dari mereka yang beruntung bisa mengunjungi gedung ini. Karena ada kejutan spesial untukmu{/cps}"

    "{cps=40}Serina mengajak Player masuk ke dalam Gedung Rektorat{/cps}"

    s "{cps=40}Di dalam gedung ini, tersembunyi hadiah spesial dari Rektor Telkom University yang bisa kamu temukan setelah memecahkan teka-teki{/cps}"

    s "{cps=40}Apa kamu berani coba?{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label admisi:

    "{cps=40}Ketika sedang explore, Serina dan Player melewati gedung Admisi. {/cps}"

    s "{cps=40}Selamat datang di rumahku{/cps}"
    
    s "{cps=40}Gedung ini adalah tempat dimana Serina hadir pertama kali untuk menemani calon mahasiswa baru{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"
    
    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label outro:

    "{cps=40}Akhirnya, perjalanan Player dan Serina telah sampai pada titik terakhir{/cps}"

    "{cps=40}Dari kejauhan, terlihat rombongan yang sedang beristirahat di depan Asrama{/cps}"

    s "{cps=40}Nah, itu rombonganmu{/cps}"

    s "{cps=40}Semoga kamu suka dengan perjalanan kita mengelilingi Telkom University{/cps}"

    "{cps=40}Saat kalian berpisah, Serina memberikan sebuah pin kecil berbentuk logo wajah Serina{/cps}"

    s "{cps=40}Simpan ini. Hanya mereka yang pernah nyasar yang dapat pin ini{/cps}"

    "{cps=40} kata Serina bercanda{/cps}"

    "{cps=40}[playername] tersenyum dan mengangguk{/cps}"

    p "{cps=40}Terima kasih, Serina. Aku pasti akan kembali bukan sebagai siswa SMA{/cps}"

    p "{cps=40}melainkan sebagai mahasiswa Telkom University{/cps}"

    "{cps=40}[playername] berlari untuk bergabung dengan rombongan{/cps}"

    "{cps=40}[playername] berlari untuk bergabung dengan rombongan{/cps}"

    "{cps=40}Namun, sebelum [playername] benar-benar pergi meninggalkan Serina{/cps}"

    "{cps=40}[playername] menoleh kembali. Terlihat Serina melambaikan tangan dengan semangat{/cps}"

    s "{cps=40}Sampai jumpa lagi, kami akan selalu menunggu kamu di sini{/cps}"

    "{cps=40}[playername] tersenyum dengan lebar{/cps}"

    "{cps=40}Player merasa bahwa kunjungan kampus ini benar-benar tidak terduga{/cps}"

    "{cps=40}dan semakin membuat Player yakin tentang masa depannya di Telkom University{/cps}"