from django.contrib import admin
from polls.models import Question, Choice, Comments
from django.http import request

admin.site.site_header = "Naijaschoice Admin"
admin.site.site_title = "Naijaschoice Admin Area"
admin.site.index_title = "Welcome to Naijaschoice Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_title']}), (None, {'fields': ['question_text']}), (None, {'fields': ['slug_field']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comments)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        queryset.update(active=True)
