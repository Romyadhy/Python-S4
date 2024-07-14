import random
namaGame = "WELCOMBACK TO MY"
chosed_user = random.randint(1, 5)

print("####################")
print(f"# {namaGame} #")
print("####################")


nama_user = input("Masukin nama lu: ")

print(f'''
    CEK {nama_user} lu coba deh liat nih di bawah ada apaan, Kira kita kalu lu disuruh liat, liat apa lu?
      ''')

user_cho = int(input("Kira kira kalo lu bener-bener pinter, coba tebak nih bearape jawabannya? Lu boleh milih: 1 / 2 / 3 / 4 / 5, pilih dah serah lu set dah: "))


print(f"pilihan elu nih {user_cho}")

comfirm = input("Apakah kamu yakin memilih ini? y/n ")
if comfirm == 'y' :
    if user_cho == chosed_user :
        print(f"Bener ga denger juga lu {chosed_user} GGG")
    else :
        print("Yah salah gimana nih yang berner aje rugi dong 💩")
        print(f"Jawaban yang bener ga degner ada di {chosed_user}")
elif comfirm == 'n' :
    print("Ya udh skip")
    
    

