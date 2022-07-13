from django.contrib import admin
from .models import Number, Rating, RatingStar, NumberView

admin.site.register(Number)
admin.site.register(NumberView)
admin.site.register(Rating)
admin.site.register(RatingStar)
