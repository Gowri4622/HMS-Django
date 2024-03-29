# Generated by Django 5.0.1 on 2024-01-17 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master_app", "0009_alter_room_room_number_alter_room_student"),
        ("transaction_app", "0007_remove_outpassrequest_student_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outpassrequest",
            name="warden",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="master_app.warden",
            ),
        ),
    ]
