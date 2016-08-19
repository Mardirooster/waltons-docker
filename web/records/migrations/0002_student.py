# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('last', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=30)),
                ('middle', models.CharField(max_length=30, blank=True)),
                ('preferred_name', models.CharField(max_length=30)),
                ('present_grade', models.CharField(max_length=3, choices=[('k4', 'K4'), ('k5', 'K5'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')])),
                ('next_grade', models.CharField(max_length=3, choices=[('k4', 'K4'), ('k5', 'K5'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')])),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])),
                ('living_with', models.CharField(max_length=1, choices=[('b', 'Both Parents'), ('m', 'Mother'), ('f', 'Father'), ('o', 'Other')])),
                ('changes_affect', models.TextField(blank=True)),
                ('allergies', models.BooleanField()),
                ('allergy_description', models.TextField(blank=True)),
                ('application_form_completed_on', models.DateField(blank=True, null=True)),
                ('application_form_complete', models.BooleanField()),
                ('application_payment_completed_on', models.DateField(blank=True, null=True)),
                ('application_payment_complete', models.BooleanField()),
                ('entrance_testing_scheduled_for', models.DateField(blank=True, null=True)),
                ('entrance_testing_complete', models.BooleanField()),
                ('parent_interview_scheduled_for', models.DateField(blank=True, null=True)),
                ('parent_interview_complete', models.BooleanField()),
                ('student_interview_scheduled_for', models.DateField(blank=True, null=True)),
                ('student_interview_complete', models.BooleanField()),
                ('decision_made', models.DateField(blank=True, null=True)),
                ('student_accepted', models.BooleanField()),
                ('registration_signed_paid', models.BooleanField()),
                ('registration_signed_paid_on', models.DateField(blank=True, null=True)),
                ('complete_documents', models.BooleanField()),
                ('complete_documents_on', models.DateField(blank=True, null=True)),
                ('custody_decision_received', models.BooleanField()),
                ('custody_decision_received_on', models.DateField(blank=True, null=True)),
                ('birth_certificate_received', models.BooleanField()),
                ('birth_certificate_received_on', models.DateField(blank=True, null=True)),
                ('immunization_record_received', models.BooleanField()),
                ('immunization_record_received_on', models.DateField(blank=True, null=True)),
                ('emergency_medical_card_received', models.BooleanField()),
                ('emergency_medical_card_received_on', models.DateField(blank=True, null=True)),
                ('payment_plan', models.CharField(max_length=1, blank=True, choices=[('1', 'This plan'), ('2', 'That plan')])),
                ('registration_complete', models.BooleanField()),
                ('currently_student', models.BooleanField()),
                ('enrolled_for_upcoming_year', models.BooleanField()),
                ('alumni', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'students',
            },
        ),
    ]
