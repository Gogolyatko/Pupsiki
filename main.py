from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
okno = QWidget()
okno.setWindowTitle("Сосисочки")
okno.move(350, 100)
okno.resize(650, 500)

knopka = QPushButton(okno)
knopka.setText("Гинирейшон")
knopka.move(350, 100)

text = QLabel(okno)
text2 = QLabel(okno)
text.setText("Клик шоб генерейшон")
text.move(70, 100)
text2.move(80, 130)

chelik = QLabel(okno)
chelik.setText("?")
chelik.move(190, 70)

def chelik_show():
    cifra = randint(1, 100)
    chelik.setText(str(cifra))
    text.setText("Циферка: ")

knopka.clicked.connect(chelik_show)




okno.show()
app.exec_()