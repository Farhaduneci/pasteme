# Generated by Django 4.0.6 on 2022-07-07 09:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(blank=True, choices=[('arduino', 'Arduino'), ('bash', 'Bash'), ('c', 'C'), ('cpp', 'C++'), ('csharp', 'C#'), ('css', 'CSS'), ('dart', 'Dart'), ('docker', 'DockerFile'), ('docker-compose', 'DockerCompose'), ('go', 'Go'), ('html', 'HTML'), ('java', 'Java'), ('js', 'JavaScript'), ('json', 'JSON'), ('lua', 'Lua'), ('md', 'markdown'), ('mysql', 'MySQL'), ('php', 'PHP'), ('python', 'Python'), ('rb', 'Ruby')], max_length=120, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default='Untitled', max_length=120, verbose_name='Title'),
        ),
    ]
