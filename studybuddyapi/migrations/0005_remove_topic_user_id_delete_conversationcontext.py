# Generated by Django 4.1.3 on 2024-01-25 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyapi', '0004_rename_country_of_origin_user_name_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='ConversationContext',
        ),
    ]