import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def password_generator():
    filename = "passwords.txt"
    while True:
        length = int(input("Şifre uzunluğunu girin: "))
        password = generate_password(length)
        print("Oluşturulan Şifre:", password)
        save_password(password, filename)
        choice = input("Yeni bir şifre oluşturmak için 'y' devam etmek için 'n' tuşuna basın: ")
        if choice.lower() != 'y':
            break

    print("Şifreler", filename, "dosyasına kaydedildi.")

password_generator()
