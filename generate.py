from docx import Document

bashIPPost = "iptables -t nat -A POSTROUTING -d %s -p tcp -m tcp --dport %s -j SNAT --to-source %s; \n"
bashIPPre = "iptables -t nat -A PREROUTING -d %s -p tcp -m tcp --dport %s -j DNAT --to-destination %s; \n"
text1 = "Сайт ОАО «Аэрофлот. План публикации обновления %s. \n Номер заявки-релиза в системе HelpDesk: #%s"
text2 = "Выполнить обновление функциональности %s выполненные в рамках заявок: \n https://support.ramax.ru/issues/%s"
text3 = "Дата и время публикации: с %s до %s %s \n Список контактов ответственных сотрудников:"
text4 = "Особый режим мониторинга не требуется."
text5 = "1. Системный администратор выполняет резервное копирование приложения и конфигурационных файлов " \
               "на серверах %s "
text6 = "%s. Системный администратор временно перенаправляет трафик %s с сервера %s на %s "
text7 = "%s. Системный администратор производит обновление кода приложения на сервере %s путем переключения" \
        " локальной версии на ветку релиза, выполнив команду Subversion. Номер ревизии: %s "
text8 = "%s. Системный администратор перезапускает приложение на сервере %s и отключает " \
                    "перенаправление трафика \n"
text9 = "/etc/init.d/prod_schedule restart; \n" \
                "while ! /usr/lib/nagios/plugins/check_tcp -H localhost -p 9780 ; do sleep 0.5 ; done; "
text10 = "%s. Системый администртор осуществляет сброс кеша Varnish на серверах afl-kvm11 и afl-kvm12"
text11 = "/usr/local/varnish/bin/varnishadm -T localhost:16080 purge.url schedule/static "
text12 = "%s. Системный администратор выполняет сравнение предыдущей и новой версии приложения," \
                    " формирует отчет, содержащий следующие сведения: "
text13 = "список измененных файлов \n diff –u (за исключением каталогов logs, pid) \n" \
                    "исключить из отчета пароли \n отчет направить на следующие адреса: "
text14 = "%s. Тестер у себя прописывает в файл hosts (%%windir%%\\System32\\drivers\\etc\\hosts) IP-адрес " \
        "площадки сайта"
text17 = "185.69.80.8        www.aeroflot.ru"
text18 = "и осуществляет тестирование по списку тест-кейсов из файла, выложенного в релизную заявку. "
text15 = "%s. В случае обнаружения ошибок на этапе тестирования принимается решение об откате" \
                    " изменений на сервере %s. "
text16 = "%s. Производится оповещение ответственных сотрудников (список сформирован на этапе 1) о " \
                "произведенной публикации."
text0 = "svn switch %s \n svn update"
text19 = "Производится рассылка плана публикации участникам проекта со стороны Исполнителя (ЗАО «РАМАКС ИНТЕРНЕЙШНЛ»). \n" \
         "Команда публикации:"
text20 = "Производится уведомление команды публикации о дате и времени проведения публикации."

def generate(self, py):
    self.py = py
    self.py.title.setText(text1 % (self.py.nameProject.text(), self.py.numBid.text()))
    self.py.target.setText(text2 % (self.py.nameProject.text(), self.py.specBid.text()))
    self.py.stage_1_text.setText(text3 % (self.py.timeIn.text(), self.py.timeOut.text(), self.py.dateIn.text()))
    self.py.stage_3_text.setText(text4)
    formText = ""
    listSer = {self.py.app1.text():self.py.ipAddress1.text()}
    listApp = [self.py.app1.text()]
    if self.py.app2.text() != "":
        listSer[self.py.app2.text()] = self.py.ipAddress2.text()
        listApp.append(self.py.app2.text())
    if self.py.app3.text() != "":
        listSer[self.py.app3.text()] = self.py.ipAddress3.text()
        listApp.append(self.py.app3.text())
    if self.py.app4.text() != "":
        listSer[self.py.app4.text()] = self.py.ipAddress4.text()
        listApp.append(self.py.app4.text())
    formText = text5 % ", ".join(i for i in listSer)
    iter = 1
    for i in range(0,len(listApp)):
        if (len(listApp) - 1) == i:
            serverPer = 0
        else:
            serverPer = i + 1
        iter += 1
        formText += text6 % (iter, self.py.nameProject.text(), listApp[i], listApp[serverPer])
        formText += bashIPPost % (listSer.get(listApp[i]), self.py.portApp.text(), listSer.get(listApp[serverPer]))
        formText += bashIPPre % (listSer.get(listApp[serverPer]), self.py.portApp.text(), listSer.get(listApp[i]))
        iter += 1
        formText +=text7 % (iter, listApp[i], self.py.numberRev.text())
        formText += text0 % (self.py.svn.text())
        iter += 1
        formText += text8 % (iter, listApp[i])
        formText += text9
        formText += bashIPPre % (listSer.get(listApp[i]), self.py.portApp.text(), listSer.get(listApp[serverPer]))
        formText += bashIPPost % (listSer.get(listApp[serverPer]), self.py.portApp.text(), listSer.get(listApp[i]))
        iter += 1
        if self.py.cache.isChecked() == True:
            formText += text10 % (iter)
            formText += text11
            iter += 1
        formText += text12 % (iter)
        formText += text13
        iter += 1
        formText += text14 % (iter)
        iter += 1
        formText += text15 % (iter, ", ".join(c for c in listApp[0:i]))
    formText += text16 % (iter+1)
    self.py.stage_2_text.setText(formText)

def saveDoc(self, py):
    self.py = py
    document = Document()

    h = document.add_header()
    h.add_paragraph(text1 % (self.py.nameProject.text(), self.py.numBid.text()))

    document.add_paragraph(u"Цель").bold = True

    document.add_paragraph(text2 % (self.py.nameProject.text(), self.py.specBid.text()))
    document.add_heading("Этап 1. Подготовка к публикации", level=2)

    document.add_paragraph(text3 % (self.py.timeIn.text(), self.py.timeOut.text(), self.py.dateIn.text()))

    make_table(document, self.py.tableView.model().cached, 0)
    document.add_paragraph(text19)
    make_table(document, self.py.tableView.model().cached, 1)
    document.add_paragraph(text20)
    #
    # document.add_paragraph(u"Производится уведомление команды публикации о дате и времени проведения публикации.")
    #
    document.add_heading("Этап 2. Публикация изменений", level=2)
    listSer = {self.py.app1.text(): self.py.ipAddress1.text()}
    listApp = [self.py.app1.text()]
    if self.py.app2.text() != "":
        listSer[self.py.app2.text()] = self.py.ipAddress2.text()
        listApp.append(self.py.app2.text())
    if self.py.app3.text() != "":
        listSer[self.py.app3.text()] = self.py.ipAddress3.text()
        listApp.append(self.py.app3.text())
    if self.py.app4.text() != "":
        listSer[self.py.app4.text()] = self.py.ipAddress4.text()
        listApp.append(self.py.app4.text())
    document.add_paragraph(text5 % ", ".join(i for i in listSer))
    iter = 1
    for i in range(0, len(listApp)):
        if (len(listApp) - 1) == i:
            serverPer = 0
        else:
            serverPer = i + 1
        iter += 1
        document.add_paragraph(text6 % (iter, self.py.nameProject.text(), listApp[i], listApp[serverPer]))
        tbl = document.add_table(1, 1)
        tbl.cell(0,0).add_paragraph(bashIPPost % (listSer.get(listApp[i]), self.py.portApp.text(),
                                                  listSer.get(listApp[serverPer])))
        tbl.cell(0, 0).add_paragraph(bashIPPre % (listSer.get(listApp[serverPer]), self.py.portApp.text(),
                                                  listSer.get(listApp[i])))
        iter += 1
        document.add_paragraph(text7 % (iter, listApp[i], self.py.numberRev.text()))
        tbl = document.add_table(1, 1)
        tbl.cell(0, 0).add_paragraph(text0 % (self.py.svn.text()))
        iter += 1
        document.add_paragraph(text8 % (iter, listApp[i]))
        tbl = document.add_table(1, 1)
        tbl.cell(0, 0).add_paragraph(text9)
        tbl.cell(0, 0).add_paragraph(bashIPPre % (listSer.get(listApp[i]), self.py.portApp.text(),
                                                  listSer.get(listApp[serverPer])))
        tbl.cell(0, 0).add_paragraph(bashIPPost % (listSer.get(listApp[serverPer]), self.py.portApp.text(),
                                                   listSer.get(listApp[i])))
        iter += 1
        if self.py.cache.isChecked() == True:
            document.add_paragraph(text10 % (iter))
            tbl = document.add_table(1, 1)
            tbl.cell(0, 0).add_paragraph(text11)
            iter += 1
        document.add_paragraph(text12 % (iter))
        document.add_paragraph(text13)
        document.add_paragraph(" /n".join( i[6] for i in (self.py.tableView.model().cached) if i[2] == True))
        iter += 1
        document.add_paragraph(text14 % (iter))
        tbl = document.add_table(1, 1)
        tbl.cell(0, 0).add_paragraph(text17)
        document.add_paragraph(text18)
        iter += 1
        document.add_paragraph(text15 % (iter, ", ".join(c for c in listApp[0:i])))

    document.add_heading("Этап 3. Мониторинг работы", level=2)
    document.add_paragraph(text4)

    document.save("123.docx")


def make_table(document, data, num):
    iata = []
    for i in data:
        if i[num] == True:
            iata.append([i[5], i[4], i[6]])

    tbl = document.add_table(len(iata) + 1, 3)
    for i, h in enumerate((u"Компания", u"Представитель", u"Email")):
        tbl.cell(0, i).add_paragraph(h)
    for i, r in enumerate(iata):
        for j, val in enumerate(r):
            tbl.cell(i+1, j).add_paragraph(val)