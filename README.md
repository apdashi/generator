# generator

Приложение по генерации документа "План публикации"

1. Установка
git clone https://github.com/apdashi/generator.git
cd ./generator
pip3 install -r requirements.txt
2. Запуск
python3.5 start.py или запустить start.sh
3. Работа с программой:
  Программа работает с БД SQLite3. При первом запуске будет автоматичски создан файл example.db с соответствующей структурой. В случае ошибки создании БД будет выведена ошибка.
  Работа с проектом:
    - добавить проект
      При нажатии появится окно, в котором нужно ввести Наименование проекта. Далее нажить ОК. если добавление проекта произошло успешно, то окно закроется, иначе появится ошибка и окно не закроется. 
    - изменить проект (Меняется только наименование)
      Выбрать проект. Нажать изменить проект. Далее как пунктом выше.
    - удалить проект 
      Выбрать проект. НАжать удалить проект. Появится сообщение об выполнение(Успешно или не успешно). В случае успешного выполнения список проектов обновится
    - сохранить проект
      При сохранении сохраняются большинство данных, так же сохраняются данные таблицы(первые 3 колонки)
    - загрузить проект
      то что сохранили теперь и загружаем.
      
  Работа с компанией:
    добавление компании происходит из окна работы с сотрудником(При нажатии на кнопку добавить сотрудника).
    Компанию можно добавить или изменить. У каждой компании есть поле приоритет. Оно служит для правильной сортировки в таблице в документе. Наивысшим приоритетом является 0, наименьшим 9.
  Работа с сотрудниками.
    - Добавить сотрудника.
      Нажимаем, в появившемся окно вводим данные и выбираем компанию(если список пуст, то сначала нужно добавить компанию). При OK сотрудник появится в таблице
    - Изменить сотрудника
      нажимаем на нужного сотрудника и изменить сотрудника. 
      Данные напрямую измененые в таблице не сохраняются.
    - удалить сотрудника.
      нажимаем на нужного сотрудника и удалить сотрудника
    - обновить таблицу. 
      Обновляем таблицу. Все чеки уберутся.
    
  Создание документа:
    - Заполняем все параметры и нажимаем save. Вводим имя файла. 
    - кнопка open не реализована, да и бессмыслена
