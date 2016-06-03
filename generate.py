def generate(self, py):
    self.py = py
    self.py.title.setText("Сайт ОАО «Аэрофлот. План публикации обновления %s. \n "\
                    "Номер заявки-релиза в системе HelpDesk: #%s" % (self.py.nameProject.text(), self.py.numBid.text()))
    self.py.target.setText("Выполнить обновление функциональности %s выполненные в рамках заявок:" \
                    "https://support.ramax.ru/issues/%s" % (self.py.nameProject.text(), self.py.specBid.text()))
    self.py.stage_1_text.setText("Дата и время публикации: с %s до %s %s \n" \
                    "Список контактов ответственных сотрудников:" % (self.py.timeIn.text(),self.py.timeOut.text(),
                                                                      self.py.dateIn.text()))
    self.py.stage_3_text.setText("Особый режим мониторинга не требуется.")
