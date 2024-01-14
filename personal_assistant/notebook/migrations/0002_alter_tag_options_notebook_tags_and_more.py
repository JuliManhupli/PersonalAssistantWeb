# Generated by Django 5.0.1 on 2024-01-12 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='notebook',
            name='tags',
            field=models.ManyToManyField(related_name='notebooks', through='notebook.NotebookTag', to='notebook.tag'),
        ),
        migrations.AlterField(
            model_name='notebooktag',
            name='notebook_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notebook_tags', to='notebook.notebook'),
        ),
        migrations.AlterField(
            model_name='notebooktag',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_notebooks', to='notebook.tag'),
        ),
    ]