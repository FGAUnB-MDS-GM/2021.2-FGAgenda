# Generated by Django 3.2.6 on 2022-03-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=50, null=True, verbose_name='Tarefa')),
            ],
            options={
                'verbose_name': 'Lista de Tarefa',
                'verbose_name_plural': 'Lista de Tarefas',
            },
        ),
    ]
