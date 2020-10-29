from django.contrib import admin
from .models import Batsmen_info

# Register your models here.
class Batsmen_infoAdmin(admin.ModelAdmin):
    '''
        Admin View for Batsmen_info
    '''
    list_display = ('FIRST_NAME','LAST_NAME','COUNTRY','AGE','RUNS','AVG','RANK','PLAYED','STR')
    

admin.site.register(Batsmen_info, Batsmen_infoAdmin)