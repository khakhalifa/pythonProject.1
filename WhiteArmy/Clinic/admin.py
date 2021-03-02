from django.contrib import admin


from .models import Date_of_examination, Id, Present_complaint, Past_history, Advise, Management

# Register your models here.
admin.site.register(Date_of_examination)
admin.site.register(Id)
admin.site.register(Present_complaint)
admin.site.register(Past_history)
admin.site.register(Advise)
admin.site.register(Management)