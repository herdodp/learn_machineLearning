#Transformasi angka, karakter, dan string

#uppercase (huruf besar)
nama  = "herdo"
namabesar = nama.upper()
print(namabesar)

#lower (huruf kecil)
namakecil = nama.lower()
print(namakecil)

#menghilangkan whitespace atau karakter yang tidak diinginkan
namaspasi = "  herdo   pratirto   "
print(namaspasi.strip()) #menghilangkan whitespace di awal dan akhir string
print(namaspasi.lstrip()) #menghapus whitespace awal string
print(namaspasi.rstrip()) #menghapus whitespace akhir string

namanonspasi = 'herdo dimas'
print(namanonspasi.strip("herdo")) #menghilangkan kata herdo


#startswith
#menemukan suatu kata di awal string
print(namanonspasi.startswith('herdo')) #hasil berupa boolean 

#endswith()
#menemukan suatu kata pada akhir string
print(namanonspasi.endswith("dimas")) #hasil berupa boolean

#join()
#memisah dan menggabungkan string
print(' '.join(['herdo',  'dimas', 'pratirto']))

#split()
#memisahkan kata/substring berdasarkan delimiter
print('herdo dimas pratirto'.split()) #hasilnya berupa list


#replace()
#mengganti elemen string dengan string yang lain
namalengkap = 'herdo dimas'
namalengkapreplace = namalengkap.replace('dimas','pratirto')
print(namalengkapreplace)

#mengecek string huruf besar semua
teks = 'kucing'
print(teks.isupper()) #hasil berupa boolean

#mengecek string huruf kecil semua
print(teks.islower()) #hasil berupa boolean

#mengecek string huruf alfabet semua
print(teks.isalpha()) #hasil berupa boolean

#mengecek string berisi alfanumerik
print(teks.isalnum()) #hasil berupa boolean

#mengecek string berisi numerik
print(teks.isdecimal()) #hasil berupa boolean

#mengecek string hanya berisi whitespace
print(teks.isspace()) #hasil berupa boolean

#mengecek setiap kata dalam string berawal huruf kapital
print(teks.istitle()) #hasil berupa boolean




#Formatting pada string
# zfill(), rjust(), ijust(), center()

#zfill() menambahkan 0 didepan string dengan panjang tertentu
cobateks = 'herdo'
coba0 = cobateks.zfill(6)
print(coba0)
#zfill() akan menambahkan angka 0 pada awal string jika panjang kata dalam string lebih sedikit dari panjang yang ada dalam zfill. dalam contoh diatas, panjang string adalah 5 karakter, dalam zfill(6) ada 6 karakter. karena panjang pada zfill(6) ada 6 karakter, maka akan ditambahkan angka 0 diawal string karena kata herdo 'herdo' hanya ada 5 karakter

#rjust() membuat teks/sring rata kanan
print(cobateks.rjust(20))
print(cobateks.rjust(20, '!'))

#ljust membuat teks/string rata kiri
print(cobateks.ljust(20))
print(cobateks.ljust(20, '!'))

#center() membuat teks/string rata tengah
print(cobateks.center(20, "!"))

#escape character
# \' \" \n \t \\ 
esch = "\"jum\'at\""
print(esch)

#raw string : mencetak sesuai dengan apapun teks yang diberikan

raws = r"herdo dimas\n"
print(raws)


