from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','own','get_tags','category','timestamp','read_num')
    list_filter = ('own','tags','category','published')
    date_hierarchy = 'timestamp'

admin.site.register(Tag)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)