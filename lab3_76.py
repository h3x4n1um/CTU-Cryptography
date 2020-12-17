# Họ và tên sinh viên: Nguyễn Thanh Hoàng Hải
# Mã số sinh viên: B1812339
# STT: 76

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from tkinter import *
from tkinter import filedialog
import base64

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

def generate_key():
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

    pri_key.delete('1.0',END)
    pri_key.insert(END,key.exportKey('PEM'))
    pub_key.delete('1.0',END)
    pub_key.insert(END,key.publickey().exportKey('PEM'))

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

    if key_style == "Public Key":
        pub_key.delete('1.0',END)
        pub_key.insert(END,key)
    elif key_style == "Private Key":
        pri_key.delete('1.0',END)
        pri_key.insert(END,key)

    return RSA.importKey(key)

def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima_rsa():
    cipher = PKCS1_v1_5.new(get_key("Private Key"))
    detxt = cipher.decrypt(
        base64.b64decode(ciphertxt.get()),
        "Lỗi khi giải mã RSA").decode()
    denctxt.delete(0,END)
    denctxt.insert(INSERT,detxt)

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ BẤT ĐỐI XỨNG RSA",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb.grid(column=0, row=3)

plaintxt = Entry(window,width=75)
plaintxt.grid(column=1, row=3)

cipherlb = Label(window, text="Văn bản được mã hoá",font=("Arial", 14))
cipherlb.grid(column=0, row=4)

ciphertxt = Entry(window,width=75)
ciphertxt.grid(column=1, row=4)

denclb = Label(window, text="Văn bản được giải mã",font=("Arial", 14))
denclb.grid(column=0, row=5)

denctxt = Entry(window,width=75)
denctxt.grid(column=1, row=5)

pri_keylb = Label(window, text="Khóa cá nhân",font=("Arial", 14))
pri_keylb.grid(column=0, row=6)

pri_key = Text(window, height=7, width=75)
pri_key.grid(column=1, row=6)

pub_keylb = Label(window, text="Khóa công khai",font=("Arial", 14))
pub_keylb.grid(column=0, row=7)

pub_key = Text(window, height=7, width=75)
pub_key.grid(column=1, row=7)

RSAbtn = Button(window, text="Tạo Khóa", command=generate_key)
RSAbtn.grid(column=1, row=8)

RSAbtn = Button(window, text="Mã Hóa", command=mahoa_rsa)
RSAbtn.grid(column=1, row=9)

DERSAbtn = Button(window, text="Giải Mã", command=giaima_rsa)
DERSAbtn.grid(column=1, row=10)

window.geometry('800x600')
window.mainloop()