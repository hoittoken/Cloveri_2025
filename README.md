<img src="https://github.com/hoittoken/Cloveri_2025/blob/a8a7865557d997f55c99dc3add4f0efa1681d88d/images/cloveri_start.png" width="300" />

# Стажировка в Cloveri 2025 год.
<a class="anchor" id=0></a>
- [Задачи](#задачи)
- [Макет сертификата](#макет-сертификата)
- [Структура базы данных](#структура-базы-данных)
- [Описание используеммых таблиц](#описание-используемых-таблиц)
- [Пример SQL запросов]()
- [Фреймворк для реализации]()
- [Костыльный пример исполнения]()


## Искомая позиция: **Python-программист**

## Тестовое задание: **Спроектировать структуру базы данных для хранения информации о сертификатах о прохождении стажировки**

Проектирование осуществляется на основе [макета сертификата.](https://cloveri.com/certificate/f7bcd817-42f9-e2ca-0226-f6e916ce6b73)

## Задачи:

1. Пришлите описание используемых таблиц, включая информацию о названиях и формате полей.
2. Предложите индексы для каждой из таблиц, которые помогут быстрее выдавать информацию о сертификате
3. Напишите SQL-запрос, который выведет все сертификаты, для которых не заданы навыки, которые есть у владельца сертификата
4. Какой фреймворк вы бы выбрали для реализации и почему?

[наверх](#стажировка-в-cloveri-2025-год)

## Макет сертификата

<img src="https://github.com/hoittoken/Cloveri_2025/blob/0c9333a94b83cedb8427aa8e0254c89ef646608e/images/cloveri_certificate.png" width="600" />

Сущности, которые можно выделить из макета сертификата:

1. Имя и фамилия стажера
2. Роль на стажировке
3. Название стажировки
4. Даты прохождения стажировки
5. Полярная диаграмма с 11-ю оценками по основным предметам стажировки
6. Навыки и инструменты

Также из условий задачи мы знаем, что у каждого сертификата есть уникальный номер, а у каждого стажера электронная почта, к которой привязан сертификат.

Прикинем какую информацию мы будем хранить в нашей базе данных:

| № | Название | Описание |  Тип данных | Уникальность | Примеры |
| - | -------- | -------- | ----------- | ------------ | ---------- |
| 1 | id       | уникальный id <br>каждого стажера | serial или text | уникально для<br> каждого сертификата | 1, 2, 'f7bc38aa' |
| 2 | email | адрес электронной <br>почты стажера | varchar(320) <br>или text | уникально для<br> каждого стажера | 'work.aubakirov@gmail.com' |
| 3 | username | Имя и фамилия стажера | varchar(100) <br>или text | уникально для<br> каждого стажера | 'Михаил Аубакиров' |
| 4 | user_role | роль на конкретной стажировке | varchar(100) <br>или text | около 10-и уникальных значений | Python-программист, <br>QA-инженер, <br>UX/UI-дизайнер |
| 5 | internship | название стажировки (проекта) | varchar(100) <br>или text | единовремено меньше 10-и, архивно десятки | 'Кабинет Кловери', <br>'MAIBO', 'Лектоник' |
| 6 | start_date | дата начала стажировки | date | уникальна для каждой стажировки | 2025-01-15 |
| 7 | end_date | дата окончания стажировки | date | уникальна для каждой стажировки | 2025-04-28 |
| 8 | grades | оценки по ключевым навыкам | numeric (2,1) <br> или real | уникальны для каждой роли (всего около 20) <br>диапазон [0.0, 10.0] | 4.2, 6.0, 3.7|
| 9 | tools | навыки и инструменты | boolean | уникальны для каждого сочетания роли и стажировки | Pycaret, Random Forest, Optuna |

[наверх](#стажировка-в-cloveri-2025-год)

## Структура базы данных

Можно представить следующую [структуру](https://dbdiagram.io/d/677eccc20231eca729926414) базы данных PostgreSQL:

<img src="https://github.com/hoittoken/Cloveri_2025/blob/06f8daa10d8a51edca245500fa1451b64d97746f/images/structure_v.1.4.png" width="800" />

## Описание используемых таблиц

### Таблица **interns**
* Храним информацию о выданных сертификатах и стажерах, 
* Primary key тут будет **id**, он же будет являться кластерным индексом, некластерным индексом будут значения **email**.


### Таблица **grades**
* Храним оценки по каждому ключевому навыку (skills), полученному каждым стажером, во время прохождения стажировки. 
* Primary key тут будет **id**, он же будет являться кластерным индексом.
* Соотносится с таблицей **interns** посредством `interns.id = grades.interns_id`
* Используется для построения полярной диаграммы скилов. 


### Таблица **tools**
* Храним инструменты освоенные стажером во время прохождения стажировки с привязкой к исполненной роли (Python-программист, QA-инженер, UX/UI-дизайнер и т.д.). 
* Primary key тут будет **id**, не кластерным индексом будет сочетание роли и названия стажировки. 

    К примеру для роли Python-программиста при разработке мобильного-приложения и Python-программиста при разработке рекомендательной системы потребуются разные навыки и инструменты (tools).

* Соотносится с таблицей **interns** посредством `interns.user_role = tolls.user_role and interns.internship = tolls.internship`

[наверх](#стажировка-в-cloveri-2025-год)

## Примеры SQL запросов

Самый простой select:
```SQL
SELECT 
    *
FROM
    cloveri.interns
```
Реализация при использовании [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/) и собственных [моделей](https://github.com/hoittoken/Cloveri_2025/blob/06f8daa10d8a51edca245500fa1451b64d97746f/models.py):

```python
with session_factory() as session:
    stmt = select(InternsOrm)
    print(f"{stmt.compile(compile_kwargs={"literal_binds": True})}\n")
    result = session.execute(stmt)
    interns = result.scalars().all()
    for model in interns:
        print(model.id, model.username, model.internship)

>>> SELECT cloveri.interns.id, cloveri.interns.email, cloveri.interns.username, cloveri.interns.user_role, cloveri.interns.internship, cloveri.interns.start_date, cloveri.interns.end_date, cloveri.interns.notes 
>>> FROM cloveri.interns

>>> f1 Miguel Aubakirov Кабинет Кловери
>>> f2 Miguel Aubakirov MAIBO
>>> f3 Nombre Apellido Кабинет Кловери
>>> f4 Jose Rodrigues MAIBO
>>> f5 Soledad Lorna Платформа для ВУЗов    
```
Результатом выполнения запроса будет список моделей экземпляров класса `InternsOrm` записанные в переменную interns.

```python
class InternsOrm(Base):
    __tablename__ = "interns"
    __table_args__ = {"schema": "cloveri"}
    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str]
    username: Mapped[str]
    user_role: Mapped[str]
    internship: Mapped[str]
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    notes: Mapped[str | None]
```

***
Простой запрос с фильтрацией, посмотрим сколько записей в таблице interns есть для пользователя с адресом электронной почты `work.aubakirov@gmail.com`

```SQL
SELECT * 
FROM cloveri.interns 
WHERE (cloveri.interns.email LIKE '%' || 'work.aubakirov@gmail.com' || '%')
```
SQLAlchemy:
```Python
intern_email = 'work.aubakirov@gmail.com'

with session_factory() as session:
    query = (
        select(InternsOrm)
        .filter(InternsOrm.email.contains(intern_email))
            )
    result = session.execute(query)
    interns = result.scalars().all()
    for model in interns:
        print(model.id, model.username, model.internship, model.user_role)

>>> f1 Miguel Aubakirov Кабинет Кловери Python-программист
>>> f2 Miguel Aubakirov MAIBO Python-программист
```

*** 

Объединим все таблицы в одну, получим их как объекты класса `InternsOrm` и для наглядности `Pandas.DataFrame`.

```SQL
SELECT i, g, t
FROM cloveri.grades AS g 
JOIN cloveri.interns AS i ON i.id = g.intern_id 
JOIN cloveri.tools AS t ON i.user_role = t.user_role 
WHERE i.internship = t.internship
```
SQLAlchemy:
```Python
i = aliased(InternsOrm, name="i")
g = aliased(GradesOrm, name="g")
t = aliased(ToolsOrm, name="t")

with session_factory() as session:
    stmt = (select(i, g, t)
            .join(i, i.id == g.intern_id)
            .join(t, i.user_role == t.user_role)
            .where(i.internship == t.internship))
    result = session.execute(stmt)
    interns = result.scalars().all()
    for model in interns:
        print(model)
    df = pd.read_sql(stmt, session.bind)
```
***
В тестовом задании просили написать SQL-запрос, который выведет все сертификаты, для которых не заданы навыки, которые есть у владельца сертификата.

Можно сделать исключение по навыкам из объединённых таблиц:

```SQL
SELECT t.pycaret, t.random_forest, t.anomaly_detection, t.gradient_boosting, t.cluster_analysis, t.k_fold, t.optuna, t.shap, t.tsfresh, t.sklearn_feature_selection, t.imblearn, t.streamlit, t.selenium, t.allure, t.nose, t.simpletest, t.docker, t.jira, t.adobe_xd, t.figma, t.mockplus, t.yandex_metrika, t.google_analytics, t.sketch, t.fontjoy, t.sqlalchemy, t.postgresql, t.git, t.django 
FROM cloveri.tools AS t JOIN cloveri.interns AS i ON i.user_role = t.user_role
EXCEPT
SELECT * FROM (SELECT t.pycaret, t.random_forest, t.anomaly_detection, t.gradient_boosting, t.cluster_analysis, t.k_fold, t.optuna, t.shap, t.tsfresh, t.sklearn_feature_selection, t.imblearn, t.streamlit, t.selenium, t.allure, t.nose, t.simpletest, t.docker, t.jira, t.adobe_xd, t.figma, t.mockplus, t.yandex_metrika, t.google_analytics, t.sketch, t.fontjoy, t.sqlalchemy, t.postgresql, t.git, t.django 
FROM cloveri.tools AS t JOIN cloveri.interns AS i ON i.user_role = t.user_role 
WHERE i.internship = t.internship AND i.id = 'f1') subq
```
Можно на стороне дата базы получить столбцы и по значениям в них провести сравнение навыков выбранного пользователя и навыков всех остальных пользователей.

```SQL
SELECT json_object_keys(to_json(json_populate_record(NULL::cloveri.tools, '{}'::JSON)))
```
Можно внутри SQLAlchemy посмотреть на функции sqlalchemy.sql.expression.except_ и sqlalchemy.sql.expression.exists, но к сожалению, тех трёх дней, что у меня было на выполнение тестового (а значит и изучения SQLAlchemy) **мне не хватило**.

Значит будем костыльно реализовать тестовое при помощи pandas 😉.

Все навыки хранятся в таблице tools, получим их:

```Python
from sqlalchemy import inspect
from orm import ToolsOrm

inst = inspect(ToolsOrm)
tools = [c_attr.key for c_attr in inst.mapper.column_attrs]
tools = tools[2:]
tools

>>> ['internship','pycaret','random_forest','anomaly_detection','gradient_boosting','cluster_analysis','k_fold','optuna','shap','tsfresh','sklearn_feature_selection','imblearn','streamlit','selenium','allure','nose','simpletest','docker','jira','adobe_xd','figma','mockplus','yandex_metrika','google_analytics','sketch','fontjoy','sqlalchemy','postgresql','git','django']
```
Пользователь Miguel Aubakirov, прошедший стажировку в Кабинете Кловери на позиции Python-программиста имеет следующие навыки:

```Python
df.loc[0][tools].dropna()
```
| internship | Кабинет кловери |
| - | - |
| pycaret |  True |
| optuna | True  |
| docker |  True |
| jira | True  |
| sqlalchemy | True  |
| postgresql | True  |
| git | True  |
| django | True  |

Пробежим по остальное таблице, сравним, и запишем индексы строк где не заполненны соответсвующие инструменты:

```Python
mike = df.loc[0][tools]
found_index = []
for i in df.index:
    if len(mike.compare(df.iloc[i][tools])) != 0:
        found_index.append(i)
df.loc[found_index]['id'].values

>>> array(['f2', 'f4', 'f5'], dtype=object)
```
Искомые сертификаты найдены (хоть и жутко костыльно).

[наверх](#стажировка-в-cloveri-2025-год)

## Фреймворк для реализации

Фреймвормком для реализации был выбран [SQLAlchemy](https://www.sqlalchemy.org/). 
Алхимия один из самых популярных фреймворков для работы с SQL в целом и используя ORM подход в частности.

SQLAlchemy:

* Безопасная. Параметры запросов экранируются, что делает атаки типа внедрение SQL-кода маловероятными (если только сам не хахочешь обратного).
* Производительная. Повышается вероятность повторного использования запроса к серверу базы данных, что может позволить ему в некоторых случаях применить повторно план выполнения запроса.
* Переносимая. SQLAlchemy, при должном подходе, позволяет писать код на Python, совместимый с несколькими back-end СУБД. Несмотря на стандартизацию языка SQL, между базами данных имеются различия в его реализации, абстрагироваться от которых и помогает SQLAlchemy.

        Сильно либимый мной Pandas при работе с SQL настоятельно рекомендует использовать SQLAlchemy, о чём, в случае не выполнения этой рекомендации будет выкидывать ошибку:
        UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
        Такой рекомендации, мне уже было достаточно :)

## Костыльный пример исполнения

Чуть нагляднее всё это великолепие можно посмотреть в ноутбуке [demostation.ipynb](https://github.com/hoittoken/Cloveri_2025/blob/06f8daa10d8a51edca245500fa1451b64d97746f/demostation.ipynb)

Получилось конечно так себе, но зато у меня теперь есть: 
* [микроскопическая база данных](https://github.com/hoittoken/Cloveri_2025/blob/7683d41a765f794e7db9057402f78f70691c4f68/images/db.png), которая не принимает более 5 одновременных соединения (причём веб-клиент на стороне [filess.io](https://filess.io) занимает сразу 4 из них - удобно).
* Какой-никакой [функционал](https://github.com/hoittoken/Cloveri_2025/blob/7683d41a765f794e7db9057402f78f70691c4f68/orm.py) для работы с ней.
* Ну и теперь не нужно будет стыдливо `warnings.filterwarnings("ignore")`, чтобы pandas не ругалась об использовании чего-то другого кроме SQLAlchemy.

[наверх](#стажировка-в-cloveri-2025-год)