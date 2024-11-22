import random
import sys
from PyQt6.QtWidgets import QWidget, QApplication
from layout import Ui_Dialog


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        specializacja = ""
        cena = 0
        liczba_dni = 0

        if self.ui.internistaRadio.isChecked():
            specializacja = "Internisty"
        elif self.ui.pediatraRadio.isChecked():
            specializacja = "Pediatry"
        elif self.ui.dermatologRadio.isChecked():
            specializacja = "Dermatologa"
        else:
            specializacja = "nie wybrano"

        if self.ui.privateCheck.isChecked():
            liczba_dni = random.randint(0,14)
            cena = 200
        else:
            liczba_dni = random.randint(0,1000)
            cena = 0

        self.ui.resultLabel.setText(f'Pomyślnie zarezerwowano wizytę u lekarza: {specializacja}. '
                                    f'Termin wizyty przypada za: {liczba_dni} dni. '
                                    f'Koszt wizyty: {cena}.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())

