# Театр «Маска» — Django (модели, миграции, CRUD, статика)

Практическая работа: модели, миграции и обработка статических/медиа файлов.

## Что реализовано

- **8 таблиц (моделей)**: Position, Worker, Genre, Performance, Role, Award, Repertoire, Ticket
- **CRUD на 5 основных** через дженерики Django:
  - Worker (с фото)
  - Performance (с фото/афишей)
  - Genre
  - Role
  - Award
- Все данные выводятся через шаблонные теги Django
- Фотографии корректно загружаются и отображаются
- Статические файлы (CSS) и медиа настроены
- После создания / редактирования / удаления — возврат на список

## Запуск

```bash
pip install django pillow
cd django_theater
python manage.py runserver
```

Откройте http://127.0.0.1:8000/

**Админка:** /admin/  
логин: `admin`  
пароль: `admin123`

## Основные маршруты

| URL | Описание |
|-----|----------|
| / | Главная |
| /workers/ | Список работников (+ CRUD) |
| /performances/ | Список спектаклей (+ CRUD) |
| /genres/ | Жанры (+ CRUD) |
| /roles/ | Роли (+ CRUD) |
| /awards/ | Награды (+ CRUD) |
| /troupe/ | Труппа (данные из БД) |
| /poster/ | Афиша (данные из БД) |
| /admin/ | Админ-панель |

## Структура

- `main/models.py` — все 8 моделей
- `main/views.py` — дженерики + старые страницы
- `main/urls.py` — маршруты
- `main/templates/` — шаблоны (workers/, performances/, genres/ и т.д.)
- `media/` — загруженные фото
- `main/static/main/css/style.css` — стили
