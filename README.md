# At your service
At your service - сервис для нахожденя исполнителей как для мелких бытовых проблем, так для крупных бизнес-задач.
## Локальный запуск
Для запуска сайта на вашем устройстве **необходимо**:
1. Клонировать Git репозиторий: *git clone git@<span></span>github.com:AlexKhaliman/Course-work.git*
2. Создать виртуальное окружение:

*virtualenv \*venv_name\*

*source \*venv_name\*/bin/activate*

*pip install -r requirements.txt*

> установленные панеты можно посмотреть в [requirements.txt](https://github.com/AlexKhaliman/Course-work/blob/master/requirements.txt)
3. Запустить файл .bash_profile: *source .bash_profile*
4. Создать БД и изменить найстроки файла course_work/setting.py
> Если ваша СУБД - PostgreSQL, то измените значения ключей
> - **USER**
> - **PASSWORD**
> - **NAME**
>
> Если же ваша СУБД - MySQL, также измените значение поля **ENGINE** на *'django.db.backends.mysql'*
## Дополнительная информация
[Диаграммы](https://github.com/AlexKhaliman/Course-work/tree/master/diagrams):
- [Entity Relationship](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/ERD%20.png)
- [Use Case](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/UCD.png)
- [Sequence](https://github.com/AlexKhaliman/Course-work/blob/master/diagrams/sequences.png)
Для обратной связи пишите на khalimantsevich174@mail.ru