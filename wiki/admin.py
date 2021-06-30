from django.contrib import admin
from django.db import models
from .models import Article


from search_admin_autocomplete.admin import SearchAutoCompleteAdmin


# @admin.register(Article)
class ArticleAdmin(SearchAutoCompleteAdmin):
    search_fields = ['title']
    fields = ['title', 'url', 'image']

admin.site.register(Article, ArticleAdmin)
