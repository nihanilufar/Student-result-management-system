from django.contrib import admin
from .models import student,Subject,Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list display = ['name','roll_number','batch']
    search_fields = ['name','roll_number']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list display = ['name','code','max_marks']

@admin.register(result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks_obtained']
    list_filter = ['subject','student__batch']



