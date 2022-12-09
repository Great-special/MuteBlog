from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(BlogModel)
admin.site.register(BlogComment)
admin.site.register(CommentReply)
admin.site.register(Profile)