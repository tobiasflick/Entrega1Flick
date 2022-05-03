from django.db import models

class Locales(models.Model):
    cantLocales=models.IntegerField(default=0)
    nomLocales=models.CharField(max_length=100,default=0)
    class Meta:
        verbose_name="Local"
        verbose_name_plural="Locales"

class PatioComidas(models.Model):
    cantLocales=models.IntegerField(default=0)
    nomLocales=models.CharField(max_length=100, default=0)
    class Meta:
        verbose_name="Patio de Comidas"
        verbose_name_plural="Patio de Comidas"

class Cine(models.Model):
    cine="Cinemark"
    cantPelis=models.IntegerField(default=0)
    peliculas=models.CharField(max_length=100, default=0)
    class Meta:
        verbose_name="Cine"
        verbose_name_plural="Cines"

class Promos(models.Model):
    promociones=models.IntegerField(default=0)
    precios=models.BooleanField(default=0)
    fechas=models.DurationField(default=0)
    class Meta:
        verbose_name="Promo"
        verbose_name_plural="Promos"

class Usuarios(models.Model):
    usuario=models.CharField(max_length=100)
    edad=models.IntegerField(default=0)
    email=models.EmailField()
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    

    


