# --------------------------------------------------------------
#  DL_QRCODE_GENERATOR.py
#  Version: v01.1
#  Author: Danilo de Lucio
#
#  Last Modified by: Danilo de Lucio
#  Last Updated: September 23th, 2021
# --------------------------------------------------------------

import pyqrcode
import png
from pyqrcode import QRCode
import time

def error_msg():
    print("-" * 55)
    print("ERROR! Please choose one option above and try again!")
    print("-" * 55)

def sucess_msg():
    print("-" * 57)
    print("DONE! Your QR Code was generated and saved successfully!")
    print("-" * 57)

def welcome_msg():
    print("-" * 32)
    print("WELCOME TO DL_QRCODE_GENERATOR!")
    print("-" * 32)

def end_msg():
    print("")
    print("-" * 43)
    print("Thanks for using my humble app my friend!")
    print("")
    print("Developed by: Danilo de Lucio")
    print("https://www.danilodelucio.com/")
    print("https://github.com/danilodelucio")
    print("-" * 43)

welcome_msg()

while True:
    print("")
    # Content generate QRCode
    link = input(str("Content to generate QRCode: "))

    # Generating the QRCode
    url = pyqrcode.create(link)

    # File name
    file_name = str(input("File name: "))

    # File Resolution
    file_res = ""
    while True:
        file_res = str(input("Resolution: \n- [1] Low; \n- [2] Medium; \n- [3] High; \n"))

        if file_res == "1":
            file_res = 8
            break
        if file_res == "2":
            file_res = 20
            break
        if file_res == "3":
            file_res = 50
            break
        else:
            error_msg()
            continue

    # File Format
    file_format = ""
    while True:
        print("")
        file_format = str(input("File format: \n- [1] PNG; \n- [2] JPG; \n"))

        if file_format == "1":
            file_format = "png"
            break
        if file_format == "2":
            file_format = "jpg"
            break

        else:
            error_msg()
            continue


    # Saving the QRCode
    url.png(rf'{file_name}.{file_format}', scale=file_res)
    sucess_msg()

    # Asking if the user wants to generate another QRCode or not
    ask = ""
    while True:
        print("")
        ask = str(input("Would you like to generate another one? \n- [1] Yes; \n- [2] No; \n"))
        if ask in "12":
            break

        else:
            error_msg()
            continue

    if ask == "1":
        continue
    if ask == "2":
        break


# Credits
end_msg()
time.sleep(5)