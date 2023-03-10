from django.contrib import admin

# Register your models here.
from .models import MyModel


class MyModelInAdmin(admin.ModelAdmin):
    list_display = ('my_file', 'my_image')


# Register your models here.
# here we add the table and it means we had registered it to appear in admin tab
# descond argument hi admin page of django ah khan ege lang se kan tih
admin.site.register(MyModel, MyModelInAdmin)
