from django.contrib import admin
from .models import Questions,Choice,Difficulty
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra = 3

class DiffInline(admin.TabularInline):
    model=Difficulty
    extra = 1

class QuestionAdminz(admin.ModelAdmin):
    list_display = ["question", "pub_date","wasPublishedRecently"]
    list_filter =["pub_date"]
    search_fields =["question"]
    fieldsets = [ ("Date Published", {"fields":["pub_date"]}),
                ("Add Question", {"fields": ["question"]}),
                  ]
    inlines=[ChoiceInline, DiffInline]
admin.site.register(Questions,QuestionAdminz)
admin.site.register(Difficulty)

