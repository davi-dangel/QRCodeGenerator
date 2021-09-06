import pyqrcode
import png
from pyqrcode import QRCode
import validators
import sys
import os

extension = '.png'

def main():
    qrcode_url = link_input()
    qrcode_name = qrcode_name_inputs()
    generate_qrcode(qrcode_url, qrcode_name)

def link_input():
    link = input("Entre com o link desejado: ")
    validate_link(link)
    return link

def validate_link(link):
    if not validators.url(link):
        print("Seu Link não é válido")
        sys.exit()

def qrcode_name_inputs():
    name = input("Entre com o nome do QRCode: ")
    validate_name(name)
    return name

def validate_name(name):
    if len(name) == 0:
        print("Você precisa inserir um nome")
        sys.exit()

def generate_qrcode(link, name):
    qrcode = pyqrcode.create(link)

    png_name = name + extension
    save_qrcode(png_name, qrcode)
    

def save_qrcode(png_name, qrcode):
    try:
        qrcode.png('C:\QRCode\\' + png_name, scale=8)
    except:
        qrcode.png(png_name, scale=8)


main()