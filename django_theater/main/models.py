from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название должности')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Оклад')
    duties = models.TextField(verbose_name='Обязанности', blank=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Worker(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, verbose_name='Мобильный номер')
    email = models.EmailField(verbose_name='Email')
    start_date = models.DateField(verbose_name='Дата начала работы')
    children_count = models.PositiveIntegerField(default=0, verbose_name='Количество детей')
    photo = models.ImageField(upload_to='workers/', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Performance(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название спектакля')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность (мин)')
    age_limit = models.CharField(max_length=10, verbose_name='Возрастное ограничение')
    premiere_date = models.DateField(verbose_name='Дата премьеры')
    seats = models.PositiveIntegerField(verbose_name='Количество мест в зале')
    photo = models.ImageField(upload_to='performances/', verbose_name='Афиша', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'

    def __str__(self):
        return self.title


class Role(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, verbose_name='Спектакль')
    name = models.CharField(max_length=100, verbose_name='Название роли')
    description = models.TextField(verbose_name='Описание роли', blank=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return f'{self.name} ({self.performance})'


class Award(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование награды')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Работник')
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, verbose_name='Спектакль')
    year = models.PositiveIntegerField(verbose_name='Год получения', null=True, blank=True)

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

    def __str__(self):
        return self.name


class Repertoire(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, verbose_name='Спектакль')
    show_time = models.TimeField(verbose_name='Время показа')
    show_date = models.DateField(verbose_name='Дата показа')

    class Meta:
        verbose_name = 'Репертуар'
        verbose_name_plural = 'Репертуар'

    def __str__(self):
        return f'{self.performance} — {self.show_date}'


class Ticket(models.Model):
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE, verbose_name='Репертуар')
    row = models.PositiveIntegerField(verbose_name='Ряд')
    seat = models.PositiveIntegerField(verbose_name='Место')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'Ряд {self.row}, место {self.seat}'
