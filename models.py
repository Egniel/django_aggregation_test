from django.db import models
from django.db.models import Count, Max, F


# 4. Добавить возможность вызывать вышеописанные запросы через objects,
# как стандартные методы .all(), .filter()
class CountryQuerySet(models.QuerySet):
    def with_num_cities(self):
        return self.annotate(
            num_cities=Count('cities'))

    def with_biggest_city_size(self):
        return self.annotate(
            biggest_city_size=Max('cities__area'))


class CityQuerySet(models.QuerySet):
    def with_dencity(self):
        return self.annotate(
            dencity=F('population') / F('area'))


class CityManager(models.Manager):
    def get_queryset(self):
        return CityQuerySet(self.model, using=self._db)

    def with_dencity(self):
        return self.get_queryset().with_dencity()


class CountryManager(models.Manager):
    def get_queryset(self):
        return CountryQuerySet(self.model, using=self._db)

    def with_num_cities(self):
        return self.get_queryset().with_num_cities()

    def with_biggest_city_size(self):
        return self.get_queryset().with_biggest_city_size()


class Country(models.Model):
    objects = CountryManager()
    name = models.CharField(
        'Название',
        max_length=255
    )

class City(models.Model):
    objects = CityManager()
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        related_name='cities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название',
        max_length=255
    )
    population = models.FloatField(
        'Население'
    )
    area = models.FloatField(
        'Площадь'
    )


# 1. Получить QuerySet всех стран, так чтобы у каждого элемента в QuerySet
# было значение num_cities с количеством всех городов
def get_countries_cities_count():
    return Country.objects.annotate(num_cities=Count('cities'))


# 2. Получить QuerySet всех стран, так чтобы у каждого элемента в QuerySet
# было значение biggest_city_size - самый большой показатель area из городов
# данной страны
def get_countries_biggest_city_size():
    return Country.objects.annotate(biggest_city_size=Max('cities__area'))


# 3. Получить QuerySet всех городов, так чтобы у каждого элемента в QuerySet
# было значение dencity, расcчитывается как значение population / area
def get_cities_dencity():
    return City.objects.annotate(dencity=F('population') / F('area'))