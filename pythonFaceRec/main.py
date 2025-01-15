#OPENCV Görüntü İşleme Paketi kullanıldı
import cv2
#EKRANA GÖRÜNTÜ İŞLEME SONRAIS ANALİZ PAKETİ    
import numpy as np

import tkinter as tk
from tkinter import filedialog



#frontalface_default ile Ön Yüzün genel hatları tarandı
face_cascade = cv2.CascadeClassifier(r"classifier/haarcascade_frontalface_default.xml")
#VideoCapture fonksiyonu ile video içeri aktarıldı
#DÖNGÜ OLUŞTURULARAK VİDEONUN TARANMASI SAĞLANDI
font = cv2.FONT_HERSHEY_PLAIN  # Yazı tipi
bottomLeftCorner = (5, 20)  # Açıklama metninin sol alt köşesi
fontColor = (255, 255, 255)  # Yazı rengi
boxColor = (0, 0, 0)  # Kutucuk rengi
fontScale=1
thickness=0
pencere = tk.Tk()
pencere.title("Dosya Seç")
def add_description(frame, text):
    cv2.putText(frame, text, (160, 0), font, fontScale, fontColor, thickness)

dosya_stringi=""
def dosya_sec():
    dosya_yolu = filedialog.askopenfilename()
    if dosya_yolu:
        dosya_etiketi.config(text=dosya_yolu)
        return dosya_yolu
        

dosya_secme_butonu = tk.Button(pencere, text="Dosya Seç", command=dosya_sec)
dosya_secme_butonu.pack()

dosya_etiketi = tk.Label(pencere, text="Seçilen Dosya Yok")
dosya_etiketi.pack()
dosya_stringi = dosya_sec()
print(dosya_stringi)
cap = cv2.VideoCapture(dosya_stringi)


while cap.isOpened():
    _,img = cap.read()
    """
    img = cv2.imread(r"photos/a.jpg")
    bu kod ile resimden de yüz tespiti yapilarak tarama yapilabilir
    """
    #YUZU KARE İÇİNE ALACAK ŞEKLİ AKTARMA
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #KAREYİ YÜZE SABİTLEME
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)
        # Tespit Edilen Yüz Sayısını Hesapla
        face_count = len(faces)
        # Sağ Üst Köşeye Kutucuk Oluştur
        cv2.rectangle(img, (0, 0), (150, 40), boxColor, -1)
        # Yüz Sayısını Yazdır
        cv2.putText(img, f"Yuz Sayisi: {face_count}", bottomLeftCorner, font, 
            fontScale, fontColor, thickness)
    add_description(img, "INFO")
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
