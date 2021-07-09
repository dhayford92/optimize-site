from django.contrib import admin
from .models import*


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title']
    class Meta:
        model = Project


class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ['project']

    class Meta:
        model = ProjectImage


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')

    class Meta:
        model = Contact

class TeatAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    class Meta:
        model = Team


admin.site.register(Project, ProductAdmin)
admin.site.register(ProjectImage, ImageAdmin)
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin) 
admin.site.register(Team, TeatAdmin)