# -*-coding: utf8 -*-
from tkinter import *
from Crypto.Cipher import DES
import base64


def pad(s):
    # Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)


def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    denctxt.delete(0, END)
    denctxt.insert(INSERT, detxt)


window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb = Label(window, text="Văn bản gốc", font=("Arial", 14))
plainlb.grid(column=0, row=3)

plaintxt = Entry(window, width=75)
plaintxt.grid(column=1, row=3)

keylb = Label(window, text="Khoá", font=("Arial", 14))
keylb.grid(column=0, row=4)

keytxt = Entry(window, width=75)
keytxt.grid(column=1, row=4)

cipherlb = Label(window, text="Văn bản được mã hoá", font=("Arial", 14))
cipherlb.grid(column=0, row=5)

ciphertxt = Entry(window, width=75)
ciphertxt.grid(column=1, row=5)

denclb = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
denclb.grid(column=0, row=6)

denctxt = Entry(window, width=75)
denctxt.grid(column=1, row=6)

DESbtn = Button(window, text="Mã Hóa", command=mahoa_DES)
DESbtn.grid(column=0, row=7)

DEDESbtn = Button(window, text="Giải Mã", command=giaima_DES)
DEDESbtn.grid(column=1, row=7)

window.geometry('800x600')
window.mainloop()
