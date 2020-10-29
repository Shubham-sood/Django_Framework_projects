from django.contrib import admin
from .models import AccDetails

# Register your models here.
class AccDetailsAdmin(admin.ModelAdmin):
    '''
        Admin View for AccDetails
    '''
    list_display = ('FIRST_NAME','LAST_NAME','DOB','ADDRESS','ACCTYPE','PAN_NO')
   

admin.site.register(AccDetails, AccDetailsAdmin)
