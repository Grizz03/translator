from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translations = translator.translate(text)
        print(translations)
except FileNotFoundError as e:
    print('Check your file location')
