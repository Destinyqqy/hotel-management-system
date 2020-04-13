from django.contrib import admin

from .models import customer
from .models import room
from .models import past_customer
from .models import preferred_food
from .models import dishclass
from .models import dish

class customerAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','birthday','is_checked','agree_record','room_id')
class roomAdmin(admin.ModelAdmin):
    list_display = ('room_id','room_type','room_floor','room_deposit','room_is_booked')
class past_customerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'birthday')
class prefered_foodAdmin(admin.ModelAdmin):
    pass
class dishclassAdmin(admin.ModelAdmin):
    list_display = ('classname','dishclassno')
class dishAdmin(admin.ModelAdmin):
    list_display = ('name','dishclassno')

admin.site.register(room,roomAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(past_customer,past_customerAdmin)
admin.site.register(preferred_food,prefered_foodAdmin)
admin.site.register(dishclass,dishclassAdmin)
admin.site.register(dish,dishAdmin)
