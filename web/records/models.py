#-*- coding: utf-8 -*-
from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text





gender_choices = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
)


class Instrument(models.Model):
    name = models.CharField(max_length=50)


class Teacher(models.Model):
    last = models.CharField(max_length=50)
    first = models.CharField(max_length=30)
    middle = models.CharField(max_length=30, blank=True)
    preferred_name = models.CharField(max_length=30)

    date_of_birth = models.DateField()

    gender = models.CharField(max_length=1, choices=gender_choices)

    def lessons(self):
        return self.lesson_set.all()

    def __unicode__(self):
        name = self.preferred_name + ' ' + self.last
        return name

    def name(self):
        return self.preferred_name + ' ' + self.last

    class Meta:
        verbose_name_plural = "teachers"

# Create your models here.
class Student(models.Model):
#    user = models.ForeignKey('UserProfile')
    last = models.CharField(max_length=50)
    first = models.CharField(max_length=30)
    middle = models.CharField(max_length=30, blank=True)
    preferred_name = models.CharField(max_length=30)


    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    living_with_choices = (
        ('b', 'Both Parents'),
        ('m', 'Mother'),
        ('f', 'Father'),
        ('o', 'Other'),
    )
    living_with = models.CharField(max_length=1, choices=living_with_choices)

    # Registration Process
    registration_signed_paid = models.BooleanField()
    registration_signed_paid_on = models.DateField(blank=True,null=True)



    plan = (
        ('1','This plan'),
        ('2', 'That plan'),
    )
    payment_plan =  models.CharField(max_length=1, choices=plan, blank=True)
    registration_complete = models.BooleanField()

    # General status
    currently_student = models.BooleanField()
    enrolled_for_upcoming_year = models.BooleanField()
    alumni = models.BooleanField()

    def age_in_years(self):
        return str((datetime.date.today()-self.date_of_birth).days/365)

    def __unicode__(self):
        name = self.preferred_name + ' ' + self.last
        return name

    def name(self):
        return self.preferred_name + ' ' + self.last

    class Meta:
        verbose_name_plural = "students"


class Lesson(models.Model):
    lessonname = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    #instrument = models.ForeignKey(Instrument)

    course_student = models.ForeignKey(Student) #objects.all())
    course_teacher = models.ForeignKey(Teacher) #objects.all())

    def name(self):
        return self.lessonname

    class Meta:
        verbose_name_plural = "courses"

class GroupCourse(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    course_students = models.ManyToManyField(Student)
    course_teacher = models.ForeignKey(Teacher)

    def name(self):
        return self.name

    class Meta:
        verbose_name_plural = "group courses"