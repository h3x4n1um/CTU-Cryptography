from Crypto.Cipher import DES
import base64


def pad(s):
    # Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def mahoa_DES(s, k):
    txt = pad(s).encode("utf8")
    key = pad(k).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    return entxt


def giaima_DES(s, k):
    txt = base64.b64decode(s)
    key = pad(k).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    return detxt


if __name__ == "__main__":
    opt = 2
    while opt not in {0, 1}:
        opt = int(input("Nhap lua chon ban muon dung (0: ma hoa, 1: giai ma): "))
    input_path = input("Nhap duong dan file: ")
    key = input("Nhap khoa: ")
    input_file = open(input_path, 'r')
    if opt == 0:
        output_path = input_path+"_mahoa"
        output_file = open(output_path, 'w')
        output_file.write(mahoa_DES(input_file.read(), key).decode("utf8"))
    else:
        output_path = input_path+"_giaima"
        output_file = open(output_path, 'w')
        output_file.write(giaima_DES(input_file.read(), key).decode("utf8"))
