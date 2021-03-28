from django.contrib import admin

# Register your models here.
from .models import User, UserProfile, LeadManager, LeadDoctor,FollowUp, Doctor, Category

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(LeadManager)
admin.site.register(LeadDoctor)
admin.site.register(FollowUp)
admin.site.register(Doctor)
admin.site.register(Category)