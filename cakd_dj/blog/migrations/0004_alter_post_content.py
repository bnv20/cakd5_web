# Generated by Django 4.0.4 on 2022-05-30 02:07

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
