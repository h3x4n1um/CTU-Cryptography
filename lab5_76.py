# Họ và tên sinh viên: Nguyễn Thanh Hoàng Hải
# Mã số sinh viên: B1812339
# STT: 76

# -*-coding: utf8 -*-
from tkinter import *

from Crypto.Cipher import DES
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from tkinter import filedialog

import base64
import tkinter as tk



##################################################
# Affine dependencies                            #
##################################################

def Char2Num(c):
        return ord(c)-65

def Num2Char(n):
    return chr(n+65)

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 -q * x1
        y0, y1 = y1, y0 -q * y1
    if x0 < 0: x0 = temp+x0
    return x0

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

def decryptAF(txt,a,b,m):
    r = ""
    a1 = xgcd(a,m)
    for c in txt:
        e = (a1*(Char2Num(c)-b )) % m
        r = r+Num2Char(e)
    return r



##################################################
# DES dependencies                               #
##################################################

def pad(s):
    #Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 -len(s) % 8) * chr(8 -len(s) % 8)
    
def unpad(s):
    return s[:-ord(s[len(s)-1:])]



##################################################
# RSA dependencies                               #
##################################################

def save_file(content, _mode, _title, _filetypes, _defaultextension):
        f = filedialog.asksaveasfile(
            mode = _mode,
            initialdir = "C:/",
            title = _title,
            filetypes = _filetypes,
            defaultextension = _defaultextension)

        if f is None:
            return
        f.write(content)
        f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(
        initialdir = "C:/",
        title = "Open " + key_style,
        filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
    if filename is None:
        return
    file = open(filename,"rb")
    key = file.read()
    file.close()

    return RSA.importKey(key)



class MAHOA_Affine(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x600')

        # Them cac control
        self.lb0 = Label(self, text=" ",font=("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)

        self.lbl = Label(self, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(self, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
        self.lb2.grid(column=0, row=2)

        self.plainlb3 = Label(self, text="PLAIN TEXT",font=("Arial", 14))
        self.plainlb3.grid(column=0, row=3)

        self.plaintxt = Entry(self,width=20)
        self.plaintxt.grid(column=1, row=3)

        self.KEYlb4 = Label(self, text="KEY PAIR",font=("Arial", 14))
        self.KEYlb4.grid(column=2, row=3)

        self.KEYA1 = Entry(self,width=3)
        self.KEYA1.grid(column=3, row=3)

        self.KEYB1 = Entry(self,width=5)
        self.KEYB1.grid(column=4, row=3)

        # Hoc vien bo sung code tai day
        # de co duoc giao dien nhuyeu cau cua bai toan
        # ...
        self.cipherlb3 = Label(self, text="CIPHER TEXT",font=("Arial", 14))
        self.cipherlb3.grid(column=0, row=4)

        self.ciphertxt3 = Entry(self,width=20)
        self.ciphertxt3.grid(column=1, row=4)

        self.decrypttxt = Entry(self,width=20)
        self.decrypttxt.grid(column=3, row=4)

        # Tao nut co ten AFbtn
        self.AFbtn = Button(self, text="Mã Hóa", command=self.mahoa)
        self.AFbtn.grid(column=5, row=3)

        # Hoc vien bo sung code de tao nut co ten la DEAFbtn
        # ...
        self.DEAFbtn = Button(self, text="Giải Mã", command=self.giaima)
        self.DEAFbtn.grid(column=2, row=4)

        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=5)

    def mahoa(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = encryptAF(self.plaintxt.get(),a,b,m)
        self.ciphertxt3.delete(0,END)
        self.ciphertxt3.insert(INSERT,entxt)

    def giaima(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = decryptAF(self.ciphertxt3.get(),a,b,m)
        self.decrypttxt.delete(0,END)
        self.decrypttxt.insert(INSERT,entxt)



class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x600')

        self.lbl = Label(
            self,
            text="CHƯƠNG TRÌNH DEMO",
            font=("Arial Bold", 20)
        )
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(
            self,
            text="MẬT MÃ ĐỐI XỨNG DES",
            font=("Arial Bold", 15)
        )
        self.lb2.grid(column=1, row=2)
        
        self.plainlb3 = Label(
            self,
            text="Văn bản gốc",
            font=("Arial", 14)
        )
        self.plainlb3.grid(column=0, row=4)
        
        self.plaintxt = Entry(self,width=100)
        self.plaintxt.grid(column=1, row=4)
        
        self.lb4 = Label(
            self,
            text="Khóa",
            font=("Arial", 14)
        )
        self.lb4.grid(column=0, row=5)
        
        self.keytxt = Entry(self,width=100)
        self.keytxt.grid(column=1, row=5)
        
        self.lb5 = Label(
            self,
            text="Văn bản được mã hóa",
            font=("Arial", 14)
        )
        self.lb5.grid(column=0, row=6)
        
        self.ciphertxt = Entry(self,width=100)
        self.ciphertxt.grid(column=1, row=6)
        
        self.lb6 = Label(
            self,
            text="Văn bản được giải mã",
            font=("Arial", 14)
        )
        self.lb6.grid(column=0, row=7)
        
        self.denctxt = Entry(self,width=100)
        self.denctxt.grid(column=1, row=7)
        
        self.btn_enc = Button(
            self,
            text="Mã Hóa",
            command=self.mahoa_DES
        )
        self.btn_enc.grid(column=1, row=9)
        
        self.btn_dec = Button(
            self,
            text="Giải Mã ",
            command=self.giaima_DES
        )
        self.btn_dec.grid(column=1, row=10)
        
        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=11)
    
    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode()
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)
        
    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.denctxt.delete(0,END)
        self.denctxt.insert(INSERT,detxt)



class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa bất đối xứng")
        self.geometry('800x600')

        self.lb0 = Label(self, text=" ",font=("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)

        self.lbl = Label(self, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(self, text="MẬT MÃ BẤT ĐỐI XỨNG RSA",font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)

        self.plainlb = Label(self, text="Văn bản gốc",font=("Arial", 14))
        self.plainlb.grid(column=0, row=3)

        self.plaintxt = Entry(self,width=75)
        self.plaintxt.grid(column=1, row=3)

        self.cipherlb = Label(self, text="Văn bản được mã hoá",font=("Arial", 14))
        self.cipherlb.grid(column=0, row=4)

        self.ciphertxt = Entry(self,width=75)
        self.ciphertxt.grid(column=1, row=4)

        self.denclb = Label(self, text="Văn bản được giải mã",font=("Arial", 14))
        self.denclb.grid(column=0, row=5)

        self.denctxt = Entry(self,width=75)
        self.denctxt.grid(column=1, row=5)

        self.pri_keylb = Label(self, text="Khóa cá nhân",font=("Arial", 14))
        self.pri_keylb.grid(column=0, row=6)

        self.pri_key = Text(self, height=7, width=75)
        self.pri_key.grid(column=1, row=6)

        self.pub_keylb = Label(self, text="Khóa công khai",font=("Arial", 14))
        self.pub_keylb.grid(column=0, row=7)

        self.pub_key = Text(self, height=7, width=75)
        self.pub_key.grid(column=1, row=7)

        self.RSAbtn = Button(self, text="Tạo Khóa", command=self.generate_key)
        self.RSAbtn.grid(column=1, row=8)

        self.RSAbtn = Button(self, text="Mã Hóa", command=self.mahoa_rsa)
        self.RSAbtn.grid(column=1, row=9)

        self.DERSAbtn = Button(self, text="Giải Mã", command=self.giaima_rsa)
        self.DERSAbtn.grid(column=1, row=10)

        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=11)

    def generate_key(self):
        key = RSA.generate(1024)
        
        save_file(
            key.exportKey('PEM'),
            'wb',
            'Lưu khóa cá nhân',
            (("PEM files", "*.pem"), ("All files", "*.*")),
            ".pem")

        save_file(
            key.publickey().exportKey('PEM'),
            'wb',
            'Lưu khóa công khai',
            (("PEM files", "*.pem"), ("All files", "*.*")),
            ".pem")

        self.pri_key.delete('1.0',END)
        self.pri_key.insert(END,key.exportKey('PEM'))
        self.pub_key.delete('1.0',END)
        self.pub_key.insert(END,key.publickey().exportKey('PEM'))

    def mahoa_rsa(self):
        txt = self.plaintxt.get().encode()
        pub_key = get_key("Public Key")
        cipher = PKCS1_v1_5.new(pub_key)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)

    def giaima_rsa(self):
        cipher = PKCS1_v1_5.new(get_key("Private Key"))
        detxt = cipher.decrypt(
            base64.b64decode(self.ciphertxt.get()),
            "Lỗi khi giải mã RSA").decode()
        self.denctxt.delete(0,END)
        self.denctxt.insert(INSERT,detxt)



class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)

        self.mahoa_Affine = Button(
            text="Mã hóa Affine",
            font=("Times New Roman", 11),
            command=self.affine
        )
        self.mahoa_Affine.pack()
        
        self.mahoa_DES = Button(
            text="Mã hóa DES",
            font=("Times New Roman", 11),
            command=self.des
        )
        self.mahoa_DES.pack()
        
        self.mahoa_RSA = Button(
            text="Mã hóa RSA",
            font=("Times New Roman", 11),
            command=self.rsa
        )
        self.mahoa_RSA.pack()

        self.thoat = Button(
            text="Kết Thúc",
            font=("Times New Roman", 11),
            command=quit
        )
        self.thoat.pack()

    def affine(self):
        MAHOA_Affine(self)

    def des(self):
        MAHOA_DES(self)
    
    def rsa(self):
        MAHOA_RSA(self)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()
