# Generated by Django 5.1.4 on 2025-01-13 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kwork',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kworkfeedback',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kworkfeedback',
            name='kwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.kwork'),
        ),
        migrations.AddField(
            model_name='kworkfile',
            name='kwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.kwork'),
        ),
        migrations.AddField(
            model_name='kworkservicetype',
            name='kwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.kwork'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='common.category'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.portfolio'),
        ),
        migrations.AddField(
            model_name='portfoliofile',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.portfolio'),
        ),
        migrations.AddField(
            model_name='sellerskill',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.seller'),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.category'),
        ),
        migrations.AddField(
            model_name='portfoliofile',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.servicetype'),
        ),
        migrations.AddField(
            model_name='kworkservicetype',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.servicetype'),
        ),
        migrations.AddField(
            model_name='sellerskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.skill'),
        ),
    ]
