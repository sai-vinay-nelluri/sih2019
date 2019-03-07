from django.contrib import admin
from . import models
admin.site.site_header = "TVS Motors Administration"
admin.site.site_title = "TVS Motors Administration"
admin.site.index_title = ""
admin.site.register(models.Sale)
admin.site.register(models.ShowRoom)