def generate(self, py):
    bashIPPost = "iptables -t nat -A POSTROUTING -d %s -p tcp -m tcp --dport %s -j SNAT --to-source %s; \n"
    bashIPPre = "iptables -t nat -A PREROUTING -d %s -p tcp -m tcp --dport %s -j DNAT --to-destination %s; \n"
    self.py = py
    self.py.title.setText("Сайт ОАО «Аэрофлот. План публикации обновления %s. \n "\
                    "Номер заявки-релиза в системе HelpDesk: #%s" % (self.py.nameProject.text(), self.py.numBid.text()))
    self.py.target.setText("Выполнить обновление функциональности %s выполненные в рамках заявок:" \
                    "https://support.ramax.ru/issues/%s" % (self.py.nameProject.text(), self.py.specBid.text()))
    self.py.stage_1_text.setText("Дата и время публикации: с %s до %s %s \n" \
                    "Список контактов ответственных сотрудников:" % (self.py.timeIn.text(),self.py.timeOut.text(),
                                                                      self.py.dateIn.text()))
    self.py.stage_3_text.setText("Особый режим мониторинга не требуется.")
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
    formText = "1. Системный администратор выполняет резервное копирование приложения и конфигурационных файлов " \
               "на серверах %s \n" % ", ".join(i for i in listSer)
    iter = 1
    for i in range(0,len(listApp)):
        if (len(listApp) - 1) == i:
            serverPer = 0
        else:
            serverPer = i + 1
        iter += 1
        formText += "%s. Системный администратор временно перенаправляет трафик %s с сервера %s на %s \n"\
                    % (iter, self.py.nameProject.text(), listApp[i], listApp[serverPer])
        formText += bashIPPost % (listSer.get(listApp[i]), self.py.portApp.text(), listSer.get(listApp[serverPer]))
        formText += bashIPPre % (listSer.get(listApp[serverPer]), self.py.portApp.text(), listSer.get(listApp[i]))
        iter += 1
        formText += "%s. Системный администратор производит обновление кода приложения на сервере %s путем переключения" \
                    " локальной версии на ветку релиза, выполнив команду Subversion. Номер ревизии: %s \n" % \
                    (iter, listApp[i], self.py.numberRev.text())
        formText += "svn switch %s \n svn update" % (self.py.svn.text())
        iter += 1
        formText += "%s. Системный администратор перезапускает приложение на сервере %s и отключает " \
                    "перенаправление трафика \n" % (iter, listApp[i])
        formText += "/etc/init.d/prod_schedule restart; \n" \
                "while ! /usr/lib/nagios/plugins/check_tcp -H localhost -p 9780 ; do sleep 0.5 ; done; \n"
        formText += bashIPPre % (listSer.get(listApp[i]), self.py.portApp.text(), listSer.get(listApp[serverPer]))
        formText += bashIPPost % (listSer.get(listApp[serverPer]), self.py.portApp.text(), listSer.get(listApp[i]))
        iter += 1
        if self.py.cache.isChecked() == True:
            formText += "%s. Системый администртор осуществляет сброс кеша Varnish на серверах afl-kvm11 и afl-kvm12\n"\
                        % (iter)
            formText += "/usr/local/varnish/bin/varnishadm -T localhost:16080 purge.url schedule/static \n"
            iter += 1
        formText += "%s. Системный администратор выполняет сравнение предыдущей и новой версии приложения,\n" \
                    " формирует отчет, содержащий следующие сведения: \n" % (iter)
        formText += "список измененных файлов \n diff –u (за исключением каталогов logs, pid) \n" \
                    "исключить из отчета пароли \n отчет направить на следующие адреса: \n"
        iter += 1
        formText += "%s. Тестер у себя прописывает в файл hosts (%%windir%%\\System32\\drivers\\etc\\hosts) IP-адрес " \
                    "площадки сайта \n 185.69.80.8        www.aeroflot.ru \n и осуществляет тестирование по " \
                    "списку тест-кейсов из файла, выложенного в релизную заявку." % (iter)
        iter += 1
        formText += "%s. В случае обнаружения ошибок на этапе тестирования принимается решение об откате" \
                    " изменений на сервере %s." % (iter, ", ".join(c for c in listApp[0:i]))
    formText += "%s. Производится оповещение ответственных сотрудников (список сформирован на этапе 1) о " \
                "произведенной публикации." % (iter+1)
    self.py.stage_2_text.setText(formText)
