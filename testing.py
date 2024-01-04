listTamuVip = ['jarot', 'dolah', 'ibong', 'lapet', 'jotaro']
check_nama = input('Check tamu VIP, Masukkan Nama Anda: ')

if check_nama in listTamuVip:
    print('Nama anda ada didalam Daftar Tamu VIP kami.')
    print(f"{check_nama}, Kamu salah satu tamu VIP kami.")
else:
    print(f"{check_nama}, Tidak ada didalam daftar Tamu VIP kami.")