from django.contrib import admin

# Register your models here.
from core.models import newsletter, contact, food, order, category

admin.site.register(newsletter)
admin.site.register(contact)
admin.site.register(food)
admin.site.register(order)
admin.site.register(category)
