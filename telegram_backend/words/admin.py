from django.contrib import admin
from words.models import Words


class WordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'gender', 'word')
    list_editable = ('gender', 'word')


admin.site.register(Words, WordAdmin)

