# Generated by Django 3.0.4 on 2020-03-15 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.Article'),
        ),
    ]
