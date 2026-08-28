from translate import Translator
from collections import defaultdict

qwestions = {'как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}

class TextAnalysis():   
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            if self.text.lower() in qwestions.keys():
                self.response = qwestions[self.text.lower()]
            else:
                self.response = self.get_answer() 
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"
