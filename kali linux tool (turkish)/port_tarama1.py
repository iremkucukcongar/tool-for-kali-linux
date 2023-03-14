#!/usr/bin/env/python
import os
os.system("apt get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port Tarama Aracına Hoşgeldiniz :)
1)HIZLI TARAMA
2)SERVİS VE VERSİYON BİLGİSİ
3)İSLETİM SİSTEMİ BİLGİSİ

""")
islemno = input("İşlem Numarasını Girin : ")
if(islemno=="1"):
    hedefip = input("Hedef Ip Girin:")
    os.system("nmap " + hedefip)
elif(islemno=="2"):
    hedefip = input("Hedef Ip Gİrin:" )
    os.system("nmap -sS -sV" + hedefip)
elif(islemno=="3"):
    hedefip = input("Hedef Ip Gİrin:" )
    os.system("nmap -0 " + hedefip)
else:
   print("Hatalı seçim")
   
