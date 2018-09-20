def reverse(text):
    res = ""
    for i in text:
        res = i + res
    return res


def reverse_2(text):
    return text[::-1]


my_text = "мой текст"

print(reverse(my_text))
print(reverse_2(my_text))
