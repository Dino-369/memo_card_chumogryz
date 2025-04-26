#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QMessageBox,QRadioButton, QGroupBox, QButtonGroup
app = QApplication([])
from random import shuffle,randint

class Question():
    def __init__(self, question55, R_ANS, wrong1, wrong2, wrong3):
        self.question55 = question55
        self.R_ANS = R_ANS
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RGBox.hide()
    AnsGBox.show()
    BUTTOM_ok.setText("Следущий вопрос")

def show_Question():
    RGBox.show()
    AnsGBox.hide()
    BUTTOM_ok.setText("Oтветить")
    RadioGroup.setExclusive(False)
    but1.setChecked(False)
    but2.setChecked(False)
    but3.setChecked(False)
    but4.setChecked(False)
    RadioGroup.setExclusive(True)
'''
#def test():
    #if BUTTOM_ok.text() == "Oтветить":
     #   show_result()
    #else:
        #show_Question()'''

def aisSUGAR(q: Question):#было p  и норм !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    shuffle(AnswerS)
    AnswerS[0].setText(q.R_ANS)
    AnswerS[1].setText(q.wrong1)
    AnswerS[2].setText(q.wrong2)
    AnswerS[3].setText(q.wrong3)
    question.setText(q.question55)
    ib_corr.setText(q.R_ANS)
    show_Question()

def show_correct(res):
    ib_result.setText(res)
    show_result()

def check_ANSWER():
    main_win.resize(400, 200)
    if AnswerS[0].isChecked():
        show_correct("Good!")
        main_win.score += 1
        #print("Статистика:",)
        print("Рейтинг:", (main_win.score/main_win.total_otvetov * 100), "%")
    else:
        show_correct("Неправельно!\nскажи своей училке Инглиша \nчто-бы она тебя поругала\n стоп, нет,\n скажи маме чтобы поставила 2\n нет, всё хватит")
        print("Рейтинг:", (main_win.score/main_win.total_otvetov * 100), "%")
def next_question():
    main_win.total_otvetov += 1
    cur_question = randint(0,len(question_list)- 1)
    q = question_list[cur_question]
    # main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 
    question_list[main_win.cur_question]
    aisSUGAR(q)

def click_OK():
    if BUTTOM_ok.text() == "Oтветить":
        check_ANSWER()
    else:
        next_question()

question_list = []
question_list.append(Question("На каком языке говорят Чумогрызы?\n(Знают с самого детства)","Симлиш","язык Майя","Русский","язык Гроксов"))
question_list.append(Question("Как называется гимн империи Чумогрыз?","Гимн чумогрызовой сирени","Тритмайские байки","Союз ЧМ№","гимн Гроксов"))
question_list.append(Question("За что империю Чумогрыз ненавидила ПОЧТИ вся галактика?","Союз с Гроксами","Дары","Кража ресурсов","Нарушение галактического кодекса"))
question_list.append(Question("Эксперемент №*1*: была создана ипмерия:","Мудрозавр","Чумогрыз(племенная одежда)","Гравизмей","Королевский гравизмей"))
question_list.append(Question("Эксперемент №**: была создана (неизвестно как) ипмерия:","..Горкл.","...","...","..."))
question_list.append(Question("Родная планета империи Чумогрыз?","планета Рекадиум\nсистема Джелитен","планета Ангеннас\nсистема Ашлинаница","планета Фрилик\nсистема Заха","планета Этлиас\nсистема Джелитен"))
question_list.append(Question("С помощью какой планеты империя Чумогрыз стала богатой?","планета Канир\nсистема Маракей","планета Этлиас\nсистема Джелитен","планета Сиастов\nсистема Самбене","планета Филорайон\nсистема Аман 1"))
#привязка элементов к вертикальной линии
RGBox = QGroupBox("Вырианты ответов:")

main_win = QWidget()
main_win.setWindowTitle("Memo Card")
question = QLabel('Какой национальности не существует? \n Подсказка: "Чумогрыз" существует!')

main_win.cur_question = -1
main_win.setWindowTitle("Конкурс Memory Card")
main_win.resize(400, 200)
BUTTOM_ok = QPushButton("Oтветить")


but1 = QRadioButton("Энцы")
but2 = QRadioButton("Смурфы")
but3 = QRadioButton("Чулымцы")
but4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(but1)
RadioGroup.addButton(but2)
RadioGroup.addButton(but3)
RadioGroup.addButton(but4)

Layout_main = QVBoxLayout()
LayoutH1 = QHBoxLayout()
LayoutH2 = QVBoxLayout()
LayoutH3 = QVBoxLayout()
#LayoutH4 = QHBoxLayout()

LayoutH2.addWidget(but1)
LayoutH2.addWidget(but2)
LayoutH3.addWidget(but3)
LayoutH3.addWidget(but4)
LayoutH1.addLayout(LayoutH2)
LayoutH1.addLayout(LayoutH3)

RGBox.setLayout(LayoutH1)

AnsGBox = QGroupBox("Результат текста")
ib_result = QLabel("Прав ты или нет?")
ib_corr = QLabel("Ответ будет тут!")
Layout_res = QVBoxLayout()
Layout_res.addWidget(ib_result, alignment=(Qt.AlignLeft))
Layout_res.addWidget(ib_corr, alignment=Qt.AlignLeft, stretch=2)
AnsGBox.setLayout(Layout_res)


LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()

LayoutH1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
LayoutH2.addWidget(RGBox)

LayoutH2.addWidget(AnsGBox)##
AnsGBox.hide()

LayoutH3.addStretch(3)#1
LayoutH3.addWidget(BUTTOM_ok, stretch=9)
LayoutH3.addStretch(3)

Layout_card = QVBoxLayout()
Layout_card.addLayout(LayoutH1,stretch=2)# ???
Layout_card.addLayout(LayoutH2,stretch=8)# ??? что то тут чтоб пробелв не было надо исправить в цифрах чтоб все брастояния были одинаковы как в первом вопросе остальные старо выходят
Layout_card.addStretch(2)# ???
Layout_card.addLayout(LayoutH3, stretch=1)# ???
Layout_card.addStretch(1)# ???
Layout_card.addSpacing(5)

AnswerS = [but1, but2,but3,but4]

q = Question("Язык бразилии","Португальский","Бразильский","Испанский","Итальяно")

aisSUGAR(q)
BUTTOM_ok.clicked.connect(click_OK)
main_win.score = 0
main_win.total_otvetov = 0
next_question()


main_win.setLayout(Layout_card)
main_win.show()
app.exec_()