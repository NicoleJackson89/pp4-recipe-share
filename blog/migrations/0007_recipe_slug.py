# Generated by Django 4.2.11 on 2024-04-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_instruction_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
