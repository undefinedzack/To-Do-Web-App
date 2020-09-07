from django.contrib import admin
from .models import Text

class TextAdmin(admin.ModelAdmin):
    fields = ['text', 'description']

# Register your models here.

admin.site.register(Text)