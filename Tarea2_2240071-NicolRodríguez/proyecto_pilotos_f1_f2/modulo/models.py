from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Piloto(models.Model):
    CATEGORIAS = [
        ('F1', 'Fórmula 1'),
        ('F2', 'Fórmula 2'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pilotos',
        verbose_name='Usuario responsable',
    )
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre completo',
    )
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS,
        verbose_name='Categoría',
    )
    escuderia = models.CharField(
        max_length=100,
        verbose_name='Escudería',
    )
    edad = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(70)],
        verbose_name='Edad',
        help_text='La edad debe estar entre 16 y 70 años.',
    )
    anio_debut = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2100)],
        verbose_name='Año de debut',
    )
    nacionalidad = models.CharField(
        max_length=60,
        verbose_name='Nacionalidad',
    )
    descripcion = models.TextField(
        verbose_name='Descripción',
    )
    imagen = models.CharField(
        max_length=120,
        blank=True,
        help_text=(
            'Nombre del archivo de imagen dentro de static/modulo/img '
            '(ej. max-verstappen-2026.png).'
        ),
        verbose_name='Archivo de imagen',
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(edad__gte=16, edad__lte=70),
                name='piloto_edad_16_70',
            ),
            models.CheckConstraint(
                condition=models.Q(
                    anio_debut__gte=1950,
                    anio_debut__lte=2100,
                ),
                name='piloto_debut_valido',
            ),
        ]

    def __str__(self):
        return f'{self.nombre} ({self.get_categoria_display()})'

    def get_absolute_url(self):
        return reverse('piloto_detalle', args=[self.pk])
