import re

def prepare_text(text):
    text = text.lower()  # Приведение к нижнему регистру
    text = re.sub(r'[^а-яё]', '', text)  # Очистка от небуквенных символов и пробелов
    text = text.replace('ё', 'е')  # Замена Ё на Е
    return text

def encrypt(text, key):
    encrypted_text = ''
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('а')
        encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ''
    for i, char in enumerate(encrypted_text):
        shift = ord(key[i % len(key)]) - ord('а')
        decrypted_char = chr((ord(char) - ord('а') - shift) % 32 + ord('а'))
        decrypted_text += decrypted_char
    return decrypted_text

def find_key_length(ciphertext):
    # Реализация метода Казиского для поиска длины ключа
    # (может быть заменена методом Фридмана)
    pass

def hack_vigenere(ciphertext, key_length):
    # Реализация взлома методом наименьших квадратов
    pass

def group_text(text, n):
    return ' '.join([text[i:i+n] for i in range(0, len(text), n)])

def main():
    print("Программа для шифрования и дешифрования методом Виженера")
    while True:
        choice = input("Выберите режим:\n1. Зашифровать текст\n2. Расшифровать текст\n3. Выйти\nВаш выбор: ")
        if choice == '1':
            plaintext = input("Введите текст для шифрования: ")
            key = input("Введите ключ: ")
            plaintext = prepare_text(plaintext)
            encrypted_text = encrypt(plaintext, key)
            print("Зашифрованный текст:")
            print(group_text(encrypted_text, 5))
        elif choice == '2':
            ciphertext = input("Введите зашифрованный текст: ")
            key = input("Введите ключ: ")
            ciphertext = prepare_text(ciphertext)
            decrypted_text = decrypt(ciphertext, key)
            print("Расшифрованный текст:")
            print(group_text(decrypted_text, 5))
        elif choice == '3':
            print("Выход из программы")
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
