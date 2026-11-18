# Театр «Маска» — Django маршрутизация

Практическая работа по МДК 02.02 «Инструментальные средства разработки программного обеспечения».

## Запуск

1. Создайте виртуальное окружение и установите Django:
   ```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install django
   ```

2. Перейдите в папку проекта и запустите:
   ```
   python manage.py runserver
   ```

3. Откройте http://127.0.0.1:8000/

## Структура маршрутов (в main/urls.py)

- `/` — Главная (name='home')
- `/about/` — О театре (name='about')
- `/contacts/` — Контакты (name='contacts')
- `/how-to-find/` — Как нас найти (name='how_to_find')
- `/poster/` — Афиша (name='poster')
- `/troupe/` — Труппа (name='troupe')

Все ссылки используют именованные маршруты {% url 'name' %}.
