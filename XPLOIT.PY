import os
import random

os.system("cls")

#password login
print("MASUKAN PASSWORD UNTUK MASUK KE PROGRAM KU")
password1=str(input("password: "))
if ( password1=="55146"):
    print("SELAMAT DATANG")

else:
    print("Passowrd Anda Salah!")




os.system("cls")


if ( password1=="55146"):

    print("ini adalah program buatan saya")
    print("dengan 10 pilihan:")
    print("1. QnA with bot")
    print("2. kekola uang saya")
    print("3. cek user")
    print("4. link Al Quran")
    print("5. Tentang Python")
    print("6. tools tools hacking")
    print("7. Book OF experience (creator only)")
    print("8. HELP")
    print("9. HACK DATA")
    print("10. ")
    option=int(input("silahkan pilih:"))

#ini option satu

os.system("cls")

if option==1:
    print("hallo ini bot sky xploit")
    print("disini ada menu yang bisa di tanyakan(akan terus di update)")
    print("1.siapa creator bot ini?")
    print("2.kapan di dirikan bot ini")
    print("3.apa itu QnA with bot")
    print("4.Sadboy1")
    print("5.Sadboy2")
    print("6.Sadboy3")
    option1=int(input("silahkan pilih option:"))
    if option1==1:
        print("crator bot ini adalah irfan")
    if option1==2:
        print("bot ini didirikan pada selasa,27 july 2021 07:30")
    if option1==3:
        print("QnA with bot adalah semacam media platfrom di didirikan oleh prof.irfan untuk menjawab pertanyaan dari kalian!")
    if option1==4:
        print("Aku berharap kamu menjadi pelangi yang muncul setelah hujan, tapi nyatanya kamu malah pergi bahkan sebelum hujan datang.")
        print("Sebelum kau sedingin hamparan hujan deras. Kau pernah sehangat hembusan nafas.")
        print("Pernah berjuang untuk sebuah senyuman, hingga akhirnya tinggal kenangan. Pernah menjadi bayangan, lalu hilang terbawa angan.")
    if option1==5:
        os.system("cls")
        print("Aku terlalu bersahabat dengan luka hingga lupa rasanya bahagia.")
        print( "Sakit hati ini sudah mulai terasa, setelah lama aku memendam perasaan sedih dan kecewa.")
        print( "Bodohnya aku masih merasa cemburu, ketika melihatmu dengan kekasih yang baru.")
    if option1==6:
        print( "Mencintaimu adalah hal yang paling mudah untuk aku lakukan, tetapi untuk mendapatkan cintamu itu lah hal yang paling sulit untuk aku lakukan.")
        print( "Mungkin kebahagiaan bersamamu hanya seperti mimpi, tapi biarlah mimpi itu terus menemani di setiap tidurku.")
        print( "Baru kusesali setelah ia pergi, dan menginginkannya kembali setelah ia menemukan pujaan hati.")
#ini option dua
if option==2:
    print("uang kamu saat ini Rp.800.000")
    print("__________________________________________")
    print("1. ingin ambil uang?(uang kamu akan berkurang)")
    print("2. ingin nabung?(uang kamu akan bertambah)")
    uang_saya=800000
    silahkan_pilih=int(input("option :"))
    if silahkan_pilih==1:
        print("ambil uang berapa?")
        option3=int(input("masukan jumlah uang ;"))
        hasil_uang=uang_saya-option3
        print("mengambil sukses!")
        print("uang anda sekarang adalah ",hasil_uang)
    elif silahkan_pilih==2:
        print("ingin nabung berapa?")
        option4=int(input("masukan jumlah uang ;"))
        hasil_uang2=uang_saya+option4
        print("menabung sukses")
        print("uang kamu sekarang adalah", hasil_uang2)
    else:
        print("mohon pilih yang benar")
#ini option tiga      
if option==3:
    print("irfan........(online)")
    print("syafiq.......(offline)")
    print("bot,cs.......(always on)")
    print(".......")
    print(".......")
    print("can't find another user")

#ini option empat
if option==4:
    print("1. QS. AL KAHFI UST HANAN ATTAKI 1 JAM")
    print("2. QS. AL BAQARAH UMMI FULL")
    mohon_dipilih=int(input("option :"))
    if mohon_dipilih==1:
        print("https://youtu.be/gFjUGvsyfxw")
    if mohon_dipilih==2:
        print("https://youtu.be/9PLwinD1sBI")
#ini option lima
if option==5:
    print(" python merupakan suatu bahasa programan yang cukup tergolong mudah")
    print("___________________________________________________")
    print(" mengapa bisa mudah? karena dia berbasis menggunakan bahasa inggris(tidak sepenuhnya code)")
    print(" nah kalau kalian ingin belajar Python klik 1 ")
    print("1. mulai belajar python!")
    silahkan=int(input("option :"))
    if silahkan==1:
        print("anda akan di ajarkan python jika prof.irfan mengizinkan!(izin terlebih dahulu)")
        print("contant prof.081293737374(creator)")
#ini option enam
if option==6:
    print("tools tools for hack")
    print("ada 10 tools hacking")
    print("1.John The Ripper")
    print("2.metasploit framework")
    print("3.Nmap")
    print("4.Aircrack-ng")
    print("5.Social Engineering Toolki")
    print("6.Maltego")
    print("7.Wireshark")
    print("8.Kismet")
    print("9.Burp suite")
    print("10.Ettercap")
    tools_hc=int(input("pilih :"))
    if tools_hc==1:
        print("John the Ripper adalah alat perangkat lunak peretas kata sandi gratis. Awalnya dikembangkan untuk sistem operasi Unix, dapat berjalan di lima belas platform yang berbeda.")
    if tools_hc==2:
        print("Kerangka Metasploit adalah alat canggih yang dapat digunakan oleh penjahat dunia maya, peretas topi putih, dan spesialis penetrasi untuk menyelidiki kerentanan jaringan dan server. Karena ini adalah kerangka kerja sumber terbuka, ini dapat dengan mudah dikonfigurasi dan digunakan pada kebanyakan sistem operasi")
    if tools_hc==3:
        print("Nmap (Network Mapper) adalah sebuah aplikasi atau tool yang berfungsi untuk melakukan port scanning. Nmap dibuat oleh Gordon Lyon, atau lebih dikenal dengan nama Fyodor Vaskovich. Aplikasi ini digunakan untuk meng-audit jaringan yang ada.")
    if tools_hc==4:
        print("Aircrack-ng adalah berbagai kumpulan aplikasi yang berguna untuk menilai dan mengukur tingkat keamanan pada jaringan WiFi. Aircrack bekerja pada jaringan WiFi yang mendukung monitoring mode dan bisa mendeteksi trafik jaringan dari 802.11a, 802.11b and 802.11g.")
    if tools_hc==5:
        print("Social Engineer Toolkit - Sebuah software hacking yang bertujuan untuk mencuri certificate atau permit dalam software. Caranya dengan menyimulasikan teknik hacking Social Engineer attack lalu memanfaatkan kelemahan pengguna.")
    if tools_hc==6:
        print("Maltego adalah salah satu tools OSINT(open source intelligence) yang digunakan untuk analisis berbasis gambar dalam mengumpulkan dan menghubungkan informasi untuk keperluan investigasi, intelligence dan forensics.")
    if tools_hc==7:
        print("Wireshark adalah program Network Protocol Analyzer alias penganalisa protokol jaringan yang lengkap. ... Program ini dapat merakam semua paket yang lewat serta menyeleksi dan menampilkan data tersebut sedetail mungkin, misalnya postingan komentar kamu di blog atau bahkan Username dan Password.")
    if tools_hc==8:
        print("Kismet adalah detektor jaringan wireless, sniffer, dan sistem pendeteksi penyusup pada komputer. ... - Untuk mendeteksi dan melihat semua jaringan nirkabel yang terbuka, serta Wireless Network yang tidak menggunakan SSID. Dengan menggunakan tool ini maka dalam hitungan menit kita bisa mengidentifikasi jaringan disekitar.")
    if tools_hc==9:
        print("BurpSuite berisi intercepting proxy yang memungkinkan pengguna melihat dan memodifikasi konten permintaan dan tanggapan saat sedang transit. Itu juga memungkinkan pengguna mengirim permintaan / tanggapan di bawah pemantauan ke tool lain yang relevan di BurpSuite, menghilangkan beban copy-paste.")
    if tools_hc==10:
        print("Ettercap adalah sebuah alat yang dibuat oleh Alberto Ornaghi (AloR) dan Marco Valleri (NaGa) dan pada dasarnya adalah sebuah perlengkapan untuk penyerangan “penengah” pada sebuah LAN. Untuk mereka yang tidak menyukai perintah berbaris (CLI), alat bentu ini disediakan dengan antar muka grafis yang mudah")
#ini opton tujuh
if option==7:
    print("maaf tetapi ini hanya bisa di akses oleh creator!")
    print(" apakah anda creator?")
    password=str(input("password: "))
    if ( password=="1401041"):
        print(" anda telah login!")
        print("ini lah buku pengalaman saya:")
        print("1. pengalaman coding")
        print("2. pengalaman gaming")
        print("3. pengalaman jb")
        print("4. pengalaman C")
        op7=int(input("pilih pengalaman berapa :"))
        if op7==1:
            print("pengalaman saya ketika coding,")     
            print(" cara tertarik pada programmer pada tahun 2019 walaupun saya tidak tahu apa apa pada saat itu")
            print(" tidak lama saya belajar jadi hacker gadungan haha, bermodal hp dan termux dan saya tidak mengerti apa itu coding, script")
            print(" dan pada akhirnya saya sempat vakum, lalu pada tahun 2021 saya ke ingat dengan sosok hacker di yt(hackbae) lalu tak lama saya tonton")
            print(" dan setelah menonton dia saya ada keinginan mencari tahu akan codingan, lalu saya menemukan channel web programing unpas,")
            print(" disitu lah saya belajar programan dari di mulai html,css. lalu saya beralih ke python")
            print(" semua yang saya pelajari secara otodidak, ya memang tidak mudah menjadi seorang programmer")
            print(" hal tersulit ketika sytnax eror disitu kita akan pusing wkwkw, sekarang saya dari python ingin beralih lagi ke java script")
        if op7==2:
            print(" pengalaman saya dalam gaming pada awal mula saya memainkan pvz, lalu saya beralih ")
            print(" ya itu aja sih gk banyak banyak pengalaman gua tentan gaming")

        

    else:
        print("password anda salah!")

#ini option delapan
if option==8:
    print("PANDUAN MENGGUNAKAN TERMINAL SAYA")
    print("SAYA HARAP INI BISA MENJAWAB PERTANYAAN KALIAN")
    print("1.BAGAIMANA CARA NGETIKNYA")
    print("2.BAGAIMANA INGIN MENGULANG PYTHON SCRIPT KE TERMINAL")
    op8=int(input("PILIH:"))
    if op8==1:
        print("DITERMINAL ANDA HANYA PERLU MASUKAN ANGKA SAJA, TIDAK USAH MEMAKAI HURUF")
    if op8==2:
        print("CARA MENGULANG PYTHON SCRIPT DI TERMINAL(MEREFRESH) ADALAH KLIK TOMBOL HIJAU DI SEBELAH KIRI KATA PROBLEM(DIBAGIAN ATAS)")
#ini option sembilan
if option==9:
    print("ONLY CREATOR!!!!!")
    print("ONLY CAN PASSWORD TO HACK")
    password9=str(input("password: "))
    if ( password9=="22664488157"):


        os.system("cls")


        print("hello sky!")
        print("00101001010101000101010010101010010000111110001010101010000101110010101010101010")
        print("0010100   01010   01010010     10010000111         110100   01110     0110101010")
        print("0010100   01010   010100   101   0100001  101010101010100   0111    101010101010")
        print("0010100   01010   01010    0101   100001  110101010101010   10   101010101010101")
        print("0010100           01010            01000  110010101010100      10010101010101010")
        print("0010100           010100   0101   000011  110010101010100   01   110101010101010")
        print("0010100   01010   010100   0101   000011  110101000010100   011    1000101010101")
        print("0010100   01010   010100   0101   000011  100010101010100   01110    01011101010")
        print("0010100   01010   010100   0101   00001110         010100   011100    0101010101")
        print("00101001010101000101010010101010010000111110001010101010000101110010101010101010")


        print("1.kelas 81")
        print("2.kelas 82")
        print("3.kelas 83")
        print("4.kelas 84")
        print("5.kelas 85")
        option5=int(input("$ :"))
        if option5==1:
            print("0075688497	Aida Zahra Qolbiah	Kelas VIII - Kelas VIII.1	P	Depok,-	93JG8S")
            print("0071849377	Alya Febrina Hamami Nata	Kelas VIII - Kelas VIII.1	P	Peureumeue,-	WGMH5F")
            print("0064341823	Areta Nuri Mahirah	Kelas VIII - Kelas VIII.1	P	Jakarta,-	B8VCW3")
            print("0061706522	Farhan Putra Wibowo	Kelas VIII - Kelas VIII.1	L	Jakarta,-	8K45CY")
            print("0074818558	Fayza Hani Ameera	Kelas VIII - Kelas VIII.1	P	Jakarta,-	CYFS9P")
            print("0073099996	Fiantika Risma Andira	Kelas VIII - Kelas VIII.1	P	Depok,-	0TMWV3")
            print("0069998859	Fitra Saiful Abral	Kelas VIII - Kelas VIII.1	L	Jakarta,-	6R1J3Z")
            print("0072349088	Irfan Arya Kusumawardhana	Kelas VIII - Kelas VIII.1	L	Jakarta,-	65NVBF")
            print("0073926635	Ismail Jaelani	Kelas VIII - Kelas VIII.1	L	Depok,-	ZC6Y5W")
            print("0066318655	Keisya Aprilia Maharani	Kelas VIII - Kelas VIII.1	P	Jakarta,-	H2PRZ6")
            print("0063161149	M. Dwi Ridwan Wicaksono Nugroho	Kelas VIII - Kelas VIII.1	L	Palembang,-	8YP9TV")
            print("0066448081	Muhamad Fahri Irawan	Kelas VIII - Kelas VIII.1	L	Tasikmalaya,-	MNS4BZ")
            print("0068107874	Muhammad Akbar Muzakki	Kelas VIII - Kelas VIII.1	L	Jakarta,-	H80XNG")
            print("0062990435	Muhammad Arvy Asy Syadzily	Kelas VIII - Kelas VIII.1	L	Jakarta,-	R92Q7D")
            print("0067348457	Muhammad Hafidz Ikhsananda	Kelas VIII - Kelas VIII.1	L	Jakarta,-	C94Z86")
            print("0067373525	Muhammad Putra Sandy	Kelas VIII - Kelas VIII.1	L	Bima,-	XM1GNZ")
            print("0074572343	Nafis Nabil Brian Fadhila	Kelas VIII - Kelas VIII.1	P	Depok,-	YGKV87")
            print("0075266589	Najwa Maulida	Kelas VIII - Kelas VIII.1	P	Depok,-	4GF78H")
            print("0074762928	Nayla Nurul Hidayat	Kelas VIII - Kelas VIII.1	P	Jakarta,-	1DWY3P")
            print("0078007963	Nazwa Zeeya Firmansyah	Kelas VIII - Kelas VIII.1	P	Depok,-	ZN368G")
            print("0072166229	Rangga Sindi Wardana	Kelas VIII - Kelas VIII.1	L	Jakarta,-	647W3F")
            print("0071235141	Ratih Miftahul Jannah	Kelas VIII - Kelas VIII.1	P	Jakarta,-	JYZ9P1")
            print("0077522305	Refiska Aulia Dewanti	Kelas VIII - Kelas VIII.1	P	Jakarta,-	3H49S8")
            print("0076523424	Revolino Purbo Dinata	Kelas VIII - Kelas VIII.1	L	Kediri,-	WSPXN3")
            print("0064971790	Rodiyatul Hadawiyah	Kelas VIII - Kelas VIII.1	P	Indramayu,-	8H2PCQ")
            print("0064376891	Saskia Desvita Akbar	Kelas VIII - Kelas VIII.1	P	Jakarta,-	3H6XWY")
            print("0069060874	Selena Firza Oktova	Kelas VIII - Kelas VIII.1	P	Cimahi,-	8P3Z4R")
            print("0073362759	Syahla Bahijatus Tsania	Kelas VIII - Kelas VIII.1	P	Depok,-	587MRV")
            print("0078567428	Syifa Alya Rachenda	Kelas VIII - Kelas VIII.1	P	Serang,-	JFH0Y5")
            print("0075506716	Ugroseno Dwi Prakastyo	Kelas VIII - Kelas VIII.1	L	Depok,-	K39YXS")
            print("0077456620	Zhalfan Thariq	Kelas VIII - Kelas VIII.1	L	Jakarta,-	ZYN3XS")
        else:
            print("LOL, TRY again")
            
        if option5==2:
            print("0079727798	Ade Agustyan	Kelas VIII - Kelas VIII.2	L	Depok,-	JR4BVH")
            print("0071980132	Ahyan Fikri Rasyid Hidayat	Kelas VIII - Kelas VIII.2	L	Jakarta,-	4WCHMP")
            print("0077960930	Alletha Yaskia Farizy	Kelas VIII - Kelas VIII.2	P	Jakarta,-	C26TRG")
            print("0071391459	Amanda Tarissya Putri	Kelas VIII - Kelas VIII.2	P	Depok,-	S416B5")
            print("0075458583	Aprilia Kurniawati	Kelas VIII - Kelas VIII.2	P	Jakarta,-	BXZG1N")
            print("0067030665	Aqib Krisan Rauf	Kelas VIII - Kelas VIII.2	L	Jakarta,-	734Y01")
            print("0077840438	Arpeggianita Meivika Prestanti	Kelas VIII - Kelas VIII.2	P	Jakarta,-	62R85N")
            print("0067553023	Arya Galih Putranto	Kelas VIII - Kelas VIII.2	L	Jakarta,-	YP0621")
            print("0074735245	Dzaki Fasya	Kelas VIII - Kelas VIII.2	L	Jakarta,-	MTR5Z9")
            print("0065088668	Fauzan Falihussyawal	Kelas VIII - Kelas VIII.2	L	Jakarta,-	XV9PSM")
            print("0068767287	Fitri Nurul Ulya	Kelas VIII - Kelas VIII.2	P	Jakarta,-	0V7NCZ")
            print("0066637009	Gendis Sekar Ayu Wahyono Putri	Kelas VIII - Kelas VIII.2	P	Jakarta,-	8925FD")
            print("0078105700	Githa Aura Febrianti	Kelas VIII - Kelas VIII.2	P	Langsa,-	YH9VNZ")
            print("0071529952	Hadyan Wafi Adlan	Kelas VIII - Kelas VIII.2	L	Jakarta,-	GY9K0N")
            print("0076690053	Kamilia Raina Naznin	Kelas VIII - Kelas VIII.2	P	Depok,-	2TDHG8")
            print("0071539561	Keysha Daffa Alisya	Kelas VIII - Kelas VIII.2	P	Kuningan,-	M86JRH")
            print("0068577150	Ladyra Selviana Andarosanti	Kelas VIII - Kelas VIII.2	P	Pekanbaru,-	MYNKGX")
            print("0068110280	Menara Nur Ramadani	Kelas VIII - Kelas VIII.2	P	Jakarta,-	ZG3HRT")
            print("0063984852	Muhammad Fajri Maulana	Kelas VIII - Kelas VIII.2	L	Jakarta,-	GD351S")
            print("0071481445	Muhammad Husni Thamrin	Kelas VIII - Kelas VIII.2	L	Karanganyar,-	K1DZBF")
            print("0071233377	Muhammad Rafli Azhar	Kelas VIII - Kelas VIII.2	L	Jakarta,-	Q0MT9V")
            print("0062594162	Muhammad Ridwane	Kelas VIII - Kelas VIII.2	L	Jakarta,-	2Z8DB3")
            print("0076464209	Muhammad Rozaan Arkansyah	Kelas VIII - Kelas VIII.2	L	Jakarta,-	WM5KP3")
            print("0066160554	Nur Ainayya	Kelas VIII - Kelas VIII.2	P	Depok,-	8CX53K")
            print("0113586047	Ra'afi Hermawan	Kelas VIII - Kelas VIII.2	L	Jakarta,-	V52GCB")
            print("0065968038	Rasyid Abdul Ghani Hidayatullah	Kelas VIII - Kelas VIII.2	P	Jakarta,-	7V6NBJ")
            print("0067951981	Sandy Avicena Alfitra	Kelas VIII - Kelas VIII.2	L	Jakarta,-	Z8XJC2")
            print("0069595929	Syafira Putri Alifia	Kelas VIII - Kelas VIII.2	P	Jakarta,-	CK3ZFM")
            print("077007342	Syah Fattah Ramadhan Assegaff	Kelas VIII - Kelas VIII.2	L	Bogor,-	PBGWSH")
            print("0062803706	Zahra Aulya Rahmadani	Kelas VIII - Kelas VIII.2	P	Jakarta,-	10M3DQ")
            print("0065953926	Zakiyatussakinah Yamani	Kelas VIII - Kelas VIII.2	P	Jakarta,-	N10ZBK")
            print("0074551079	Ziddan Yasir Emyutama	Kelas VIII - Kelas VIII.2	L	Tegal,-	W10DJ7")
        if option5==3:
            print("0076453111	Achmad Restu Firansyah	Kelas VIII - Kelas VIII.3	L	Depok,-	N5J6Y1")
            print("0076665842	Achmad Rif'at Bana'mah	Kelas VIII - Kelas VIII.3	L	Depok,-	3GWYXJ")
            print("0065277835	Ahmad Zakiy	Kelas VIII - Kelas VIII.3	L	Grobogan,-	06S1PR")
            print("0071077632	Althof Fabio Hibatulloh	Kelas VIII - Kelas VIII.3	L	Bekasi,-	WY1X65")
            print("0072303726	Angelina Keisha Putri	Kelas VIII - Kelas VIII.3	P	Jakarta,-	32TSN8")
            print("0065991592	Arbie Mulki Alpian	Kelas VIII - Kelas VIII.3	L	Jakarta,-	Q265KX")
            print("0074971321	Arisena Respati	Kelas VIII - Kelas VIII.3	L	Jakarta,-	3BTGCZ")
            print("0064234516	Augie Naurah Yumna Prastuti	Kelas VIII - Kelas VIII.3	L	Jakarta,-	ND52TY")
            print("0071591223	Aulia Nasova Solihat	Kelas VIII - Kelas VIII.3	P	Jakarta,-	W0GXRF")
            print("0069429461	Aziz Alfaruqi	Kelas VIII - Kelas VIII.3	L	Bogor,-	QVT5KY")
            print("0069395409	Deandra Tatyana Putri Timerman	Kelas VIII - Kelas VIII.3	P	Jakarta,-	7B0458")
            print("0063172311	Dido Wili Figoera	Kelas VIII - Kelas VIII.3	L	Purwokertao,-	56G3H0")
            print("0071995009	Dio Anugrah	Kelas VIII - Kelas VIII.3	L	Depok,-	HZP1YR")
            print("0065420814	Faatih Rizky Ananda	Kelas VIII - Kelas VIII.3	P	Jakarta,-	XV0N5P")
            print("076965271	Faiq Abdul Karim Shiddiq	Kelas VIII - Kelas VIII.3	L	Depok,-	5F7XBC")
            print("0074683472	Faulya Syifa Febriyani	Kelas VIII - Kelas VIII.3	P	Jakarta,-	7F4VGJ")
            print("0066307516	Gea Azzahra Ramadani Permana	Kelas VIII - Kelas VIII.3	P	Jakarta,-	HXJ48P")
            print("0075601926	Hafiz Riqki Maulana	Kelas VIII - Kelas VIII.3	L	Bogor,-	5MYNTW")
            print("0063014097	Izza Billah	Kelas VIII - Kelas VIII.3	P	Jakarta,-	2TF4DY")
            print("0068377161	Jafar Shodik	Kelas VIII - Kelas VIII.3	L	Jakarta,-	CBF9WQ")
            print("074817496	Keisya Zaharani Putri Hajar	Kelas VIII - Kelas VIII.3	P	Depok,-	J1BCHP")
            print("0077800956	Keizya Sitiandini	Kelas VIII - Kelas VIII.3	P	Jakarta,-	YQZ45D")
            print("0073149367	Maylaffaiza	Kelas VIII - Kelas VIII.3	P	Bekasi,-	XS4V9H")
            print("0057932650	Muhamad Rifqy	Kelas VIII - Kelas VIII.3	L	Jakarta,-	TRP7N5")
            print("0071570134	Muhammad Afif Syaifullah	Kelas VIII - Kelas VIII.3	L	Makassar,-	2WMZJT")
            print("0077671600	Muhammad Akbar Kaisar	Kelas VIII - Kelas VIII.3	L	Depok,-	6BMZ7D")
            print("0067230752	Nilam Rahma Sari	Kelas VIII - Kelas VIII.3	P	Jakarta,-	859W0D")
            print("0063282543	Shindi Rahayu	Kelas VIII - Kelas VIII.3	P	Tasikmalaya,-	RJ5FZS")
            print("0072615576	Sulthan Muhammad Haikhal	Kelas VIII - Kelas VIII.3	P	Jakarta,-	7JZW42")
            print("0071925596	Syafina Fathi Rizka	Kelas VIII - Kelas VIII.3	P	Jakarta,-	58PQXH")
            print("0053682445	Syahril Armani	Kelas VIII - Kelas VIII.3	P	Jakarta,-	T9SYB6")
        if option5==4:
            print("0074358289	Adam Gusti Nugroho	Kelas VIII - Kelas VIII.4	L	Jakarta,-	3DXG2V")
            print("0071424458	Alfin Firman Fatchurrozy	Kelas VIII - Kelas VIII.4	L	Surakarta,-	793RG2")
            print("0079278501	Alfira Gita Savina	Kelas VIII - Kelas VIII.4	P	Depok,-	1CNMRW")
            print("0072501394	Aly Rossyd Afwghony Putra	Kelas VIII - Kelas VIII.4	L	Jakarta,-	913Z2R")
            print("0074842994	Amanda Zahra Bilbina	Kelas VIII - Kelas VIII.4	P	Jakarta,-	7TGWDP")
            print("0075549541	Anisa Fauziyah Ardhiningrum	Kelas VIII - Kelas VIII.4	P	Depok,-	B4PSM8")
            print("0074600738	Bando Pratama	Kelas VIII - Kelas VIII.4	L	Depok,-	XNW1GQ")
            print("0068559122	Dewa Ayu Salsabila Gadis Ananda	Kelas VIII - Kelas VIII.4	P	Jakarta,-	M8W3BR")
            print("0071749075	Dhanendra Putra Keywa	Kelas VIII - Kelas VIII.4	L	Depok,-	MC9X2D")
            print("0076516269	Dian Shavira Aprillia	Kelas VIII - Kelas VIII.4	P	Jakarta,-	R7KXH4")
            print("0079554009	Early Khansa Haura	Kelas VIII - Kelas VIII.4	P	Depok,-	C3P8XF")
            print("0073496830	Faisal Gadil Mirsab	Kelas VIII - Kelas VIII.4	L	Jakarta,-	C8XZYM")
            print("0072191116	Fathur Rahman Nuska	Kelas VIII - Kelas VIII.4	L	Saning Bakar,-	QBCFK3")
            print("0078768697	Ghifana Adzkia Ahmad	Kelas VIII - Kelas VIII.4	L	Jakarta,-	CH96FK")
            print("0072031435	Kania Siti Nuraisyah	Kelas VIII - Kelas VIII.4	P	Jakarta,-	T8FV6K")
            print("0066525174	Kartika Mutiara Putri	Kelas VIII - Kelas VIII.4	P	Jakarta,-	CTZNJG")
            print("0074525213	Khaela Farras Ramadhani	Kelas VIII - Kelas VIII.4	P	Bogor,-	MNP91Z")
            print("0067641832	Khaira Nazira Siregar	Kelas VIII - Kelas VIII.4	P	Jakarta,-	PYQJ8V")
            print("0073457107	Khumaero Tunnisa Nur Rachmat	Kelas VIII - Kelas VIII.4	P	Depok,-	N8FZWD")
            print("0069551153	Mila Ayuning Tias	Kelas VIII - Kelas VIII.4	P	Nganjuk,-	4M7TW5")
            print("0073076172	Mochammad Febriansyah	Kelas VIII - Kelas VIII.4	L	Jakarta,-	XVYQ1H")
            print("0079251392	Muhammad Fadlu Robbi	Kelas VIII - Kelas VIII.4	L	Depok,-	6PHX0J")
            print("0064755873	Muhammad Zaky Kusumardi	Kelas VIII - Kelas VIII.4	L	Depok,-	KDZ4RT")
            print("0063609322	Mutia Kartika Kirana	Kelas VIII - Kelas VIII.4	P	Bekasi,-	FZWNDP")
            print("0061807423	Nuril Ardilah Bintari	Kelas VIII - Kelas VIII.4	L	Jakarta,-	9M3PWS")
            print("0064694457	Raden Roro Nayla Nadya Wibowo	Kelas VIII - Kelas VIII.4	P	Depok,-	CX78BG")
            print("0073065024	Radja Aditya Putra	Kelas VIII - Kelas VIII.4	L	Depok,-	8FRV4Q")
            print("0076165022	Rafiqa Putri Ramadhani	Kelas VIII - Kelas VIII.4	L	Jakarta,-	YJ74WB")
            print("0073954516	Saskia Hazizah	Kelas VIII - Kelas VIII.4	P	Depok,-	Y2WM1K")
            print("0078748025	Siti Hala	Kelas VIII - Kelas VIII.4	P	Jakarta,-	YV3RXQ")
            print("0078047236	Zahra Aulia Assholihah	Kelas VIII - Kelas VIII.4	P	Depok,-	SKC6M0")
        if option==5:
            print("0067832388	Adhesta Putra Pradhana	Kelas VIII - Kelas VIII.5	L	Jakarta,-	XVTZS3")
            print("0063947016	Adhwa Syafira Amnesti	Kelas VIII - Kelas VIII.5	P	Tebo,-	ZHJ3GB")
            print("0061917398	Andhika Wira Pratama	Kelas VIII - Kelas VIII.5	L	Jakarta,-	DMFJW0")
            print("0063280743	Anniza Destianti	Kelas VIII - Kelas VIII.5	P	Jakarta,-	4SFRD7")
            print("0058412135	Aril Nazam Pratama	Kelas VIII - Kelas VIII.5	L	Jakarta,-	308V4P")
            print("0074252381	Atikah	Kelas VIII - Kelas VIII.5	P	Depok,-	53478R")
            print("0071886863	Bintang Satrio Bumi	Kelas VIII - Kelas VIII.5	L	Banjarnegara,-	2MT94G")
            print("0077374542	Fika Istiqomah	Kelas VIII - Kelas VIII.5	P	Kuningan,-	7CDQVK")
            print("0076104060	Handika Wira Putra	Kelas VIII - Kelas VIII.5	L	Jakarta,-	0T2BKD")
            print("0071090316	Kaila Mozabila	Kelas VIII - Kelas VIII.5	P	Jakarta,-	SP001Q")
            print("0068038592	Keisya Ramadhani	Kelas VIII - Kelas VIII.5	P	Jakarta,-	B3JPQC")
            print("0072979607	Khamilla Putri Afifah	Kelas VIII - Kelas VIII.5	P	Jakarta,-	N29WCJ")
            print("0062020598	Khansa Azizah Septiandra	Kelas VIII - Kelas VIII.5	L	Jakarta,-	NKDBHP")
            print("0075422946	Makia Nur Asyarifah	Kelas VIII - Kelas VIII.5	P	Depok,-	VDC2M5")
            print("0066957934	Maulana Muhammad Zakariyya	Kelas VIII - Kelas VIII.5	L	Jakarta,-	6VRK80")
            print("0077676039	Maulidina Nuruddiniyah	Kelas VIII - Kelas VIII.5	P	Jakarta,-	2RYV4Q")
            print("0076318057	Muhammad Gautus Alam	Kelas VIII - Kelas VIII.5	L	Depok,-	YZNP6B")
            print("0079244508	Nabila Anindya Ramadhani	Kelas VIII - Kelas VIII.5	P	Jakarta,-	N1SY6X")
            print("0064685461	Nabila Aprilia Hidayat	Kelas VIII - Kelas VIII.5	P	Jakarta,-	4ZBDWY")
            print("0071575336	Naifa Anindyta Ramadhani	Kelas VIII - Kelas VIII.5	P	Jakarta,-	KSC6TZ")
            print("0077808947	Nirmala Afiffatu Syifa	Kelas VIII - Kelas VIII.5	P	Jakarta,-	8HCVDM")
            print("0068195446	Oktavia Rahma Fitriani	Kelas VIII - Kelas VIII.5	P	Jakarta,-	64FVC9")
            print("0073280580	Puan Kayla Lisana Sidqinia	Kelas VIII - Kelas VIII.5	P	Jakarta,-	XZT1W0")
            print("0063339988	Raden Genta Pasha Al-Kafi	Kelas VIII - Kelas VIII.5	L	Jakarta,-	DP3S6T")
            print("0063544635	Raihan Eka Prastiyo	Kelas VIII - Kelas VIII.5	P	Depok,-	FK4M7V")
            print("0076874909	Ravli Putra Boma	Kelas VIII - Kelas VIII.5	L	Jakarta,-	M9N806")
            print("0058348446	Rizky Ramadhan	Kelas VIII - Kelas VIII.5	L	Jakarta,-	R9JTV0")
            print("0065019666	Sania Salfa Sabilla	Kelas VIII - Kelas VIII.5	P	Jakarta,-	CQ0GK1")
            print("0065398254	Sheldy Melandri	Kelas VIII - Kelas VIII.5	P	Jakarta,-	2D6Z5F")
            print("0075726504	Siti Zahrotin Umaroh	Kelas VIII - Kelas VIII.5	P	Jakarta,-	XPZFNR")
            print("0068809765	Tasya Maghfiro	Kelas VIII - Kelas VIII.5	P	Jakarta,-	3VJGW6")
            print("0067759852	Thufail Al Ghifari	Kelas VIII - Kelas VIII.5	P	Jakarta,-	NK0XMC")
            print("0078956975	Tyo Putra Alfadhil	Kelas VIII - Kelas VIII.5	L	Depok,-	K29HTB")

#ini option sepuluh
if option==10:
    print("hello world")
