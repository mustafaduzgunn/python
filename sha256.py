import hashlib

def sha256_sifrele():
    # Kullanıcıdan bir metin girdisi al
    text = input("Enter text to hash: ")

    # Metni SHA-256 ile şifrele
    hash_object = hashlib.sha256(text.encode('utf-8'))
    hex_dig = hash_object.hexdigest()

    # Şifrelenmiş veriyi yazdır
    print("SHA-256 hash: ", hex_dig)

def sha256_sifre_dogrula():
    hashed_password = "004687553429516cefacdedeaf3a24ce9324d0eb0739c192e21d3ecb883aef5b"
    password = input("Lütfen şifreyi giriniz: ")
    if hashlib.sha256(password.encode('utf-8')).hexdigest() == hashed_password:
        print("Doğru Şifre")
    else:
        print("Hatalı Şifre")

islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n1-) SHA-256 ile şifreleme\n2-) SHA-256 ile şifrelenmiş metnin şifresini doğrulama\n")
if (islem=="1"):
    sha256_sifrele()
if (islem=="2"):
    sha256_sifre_dogrula()
else:
    print ("Hatalı işlem!")