# Data typing

age = 17
salary = 100000.0

print(type(age))
print(type(salary))

#tipe data ada 2 : tipe data primitif dan tipe data collection
# 1. tipe data primitif : number(Integer, float,complex), boolean(true, false), string
# 2. Tipe data collection : List, Tuple, set, dictionary

#tipe data number bersifat immutable
var = 10
print(id(var))

var = 20
print(id(var))

#string
teks = "herdo"
print(type(teks))

tekspanjang = """
    halo nama saya herdo
    saya tinggal di batam
    saya sangat menyukai pemrograman
    karena dengan pemrograman kita dapat menciptakan banyak hal

"""
print(tekspanjang)

#indexing/slicing string
print(teks[0])
print(teks[2:])

#string formatting 
print(f"nama saya {teks}") #format string
print("nama saya %s" %(teks)) #%-formating
print("nama saya {}".format(teks)) #str.format()

#List
x = [1,2,3,4,5,6,7,8,9]
#x[1] = 0 -> ini dapat di eksekusi karena tidak bersifat immutable
print(x[1])

#tuple
c = (1,2,3,4,5,6,7,8,9)
#c[2] = 0 -> ini akan menyebabkan error karena tuple bersifat immutable
print(c[2])

#set
d = {1,2,3} #data pada set tidak akan ada duplikat
f = {4,5,6} 

z = d.union(f) #menggabungkan 2 set, yaitu d dan f
print(z)

g = z.intersection(f)
print(g)

#dictionary
kucing = {
    'warna' : 'hitam',
    'jenis' : 'anggora',
    'umur'  : '2 tahun'
}
kucing['pemilik'] = "herdo" #menambahkan data
del kucing['jenis'] #enghapus data
kucing['warna'] = 'merah' #mengubah isi data

print(kucing['warna'])
print(kucing['pemilik'])


#konversi integer ke float
angka1 = 10
angkafloat1 =  float(angka1)
print(angkafloat1)

# konversi ke int : int()
# konversi ke string : str()
# konversi ke tuple :  tuple()
# konversi ke set : set()
# konversi ke list : list()

# contoh konversi ke dictionary : 
# dict([[1,2], [3,4]])