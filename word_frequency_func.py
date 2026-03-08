def count_frequency(text):
    print(text)
    words = text.split()
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else :
            dict[word] = 1
    print(dict)
text = input("Enter text: ")
count_frequency(text) 