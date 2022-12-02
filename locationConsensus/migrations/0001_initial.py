# Generated by Django 4.1.3 on 2022-12-02 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EphID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ephID', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interactionID', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='time occured')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='locationConsensus.location')),
                ('spotted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EphIDs_spotted', to='locationConsensus.ephid')),
                ('spotter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EphID_spotters', to='locationConsensus.ephid')),
            ],
        ),
    ]
