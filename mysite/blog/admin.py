from django.contrib import admin
from blog.models import Post, Comment

###########################
####   Admin Details   ####
###########################
'''
username : Ayush
email : ayushk39@gmail.com
password : Ayu!@12345
'''

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)