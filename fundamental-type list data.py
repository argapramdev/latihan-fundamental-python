# tipe data sederhana/skalar
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list atau daftar atau array
#berbeda dengan type data skalar yang punya 4 variabel (anak1 s/d anak4), disini kita cukup pakai 1 variabel yaitu anak

anak = ['eko', 'dwi', 'tri', 'catur']
#biasa dibuat seperti ini, tapi ini masih rumit, karena masih banyak variabel yang perlu kita ketik, misal kita print
print(anak)
#maka akan muncul nama anak, dalam tulisan mendatar

#karena phycarm ini canggih maka bisa dengan melihat tanda kuning yang dtulisan anak, apabila kita sorot/alt enter
#maka akan berubah menjadi bentuk daftar seperti format yang telah di run, ex anak = ['eko', 'dwi', 'tri', 'catur']
#apabila kita pingin menambahkan nama anak maka kita pakai script anak append contoh;
anak.append('limo')
print(anak)
#bisa dilihat anak ke lima sudah ditambahkan dengan append
#kalau kita ingin menyapa anak ke lima caranya dengan fungsi f
print(f'haiiiii {anak[4]}!')
#inget kenapa kita tuliskan 4 padahal kita ingin memangiil anak ke 5, karena di script, ngitungnya mulai dari 0

#cara menyapa semua anak, dengan fungsi for a in anak
for a in anak:
    print(f'haloo {a}!')








