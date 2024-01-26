# Generated by Django 4.1.3 on 2024-01-25 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyapi', '0007_remove_topic_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studybuddyapi.user'),
        ),
    ]