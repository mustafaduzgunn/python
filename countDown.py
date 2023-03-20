import time
import datetime

def countdown_with_time(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print("Süre Doldu!!!") 

def countdown_with_date(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Süre Doldu!!!")
            break
        if (difference.days < 0 or count_hours < 0 or count_minutes == 0 or count_seconds == 0):
            print (str(stop) + " tarihi geçmiş bir tarih olduğundan geri sayım başlatılamadı!")
            break
        print(('Kalan süre: '
              + str(difference.days) + " gün "
              + str(count_hours) + " saat "
              + str(count_minutes) + " dakika "
              + str(count_seconds) + " saniye "), end="\r")
        time.sleep(1)


tarih = datetime.datetime.now()
print (tarih)
while 1:
    tercih = input("Lütfen geri sayım için bir tercih seçimi yapınız.\n(1) Belirli bir süre için geri sayım yap.\n(2) Belirli bir tarihe kadar geri sayım yap.\nÇıkmak için 'q' tuşuna basınız.\n")
    if tercih == "1":
        t = input("Geri sayım için saniye cinsinden istenilen süreyi giriniz: ") 
        countdown_with_time(int(t)) 
    elif tercih == "2":
        yil = input ("Geri sayım yapılacak yılı giriniz (Örn:2021) : ")
        if yil == '':
            yil = tarih.strftime("%Y")
            print ("Gün değeri "+str(yil)+" olarak değerlendirilecek")
        ay = input ("Geri sayım yapılacak ayı giriniz (Örn:12) : ")
        if ay == '':
            ay = tarih.strftime("%m")
            print ("Gün değeri "+str(ay)+" olarak değerlendirilecek")
        gun = input ("Geri sayım yapılacak günü giriniz (Örn:31) : ")
        if gun == '':
            gun = tarih.strftime("%d")
            print ("Gün değeri "+str(gun)+" olarak değerlendirilecek")
        saat = input ("Geri sayım yapılacak saati giriniz (Örn:23) : ")
        if saat == '':
            print ("Saat değeri 0 olarak değerlendirilecek")
            saat = "0"
        dakika = input ("Geri sayım yapılacak dakikayı giriniz (Örn:59) : ")
        if dakika == '':
            print ("Dakika değeri 0 olarak değerlendirilecek")
            dakika = "0"
        saniye = input ("Geri sayım yapılacak saniyeyi giriniz (Örn:0) : ")

        if saniye == '':
            print ("Saniye değeri 0 olarak değerlendirilecek")
            saniye = "0"

        end_time = datetime.datetime(int(yil), int(ay), int(gun), int(saat), int(dakika), int(saniye))
        countdown_with_date(end_time)
    elif tercih == "q":
        break
    else:
        print ("Geçersiz tercih yaptınız. Lütfen tercihinizi kontrol ediniz.")