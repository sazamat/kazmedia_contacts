from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=120, unique=True, verbose_name='Департаменты')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Division(models.Model):
    division = models.CharField(max_length=120, unique=True, verbose_name='Отделы')
    department = models.ForeignKey('Department', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.division

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Phone(models.Model):
    phone = models.IntegerField(unique=True, verbose_name='Телефон')

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Employee(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    department = models.ForeignKey('Department', verbose_name='Департамент', blank=True, on_delete=models.SET_NULL,
                                   null=True)
    division = models.ForeignKey('Division', blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Отдел')
    position = models.CharField(max_length=120, verbose_name='Позиция')
    is_published = models.BooleanField(blank=True, default=True, verbose_name='Публикация')
    cell = models.CharField(max_length=120, blank=True, verbose_name='Сотовый телефон')
    phone = models.ForeignKey('Phone', blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name', 'cell']
