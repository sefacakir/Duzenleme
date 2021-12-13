import turtle
import time
import random
import keyboard
from Yem import Yem

delay = 0.05
skor = -3       
kingSkor = 0    
turboBool = False   

delaySayaci = 10    
renkSayaci = 0           
baslangicKuyrukSayaci = 3   
altinYemekSayaci = 5    
altinKuyrukSayaci = 0   
turboSayici = 1     
delayTutucu = 0     

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("gray")
pencere.setup(width=700,height=700)
pencere.tracer(0) 

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

ozellik = turtle.Turtle()
ozellik.speed(0)
ozellik.color("black")
ozellik.penup()
ozellik.goto(-330,300)
ozellik.write("Ozellik:",align='left',font =('Courier',13,'bold'))
ozellik.hideturtle()

ozellikDurumu = turtle.Turtle()
ozellikDurumu.speed(0)
ozellikDurumu.shape("circle")
ozellikDurumu.color("lightgreen")
ozellikDurumu.penup()
ozellikDurumu.goto(-240,310)
ozellikDurumu.shapesize(0.5)

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.goto(0,100)
yemek.shapesize(1)

yemekler = []

def goUp():
    if kafa.direction != "down":
        if kafa.direction == "up":
            move()
            move()
            move()
            move()

        elif len(yemekler)>0 and yemekler[0].ycor()-15 == kafa.ycor():
            print("Çarpışma önlendi.")
        else:
            kafa.direction = 'up'

def goDown():
    if kafa.direction != "up":
        if kafa.direction == "down":
            move()
            move()
            move()
            move()
        elif len(yemekler)>0 and yemekler[0].ycor()+15 == kafa.ycor():
            print("Çarpışma önlendi.")
        else:
            kafa.direction = 'down'

def goRight():
    if kafa.direction != "left":
        if kafa.direction == "right":
            move()
            move()
            move()
            move()
        elif len(yemekler)>0 and yemekler[0].xcor()-15 == kafa.xcor():
            print("Çarpışma önlendi.")
        else:
            kafa.direction = 'right'
def goLeft():
    if kafa.direction != "right":
        if kafa.direction == "left":
            move()
            move()
            move()
            move()
        elif len(yemekler)>0 and yemekler[0].xcor()+15 == kafa.xcor():
            print("Çarpışma önlendi.")
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
    delayTutucu = delay
    if turboSayici > 0:
        turboSayici = 30
        turboBool = True


pencere.listen()
pencere.onkeypress(goUp, 'Up')
pencere.onkeypress(goDown, 'Down')
pencere.onkeypress(goRight, 'Right')
pencere.onkeypress(goLeft, 'Left')
pencere.onkeypress(yavasla,'x')


def beyazKafa():
    kafa.color("white")

def siyahKafa():
    kafa.color("black")

def tekrarBasla():
    oyunBitti()
    kafa.direction = "stop"
    for i in yemekler:
        i.goto(1000,1000) 
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


def kuyrukEkle():
    kuyruk = turtle.Turtle()
    kuyruk.speed = 0
    kuyruk.shape("circle")
    kuyruk.color("green")
    kuyruk.penup()
    yemekler.append(kuyruk)
    global skor
    skor += 1
#    print("Skor: {}".format(skor))

def oyunBitti():
    value = 3
    if len(yemekler)<10:
        value = 3
    elif len(yemekler)<20:
        value = 2
    else:
        value = 1

    for i in range(value):
        for i in range(len(yemekler)-1,-1,-1): 
            yemekler[i].color("white")
            pencere.update()
            time.sleep(0.02)

        for i in range(len(yemekler)-1,-1,-1):
            yemekler[i].color("red")
            pencere.update()
            time.sleep(0.02)


def yemekYenildiMi():
    if kafa.distance(yemek)<10:
        return True
    else:
        return False

def yemekKonumuDegistir():
    xkonum = random.randint(-250,250) 
    x = xkonum - (xkonum%15)
    ykonum = random.randint(-250,250)
    y = ykonum - (ykonum%15)
    #print("Yemek konumu: ",x,y)
    yemek.goto(x,y)



def kuyrukTakibi():
    for i in range(len(yemekler)-1,0,-1):
        x = yemekler[i-1].xcor()
        y = yemekler[i-1].ycor()
        yemekler[i].goto(x,y)
    
    if len(yemekler) >= 1: 
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

    if yemek.color() == ('red','red'): 
        altinYemekSayaci -= 1
        kuyrukEkle() 
        
    elif yemek.color() == ('orange','orange'): 
        global delay
        altinKuyrukSayaci = 10
        altinYemekSayaci = 5
        delay -= 0.01
        yemek.color("blue")

    else:
        i = rastGele()
        if i == 0:
            print("Puan kazanılmadı.")
            yemek.color("red")
        elif i==1:
            altinYemekSayaci=0
            print("Bir sonraki yemek altın yemek olacak.")
        elif i==2:
            print("5 kuyruk silindi.")
            skor -=5
            for i in range(5):
                yemekler[len(yemekler)-1].goto(1000,1000)
                yemekler.pop()
        elif i==3:
            print("-15 puan")
            skor -= 15
            for i in range(15):
                yemekler[len(yemekler)-1].goto(1000,1000)
                yemekler.pop()
        else:
            print("5 kuyruk eklendi.")
            altinKuyrukSayaci = 5
            yemek.color("red")
    
def altinYemekMi():
    if altinYemekSayaci == 0: 
        yemek.color("orange")

def baslangicKuyrukEklemesi():
    global baslangicKuyrukSayaci
    if baslangicKuyrukSayaci>0 and kafa.direction!="stop": 
        kuyrukEkle()
        baslangicKuyrukSayaci -= 1 

def altinYemYenildi():
    global altinKuyrukSayaci
    if altinKuyrukSayaci > 0 :
        kuyrukEkle()
        altinKuyrukSayaci -= 1

def atama():
    global delayTutucu
    delayTutucu = delay

def turboKontrol():
    global delay
    global turboSayici
    global turboBool
    global delayTutucu
    if turboSayici > 0:
        delay = 0.15
        turboSayici -= 1
    else:
        delay = delayTutucu
        turboSayici = -200
        turboBool = False

def ozellikKontrol():
    global turboSayici
    if turboBool: 
        turboKontrol()
    elif turboBool==False and kafa.direction != "stop":
        turboSayici += 1
    
    if turboBool == False and turboSayici > 0:
        ozellikDurumu.color("lightgreen")
    else:
        ozellikDurumu.color("red")

while True:
    time.sleep(delay)
    ozellikKontrol()       
    enYuksekSkorKontrol()   
    skorGuncelle()          
    if yemekYenildiMi():  
        yenilenYemegeGoreEtkiYap()
        altinYemekMi()
        yemekKonumuDegistir() 
        while(kuyrukYemekCakismasi()): 
            yemekKonumuDegistir()
        renkSayaci = 7 
    renkSayaci = kafaRengiAyarla(renkSayaci) 
    kuyrukKafaCakismasi() 
    kenaraCarpma() 
    baslangicKuyrukEklemesi()
    altinYemYenildi()
    kuyrukTakibi() 
    move()  
    pencere.update() 
