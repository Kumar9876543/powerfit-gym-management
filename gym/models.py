from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    fee_per_month = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='trainers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_in_months = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

from datetime import timedelta
from django.utils import timezone

from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)

    join_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.join_date:
            self.join_date = timezone.now().date()

        if self.plan:
            self.expiry_date = self.join_date + timedelta(days=self.plan.duration_in_months * 30)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name