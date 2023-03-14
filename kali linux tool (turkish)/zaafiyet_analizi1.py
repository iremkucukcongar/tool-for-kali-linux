#!/usr/bin/env python
import os
os.system("apt-get insall figlet")
os.system("clear")
os.system("figlet ZAAFIYET ANALIZI")
print("""
zaafiyet analizine hoşgeldiniz
""")
hedef_ip = input("Hedef Ip Girin :")
os.system("nikto -h " + hedef_ip)
