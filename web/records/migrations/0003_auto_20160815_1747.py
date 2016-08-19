# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='GroupCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'group courses',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('last', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=30)),
                ('middle', models.CharField(max_length=30, blank=True)),
                ('preferred_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'teachers',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='student',
            name='allergy_description',
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_form_complete',
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_form_completed_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_payment_complete',
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_payment_completed_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_certificate_received',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_certificate_received_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='changes_affect',
        ),
        migrations.RemoveField(
            model_name='student',
            name='complete_documents',
        ),
        migrations.RemoveField(
            model_name='student',
            name='complete_documents_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='custody_decision_received',
        ),
        migrations.RemoveField(
            model_name='student',
            name='custody_decision_received_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='decision_made',
        ),
        migrations.RemoveField(
            model_name='student',
            name='emergency_medical_card_received',
        ),
        migrations.RemoveField(
            model_name='student',
            name='emergency_medical_card_received_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='entrance_testing_complete',
        ),
        migrations.RemoveField(
            model_name='student',
            name='entrance_testing_scheduled_for',
        ),
        migrations.RemoveField(
            model_name='student',
            name='immunization_record_received',
        ),
        migrations.RemoveField(
            model_name='student',
            name='immunization_record_received_on',
        ),
        migrations.RemoveField(
            model_name='student',
            name='next_grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_interview_complete',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_interview_scheduled_for',
        ),
        migrations.RemoveField(
            model_name='student',
            name='present_grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_accepted',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_interview_complete',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_interview_scheduled_for',
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='course_students',
            field=models.ManyToManyField(to='records.Student'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='course_teacher',
            field=models.ForeignKey(to='records.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_student',
            field=models.ForeignKey(to='records.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(to='records.Teacher'),
        ),
    ]
