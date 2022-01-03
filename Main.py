import turtle
import time
import random
import keyboard
from Yem import Yem

delay = 0.05    #hızımızı belirleyen faktör, sleep fonksiyonunda programı bekletmek için kullanıyoruz. ne kadar azalırsa o kadar hızlı olur.
skor = -3       #puanımızı gösteren sayac, başlangıçta -3, çünkü başlangıçta 3 kuyruk ile başlıyoruz.

renkSayaci = 0           #bu sayac, yılanın yem yediğinde kafasının renginin değişmesi için kullanılıyor.
sureliYemSayaci = 5    #kaç yemekten sonra altın yemek gelsin, bunu tutar.
eklenecekKuyrukSayaci = 3    
yavaslatmaBool = False   #yavaşlatma özelliğinin kullanılabilmesi için
yavaslatmaSayaci = 1     #turbo sayacı da, yavaşlama kaç adım geçerli olsun
delayTutucu = 0     #turbo özelliğinden sonra eski hızına dönmesi için bir tutucu

icindenGecBool = False
icindenGecSayac = 1

sureliYemGorunmeSayaci = 80
sureliYemGorunmeBool = False

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("gray")
pencere.setup(width = 705,height = 705)
pencere.tracer(0) #ekranın kendini yenilememesi için

sYem = Yem("black",-300,50,1)
yYem = Yem("green",-300,10,1)
kYem = Yem("red",-300,-30,1) 
tYem = Yem("orange",-300,-70,1)
mYem = Yem("blue",-300,-110,1)
kullanimaHazir = Yem("green",-300,-250,0.5)
kullaniliyor = Yem("lightgreen",-300,-270,0.5)
kullanilamaz = Yem("red",-300,-290,0.5)


carpismaDurumu = turtle.Turtle()
carpismaDurumu.speed(0)
carpismaDurumu.shape("circle")
carpismaDurumu.color("green")
carpismaDurumu.penup()
carpismaDurumu.goto(-220,290)
carpismaDurumu.shapesize(0.5)


yavaslamaDurumu = turtle.Turtle()
yavaslamaDurumu.speed(0)
yavaslamaDurumu.shape("circle")
yavaslamaDurumu.color("green")
yavaslamaDurumu.penup()
yavaslamaDurumu.goto(-220,310)
yavaslamaDurumu.shapesize(0.5)


pencere.update() 

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("circle")
kafa.color("black")
kafa.goto(0,0)
kafa.penup()
kafa.direction = "stop"
kafa.shapesize(1)

bilgilendirme = turtle.Turtle()
bilgilendirme.speed(0)
bilgilendirme.color("black")
bilgilendirme.penup()
bilgilendirme.goto(0,-300)
bilgilendirme.write("Başlamak için SPACE tuşuna basınız.\n\n\nOYUN KURALLARI:\n\nOk tuşları ile hareket edebilirsiniz.\n\nYılanın kafasını göstermektedir.\n\nKuyruğu göstermektedir.\n\n+1 puanlık yemlerdir.\n\n+10 puanlık yemlerdir.\n\nŞans yemleri yılanın boyunda değişiklik yaratır.\n\nYETENEKLER:\nX tuşu ile yavaşlatma becersini aktif edebilirsiniz.\nY tuşu ile çarpışma becerisini aktif edebilirsiniz.\n\nBECERİLERİN KENARINDAKİ IŞIKLARIN ANLAMLARI \n--> Kullanıma Hazır.\n--> Şu anda kullanılıyor.\n--> Beceri kapalı, kullanılamaz.",align='center',font =('Courier',13,'bold'))

skorBilgi = turtle.Turtle()     #ekranda skoru görebilmemiz için yazı.
skorBilgi.speed(0)
skorBilgi.color("black")
skorBilgi.penup()
skorBilgi.goto(200,300)
skorBilgi.hideturtle()

enYuksekSkor = 0                    
enYuksekSkorBilgi = turtle.Turtle()     #en yüksek skoru görebilmemiz için yazı
enYuksekSkorBilgi.speed(0)              
enYuksekSkorBilgi.color("black")
enYuksekSkorBilgi.penup()
enYuksekSkorBilgi.goto(0,300)
enYuksekSkorBilgi.hideturtle()

yavaslama = turtle.Turtle()             #yavaslama becerisinin durumunu görebilmemiz için gerekli yazı
yavaslama.speed(0)
yavaslama.color("black")
yavaslama.penup()
yavaslama.goto(-330,300)
yavaslama.write("Yavaslama:",align='left',font =('Courier',13,'bold'))
yavaslama.hideturtle()

carpisma = turtle.Turtle()              #carpışma becerisinin durumunu görebilmemiz için gerekli yazı
carpisma.speed(0)
carpisma.color("black")
carpisma.penup()
carpisma.goto(-330,280)
carpisma.write("Çarpışma :",align='left',font =('Courier',13,'bold'))
carpisma.hideturtle()

yemek = turtle.Turtle()         #normal yemler buradan erişiliyor.
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.goto(0,105)
yemek.shapesize(1)

sureliYem = turtle.Turtle()     #özel yemler buradan erişiliyor.
sureliYem.speed(0)
sureliYem.shape("circle")
sureliYem.color("orange")
sureliYem.penup()
sureliYem.goto(1000,1000)
sureliYem.shapesize(1)

yemekler = []       #kuyruğumuzu tutacak olan dizi.

def atla():         #atlama becerisi kullanıldığında kaç birim atlaması gerekiyor burda belirliyoruz.
    move()
    move()
    move()
    move()
    move()

def goUp():     #yukarı yönlendirme fonksiyonumuz.
    if kafa.direction != "down":
        if kafa.direction == "up":      #yukarı gidiyorsa zaten burda atla fonksiyonu çalışıyor.
            atla()
        elif len(yemekler)>0 and yemekler[0].ycor()-15 == kafa.ycor():
            print("\tDelaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'up'

def goDown():   #aşağı yönlendirme fonksiyonumuz.
    if kafa.direction != "up":
        if kafa.direction == "down":
            atla()
        elif len(yemekler)>0 and yemekler[0].ycor()+15 == kafa.ycor():
            print("\tDelaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'down'

def goRight():  #sağa yönlendirme fonksiyonumuz
    if kafa.direction != "left":
        if kafa.direction == "right":
            atla()
        elif len(yemekler)>0 and yemekler[0].xcor()-15 == kafa.xcor():
            print("\tDelaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'right'

def goLeft():   #sola yönlendirme fonksiyonumuz.
    if kafa.direction != "right":
        if kafa.direction == "left":
            atla()
        elif len(yemekler)>0 and yemekler[0].xcor()+15 == kafa.xcor():
            print("\tDelaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'left'

def move():                          #hareket fonksiyonumuz. Main fonksiyonundan çağrılarak bir birim hareketi gerçekleştiriyor.
    if kafa.direction == "up":
        kafa.sety(kafa.ycor()+15)

    if kafa.direction == "down":
        kafa.sety(kafa.ycor()-15)
        
    if kafa.direction == "right":
        kafa.setx(kafa.xcor()+15)

    if kafa.direction == "left":
        kafa.setx(kafa.xcor()-15)


def yavasla():                  #yavaslama becerisini aktif ettiğimiz fonksiyon.
    global yavaslatmaSayaci     #global keywordu, sayfada tanımlanan değişkeni kullanabilmek için. 
    global yavaslatmaBool
    global delayTutucu
    global delay
    if yavaslatmaBool == True:  
        return
    delayTutucu = delay
    if yavaslatmaSayaci > 0:    #kullanılabilir halde olduğunu gösterir.
        yavaslatmaSayaci = 30
        yavaslatmaBool = True
        print("\tYavaşlama becerisi aktif edildi.")

def icindenGec():               #carpışma becerisini aktif ettiğimiz fonksiyon.
    global icindenGecBool
    global icindenGecSayac
    if icindenGecBool == True:
        return
    if icindenGecSayac > 0:
        icindenGecSayac = 100
        icindenGecBool = True
        print("\tÇarpışma becerisi aktif edildi.")


pencere.listen()                        #klavyemizi dinleyip, basılan tuşlara göre ilgili fonksiyonların çalıştırılması
pencere.onkeypress(goUp, 'Up')
pencere.onkeypress(goDown, 'Down')
pencere.onkeypress(goRight, 'Right')
pencere.onkeypress(goLeft, 'Left')
pencere.onkeypress(yavasla,'x')
pencere.onkeypress(icindenGec,'z')

def beyazKafa():
    kafa.color("white")
def siyahKafa():
    kafa.color("black")

def tekrarBasla():                      #oyun sona erdikten sonra gerekli sıfırlama işlemleri burada gerçekleştiriliyor.
    oyunBitti()
    kafa.direction = "stop"
    for i in yemekler:
        i.goto(1000,1000)               #kuyruğu ekran dışına taşıdık
    yemekler.clear()
    kafa.goto(0,0)
    global skor
    skor = -3
    global sureliYemSayaci
    sureliYemSayaci = 5
    yemekKonumuDegistir(yemek)
    yemek.color("red")
    global eklenecekKuyrukSayaci
    eklenecekKuyrukSayaci = 3
    global delay
    delay = 0.05
    global yavaslatmaBool
    yavaslatmaBool = False
    global yavaslatmaSayaci
    yavaslatmaSayaci = 1
    yavaslamaDurumu.color("green")
    global icindenGecSayac
    icindenGecSayac = 1
    carpismaDurumu.color("green")
    global icindenGecBool 
    icindenGecBool = False
    global sureliYemGorunmeBool
    global sureliYemGorunmeSayaci
    sureliYemGorunmeSayaci = 0
    sureliYemGorunmeBool = False
    sureliYem.goto(1000,1000)
    print("\n\n\nOYUN TEKRAR BAŞLATILIYOR.\n\n\n")


def kuyrukEkle():
    kuyruk = turtle.Turtle()
    kuyruk.speed = 0
    kuyruk.shape("circle")
    kuyruk.color("green")
    kuyruk.penup()
    kuyruk.goto(1000,1000)
    yemekler.append(kuyruk)
    global skor
    skor += 1

def oyunBitti():
    for i in range(4):      #oyunun bittiğine dair basit bir animasyon.
        for i in range(len(yemekler)-1,-1,-1): #tüm kuyruk beyaz yapıldı.
            yemekler[i].color("white")
        
        pencere.update()
        time.sleep(0.1)

        for i in range(len(yemekler)-1,-1,-1): #tüm kuyruk kırmızı yapıldı.
            yemekler[i].color("red")
        pencere.update()
        time.sleep(0.1)


def yemekYenildiMi():               #kafa ile yemek arası boşluk 15'in altına düştüğünde yeme işlemi gerçekleşmiş demektir.
    if kafa.distance(yemek) < 15 or kafa.distance(sureliYem) < 15:
        return True
    else:
        return False

def yemekKonumuDegistir(yem):
    xkonum = random.randint(-250,250)      #piksel uyuşmazlığı için ayarlamalar yapıldı.
    x = xkonum - (xkonum%15)
    ykonum = random.randint(-250,250)
    y = ykonum - (ykonum%15)
    yem.goto(x,y)
    kuyrukYemekCakismasi(yem)
    yemlerinCakismasi()

def yemlerinCakismasi():
    if yemek.xcor() == sureliYem.xcor() and yemek.ycor() == sureliYem.ycor():
        print("\tYemler çakıştığı için, süreli yem yeri değişiyor.")
        yemekKonumuDegistir(sureliYem)


def kuyrukTakibi():
    for i in range(len(yemekler)-1,0,-1):           #uzunluktan -1 ekleyerek sıfıra kadar.
        x = yemekler[i-1].xcor()
        y = yemekler[i-1].ycor()
        yemekler[i].goto(x,y)
    
    if len(yemekler) >= 1:                          #ilk düğüm için başı takip etmesi gerektiğini söyledik. aşağıda başı bir sonraki hedefe alıyoruz.
        x = kafa.xcor()
        y = kafa.ycor()
        yemekler[0].goto(x,y)


def kuyrukYemekCakismasi(yem):
    
    for i in range(len(yemekler)-1,0,-1):
        if yemekler[i].xcor() == yem.xcor() and yemekler[i].ycor() == yem.ycor():
            print("\tYemek ile kuyruk çakıştı. Tekrar yemek ataması yapılıyor.")
            yemekKonumuDegistir(yem)
            break

def kuyrukKafaCakismasi():
    if icindenGecBool == False:
        for i in range(len(yemekler)-1,0,-1):
            if kafa.xcor() == yemekler[i].xcor() and kafa.ycor() == yemekler[i].ycor():
                tekrarBasla()
                break
        
def kafaRengiAyarla(sayac):
    if sayac>5 or (sayac>1 and sayac<=3):
        beyazKafa()
        sayac-=1
    else:
        siyahKafa()
        sayac-=1
    return sayac

def kenaraCarpma():
    if(kafa.xcor() <-331 or kafa.xcor() > 331 or kafa.ycor() <-331 or kafa.ycor() > 331):
        tekrarBasla()

def rastgele():
    i = random.randint(0,1)
    return i

while True:
    time.sleep(0.1)                         #çok fazla işlem yükünün engellenmesi için.
    if keyboard.is_pressed('space'):        #space tuşuna basılana kadar burada kontrol gerçekleştiriliyor. Basıldığında ilerliyor. 
        mYem.goto(1000,1000)
        sYem.goto(1000,1000)
        tYem.goto(1000,1000)
        kYem.goto(1000,1000)
        yYem.goto(1000,1000)
        kullanilamaz.goto(1000,1000)
        kullaniliyor.goto(1000,1000)
        kullanimaHazir.goto(1000,1000)
        bilgilendirme.clear()
        bilgilendirme.goto(1000,1000)
        pencere.update()
        break

def enYuksekSkorKontrol():
    global skor
    global enYuksekSkor
    if skor > enYuksekSkor:
        enYuksekSkor = skor
        enYuksekSkorBilgi.clear()
        enYuksekSkorBilgi.write("En Yuksek: {}".format(enYuksekSkor), font =('Courier',13,'bold'))

def skorGuncelle():
    if skor > 0:
        skorBilgi.clear()
        skorBilgi.write("Puan: {}".format(skor), font =('Courier',13,'bold'))
    else:
        skorBilgi.clear()
        skorBilgi.write("Puan: 0", font =('Courier',13,'bold'))


def sureliYemYenildi():
    global delay
    if delay > 0.01:
        print("\tHız artırıldı.")
        delay -= 0.01
    else:
        print("Hız maksimumda olduğu için artırılamıyor.")

    if sureliYem.color() == ('orange','orange'):
        global eklenecekKuyrukSayaci
        global sureliYemSayaci
        global skor
        eklenecekKuyrukSayaci += 10
        sureliYemSayaci = 5
        print("+10: Altın (turuncu) yem yenildi.")
    else:
        i = rastgele()
        if i==0:
            temp = 0
            if skor%2 == 1:
                skor+=1
            temp = 1
            skor /=2
            skor = int(skor)
            temp = skor - temp
            for i in range(temp):
                yemekler[len(yemekler)-1].goto(1000,1000)
                yemekler.pop()
            print("-{}: Skor yarıya indi.".format(temp))
        else:
            print("+{}: Skor 2 ile çarpıldı.".format(skor))
            eklenecekKuyrukSayaci += skor

def normalYemYenildiMi():
    if kafa.distance(yemek) < 15:
        return True
    else:
        return False

def normalYemYenildi():
    global sureliYemSayaci
    sureliYemSayaci -= 1
    kuyrukEkle() #kırmızı yemek yenildiğinde bir kuyruk ekleniyor
    print("+1: Normal yem yenildi.")

def kuyrukEklenecekMi():
    global eklenecekKuyrukSayaci
    if eklenecekKuyrukSayaci > 0 and kafa.direction!="stop":#altın yem yenildiği takdirde altınKuyruk sayacı 10 yapılıyor.
        #her adımda bir yeni bir kuyruk eklenmesi için. Eğer bir adımda hepsini eklersek, kuyruk takibinde sıkıntı çıkar.
        kuyrukEkle()
        eklenecekKuyrukSayaci -= 1

def atama():
    global delayTutucu
    delayTutucu = delay

def turboKontrol():
    global delay
    global yavaslatmaSayaci
    global yavaslatmaBool#sayac 0
    global delayTutucu
    if yavaslatmaSayaci > 0: #şuanda kullanılıyor.
        delay = 0.15
        yavaslatmaSayaci -= 1
        yavaslamaDurumu.color("lightgreen")
    else:   #şuanda kullanılamaz durumda, hazırlanma sürecinde.
        delay = delayTutucu
        yavaslatmaSayaci = -200
        yavaslatmaBool = False
        yavaslamaDurumu.color("red")
        print("\tYavaşlatma becerisinin kullanım süresi doldu. Tekrar kullanım için hazırlanıyor")

def yavaslamaKontrol():
    global yavaslatmaSayaci
    if yavaslatmaBool:                                           #yavaşlama becerisinin kontrolü gerçekleştiriliyor.
        turboKontrol()
    elif yavaslatmaBool==False and kafa.direction != "stop":     #eğer beceri kullanılmıyorsa ve yılan hareket ediyorsa şuanda kullanılabilir hale getiriliyor.
        yavaslatmaSayaci += 1
        if yavaslatmaSayaci==0:
            print("\tYavaşlama becerisi kullanıma hazır.")
            yavaslamaDurumu.color("green")


def icindenGecKontrol():        #kuyruğa çarpmama özelliği
    global icindenGecSayac
    global icindenGecBool
    if icindenGecBool and icindenGecSayac > 0:  #true yapıldı ve 30 atandı. Kullanılıyor şuanda
        icindenGecSayac -= 1                    #her adımda bir azaltılıyor. hala true olarak kalıyor.
        carpismaDurumu.color("lightgreen")
        if icindenGecSayac == 0:                #özellik kullanımı bitti, şimdi kullanılamaz hale getirmem lazım.
            icindenGecSayac = -200              #200 birim sonra kullanılabilir hale gelicek
            icindenGecBool = False
            carpismaDurumu.color("red")
            print("\tÇarpışma becerisinin kullanımı doldu. Geçici bir süre kullanılamayacak.")
    else:
        icindenGecSayac += 1                    #her adımda sayacımızı +1 artırıyoruz.
    if icindenGecBool == False and icindenGecSayac < 0:
        carpismaDurumu.color("red")
        if icindenGecSayac+1 == 0:
            carpismaDurumu.color("green")
            print("\tÇarpışma becerisi kullanıma hazır.")

def sureliYemOrtayaCikis():
    global sureliYemGorunmeSayaci
    global sureliYemGorunmeBool
    global sureliYemSayaci
    if sureliYemSayaci == 0:            #sureli Yem oluşturulacak.
        i = rastgele()
        if i == 1:                      #turuncu
            sureliYem.color("orange")
        else:
            sureliYem.color("blue")

        yemekKonumuDegistir(sureliYem)
        sureliYemGorunmeSayaci = 80
        sureliYemGorunmeBool = True
        sureliYemSayaci = 5

def sureliYemKaybolma():
    global sureliYemGorunmeSayaci
    global sureliYemGorunmeBool
    if sureliYemGorunmeBool == True:        #eğer süreli yem ekranda görünüyorsa
        sureliYemGorunmeSayaci -= 1
        if sureliYemGorunmeSayaci == 0:
            sureliYemGorunmeBool = False
            sureliYem.goto(1000,1000)

while True:
    time.sleep(delay)
    sureliYemOrtayaCikis()
    sureliYemKaybolma()
    icindenGecKontrol()
    yavaslamaKontrol()                           # x tuşuna basıp özelliği aktif etti mi diye kontrol ediyoruz.
    enYuksekSkorKontrol()                       #en yüksek skorun kotrolü gerçekleştiriliyor. Eğer skor daha büyükse, en yüksek skorda ona eşit yapılıyor.
    skorGuncelle()                              #başlangçta skoru -3ten başlattığım için o gözükmesin diye buraya bir karşılaştırma yapısı eklendi.
    if yemekYenildiMi():                        #bir yemek yenildiyse aşağıdaki işlemler uygulanacak.
        if normalYemYenildiMi():
            normalYemYenildi()
            yemekKonumuDegistir(yemek)                   #bir sonraki yemin konumu ayarlanıyor.
        else:
            sureliYemYenildi()
            sureliYem.goto(1000,1000)
        renkSayaci = 7                          # bu sayac, kafa renginin yeme işleminden sonra 2 adımda bir değişebilmesi için gerekli.
    renkSayaci = kafaRengiAyarla(renkSayaci) 
    kuyrukKafaCakismasi()                       #kafanın kuyrukta herhangi bir bölüme çarpmasında oyun sona eriyor. Baştan tekrar başlatılıyor.
    kenaraCarpma()                              #Kafanın kenara çarpması durumunda yeniden başlatılması için yazılıyor.
    kuyrukEklenecekMi()                           #yenilen yem altın yem ise her adımda kuyruk eklemesi gerçekleştirebilmek için gerekli.
    kuyrukTakibi()                              #kuyruğun kafayı takip etme olayını burada gerçekleştiriliyor. Her bir kuyruk kendisinden önceki kuyruğun yerini alıyor
    move()                                      #hareket fonksiyonu, yılanı 1 birim hareket ettiriyor
    pencere.update()                            #her bir adımın görüntülenmesi için pencere güncelleniyor.+
