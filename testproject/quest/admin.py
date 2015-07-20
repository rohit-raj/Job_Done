from django.contrib import admin

from .models import Category, Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)

# Register your models here.
