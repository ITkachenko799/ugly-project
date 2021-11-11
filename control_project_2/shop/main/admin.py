from django.forms import ModelChoiceField,ModelForm,ValidationError
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Prod)
class ProdAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'price', 'img_prod', 'info']
    list_filter = ["category"]

    def img_prod(self,obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}">'.format(
            url=obj.img.url,
            width = '40%',
            height='40%'
        ))

    img_prod.short_description = 'Изображение товара'



