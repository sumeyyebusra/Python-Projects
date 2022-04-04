def oyun_tahtasi():
    sayac = 0
    satir1 = ['x1',' ',' ',' ',' ',' ',' ']
    satir2 = ['x2', 'x2',' ',' ',' ',' ',' ']
    satir3 = ['x3','x3','x3',' ',' ',' ',' ']
    satir4 = ['x4','x4','x4','x4',' ',' ',' ']
    satir5 = ['x5','x5','x5','x5','x5',' ',' ']
    satir6 = ['x6','x6','x6','x6','x6','x6',' ']
    satir7 = ['x7','x7','x7','x7','x7','x7','x7']
    satirlar = satir1 + satir2 + satir3 + satir4 + satir5 + satir6 + satir7
    sutunlar = ['y1','y2','y3','y4','y5','y6','y7']
    taslar = satirlar + sutunlar
    girilen_cevaplar = ' '
    while ('x1' in satir1) or ('x2' in satir2) or ('x3' in satir3) or ('x4' in satir4) or ('x5' in satir5) or ('x6' in satir6) or ('x7' in satir7):
        print("OYUN TAHTASININ BAŞLANGIÇ KONUMU")
        print(satir1) 
        print(satir2)
        print(satir3)
        print(satir4)
        print(satir5)
        print(satir6)
        print(satir7)
        cevap1 = input("Sıra birinci oyuncuda! Kaldırmak istediğiniz satır ya da sütun numarasını giriniz:")

        while (cevap1 not in taslar):
            cevap1 = input("Burada bir taş yok. Lütfen geçerli bir numara giriniz:")
        while cevap1 in girilen_cevaplar:
            cevap1 = input("Burada bir taş yok. Lütfen geçerli bir numara giriniz:")
        girilen_cevaplar += cevap1

        if cevap1 in taslar:
            if 'x' in cevap1:
                if cevap1 == "x1":
                    satir1[0] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x2":
                    satir2[0:2] = ' '*2
                    print (satir1)
                    print(satir2)
                    print (satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x3":
                    satir3[0:3] = ' '*3
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x4":
                    satir4[0:4] = ' '*4
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x5":
                    satir5[0:5] = ' '*5
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x6":
                    satir6[0:6] = ' '*6
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "x7":
                    satir7[0:7] = ' '*7
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
            if "y" in cevap1:
                if cevap1 == "y1":
                    satir1[0] = ' '
                    satir2[0] = ' '
                    satir3[0] = ' '
                    satir4[0] = ' '
                    satir5[0] = ' '
                    satir6[0] = ' '
                    satir7[0] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y2":
                    satir2[1] = ' '
                    satir3[1] = ' '
                    satir4[1] = ' '
                    satir5[1] = ' '
                    satir6[1] = ' '
                    satir7[1] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y3":
                    satir3[2] = ' '
                    satir4[2] = ' '
                    satir5[2] = ' '
                    satir6[2] = ' '
                    satir7[2] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y4":
                    satir4[3] = ' '
                    satir5[3] = ' '
                    satir6[3] = ' '
                    satir7[3] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y5":
                    satir5[4] = ' '
                    satir6[4] = ' '
                    satir7[4] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y6":
                    satir6[5] = ' '
                    satir7[5] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap1 == "y7":
                    satir7[6] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
        sayac += 1
        if  ('x1' not in satir1) and ('x2' not in satir2) and ('x3' not in satir3) and ('x4' not in satir4) and ('x5' not in satir5) and ('x6' not in satir6) and ('x7' not in satir7):
            break

        cevap2 = input("Sıra ikinci oyuncuda! Kaldırmak istediğiniz satır ya da sütun numarasını giriniz:")
        while (cevap2 not in taslar):
            cevap2 = input("Burada bir taş yok. Lütfen geçerli bir numara giriniz:")
        while cevap2 in girilen_cevaplar:
            cevap2 = input("Burada bir taş yok. Lütfen geçerli bir numara giriniz:")
        girilen_cevaplar += cevap2

        if cevap2 in taslar:
            if 'x' in cevap2:
                if cevap2 == "x1":
                    satir1[0:1] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x2":
                    satir2[0:2] = ' '*2
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x3":
                    satir3[0:3] = ' '*3
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x4":
                    satir4[0:4] = ' '*4
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x5":
                    satir5[0:5] = ' '*5
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x6":
                    satir6[0:6] = ' '*6
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "x7":
                    satir7[0:7] = ' '*7
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
            if "y" in cevap2:
                if cevap2 == "y1":
                    satir1[0] = ' '
                    satir2[0] = ' '
                    satir3[0] = ' '
                    satir4[0] = ' '
                    satir5[0] = ' '
                    satir6[0] = ' '
                    satir7[0] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                if cevap2 == "y2":
                    satir2[1] = ' '
                    satir3[1] = ' '
                    satir4[1] = ' '
                    satir5[1] = ' '
                    satir6[1] = ' '
                    satir7[1] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "y3":
                    satir3[2] = ' '
                    satir4[2] = ' '
                    satir5[2] = ' '
                    satir6[2] = ' '
                    satir7[2] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "y4":
                    satir4[3] = ' '
                    satir5[3] = ' '
                    satir6[3] = ' '
                    satir7[3] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "y5":
                    satir5[4] = ' '
                    satir6[4] = ' '
                    satir7[4] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "y6":
                    satir6[5] = ' '
                    satir7[5] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
                elif cevap2 == "y7":
                    satir7[6] = ' '
                    print(satir1)
                    print(satir2)
                    print(satir3)
                    print(satir4)
                    print(satir5)
                    print(satir6)
                    print(satir7)
        sayac += 1
    if sayac % 2 == 0:
        print("BİRİNCİ OYUNCU KAZANDI!")
    else:
        print("İKİNCİ OYUNCU KAZANDI!")
oyun_tahtasi()

