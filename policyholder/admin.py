from django.contrib import admin
from .models import PolicyModel, PolicyRecordModel, QuestionModel, CategoryModel

# Register your models here.


admin.site.register(PolicyModel)
admin.site.register(PolicyRecordModel)
admin.site.register(CategoryModel)
admin.site.register(QuestionModel)
