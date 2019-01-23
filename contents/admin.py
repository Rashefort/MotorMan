from django.contrib import admin

from contents.models import Article



@admin.register(Article)
class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'image', 'hashtag', 'date', ('views', 'comments'), 'close']
    readonly_fields = ('views', 'comments')
