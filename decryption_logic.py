def encrypt(text):
    new_text = ""
    for ch in text:
        new_char = chr(ord(ch)+3)
        new_text = new_text + new_char
    return new_text
text = input("Enter text :")
print("Encrypted message:",encrypt(text))