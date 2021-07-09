from django.contrib import admin
from .models import*

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_on')
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)