#!/bin/python3

import os

os.system("clear")

info = "[+] Realtek Semiconductor Co., Ltd\n\
[+] Wireless Network Adapter\n----------------------------\n\
[+] Installer of RTL8821CE for Debian-based distributions"

print(info) 
print("[+] Controller by Tomas Pinho -> https://github/tomaspinho")
print("[+] Installer by Esteban Buror -> https://github/aburgoaor\n")

value = input("[+] Want to proceed with the installation? (y or n): ")

if value.lower() == "y" or value.lower() == "s":
	os.system("clear")
	print(info)
	print("\n[+] Downloading driver rtl8821ce...")
	os.system("git clone https://github.com/tomaspinho/rtl8821ce")

	os.system("clear")
	print(info)
	print("\n[+] Installing driver...")
	os.chdir("rtl8821ce/")
	# REALIZA LA INSTALACION DEL CONTROLADOR

	os.system("clear")
	print(info)
	print("\n[+] Installation complete...")
	reboot = input("[+] Do you want restart now? (y or n): ")
	if reboot.lower() == "y" or reboot.lower() == "s":
		print("[+] Thanks to install, enjoy!\n[+] Reestarting...")
		os.system("reboot")
	else:
		os.system("clear")
		print(info)
		print("\n[+] Thanks to install, enjoy!")

else:
	os.system("clear")
	print(info)
	print("\n[+] Good bye :)")
