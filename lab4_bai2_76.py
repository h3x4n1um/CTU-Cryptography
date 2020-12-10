# Họ và tên sinh viên: Nguyễn Thanh Hoàng Hải
# Mã số sinh viên: B1812339
# STT: 76

from tkinter import *
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
import csv
import random

def register():
    # check existing id
    with open("CSDL.csv", 'r+', newline='') as csdl:
        csdl_reader = csv.reader(csdl, delimiter='\t', quotechar='|')
        usr = usrtxt.get()
        for row in csdl_reader:
            if usr == row[0]:
                print("Đã có user", usr, "trong CSDL")
                return
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
        hash_mode = random.randint(0, 3)
        csdl_writer = csv.writer(csdl, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csdl_writer.writerow([usr, result[hash_mode].hexdigest().upper()])
        print("Tạo user", usr, "thành công với mật khẩu được hash bởi", hash_info[hash_mode])
    return

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="Tạo tài khoản",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

usrlb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usrlb.grid(column=0, row=2)

usrtxt = Entry(window)
usrtxt.grid(column=1, row=2)

pwdlb = Label(window, text="Mật khẩu",font=("Arial", 14))
pwdlb.grid(column=0, row=3)

pwdtxt = Entry(window, show='*')
pwdtxt.grid(column=1, row=3)

registerbtn = Button(window, text="Tạo tài khoản", command=register)
registerbtn.grid(column=1, row=4)

window.geometry('800x600')
window.mainloop()
