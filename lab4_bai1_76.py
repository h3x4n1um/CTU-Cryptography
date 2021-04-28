# Họ và tên sinh viên: Nguyễn Thanh Hoàng Hải
# Mã số sinh viên: B1812339
# STT: 76

from tkinter import *
from Crypto.Hash import MD5, SHA1, SHA256, SHA512


def hashing():
    content = plaintxt.get().encode()
    result = {
        0: MD5.new(content),
        1: SHA1.new(content),
        2: SHA256.new(content),
        3: SHA512.new(content),
    }

    rs = result[hashmode.get()].hexdigest().upper()
    hashvalue.delete(0, END)
    hashvalue.insert(INSERT, rs)


window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="Chuơng trình Băm", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

plainlb = Label(window, text="Văn bản", font=("Arial", 14))
plainlb.grid(column=0, row=2)

plaintxt = Entry(window, width=75)
plaintxt.grid(column=1, row=2)

radioGroup = LabelFrame(window, text="Hàm băm")
radioGroup.grid(column=1, row=3)
hashmode = IntVar()
hashmode.set(-1)

md5_func = Radiobutton(
    radioGroup,
    text="Hash MD5",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=0,
    command=hashing)
md5_func.grid(column=0, row=4)

sha1_func = Radiobutton(
    radioGroup,
    text="Hash SHA1",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=1,
    command=hashing)
sha1_func.grid(column=0, row=5)

sha256_func = Radiobutton(
    radioGroup,
    text="Hash SHA256",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=2,
    command=hashing)
sha256_func.grid(column=0, row=6)

sha512_func = Radiobutton(radioGroup,
                          text="Hash SHA512",
                          font=("Times New Roman", 11),
                          variable=hashmode,
                          value=3,
                          command=hashing)
sha512_func.grid(column=0, row=7)

hashvaluelb = Label(window, text="Giá trị băm", font=("Arial", 14))
hashvaluelb.grid(column=0, row=8)

hashvalue = Entry(window, width=75)
hashvalue.grid(column=1, row=8)

window.geometry('800x600')
window.mainloop()
