from django.contrib import admin
from .models import Feedback
# Register your models here.
from .models import Category,Sub_category,Product,Contact_us,Order,Brand

admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Contact_us)
admin.site.register(Order)
admin.site.register(Brand)





admin.site.register(Feedback)
# Admin customization notes
# Use list_display to show more fields in admin list view
# Use search_fields to enable search in admin
