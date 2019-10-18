# At your service 

At your service - сервис, на котором можно найти исполнителей как для мелких бытовых проблем, так и для крупных бизнес-задач.

## Локальный запуск

Для запуска сайта на своем устройстве **требуется**:
1. Клонировать git репозиторий: *git clone git@<span></span>github.com:AlexKhaliman/Course-work.git* 
2. Запустить виртуальное окружение: *source projectenv/bin/activate*
> установленные пакеты можно посмотреть [здесь](https://github.com/AlexKhaliman/Course-work/blob/master/requirements.txt)
3. Запустить файл .bash_profile для объектов мэппинга: *source .bash_profile*
4. Создайте собственную БД и поменяйте в файле course_work/settings.py настройки баз данных.
>  Если у вас СУБД - postgreSQL, поменять значение следующих ключей:
> - **USER**
> - **PASSWROD**
> - **NAME**
>
> Если же ваша СУБД - MySQL, также поменяйте значение ключа **ENGINE** на *'django.db.backends.mysql*'

## Дополнительная информация

[Диаграммы:](https://github.com/AlexKhaliman/Course-work/tree/master/diagrams)
- [Вариантов использования](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/UCD.png)
- [Последовательностей](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/sequence.png)
- [ER](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/ERD.png)

Для обратной связи пишите на khalimantsevich174@mail.ru
