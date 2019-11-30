from django.contrib import admin
from .models import BlogPost
from tinymce.widgets import TinyMCE
from django.db import models

class BlogPostAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title/Date', {'fields': ['post_title','post_date']}),
        ('Content', {'fields': ['post_content']})

     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
