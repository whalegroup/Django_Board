from django.contrib import admin
from sample.models import Order


# Order TableName
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'field_name1', 'field_name2','field_name3','field_name4','field_name5','field_name6'
    )

#TableName,TableNameAdmin
admin.site.register(Order,OrderAdmin)