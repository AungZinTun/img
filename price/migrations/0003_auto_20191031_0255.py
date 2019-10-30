# Generated by Django 2.2.5 on 2019-10-30 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
