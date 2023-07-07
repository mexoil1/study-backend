from django.db import models


class Teacher(models.Model):
    """Модель преподавателя или курса."""
    name = models.CharField(max_length=250, verbose_name='ФИО или название')
    institute = models.CharField(max_length=250, verbose_name='Институт')
    image = models.ImageField(upload_to='teachers/', verbose_name='Фотография')
    contacts = models.TextField(verbose_name='Ссылка на сайте УрФУ')

    class Meta:
        ordering = ['name']
        verbose_name = 'Преподаватель или курс'
        verbose_name_plural = 'Преподаватели и курсы'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель отзыва."""
    CHOICES = (
        ('first', '1 курс'),
        ('second', '2 курс'),
        ('third', '3 курс'),
        ('fourth', '4 курс'),
    )

    course = models.CharField(
        max_length=200,
        choices=CHOICES,
        verbose_name='Курс')

    teacherOrCourse = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель или курс',
        related_name='nam')

    text = models.TextField(verbose_name='Отзыв')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на {self.teacherOrCourse.name}, за {self.pub_date}'


class Advice(models.Model):
    """Модель совета."""
    text = models.TextField(verbose_name='Совет')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'

    def __str__(self):
        return f'Совет за {self.pub_date}'
