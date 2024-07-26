# Generated by Django 4.1.6 on 2023-04-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_accenture_amazon_atos_capgemini_coginzant_delloite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cisco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infosys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PWC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wipro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(null=True)),
                ('input_format', models.TextField(null=True)),
                ('output_format', models.TextField(null=True)),
                ('correct_ans', models.TextField(null=True)),
            ],
        ),
    ]
