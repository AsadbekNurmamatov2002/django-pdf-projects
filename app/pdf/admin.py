from django.contrib import admin
from .models import Grops, Talaba, Talababaholash, Bahosi


admin.site.register(Grops)
admin.site.register(Talaba)

class TalabaInline(admin.TabularInline):
    model =Talababaholash
    raw_id_fields = ["fanlar"]
    
@admin.register(Bahosi)
class BahosiAdmin(admin.ModelAdmin):
    list_display=['fan', 'uquv_boshqarma_boshligi']
    inlines = [TalabaInline]