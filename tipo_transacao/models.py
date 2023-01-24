from django.db import models


class SinalOptions(models.TextChoices):
    SINAL = "+"
    DEFAULT = "-"

class NaturezaOptions(models.TextChoices):
    ENTRADA = "Entrada"
    DEFAULT = "Saída"

class TipoTransacao(models.Model):
     descricao = models.CharField(max_length=125)
     natureza = models.CharField(
     max_length=7,
        choices=NaturezaOptions.choices,
        default=NaturezaOptions.DEFAULT,
        null=True,
    )
     sinal = models.CharField(
    max_length=1,
        choices=SinalOptions.choices,
        default=SinalOptions.DEFAULT,
        null=True,
    )
     