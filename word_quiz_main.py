from word_quiz import WUi_Form
from soru_alani import SUi_Form
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QGridLayout,QPushButton,QListWidget
import random
import kaynak

kelimeler = ["admiration", "architecture", "blame", "boredom", "bravery", "comprehension", "correspondence",
                 "estimation",
                 "evidence", "excitement", "foolishness", "generosity", "evolution", "gravity", "hardware",
                 "integration", "knowledge", "legislation",
                 "leisure", "momentum", "participation", "poetry", "pollution", "poverty", "pride", "significance",
                 "slang", "superiority",
                 "violence", "wisdom"]



anlamlari = {"admiration": "hayranlık",  # admiration 0
                 "architecture":"mimari",  # architecture 1
                 "blame":"suç",  # blame 2
                 "boredom":"sıkıntı",  # boredom 3
                 "bravery":"cesurluk",  # bravery 4
                 "comprehension":"anlama",  # comprehension 5
                 "correspondence":"yazışma",  # correspondence 6
                 "estimation":"tahmin",  # estimation 7
                 "evidence":"kanıt",  # evidence 8
                 "excitement":"heyecan",  # excitement 9
                 "foolishness":"aptallık",  # foolishness 10
                 "generosity":"cömertlik",  # generosity 11
                 "evolution":"evrim",  # evolution 12
                 "gravity":"yerçekimi",  # gravity 13
                 "hardware":"donanım",  # hardware 14
                 "integration":"bütünleşme",  # integration 15
                 "knowledge":"bilgi",  # knowledge #16
                 "legislation":"yasa koyma",  # legislation 17
                 "leisure":"boş vakit",  # leisure 18
                 "momentum":"ivme",  # momentum 19
                 "participation":"katılma",  # participation 20
                 "poetry":"şiir",  # poetry 21
                 "pollution":"kirlilik",  # pollution 22
                 "poverty":"yoksulluk",  # poverty 23
                 "pride":"gurur",  # pride 24
                 "significance":"önem",  # significance 25
                 "slang":"argo",  # slang 26
                 "superiority":"üstünlük",  # superiority 27
                 "violence":"şiddet",  # violence 28
                 "wisdom":"bilgelik"  # wisdom 29
             }

#----------------------------------------------------------


class Soru(QWidget,SUi_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.insertItem(0,"Cevaplarınız:")

        self.dogru = 0
        self.yanlis = 0
        self.kalankelime = 30
        self.suanki_kelime = ""
        self.yanlis_kelimeler = []
        self.yeni_soru()


        self.tamam.clicked.connect(self.kontrol)



    def kontrol(self):



        if self.verigirisi.text() == anlamlari[self.suanki_kelime]:


            if self.kalankelime > 0:
                self.listWidget.addItem(self.verigirisi.text())


            self.dogru+=1
            self.kalankelime-=1

            if self.kalankelime == 0:
                self.sonuc_ekrani()

            self.kalan_kelime.setText("Kalan kelime:{}".format(self.kalankelime))



        elif self.verigirisi.text() != anlamlari[self.suanki_kelime]:


            if self.kalankelime > 0:
                self.listWidget.addItem(self.verigirisi.text())


            self.yanlis+=1
            self.kalankelime-=1


            if self.kalankelime == 0:
                self.sonuc_ekrani()


            self.kalan_kelime.setText("Kalan kelime:{}".format(self.kalankelime))

            self.yanlis_kelimeler+=["-"*30,"Sizin cevabınız: {}".format(self.verigirisi.text()),
                                   "Doğrusu: {} / {}".format(anlamlari[self.suanki_kelime],self.suanki_kelime)]

        self.yeni_soru()




    def sonuc_ekrani(self): #Sonuç ekranı.
        self.tamam.setEnabled(False)
        self.sonuc = QWidget()
        self.sonuc.setWindowTitle("Sonuçlarınız!")
        self.sonuc.setWindowIcon(QIcon(":/resim/logo_wq.ico"))
        self.sonuc.resize(500,150)
        self.sonuc.setMaximumSize(500,150)
        self.sonuc.setMinimumSize(500,150)

        self.layout2 = QGridLayout(self.sonuc)

        self.dogrusayisi = QLabel(self.sonuc)
        self.dogrusayisi.setText("Doğru sayınız: {}".format(self.dogru))

        self.yanlissayisi = QLabel(self.sonuc)
        self.yanlissayisi.setText("Yanlış sayınız: {}".format(self.yanlis))

        self.yanlis = QListWidget(self.sonuc)
        self.yanlis.insertItem(0,"Yanlış cevapladıklarınız:")
        self.yanlis.insertItems(1, self.yanlis_kelimeler)

        self.tekrar_coz = QPushButton(self.sonuc)
        self.tekrar_coz.setText("Tekrar Çöz!")
        self.tekrar_coz.clicked.connect(self.yeniden_coz)

        self.layout2.addWidget(self.dogrusayisi,0,0,1,1)
        self.layout2.addWidget(self.yanlissayisi,1,0,1,1)
        self.layout2.addWidget(self.yanlis,0,1,3,1)
        self.layout2.addWidget(self.tekrar_coz,2,0,1,1)

        self.sonuc.show()




    def yeniden_coz(self):
        self.sonuc.close()
        self.close()
        pencere.show()





    def yeni_soru(self):

        self.verigirisi.clear()
        self.suanki_kelime = self.kelime_uret()
        self.kelime.setText(self.suanki_kelime)





    def kelime_uret(self):

        return random.choice(list(anlamlari.keys())) # Burada random olarak bir kelime seçtik.



#--------------------------------------------------------


class Baslangic(WUi_Form,Soru): #Başlangıç ekranı

        def __init__(self):
            super(Soru,self).__init__()
            self.setupUi(self)
            self.basla.clicked.connect(self.goster)



        def goster(self): # Bu fonksiyon sayesinde soru ekranı gösteriliyor
            pencere.close()
            self.yenipen = Soru()
            self.yenipen.show()




app = QApplication([])
pencere = Baslangic()
pencere.show()
app.exec_()