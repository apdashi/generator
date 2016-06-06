import docx
bashIPPost = "iptables -t nat -A POSTROUTING -d %s -p tcp -m tcp --dport %s -j SNAT --to-source %s; "
bashIPPre = "iptables -t nat -A PREROUTING -d %s -p tcp -m tcp --dport %s -j DNAT --to-destination %s; "
text1 = "Сайт ОАО «Аэрофлот. План публикации обновления %s. \n Номер заявки-релиза в системе HelpDesk: #%s"
text2 = "Выполнить обновление функциональности %s выполненные в рамках заявок: \n https://support.ramax.ru/issues/%s"
text3 = "Дата и время публикации: с %s до %s %s \n Список контактов ответственных сотрудников:"
text4 = "Особый режим мониторинга не требуется."
text5 = "Системный администратор выполняет резервное копирование приложения и конфигурационных файлов " \
               "на серверах %s "
text6 = "Системный администратор временно перенаправляет трафик %s с сервера %s на %s "
text7 = "Системный администратор производит обновление кода приложения на сервере %s путем переключения" \
        " локальной версии на ветку релиза, выполнив команду Subversion. Номер ревизии: %s "
text8 = "Системный администратор перезапускает приложение на сервере %s и отключает " \
                    "перенаправление трафика "
text9 = "/etc/init.d/prod_schedule restart; \n" \
                "while ! /usr/lib/nagios/plugins/check_tcp -H localhost -p 9780 ; do sleep 0.5 ; done; "
text10 = "Системый администртор осуществляет сброс кеша Varnish на серверах afl-kvm11 и afl-kvm12"
text11 = "/usr/local/varnish/bin/varnishadm -T localhost:16080 purge.url schedule/static "
text12 = "Системный администратор выполняет сравнение предыдущей и новой версии приложения," \
                    " формирует отчет, содержащий следующие сведения: "
text13_0 = "список измененных файлов"
text13_1 = "diff –u (за исключением каталогов logs, pid)"
text13_2 = "исключить из отчета пароли"
text13_3 = "отчет направить на следующие адреса: "
text14 = "Тестер у себя прописывает в файл hosts (%%windir%%\\System32\\drivers\\etc\\hosts) IP-адрес " \
        "площадки сайта"
text17 = "185.69.80.8        www.aeroflot.ru"
text18 = "и осуществляет тестирование по списку тест-кейсов из файла, выложенного в релизную заявку. "
text15 = "В случае обнаружения ошибок на этапе тестирования принимается решение об откате" \
                    " изменений на сервере %s. "
text16 = "Производится оповещение ответственных сотрудников (список сформирован на этапе 1) о " \
                "произведенной публикации."
text0 = "svn switch %s \n svn update"
text19 = "Производится рассылка плана публикации участникам проекта со стороны Исполнителя (ЗАО «РАМАКС ИНТЕРНЕЙШНЛ»). \n" \
         "Команда публикации:"
text20 = "Производится уведомление команды публикации о дате и времени проведения публикации."


def saveDoc(self, py):
    self.py = py
    document = docx.Document()
    styles = document.styles
    styles["ListNumber"].font.name = "Calibri"
    styles["Normal"].font.name = "Calibri"

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
    document.add_paragraph(text5 % ", ".join(i for i in listSer), style='ListNumber')
    for i in range(0, len(listApp)):
        if (len(listApp) - 1) == i:
            serverPer = 0
        else:
            serverPer = i + 1
        document.add_paragraph(text6 % (self.py.nameProject.text(), listApp[i], listApp[serverPer]), style='ListNumber')
        document.add_paragraph(bashIPPost % (listSer.get(listApp[i]), self.py.portApp.text(),
                                                  listSer.get(listApp[serverPer])))
        document.add_paragraph(bashIPPre % (listSer.get(listApp[serverPer]), self.py.portApp.text(),
                                                  listSer.get(listApp[i])))
        document.add_paragraph(text7 % (listApp[i], self.py.numberRev.text()), style='ListNumber')
        document.add_paragraph(text0 % (self.py.svn.text()))
        document.add_paragraph(text8 % (listApp[i]), style='ListNumber')
        document.add_paragraph(text9)
        document.add_paragraph(bashIPPre % (listSer.get(listApp[i]), self.py.portApp.text(),
                                                  listSer.get(listApp[serverPer])))
        document.add_paragraph(bashIPPost % (listSer.get(listApp[serverPer]), self.py.portApp.text(),
                                                   listSer.get(listApp[i])))
        if self.py.cache.isChecked() == True:
            document.add_paragraph(text10, style='ListNumber')
            document.add_paragraph(text11)
        document.add_paragraph(text12, style='ListNumber')
        document.add_paragraph(text13_0, style='ListBullet')
        document.add_paragraph(text13_1, style='ListBullet')
        document.add_paragraph(text13_2, style='ListBullet')
        document.add_paragraph(text13_3, style='ListBullet')
        for j in (self.py.tableView.model().cached):
            if j[2] == True:
                document.add_paragraph(j[6], style='ListContinue')
        document.add_paragraph(text14, style='ListNumber')
        document.add_paragraph(text17)
        document.add_paragraph(text18)
        s = ", ".join(c for c in listApp[0:i])
        document.add_paragraph(text15 % s, style='ListNumber')

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
        tbl.cell(0, i).text = h
    for i, r in enumerate(iata):
        for j, val in enumerate(r):
            tbl.cell(i+1, j).text = val