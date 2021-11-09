import math as mt

def Analiz(soru):
                        ##########  SORUDAKİ ÖNEMLİ ANAHTAR KELİMELERİ BULMA (1. KISIM)  ##########

    sayilar = "0123456789"   # sağ taraftaki değerlerin int olup olmadığı kontrolü için lazım olan değer
    #kalip1List = []          # kalıpların sağında sayı, kenar ve açı orantıları ve sadece bilinmeyen değer içeren kalıp listesi
    #kalip2List = []          # kalıbın sağı int ve str değerlerden oluşan kalıp listesi
    #sorulan = []             # soruda cevabı istenilen kalıbın sağ tarafını içeren liste 
    
    soru = soru.replace('\n','') # görüntüden gelen metindeki fazlalık boşlukları temizler

    def GereksizSil(metin):

        soru = metin
        soru = soru.replace('I','') # | işaretini I diye algıladığında, I işaretini temizler
    
        k = 0 
        a = 0
        b = -1
        for i in soru:
            a+=1

            if (i == '.' or i == "'" or i == ',' or i == '°'):
                soru = soru.replace(i,' ')

            if (i =='t' or i =='d' ):            

                if (soru[a] =='ı' or soru[a] == 'i' or soru[a] == 'u' or soru[a] == 'ü'):

                    if soru[a+1] == 'r':
                        soru = soru.replace(soru[a-1:a+2],'   ')  
        for i in soru:
            b+=1
            if(i == "]"):   # diklik işaretini 1 diye algılarsa                
                if(soru[b+2] == '1'):
                    soru = soru[0:b+1]+ "⊥"+ soru[b+3:len(soru)]

        soru = soru.replace("   "," ")
    
        bos = BoslukSay(soru)

        son = BoslukKoy(soru,bos,k)
        return son       # Sorudaki . , ' dır dir gibi kalıpları silme ve kalıplar arasına boşluk koyma fonksiyonu 
                                     


    def HarfSekil(soru): # sekil döndüren fonksiyon ABC.....

        cumle = soru.split() # split fonksiyonu belirten karaktere göre cümleyi kelimelere bölüp diziye aktarır
        a = 0
        #harfsekil = []

        for kelime in cumle:

            if (kelime.isupper() and len(kelime) > 2): # tüm harfler büyük ve 3ten fazla ise
                i = kelime[0]
                k = (len(kelime)-1)

                if (i != '(' and i != '[' and i != '=' and i != '/' and i != '⊥'):# baştaki karakter kontrolü 

                    if (kelime[k] != ')' and kelime[k] != ']' and kelime[k] != '⊥' and kelime[k] != '/' and kelime[k] != '°'): # sondaki karakter kontrolü
                        harfsekil = kelime
                        break
                        #islemDosyasiOlustur(kelime)
        return harfsekil          # Sorudaki köşe harflerini ('ABC üçgen' deki ABC kalıbı gibi) bulup Sekil değişkenine atama işlemi


    
    def AnahtarMi(soru): # tur döndüren fonksiyon

        cumle = soru.split()
        # dosyadaki anahtar kelimeleri diziye aktarma
        anahtarKelimeler = ["ikizkenar","eşkenar","eskenar","çeşitkenar","cesitkenar","düzgün","duzgun","dik","üçgen","ucgen","diküçgen","dikucgen"]
        #with open("anahtar.txt", "r") as f:
        #    anahtarKelimeler = f.read().splitlines() # satır satır okuyup aktarma

        aKel = []
        for anahtar in anahtarKelimeler:

            for kelime in cumle:
                               
                if kelime == anahtar:
                    aKel.append(kelime)

        k = len(aKel) - 1
        for i in aKel:
            a = 0

            while(k<0): # listenin elemanmalarını tersine sıralar
                gecici = aKel[k]
                aKel[k] = i
                aKel[a] = gecici
                k-=1

        tur = ""
        t = 0
        while(t != len(aKel) ): #aKel listesini birleştir

            tur = tur + aKel[t]
            t+=1

        return tur          # Şeklin türünü ve özelliğini belirten kelimeleri bulma 
                                     # Soru kalıbından şeklin türünü bulup tur değişkenine atıyor. ('ABC bir ikizkenar üçgen' cümlesindeki tur = ikizkenarüçgen olur)

    def KalipYaz(soru):

        kalipList = []
    
        sag = SagBul(soru)
        sol = SolBul(soru)
    
        i = 0
        j = 0
        while (j < len(sag)):

            if(len(sol[i])<3): # kenar işaretinde | olmadığı durumda ekleme yap
                if(len(sag[j])<3 and sag[j] not in sayilar):
                    kalip = "|"+sol[i]+"|"+" "+ sol[i+1] +" "+"|"+ sag[j]+"|"
                else:
                    kalip = "|"+sol[i]+"|"+" "+ sol[i+1] +" "+ sag[j]
            else:
                kalip = sol[i] +" "+ sol[i+1] +" "+ sag[j]
            kalipList.append(kalip) # kalipları Kalipliste ekleme

            j += 1
            i += 2

        return kalipList         # Bulduğu tüm kalıpları kalıplistesine ekleme 

    def BoslukSay(soru):
        a=0
        b=0
        c=0
        for i in soru:
            a+=1
            if i == "=":
                b += 1  
            if i == "/":
                c = a
            if soru[c+1]== "/":
                    b += 1  
            if i == "⊥":
                b += 1  
        return b          # sorudaki boşlukları saymak için fonksiyon (kalıpların bazılarında boşluk varsa boşluk koymasın diye gerekli)


    def BoslukKoy(soru,b,k):
  

        while (k < b):
            a=-1
            for i in soru:
                a +=1
                if (i == "=" ):
                    if soru[a-1] != " ":
                        soru = soru[:a] + " " + soru[a] + soru[a+1:]
                        a += 1
                    if soru[a+1] != " ":
                        soru = soru[:a] + soru[a] + " " + soru[a+1:]
                        a += 1


                if (i == "⊥") :
                   if soru[a-1] != " ":
                       soru = soru[:a] + " " + soru[a] + soru[a+1:]
                       a += 1
                   if soru[a+1] != " ":
                       soru = soru[:a] + soru[a] + " " + soru[a+1:]
                       a += 1



                if i == "/":
                    if soru[a+1] == "/":
                        if soru[a-1] != " ":
                            soru = soru[:a] + " " + soru[a] + soru[a+1:]
                            a += 1

                    if soru[a-1] == "/":                                   
                        if soru[a+1] != " ":
                            soru = soru[:a] + soru[a] + " " + soru[a+1:]
                            a += 1
                   
                    

                k +=1
                BoslukKoy(soru,b,k)
        return soru      # kalıplar arasına boşluk koymak için kullanılan fonksiyon


    def SolBul(soru): # operatorun solundaki kelimeyi algilamaya yarar
        a = 0 # = operatorune kadar gidip kacinci indekste oldugunu anlamamizi saglayan degisken
        b = 0 # = e kadar kac tane bosluk oldugunu saymamıza yarayan degisken
        c = 0 # boslukları saymaya yarayan baska bir degisken. b ye esit olana kadar sayıyor aynı surede d degiskeni de tum ındekslerı sayıyor bu sayede a ile d arasindaki harfleri elde edebiliyoruz
        d = 0 # gerekli olan kelimenin baslangicini veya sonunu temsil eden degisken
        sol = []
        opr = []
        m = 0
        for i in soru:
            a += 1
            if i == " ":
                b += 1 # bosluklari sayar
      
            if i == "=": # i operatore esit oldugunda dibinde bosluk olup olmadiginin kontrolu yapilir
                b -= 1 # esitse bir önceki bosluga erisim saglayabilmek icin b bir azaltilir
            
                for j in soru:
                    d += 1
                
                    if j == " ":
                        c += 1
                   
                        if c == b: # c'nin indeksi b'ye esit olana kadar d indeksi arttırlır bu sayede ilgili boslugun indeksi d de tutulur
                            temp = soru[d:a-2]
                            sol.append(temp)
                            sol.append("=")
                            b +=1
                            d = 0
                            c = 0
                            break


            if i == "/": # i operatore esit oldugunda dibinde bosluk olup olmadiginin kontrolu yapilir
                m = a-1
                if soru[m+1] == "/":

                    b -= 1 # esitse bir önceki bosluga erisim saglayabilmek icin b bir azaltilir

           
                    for j in soru:
                        d += 1
                
                        if j == " ":
                            c += 1
                   
                            if c == b: # c'nin indeksi b'ye esit olana kadar d indeksi arttırlır bu sayede ilgili boslugun indeksi d de tutulur
                                temp = soru[d:a-2]
                                sol.append(temp)
                                sol.append("//")
                                b +=1
                                d = 0
                                c = 0
                                break


            if i == "⊥": # i operatore esit oldugunda dibinde bosluk olup olmadiginin kontrolu yapilir
                b -= 1 # esitse bir önceki bosluga erisim saglayabilmek icin b bir azaltilir
            
                for j in soru:
                    d += 1
                
                    if j == " ":
                        c += 1
                   
                        if c == b: # c'nin indeksi b'ye esit olana kadar d indeksi arttırlır bu sayede ilgili boslugun indeksi d de tutulur
                            temp = soru[d:a-2]
                            sol.append(temp)
                            sol.append("⊥")
                            b +=1
                            d = 0
                            c = 0
                            break

                        
        return sol             # eşitlik, diklik ve paralellik gibi işaretlerin sol tarafındaki kenar, açı bilgisini bulmak için fonksiyon
            

    def SagBul(soru): 
        a = 0 
        b = 0
        c = 0 
        d = 0
        m = 0
        sag = []
   

        for i in soru:
            a += 1
        
            if i == " ":
                b += 1

            if i == "=":           
                a += 1
                b += 2

                for j in soru:
                    d += 1
                    
                    if j == " ":
                        c += 1
                        
                        if c == b:
                            temp = soru[a:d-1]
                            sag.append(temp)

                            a -=1
                            b -=2
                            d = 0
                            c = 0
                            break


            if i == "/":
                m = a-1
                if soru[m+1] == "/":
                    a += 1
                    b += 2

                    for j in soru:
                        d += 1
                    
                        if j == " ":
                            c += 1
                        
                            if c == b:
                                temp = soru[a+1:d-1]
                                sag.append(temp)

                                a -=1
                                b -=2
                                d = 0
                                c = 0
                                break


            if i == "⊥":           
                a += 1
                b += 2

                for j in soru:
                    d += 1
                    
                    if j == " ":
                        c += 1
                        
                        if c == b:
                            temp = soru[a:d-1]
                            sag.append(temp)

                            a -=1
                            b -=2
                            d = 0
                            c = 0
                            break


        return sag             # eşitlik, diklik ve paralellik gibi işaretlerin sağ tarafındaki kenar, açı bilgisini bulmak için fonksiyon

 
                         ########## KALIPLARI BÖLMEK İÇİN YAZILAN KOD ###########


    def KalipYardFonk(kaliplar): # kalıplar listesinin uzunluğuna göre işlem yapar.

        if len(kaliplar) > 1:    # kaliplar listesinde birden fazla kalip varsa
        
            for kalip in kaliplar:
                KalipAyirmaIslemi(kalip)
            
        else:
            KalipAyirmaIslemi(kaliplar)      # Kalıplar listesinin uzunluğuna göre işlem yapan yardımcı fonksiyon (birden fazlaysa kalıpları kalıp ayırma fonksiyonuna tek tek gönderme işini yapar)
            

    def KalipAyirmaIslemi(kalip): # kalıpları kalip1List ve kalip2List ayırır.

        bol = kalip.split('=')
        bolSag = bol[1]
        bolSag = bolSag.replace(" ","") # gereksiz boşlukları temizler
        a = 0
        op = ["+","-"]
        for i in bolSag:
           
            if  ((i == "x" and len(bolSag) < 2 ) or i == "?"): # |AB|= ? veya |AB|=x kalıbından |AB| kalıbını bırakmak için
                kalip = bol[0]+ " = "+bol[1] 
                kalip1List.append(kalip)    # kenarın veya açının 1. indexi bilinmeyen olarak işarelensin diye kalıp1 listesine de ekleniliyor
                isaret = "|[]()ms"
                for i in bol[0]:
                    if i in isaret:
                        bol[0] = bol[0].replace(i,"")
                sorulan.append(bol[0])
                return sorulan
                break

            if (i =='+'or i=='-'): # kalıpta + - var ise kalıp2 ye ekle

                harfli = bolSag.split(i)
                otaraf = harfli[0] # operatörden önceki taraf
                staraf = harfli[1] # operatörden sonraki taraf
                kalip = bol[0] + " = " + otaraf + " "+ i + " " + staraf
                kalip2List.append(kalip) #harfli kalıpların olduğu liste
                return kalip2List
                break
            a+=1
        kalip = bol[0]+ " = "+ bol[1]
        kalip1List.append(kalip) # normal kalıpların olduğu liste
        return kalip1List     # kalıpları kalip1List, kalip2List ve sorulan listelerine ayırır.
                                         # sorulan listesindeki kalıpların tümü kalıp1List'e de eklenir.

                      ##########  KALIPLARI VE ANAHTAR KELİMELERİ KULLANAN KOD ( 2. KISIM )  ##########



    ToplamKorAList = []        # kenar ve açı isimleri listesi
    ToplamKatsayiList = []     # katsayıların listesi

    def ucgen(sekil, tur, kalip):

        print("KALIPLAR:",kalip)
        print(" ")
                                # Seklin kose sayisi kadar kenar ve aci olusturulur
        kenar01 = ["s",1,"k0","h"]  # Her kenarin veya acinin 4 indexi olur [ oranti , sayisal_deger , katsayi , koselere_gore_isim ]
        kenar12 = ["s",1,"k1","h"]
        kenar20 = ["s",1,"k2","h"]

        kenar01.insert(0,(sekil[0]+sekil[1])) # sekil degiskeninde verilen harflere gore kenar ve acilarin kendilerine ait listelerine 4. indexler eklenir
        kenar12.insert(0,(sekil[1]+sekil[2]))
        kenar20.insert(0,(sekil[2]+sekil[0]))

        aci012 = ["s",1,"a0","h"]
        aci120 = ["s",1,"a1","h"]
        aci201 = ["s",1,"a2","h"]

        aci012.insert(0,(sekil[0]+sekil[1]+sekil[2]))
        aci120.insert(0,(sekil[1]+sekil[2]+sekil[0]))
        aci201.insert(0,(sekil[2]+sekil[0]+sekil[1]))
        KorA = [kenar01,kenar12,kenar20,aci012,aci120,aci201]

        # >>yazdir<< Soruda verilenleri analiz ederek elde edilen bilgiler ekrana yazdirilir
        def yazdir(): 

            print("")
            print("ANALIZLER")
            print("")
            print("[0]=[1]=[2]=[3]=[4]")
            print(kenar01[0],"=",kenar01[1],"=",kenar01[2],"=",kenar01[3],"=",kenar01[4])
            print(kenar12[0],"=",kenar12[1],"=",kenar12[2],"=",kenar12[3],"=",kenar12[4])
            print(kenar20[0],"=",kenar20[1],"=",kenar20[2],"=",kenar20[3],"=",kenar20[4])
            print(" ")
            print(aci012[0],"=",aci012[1],"=",aci012[2],"=",aci012[3],"=",aci012[4])
            print(aci120[0],"=",aci120[1],"=",aci120[2],"=",aci120[3],"=",aci120[4])
            print(aci201[0],"=",aci201[1],"=",aci201[2],"=",aci201[3],"=",aci201[4])        
            print(" ")

        # >>KorATani<< Parametre olarak girilen değerin (BC gibi) hangi kenar veya açıyı temsil ettiğini belirler
        def KorATani(taninmayan): 
            for i in KorA:
                if (i[0] == taninmayan):
                    taninan = i
                    return taninan

        # Eger kenarlar arasinda 3'lu oranti varsa (örneğin |AB| = 3|BC| , 2|BC| = 3|CA|) katsayilar arasinda tutarsizlik olmamasi icin ortak katlari alinir 
        def OrtakKatUygula(isimlist, katsayilist): 
            tut=0
            i=0
            j=0
            while i < len(isimlist):
                j= i+1
                while j < len(isimlist):            # isimListteki i. indexi iden sonraki elemanlarla karşılaştırıyor
                    if(isimlist[i] == isimlist[j]): #  eğer aynı eleman var ise 
                        tut=int(katsayilist[i]) 
                        if(i%2==0):                 # 3'lü kalıplar 2'şerli kalıp olacak şekilde alınıyor bu yüzden i. index çift ise bu sonraki index ile, tek ise öncekiyle orantılıdır (j için de aynı durum geçerlidir)
                            katsayilist[i] = int(katsayilist[j]) * int(katsayilist[i]) 
                            katsayilist[i+1] = int(katsayilist[j]) * int(katsayilist[i+1])
                        if(i%2!=0):
                            katsayilist[i] = int(katsayilist[j]) * int(katsayilist[i])
                            katsayilist[i-1] = int(katsayilist[j]) * int(katsayilist[i-1])
                        if(j%2==0):
                            katsayilist[j] = tut * int(katsayilist[j])
                            katsayilist[j+1] = tut * int(katsayilist[j+1])
                        if(j%2!=0):
                            katsayilist[j] = tut * int(katsayilist[j])
                            katsayilist[j-1] = tut * int(katsayilist[j-1])
                    j+=1
                i +=1
            i=0
            while i < len(isimlist):
                KorATani(isimlist[i])[2] = katsayilist[i]
                i+= 1    

        #Tüm kalıplar üzerinde dolaşılarak katsayılar belirlenir ve gerekli işlemlerden geçirildikten sonra işleme alınmak üzere veritabanında tutulur
        def KatsayiIsle():
            KorAList = []      # kenar ve açı isimlerinin listesi
            KatsayiList = []   # katsayıların listesi
            a = 0
            i = 0
            while (i < len(kalip)): # kalip listeseindeki her eleman icin islem yapılmasini saglayan dongu
                temp = kalip[a]
                a += 1
                b = -1
                for j in temp:                                                          # Bir kalip icerisindeki karakterlerde for dongusu ile gezinilir
                    b +=1                                                               # --KENAR ISLEMLERI--
                    if (j == "="):    
                        if(temp[b-2] == "|" and temp[len(temp)-1] == "|"):              # Operatorun hem sağında hem solunda birer kenar varsa    
                            if(len(KorAList)<2):
                                KorAList.append(temp[b-4]+temp[b-3])
                                KatsayiList.append(temp[:b-5])
                            else:
                                KorAList[0] = (temp[b-4]+temp[b-3])
                                KatsayiList[0] = (temp[:b-5])

                            if(temp[0] == "|"):                                         # eğer kalip | ile basliyorsa katsayi 1 e esitlenir
                                KatsayiList[0] = 1

                         
                            if(len(KorAList)<2):
                                KorAList.append(temp[len(temp)-3:len(temp)-1])
                                KatsayiList.append(temp[b+2:len(temp)-4])
                            else:
                                KorAList[1] = (temp[len(temp)-3:len(temp)-1])
                                KatsayiList[1] = (temp[b+2:len(temp)-4])
                            
                            if(temp[b+2] == "|"):
                                KatsayiList[1] = 1
              
                            KorATani(KorAList[0])[2] = KatsayiList[0]    
                            KorATani(KorAList[1])[2] = KatsayiList[1]

                            ToplamKorAList.append(KorAList[0])
                            ToplamKorAList.append(KorAList[1])
                            ToplamKatsayiList.append(KatsayiList[0])
                            ToplamKatsayiList.append(KatsayiList[1])
                                               

                            if ((KorAList[0] == kenar01[0] and KorAList[1] == kenar12[0]) or (KorAList[1] == kenar01[0] and KorAList[0] == kenar12[0])):
                                if (kenar01[3] == kenar20[3] or kenar12[3] == kenar20[3]):                            
                                    kenar12[3] = kenar01[3]
                                    kenar20[3] = kenar01[3]
                                else:
                                    kenar12[3] = kenar01[3]
                                

                            if ((KorAList[0] == kenar12[0] and KorAList[1] == kenar20[0]) or (KorAList[1] == kenar12[0] and KorAList[0] == kenar20[0])):
                                if (kenar01[3] == kenar20[3] or kenar12[3] == kenar01[3]):                            
                                    kenar01[3] = kenar12[3]
                                    kenar20[3] = kenar12[3]
                                else:
                                    kenar20[3] = kenar12[3]
                                

                            if ((KorAList[0] == kenar20[0] and KorAList[1] == kenar01[0]) or (KorAList[1] == kenar20[0] and KorAList[0] == kenar01[0])):
                                if (kenar01[3] == kenar12[3] or kenar12[3] == kenar20[3]):    
                                    kenar12[3] = kenar20[3]
                                    kenar01[3] = kenar20[3]
                                else:
                                    kenar01[3] = kenar20[3]
                               
                                                                                         # --AÇI İŞLEMLERİ--
                        if ( temp[b-2] == ")" and temp[len(temp)-1] == ")"):             # Operatörün hem sağında hem de solunda açı var ise

                            if len(KorAList) < 2:
                                KorAList.append(temp[b-5:b-2])
                                KorAList.append(temp[len(temp)-4:len(temp)-1])
                                KatsayiList.append(temp[:b-7])
                                KatsayiList.append(temp[b+2:len(temp)-6])
                            
                            else:
                               KorAList[0] = (temp[b-5:b-2])
                               KatsayiList[0] = (temp[:b-7])
                               KorAList[1] = (temp[len(temp)-4:len(temp)-1])
                               KatsayiList[1] = (temp[b+2:len(temp)-6])

                            if (temp[0] == 'm' or temp[0] == 's') :
                                KatsayiList[0] = 1

                            if (temp[b+2] == 'm' or temp[b+2] == 's'):
                                KatsayiList[1] = 1

                            KorATani(KorAList[0])[2] = KatsayiList[0]                   # Açının bulunduğu açı değişkeninin 2. indexine katsayı ekleme işlemi
                            KorATani(KorAList[1])[2] = KatsayiList[1]

                            ToplamKorAList.append(KorAList[0])
                            ToplamKorAList.append(KorAList[1])
                            ToplamKatsayiList.append(KatsayiList[0])
                            ToplamKatsayiList.append(KatsayiList[1])

                       
                            if ((KorAList[0] == aci012[0] and KorAList[1] == aci120[0]) or (KorAList[1] == aci012[0] and KorAList[0] == aci120[0])):
                                if (aci012[3] == aci201[3] or aci120[3] == aci201[3]):                            
                                    aci120[3] = aci012[3]
                                    aci201[3] = aci012[3]
                                else:
                                    aci120[3] = aci012[3]
              

                            if ((KorAList[0] == aci120[0] and KorAList[1] == aci201[0]) or (KorAList[1] == aci120[0] and KorAList[0] == aci201[0])):
                                if (aci012[3] == aci201[3] or aci120[3] == aci012[3]):                            
                                    aci012[3] = aci120[3]
                                    aci201[3] = aci120[3]


                                else:
                                    aci201[3] = aci120[3]

                            if ((KorAList[0] == aci201[0] and KorAList[1] == aci012[0]) or (KorAList[1] == aci201[0] and KorAList[0] == aci012[0])):
                                if (aci012[3] == aci120[3] or aci120[3] == aci201[3]):    
                                    aci120[3] = aci201[3]
                                    aci012[3] = aci201[3]
                                else:
                                    aci012[3] = aci201[3]
                i+=1 
            
        # buraya bak bir ara  Tüm kalıplar üzerinde dolaşılarak sayısal veya harfli değerler belirlenir ve veritabanına işlenir (operatör = yerine ⊥ ise ilgili açı 90 a eşitlenir)
        def SayiveHarfIsle():   
            KorAList = []
            SayiList = []
            DiklikList = []
            sayilar = "0123456789"  # eşitliğin sağ ve sol tarafının int olduğunu kontrol etmek için oluşturulan liste
            harfler = "+-x"
            a = 0
            i = 0
            while (i < len(kalip)): # kalip listeseindeki her eleman icin islem yapılmasini saglayan dongu
                temp = kalip[a]
                a += 1
                b = -1
                for j in temp:                                                          # Bir kalip icerisindeki karakterlerde for dongusu ile gezinilir
                    b +=1                                                               # --KENAR ISLEMLERI--            temp = kalip[a]

                    if (j == "⊥"):
                        if (temp[b-2] == "]"):                                          # Islem yapilacak kenarlar belirlenir
                            DiklikList.append(temp[b-4]+temp[b-3])
                            DiklikList.append(temp[b+3]+temp[b+4])
                        else:
                            DiklikList.append(temp[b-3]+temp[b-2])
                            DiklikList.append(temp[b+2]+temp[b+3])
                    
                        if((DiklikList[0] == kenar01[0] and DiklikList[1] == kenar12[0]) or(DiklikList[1] == kenar01[0] and DiklikList[0] == kenar12[0])):
                            aci012[1] = 90
                            print(DiklikList[0] + " kenarı ile " + DiklikList[1] + " kenarı birbirine dik olduğu için " + aci012[0] + " açısı 90 derecedir.")
                        if((DiklikList[0] == kenar12[0] and DiklikList[1] == kenar20[0]) or(DiklikList[1] == kenar12[0] and DiklikList[0] == kenar20[0])):
                            aci120[1] = 90
                            print(DiklikList[0] + " kenarı ile " + DiklikList[1] + " kenarı birbirine dik olduğu için " + aci120[0] + " açısı 90 derecedir.")
                        if((DiklikList[0] == kenar20[0] and DiklikList[1] == kenar01[0]) or(DiklikList[1] == kenar20[0] and DiklikList[0] == kenar01[0])):
                            aci201[1] = 90
                            print(DiklikList[0] + " kenarı ile " + DiklikList[1] + " kenarı birbirine dik olduğu için " + aci201[0] + " açısı 90 derecedir.")


                    if (j == "="):
                        sag_taraf = temp[b+2:len(temp)]
                        sol_taraf = temp[0:b-1]
                        for k in sol_taraf:               # eşitliğin sol tarafını sayı olup olmadığını kontrol ediyor, sayı ise True döndürüyor değilse False
                            if k not in sayilar:
                                sol_sayidir = False
                                break
                            else:
                                sol_sayidir = True

                        for k in sag_taraf:              # sağ tarafı kontrol ediyor hepsi sayıysa True döndürüyor değilse False  
                            if k not in sayilar:
                                sag_sayidir = False
                                break
                            else:
                                sag_sayidir = True
                        for z in sag_taraf:              # sag tarafın harfli kontrolü
                            if z in harfler:
                                sag_harflidir = True
                                break
                            else:
                                sag_harflidir = False

                        for z in sol_taraf:              # sol tarafın harfli kontrolü
                            if z in harfler:
                                sol_harflidir = True
                                break
                            else:
                                sol_harflidir = False

                        if sag_sayidir == True :
                            if len(sol_taraf) < 5:  # kenar ise
                                if(len(KorAList)<1):                                                                                 
                                    KorAList.append(temp[b-4]+temp[b-3])
                                    SayiList.append(temp[b+2:])
                                    print(str(KorAList[-1]) + " kenarının uzunluğu = " + str(SayiList[-1]))
                                else:
                                    KorAList[0] = (temp[b-4]+temp[b-3])
                                    SayiList[0] = (temp[b+2:])  
                                    print(str(KorAList[-1]) + " kenarının uzunluğu = " + str(SayiList[-1]))
                            else:                   # açı ise
                                if(len(KorAList)<1):                                                      # Eğer esitligin sağ tarafinda kenar yoksa bir sayi var demektir                            
                                    KorAList.append(temp[b-5:b-2])
                                    SayiList.append(temp[b+2:])
                                    print(str(KorAList[-1]) + " açısının ölçüsü = " + str(SayiList[-1]))
                                else:
                                    KorAList[0] = (temp[b-5:b-2])
                                    SayiList[0] = (temp[b+2:])
                                    print(str(KorAList[-1]) + " açısının ölçüsü = " + str(SayiList[-1]))
                               
                            KorATani(KorAList[0])[1] = SayiList[0]
                        
                        if sol_sayidir == True:     
                            if len(sag_taraf) < 5: 
                                if(len(KorAList)<1):                                                      
                                    KorAList.append(temp[len(temp)-3:len(temp)-1])
                                    SayiList.append(temp[:b-1]) 
                                    print(str(KorAList[-1]) + " kenarının uzunluğu = " + str(SayiList[-1]))
                                else:
                                    KorAList[0] = (temp[len(temp)-3:len(temp)-1])
                                    SayiList[0] = (temp[:b-1]) 
                                    print(str(KorAList[-1]) + " kenarının uzunluğu = " + str(SayiList[-1]))

                            else:
                                if(len(KorAList)< 1):
                                    KorAList.append(temp[len(temp)-4:len(temp)-1])
                                    SayiList.append(temp[:b-1])
                                    print(str(KorAList[-1]) + " açısının ölçüsü = " + str(SayiList[-1]))
                                else:
                                    KorAList[0] = (temp[len(temp)-4:len(temp)-1])
                                    SayiList[0] = (temp[:b-1]) 
                                    print(str(KorAList[-1]) + " açısının ölçüsü = " + str(SayiList[-1]))
           

                            KorATani(KorAList[0])[1] = SayiList[0]

                        if sag_harflidir == True :
                            if len(sol_taraf) < 5:  
                                if(len(KorAList)<1):                                                                               
                                    KorAList.append(temp[b-4]+temp[b-3])
                                    SayiList.append(temp[b+2:])
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " kenar uzunlugu istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " kenar uzunlugu " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                                else:
                                    KorAList[0] = (temp[b-4]+temp[b-3])
                                    SayiList[0] = (temp[b+2:])  
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " kenar uzunlugu istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " kenar uzunlugu " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                            else:                   
                                if(len(KorAList)<1):                                                                             
                                    KorAList.append(temp[b-5:b-2])
                                    SayiList.append(temp[b+2:])
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " açısı istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " açısı " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                                else:
                                    KorAList[0] = (temp[b-5:b-2])
                                    SayiList[0] = (temp[b+2:])
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " açısı istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " açısı " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")

                            KorATani(KorAList[0])[4] = SayiList[0]

                        if sol_harflidir == True:
                            if len(sag_taraf) < 5: 
                                if(len(KorAList)<1):                                                      
                                    KorAList.append(temp[len(temp)-3:len(temp)-1])
                                    SayiList.append(temp[:b-1]) 
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " kenar uzunlugu istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " kenar uzunlugu " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                                else:
                                    KorAList[0] = (temp[len(temp)-3:len(temp)-1])
                                    SayiList[0] = (temp[:b-1]) 
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " kenar uzunlugu istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " kenar uzunlugu " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                            else:
                                if(len(KorAList)< 1):
                                    KorAList.append(temp[len(temp)-4:len(temp)-1])
                                    SayiList.append(temp[:b-1])
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " açısı istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " açısı " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")
                                else:
                                    KorAList[0] = (temp[len(temp)-4:len(temp)-1])
                                    SayiList[0] = (temp[:b-1])
                                    if(str(SayiList[-1])== "x"):
                                        print("Bizden "+str(KorAList[-1]) + " açısı istenilmektedir.")
                                    else:
                                        print(str(KorAList[-1]) + " açısı " + str(SayiList[-1]) + " olarak verilmiştir ve bizden bilinmeyen değer istenilmektedir.")

                            KorATani(KorAList[0])[4] = SayiList[0]                       
                i+=1 

        #Parametre olarak girilen bilinmeyenli kalıp parçalanır (2x - 30   --->  2,x,-,30) 
        def Parcala(butun):  
            sayilar = "0123456789"
            a=0
            op = "yok"
            for i in butun:            
                if(i == "+" or i == "-"):
                    op = i
                    if butun[a-2] not in sayilar :       # 1. kısım int değer değilse 2x - 10
                        harflilist = ["s","x","o","i"]
                        s_t = (butun[:a-2])  
                        i_t = (butun[a+2:])
                        xyz = butun[a-2]                
                        if(s_t == ""):          
                            s_t = 1   
                        harflilist[0] = s_t  # x ön sayısı
                        harflilist[1] = xyz  # 
                        harflilist[2] = op    #+-
                        harflilist[3] = i_t   #integer 
                        return harflilist
                        break
                                            
                    else:              # 1. kısım int değer ise 10 - 2x
                        harflilist = ["i","o","s","x"]
                        s_t = butun[a+1:len(butun)-1]
                        i_t = butun[:a-1]
                        xyz = butun[len(butun)-1]
                        if (s_t == " " or s_t == ""):
                            s_t = 1
                        harflilist[0] = i_t
                        harflilist[1] = op
                        harflilist[2] = s_t
                        harflilist[3] = xyz                  
                        return harflilist
                        break                                            
                        
                a+=1
        
            if(op == "yok"):
                harflilist = ["s","x","o","i"]
                i_t = 0  
                s_t = (butun[:len(butun)-1])
                xyz = butun[len(butun)-1]
                if(s_t == ""):
                    s_t = 1         

                harflilist[0] = s_t
                harflilist[1] = xyz
                harflilist[2] = ""
                harflilist[3] = i_t
                return harflilist
                         
        #İşlemler yapıldıktan sonra elde edilen bilgiler kullanılarak veritabanındaki boşluklar doldurulmaya çalışılır
        def BoslukDoldur():     
            i, j = 0, 0
            #print(KorA[1][0])
            while i < len(KorA):
                harfli = "xyzab"
                j = i+1
                while j < len(KorA):
                    if (KorA[i][3] == KorA[j][3] and KorA[i][1] != "s" and KorA[j][1] == "s"):
                        KorA[j][1] = int(KorA[i][1]) * (float(KorA[i][2])/float(KorA[j][2]))
                        OranYazdir(KorA[i],KorA[j])
                    
                    if (KorA[i][3] == KorA[j][3] and KorA[i][1] == "s" and KorA[j][1] != "s"):
                        KorA[i][1] = int(KorA[j][1]) * (float(KorA[j][2])/float(KorA[i][2]))
                        OranYazdir(KorA[j],KorA[i])                    
                
                    if (KorA[i][3] == KorA[j][3] and KorA[i][4] == "h" and KorA[j][4] != "h" ):
                        if(Parcala(KorA[j][4])[2] != "" and (Parcala(KorA[j][4])[1] in harfli)):  # 2x-10 kalıbı için
                            KorA[i][4] = str(float(Parcala(KorA[j][4])[0])*(float(KorA[j][2])/float(KorA[i][2]))) +  str(Parcala(KorA[j][4])[1]) + " " + str(Parcala(KorA[j][4])[2]) + " "+ str(float(Parcala(KorA[j][4])[3])*(float(KorA[j][2])/float(KorA[i][2])))
                            
                            print(str(KorA[j][0]) + " açısının "+ str(KorA[j][2]) +" katı " + str(KorA[i][0]) + " açısının "+str(KorA[i][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[i][0]) + " = " + str(KorA[i][4]) + " olur.") 
                            if(KorA[i][1] != 's'):
                                if(Parcala(KorA[i][4])[2] == "+"):
                                    bilinmeyen = (float(KorA[i][1]) - float(Parcala(KorA[i][4])[3]))/(float(Parcala(KorA[i][4])[0]))
                                    print(KorA[i][0] + " => "+KorA[i][4]+" = "+ str(KorA[i][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[i][4])[0]+Parcala(KorA[i][4])[1]+ " = "+ str(float(KorA[i][1]) - float(Parcala(KorA[i][4])[3])))
                                    print("=> "+ Parcala(KorA[i][4])[1]+ " = "+ str(bilinmeyen)+ "değeri bulunur.")
                                else:
                                    bilinmeyen = (float(KorA[i][1]) + float(Parcala(KorA[i][4])[3]))/ (float(Parcala(KorA[i][4])[0]))
                                    print(KorA[i][0] + " => "+KorA[i][4]+" = "+ str(KorA[i][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[i][4])[0]+Parcala(KorA[i][4])[1]+ " = "+ str(float(KorA[i][1]) + float(Parcala(KorA[i][4])[3])))
                                    print("=> "+ Parcala(KorA[i][4])[1]+ " = "+ str(bilinmeyen)+ "değeri bulunur.")
                            
                        elif(Parcala(KorA[j][4])[2] == "" and (Parcala(KorA[j][4])[1] in harfli)): # x, 2x vb kalıplar için                        
                            KorA[i][4] = str((float(Parcala(KorA[j][4])[0])*(float(KorA[j][2])/float(KorA[i][2])))) +  str(Parcala(KorA[j][4])[1])
                           
                            print(str(KorA[j][0]) + " açısının "+ str(KorA[j][2]) +" katı " + str(KorA[i][0]) + " açısının "+str(KorA[i][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[i][0]) + " = " + str(KorA[i][4]) + " olur.") 
                            if(KorA[i][1] != 's'):                            
                                bilinmeyen = (float(KorA[i][1]))/(float(Parcala(KorA[i][4])[0]))
                                print(KorA[i][0] + " => "+KorA[i][4]+" = "+ str(KorA[i][1])+ " eşitliğinden")
                                print("=> " +Parcala(KorA[i][4])[0]+Parcala(KorA[i][4])[1]+ " = "+ str(float(KorA[i][1])))
                                print("=> "+ Parcala(KorA[i][4])[1]+ " = "+ str(bilinmeyen)+ "değeri bulunur.")
                           
                        else:                                                                      # 10 - 2x kalıbı için
                            KorA[i][4] = str(float(Parcala(KorA[i][4])[0])*(float(KorA[j][2])/float(KorA[i][2]))) + " " + str(Parcala(KorA[i][4])[1]) + " " + str(float(Parcala(KorA[i][4])[2])*(float(KorA[i][2])/float(KorA[j][2]))) + Parcala(KorA[i][4])[3]
                            
                            print(str(KorA[j][0]) + " açısının "+ str(KorA[j][2]) +" katı " + str(KorA[i][0]) + " açısının "+str(KorA[i][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[i][0]) + " = " + str(KorA[i][4]) + " olur.")                  
                    
                            if(KorA[i][1] != 's'):
                                if(Parcala(KorA[i][4])[1] == "+"):
                                    bilinmeyen = (-float(KorA[i][1])+ float(Parcala(KorA[i][4])[0]))/(float(Parcala(KorA[i][4])[2]))
                                    print(KorA[i][0] + " => "+KorA[i][4]+" = "+ str(KorA[i][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[i][4])[2]+Parcala(KorA[i][4])[3]+ " = "+ str(float(Parcala(KorA[i][4])[0]) - float(KorA[i][1])))
                                    print("=> "+ Parcala(KorA[i][4])[2]+ " = "+ str(bilinmeyen)+ "değeri bulunur.")
                                else:
                                    bilinmeyen = (float(KorA[i][1]) - float(Parcala(KorA[i][4])[0]))/(float(Parcala(KorA[i][4])[2]))
                                    print(KorA[i][0] + " => "+KorA[i][4]+" = "+ str(KorA[i][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[i][4])[2]+Parcala(KorA[i][4])[3]+ " = "+ str(float(Parcala(KorA[i][4])[0]) + float(KorA[i][1])))
                                    print("=> "+ Parcala(KorA[i][4])[2]+ " = "+ str(bilinmeyen)+ "değeri bulunur.")
                    
                    if (KorA[i][3] == KorA[j][3] and KorA[i][4] != "h" and KorA[j][4] == "h"):  
                        if (Parcala(KorA[i][4])[2] != "" and (Parcala(KorA[i][4])[1] in harfli)):
                            KorA[j][4] = str(float(Parcala(KorA[i][4])[0])*(float(KorA[i][2])/float(KorA[j][2]))) +  Parcala(KorA[i][4])[1] + " " +Parcala(KorA[i][4])[2] + " "+ str(float(Parcala(KorA[i][4])[3])*(float(KorA[i][2])/float(KorA[j][2])))
                        
                            print(str(KorA[i][0]) + " açısının "+ str(KorA[i][2]) +" katı " + str(KorA[j][0]) + " açısının "+str(KorA[j][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[j][0]) + " = " + str(KorA[j][4]) + " olur.")
                            if(KorA[j][1] != 's'):
                                if(Parcala(KorA[j][4])[2] == "+"):
                                    bilinmeyen = (float(KorA[j][1]) - float(Parcala(KorA[j][4])[3]))/(float(Parcala(KorA[j][4])[0]))
                                    print(KorA[j][0] + " => "+KorA[j][4]+" = "+ str(KorA[j][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[j][4])[0]+Parcala(KorA[j][4])[1]+ " = "+ str(float(KorA[j][1]) - float(Parcala(KorA[j][4])[3])))
                                    print("=> "+ Parcala(KorA[j][4])[1]+ " = "+ str(bilinmeyen)+ " değeri bulunur.")
                                else:
                                    bilinmeyen = (float(KorA[j][1]) + float(Parcala(KorA[i][4])[3]))/ (float(Parcala(KorA[i][4])[0]))
                                    print(KorA[i][0] + " => "+KorA[j][4]+" = "+ str(KorA[j][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[i][4])[0]+Parcala(KorA[i][4])[1]+ " = "+ str(float(KorA[j][1]) + float(Parcala(KorA[i][4])[3])))
                                    print("=> "+ Parcala(KorA[i][4])[1]+ " = "+ str(bilinmeyen)+ " değeri bulunur.")

                        elif(Parcala(KorA[i][4])[2] == "" and (Parcala(KorA[i][4])[1] in harfli)): # x, 2x vb kalıplar için
                            KorA[j][4] = str((float(Parcala(KorA[i][4])[0])*(float(KorA[i][2])/float(KorA[j][2])))) +  str(Parcala(KorA[i][4])[1])
                        
                            print(str(KorA[i][0]) + " açısının "+ str(KorA[i][2]) +" katı " + str(KorA[j][0]) + " açısının "+str(KorA[j][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[j][0]) + " = " + str(KorA[j][4]) + " olur.")
                            if(KorA[j][1] != 's'):                            
                                bilinmeyen = (float(KorA[j][1]))/(float(Parcala(KorA[j][4])[0]))
                                print(KorA[i][0] + " => "+KorA[j][4]+" = "+ str(KorA[j][1])+ " eşitliğinden")
                                print("=> " +Parcala(KorA[j][4])[0]+Parcala(KorA[j][4])[1]+ " = "+ str(float(KorA[j][1])))
                                print("=> "+ Parcala(KorA[j][4])[1]+ " = "+ str(bilinmeyen)+ " değeri bulunur.")
                        else:
                            KorA[j][4] = str(float(Parcala(KorA[i][4])[0])*(float(KorA[i][2])/float(KorA[j][2]))) + " " + Parcala(KorA[i][4])[1] + " " + str(float(Parcala(KorA[i][4])[2])*(float(KorA[i][2])/float(KorA[j][2]))) + Parcala(KorA[i][4])[3] 
                        
                            print(str(KorA[i][0]) + " açısının "+ str(KorA[i][2]) +" katı " + str(KorA[j][0]) + " açısının "+str(KorA[j][2])  + " birbirine eşit olduğundan:")
                            print("=> "+str(KorA[j][0]) + " = " + str(KorA[j][4]) + " olur.")
                            if(KorA[j][1] != 's'):
                                if(Parcala(KorA[j][4])[1] == "+"):
                                    bilinmeyen = (-float(KorA[j][1])+ float(Parcala(KorA[j][4])[0]))/(float(Parcala(KorA[j][4])[2]))
                                    print(KorA[j][0] + " => "+KorA[j][4]+" = "+ str(KorA[j][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[j][4])[2]+Parcala(KorA[j][4])[3]+ " = "+ str(float(Parcala(KorA[j][4])[0]) - float(KorA[j][1])))
                                    print("=> "+ Parcala(KorA[j][4])[2]+ " = "+ str(bilinmeyen)+ " değeri bulunur.")
                                else:
                                    bilinmeyen = (float(KorA[j][1]) - float(Parcala(KorA[j][4])[0]))/(float(Parcala(KorA[i][4])[2]))
                                    print(KorA[j][0] + " => "+KorA[j][4]+" = "+ str(KorA[j][1])+ " eşitliğinden")
                                    print("=> " +Parcala(KorA[j][4])[2]+Parcala(KorA[j][4])[3]+ " = "+ str(float(Parcala(KorA[j][4])[0]) + float(KorA[j][1])))
                                    print("=> "+ Parcala(KorA[j][4])[2]+ " = "+ str(bilinmeyen)+ " değeri bulunur.")                 
                                                                      
                    j+=1
                i+=1   
            AciTList = []
            if(aci012[1] != "s"):
                AciTList.append(aci012)
            
            else:
                BilinmeyenKenar = aci012

            if(aci120[1] != "s"):
                AciTList.append(aci120)

            else:
                BilinmeyenKenar = aci120

            if(aci201[1] != "s"):
                AciTList.append(aci201)

            else:
                BilinmeyenKenar = aci201


            if(len(AciTList) == 2):
                print()
                print("Üçgenin içi açılarının toplamı 180 derece olduğundan dolayı :")
                BilinmeyenKenar[1] = (180 - (float(AciTList[0][1]) + float(AciTList[1][1])))
                print("180" + " - ( " +  str(float(AciTList[0][1])) + " + " + str( float(AciTList[1][1])) + " ) = " + str(float(BilinmeyenKenar[1]))) 
    
        def OzelUcgen():
            i = 0        
            while i < len(KorA):
                 if (KorA[i][1] == "90" or KorA[i][1] == 90): # bir açı 90 derece olduğu biliniyorsa üçgen dik ise örnek olarak ABC üçgeni verildi
                 
                     for aci in KorA:
                         # aci012 açısı 90 dereceyse
                         if (aci[0] == aci012[0] and aci == KorA[i]): 
                             Doksan_Kenar(aci012, aci120, aci201, kenar01, kenar12, kenar20)

                         # aci120 açısı 90 dereceyse
                         if (aci[0] == aci120[0] and aci == KorA[i]):
                             Doksan_Kenar(aci120, aci012, aci201, kenar12, kenar20, kenar01)

                         # aci201 açısı 90 dereceyse
                         if (aci[0] == aci201[0] and aci == KorA[i]):
                             Doksan_Kenar(aci201, aci012, aci120, kenar01, kenar20, kenar12)
                     #i = len(KorA)
                 #---------------------------------------------------------------------------------------------------------------------------------------------#
                 # cos teoremi kullanarak kenarın bulunması

                 elif (KorA[i][1] != "s"):
                     for aci in KorA:
                        if(aci[0] == aci012[0] and aci == KorA[i]):
                            Yuzyirmi_Aci(aci012, aci120, aci201, kenar01, kenar12, kenar20)

                        if(aci[0] == aci120[0] and aci == KorA[i] ):
                            Yuzyirmi_Aci(aci120, aci012, aci201, kenar20, kenar12, kenar01)

                        if(aci[0] == aci201[0] and aci == KorA[i] ):
                            Yuzyirmi_Aci(aci201, aci012, aci120, kenar01, kenar20, kenar12)
                   
                 i+=1                           
   
        def Doksan_Kenar(Aci90, BAci1, BAci2,Bkenar1, Bkenar2, Hipokenar): # aci012 bilinen 90 derece
        
                PTList=[]
                if(Bkenar1[1] != "s"):
                    PTList.append(Bkenar1)
                else:
                    BilinmeyenKenar = Bkenar1
                if(Bkenar2[1] != "s"):
                    PTList.append(Bkenar2)
                else:
                    BilinmeyenKenar = Bkenar2
                if(Hipokenar[1] != "s"):
                    PTList.append(Hipokenar)
                else:
                    BilinmeyenKenar = Hipokenar
                if(len(PTList) == 2):
                    print("")
                    print (str( Aci90[0] ) + " = 90° olduğundan pisagor teoremi uygulanır.")
                    print("a^2 = b^2 + c^2")
                    BilinmeyenKenar[1] = Pisagor(Hipokenar,PTList[0],PTList[1])

                if (KorATani(Hipokenar[0])[1] != "s" and ((KorATani(BAci1[0])[1] == "60" or KorATani(BAci2[0])[1] == "30") or (KorATani(BAci2[0])[1] == "60" or KorATani(BAci1[0])[1] == "30"))):
                    if (KorATani(BAci2[0])[1] == "60" or KorATani(BAci1[0])[1] == "30"):
                        Uc_Alti ( KorATani(Bkenar2[0]), KorATani(Bkenar1[0]), KorATani(Hipokenar[0]))                #str(float(KorATani("CA")[1])/2)+"√3"
                        if (KorATani(BAci2[0])[1] == "s"):
                            KorATani(BAci2[0])[1] = "60"
                        else:                                    
                            KorATani(BAci1[0])[1] = "30"
                    else:
                        Uc_Alti (  KorATani(Bkenar1[0]),KorATani(Bkenar2[0]), KorATani(Hipokenar[0])) 
                        if (KorATani(BAci2[0])[1] == "s"):
                            KorATani(BAci2[0])[1] = "30"
                        else:                                    
                            KorATani(BAci1[0])[1] = "60"

                elif (KorATani(Hipokenar[0])[1] != "s" and (KorATani(BAci1[0])[1] == "45" or KorATani(BAci2[0])[1] == "45")): # 90'nın karşısı biliniyorsa 
                    Dort_Bes(KorATani(Bkenar2[0]),KorATani(Bkenar1[0]),KorATani(Hipokenar[0]))
                    if (KorATani(BAci2[0])[1] == "s"):
                            KorATani(BAci2[0])[1] = "45"
                    else:
                            KorATani(BAci1[0])[1] = "45"
   
                elif (KorATani(Bkenar1[0])[1] != "s" and (KorATani(BAci1[0])[1] == "60" or KorATani(BAci2[0])[1] == "30")):
                    Alti_Dokuz(KorATani(Bkenar2[0]), KorATani(Bkenar1[0]), KorATani(Hipokenar[0]))
                    if(KorATani(BAci1[0])[1] == "60"):
                        KorATani(BAci2[0])[1] = "30"
                    else:
                        KorATani(BAci2[0])[1] = "60"

                elif (KorATani(Bkenar1[0])[1] != "s" and (KorATani(BAci1[0])[1] == "30" or KorATani(BAci2[0])[1] == "60")):
                    Uc_Dokuz(KorATani(Bkenar1[0]),KorATani(Bkenar2[0]),KorATani(Hipokenar[0]) )
                    if(KorATani(BAci1[0])[1] == "30"):
                        KorATani(BAci2[0])[1] = "60"
                    else:
                        KorATani(BAci1[0])[1] = "30"

                elif (KorATani(Bkenar1[0])[1] != "s" and (KorATani(BAci1[0])[1] == "45" or KorATani(BAci2[0])[1] == "45")):
                    Dort_Dokuz(KorATani(Bkenar1[0]),KorATani(Bkenar2[0]),KorATani(Hipokenar[0]))    

                elif (KorATani(Bkenar2[0])[1] != "s" and (KorATani(BAci1[0])[1] == "60" or KorATani(BAci2[0])[1] == "30")):
                    Uc_Dokuz(KorATani(Bkenar2[0]), KorATani(Bkenar1[0]), KorATani(Hipokenar[0]))
                    if(KorATani(BAci1[0])[1] == "60"):
                        KorATani(BAci2[0])[1] = "30"
                    else:
                        KorATani(BAci1[0])[1] = "60"

                elif (KorATani(Bkenar2[0])[1] != "s" and (KorATani(BAci1[0])[1] == "30" or KorATani(BAci2[0])[1] == "60")): 
                    KorATani(Hipokenar[0])[1] = float(KorATani(Bkenar2[0])[1])*2
                    KorATani(Bkenar1[0])[1] = round(float(KorATani(Bkenar2[0])[1])/mt.sqrt(3),2)
                    Alti_Dokuz(KorATani(Bkenar1[0]), KorATani(Bkenar2[0]), KorATani(Hipokenar[0]))
                    if(KorATani(BAci1[0])[1] == "30"):
                        KorATani(BAci2[0])[1] = "60"
                    else:
                        KorATani(BAci1[0])[1] = "30"

                elif (KorATani(Bkenar2[0])[1] != "s" and (KorATani(BAci1[0])[1] == "45" or KorATani(BAci2[0])[1] == "45")):
                    Dort_Dokuz(KorATani(Bkenar2[0]),KorATani(Bkenar1[0]), KorATani(Hipokenar[0]))
                    if (KorATani(BAci1[0])[1] == "s"):
                            KorATani(BAci1[0])[1] = "45"
                    else:
                            KorATani(BAci2[0])[1] = "45"

        def Yuzyirmi_Aci(BilinenAci, BAci1, BAci2,Bkenar1, Bkenar2, AciKarsisi):
            if((KorATani(Bkenar2[0])[3] == KorATani(Bkenar1[0])[3]) or (KorATani(BAci1[0])[1] == KorATani(BAci2[0])[1]) or ((KorATani(BAci1[0])[3] == KorATani(BAci2[0])[3]) and ((KorATani(BilinenAci[0])[1] == 120 or KorATani(BilinenAci[0])[1] == "120")))  or (KorATani(Bkenar2[0])[1] !="s" and KorATani(Bkenar1[0])[1] !="s")): 
            
                # Bir açı ve komşu 2 kenar bilindiği durumlarda 
                if (KorATani(Bkenar2[0])[1] !="s" and KorATani(Bkenar1[0])[1] !="s" and KorATani(AciKarsisi[0])[1] == "s"):                                                       
                    KorATani(AciKarsisi[0])[1] = round(mt.sqrt(pow(float(KorATani(Bkenar2[0])[1]),2)+pow(float(KorATani(Bkenar1[0])[1]),2) - (2*float(KorATani(Bkenar2[0])[1])*float(KorATani(Bkenar1[0])[1])*mt.cos(mt.radians(float(KorATani(BilinenAci[0])[1]))))),2)
                    print("")
                    print(str(BilinenAci[1]) + " açısı ve açıyı oluşturan iki kenarın uzunluğunu bilindiğinden, Kosinüs teoremi uygulanır.")
                    print("a^2 = b^2 + c^2 – 2bc(cosa)")
                    print(str(AciKarsisi[0]) + " = √ ( " + str(float(KorATani(Bkenar2[0])[1])) + "^2 + " + str(float(KorATani(Bkenar1[0])[1])) + "^2 - (2 * " + str(float(KorATani(Bkenar2[0])[1])) + " * " + str(float(KorATani(Bkenar1[0])[1])) + " * cos(" + str(BilinenAci[0]) + ")))")
                    print(str(AciKarsisi[0]) + " = " + str(KorATani(AciKarsisi[0])[1])+ " olarak bulunur.")

                # Açının 120 olup ikizkenar olması durumunda           
                elif((KorATani(BilinenAci[0])[1] == 120 or KorATani(BilinenAci[0])[1] == "120" and (KorATani(BAci1[0])[3] == KorATani(BAci2[0])[3])) and KorATani(Bkenar2[0])[1] !="s"):
                    KorATani(AciKarsisi[0])[1] = round(float(KorATani(Bkenar2[0])[1])*mt.sqrt(3),2)
                    KorATani(Bkenar1[0])[1] = KorATani(Bkenar2[0])[1]
                    print("")
                    print("120 - 30 - 30 üçgeni ikizkenar üçgendir. Bir kısa kenarı bilindiğine göre diğeri de ona eşit olmaktadır. ")
                    print(str(Bkenar2[0]) + " = "  + str(KorATani(Bkenar2[0])[1]) + " olduğuna göre " + str(Bkenar1[0]) + " = " + str(KorATani(Bkenar1[0])[1]) + " olmaktadır.")
                    print("Uzun kenarı ise aşağıdaki gibi hesaplanmaktadır.")
                    print(str(float(KorATani(Bkenar2[0])[1])) + " * √3 = " + str(KorATani(AciKarsisi[0])[1]) )

                elif((KorATani(BilinenAci[0])[1] == 120 or KorATani(BilinenAci[0])[1] == "120" and (KorATani(BAci1[0])[3] == KorATani(BAci2[0])[3])) and KorATani(Bkenar1[0])[1] !="s"):
                    KorATani(AciKarsisi[0])[1] = round(float(KorATani(Bkenar1[0])[1])*mt.sqrt(3),2)
                    KorATani(Bkenar2[0])[1] = KorATani(Bkenar1[0])[1]
                    print("")
                    print("120 - 30 - 30 üçgeni ikiz kenar üçgendir. Bir kısa kenarı bilindiğine göre diğeri de ona eşit olmaktadır. ")
                    print(str(Bkenar1[0]) + " = "  + str(KorATani(Bkenar1[0])[1]) + "  olduğuna göre " + str(Bkenar2[0]) + " = " + str(KorATani(Bkenar2[0])[1]) + " olmaktadır.")
                    print("Uzun kenarı ise aşağıdaki gibi hesaplanmaktadır.")
                    print(str(float(KorATani(Bkenar1[0])[1])) + " * √3 = " + str(KorATani(Bkenar2[0])[1]) )

                elif((KorATani(BilinenAci[0])[1] == 120 or KorATani(BilinenAci[0])[1] == "120" and (KorATani(BAci1[0])[3] == KorATani(BAci2[0])[3])) and KorATani(AciKarsisi[0])[1] !="s"):
                    KorATani(Bkenar2[0])[1] = round(float(KorATani(AciKarsisi[0])[1])/mt.sqrt(3),2)
                    KorATani(Bkenar1[0])[1] = KorATani(Bkenar2[0])[1]
                    print("")
                    print ("Uzun kenarı bilinen üçgenin kısa kenarlarından biri aşağıdaki gibi bulunur.")
                    print(str(float(KorATani(AciKarsisi[0])[1])) + " / √3 = " + str(KorATani(Bkenar2[0])[1]) )
                    print("120 - 30 - 30 üçgeni ikiz kenar üçgendir. Bir kısa kenarı bulunduğuna göre diğeri de ona eşit olmaktadır. ")
                    print(str(Bkenar2[0]) + " = "  + str(KorATani(Bkenar2[0])[1]) + " olduğuna göre " + str(Bkenar1[0]) + " = " + str(KorATani(Bkenar1[0])[1]) + " olmaktadır.")

                if((KorATani(BilinenAci[0])[1] != "s") and (KorATani(BAci1[0])[3] == KorATani(BAci2[0])[3])):
                    OranYazdir(KorATani(BAci1[0]),KorATani(BAci2[0]))
                    KorATani(BAci1[0])[1] = (180 - float(KorATani(BilinenAci[0])[1]))*float(KorATani(BAci2[0])[2])/(float(KorATani(BAci1[0])[2])+float(KorATani(BAci2[0])[2]))
                    KorATani(BAci2[0])[1] = (180 - float(KorATani(BilinenAci[0])[1]))*float(KorATani(BAci1[0])[2])/(float(KorATani(BAci1[0])[2])+float(KorATani(BAci2[0])[2]))
                    print()
                    print(str(KorATani(BAci1[0])[0])+ " = 180 - ("+ str(float(KorATani(BilinenAci[0])[1]))+ " x "+str(float(KorATani(BAci2[0])[2]))+ " / ("+str(float(KorATani(BAci1[0])[2]))+" + "+str(float(KorATani(BAci2[0])[2]))+"))")
                    print("=> "+str(KorATani(BAci1[0])[0])+ " = "+str(KorATani(BAci1[0])[1]))
                    print()
                    print(str(KorATani(BAci2[0])[0])+ " = 180 - ("+ str(float(KorATani(BilinenAci[0])[1]))+ " x "+str(float(KorATani(BAci1[0])[2]))+ " / ("+str(float(KorATani(BAci2[0])[2]))+" + "+str(float(KorATani(BAci1[0])[2]))+"))")
                    print("=> "+str(KorATani(BAci2[0])[0])+ " = "+str(KorATani(BAci2[0])[1])+ " bulunur.")
        #Parametre olarak hipotenüs ve bilinen iki kenarı alarak pisagor teoremini uygulayıp bilinmeyen kenar değerini döndürür
        def Pisagor(hipo,kenar1,kenar2):
            if(hipo != kenar1 and hipo != kenar2):
                BilinmeyenKenar = round(mt.sqrt(((float(kenar1[1]))*float(kenar1[1])) + (float(kenar2[1]))*float((kenar2[1]))),2)
                print(str(hipo[0])+ " = √(" +str(float(kenar1[1]))+"^2 + " + str(float(kenar2[1]))+"^2")
                print(str(hipo[0])+" = "+ str(BilinmeyenKenar)+ " bulunur.")
            if(hipo == kenar1):
                BilinmeyenKenar = round(mt.sqrt(((float(hipo[1]))*float(hipo[1])) - (float(kenar2[1]))*float((kenar2[1]))),2)
                print(str(kenar1[0])+ " = √(" +str(float(hipo[1]))+"^2 - " + str(float(kenar2[1]))+"^2")
                print(str(kenar1[0])+" = "+ str(BilinmeyenKenar)+ " bulunur.")
            if(hipo == kenar2):
                BilinmeyenKenar = round(mt.sqrt(((float(hipo[1]))*float(hipo[1])) - (float(kenar1[1]))*float((kenar1[1]))),2)
                print(str(kenar2[0])+ " = √(" +str(float(hipo[1]))+"^2 - " + str(float(kenar1[1]))+"^2")
                print(str(kenar2[0])+" = "+ str(BilinmeyenKenar)+ " bulunur.")
            return BilinmeyenKenar
    
        def Alti_Dokuz(uc, altı, dokuz ): #60ın karşısı biliniyorsa diğer kenarlar
            uc[1] = round((float(altı[1])/mt.sqrt(3)),2)
            dokuz[1] = uc[1] * 2
            print("30 dercenin karşısındaki kenar uzunluğu -> ( " + str((float(altı[1]))) + "  ) / √3 = " + str(uc[1]) + " olur. " )
            print("90 dercenin karşısındaki kenar uzunluğu -> " + str((float(uc[1]))) + " * 2 = " + str(dokuz[1]) + " olur." )

        def Dort_Dokuz(a,b,dokuz):
            b[1] = a[1]
            dokuz[1] = round((float(a[1])*mt.sqrt(2)),2) 
            print("45 dereceyi gören karşı kenarların uzunlukları birbirine eşit oldukları için")
            print(str(b[0]) + " = " + str(a[1]))
            print ( str((float(a[1]))) + " * √2 = " + str(dokuz[1])+" bulunur.")

        def Dort_Bes(a,b,dokuz): # 90 karşısı biliniyor 45 kaçtır
             a[1] = round(((float(dokuz[1])/2)*mt.sqrt(2)),2)
             b[1] = round(((float(dokuz[1])/2)*mt.sqrt(2)),2)
             print ("90 derecenin karşısındaki kenar uzunluğu bilindiğine göre 45 derecenin karşısında kalan diğer iki kenarın ölçüsü: ")
             print( "( " + str((float(dokuz[1]))) + " / 2 ) * √2 = " + str(a[1]) +" bulunur." )
        
        def Uc_Dokuz(uc,alti,dokuz):
            dokuz[1] = float(uc[1])*2
            alti[1] = round(float(uc[1])*mt.sqrt(3),2)
            print("90 derecenin karşısındaki kenar uzunluğu -> "+str(float(uc[1])) + "* 2 = " + str(dokuz[1]) + " olur. ")
            print( "60 dercenin karşısındaki kenar uzunluğu -> "+str((float(uc[1]))) + " * √3 = " + str(alti[1]) + " olur." )

        def Uc_Alti(alti,uc,dokuz):  # 90 karşısının uzunluğu biliniyorsa 30 ve 60 karşısını hesaplıyor
            alti[1] = round((float(dokuz[1])/2)*mt.sqrt(3),2)
            print("60 dercenin karşısındaki kenar uzunluğu -> ( " + str((float(dokuz[1]))) + " / 2 ) * √3 = " + str(alti[1]) + " olur." )
            uc[1] = (float(dokuz[1])/2)   
            print("30 dercenin karşısındaki kenar uzunluğu -> "+ str((float(dokuz[1]))) + " / 2 = " + str(uc[1]) + " olur.")

        def OranYazdir(bilinen, bulunan): # Çözüm adımları için katsayıların oranlarını yazdırır
            print("")
            kenar = ["k0","k1","k2"]

            if(bilinen[0] in kenar):  # kenar ise yazılacak çıktı 
                if (bilinen[2] == 1 or bulunan[2] == 1):
                    if bulunan[2] == 1:
                        if(bilinen[1] != "s"):
                            print(str(bilinen[0]), "kenarı ile", str(bulunan[0]), "kenarı birbirine eşit ve", str(bilinen[0]),"=",str(bilinen[1]),"olduğundan:")
                            print(str(bulunan[0])+" => "+str(bulunan[1])+" olur.")
                        else:
                            print(str(bilinen[0]), "kenarı ile", str(bulunan[0]), "kenarı birbirine eşit olduğundan:")                       
                    
                    else:
                        if(bilinen[1] != "s"):
                            print(str(bilinen[0]), "kenarı ile", str(bulunan[0]), "kenarının", str(bulunan[2]), "katı birbirine eşit olduğundan ve", str(bilinen[0]), "=", str(bilinen[1]),"verildiğinden:")
                            print(str(bulunan[0])+" => "+str(bilinen[1])+".("+str(bilinen[2])+"/"+str(bulunan[2])+") = "+str(float(bulunan[1]))+" bulunur.")
                        else:
                            print(str(bilinen[0]), "kenarı ile", str(bulunan[0]), "kenarının", str(bulunan[2]), "katı birbirine eşit olduğundan ")

                else:
                    if(bilinen[1] != "s"):
                        print(str(bilinen[0]), "kenarının",str(bilinen[2]), "katı ile", str(bulunan[0]), "kenarının", str(bulunan[2]), "katı birbirine eşit ve", str(bilinen[0]),"=",str(bilinen[1]),"verildiğinden:")
                        print(str(bulunan[0])+" => "+str(bilinen[1])+".("+str(bilinen[2])+"/"+str(bulunan[2])+") = "+str(bulunan[1])+" olur.")
                    else:
                        print(str(bilinen[0]), "kenarının",str(bilinen[2]), "katı ile", str(bulunan[0]), "kenarının", str(bulunan[2]), "katı birbirine eşit olduğundan")


            else:                    # açı ise yazılacakları belirleme
                if (bilinen[2] == 1 or bulunan[2] == 1):
                    if bulunan[2] == 1:
                        if(bilinen[1] != "s"):
                            print(str(bilinen[0]), "açısı ile", str(bulunan[0]), "açısı birbirine eşit ve", str(bilinen[0]),"=",str(bilinen[1]),"olduğundan:")
                            print(str(bulunan[0])+" => "+str(bulunan[1])+" olur.")
                        else:
                            print(str(bilinen[0]), "açısı ile", str(bulunan[0]), "açısı birbirine eşit olduğundan:")

                    else:
                        if(bilinen[1] != "s"):
                            print(str(bilinen[0]), "açısı ile", str(bulunan[0]), "açısının", str(bulunan[2]), "katı birbirine eşit olduğundan ve", str(bilinen[0]), "=", str(bilinen[1]),"verildiğinden:")
                            print(str(bulunan[0])+" => "+str(bilinen[1])+".("+str(bilinen[2])+"/"+str(bulunan[2])+") = "+str(bulunan[1])+" olur.")
                        else:
                            print(str(bilinen[0]), "açısı ile", str(bulunan[0]), "açısının", str(bulunan[2]), "katı birbirine eşit olduğundan")

                else:
                    if(bilinen[1] != "s"):
                        print(str(bilinen[0]), "açısınnın",str(bilinen[2]), "katı ile", str(bulunan[0]), "açısının", str(bulunan[2]), "katı birbirine eşit ve", str(bilinen[0]),"=",str(bilinen[1]),"verildiğinden:")
                        print(str(bulunan[0])+" => "+str(bilinen[1])+".("+str(bilinen[2])+"/"+str(bulunan[2])+") = "+str(bulunan[1])+" olur.")
                    else:
                        print(str(bilinen[0]), "açısınnın",str(bilinen[2]), "katı ile", str(bulunan[0]), "açısının", str(bulunan[2]), "katı birbirine eşit olduğundan")

        SayiveHarfIsle()
        KatsayiIsle()
        OrtakKatUygula(ToplamKorAList,ToplamKatsayiList)
        OzelUcgen()
        BoslukDoldur()
        #Bilinmeyen()
        yazdir()
        
                                    ###########  ÇIKTILAR İÇİN ÇAĞRILAN FONKSİYONLAR  #################

    def onemliKaliplariYazdir():  

            asoru = GereksizSil(soru)
            #print("Girdi Soru => ",soru)
            print("SORU       => ", asoru)
            #print("********************************** DÜZENLENMİŞ METİN ********************************************")
            #print("")
            #print(asoru)
            print("")
            

            sekil = HarfSekil(asoru)
            print("ŞEKİL      => ", sekil)
            
            tur = AnahtarMi(asoru)
            print("TÜR        => ", tur)
            
            kalipList = KalipYaz(asoru)    # tüm kalıpların olduğu liste 
            print("KALIPLAR   => ",kalipList)
            #print("")
            #print("*************************** 2. KISIMDA İŞLENEN VERİLER VE ÇÖZÜM *****************************")

            ucgen(sekil,tur,kalipList)

    onemliKaliplariYazdir()

def FonkCagır():
    soru = "ABC bir dik üçgendir.  m(ABC)=90, m(ABC)=2m(BCA), m(BCA)=x kaçtır?" # örnek soru girdisi
    print("****************************** GÖRÜNTÜDEN AGILANAN METİN **************************************")
    print(soru)
    print("***************************** 1. KISIMDAN GELEN BİLGİLER ************************************")
    print("")
    Analiz(soru)

FonkCagır()

