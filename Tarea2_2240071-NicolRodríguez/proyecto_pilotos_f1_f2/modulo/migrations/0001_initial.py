import django.core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('categoria', models.CharField(choices=[('F1', 'Fórmula 1'), ('F2', 'Fórmula 2')], max_length=2, verbose_name='Categoría')),
                ('escuderia', models.CharField(max_length=100, verbose_name='Escudería')),
                ('edad', models.PositiveSmallIntegerField(help_text='La edad debe estar entre 16 y 70 años.', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(70)], verbose_name='Edad')),
                ('anio_debut', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2100)], verbose_name='Año de debut')),
                ('nacionalidad', models.CharField(max_length=60, verbose_name='Nacionalidad')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen', models.CharField(blank=True, help_text='Nombre del archivo de imagen dentro de static/modulo/img (ej. max-verstappen-2026.png).', max_length=120, verbose_name='Archivo de imagen')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilotos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario responsable')),
            ],
            options={'verbose_name': 'Piloto', 'verbose_name_plural': 'Pilotos', 'ordering': ['nombre']},
        ),
        migrations.AddConstraint(model_name='piloto', constraint=models.CheckConstraint(condition=models.Q(('edad__gte', 16), ('edad__lte', 70)), name='piloto_edad_16_70')),
        migrations.AddConstraint(model_name='piloto', constraint=models.CheckConstraint(condition=models.Q(('anio_debut__gte', 1950), ('anio_debut__lte', 2100)), name='piloto_debut_valido')),
    ]
