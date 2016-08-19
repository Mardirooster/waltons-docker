#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Choice, Poll, Student, Teacher, Lesson


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)
    search_fields = ['question']

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vitals', {
            'classes': ('collapse',),
            'fields': ('first', 'middle', 'last', 'preferred_name', 
                                'date_of_birth','gender', 'living_with', )
        }),
        ('Registration', {
            'classes': ('collapse',),
            'fields': ( 
                ('registration_signed_paid_on','registration_signed_paid',),
                'payment_plan',
                'registration_complete',
            )
        }),
        ('Status', {
            'classes': ('collapse',),
            'fields': (
                'currently_student', 'enrolled_for_upcoming_year', 'alumni', 
            )

        }),

    )


    list_display = ('__unicode__', 'date_of_birth', 'gender', )
    search_fields = ['last', 'first', 'middle', 'preferred_name',  ]
    list_filter = ['currently_student', 'enrolled_for_upcoming_year','gender', 'living_with', 
    ##registration
        'registration_signed_paid', 'registration_complete',
    ##enrollment
        'enrolled_for_upcoming_year','payment_plan',]
    #inlines = [EnrollmentInline, DisciplinaryActionInline, VoucherInline]



class TeacherAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vitals', {
            'classes': ('collapse',),
            'fields': ('first', 'middle', 'last', 'preferred_name', 
                                'date_of_birth','gender', )
        }),
    )



    list_display = ('__unicode__', 'date_of_birth', 'gender', )
    search_fields = ['last', 'first', 'middle', 'preferred_name',  ]

class LessonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vitals', {
            'fields': ('lessonname', 'description', 'course_student', 'course_teacher', )
        }),
    )



    list_display = ('lessonname', 'description', 'course_student', 'course_teacher', )
    search_fields = ['lessonname',]


admin.site.register(Lesson, LessonAdmin)

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
