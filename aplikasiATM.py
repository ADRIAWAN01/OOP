print ("sela,ata datang di ATM ADRIAWAN")
print("pilih option  : ")
print("1.cek saldo")
print("2.Tarik uang")
print("3.Tabung uang")
option=int(input("silahkan pilih option : "))
if option == 1 :
    print("uang kamu berjumlah Rp.200.000")
elif option==2 :
    print("uang kamu berjumlah Rp.200.000, mau ambil berapa")
    print("1. 100.000")
    print("2. 200.000")
    uang_kamu=200000
    option2=int(input("pilih option : "))
    if option2==1 :
        hasil=uang_kamu-200000
        print("uang kamu sekarang berjumlah Rp. :",hasil)
    elif option2==2 :
        hasil=uang_kamu-200000
        print("uang kamu sekarang berjumlah Rp. :",hasil2)
    else:
        print("keyboard anda salah!")
elif option==3:
    uang_kamu=200000
    print("uang berjumlah Rp.200.000,mau ambil berapa.?")
    option=int(input("masukkan jumlah uang : "))
    hasil=uang+option3
    print("jumlah uang kamu sekarang adalah Rp. : ",hasil3)
else:
    print("keyboard anda salah,silahkan masukkan lagi : ")