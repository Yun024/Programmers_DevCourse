from django.contrib import admin
from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 어떤 필드를 어드민에서 사용할지
    fieldsets = [
        ('질문섹션', {'fields': ['question_text']}),
        ('생성일',{'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    list_display = ('question_text','pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text','choice__choice_text']

# 만들어진 다음에 등록이 되어야 하기때문에 아래로 이동 
admin.site.register(Question, QuestionAdmin)

