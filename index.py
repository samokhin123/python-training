text="Программирование - это процесс создания программ. Программирование помогает автоматизировать работу. Программирование интересно и полезно!"
text=text.split(" ")
text.remove("-")
text2=set(text)
print(len(text2))
c=0
b=0
for i in text2:
    a= len(i)
    if a > c:
        c=a
        b=i
print("Самое длинное слово:", b, "длина слова:", c)
def len_word (d):
    g=len(d)
    return g
len_word=len_word(str(input()))
print("длина слова:", len_word)