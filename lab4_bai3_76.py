# Họ và tên sinh viên: Nguyễn Thanh Hoàng Hải
# Mã số sinh viên: B1812339
# STT: 76

from tkinter import *
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
import csv
import random

def login():
    # check existing id
    with open("CSDL.csv", 'r', newline='') as csdl:
        csdl_reader = csv.reader(csdl, delimiter='\t', quotechar='|')
        usr = usrtxt.get()
        for row in csdl_reader:
            if usr == row[0]:
                pwd = pwdtxt.get().encode()
                result = {
                    0: MD5.new(pwd),
                    1: SHA1.new(pwd),
                    2: SHA256.new(pwd),
                    3: SHA512.new(pwd),
                }
                hash_info = {
                    0: "MD5",
                    1: "SHA1",
                    2: "SHA256",
                    3: "SHA512",
                }
                for hash_mode in range(4):
                    if row[1] == result[hash_mode].hexdigest().upper():
                        print("User", usr, "đăng nhập thành công với cách hash", hash_info[hash_mode])
                        return
                print("Sai mật khẩu!")
                return

    print("Không tìm thấy user", usr, "trong CSDL!")
    return

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="Đăng nhập",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

usrlb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usrlb.grid(column=0, row=2)

usrtxt = Entry(window)
usrtxt.grid(column=1, row=2)

pwdlb = Label(window, text="Mật khẩu",font=("Arial", 14))
pwdlb.grid(column=0, row=3)

pwdtxt = Entry(window, show='*')
pwdtxt.grid(column=1, row=3)

loginbtn = Button(window, text="Đăng nhập", command=login)
loginbtn.grid(column=1, row=4)

window.geometry('800x600')
window.mainloop()
