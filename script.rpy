define s = Character("Serina")

define p = Character("[playername]")

transform mid:
    xalign 0.5
    yalign -3.0

transform left:
    xalign 0.2
    yalign -3.0

transform right:
    xalign 0.8
    yalign -3.0

label start:

    $ playername = renpy.input("Siapa Namamu?", length=32)
    $ playername = playername.strip()

    if not playername:
        $ playername = "Audric"

    p "Namamu adalah [playername]"

label intro:

    scene bg gku:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}[playername] adalah seorang calon mahasiswa yang mengikuti Campus Tour di Telkom University. Bersama rombongannya{/cps}"

    "{cps=40}[playername] mendengar penjelasan kakak Marketing Crew tentang berbagai fasilitas dan fakultas yang ada di Telkom University{/cps}"

    "{cps=40}Namun, saat tiba di Gedung GKU, tiba-tiba pandangan [playername] teralihkan oleh sekelompok angsa yang ada di penangkaran{/cps}"

    "{cps=40}[playername] malah mendekat ke kandang angsa{/cps}"

    scene bg kandang:
        zoom 0.25
    
    with Dissolve(0.5)

    pause 0.5

    p "{cps=40}Lucu juga ya, ada angsa di kampus{/cps}"

    "{cps=40}[playername] memandang dengan kagum{/cps}"

    "{cps=40}Saking asyiknya memperhatikan, [playername] tidak sadar kalau rombongannya sudah berjalan jauh meninggalkan [playername]{/cps}"

    "{cps=40}[playername] panik dan berlari untuk mengejar, tetapi ketika melihat sekeliling, mereka sudah tidak terlihat{/cps}"

    "{cps=40}Namun, sebelum benar-benar putus asa, seseorang menepuk bahu [playername] dengan pelan{/cps}"

    "?" "{cps=40}Hey, kamu nyasar ya?{/cps}"

    "{cps=40}Suara lembut seorang gadis mengagetkan [playername]{/cps}"

    "{cps=40}[playername] menoleh dan melihat seorang gadis dengan senyum wajah ramah di wajahnya{/cps}"

    "{cps=40}Gadis itu mengenakan jaket bertuliskan “Official Campus Guide” dengan name tag Serina di dadanya{/cps}"

    show serina neutral at mid:
        zoom 0.3

    with Dissolve(0.5)

    pause 0.5

    hide serina neutral

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    pause 0.5

    s "{cps=40}Aku Serina, guide di sini. Kamu dari rombongan mana?{/cps}"

    hide serina smile

    show serina neutral at mid:
        zoom 0.3

    with Dissolve(0.5)

    p "{cps=40}“Uh, rombongan yang tadi lewat situ…{/cps}"

    hide serina smile

    with Dissolve(0.5)

    "{cps=40}jawab [playername] sambil menunjuk arah depan GKU. Tempat terakhir ia melihat rombongan tour nya{/cps}"

    "{cps=40}Serina tertawa kecil{/cps}"

    show serina neutral at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Tenang saja, aku bisa bantu kamu. Karena kamu nyasar, gimana kalau aku kasih private tour yang lebih seru?{/cps}"

    hide serina neutral

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Aku bisa nunjukin tempat-tempat yang mungkin rombongan kamu nggak sempat kunjungi{/cps}"

    hide serina smile

    with Dissolve(0.5)

    "{cps=40}[playername] berbinar serta mengangguk mantap{/cps}"

label fit:

    scene bg fit:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Ilmu Terapan (FIT).{/cps}"

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0,5)

    s "{cps=40}FIT ini adalah salah satu dari tujuh fakultas di Telkom University{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40} Di fakultas ini, kamu akan lebih banyak mempelajari praktik ketimbang teori{/cps}"

    hide serina u 

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}jadi cocok buat kamu yang mau langsung terjun ke dunia kerja setelah lulus{/cps}"

label opsi_fit:

    hide serina smile

    s "{cps=40}Kamu bisa pilih informasi lain yang kamu inginkan di sini{/cps}"

    menu:

        s "Kamu bisa pilih informasi lain yang kamu inginkan di sini"

        "Program Studi":
            jump program_studi_fit

        "Prospek Kerja":
            jump prospek_kerja_fit

        "Fasilitas":
            jump fasilitas_fit

label program_studi_fit:

    show serina neutral at left

    screen display_text():
        add Text("{color=#FFFFFF}D3 Teknik Telekomunikasi\nD3 Rekayasa Perangkat Lunak Aplikasi\nD3 Sistem Informasi\nD3 Sistem Informasi Akuntansi\nD3 Teknologi Komputer \nD3 Digital Marketing\nD3 Hospitality & Culinary Art\nD3 Teknik Telekomunikasi (Jakarta)\nS1 Terapan Digital Creative Multimedia\nS1 Terapan Sistem Informasi Kota Cerdas{/color}", size=40) xalign 0.8 yalign 0.3

    show screen display_text

    s "{cps=40}Berikut Program-Program Studi yang ada di FIT{/cps}"

    hide screen display_text

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fit

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fit

label prospek_kerja_fit:

    show serina neutral at left

    screen display_text1():
        add Text("{color=#FFFFFF}Telecommunication Customer Service Specialist\nSoftware Developer\nFinancial Analyst\nMarketing Specialist\nHotel Operational Manager\nEntrepreneur{/color}", size=40) xalign 0.8 yalign 0.3

    show screen display_text1

    s "{cps=40}Berikut Prospek Kerja dari FIT{/cps}"

    hide screen display_text1

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fit

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fit

label fasilitas_fit:

    show serina neutral at left

    screen display_text2():
        add Text("{color=#FFFFFF}Mechanic Workshop Laboratory\nCellular Communication (CellComm) Laboratory\nTelecommunication Networking (TelNet) Laboratory\nOptical Communication System (OCS) Laboratory\nWireless Communication (WiComm) Laboratory\nElectronics and Communication System (ECS) Laboratory\nTelecommunication Technology Research Laboratory\nBusiness Computer Laboratory\nRetail Laboratory\nPangrango Office and Lounge{/color}", size=40) xalign 0.8 yalign 0.3

    show screen display_text2

    s "{cps=40}Berikut Fasilitas-Fasilitas dari FIT{/cps}"

    hide screen display_text2

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fit

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fit

label menu_fit:

    menu:

        s "{cps=40}Prodi apa yang fokus pada pengembangan aplikasi dan perangkat lunak?{/cps}"

        "Hospitality and Culinary Arts":
            jump fit_wrong

        "Rekayasa Perangkat Lunak":
            jump fit_right

label fit_wrong:

    "{cps=40}Salah, coba lagi ya. Cluenya, prodi ini sering bikin coding marathon{/cps}"

    jump menu_fit

label fit_right:
    
    "{cps=40}Benar! Kamu ternyata jago juga. Yuk, lanjut ke fakultas berikutnya{/cps}"

    jump fks

label fks:

    scene bg fks:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] menuju Fakultas Komunikasi dan Ilmu Sosial (FKS){/cps}"

    "{cps=40}Saat mereka tiba, Serina memberikan senyum misterius{/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}FKS merupakan tempat yang tepat buat kamu yang ingin mendalami atau mempelajari dinamika sosial{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Fakultas Komunikasi dan Ilmu Sosial (FKS) memiliki lima program studi yang telah terakreditasi nasional{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}beberapa program studi diantaranya telah terakreditasi Unggul dan A{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Selain itu terdapat program studi yang telah terakreditasi internasional dari IABEE{/cps}"

label opsi_fks:

    hide serina smile

    s "{cps=40}Kamu bisa pilih informasi lain yang kamu inginkan di sini{/cps}"

    menu:

        s "Kamu bisa pilih informasi lain yang kamu inginkan di sini"

        "Program Studi":
            jump program_studi_fks

        "Prospek Kerja":
            jump prospek_kerja_fks

        "Fasilitas":
            jump fasilitas_fks

label program_studi_fks:

    show serina neutral at left

    screen fks1():
        add Text("{color=#FFFFFF}Ilmu Komunikasi\nHubungan Masyarakat\nDigital Content Broadcasting\nPsikologi{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fks1

    s "{cps=40}Berikut Program-Program Studi yang ada di FKS{/cps}"

    hide screen fks1

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fks

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fks

label prospek_kerja_fks:

    show serina neutral at left

    screen fks2():
        add Text("{color=#FFFFFF}Corporate Communications Manager\nSocial Media Specialist\nSocial Media Data Analyst\nDigital Content Manager\nDigital Content Producer\nDigital Content Performance Analyst{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fks2

    s "{cps=40}Berikut Prospek Kerja dari FKS{/cps}"

    hide screen fks2

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fks

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fks

label fasilitas_fks:

    show serina neutral at left

    screen fks3():
        add Text("{color=#FFFFFF}Lab Post Production\nLab Fotografi\nLab Public Relations\nLab Broadcast Televisi 1\nLab Multimedia\nLab Audit Komunikasi\nLab Radio\nLaboratorium Broadcast Televisi 2\nLaboratorium Simulasi Bisnis\nLaboratorium Retailpreneur{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fks3

    s "{cps=40}Berikut Fassilitas-Fasilitas dari FKS{/cps}"

    hide screen fks3

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fks

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fks

label menu_fks:

    menu:

        s "{cps=40}Di FKS, jurusan apa yang fokus pada membangun hubungan publik yang kuat?{/cps}"

        "Ilmu Komunikasi":
            jump fks_wrong

        "Hubungan Masyarakat":
            jump fks_right

        "Digital Content Broadcasting ":
            jump fks_wrong

        "Psikologi":
            jump fks_wrong

label fks_right:

    "{cps=40}Wah, kamu cepat paham! Yuk, lanjut ke lokasi berikutnya!{/cps}"

    jump feb

label fks_wrong:

    s "{cps=40}Jawabannya masih salah.. Coba lagi ya{/cps}"

    jump menu_fks

label feb:

    scene bg feb:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] menuju Fakultas Ekonomi dan Bisnis (FEB){/cps}"

    "{cps=40}Saat mereka tiba, Serina memberikan senyum misterius{/cps}"

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Ekonomi dan Bisnis (FEB){/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Fakultas Ekonomi dan Bisnis (FEB) merupakan satu dari tujuh fakultas yang ada di dalam Universitas Telkom{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Fakultas Ekonomi dan Bisnis Telkom University hadir untuk menjawab segenap tantangan yang muncul dari perkembangan teknologi digital{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.5

    s "{cps=40}dengan merumuskan konsep education 4.0 yang akan menjawab tuntutan dari industry 4.0{/cps}"

    hide serina u 

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}mengeksploitasi teknologi digital dan mendukung terciptanya collaborative learning{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40} serta lifelong learning dengan tagline “Preparing The Digital Business Leader”{/cps}"

label opsi_feb:

    hide serina u 

    s "{cps=40}Kamu bisa pilih informasi lain yang kamu inginkan di sini{/cps}"

    menu:

        s "Kamu bisa pilih informasi lain yang kamu inginkan di sini"

        "Program Studi":
            jump program_studi_feb

        "Prospek Kerja":
            jump prospek_kerja_feb

        "Fasilitas":
            jump fasilitas_feb

label program_studi_feb:

    show serina neutral at left

    screen feb1():
        add Text("{color=#FFFFFF}S1 Manajemen Bisnis Telekomunikasi & Informatika (MBTI)\nS1 Akuntansi\nS1 Leisure Management\nS1 Administrasi Bisnis\nS1 Bisnis Digital\nS2 Manajemen\nS2 Manajemen PJJ\nS2 Administrasi Bisnis{/color}", size=40) xalign 0.8 yalign 0.3

    show screen feb1

    s "{cps=40}Berikut Program-Program Studi yang ada di FEB{/cps}"

    hide screen feb1

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_feb

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_feb

label prospek_kerja_feb:

    show serina neutral at left

    screen feb2():
        add Text("{color=#FFFFFF}Human Resource Manager\nBusiness Analyst\nAnalisator Keuangan\nKonsultan Pajak\nTravel and Tourism Management\nEntrepreneur{/color}", size=40) xalign 0.8 yalign 0.3

    show screen feb2

    s "{cps=40}Berikut Prospek Kerja dari FEB{/cps}"

    hide screen feb2

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_feb

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_feb

label fasilitas_feb:

    show serina neutral at left

    screen feb3():
        add Text("{color=#FFFFFF}Laboratorium Social Computing & Big Data\nLaboratorium Akuntansi Berbasis Komputer\nLaboratorium E-Commerce & IT Business\nLaboratorium Enterprise Resource Planning\nLaboratorium Statistics for Business\nLaboratorium Praktik Perpajakan\nLaboratorium Simulasi Bisnis\nTempat Uji Kompetensi FEB{/color}", size=40) xalign 0.8 yalign 0.3

    show screen feb3

    s "{cps=40}Berikut Fasilitas-Fasilitas dari FEB{/cps}"

    hide screen feb3

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_feb

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_feb

label menu_feb:

    menu:

        s "Benda apa yang identik dengan FEB?"

        "Microphone":
            jump feb_wrong

        "Pensil":
            jump feb_wrong

        "Kalkulator":
            jump feb_right

label feb_right:

    s "{cps=40}Wah, kamu cepat paham! Yuk, lanjut ke lokasi berikutnya!{/cps}"

    jump fik

label feb_wrong:

    s "{cps=40}Ups, salah! Cluenya, benda ini dipakai untuk menghitung.{/cps}"

    jump menu_feb

label fik:

    scene bg fik:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Industri Kreatif (FIK){/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Fakultas Industri Kreatif (FIK) Telkom University memiliki 7 Program Studi unggulan dan terlengkap di bidang kreatif{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}FIK telah menghasilkan banyak lulusan yang kiprahnya telah banyak memberikan warna pada perkembangan industri kreatif di Indonesia dan mancanegara{/cps}"

label opsi_fik:

    hide serina smile

    s "{cps=40}Kamu bisa pilih informasi lain yang kamu inginkan di sini{/cps}"

    menu:

        s "Kamu bisa pilih informasi lain yang kamu inginkan di sini"

        "Program Studi":
            jump program_studi_fik

        "Prospek Kerja":
            jump prospek_kerja_fik

        "Fasilitas":
            jump fasilitas_fik

label program_studi_fik:

    show serina neutral at left

    screen fik1():
        add Text("{color=#FFFFFF}S1 Desain Komunikasi Visual\nS1 Desain Produk\nS1 Desain Interior\nS1 Seni Rupa\nS1 Kriya \nS1 Film dan Animasi\nS1 Desain Komunikasi Visual (Jakarta)\nS2 Desain{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fik1

    s "{cps=40}Berikut Program-Program Studi yang ada di FIK{/cps}"

    hide screen fik1

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fik

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fik

label prospek_kerja_fik:

    show serina neutral at left

    screen fks2():
        add Text("{color=#FFFFFF}Desainer Grafis\nDesainer Produk\nDesainer Interior\nKriyawan\nSeniman\nCreative Director{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fik2

    s "{cps=40}Berikut Prospek Kerja dari FIK{/cps}"

    hide screen fik2

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fik

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fik

label fasilitas_fik:

    show serina neutral at left

    screen fik3():
        add Text("{color=#FFFFFF}Telkom University Creative Center (TUCC)\mGaleri Idealoka\nAula Fakultas Industri Kreatif\nLab Pola\nLab Bengkel\nLab Lukis\nLab Videografi\nLab Fotografi\nLab Ergonomi dan Material\nLab Display dan Lighting\nLab Mac\nLab Multimedia\nKelas Teori\nKelas Praktek{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fik3

    s "{cps=40}Berikut Fasilitas-Fasilitas di FIK{/cps}"

    hide screen fik3

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fik

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fik

label menu_fik:

    menu:

        s "Salah satu keahlian utama yang diajarkan di Fakultas Industri Kreatif adalah kemampuan mengembangkan konsep kreatif. Alat digital apa yang sering digunakan untuk membuat desain grafis?"

        "Microsoft Word":
            jump fik_wrong

        "Adobe Illustrator":
            jump fik_right

        "Excel":
            jump fik_wrong

        "PowerPoint":
            jump fik_wrong

label fik_right:

    s "{cps=40}Wah, kamu cepat paham! Yuk, lanjut ke lokasi berikutnya!{/cps}"

    jump fri

label fik_wrong:

    s "{cps=40}Ups, kurang tepat! Coba lagi ya..{/cps}"

    jump menu_fik

label fri:

    scene bg sl-fri:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Rekayasa Industri (FRI){/cps}"

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Kali ini kamu sedang ada di Gedung Kuliah 20 lantai Telkom University! Asik banget deh kalau dapat kelas di sini{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Soalnya bisa sambil lihat pemandangan Bandung dari atas{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Kalau kamu beruntung, bisa juga sambil melihat KCIC Whoosh sedang melaju cepat{/cps}"

label opsi_fri:

    hide serina smile

    s "{cps=40}Kamu bisa pilih informasi lain yang kamu inginkan di sini{/cps}"

    menu:

        s "Kamu bisa pilih informasi lain yang kamu inginkan di sini"

        "Program Studi":
            jump program_studi_fri

        "Prospek Kerja":
            jump prospek_kerja_fri

label program_studi_fri:

    show serina neutral at left

    screen fri1():
        add Text("{color=#FFFFFF}S1 Sistem Informasi\nS1 Sistem Informasi (International Class)\nS1 Sistem Informasi (Lanjutan)\nS1 Teknik Industri\nS1 Teknik Industri (International Class) \nS1 Digital Supply Chain \nS1 Manajemen Rekayasa{/color}", size=40) xalign 0.8 yalign 0.3

    show screen fri1

    s "{cps=40}Berikut Program-Program Studi yang ada di FRI{/cps}"

    hide screen fri1

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fri

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fri

label prospek_kerja_fri:

    show serina neutral at left

    screen fri2():
        add Text("{color=#FFFFFF}Application analys\nCyber security analyst \nData Analyst \nData Scientist \nDatabase Administrator \nIT Consultant \nIT Technical support officer \nSoftware engineer \nSystem Analyst {/color}", size=40) xalign 0.8 yalign 0.3

    show screen fri2

    s "{cps=40}Berikut Prospek Kerja dari FRI{/cps}"

    hide screen fri2

    menu:

        s "Masih ada yang ingin ditanyakan?"

        "Ya":
            jump opsi_fri

        "Tidak":

            s "{cps=40}Kalau gitu coba jawab pertanyaan berikut{/cps}"

            jump menu_fri

label menu_fri:

    menu:

        s "{cps=40}Jurusan IPS tidak bisa mendaftar Program Studi S1 Teknik Industri{/cps}"

        "Mitos":
            jump fri_right

        "Fakta":
            jump fri_wrong

label fri_right:

    s "{cps=40}Benar! Baik siswa IPA maupun IPS bisa mendaftar di Program Studi S1 Teknik Industr{/cps}"

    jump fte

label fri_wrong:

    s "{cps=40}Salah, coba lagi ya. Walaupun sudah pasti jawaban satunya yang benar{/cps}"

    jump menu_fri

label fte:

    scene bg sl-fte:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Teknik Elektro (FTE){/cps}"

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Masih di gedung kuliah TULT{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}mahasiswa Fakultas Teknik Elektro juga kuliah di sini lho! {/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Mahasiswa di fakultas ini suka banget bikin robot atau benda-benda keren lainnya. Yuk kita lihat!”{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label fte_right:

    s "{cps=40}{/cps}"

label fte_wrong:

    s "{cps=40}{/cps}"

label fif:

    scene bg sl-fif:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Fakultas Informatika (FIF){/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Program studi yang ada di Fakultas Informatika terkenal dengan coding dan data{/cps}"

    hide serina u 

    show serina smile:
        zoom 0.3

    s "{cps=40}Mereka juga belajar banyak hal tentang software dan cybersecurity{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label fif_right:

    s "{cps=40}{/cps}"

label fif_wrong:

    s "{cps=40}{/cps}"

label situ_techno:

    scene bg danau:
        zoom 0.25

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    pause 0.5

    s "{cps=40}Selamat datang di Situ Techno!{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Situ Techno sering dijuluki sebagai Danau Galau{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Pssstttt, konon katanya disebut sebagai Danau Galau karena ada mahasiswa teknik yang duduk-duduk di pinggiran situ sambil menggalaukan tugas akhirnya{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Situ Techno terletak tepat di depan Gedung Kuliah Umum (GKU){/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Situ ini, sering digunakan untuk bersantai , kerja kelompok, dan acara berkumpul lainnya.{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Di pinggiran Situi, disediakan banyak tempat duduk yang cocok digunakan oleh mahasiswa sebagai sarana bersantai maupun berkumpul{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Setelah sekilas mengetahui tentang Situ Techno, yuk bantu aku temukan teman untuk nongkrong cantik di Situ Techno!{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label asrama:

    scene bg asrama:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina Mengajak [playername] untuk bersepeda menggunakan beam menuju Asrama{/cps}"

    "{cps=40}Ketika sampai, Serina tersenyum lebar penuh antusias{/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Gedung Asrama merupakan 'rumah' bagi setiap mahasiswa baru!{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Gedung ini juga bisa secepatnya jadi rumah untuk Kamu!{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Di gedung ini, akan ada hadiah tersembunyi khusus untuk Kamu setelah menyelesaikan teka-teki{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Apakah kamu siap memecahkannya?{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label rektorat:

    scene bg bangkit2:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Serina mengajak [playername] berlari menuju Gedung Rektorat. Ketika sampai, Serina tersenyum penuh antusias{/cps}"

    show serina u at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Kamu adalah salah satu dari mereka yang beruntung bisa mengunjungi gedung ini. Karena ada kejutan spesial untukmu{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    "{cps=40}Serina mengajak [playername] masuk ke dalam Gedung Rektorat{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Di dalam gedung ini, tersembunyi hadiah spesial dari Rektor Telkom University yang bisa kamu temukan setelah memecahkan teka-teki{/cps}"

    hide serina u

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Apa kamu berani coba?{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label admisi:

    scene bg admisi:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Ketika sedang explore, Serina dan [playername] melewati gedung Admisi. {/cps}"

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Selamat datang di rumahku{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3
    
    s "{cps=40}Gedung ini adalah tempat dimana Serina hadir pertama kali untuk menemani calon mahasiswa baru{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

    "{cps=40}{/cps}"
    
    "{cps=40}{/cps}"

    "{cps=40}{/cps}"

label outro:

    scene bg admisi:
        zoom 0.25

    with Dissolve(0.5)

    pause 0.5

    "{cps=40}Akhirnya, perjalanan [playername] dan Serina telah sampai pada titik terakhir{/cps}"

    "{cps=40}Dari kejauhan, terlihat rombongan yang sedang beristirahat di depan Asrama{/cps}"

    show serina neutral at mid:
        zoom 0.3

    with Dissolve(0.5)

    pause 0.5

    hide serina neutral

    show serina smile at mid:
        zoom 0.3

    s "{cps=40}Nah, itu rombonganmu{/cps}"

    hide serina smile

    show serina u at mid:
        zoom 0.3

    s "{cps=40}Semoga kamu suka dengan perjalanan kita mengelilingi Telkom University{/cps}"

    hide serina u

    show serina neutral at mid:
        zoom 0.3

    "{cps=40}Saat kalian berpisah, Serina memberikan sebuah pin kecil berbentuk logo wajah Serina{/cps}"

    hide serina neutral 

    show serina wink at mid:
        zoom 0.3

    s "{cps=40}Simpan ini. Hanya mereka yang pernah nyasar yang dapat pin ini{/cps}"

    hide serina wink

    show serina neutral at mid:
        zoom 0.3

    "{cps=40} kata Serina bercanda{/cps}"

    "{cps=40}[playername] tersenyum dan mengangguk{/cps}"

    p "{cps=40}Terima kasih, Serina. Aku pasti akan kembali bukan sebagai siswa SMA{/cps}"

    p "{cps=40}melainkan sebagai mahasiswa Telkom University{/cps}"

    hide serina neutral

    with Dissolve(0.5)

    "{cps=40}[playername] berlari untuk bergabung dengan rombongan{/cps}"

    "{cps=40}Namun, sebelum [playername] benar-benar pergi meninggalkan Serina{/cps}"

    "{cps=40}[playername] menoleh kembali. Terlihat Serina melambaikan tangan dengan semangat{/cps}"

    show serina smile at mid:
        zoom 0.3

    with Dissolve(0.5)

    s "{cps=40}Sampai jumpa lagi, kami akan selalu menunggu kamu di sini{/cps}"

    hide serina smile

    with Dissolve(0.5)

    "{cps=40}[playername] tersenyum dengan lebar{/cps}"

    "{cps=40}[playername] merasa bahwa kunjungan kampus ini benar-benar tidak terduga{/cps}"

    "{cps=40}dan semakin membuat [playernam] yakin tentang masa depannya di Telkom University{/cps}"