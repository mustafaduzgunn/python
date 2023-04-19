import random
import string

def generate_password():
    character1 = string.ascii_letters + string.digits
    character2 = '!' + '.' + '*' + '@'
    pass1 = ''.join(random.choice(character1) for i in range(8))
    pass2 = ''.join(random.choice(character2) for i in range(4))
    temp_pass = list(pass1+pass2)
    random.shuffle(temp_pass)
    password = ''.join(temp_pass)
    return password

password = generate_password()
print("Oluşturulan şifre:", password)