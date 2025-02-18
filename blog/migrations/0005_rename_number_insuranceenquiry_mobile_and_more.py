# Generated by Django 5.0.1 on 2024-01-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insuranceenquiry',
            old_name='number',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='vehicleinformation',
            name='insurance_enquiry',
        ),
        migrations.AddField(
            model_name='vehicleinformation',
            name='mobile',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
