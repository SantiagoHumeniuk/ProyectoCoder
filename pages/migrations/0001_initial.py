# Generated by Django 4.0.3 on 2022-05-04 03:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtitulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Texto del Blog')),
                ('image', models.ImageField(blank=True, null=True, upload_to='page_imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor del Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comentarios', to='pages.page')),
            ],
        ),
    ]