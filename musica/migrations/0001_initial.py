# Generated by Django 3.1.5 on 2021-01-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membro', '0001_initial'),
        ('banda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('letra', models.TextField(blank=True)),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banda.banda')),
                ('participacoes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membro.membro')),
            ],
            options={
                'verbose_name': 'Musica',
                'verbose_name_plural': 'Musicas',
            },
        ),
    ]
