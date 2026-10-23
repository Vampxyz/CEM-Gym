from django.db import models


# Create your models here.
class Modality(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Nome da modalidade"
    )
    description = models.TextField(blank=True, verbose_name="Descrição da modalidade")
    active = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Modalidade"
        verbose_name_plural = "Modalidades"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Class(models.Model):
    daysOfWeek = [
        (1, "Segunda-feira"),
        (2, "Terça-feira"),
        (3, "Quarta-feira"),
        (4, "Quinta-feira"),
        (5, "Sexta-feira"),
        (6, "Sábado"),
    ]

    modality = models.ForeignKey(
        Modality,
        on_delete=models.PROTECT,
        related_name="classes",
        verbose_name="Modalidade",
    )

    dayOfWeek = models.IntegerField(choices=daysOfWeek, verbose_name="Dia da semana")

    hour = models.TimeField(verbose_name="Horário")

    instructor = models.CharField(max_length=100, verbose_name="Instrutor")
    vacancy = models.PositiveIntegerField(default=10, verbose_name="Vagas")

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ["dayOfWeek", "hour"]

    def __str__(self):
        dayName = self.get_dayOfWeek_display()
        formattedHour = self.hour.strftime("%H:%M")
        return f"{self.modality.name} - {dayName} {formattedHour}"
