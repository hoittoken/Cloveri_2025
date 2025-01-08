<img src="https://github.com/hoittoken/Cloveri_2025/blob/a8a7865557d997f55c99dc3add4f0efa1681d88d/images/cloveri_start.png" width="300" />

# Стажировка в Cloveri 2025 год.
<a class="anchor" id=0></a>
- [Задачи](#задачи)
- [Макет сертификата](#макет-сертификата)
- []



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
| 3 | name | Имя и фамилия стажера | varchar(100) <br>или text | уникально для<br> каждого стажера | 'Михаил Аубакиров' |
| 4 | role | роль на конкретной стажировке | varchar(100) <br>или text | около 10-и уникальных значений | Python-программист, <br>QA-инженер, <br>UX/UI-дизайнер |
| 5 | internship | название стажировки (проекта) | varchar(100) <br>или text | единовремено меньше 10-и, архивно десятки | 'Кабинет Кловери', <br>'MAIBO', 'Лектоник' |
| 6 | start | дата начала стажировки | date | уникальна для каждой стажировки | 2025-01-15 |
| 7 | end | дата окончания стажировки | date | уникальна для каждой стажировки | 2025-04-28 |
| 8 | grades | оценки по ключевым навыкам | numeric (2,1) <br> или real | уникальны для каждой роли (всего около 20) <br>диапазон [0.0, 10.0] | 4.2, 6.0, 3.7|
| 9 | skills | навыки и инструменты | text | уникальны для каждой роли (всего около 40) | Pycaret, Random Forest, Optuna |

[наверх](#стажировка-в-cloveri-2025-год)

## Структура базы данных

Можно представить следующую структуру базы данных 