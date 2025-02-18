# Generated by Django 5.0.1 on 2024-02-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_vehicleinformation_email_vehicleinformation_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='policyissue',
            options={},
        ),
        migrations.RemoveField(
            model_name='policyissue',
            name='PayoutDiscount',
        ),
        migrations.RemoveField(
            model_name='policyissue',
            name='net_profit',
        ),
        migrations.RemoveField(
            model_name='policyissue',
            name='payout_discount',
        ),
        migrations.RemoveField(
            model_name='policyissue',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='policyissue',
            name='profit_after_tds',
        ),
        migrations.AddField(
            model_name='policyissue',
            name='PayoutAmount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='policyissue',
            name='netProfitResult',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='policyissue',
            name='profitAfterTDSResult',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='policyissue',
            name='profitResult',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='DSA',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='HP_bank',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='Location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='Ncb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='PE_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='PS_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='Premium',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='Vehicle',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='business_type',
            field=models.CharField(choices=[('New', 'New'), ('Data', 'Data'), ('Renewal', 'Renewal'), ('Endorsement', 'Endorsement')], default='Data', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='c_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='commissionPercentage',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='e_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='insurance_portal',
            field=models.CharField(choices=[('Mintpro', 'Mintpro'), ('Agency', 'Agency'), ('Ahmedabad', 'Ahmedabad'), ('IRSS', 'IRSS'), ('Probus', 'Probus'), ('Insurance_Dekho', 'Insurance_Dekho')], default='Agency', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='insurance_type',
            field=models.CharField(choices=[('Full', 'Full'), ('TP', 'TP'), ('SOD', 'SOD'), ('Package', 'Package'), ('Health', 'Health')], default='TP', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='number',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='odNetPremium',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='p_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='payment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='payment_sos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='tdsPercentage',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policyissue',
            name='v_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='policyissue',
            name='payoutDiscount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
