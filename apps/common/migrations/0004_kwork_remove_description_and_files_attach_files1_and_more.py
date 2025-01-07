# Generated by Django 5.1.4 on 2025-01-07 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_frequently_asked_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='description_and_files',
            name='attach_files1',
        ),
        migrations.RemoveField(
            model_name='description_and_files',
            name='attach_files2',
        ),
        migrations.RemoveField(
            model_name='basic_information',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category_select',
            name='add_type_of_services',
        ),
        migrations.RemoveField(
            model_name='onecategory',
            name='select_category',
        ),
        migrations.RemoveField(
            model_name='prices_and_services',
            name='extra_options',
        ),
        migrations.DeleteModel(
            name='Frequently_Asked_Questions',
        ),
        migrations.DeleteModel(
            name='Attach_files',
        ),
        migrations.DeleteModel(
            name='Description_and_files',
        ),
        migrations.DeleteModel(
            name='Basic_information',
        ),
        migrations.DeleteModel(
            name='TypeOfService',
        ),
        migrations.DeleteModel(
            name='Category_select',
        ),
        migrations.DeleteModel(
            name='OneCategory',
        ),
        migrations.DeleteModel(
            name='Extra_options',
        ),
        migrations.DeleteModel(
            name='Prices_and_Services',
        ),
    ]
