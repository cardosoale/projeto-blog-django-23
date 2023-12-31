# Generated by Django 4.2.8 on 2023-12-24 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_page_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': ('Page',), 'verbose_name_plural': ('Pages',)},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('excerpt', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=False, help_text='Marque para publicar a post')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Marque para exibir a capa dentro do post')),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': ('Post',),
                'verbose_name_plural': ('Posts',),
            },
        ),
    ]
