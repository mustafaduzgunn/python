from Crypto.Cipher import AES
import base64

# Şifreleme fonksiyonu
def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return base64.b64encode(cipher.nonce + ciphertext + tag)

def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    nonce = ciphertext[:16]
    tag = ciphertext[-16:]
    ciphertext = ciphertext[16:-16]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    except ValueError:
        print("Incorrect key or corrupt ciphertext")
    return ""

# Anahtar (key)
islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n1-) Şifreleme\n2-) Şifre Çözme\n")
if (islem=="1"):
    while True:
        # Anahtar (key)
        key = input("Lütfen 16, 24 veya 32 byte'dan oluşan şifreleme anahtarını giriniz: ").encode('utf-8') #AES algoritması için anahtarın uzunluğu 16, 24 veya 32 byte olmalıdır. 
        if ((len(key) != 16) and (len(key) != 24) and (len(key) != 32)):
            print("Girmiş olduğunuz anahtar " + str(len(key)) +" byte'tan oluşuyor.")
        else:
            break  
    # Şifrelenecek metin
    plaintext = input("Lütfen şifrelenecek metni giriniz: ").encode('utf-8')

    # Metni şifrele
    ciphertext = encrypt(plaintext, key)

    # Şifrelenmiş metnin cleartext hali
    print("Şifrelenmiş metin: "+ciphertext.decode('utf-8'))

if (islem=="2"):
    ciphertext = input("Lütfen şifrelenmiş metni giriniz: ").encode('utf-8')
    key = input("Lütfen şifreleme anahtarını giriniz: ").encode('utf-8')

    # Şifreli metnin çözülebilmesi için gerekli olan fonksiyon
    plaintext = decrypt(ciphertext, key)

    # Çözülen metnin cleartext hali
    print("Çözülen metnin cleartext hali: " + plaintext.decode('utf-8'))

else:
    print ("Hatalı işlem!")
    