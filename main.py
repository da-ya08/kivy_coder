from random import randint
import clipboard
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix import boxlayout
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '720')

abc = "вБsШуЕCoЗBvА…МeJщXСKQWкqЧВЭЪ0ЬtЦЯmбAгд2:ж7иO.Yz+опр*jД8х ч9uёiьэХяdсЁ-Ръ," \
      "1шТ!лMgRNУыЖйU3ФтxИabcКНTПюyIZl=ЩkDLrмhц6wОЫGЮ_аF;Лn?EHfV45нзЙфpеГPS❤"
abc_cezar = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
             'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
             'э', 'ю', 'я']


class MainWidget(boxlayout.BoxLayout):
    text_input = ObjectProperty()
    do_coded_text = ObjectProperty()
    coder_da_ya = ObjectProperty()
    coder_cezar = ObjectProperty()
    show_mode = ObjectProperty()
    mode = 1

    def changed_text(self):
        if self.text_input.text == "":
            self.do_coded_text.text = ""
        elif self.text_input.text[0:5] == "DA YA" and self.mode == 1:
            self.do_coded_text.text = self.decode_da_ya(self.text_input.text)
        elif self.mode == 1:
            self.do_coded_text.text = self.encode_da_ya(self.text_input.text)
        elif (self.text_input.text[0] == "C" or self.text_input.text[0] == "c") and self.mode == 2:
            self.do_coded_text.text = self.decode_cezar(self.text_input.text)
        elif self.mode == 2:
            self.do_coded_text.text = self.encode_cezar(self.text_input.text)
        print(self.mode)

    def decode_da_ya(self, text):
        out_text = ""
        tx = text.replace("@", "")
        tx = tx.replace("DA YA", "")
        temp = ""
        for i in range(0, len(tx)):
            if i == 0 or i % 3 == 0 or i == len(tx) - 1:
                continue
            temp += tx[i]
        tx = temp
        key = tx[0:2]
        tx = tx.replace(key, "")
        while len(str(key)) < len(tx):
            key = str(int(key) ** 2)
        for i in range(len(tx)):
            for a in range(len(abc)):
                if tx[i] == abc[a]:
                    try:
                        out_text += abc[a + int(key[i])]
                    except IndexError:
                        out_text += abc[a - (142 - int(key[i]))]
        self.otext = out_text
        return out_text

    def encode_da_ya(self, text):
        out_text = "DA YA "
        key = 0
        while int(key) % 10 == 0:
            key = str(randint(11, 99))
        out_text += key + " "
        while len(str(key)) < len(text):
            key = str(int(key) ** 2)
        for i in range(len(text)):
            for a in range(len(abc)):
                if text[i] == abc[a]:
                    out_text += abc[a - int(key[i])]
            if i % 2 != 0:
                out_text += " "
        if len(text) % 2 != 0:
            out_text += '@ '
        out_text += "DA YA"
        self.otext = out_text
        return out_text

    def decode_cezar(self, text):
        if len(text) < 3:
            return text
        key = text[1]
        text = text[2:]
        outtxt = ""
        for i in range(len(text)):
            if text[i] in abc_cezar:
                for j in range(len(abc_cezar)):
                    if text[i] == abc_cezar[j]:
                        try:
                            outtxt += abc_cezar[j + int(key)]
                        except:
                            try:
                                outtxt += abc_cezar[j - (66 - int(key))]
                            except:
                                return "Error"
            else:
                outtxt += text[i]
        return outtxt

    def encode_cezar(self, text):
        if len(text) < 2:
            return text
        key = text[0]
        text = text[1:]
        outtxt = ""
        for i in range(len(text)):
            if text[i] in abc_cezar:
                for j in range(len(abc_cezar)):
                    if text[i] == abc_cezar[j]:
                        try:
                            outtxt += abc_cezar[j - int(key)]
                        except:
                            self.do_coded_text.text = "Error"
            else:
                outtxt += text[i]
        return outtxt

    def cleaning(self):
        self.text_input.text = ""

    def copy_text(self):
        try:
            clipboard.copy(self.do_coded_text.text)
        except:
            return

    def change_mode(self, mode):
        if mode == 1:
            self.show_mode.text = "DA YA mode"
            self.do_coded_text.text = "Вставьте текст"
            self.mode = 1
        elif mode == 2:
            self.show_mode.text = "Cezar mode"
            self.do_coded_text.text = "Введите сообщение в формате:\nАгнлийская С(если нужно расшифровать) + число + " \
                                      "текст "
            self.mode = 2


class CoderApp(App):

    def build(self):
        self.title = "Coder 6.2"
        return MainWidget()


if __name__ == '__main__':
    app = CoderApp()
    app.run()
