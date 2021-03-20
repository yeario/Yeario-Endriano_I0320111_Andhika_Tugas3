# List teman rio sebanyak 10
chingu = ['Sonny', 'Bagus', 'Attar', 'Alvin', 'Ano', 'Ryan', 'Raka', 'Nanda', 'Wahyu', 'Tito']

# menampilakan list indeks nomor 1,3,5
print(chingu[1], chingu[3], chingu[5])

# Mengganti list 2,5,9
chingu[2] = 'Ahmed'
chingu[4] = 'Rahmat'
chingu[9] = 'Rizal'

print(chingu)

# Menambah 2 teman rio pada list
chingu.extend(["Alda", "William"])

print(chingu)

# Menampilkan semua teman rio dengan perulangan
print("Teman rio : ada {} orang".format(len(chingu)))
for teman in chingu:
    print(teman)

# Menampilkan Panjang list
print(len(chingu))