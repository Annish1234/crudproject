from atexit import register
from django.contrib import admin
from enroll.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','name','email','password')



    # username = annishjk
    # password = password
