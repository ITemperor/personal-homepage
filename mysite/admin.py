from django.contrib import admin
from .models import Image,Text

class ImageInfoAdmin(admin.ModelAdmin):
	list_display=('id',)

class TextInfoAdmin(admin.ModelAdmin):
	list_display=('id',)
admin.site.register(Image,ImageInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
