import math


def Char2Num(c):
    return ord(c)-65


def Num2Char(n):
    return chr(n+65)


def decrypt(encrypted, a, b, m):
    # find a^-1
    rev_a = 0
    for i in range(m):
        if (a*i % m == 1):
            rev_a = i
            break

    # decrypting
    decrypted = ""
    for y in encrypted:
        tmp = rev_a*(Char2Num(y)-b) % m
        decrypted = decrypted + Num2Char(tmp)
    return decrypted


if __name__ == "__main__":
    encrypted = "HKLZOVYQPTOBJDVOBLBUBOHKWBGVUVYVZUTZGHOVYQPBYVREOZRBTTBT"
    m = 26

    # should print AFFINECIPHER
    print(decrypt("IHHWVCSWFRCP", 5, 8, m))

    # should print HAOMIGOI
    print(decrypt("CFZLJVZJ", 7, 5, m))

    # brute force decode
    for a in range(m):
        if (math.gcd(a, m) == 1):
            for b in range(m):
                print("a: ", a, "b: ", b)
                print(decrypt(encrypted, a, b, m))
                print()

    # after looking in all possible strings in decrypted list
    # a = 5, b = 7
    # decrypted text:
    # ALGORITHMSREQUIREGENERALDEFINITIONSOFARITHMETICPROCESSES
    # ALGORITHMS REQUIRE GENERAL DEFINITIONS OF ARITHMETIC PROCESSES
    print(decrypt(encrypted, 5, 7, m))
