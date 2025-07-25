# Generated by Django 5.2 on 2025-07-03 02:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InformacionContacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=200, verbose_name="Email Empresa"),
                ),
                (
                    "telefono_empresa",
                    models.CharField(max_length=20, verbose_name="Teléfono"),
                ),
                (
                    "direccion",
                    models.CharField(max_length=40, verbose_name="Dirección"),
                ),
                (
                    "dias",
                    models.CharField(
                        choices=[
                            ("LU", "Lunes"),
                            ("MA", "Martes"),
                            ("MI", "Miércoles"),
                            ("JU", "Jueves"),
                            ("VI", "Viernes"),
                            ("SA", "Sábado"),
                            ("DO", "Domingo"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "hora_apertura",
                    models.CharField(
                        choices=[
                            (0, "f:{:00}"),
                            (1, "f:{:00}"),
                            (2, "f:{:00}"),
                            (3, "f:{:00}"),
                            (4, "f:{:00}"),
                            (5, "f:{:00}"),
                            (6, "f:{:00}"),
                            (7, "f:{:00}"),
                            (8, "f:{:00}"),
                            (9, "f:{:00}"),
                            (10, "f:{:00}"),
                            (11, "f:{:00}"),
                            (12, "f:{:00}"),
                            (13, "f:{:00}"),
                            (14, "f:{:00}"),
                            (15, "f:{:00}"),
                            (16, "f:{:00}"),
                            (17, "f:{:00}"),
                            (18, "f:{:00}"),
                            (19, "f:{:00}"),
                            (20, "f:{:00}"),
                            (21, "f:{:00}"),
                            (22, "f:{:00}"),
                            (23, "f:{:00}"),
                        ],
                        verbose_name="Horario apertura",
                    ),
                ),
                (
                    "hora_cierre",
                    models.CharField(
                        choices=[
                            (0, "f:{:00}"),
                            (1, "f:{:00}"),
                            (2, "f:{:00}"),
                            (3, "f:{:00}"),
                            (4, "f:{:00}"),
                            (5, "f:{:00}"),
                            (6, "f:{:00}"),
                            (7, "f:{:00}"),
                            (8, "f:{:00}"),
                            (9, "f:{:00}"),
                            (10, "f:{:00}"),
                            (11, "f:{:00}"),
                            (12, "f:{:00}"),
                            (13, "f:{:00}"),
                            (14, "f:{:00}"),
                            (15, "f:{:00}"),
                            (16, "f:{:00}"),
                            (17, "f:{:00}"),
                            (18, "f:{:00}"),
                            (19, "f:{:00}"),
                            (20, "f:{:00}"),
                            (21, "f:{:00}"),
                            (22, "f:{:00}"),
                            (23, "f:{:00}"),
                        ],
                        verbose_name="Hora de cierre",
                    ),
                ),
            ],
        ),
    ]
