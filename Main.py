import turtle
import time
import random
import keyboard
from Yem import Yem

delay = 0.05    #hızımızı belirleyen faktör, sleep fonksiyonunda programı bekletmek için kullanıyoruz. ne kadar azalırsa o kadar hızlı olur.
skor = -3       #puanımızı gösteren sayac, başlangıçta -3, çünkü başlangıçta 3 kuyruk ile başlıyoruz.
kingSkor = 0    #en yüksek skoru gösteren sayac

delaySayaci = 10    #delay sayaci, her 10 yemde bir hızımızı biraz daha artırmamız için kullanıyoruz.
renkSayaci = 0           #bu sayac, yılanın yem yediğinde kafasının renginin değişmesi için kullanılıyor.
baslangicKuyrukSayaci = 3   #başlangıçta eklenecek kuyruk sayısını belirler.
altinYemekSayaci = 5    #kaç yemekten sonra altın yemek gelsin, bunu tutar.
altinKuyrukSayaci = 0   #altın yemek yenildikten sonra kaç adımda kuyruk eklemesi yapılsın 
turboBool = False   #yavaşlatma özelliğinin kullanılabilmesi için
turboSayici = 1     #turbo sayacı da, yavaşlama kaç adım geçerli olsun
delayTutucu = 0     #turbo özelliğinden sonra eski hızına dönmesi için bir tutucu

icindenGecBool = False
icindenGecSayac = 1

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("gray")
pencere.setup(width = 705,height = 705)
pencere.tracer(0) #ekranın kendini yenilememesi için

sYem = Yem("black",-330,110)
yYem = Yem("green",-330,50)
kYem = Yem("red",-330,-30)
tYem = Yem("orange",-330,-100)
mYem = Yem("blue",-330,-180)

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
bilgilendirme.goto(0,-250)
bilgilendirme.write("Hoş Geldiniz. Garip bir yılan oyunu ile karşı karşıyasınız.\nBu bölümü okumadan oyuna başlamayın, sonuçları acı olabilir.\n\nSiyah daire, yılanımızın kafasıdır.\nOk tuşları ile yönlendirebilirsiniz.\n\nYeşil daire, yılanın kuyruğudur\nBaşlangıçta 3 birim kuyruk ile başlanacaktır.\n\nYEMLER:\nKırmızı daireler, kalitesiz yemlerdir. \nBu yemler yılanın boyunu ancak bir birim artırabilir.\n\nTuruncu yemler, kaliteli yemlerdir.\nHer 5 kalitesiz yem yemenizin ardından,\nbir kaliteli yem yiyebilirsiniz. 15 puan değerindedir!!\n\nMavi yemler ise, ne olduğu belirsiz yemlerdir. \nBu yemler altın yemlerden sonra gelir. \nBunları yerken dikkatli olun!! \n\nOyuna geçmek için \"Space\" tuşuna basın. Başarılar.. ",align='center',font =('Courier',13,'bold'))

skorBilgi = turtle.Turtle()
skorBilgi.speed(0)
skorBilgi.color("black")
skorBilgi.penup()
skorBilgi.goto(200,300)
skorBilgi.hideturtle()

enYuksekSkor = 0
enYuksekSkorBilgi = turtle.Turtle()
enYuksekSkorBilgi.speed(0)
enYuksekSkorBilgi.color("black")
enYuksekSkorBilgi.penup()
enYuksekSkorBilgi.goto(0,300)
enYuksekSkorBilgi.hideturtle()

yavaslama = turtle.Turtle()
yavaslama.speed(0)
yavaslama.color("black")
yavaslama.penup()
yavaslama.goto(-330,300)
yavaslama.write("Yavaslama:",align='left',font =('Courier',13,'bold'))
yavaslama.hideturtle()

carpisma = turtle.Turtle()
carpisma.speed(0)
carpisma.color("black")
carpisma.penup()
carpisma.goto(-330,280)
carpisma.write("Çarpışma :",align='left',font =('Courier',13,'bold'))
carpisma.hideturtle()

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

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.goto(0,100)
yemek.shapesize(1)

yemekler = []

def atla(): 
    move()
    move()
    move()
    move()
    move()

def goUp():
    if kafa.direction != "down":
        if kafa.direction == "up":
            atla()
        elif len(yemekler)>0 and yemekler[0].ycor()-15 == kafa.ycor():
            print("Delaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'up'

def goDown():
    if kafa.direction != "up":
        if kafa.direction == "down":
            atla()
        elif len(yemekler)>0 and yemekler[0].ycor()+15 == kafa.ycor():
            print("Delaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'down'

def goRight():
    if kafa.direction != "left":
        if kafa.direction == "right":
            atla()
        elif len(yemekler)>0 and yemekler[0].xcor()-15 == kafa.xcor():
            print("Delaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'right'
def goLeft():
    if kafa.direction != "right":
        if kafa.direction == "left":
            atla()
        elif len(yemekler)>0 and yemekler[0].xcor()+15 == kafa.xcor():
            print("Delaydan kaynaklanan kafa çakışması engellendi.")
        else:
            kafa.direction = 'left'

def move():
    if kafa.direction == "up":
        y=kafa.ycor()
        kafa.sety(y+15)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y-15)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x+15)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x-15)

def yavasla():
    global turboSayici
    global turboBool
    global delayTutucu
    global delay
    if turboBool == True:
        #özellik kullanılıyor demektir.
        return
    delayTutucu = delay
    if turboSayici > 0:
        turboSayici = 30
        turboBool = True
        print("Yavaşlama becerisi aktif edildi.")

def icindenGec():
    global icindenGecBool
    global icindenGecSayac
    if icindenGecBool == True:
        return
    if icindenGecSayac > 0:
        icindenGecSayac = 100
        icindenGecBool = True
        print("Çarpışma becerisi aktif edildi.")




pencere.listen()
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

def tekrarBasla():
    oyunBitti()
    kafa.direction = "stop"
    for i in yemekler:
        i.goto(1000,1000) #kuyruğu ekran dışına taşıdık
    yemekler.clear()
    kafa.goto(0,0)
    global baslangicKuyrukSayaci
    baslangicKuyrukSayaci = 3
    global skor
    skor = -3
    global altinYemekSayaci
    altinYemekSayaci = 5
    yemekKonumuDegistir()
    yemek.color("red")
    global altinKuyrukSayaci
    altinKuyrukSayaci = 0
    global delay
    delay = 0.05
    global turboBool
    turboBool = False
    global turboSayici
    turboSayici = 1
    global icindenGecSayac
    icindenGecSayac = 1
    global icindenGecBool 
    icindenGecBool = False


def kuyrukEkle():
    kuyruk = turtle.Turtle()
    kuyruk.speed = 0
    kuyruk.shape("circle")
    kuyruk.color("green")
    kuyruk.penup()
    yemekler.append(kuyruk)
    global skor
    skor += 1

def oyunBitti():
    for i in range(4):
        for i in range(len(yemekler)-1,-1,-1): #tüm kuyruk beyaz yapıldı.
            yemekler[i].color("white")
        
        pencere.update()
        time.sleep(0.1)

        for i in range(len(yemekler)-1,-1,-1): #tüm kuyruk kırmızı yapıldı.
            yemekler[i].color("red")
        pencere.update()
        time.sleep(0.1)


def yemekYenildiMi():
    if kafa.distance(yemek)<10:
        return True
    else:
        return False

def yemekKonumuDegistir():
    xkonum = random.randint(-250,250)               #piksel uyuşmazlığı için ayarlamalar yapıldı.
    x = xkonum - (xkonum%15)
    ykonum = random.randint(-250,250)
    y = ykonum - (ykonum%15)
    yemek.goto(x,y)



def kuyrukTakibi():
    for i in range(len(yemekler)-1,0,-1):           #uzunluktan -1 ekleyerek sıfıra kadar.
        x = yemekler[i-1].xcor()
        y = yemekler[i-1].ycor()
        yemekler[i].goto(x,y)
    
    if len(yemekler) >= 1:                          #ilk düğüm için başı takip etmesi gerektiğini söyledik. aşağıda başı bir sonraki hedefe alıyoruz.
        x = kafa.xcor()
        y = kafa.ycor()
        yemekler[0].goto(x,y)


def kuyrukYemekCakismasi():
    for i in range(len(yemekler)-1,0,-1):
        if yemekler[i].xcor() == yemek.xcor() and yemekler[i].ycor() == yemek.ycor():
            print("Yemek ile kuyruk çakıştı. Tekrar yemek ataması yapılıyor.")
            return True
        else:
            False

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

def rastGele():
    i = random.randint(0,5)
    return i

while True:
    time.sleep(0.1)
    if keyboard.is_pressed('space'):
        mYem.goto(1000,1000)
        sYem.goto(1000,1000)
        tYem.goto(1000,1000)
        kYem.goto(1000,1000)
        yYem.goto(1000,1000)
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
    
    
def yenilenYemegeGoreEtkiYap():
    global altinYemekSayaci
    global skor
    global altinKuyrukSayaci

    if yemek.color() == ('red','red'): #eğer kırmızı yemek yenildi ise bir sonraki altın yemek için sayac başlatılıyor.
        altinYemekSayaci -= 1
        kuyrukEkle() #kırmızı yemek yenildiğinde bir kuyruk ekleniyor
        print("Kırmızı yem yenildi: Skor +1")

    elif yemek.color() == ('orange','orange'): #burada altın yemek yenildiyse sayac tekrardan hazırlanıyor ve bir sonraki yemeğin rengi kırmızı yapılıyor.
        global delay
        altinKuyrukSayaci = 10
        altinYemekSayaci = 5
        if delay > 0.01:
            print("Hız %20 oranında artırıldı.")
            delay -= 0.01
        else:
            print("Hız maksimumda, tebrikler fena değilsiniz.")
            delay = 0.005
        yemek.color("blue")
        print("Altın yem yenildi: Skor +15")

    else:
        #burda rastgele bir işlem yapıcaz.
        i = rastGele()
        if i==0:
            altinYemekSayaci=0
            kuyrukEkle()
            print("Mavi yem yenildi. +1 puan kazanıldı. Ayrıca bir sonraki yem altın yem yapıldı.")
        elif i==1:
            print("Mavi yem yenildi. -5 puan kaybedildi.")
            skor -=5
            for i in range(5):
                yemekler[len(yemekler)-1].goto(1000,1000)
                yemekler.pop()
            yemek.color("red")
        elif i==2:
            print("Mavi yem yenildi. -15 paun kaybedildi.")
            skor -= 15
            for i in range(15):
                yemekler[len(yemekler)-1].goto(1000,1000)
                yemekler.pop()
            yemek.color("red")
        else:
            print("Mavi yem yenildi. +5 puan kazanıldı.")
            altinKuyrukSayaci = 5
            yemek.color("red")
    
def altinYemekMi():
    if altinYemekSayaci == 0: #eğer altın yemek sayacı 0'a ulaştıysa bir sonraki yemek altın yemek olduğu anlamına geliyor.
        yemek.color("orange")

def baslangicKuyrukEklemesi():
    global baslangicKuyrukSayaci
    if baslangicKuyrukSayaci>0 and kafa.direction!="stop": #program başlangıcında kuyrukların kafa ile çarpışmasını engellemek için
        kuyrukEkle()
        baslangicKuyrukSayaci -= 1 #başlangıçta 3 kuyruk ile başlaması kuralı koyuyoruz.

def altinYemYenildi():
    global altinKuyrukSayaci
    if altinKuyrukSayaci > 0 :#altın yem yenildiği takdirde altınKuyruk sayacı 10 yapılıyor.
        #her adımda bir yeni bir kuyruk eklenmesi için. Eğer bir adımda hepsini eklersek, kuyruk takibinde sıkıntı çıkar.
        kuyrukEkle()
        altinKuyrukSayaci -= 1

def atama():
    global delayTutucu
    delayTutucu = delay

def turboKontrol():
    global delay
    global turboSayici
    global turboBool#sayac 0
    global delayTutucu
    if turboSayici > 0: #şuanda kullanılıyor.
        delay = 0.15
        turboSayici -= 1
        yavaslamaDurumu.color("lightgreen")
    else:   #şuanda kullanılamaz durumda, hazırlanma sürecinde.
        delay = delayTutucu
        turboSayici = -200
        turboBool = False
        yavaslamaDurumu.color("red")
        print("Yavaşlatma becerisinin kullanım süresi doldu. Tekrar kullanım için hazırlanıyor")

def ozellikKontrol():
    global turboSayici
    if turboBool:                                       #yavaşlama becerisinin kontrolü gerçekleştiriliyor.
        turboKontrol()
    elif turboBool==False and kafa.direction != "stop": #eğer beceri kullanılmıyorsa ve yılan hareket ediyorsa şuanda kullanılabilir hale getiriliyor.
        turboSayici += 1
        if turboSayici==0:
            print("Yavaşlama becerisi kullanıma hazır.")
            yavaslamaDurumu.color("green")


def icindenGecKontrol():
    global icindenGecSayac
    global icindenGecBool
    if icindenGecBool and icindenGecSayac > 0:  #true yapıldı ve 30 atandı. Kullanılıyor şuanda
        icindenGecSayac -= 1                    #her adımda bir azaltılıyor. hala true olarak kalıyor.
        carpismaDurumu.color("lightgreen")
        if icindenGecSayac == 0:                #özellik kullanımı bitti, şimdi kullanılamaz hale getirmem lazım.
            icindenGecSayac = -200              #200 birim sonra kullanılabilir hale gelicek
            icindenGecBool = False
            carpismaDurumu.color("red")
            print("Çarpışma becerisinin kullanımı doldu. Geçici bir süre kullanılamayacak.")
    else:
        icindenGecSayac += 1                    #her adımda sayacımızı +1 artırıyoruz.

    if icindenGecBool == False and icindenGecSayac < 0:
        carpismaDurumu.color("red")
        if icindenGecSayac+1 == 0:
            carpismaDurumu.color("green")
            print("Çarpışma becerisi kullanıma hazır.")
        


while True:
    time.sleep(delay)
    icindenGecKontrol()
    ozellikKontrol()                            # x tuşuna basıp özelliği aktif etti mi diye kontrol ediyoruz.
    enYuksekSkorKontrol()                       #en yüksek skorun kotrolü gerçekleştiriliyor. Eğer skor daha büyükse, en yüksek skorda ona eşit yapılıyor.
    skorGuncelle()                              #başlangçta skoru -3ten başlattığım için o gözükmesin diye buraya bir karşılaştırma yapısı eklendi.
    if yemekYenildiMi():                        #bir yemek yenildiyse aşağıdaki işlemler uygulanacak.
        yenilenYemegeGoreEtkiYap()              #yenilen yemeğe göre yılanımızda değişiklikler olacaktır. Hareket hızı, uzama vs.
        altinYemekMi()                          #bir sonraki yemin altın yemek olup olmadığı burada ayarlanıyor.
        yemekKonumuDegistir()                   #bir sonraki yemin konumu ayarlanıyor.
        while(kuyrukYemekCakismasi()):          #çakışma durumu varsa eğer tekrar yemeğin konumu ayarlanıyor.
            yemekKonumuDegistir()
        renkSayaci = 7                          # bu sayac, kafa renginin yeme işleminden sonra 2 adımda bir değişebilmesi için gerekli.
    renkSayaci = kafaRengiAyarla(renkSayaci) 
    kuyrukKafaCakismasi()                       #kafanın kuyrukta herhangi bir bölüme çarpmasında oyun sona eriyor. Baştan tekrar başlatılıyor.
    kenaraCarpma()                              #Kafanın kenara çarpması durumunda yeniden başlatılması için yazılıyor.
    baslangicKuyrukEklemesi()                   #başlangıçta 3 birim kuyruk eklenmesi için kullanılıyor.
    altinYemYenildi()                           #yenilen yem altın yem ise her adımda kuyruk eklemesi gerçekleştirebilmek için gerekli.
    kuyrukTakibi()                              #kuyruğun kafayı takip etme olayını burada gerçekleştiriliyor. Her bir kuyruk kendisinden önceki kuyruğun yerini alıyor
    move()                                      #hareket fonksiyonu, yılanı 1 birim hareket ettiriyor
    pencere.update()                            #her bir adımın görüntülenmesi için pencere güncelleniyor.+
