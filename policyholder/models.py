from django.db import models
from insured.models import InsurerModel

# Create your models here.


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name}"


class PolicyModel(models.Model):
    SELECTED_CHOICES = [
        ("Not Selected", "Not Selected"),
        ("Selected", "Selected"),
    ]

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255)
    permium = models.IntegerField()
    ternure = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    is_selected = models.CharField(
        choices=SELECTED_CHOICES, max_length=255, default='Not Selected')

    def __str__(self):
        return f"{self.policy_name}"


class PolicyRecordModel(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("Aproved", "Aproved"),
        ("Denied", "Denied"),
    ]

    insurer = models.ForeignKey(InsurerModel, on_delete=models.CASCADE)
    policy = models.ForeignKey(PolicyModel, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=255, default='Pending')


class QuestionModel(models.Model):
    insurer = models.ForeignKey(
        InsurerModel, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
