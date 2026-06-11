from Aritmatika import penjumlahan, perpangkatan, perkalian
from Konversi import cm_to_m, m_to_cm
from Ubah_Bilangan import desimal_to_biner, desimal_to_oktal, desimal_to_hexa
while True:
    print("\n====MENU UTAMA====")
    print("1. Arimatika")
    print("2. Konversi")
    print("3. Ubah_Bilangan")
    print("4. keluar")
    pilihan = input("Pilihan Menu:")

    if pilihan == "1":
        print("\n==Menu Aritmatika==")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")
        sub = input("Pilih Operasi:")
        a = float(input("masukkan bilangan pertama:"))
        b = float(input("masukkan bilangan kedua:"))

        if sub == "1":
            print("Hasil =", penjumlahan(a, b))
        elif sub == "2":
            print("Hasil =", perpangkatan(a, b))
        elif sub == "3":
            print("Hasil =", perkalian(a, b))
        else:
            print("Pilihan tidak valid!")

    elif pilihan == "2":
        print("\n==MENU KONVERSI==")
        print("1. CM to M")
        print("2. M to CM")
        sub = input("Pilih konversi:")
        nilai = float(input("Masukkan nilai:"))

        if sub == "1":
            print("Hasil =", cm_to_m(nilai), "m")
        elif sub == "2":
            print("Hasil =", m_to_cm(nilai), "cm")
        else:
            print("Pilihan tidak valid!")

    elif pilihan == "3":
        print("\n==MENU UBAH BILANGAN==")    
        print("1. Desimal ke Biner")
        print("2. Dsimal ke Oktal")
        print("3. Desimal ke Hexadesimal")
        sub = input("Pilih konversi:")
        angka = int(input("Masukkan bilangan desimal:"))

        if sub == "1":
            print("Hasil =", desimal_to_biner(angka))
        elif sub == "2":
            print("Hasil =", desimal_to_hexa(angka))
        elif sub == "3":
            print("Hasil =", desimal_to_oktal(angka))
        else:
            print("Pilihan tidak valid!")

    elif pilihan == "4":
        print("Terima Kasih Telah Menggunakan Program.")
        break
    else:
        print("Pilihan tidak valid!")    





