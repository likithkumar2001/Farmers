def trans(language,text):
    from googletrans import Translator, constants
    translator = Translator()
    Text_message = translator.translate(text, dest=language)
    return Text_message.text
