# Membuat dictionary
dict = {'Nama': 'Rio', 'Hobi1': 'Koleksi sepatu', 'Hobi2': 'Fashion desain', 'Hobi3': 'Jualan', 'Sosmed1': 'ig:@yearioendriano',
        'Sosmed2': 'line:yearioendriano', 'Sosmed3': 'twitter:@ineedmorecuan', 'Lagu1': 'La La Lost You', 'Lagu2': 'Yellow',
        'Lagu3': 'To the Bone', 'Makanan1': 'Nasi goreng', 'Makanan2': 'Ayam goreng', 'Makanan3': 'Tempe'}

# Mengubah salah satu hobi dan sosmed, hapus 2 makanan, dan tambah 1 hobi
dict['Hobi2'] = 'Berenang'
dict['Sosmed3'] = 'ig:@our.dailygroup'
del dict['Makanan3']
del dict['Makanan2']
dict['Hobi4'] = 'Main Game'

print(dict)