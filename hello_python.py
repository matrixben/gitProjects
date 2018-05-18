import re

text = 'python3'
text2 = 'professional git'
message = 'Welcome to the {} world.'.format(text)
print(message)

re_word = re.compile('\w+')


def print_words(msg):
    for match in re_word.finditer(msg):
        yield match.group()

for p in print_words(message):
    print(p)
